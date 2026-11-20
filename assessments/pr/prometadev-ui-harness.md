---
harness_id: prometadev-ui-harness
project_name: UI Harness
repository: https://github.com/ProMetaDev/ui-harness
review_ref: a20efcec26292af8457cb372b4f657f53574eda2
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# UI Harness

## Review boundary

- System in focus: One UI Harness workspace and its first-party run, workflow and team CLI, with local state and operator interfaces.
- Purpose and identity: Run model-directed work with inspectable effects and recoverable execution records.
- Relevant environment: The workspace, owner, model process, optionally installed operator verifier, and external MCP and plugin processes.
- Standard-distribution boundary: First-party Rust core and CLI/web surfaces, journal, effect observation, team orchestration and isolated-apply transaction.
- Credited operating / distribution surfaces: [Model/tool loop](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/agent.rs) · [Run/team/apply surface](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/main.rs) · [Workflow definitions](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/workflow.rs) · [Isolation](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/isolate.rs)
- Adjacent first-party surfaces excluded from ownership: Release CI, explanatory proof kit, static visual prototypes, external MCP server internals and test fixtures as decision actors.
- First-party operating / deployment modes considered: Individual model-backed runs, team execution with isolated agents and operator-managed apply, and configured team acceptance.
- Recursion level: One workspace and its current team workflow. Individual turns and isolated branches are nested operational units.
- Reviewed revision: a20efcec26292af8457cb372b4f657f53574eda2
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The core compiles a snapshot, invokes the model, dispatches approved tools and journals decision/effect events. It observes actual workspace changes separately from declared tool effects. Team mode creates a plan, runs parallel child agents on isolated workspace copies, and offers separate guarded application of their outputs. The CLI exposes replay, evidence-checking and crash reconciliation.

## Operational model

An S1 unit is a model-controlled run or separately executing worker. The runtime guards tool effects and records evidence. A team produces candidate workspace changes, and the operator can determine which completed updates become part of the shared workspace. An optional independent acceptance command supplies a separate end-of-team check.

## S1 — Operations

- State: A
- Function: Perform goal-directed tool work and return results under the workspace rules.
- Disturbance / variety regulated: Changing inputs, failed calls and workspace effects require task-local decisions.
- Decisive decision or feedback right: Choose tools, interpret results and decide a subsequent action or final response.
- Decision owner: Individual run or delegated worker model.
- Supporting / enforcement mechanisms: Model adapter, effect checks, budgets, tool dispatch, snapshots and journal.
- Closure path: Completed tool results and recorded decisions feed subsequent model steps.
- Why this is / is not agent-owned: The session or worker model selects task actions through the shipped callable loop.
- Boundary reachability: The run/workflow commands construct Agent and invoke run_turn; the isolated child execution calls the same goal path with its own workspace.
- Evidence: [Turn loop](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/agent.rs) · [CLI and worker execution](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/main.rs) · [Model adapters](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/model.rs)
- Basis: structural
- Confidence: high
- Caveats: No model endpoint or provider run was exercised.

## S2 — Coordination

