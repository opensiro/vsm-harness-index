---
harness_id: af4j
project_name: AF4J
repository: https://github.com/datallmhub/agentflow4j
review_ref: f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AF4J

## Review boundary

- System in focus: The public first-party AgentFlow4J/AF4J JVM library and runtime for building and executing graph- or squad-composed AI agents.
- Purpose and identity: Provide repeatable, controlled multi-agent task execution with configurable graph steps, agent tool use, state, checkpoints, budgets, policies, approvals and observable runs.
- Relevant environment: Application requests, model/tool services, shared agent-run state, external tools, caller-supplied workflow configuration and human supervisors.
- Standard-distribution boundary: Published Java core, graph, squad and checkpoint APIs in the pinned source tree. The consuming application supplies models, concrete agents, graph topology, cost estimators, policy choices and optional stores. They are not treated as packaged autonomous organizational owners merely because the library can invoke them.
- Credited operating / distribution surfaces: `agentflow4j-core`, `agentflow4j-squad` agent executor/loop/routing, `agentflow4j-graph` graph execution, parallel merge/conflict handling, budgeting and approval, and `agentflow4j-checkpoint` persistence interfaces and implementations.
- Adjacent first-party surfaces excluded from ownership: `agentflow4j-samples`, `agentflow4j-test`, test harnesses, playground UI, docs, CI/release machinery, and contributor governance. They may corroborate shipped API behavior but do not donate decision rights to the library.
- First-party operating / deployment modes considered: JVM consumer-created `ExecutorAgent` with Spring AI `ChatClient` and configured tools; `ReActAgent` wrapper; composed graph/squad execution with optional simultaneous branches, checkpoint/resume and human approval; deterministic budget-policy routing. No autonomous agent is claimed from standalone Java graph execution without a model-backed executor.
- Recursion level: One consumer-assembled agent task organization and its sub-agents/graph nodes; upstream project governance and arbitrary downstream applications are outside this recursion.
- Reviewed revision: `f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506` (`main` at discovery).
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The first-party `ExecutorAgent` calls a configured Spring AI `ChatClient` and exposes model-mediated agent/tool execution and typed state updates. Its `ReActAgent` wrapper repeatedly executes the inner agent, applies results to the next context and terminates against a supplied stopping predicate and step cap. The `CoordinatorAgent` chooses one executor via an injected routing strategy; an LLM-driven implementation exists alongside fixed and budget-aware selection. A standalone coordinator does not split work or establish inter-agent negotiation.

`AgentGraph` composes named nodes with direct, conditional or result-dependent edges; its runtime drives frontier waves, optionally executes multiple nodes concurrently, merges their state changes, rejects incompatible writes to the same key, and waits on dependent joins. Runtime checkpoints and resume support approval/rejection and avoid replaying completed branches. A caller configures `BudgetPolicy`, `StatePolicy`, `ApprovalGate`, `ToolPolicy`, execution limits, log stores and routing strategies. These enforcement mechanisms do not by themselves own the organization's policy or resource decisions. Run logs and source tests document operational behavior, but are not independent complementary audits.

Primary source: [graph runtime](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/AgentGraph.java), [executor](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/ExecutorAgent.java), [ReAct wrapper](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/ReActAgent.java), [coordinator](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/CoordinatorAgent.java), [parallel tests](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/test/java/io/github/datallmhub/agentflow4j/graph/AgentGraphParallelTests.java), [budget tests](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/test/java/io/github/datallmhub/agentflow4j/graph/AgentGraphBudgetTests.java).

## Operational model

S1 is the model-backed agent executor carrying out application tasks and tool interactions, including separately wired branch agents. AF4J's graph supplies scheduling, conflict detection, state/policy enforcement and persistence; developer-supplied graph definitions, routing strategies and budget limits retain important construction rights. The supported first-party composition includes concrete coordination over conflicting parallel updates and a whole-run spend-dependent executor switch, both evidenced in implementation, but not an internally agent-governed metasystem. Human approvals apply to selected operational nodes, not automatically to identity/ultimate-policy governance.

