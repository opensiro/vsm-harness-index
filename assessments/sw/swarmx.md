---
harness_id: swarmx
project_name: SwarmX
repository: https://github.com/tcztzy/swarmx
review_ref: a171e0da84c7a4d667d2c314cfbed66847f3040b
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: —
---

# SwarmX

## Review boundary

- System in focus: One directory-scoped SwarmX Host work cycle, its configured native Agents, shared Memory and desktop operator controls.
- Purpose and identity: Pursue persistent research/work goals under shared budgets and independently recorded acceptance.
- Relevant environment: User goals/criteria/corrections, external native model/harness/provider behavior, tool outputs, prices/cost coverage and competing work commitments.
- Standard-distribution boundary: Electron Host/ProductServices, packaged native adapters, WorkManager, agent-selection skill and Memory review/resource lifecycle; external native agents are explicitly installed/configured execution dependencies.
- Credited operating / distribution surfaces: apps/desktop/src/host/product-services.ts, work.ts, memory.ts, memory-review.ts; packaged delegate skill and desktop work/memory controls.
- Adjacent first-party surfaces excluded from ownership: CI, agentrc contributor automation, tests and local provider substitutes, legacy Pi examples, and separate swarmx-paper publication/evaluation work; none supplies product ownership.
- First-party operating / deployment modes considered: Manual and managed Work, automatic Memory review with writeApproval=false, and separately enabled operator writeApproval=true. Native credentials, admitted configurations and learning grants are deployment prerequisites.
- Recursion level: One configured Host work cycle. A managed supervisor's single-item delegation is lower-recursion operational work; its title is not whole-cycle control.
- Reviewed revision: a171e0da84c7a4d667d2c314cfbed66847f3040b.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

SwarmX is a TypeScript/Electron local research-work system, substantially changed from its OpenAI Swarm fork ancestry. The Host loads native Codex/Claude/DSH/ACP/gateway adapters and records their execution. It has no independent built-in model tool runtime; configured native Agents are part of the explicitly declared assembled mode. ProductServices.runWork prepares goal/criteria/evidence, reserves a runtime, dispatches the selected Agent and retains execution outcomes separately from acceptance. Managed mode installs first-party supervisor instructions to delegate, inspect results and request corrective follow-ups within the root budget/deadline.

WorkManager stores cycle/items/reservations/feedback in SQLite. Trusted desktop/Host callers own administration, criteria and budget edits; active agent callers cannot administer cycles or accept their own work. Recursive costs derive from original journals. Unknown outcomes and costs retain distinct reservations. Memory review runs a separate restricted native Agent over frozen original execution/feedback snapshots. Its evaluated selection concepts are reloaded into later delegation preparation. Registered local skill changes can undergo fixed validation and optional held-out behavioral evaluation before revision-checked replacement. Approval-enabled mode stages proposed changes for authenticated operator decisions. Native login/calls, domain scientific runtimes and private research memory are not inferred from tests.

## Operational model

Configured native Agents handle work-item goals, tools, child outcomes and corrective follow-ups. The supported assembled mode, not a hypothetical custom agent, connects these loops through native adapters. Deterministic Host gates enforce grants, budget identity and cancellation. The operator has whole-cycle current-control authority. Memory's prospective provider/harness/task-fit adaptation is assessed separately from ordinary request completion and from routine correctness acceptance.

## S1 — Operations