- State: C
- Function: Reduce conflicting changes produced by parallel workers before they reach the shared workspace.
- Disturbance / variety regulated: Two independently running child agents can produce different edits to the same relative path.
- Decisive decision or feedback right: Reconcile the competing artifacts and choose the applicable work products.
- Decision owner: The first-party gate reports conflicts deterministically; reconciliation is presently external to a supplied autonomous coordinator.
- Supporting / enforcement mechanisms: Isolated working copies, per-path provenance, content comparison, parent drift check and exit status.
- Closure path: The conflict report identifies paths and child sources and excludes disputed writes. The next apply can consume a resolved selection.
- Why this is / is not agent-owned: The built-in code implements a concrete sibling-conflict and feedback path. An autonomous authority to reconcile and resubmit the competing outputs still requires composition.
- Boundary reachability: The standard team path defaults to isolated copies and the CLI exposes a review and guarded apply path for the resulting child artifacts.
- Distinct S1 units: Parallel child model sessions with individual workspaces and journals.
- Inter-S1 disturbance: Divergent changes by two children to the same destination path can overwrite each other on reintegration.
- Attenuating coordination relation: Per-path conflict detection skips incompatible proposals and names contributing child sessions; identical content can proceed subject to drift checks.
- Feedback into subsequent S1 behaviour: The review output exposes the conflicted paths for reconciliation and a subsequent restricted or amended apply.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The interaction is concrete competing writes on the same shared destination, with conflict-sensitive treatment before parent work uses them.
- Evidence: [Team source](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/main.rs) · [Parallel workflow spec](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/workflow.rs) · [Isolation manifests](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/isolate.rs) · [Operating mode](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/docs/13-team.md)
- Basis: structural
- Confidence: medium
- Caveats: No autonomy for selecting between competing outputs is inferred from the deterministic gate. The witness is specific to isolated child integration.

## S3 — Inside-and-now control

- State: P
- Function: Decide which outputs of the current team workflow should enter the shared workspace.
- Disturbance / variety regulated: The current child portfolio can complete unevenly, conflict, or become stale against the parent workspace.
- Decisive decision or feedback right: Commit or hold each currently available child output, after reviewing the team results and affected files.
- Decision owner: Workspace operator in the default inspect-then-apply path.
- Supporting / enforcement mechanisms: Team-wide output inventory, selective apply, conflict and drift enforcement, transactional return and rollback.
- Closure path: The selected outputs are applied to the shared workspace after explicit action. Holding or rolling them back changes the state exposed to the next turns.
- Why this is / is not agent-owned: The default operator mode retains integration choice after the team finishes. The opt-in apply-all mode is deterministic under a prior choice.
- Boundary reachability: The default team command reports all affected child outputs and directs an operator to first-party selective apply; the same workspace receives the committed state.
- Whole-system current view: All child execution outputs for the current team, changed paths, completion receipts and merge/drift status at its declared workflow recursion.
- Current-control decision scope: Select which completed work enters the live parent workspace or roll back a shared-work commit while preserving outstanding work evidence.
- Evidence: [Team reporting and apply](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/main.rs) · [Team operating instructions](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/docs/13-team.md) · [Isolated outcome explanation](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/docs/28-isolate-copy.md)
- Basis: structural
- Confidence: medium
- Caveats: Claim concerns current team integration, with no installation-wide autonomous supervisor credited.

## S3* — Complementary audit

