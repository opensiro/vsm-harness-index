---
harness_id: covalo
project_name: Covalo
repository: https://github.com/bzcsk2/covalo
review_ref: 2521674d0f2295226ee5075d03c851387a6c5d9b
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Covalo

## Review boundary

- System in focus: the first-party Covalo TypeScript/Bun terminal agent runtime, including the TUI-created DualAgentRuntime and WorkflowCoordinator at frozen SHA 2521674d0f2295226ee5075d03c851387a6c5d9b.
- Purpose and identity: use low-cost/local model coding Worker loops under an explicitly separate stronger Supervisor with planning, report checks, adaptive intervention, budgets and user escalation.
- Standard-distribution boundary: `packages/core` and shipped `packages/cli/src/tui.ts`, including `packages/core/src/workflow-coordinator/coordinator.ts` and the native tool loop. Do not borrow external LLM servers, plugins or development tests.
- Relevant environment: current user's engineering goal, mutable repository, tool results, Worker reports and errors, Supervisor plan/feedback, budgets and CLI operator.
- First-party modes considered: basic native coding loop, TUI dual-runtime supervised workflow, Supervisor guidance and bounded iteration. Mailbox workflow is optional and disabled by default; in-state report/plan path is counted instead.
- Recursion: one current Worker S1 and one model-driven Supervisor actor controlling that bounded workflow, not an enterprise agent fleet.
- Profile 0.2.4 / Methodology 0.3.7.
- Credited operating / distribution surfaces: packages/core/src/loop.ts native streaming model/tool loop, packages/core/src/workflow-coordinator/coordinator.ts source-implemented Supervisor/Worker plan/report/check/intervene transitions, packages/cli/src/tui.ts installed TUI wiring and DualAgentRuntime.
- Adjacent first-party surfaces excluded from ownership: other LLM provider internal implementations, content-pack plugins, tests/smoke, docs roadmaps and product/maintainer authority; disabled-by-default mailbox workflow cannot be used to add extra default autonomy.


## Repository architecture

The native packages/core/src/loop.ts runs model/tool turns and retains agent context. The TUI packages/cli/src/tui.ts constructs a DualAgentRuntime and WorkflowCoordinator with actual Supervisor and Worker instances. Coordinator runSupervisorAnalyse builds an updated task plan from goal plus previous Worker report/Supervisor feedback, runWorkerDo submits it to a model-driven Worker, runWorkerReport obtains completion claims, runSupervisorCheck parses distinct Supervisor decisions and requires structured completion audit evidence for approval, and runSupervisorIntervene triggers targeted advice on repeated Worker errors then returns to Worker execution. The optional mailbox path is explicitly disabled by default, so the first-party state-passed plan/report and TUI route are the decisive positive witnesses, not unshipped agent messaging.

## Operational model

A user starts a goal through the installed TUI. The Supervisor model reviews the whole current workflow state and creates an initial plan; a separate model-guided Worker acts with native coding tools and reports back. Supervisor checks the current report, can revise, continue, approve with evidence, ask user, block under explicit blocker conditions or intervene mid-work after repeated errors. Revised instructions return to Worker and results return again to Supervisor. This is a real current-control S3 above an operational S1, but one Worker does not prove inter-S1 S2 and in-band Supervisor checks do not become complementary S3*.

## S1 — Operations