## S1 — Operations
- State: A
- Function: A model-backed agent produces request-specific outputs and may invoke configured tools within its task environment.
- Disturbance / variety regulated: Changing user requests, tool responses, model output and intermediate state during task execution.
- Decisive decision or feedback right: Choose task responses and tool calls inside the active agent invocation; when wrapped in ReAct, act again using prior results.
- Decision owner: The invoked model-backed ExecutorAgent/ChatClient agent actor; a caller supplies tools and constraints.
- Supporting / enforcement mechanisms: ExecutorAgent tool callbacks, ToolPolicy wrapping, ReAct maxSteps/stopWhen, AgentGraph nodes and context/state transport.
- Closure path: Model response/tool activity yields AgentResult and optional state updates; ReActAgent applies results into a subsequent loop iteration, or AgentGraph passes resulting context to successor nodes.
- Boundary reachability: ExecutorAgent and ReActAgent are concrete exported first-party squad implementations used through the public Agent API and callable from AgentGraph nodes.
- Why this is / is not agent-owned: Model-mediated agent behavior is part of the supported runtime. Fixed graph routing and policy gates only support/constrain it.
- Evidence: [ExecutorAgent](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/ExecutorAgent.java), [ReActAgent](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/ReActAgent.java), [AgentGraph](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/AgentGraph.java)
- Basis: explicit source, structural runtime wiring
- Confidence: high for the shipped model-backed operating mode
- Caveats: No actual external model or tools were run for this assessment; caller-supplied providers remain outside the first-party ownership boundary.

## S2 — Coordination
- State: C
- Function: Prevent interference between distinct simultaneous graph-agent branches that modify common run state.
- Disturbance / variety regulated: Two parallel operational branches may write incompatible values to the same StateKey; premature joins can also consume an incomplete branch result.
- Decisive decision or feedback right: Choose whether conflicting concurrent writes may be accepted and whether a join may advance while a predecessor is pending.
- Decision owner: Configured first-party deterministic graph merge/join policy; the app developer chooses the branch graph and shared state. No agent owns the resolution discretion in the default path.
- Supporting / enforcement mechanisms: AgentGraph.runWave, mergeWave, StateConflictException, predecessors/waitsForFrontier and fail-fast propagation.
- Closure path: Non-conflicting branch updates are merged for subsequent graph nodes; incompatible values fail the run instead of silently selecting a winner; a join waits for gated predecessors and resumes after their completion.
- Boundary reachability: The shipped AgentGraph invokes concurrent frontiers, checks shared-key writes before merge and constructs join frontiers; these paths are exercised by native AgentGraphParallelTests rather than just README examples.
- Why this is / is not agent-owned: This is a function-specific coordination constructor with an enforceable response to an actual inter-S1 collision. The conflict choice is fixed runtime logic, so C rather than A; mere coordinator routing alone is not credited.
- Evidence: [AgentGraph mergeWave/waitsForFrontier](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/AgentGraph.java), [parallel conflicts and joins tests](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/test/java/io/github/datallmhub/agentflow4j/graph/AgentGraphParallelTests.java), [ParallelAgent](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/ParallelAgent.java)
- Basis: explicit source, structural tests
- Confidence: medium-high
- Caveats: Failing the run attenuates inconsistent state but does not negotiate a semantic resolution; this is bounded to the graph's state and join semantics, not arbitrary inter-agent disputes.

- Distinct S1 units: Two separately executing agent nodes/branches in one AgentGraph frontier, e.g. `a` and `b` in the first-party conflict tests.
- Inter-S1 disturbance: Both branches update the same shared StateKey to different values while running in parallel; the test `conflictingWritesFailTheRun` establishes the executable collision.
- Attenuating coordination relation: The graph's centralized wave merger checks cross-branch updates for equality, rejects contradictory writes and holds dependent joins until predecessors are ready.
- Feedback into subsequent S1 behaviour: On conflict, execution returns a failed result and suppresses downstream graph progression; with compatible writes the merged state reaches subsequent nodes; held joins run only after their predecessors.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The actual interference is same-key concurrent write corruption, with an explicit detection and run/next-node feedback path; selecting a worker or creating an edge was not the basis of the state.