- State: C
- Function: Independently challenge a completed-team claim against the actual workspace artifact before returning overall success.
- Disturbance / variety regulated: Ordinary child reports can overstate completion or omit a failed acceptance condition.
- Decisive decision or feedback right: Establish whether delivered artifacts pass the owner-selected acceptance checks independently of model prose.
- Decision owner: A separately supplied acceptance command owns the proof predicate. The runtime owns exit-code enforcement and the summarizer receives the outcome.
- Supporting / enforcement mechanisms: Separate owner-configured command, direct workspace access, team acceptance journal, hard failure exit and a final model check against actual artifacts.
- Closure path: A failing predicate is reported to the summarizer and forces an unsuccessful overall outcome despite a model's claim. Corrective work returns through the operator or subsequent run.
- Why this is / is not agent-owned: The distribution exposes a dedicated evidence and return path. The operator must compose the task-specific verifier and its independent trust boundary.
- Boundary reachability: The shipped team command runs the configured acceptance command after workflow/apply and before its final evidence-informed report.
- Claim being audited: A completed team result actually satisfies its task acceptance conditions.
- Ordinary reporting path: The worker runs return workflow status, journals and descriptions of their proposed changes.
- Complementary access path: A separately configured acceptance process inspects committed workspace evidence, with its exit status recorded independently of the model reply.
- Independence boundary: The checking process and criteria are supplied from the operator boundary. Independence is limited to a correctly composed verifier.
- Who acts on findings: Team runtime enforces failure at exit and provides the finding to the separate final reporting agent and operator.
- Evidence: [Team acceptance and exit](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/main.rs) · [Ordinary worker loop](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/agent.rs) · [Independent observations](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/observe.rs) · [Team process](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/docs/13-team.md)
- Basis: structural
- Confidence: medium
- Caveats: Journal replay and hash verification help reconstruction. They alone establish neither an independent task verdict nor automatic rework.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense external change and carry a future adaptation decision into the workspace's supported capability.
- Disturbance / variety regulated: Provider availability, plugin options or tool changes could affect future work.
- Decisive decision or feedback right: No first-party supported loop was identified that interprets such external changes and returns an adaptation decision.
- Decision owner: The operator supplies model, plugin and environment choices. Models operate within the chosen context.
- Supporting / enforcement mechanisms: Provider registry/config, plugin attachment, knowledge and memory checks.
- Closure path: Configured capabilities affect later runs. Runtime observations inform present execution and audit.
- Why this is / is not agent-owned: Configuration and recall do not themselves implement external prospective adaptation.
- Evidence: [Configured providers](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/providers.rs) · [Plugins](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/plugin.rs) · [Knowledge](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/knowledge.rs) · [CLI boundaries](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/main.rs)
- Basis: structural
- Confidence: medium
- Caveats: The reviewed source allows an operator to reconfigure future runs outside a supplied sensing-to-adoption loop.

### Absence scope

- Surfaces inspected: Provider registry and CLI, knowledge/memory paths, plugin loading and optional lab evidence.
- Plausible first-party paths checked: Live external capability comparisons, installed options and durable return into future execution after a decision.
- Why no material first-party path remains: The supplied provider listing reads configured choices, and evidence/knowledge tools validate records. No explicit external-change adaptation path with returned discretion was established.

## S5 — Policy and identity

- State: —
- Function: Determine lasting identity or ultimate policy for the installation and its team operation.
- Disturbance / variety regulated: Tool effects and crash recovery can pose trust or intervention questions.
- Decisive decision or feedback right: No separate ultimate-policy decision and return path was established.
- Decision owner: Code and invocation configuration set policy behavior; an operator can control approvals for current work.
- Supporting / enforcement mechanisms: Mode selection, access checks, protected paths, session approvals and historical policy replay.
- Closure path: Selected enforcement is applied to effects. Crash replay asks the operator for uncertain individual effects.
- Why this is / is not agent-owned: The reviewed authority governs execution and local exceptions within the configured workspace.
- Evidence: [Policy engine](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/policy.rs) · [Run modes](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/mode.rs) · [Approval and reconciliation](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-core/src/agent.rs) · [CLI history audit](https://github.com/ProMetaDev/ui-harness/blob/a20efcec26292af8457cb372b4f657f53574eda2/ui-cli/src/main.rs)
- Basis: structural
- Confidence: medium
- Caveats: Historical replay under an alternate mode can explain a decision without instituting a lasting governing mandate.

### Absence scope

- Surfaces inspected: Mode and effect policy, tool approvals, protected handling, team operator path and historical audit.
- Plausible first-party paths checked: Owner-governed persistent change to ultimate authority, autonomous policy revision, and cross-run return to operation.
- Why no material first-party path remains: The supported paths enact selected modes and approve or refuse scoped work/effects. The source does not show a dedicated higher-level policy authority and feedback process at this boundary.

## Recursion

Individual tool loops and isolated workers sit inside one assessed workspace. External model adapters and independent verifier code provide inputs without donating external organizational authority.

## Variety and escalation

The journal and workspace observations preserve evidence for recovery. Contested child edits return to the operator, and a failed composed acceptance check forces an unsuccessful team outcome.

## Evidence gaps

Reviewed at frozen source. No provider, desktop, or verification-kit execution performed by the assessor. No conclusions about production safety or tamper-proof truth are inferred.