- State: A
- Function: Execute source-editing and tool-based coding steps adaptively under changing task evidence.
- Disturbance / variety regulated: Changing source files, user-defined tasks, model/tool outcomes and current authority.
- Decisive decision or feedback right: Choose a function-specific next decision from current evidence.
- Decision owner: Shipped Worker model actor in packages/core/src/loop.ts, wired through CLI DualAgentRuntime; the model provider supplies inference only.
- Supporting / enforcement mechanisms: Worker streaming model/tool loop, guided prompts, selection of actions, worktree tools and bounded session results.
- Closure path: Task or supervisor plan → Worker model/tools → execution outcomes → next model call and worker report → renewed iteration.
- Why this is / is not agent-owned: The worker model chooses substantive tool actions in the native loop and can adapt to Supervisor feedback and tool results; model guidance is not just deterministic dispatch.
- Boundary reachability: The declared first-party packaged CLI or runtime directly exposes and runs the described mode without borrowing any external agent task loop.
- Evidence: [packages/core/src/loop.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/loop.ts); [packages/core/src/workflow-coordinator/coordinator.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/workflow-coordinator/coordinator.ts); [packages/cli/src/tui.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/cli/src/tui.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: high.
- Caveats: Function evidence is restricted to the frozen standard distribution and declared workflow recursion.

## S2 — Coordination

- State: —
- Function: Attenuate interference among several independent current operating S1 agents through their own adaptive coordination.
- Disturbance / variety regulated: Changing source files, user-defined tasks, model/tool outcomes and current authority.
- Decisive decision or feedback right: Choose a function-specific next decision from current evidence.
- Decision owner: No separate first-party decision owner shown at this function boundary.
- Supporting / enforcement mechanisms: Model/tool runtime, bounded configuration, observability, deterministic guards and optional user actions.
- Closure path: First-party mechanisms operate, but the required function-specific independent choice/return is not established.
- Why this is / is not agent-owned: The packaged dual-mode workflow has one current operational Worker and one supervisory model; there is no established second concurrently active S1 whose conflicts require S2 mediation.
- Evidence: [packages/core/src/workflow-coordinator/coordinator.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/workflow-coordinator/coordinator.ts); [packages/core/src/dual-agent-runtime/dual-runtime.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/dual-agent-runtime/dual-runtime.ts); [packages/cli/src/tui.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/cli/src/tui.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Function evidence is restricted to the frozen standard distribution and declared workflow recursion.

### Absence scope

- Surfaces inspected: dual-agent workflow, Worker's one task activity and optional tool concurrency and mailbox/controller.
- Plausible first-party paths checked: Supervisor versus Worker roles as two S1s, tool parallelism as inter-S1 coordination, task dependencies and shared state.
- Why no material first-party path remains: Supervisor is a model-led metasystem actor, not another independently competing operational coding S1; no concrete conflict between distinct autonomous S1s and returned mediation loop is shipped at this selected recursion.

## S3 — Inside-and-now control

- State: A
- Function: Manage the inside-and-now commitments of the bounded Supervisor–Worker coding organization, from a whole-current workflow state and repeated model-driven adjustments.
- Disturbance / variety regulated: Current Worker errors, blocked operations, incomplete tasks, budget and workflow iteration state, stale plans and unacceptable results.
- Decisive decision or feedback right: Choose next current Worker plan and feedback, intervene when repeated errors occur, decide continuation versus approval or user escalation based on current whole-workflow evidence.
- Decision owner: Model-driven Supervisor instantiated alongside Worker by the shipped TUI DualAgentRuntime and WorkflowCoordinator; legitimate human user controls the original goal.
- Supporting / enforcement mechanisms: runSupervisorAnalyse/Check/Intervene, structured decisions with confidence and audit checks, Worker state/report, GoalStore and workflow transitions.
- Closure path: Current goal/plans/Worker report+errors → Supervisor model planning/review/intervention → next Worker task instructions and goals → new Worker execution feedback → repeated Supervisor decision.
- Why this is / is not agent-owned: Supervisor is a distinct first-party model actor that inspects current goal, plan, previous worker report and feedback, and autonomously chooses followup, new plan, revise/approve/ask_user/blocked or mid-run intervention; preset audit checks constrain completion but do not choose semantic priorities.
- Boundary reachability: The declared first-party packaged CLI or runtime directly exposes and runs the described mode without borrowing any external agent task loop.
- Whole-system current view: WorkflowCoordinator reads the bounded current workflow's goal, iteration, active Supervisor plan, current Worker report and errors, Supervisor feedback, budget-limited/blocked/active GoalStore status, and operator resume instruction. One Worker is the whole operational population at this recursion; no fleet-wide view is claimed.
- Current-control decision scope: a distinct Supervisor model updates the current Worker plan, decides approve/continue/revise/ask_user/blocked under structured protocol, and supplies mid-run intervention following repeated Worker errors; these choices return to Worker execution in the next phase. Quotas and completion-audit fields constrain but do not make the model's semantic decisions.
- Evidence: [packages/core/src/workflow-coordinator/coordinator.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/workflow-coordinator/coordinator.ts); [packages/core/src/dual-agent-runtime/dual-runtime.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/dual-agent-runtime/dual-runtime.ts); [packages/cli/src/tui.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/cli/src/tui.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Positive S3 is strictly at the bounded single Supervisor–Worker workflow recursion, not across a fleet of users/projects. Structured decisions are guarded and budget-bounded.

## S3* — Complementary audit

- State: —
- Function: Complementary, independently owned auditor directly inspecting operational reality and returning a correction to the present S3 regulator.
- Disturbance / variety regulated: Changing source files, user-defined tasks, model/tool outcomes and current authority.
- Decisive decision or feedback right: Choose a function-specific next decision from current evidence.
- Decision owner: No separate first-party decision owner shown at this function boundary.
- Supporting / enforcement mechanisms: Model/tool runtime, bounded configuration, observability, deterministic guards and optional user actions.
- Closure path: First-party mechanisms operate, but the required function-specific independent choice/return is not established.
- Why this is / is not agent-owned: The Supervisor is already the S3 current controller and evaluates normal Worker reports as routine part of its plan/revise/approve cycle; completionAudit/blockerAudit structured checks and guided-loop guardrails are normal regulation, not a distinct independent audit authority.
- Evidence: [packages/core/src/workflow-coordinator/coordinator.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/workflow-coordinator/coordinator.ts); [packages/core/src/supervisor/guided-loop.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/supervisor/guided-loop.ts); [packages/core/src/workflow-coordinator/structured-protocol.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/workflow-coordinator/structured-protocol.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Function evidence is restricted to the frozen standard distribution and declared workflow recursion.

### Absence scope

- Surfaces inspected: SupervisorCheck, WorkerReport, completion evidence and blocker audit gates, guided-loop status and logs.
- Plausible first-party paths checked: Supervisor itself renamed auditor, completionAudit field as independent audit, scoring heuristic, separate provider optional reviewer.
- Why no material first-party path remains: the sampled report and completion gates are in-band Supervisor regulation, without a separately owned complementary direct-evidence audit challenging S3 decisions with a corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: Generate and implement adaptation to prospective external environment and future Covalo capabilities.
- Disturbance / variety regulated: Changing source files, user-defined tasks, model/tool outcomes and current authority.
- Decisive decision or feedback right: Choose a function-specific next decision from current evidence.
- Decision owner: No separate first-party decision owner shown at this function boundary.
- Supporting / enforcement mechanisms: Model/tool runtime, bounded configuration, observability, deterministic guards and optional user actions.
- Closure path: First-party mechanisms operate, but the required function-specific independent choice/return is not established.
- Why this is / is not agent-owned: Supervisor planning handles the current user goal and next iterations, not environmental future opportunities and systemic capability selection.
- Evidence: [packages/core/src/workflow-coordinator/coordinator.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/workflow-coordinator/coordinator.ts); [packages/core/src/goal/steering.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/goal/steering.ts); [README.md](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/README.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Function evidence is restricted to the frozen standard distribution and declared workflow recursion.

### Absence scope

- Surfaces inspected: current goal steering, model/provider selection, context/memory, workflow replan and extensions.
- Plausible first-party paths checked: future-looking Supervisor plan as S4, model fallback as strategic intelligence, auto skill evolution and explicit external horizon scanner.
- Why no material first-party path remains: all evidenced changes regulate the bounded current task; release/config and future capabilities remain externally selected.

## S5 — Policy and identity

- State: —
- Function: Legitimately resolve ultimate identity/policy contradictions and issue binding changed organizational authority.
- Disturbance / variety regulated: Changing source files, user-defined tasks, model/tool outcomes and current authority.
- Decisive decision or feedback right: Choose a function-specific next decision from current evidence.
- Decision owner: No separate first-party decision owner shown at this function boundary.
- Supporting / enforcement mechanisms: Model/tool runtime, bounded configuration, observability, deterministic guards and optional user actions.
- Closure path: First-party mechanisms operate, but the required function-specific independent choice/return is not established.
- Why this is / is not agent-owned: User goals, permission and budget policies constrain both Worker and Supervisor; model-driven choices do not redefine legitimate ultimate purpose.
- Evidence: [packages/core/src/workflow-coordinator/coordinator.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/workflow-coordinator/coordinator.ts); [packages/core/src/loop.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/core/src/loop.ts); [packages/cli/src/tui.ts](https://github.com/bzcsk2/covalo/blob/2521674d0f2295226ee5075d03c851387a6c5d9b/packages/cli/src/tui.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Function evidence is restricted to the frozen standard distribution and declared workflow recursion.

### Absence scope

- Surfaces inspected: operator goal prompts, tool permission gates, user escalation, model budget/approval and TUI controls.
- Plausible first-party paths checked: Supervisor ask_user as S5, blocked decision as policy dispute, user-configured agents as parent identity.
- Why no material first-party path remains: ask_user escalates an operational task decision; no first-party ultimate purpose conflict → legitimate authoritative decision → changed governing policy loop is evidenced.

## Distributed OSS parent arrangement

Repo contributors, operators and model endpoint providers retain distinct ownership. Covalo controls one executing supervised workflow, not legitimate policies for all independent deployed copies.

## Self-hosted and non-human modes

Bun CLI/TUI can use local or hosted models; the first-party loop owns tool execution and current Supervisor/Worker coordination. Operator sets provider routing, goal/budgets and permissions; no full external-future S4 or S5 mode is inferred.

## Recursion

One operational Worker agent (S1=A) and a separate Supervisor deciding whole-current workflow commitments (S3=A), with no independent competing worker population establishing S2. Workflow iterations are the return mechanism, not extra independent viable systems.

## Variety and escalation

Worker errors and changing tool observations drive next actions; Supervisor decisions can revise work, inject intervention, request user clarification, or block after guarded repeated evidence. Explicit budget/goal gates avoid premature completion but are not complementary independent audit.

## Evidence gaps

Positive S3 concerns one packaged workflow, not a scaled team or business. Supervisor observes model-generated Worker reports and selected errors, not an independent complementary raw audit. No model-backed deployment performance rate was measured; source-first structural evidence under pinned ref.

## Assessment summary

**Proposed included**, vector `S1=A / S2=— / S3=A / S3*=— / S4=— / S5=—`. Native Worker tools and a distinct TUI-wired adaptive Supervisor produce actual current-control return; other VSM functions are not inferred from tool names or ordinary gates.