## S3 — Inside-and-now control
- State: C
- Function: Regulate spend and constrained execution across current agent steps/branches with optional cost-aware executor selection.
- Disturbance / variety regulated: Multiple agent nodes/calls consume a shared run budget; using a premium executor after the available budget falls below a threshold can break whole-run resource constraints.
- Decisive decision or feedback right: Choose a spending limit, premium/fallback routing threshold, policy enforcement and how to respond to a budget breach.
- Decision owner: Application developer/operator supplies limits, cost functions, topology and routing strategy; first-party graph and router enforce the selected shared-current policy deterministically.
- Supporting / enforcement mechanisms: HierarchicalBudgetPolicy live per-run/per-node counters and estimators; AgentGraph budget checks and interrupts; BudgetAwareRouter reading remaining budget; optional run log.
- Closure path: The graph records spend after an agent result; the live remaining RUN budget can move a later CoordinatorAgent choice from premium to fallback; over-budget requests interrupt and prevent further node execution.
- Boundary reachability: Builder.budgetPolicy and RoutingStrategy.budgetAware are first-party production API entry points. BudgetAwareRouter reads the very BudgetPolicy instance that graph execution updates; unit tests confirm cross-node run caps and interrupts.
- Why this is / is not agent-owned: The shipped constructor can close a current, whole-run resource decision and feedback loop, but the defaults do not confer discretionary budget-priority ownership on an AI agent; static gates alone would not justify A.
- Evidence: [BudgetAwareRouter](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/BudgetAwareRouter.java), [HierarchicalBudgetPolicy](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/HierarchicalBudgetPolicy.java), [AgentGraph](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/AgentGraph.java), [budget enforcement tests](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/test/java/io/github/datallmhub/agentflow4j/graph/AgentGraphBudgetTests.java)
- Basis: explicit source and structural test; composition-dependent whole-run routing
- Confidence: medium
- Caveats: Requires a consumer to connect the budget-aware router to the same live policy instance used by the graph; enforcement of hard caps alone is not credited as autonomous S3. Human per-node approval is not treated as a separate S3 parent mode.

- Whole-system current view: A shared configured BudgetPolicy exposes aggregate remaining spend for the current graph run across nodes and calls.
- Current-control decision scope: Runtime admission/interrupt of prospective node spend and budget-dependent choice between already configured premium and fallback executors for subsequent work.

## S3* — Complementary audit
- State: —
- Function: No first-party complementary independent operational-audit decision loop was established for the assessed runnable library.
- Disturbance / variety regulated: The operating agents can make incorrect or misleading claims that would require a materially different evidence path to challenge.
- Decisive decision or feedback right: A distinct authority would need to judge direct operational evidence and return a corrective finding, not merely record run events.
- Decision owner: No such independent first-party owner identified in the reviewed supported runtime path.
- Supporting / enforcement mechanisms: Optional RunRecorder/RunLogStore, node lifecycle listeners and ordinary test infrastructure.
- Closure path: Run logs record the same execution events and tests run in adjacent development contexts; no separate independent audit-to-current-control path is shipped in the traced runtime.
- Why this is / is not agent-owned: Tracing, event logging, QA assertions and policy-error reporting do not independently challenge the agent's operational claims.
- Evidence: [RunRecorder](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/RunRecorder.java), [AgentGraph logging](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/AgentGraph.java), [run-log tests](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/test/java/io/github/datallmhub/agentflow4j/graph/RunLogTests.java)
- Basis: structural bounded absence
- Confidence: medium
- Caveats: A downstream consumer could supply an independent auditor, but its authority/closure is not in the reviewed first-party distribution.

### Absence scope

- Surfaces inspected: Graph and squad first-party runtime, run logger, execution events/listeners, run-log tests and documented public extension boundary.
- Plausible first-party paths checked: Trace-event recording, callback/listener reporting, graph failure observations, developer QA tests and hypothetical external independent evaluator integration.
- Why no material first-party path remains: These paths produce ordinary runtime records or caller-built verification, but no independently controlled complementary evidence judgment with findings changing subsequent S3 operation was located in the declared distribution.

## S4 — Outside-and-then intelligence
- State: —
- Function: No shipped loop that observes an external/prospective change, develops a capability adaptation option and returns the accepted option into current runtime capability was established.
- Disturbance / variety regulated: Changes in available tools/providers, future tasks or operating conditions could demand adaptation beyond current execution.
- Decisive decision or feedback right: A prospective adaptation judgment selecting how the harness's capability should change would be needed.
- Decision owner: Developer/application context configures agents, routing, tools and policies; no source-established prospective S4 owner in the assessed runtime.
- Supporting / enforcement mechanisms: ExecutorAgent resolves dynamic tool providers per invocation; graph supports branching, retry, state and new invocations.
- Closure path: Tool provider enumeration and per-request routing operate on current availability; no prospective external-environment option-selection/accepted capability-change return was found.
- Why this is / is not agent-owned: Current-state tool discovery, retries, model planning within task execution, configurable graphs and memory do not alone realize external-and-then adaptation.
- Evidence: [ExecutorAgent dynamic providers](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/ExecutorAgent.java), [Graph routing](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/AgentGraph.java), [RoutingStrategy implementation](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-squad/src/main/java/io/github/datallmhub/agentflow4j/squad/RoutingStrategy.java)
- Basis: bounded negative inference from first-party supported paths
- Confidence: medium
- Caveats: Custom application agents could implement prospective learning/adaptation, but their decision rights cannot be borrowed by the first-party harness.

