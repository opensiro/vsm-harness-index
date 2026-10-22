---
harness_id: moatless-tools
project_name: Moatless Tools
repository: https://github.com/aorwall/moatless-tools
review_ref: 011ead57a5c81664e9c45e07e1f50b17e695cc63
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Moatless Tools

## Review boundary

- System in focus: one Moatless action-agent coding/repository task executed through its published flow abstractions, including the normal linear `AgenticLoop` and the optional `SearchTree` flow. Not the maintainer's separate `moatless-tree-search` research repository or SWE-bench evaluation organization.
- Purpose and identity: construct context for an LLM-driven agent, generate and execute typed tool actions, then iterate using observations to inspect/edit code or complete another user task.
- Relevant environment: source repositories, workspaces and runtime environments; prompts and model completions; generated actions and tool observations; configurable flow, selector and feedback settings; operator-provided project/trajectory settings.
- Standard-distribution boundary: packaged `moatless.agent.ActionAgent`, `moatless.flow.{AgenticLoop,OneOffFlow,SearchTree}`, first-party action/completion/workspace abstractions and API/runner integrations. The README's basic agent example and supported flow configurations supply reachable modes. Separate `moatless/evaluation/` and `scripts/run_evaluation.py` benchmark campaigns are adjacent, not owners at the coding-task recursion.
- Credited operating / distribution surfaces: `moatless/agent/agent.py`, `flow/{flow,loop,oneoff,search_tree,manager}.py`, `node.py`, `actions/`, `completion/`, `feedback/`, `selector/`, `expander/`, `value_function/`, the local API and runner wiring when used to execute a task.
- Adjacent first-party surfaces excluded from ownership: SWE-bench runs and dashboards, benchmark evaluation managers and batch results, notebooks/tests, Docker/Kubernetes runner operations as independent execution infrastructure, and human OSS development/release choices. `moatless-tree-search` is explicitly linked as a different repository, so no role or result from it is borrowed.
- First-party operating / deployment modes considered: direct `ActionAgent.run_simple`, linear iterative `AgenticLoop`, one-off flow, configurable `SearchTree` with optional value function and feedback generator, API-run trajectories and optional queued project jobs. Notional third-party multi-agent compositions are excluded.
- Recursion level: one task/trajectory whose source-editing steps are executed by one configured action agent, including alternative search-node states of that task. Multi-trajectory worker infrastructure is not itself a demonstrated autonomous multi-unit organization.
- Reviewed revision: [`aorwall/moatless-tools@011ead57a5c81664e9c45e07e1f50b17e695cc63`](https://github.com/aorwall/moatless-tools/tree/011ead57a5c81664e9c45e07e1f50b17e695cc63), frozen in [batch #1884](https://github.com/opensiro/vsm-harness-index/issues/1884).
- Observation date: 2026-10-22; source/config/docs analysis only, with no LLM-agent, model-provider or SWE-bench run.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The README describes an installable Python `moatless` package and a docker-hosted UI, and shows a minimal `ActionAgent` whose completion model generates typed action arguments. The `ActionAgent` initializes completion schemas from its installed actions, creates task nodes, asks its completion model to select actions, then calls the matching action's `execute` method and attaches observations or artifact changes to the node. The next generated action uses a message-history generator and the node/workspace context.

`AgenticFlow` contains one configured `ActionAgent`, a root task node and iteration/cost caps. `AgenticLoop` repeatedly creates a successor node after an action and calls the same agent. `OneOffFlow` executes one task node. Optional `SearchTree` uses a `BaseSelector`, expander and the same `ActionAgent` for candidate child nodes; after node simulation, a value function may score the result and backpropagate a reward, while a feedback generator may place task-specific feedback in the next node's user message. Its shipped `SimpleSelector` chooses the first expandable candidate, and the expander creates child **states** rather than independent enduring agents. Neither reward, node selection nor branch breadth is automatic evidence of independent S1 management or an S2 collision-resolution relation.

`FlowManager` loads operator-stored flow/agent/model configurations, creates trajectories, starts jobs and exposes state through API/storage/eventbus. `SchedulerRunner` queues jobs with static maximum active counts by project/total. Those are supporting infrastructure and configured constraints; the project does not show a separate autonomous current-management decision owner. Optional Maven compilation feedback checks the outcome of a candidate coding action, rather than auditing S3.

Primary sources: [README](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/README.md), [ActionAgent](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/agent/agent.py), [AgenticLoop](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/loop.py), [SearchTree](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/search_tree.py), [FlowManager](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/manager.py).

## Operational model

One action agent chooses task-local actions from the model's structured completion and executes them through the workspace. A flow decides mechanically when to iterate, branch, terminate or select a candidate state; task feedback from action observations or a value function can inform later model steps. A search branch is a candidate state in the *same* task, not evidence of a separately accountable S1 cell whose commitments must be coordinated with another cell. Operator config, scheduler limits and evaluation feedback are separated from agent-owned operational judgment.

## S1 — Operations

- State: A
- Function: carry out a user-supplied coding task through model-selected actions on the workspace, with subsequent actions informed by returned observations.
- Disturbance / variety regulated: uncertain code location, incomplete task information, unsuccessful edits/tests, observed tool failures and alternative candidate task states.
- Decisive decision or feedback right: `ActionAgent._generate_actions` obtains model-created structured action arguments and chooses action types; `ActionAgent._execute` obtains the corresponding tool observation, used by later message generation and action steps.
- Decision owner: configured model-driven `ActionAgent` in the reachable basic, iterative and tree-search task modes; flow and tool classes implement selection/dispatch rules and execution support.
- Supporting / enforcement mechanisms: action schema registry, completion model, message history, node/file context and artifact observations, flow loop, optional reward and feedback generators, workspace/runtime.
- Closure path: task/root node → generated messages → model-selected action → tool execution → observation/artifact change attached to node → successor or selected task node → subsequent agent decision.
- Boundary reachability: the README directly instantiates `ActionAgent` with an action and calls `run_simple`; `AgenticFlow` holds an `ActionAgent` and `AgenticLoop` / `SearchTree` call its `run` on reachable nodes in installed first-party code.
- Why this is / is not agent-owned: the model picks executable actions and their parameters from task context rather than receiving a fixed precomputed sequence; runner and action handlers simply execute/return observations.
- Evidence: [README direct example](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/README.md), [agent model-action loop](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/agent/agent.py#L62-L236), [iterative use](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/loop.py#L20-L80).
- Basis: direct first-party code and documented reachable example.
- Confidence: high for supported S1 decision ownership; no claim about solution quality or benchmark success.
- Caveats: the model provider/benchmark were not exercised; `shadow_mode` and workspace setup affect persistence, not the existence of the task-local model/action choice.

## S2 — Coordination

- State: —
- Function: attenuate specific actual or structurally evidenced interference/oscillation between distinct operational S1 units and feed that correction into their subsequent work.
- Disturbance / variety regulated: competing code edits across workers are possible externally, but the shipped tree branches are isolated candidate states under one action-agent execution path rather than distinct operational actors with conflicting active commitments.
- Decisive decision or feedback right: no inter-S1 collision detector and coordinating correction owner is evidenced in supported flows.
- Decision owner: none at the assessed recursion; `SearchTree` selector/expander and scheduler choose candidate execution order according to configured rules.
- Supporting / enforcement mechanisms: node parent/child links and cloned file context, optional reward/backpropagation and feedback, scheduler job caps and eventbus.
- Closure path: candidate node → reward/feedback → subsequent candidate choice; this is optimization/feedback *within S1 task search*, not detection and damping of interference among independent S1 cells.
- Why this is / is not agent-owned: selecting a candidate branch and avoiding duplicates does not resolve contradictory worker commitments; the shipped simple selector is deterministic and no separate inter-agent corrective feedback exists.
- Evidence: [SearchTree selection/expansion](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/search_tree.py#L154-L255), [child state expander](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/expander/expander.py), [simple selector](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/selector/simple.py).
- Basis: bounded negative from configured runtime architecture.
- Confidence: high that no S2-specific inter-operational conflict relation is shipped in the reviewed flow modes.
- Caveats: parallel SWE-bench jobs or third-party agents are different trajectories and external orchestration, not qualifying coordination by mere coexistence.

### Absence scope

- Surfaces inspected: `ActionAgent`, `AgenticFlow`/`AgenticLoop`/`SearchTree`, selector, expander, node-state copying, runner scheduler, eventbus and workflow manager.
- Plausible first-party paths checked: independent agent construction per branch, active shared write contention, worker collision detection, corrective branch reconciliation and feedback into two distinct S1 behaviors.
- Why no material first-party path remains: the published variants execute one configured `ActionAgent` on candidate task states; optional branch valuation is task-search optimization rather than S2 interference attenuation, and global job count limits do not coordinate S1 conflicts.

## S3 — Inside-and-now control

- State: —
- Function: use a whole-current organization view to decide shared priorities, resources, commitments, accountability and corrective interventions.
- Disturbance / variety regulated: too many search iterations, API jobs and candidate costs; these are controlled by preset caps or task-local optimizer logic, not evidenced discretionary present-wide governance.
- Decisive decision or feedback right: `max_iterations`, `max_cost`, branch count and scheduler concurrency caps are configuration/enforcement; no first-party agent or legitimate parent uses a whole-current view to trade off current operational commitments.
- Decision owner: operators configure flows/models and optional job limits; code enforces them mechanically. No qualifying closed S3 decision owner in the standard task mode.
- Supporting / enforcement mechanisms: `FlowManager`, trajectory metadata and storage, `SchedulerRunner`, `AgenticFlow.is_finished`, `SearchTree` cost/terminal criteria and UI requests.
- Closure path: static limits/status → admit or stop task execution; missing sensed whole-current system dynamics → priority/resource/accountability decision → corrective return.
- Why this is / is not agent-owned: a model's per-node code action or a UCT/reward search policy is not present-wide organizational management; a scheduler enforcing a threshold does not own management just because it affects resource usage.
- Evidence: [flow constraints](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/flow.py#L25-L70), [search termination/backpropagation](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/search_tree.py#L285-L390), [scheduler caps](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/runner/scheduler.py#L21-L113), [flow manager configuration](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/manager.py#L35-L160).
- Basis: bounded first-party negative; parent/operator modes checked explicitly.
- Confidence: medium-high within the declared one-trajectory recursion.
- Caveats: a human operating an external multi-project fleet may make actual S3 decisions, but that parent organization/return loop is not implemented by these configuration forms.

### Absence scope

- Surfaces inspected: `FlowManager`, flow and search-tree controllers, `SchedulerRunner`, runner status and API controls, agent/model config managers and event/state storage.
- Plausible first-party paths checked: management by search-tree reward policy, cross-job capacity/status view, dynamic reprioritization and operator `P` authority via flow-model settings.
- Why no material first-party path remains: node selection addresses alternatives inside one task, while runner caps and settings are predeclared execution constraints; neither supplies a closed organization-wide discretionary current-management correction.

## S3* — Complementary audit

- State: —
- Function: independently inspect S3 operating/management claims via a complementary reality path and return corrective audit judgment.
- Disturbance / variety regulated: erroneous generated edits and misleading task success/reward signals; the shipped validators concern candidate coding outcomes rather than independently assessing management commitments.
- Decisive decision or feedback right: no independent management auditor or S3-directed audit verdict path is wired in standard flows.
- Decision owner: optional deterministic test/value functions or user-supplied feedback can evaluate task results, not management decisions at the chosen recursion.
- Supporting / enforcement mechanisms: `BaseValueFunction`, optional `BaseFeedbackGenerator`, Maven compiler checker, node rewards and event logs.
- Closure path: candidate code → compiler/test/reward feedback → another task search step; no complementary inspection of S3 claims → independent judgment → management correction.
- Why this is / is not agent-owned: even when an outcome validator runs separately from code generation, its subject is local code correctness, not S3 operating reality. Outcome reward parsing is not S3* ownership.
- Evidence: [value function contract](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/value_function/base.py), [feedback injection](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/search_tree.py#L251-L336), [Maven compilation feedback](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/feedback/maven_compilation_checker.py).
- Basis: bounded negative.
- Confidence: high for the reviewed published management-audit boundary.
- Caveats: benchmark result verification and human review are adjacent/outside the target task's S3* organization.

### Absence scope

- Surfaces inspected: reward/value/feedback classes, deterministic build checker, trace events, runner status, FlowManager and evaluation-adjacent modules.
- Plausible first-party paths checked: independent complementary runtime access, audit of whole-current S3 decisions, auditor independence from agent/task feedback and management corrective return.
- Why no material first-party path remains: the only evidenced feedback rates or fixes coding outcomes within the same trajectory; no S3 audit subject, independent S3* decision right or return-to-S3 path is published.

## S4 — Outside-and-then intelligence

- State: —
- Function: detect prospective external environment changes, form strategic capability options and adopt/return an option to present work.
- Disturbance / variety regulated: changed future models, technology, codebases and work requirements; the implemented code index, search and local refinement concern the present assigned problem.
- Decisive decision or feedback right: no supported running component chooses enduring capability changes from prospective external sensing.
- Decision owner: operator/maintainer selects flow and model configurations; `ActionAgent` chooses present-task actions; no autonomous or parent-closed S4 path is established.
- Supporting / enforcement mechanisms: configurable models/flows, branch rewards, history/context retrieval and benchmark research artifacts.
- Closure path: source context → present task action or branch refinement; absent outside-future scan → options/adoption authority → persistent capability change affecting future operation.
- Why this is / is not agent-owned: iterative tree search and reinforcement of candidate coding steps are not prospective strategy. Repository experiments and model choices do not prove an S4 loop in the deployed flow.
- Evidence: [README scopes/modes](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/README.md), [flow model override](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/manager.py#L60-L100), [search reward propagation](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/search_tree.py#L285-L347).
- Basis: bounded first-party absence after checking plausible learning/search paths.
- Confidence: high for absence in the reviewed task runtime.
- Caveats: a future version or external research system might introduce S4; the frozen code does not.

### Absence scope

- Surfaces inspected: agent prompts/actions, selection/expansion/reward feedback, model-config manager, trajectory persistence, README and evaluation workflows.
- Plausible first-party paths checked: learning across completed tasks, strategic proposal and adoption from benchmark trends, provider adaptation and parent-operator capability reform.
- Why no material first-party path remains: these surfaces provide current-task optimization or externally supplied settings only; no future-facing adaptation feedback and adoption loop is packaged.

## S5 — Policy and identity

- State: —
- Function: legitimately settle ultimate purpose/identity conflicts and return binding policy changes to system operation.
- Disturbance / variety regulated: mismatched user requests, model actions and code-project rules; there is no identity-policy adjudication protocol in the shipped flow.
- Decisive decision or feedback right: user input, agent system prompt and flow settings define the immediate task; neither model nor operator-facing runtime shows an explicit ultimate-policy dispute and authoritative ratification path.
- Decision owner: users/config authors set initial goals and constraints, developers maintain the package; no qualifying closed runtime S5 mode is evidenced.
- Supporting / enforcement mechanisms: `system_prompt`, typed action schemas, model/flow config storage, operator project/trajectory controls and fixed resource restrictions.
- Closure path: supplied task/prompt/config → coding actions; missing exceptional identity-policy escalation → legitimate resolution → revised binding governing identity in subsequent operations.
- Why this is / is not agent-owned: a model chooses an action inside its supplied purpose and cannot be credited with legitimate revision of that purpose. Generic user configuration is not `S5=P` without the S5-specific policy loop.
- Evidence: [agent prompt and action schema](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/agent/agent.py#L38-L85), [FlowManager configuration](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/moatless/flow/manager.py#L35-L155), [README user-supplied goal](https://github.com/aorwall/moatless-tools/blob/011ead57a5c81664e9c45e07e1f50b17e695cc63/README.md).
- Basis: bounded negative.
- Confidence: medium-high under the installed framework boundary.
- Caveats: OSS maintainer governance or an embedding application's human policy authority may exist independently, but its policy-decision closure is not wired as a first-party S5 mode here.

### Absence scope

- Surfaces inspected: agent system prompt, component/action schemas, flow/agent/model configuration manager, API/run configuration, project/trajectory control and README governance statements.
- Plausible first-party paths checked: ultimate-purpose arbitration by agent or parent, explicit S5 policy exception escalation, binding dynamic policy updates into subsequent trajectories.
- Why no material first-party path remains: operator settings and static prompt goals do not constitute a closed higher-policy decision-and-return function; no executable identity dispute/ratification path is available.

## Distributed OSS parent arrangement

Moatless is a maintainer-led open-source package, with public experiments and separate evaluation tooling. This is not evidence that maintainers form a first-party, runtime-wired management, adaptation or identity parent for each installed trajectory. No `(P)` state is credited from the existence of authors or external project maintainers.

## Self-hosted and non-human modes

Moatless supports local package use, Docker API/UI, flow configuration and optional worker runners. Configurable completions may use hosted or self-operated models; the code's ownership relation remains one model-chosen action agent inside a specified task. The scheduler's per-project/total concurrent-job limits and human flow configuration are enforcement/config surfaces, not distinct non-human S3 authority or eligible parent-closed S3–S5 modes.

## Recursion

An `ActionAgent` and its actions/tools form one task execution loop. `SearchTree` creates alternative nodes with cloned contexts and optional scalar rewards, not independently viable operational organizations with their own S2–S5; a server with multiple queued trajectories has not thereby established a recursively viable organization.

## Variety and escalation

The task loop attenuates issue-local uncertainty by generating typed actions, executing against the workspace and iterating on observations. Tree-search valuation and Maven compilation feedback alter subsequent **task** exploration. Iteration budgets and scheduler limits enforce static caps. No published path closes inter-operational conflict, whole-current management, complementary S3 audit, future strategic adaptation or ultimate-policy adjudication.

## Evidence gaps

- The frozen first-party release exposes the relevant agent, flow, tree-search and runner source. `S2–S5=—` are bounded standard-distribution conclusions, not proofs that no external orchestration or future release could add these functions.
- Configurable components permit external code to supply a custom selector, value function or strategy, but unimplemented external behavior is not a positive first-party function or an automatic `?`.
- The separate `moatless-tree-search` research repo, SWE-bench evaluation manager and notebook experiments are excluded from this particular coding-trajectory system-in-focus; results/claims from them were not borrowed.
- No LLM-agent, model-provider, benchmark or GUI quality tests were run. Validation is limited to the Index's deterministic script and contract checks.