- State: A
- Function: Produce goal-directed work through native agent tool loops and retained responsibility for delegated results.
- Disturbance / variety regulated: Task-specific uncertainty, failing/partial child results, native errors and differing capabilities.
- Decisive decision or feedback right: Select operational actions, delegation and corrective follow-up until a goal is ready for independent acceptance or escalation.
- Decision owner: The configured native executor or managed supervisor Agent; the user separately owns criteria and final acceptance.
- Supporting / enforcement mechanisms: ProductServices native adapters, recorded execution, preparation checks, WorkManager reservations and cancellation propagation.
- Closure path: runWork prepares goal/criteria → native supervisor/executor → child/tool results → agent judges next operational action → returned output/submission.
- Boundary reachability: runWork explicitly injects managed supervisor instructions and dispatches configured native Agents; source exposes and checks swarm.prepare/send_message. Native dependencies and credentials are explicit supported setup, not borrowed developer agents.
- Why this is / is not agent-owned: The Host does not invent the next corrective message; removing the native agent's judgments leaves dispatch/recording without the operational response choices.
- Evidence: [apps/desktop/src/host/product-services.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/product-services.ts) lines 531–609 and 800–891; [packages/core/swarm/skills/delegate/SKILL.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/packages/core/swarm/skills/delegate/SKILL.md); [docs/native-agents.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/docs/native-agents.md).
- Basis: structural.
- Confidence: high for the wired supported mode.
- Caveats: No live native model/provider run was executed. Operational completion is not independent acceptance.

## S2 — Coordination

- State: —
- Function: No material first-party function established at the declared recursion.
- Disturbance / variety regulated: Interference between concurrent work agents or review consumers.
- Decisive decision or feedback right: No function-specific decisive-return path supplied.
- Decision owner: No qualifying owner; operational agent choices, caller settings and runtime enforcement remain distinct.
- Supporting / enforcement mechanisms: Cycle concurrency/reservations and directory-scoped review locks attenuate concrete duplicate consumption and overspending, but the response is fixed Host/SQLite enforcement; no first-party agent coordination decision or S2-specific autonomous composition contract is exposed.
- Closure path: Positive, function-specific constructor and eligible parent-mode alternatives checked; no qualifying closure remains.
- Why this is / is not agent-owned: The bounded absence concerns the organizational relation, not implementation purity.
- Evidence: [apps/desktop/src/host/work.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/work.ts); [docs/memory.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/docs/memory.md); [apps/desktop/tests/memory-review-ownership.test.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/tests/memory-review-ownership.test.ts)
- Basis: structural.
- Confidence: medium-high within the assessed distribution.
- Caveats: A custom deployment could add the function; that is outside this shipped boundary.

### Absence scope

- Surfaces inspected: host/work.ts reserve; docs/work-management.md; docs/memory.md; tests/memory-review-ownership.test.ts; packaged swarm skill.
- Plausible first-party paths checked: Duplicate review consumers, concurrent cycle admission, shared Memory lock, delegation and same-run preparation.
- Why no material first-party path remains: Fixed queue/transaction exclusion plus generic delegation does not expose the agent-owned or deliberately composable decisive coordination response required by this publication method.

## S3 — Inside-and-now control

- State: P
- Function: Regulate current whole-cycle commitments, resources and accountability across persistent work items.
- Disturbance / variety regulated: Competing goals, held/spent/unknown costs, unresolved effects, limited capacity and changing accepted commitments.
- Decisive decision or feedback right: Set/revise cycle budget and goal criteria, start/stop/revise work, reconcile unresolved outcomes/invoices and record independent acceptance.
- Decision owner: The legitimate local operator through trusted desktop/Host administration; active Agents are explicitly denied this authority.
- Supporting / enforcement mechanisms: WorkManager transactions, expected-version checks, retained reservations, descendant accounting and authenticated window IPC.
- Closure path: Cycle snapshot exposes item/attempt/spending/feedback state → operator revises commitments/budget or reconciles outcome → stored state changes → reserve/runWork obeys the returned limits and accepted dependencies.
- Boundary reachability: Long-term work desktop and trusted Host APIs are first-party shipped controls. WorkManager.trusted rejects administration/acceptance from active agent sessions.
- Why this is / is not agent-owned: A supervisor controls one work item's execution, not the declared whole-cycle budgets/criteria. Removing operator choices leaves fixed admission rules, not autonomous whole-cycle regulation.
- Whole-system current view: Cycle snapshot combines items, attempts, feedback, spend, reservations and unknown coverage at one directory/cycle.
- Current-control decision scope: Whole-cycle budget, commitments/criteria, acceptance, continuation and reconciliation; P is a complete supported operator mode.
- Evidence: [docs/work-management.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/docs/work-management.md); [apps/desktop/src/host/work.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/work.ts) lines 155–205, 340–438 and 538–650; [apps/desktop/src/host/product-services.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/product-services.ts) runWork.
- Basis: structural.
- Confidence: high.
- Caveats: No whole-cycle S3=A is inferred from single-item supervisor delegation or hard concurrency/budget gates.