### Absence scope

- Surfaces inspected: ExecutorAgent dynamic tool-provider resolution, graph conditional transitions and retries, ReAct wrapper and squad routing; published README/runtime architecture.
- Plausible first-party paths checked: Whether live provider changes, state persistence, LLM routing or callbacks include a prospective external intelligence, option selection and path to changed current capability.
- Why no material first-party path remains: All reviewed paths are per-run execution/selection or externally configured behavior; the required outside-and-then adaptation decision and return path were not supplied by AF4J itself.

## S5 — Policy and identity
- State: —
- Function: No organization-level identity/ultimate-policy choice with a legitimate decisional authority and returned operational closure was established.
- Disturbance / variety regulated: High-impact tool use, sensitive writes and node actions may violate caller-defined constraints, but these are current task permissions rather than demonstrably identity-level policy.
- Decisive decision or feedback right: Ultimate identity or policy determination for this agent organization, with a decision returned to the active runtime, would be necessary.
- Decision owner: Caller/developer defines static policy predicates and human approval points; no in-scope decisive S5 owner/parent-governed closure was established.
- Supporting / enforcement mechanisms: ToolPolicy, StatePolicy, ApprovalGate, checkpointed approval/rejection and resume markers.
- Closure path: An operator can approve a particular node and the graph resumes it; a configured allow/deny decision enforces a tool or state constraint. Neither path is shown to decide the organization's identity/ultimate policy.
- Why this is / is not agent-owned: Runtime enforcement of configured limits and generic human approval for a step cannot be relabeled S5 or (P) without an evidenced ultimate-policy question and authority/return path.
- Evidence: [ToolPolicy](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/ToolPolicy.java), [StatePolicy](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/StatePolicy.java), [ApprovalGate](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/ApprovalGate.java), [AgentGraph resume](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/main/java/io/github/datallmhub/agentflow4j/graph/AgentGraph.java), [approval tests](https://github.com/datallmhub/agentflow4j/blob/f9a7353f43f8a760d4f2d589f8d8eaf7e1c9a506/agentflow4j-graph/src/test/java/io/github/datallmhub/agentflow4j/graph/AgentGraphApprovalGateTests.java)
- Basis: bounded absence with positive/parent alternatives considered
- Confidence: medium
- Caveats: A consuming organization can impose ultimate policy outside AF4J; its rights are not part of this reviewed harness unless a specific supported in-boundary return path is demonstrated.

### Absence scope

- Surfaces inspected: Configured tool/state allow-deny rules, approval gate and checkpoint/resume paths, graph budget policy and first-party approval tests.
- Plausible first-party paths checked: Static permission and state policy composition, per-node human approver, config/build-time definition and status/error reporting as possible S5 or parent-governed routes.
- Why no material first-party path remains: The implemented decisions concern ordinary runtime action admissibility and operator approval; there is no evidenced first-party identity/ultimate-policy issue, legitimate ultimate authority and specific decision-return loop at the assessed recursion.

## Recursion

A caller may nest graphs, use CoordinatorAgent with subordinate ExecutorAgents, or run a graph as a node of another graph. These are compositional boundaries, not proof of complete nested viable-system governance at every layer. The assessment fixes the current application-assembled graph as system-in-focus, not AF4J's development organization or all downstream programs.

## Variety and escalation

Task variety is absorbed by model-backed executors with optional ReAct continuation. Parallel-state interference is fail-closed in the graph. Run-level cost variety is handled by configured budget enforcement and optional fallback routing. An approval gate can interrupt selected operations for parent input and resume after a returned action-specific decision; that does not alone establish S5. General inter-agent semantic negotiation, independent operational audit and future-adaptation governance were not located in the supported reviewed mode.

## Evidence gaps

- This is primary-source and first-party test inspection at a frozen commit, not an executed Java build, live model/tool integration run, or independent second semantic review.
- S2=C is bounded to executable shared-state conflict detection, fail-closed response and predecessor-aware joins. It does not imply arbitrary multi-agent conflict arbitration.
- S3=C relies on an explicitly supported consumer composition of shared live spend counters and a budget-aware router. It is not a claim that the configured runtime autonomously chooses its own budget or reallocates whole-project priorities.
- Current source evidence supports no S3*, S4 or S5 positive function path at the specified library boundary. If a specific active packaged closure path is later identified, request same-ref review rather than importing speculative behavior.