## S3* — Complementary audit

- State: —
- Function: No material first-party function established at the declared recursion.
- Disturbance / variety regulated: Independent challenge to routine operational correctness/acceptance claims.
- Decisive decision or feedback right: No function-specific decisive-return path supplied.
- Decision owner: No qualifying owner; operational agent choices, caller settings and runtime enforcement remain distinct.
- Supporting / enforcement mechanisms: Trusted user/validator feedback is the routine production acceptance path. Memory reviews receive journal snapshots without tools; registered candidate evaluators test proposed resource updates rather than supply a separately governed sporadic operational audit.
- Closure path: Positive, function-specific constructor and eligible parent-mode alternatives checked; no qualifying closure remains.
- Why this is / is not agent-owned: The bounded absence concerns the organizational relation, not implementation purity.
- Evidence: [apps/desktop/src/host/memory-review.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/memory-review.ts); [docs/learning-resources.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/docs/learning-resources.md)
- Basis: structural.
- Confidence: medium-high within the assessed distribution.
- Caveats: A custom deployment could add the function; that is outside this shipped boundary.

### Absence scope

- Surfaces inspected: docs/work-management.md; docs/learning-resources.md; host/memory-review.ts; host/execution-evidence.ts; host/memory.ts.
- Plausible first-party paths checked: Original-event exports, independent acceptance, late correction, restricted memory reviewer and held-out resource evaluator.
- Why no material first-party path remains: A separate review session is not sufficient independence/complementarity by itself; no additional operational-claim audit judgment with corrective control is shipped beyond routine acceptance and learning validation.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: Adapt future execution capability/selection to observed external harness/model/provider task fit and corrected user requirements.
- Disturbance / variety regulated: Different provider/model/effort suitability, reliability/cost coverage and task conditions make an old selection policy or skill unsuitable for later work.
- Decisive decision or feedback right: Infer qualified future-use scenarios or prompt/skill changes from original execution and independent feedback, publish the chosen option into reusable selection knowledge; operator approval owns adoption in the alternate mode.
- Decision owner: Base A: configured restricted Memory-review Agent chooses the adaptation content and Host applies validated plans. Parent P: authenticated local operator approves/rejects each staged option when writeApproval is enabled.
- Supporting / enforcement mechanisms: Frozen original-event snapshots, evidence validation, durable plans, revision checks, optional fixed resource evaluator, pending-write UI and next-run preparation.
- Closure path: External/native behavior and user correction → bounded reviewer judges task/provider/effort fit and proposes future selection/skill option → automatic validated publication or operator decision → later swarm.prepare loads that evaluated concept and current feedback into operational selection.
- Boundary reachability: ProductServices constructs AgentMemory with reviewMemory and resumes it after native runtimes attach. Default Memory settings enable autoReview; the packaged delegate skill requires current private combination evaluations. Optional approval mode is wired through pending changes and decide/applyReview.
- Why this is / is not agent-owned: Credit is limited to explicit scenario-sensitive future combination/skill adaptation, not storage or retrospective summary alone. Removing reviewer judgment leaves snapshots/revision gates but no chosen future suitability recommendation. Parent adoption is separately owned when enabled.
- External distinction: Observed external provider/harness/model/effort behavior, user feedback and cost/reliability conditions, retained with scoped versions/coverage rather than fabricated universal rankings.
- Future / prospective distinction: The delegate skill asks which scenarios should choose a different combination next time; learned options persist across tasks and new preparations, rather than only repair the current answer.
- Adaptation option generated: Evidence-backed agent-selection concepts/Playbooks and registered prompt/skill candidates with counterevidence and limitations.
- Path back into current capability / S3: selection() reloads reviewed concepts plus current corrected feedback into swarm.prepare; operator-owned cycle grants/budgets bound adoption and subsequent work. Registered file changes apply on native next load.
- Evidence: [packages/core/swarm/skills/delegate/SKILL.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/packages/core/swarm/skills/delegate/SKILL.md) sections Choose a combination / Improve the evaluations; [apps/desktop/src/host/memory.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/memory.ts) selection(), review prompt and applyReview; [apps/desktop/src/host/product-services.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/product-services.ts) AgentMemory construction and callSwarm prepare; [apps/desktop/src/memory.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/memory.ts); [docs/learning-resources.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/docs/learning-resources.md).
- Basis: structural.
- Confidence: medium-high for supported selection-adaptation closure.
- Caveats: No measured gain or general provider-quality claim. Only external/task-fit prospective adaptation is credited; ordinary memory writes and all generic self-improvement are not automatically S4. Learning disabled/grant-free deployments do not exercise this path.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Restricted configured Memory-review Agent | Eligible external execution/feedback batch under enabled grants | Agent-selected scenario option is validated/published and reloaded into later delegation | host/memory.ts, host/product-services.ts, delegate skill |
| Parent (`P`) | Authenticated local operator | Same scenario-adaptation plan with writeApproval=true | approve/reject → decide/apply or no adoption → later preparation observes only accepted knowledge | host/memory.ts submit/decide/applyReview; renderer/memory.tsx |

## S5 — Policy and identity

- State: —
- Function: No material first-party function established at the declared recursion.
- Disturbance / variety regulated: Identity/ultimate-policy disputes at Host-cycle recursion.
- Decisive decision or feedback right: No function-specific decisive-return path supplied.
- Decision owner: No qualifying owner; operational agent choices, caller settings and runtime enforcement remain distinct.
- Supporting / enforcement mechanisms: Permissions, user notes, standing criteria and policy settings constrain work. updatePolicy requires idle execution and stores grants, but no identity-level dispute-to-legitimate-parent-and-return process is supplied.
- Closure path: Positive, function-specific constructor and eligible parent-mode alternatives checked; no qualifying closure remains.
- Why this is / is not agent-owned: The bounded absence concerns the organizational relation, not implementation purity.
- Evidence: [apps/desktop/src/host/product-services.ts](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/apps/desktop/src/host/product-services.ts) updatePolicy; [docs/permissions.md](https://github.com/tcztzy/swarmx/blob/a171e0da84c7a4d667d2c314cfbed66847f3040b/docs/permissions.md)
- Basis: structural.
- Confidence: medium-high within the assessed distribution.
- Caveats: A custom deployment could add the function; that is outside this shipped boundary.

### Absence scope

- Surfaces inspected: permissions.ts; settings.ts; host/product-services.ts updatePolicy; host/memory.ts; docs/permissions.md; AGENTS.md.
- Plausible first-party paths checked: Host grant edits, memory user preferences, reviewer inability to expand authority, work criteria and contributor policies.
- Why no material first-party path remains: These are permission/configuration and operational/adaptation controls; no shipped ultimate-identity decision loop is evidenced at the declared cycle boundary.

## Distributed OSS parent arrangement

P ownership is the local installed Host operator, not repository maintainers or all independent OSS contributors. No organization-level governance is borrowed from AGENTS.md or agentrc.

## Self-hosted and non-human modes

Manual/managed work and enabled learning are supported configured modes. A(P) describes alternate adoption owners, not simultaneous authority. No fully non-human whole-cycle controller or ultimate-policy owner is claimed.

## Recursion

Native supervisors and delegated tasks may regulate their own local operational goals. Their existence does not establish recursive viability or transfer lower-recursion control into the whole-cycle S3 classification.

## Variety and escalation

Host preserves unknown cost/outcome distinctions, criteria versions and cancellation identity; native interactions return questions/permissions to users. Unresolved outcomes block retry until trusted reconciliation. Such statuses alone are not algedonic channels.

## Evidence gaps

Source and first-party engineering tests were inspected without executing live native agents or the separate research protocol. Held-out resource evaluator semantics and private provider observations remain deployment-owned. S4 maps the wired prospective selection mechanism, not proven empirical improvement or every learning execution.

