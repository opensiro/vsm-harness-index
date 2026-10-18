---
harness_id: os-copilot
project_name: OS-Copilot / FRIDAY
repository: https://github.com/OS-Copilot/OS-Copilot
review_ref: f720af8807e49a92dda64572d2c6bc6c0ac7ee7e
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# OS-Copilot / FRIDAY

## Review boundary

- System in focus: one installed first-party OS-Copilot / FRIDAY runtime at pinned revision `f720af8807e49a92dda64572d2c6bc6c0ac7ee7e`, considered across its documented task-execution and self-learning operating modes so that reusable capability change can be observed across separate tasks.
- Purpose and identity: accept general computer tasks, plan and execute OS/application actions, recover from task-local failures, and optionally expand the reusable tool repertoire through the shipped self-learning workflow.
- Relevant environment: user-supplied tasks and learning targets; the operating system and filesystem; external applications/web/APIs; model/embedding providers; software packages such as `openpyxl`; demo files and other task artifacts.
- Standard-distribution boundary: `oscopilot/agents/`, first-party planner/executor/retriever/learner modules, execution environments, generated-tool repository/manager, `quick_start.py`, `course_learning.py`, and documented shipped examples/tutorials at the reviewed revision. External model providers, OS/application implementations, third-party APIs/packages and user task intent remain environment/inputs.
- Credited operating / distribution surfaces: `oscopilot/agents/friday_agent.py`; `oscopilot/agents/self_learning.py`; `oscopilot/modules/planner/friday_planner.py`; `oscopilot/modules/executor/friday_executor.py`; `oscopilot/modules/retriever/vector_retriever.py`; `oscopilot/modules/learner/self_learner.py`; `oscopilot/tool_repository/manager/tool_manager.py`; `course_learning.py`; and the documented self-learning tutorial.
- Adjacent first-party surfaces excluded from ownership: repository tests/benchmarks, contributor/project governance, frontend presentation code except as an invocation surface, and experimental/example variants not needed to establish the standard FRIDAY functional paths.
- First-party operating / deployment modes considered: normal `FridayAgent.run(task)` operation; generated Python/Shell/AppleScript/API/QA actions with model-driven repair/replanning; persistent generated-tool retrieval; and the supported `course_learning.py` self-learning mode that changes capabilities used by later tasks.
- Recursion level: one FRIDAY installation across tasks is the system-in-focus. A single user task is an operational episode inside that system. Planner/executor/retriever/learner modules are subfunctions, not separate S1 organizations merely because they have distinct module names.
- Reviewed revision: `f720af8807e49a92dda64572d2c6bc6c0ac7ee7e`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OS-Copilot ships the runnable FRIDAY computer agent rather than only an API/schema or benchmark. `FridayAgent.run()` resets the plan, decomposes the user task, executes the resulting subtasks and returns each execution state into a self-refinement loop. Python, Shell and AppleScript operations are judged from actual code/output/error/filesystem state. The agent may amend generated code or replan the remaining task graph, then execute again. Successful Python tools above the configured score threshold are persisted into the generated-tool repository.

The planner/judge/repair surfaces do not by themselves create higher VSM functions. They regulate the current operational task from inside the same FRIDAY action loop. There is no distinct whole-installation current-control actor with a management view over multiple first-party S1 operations, and the judge is built from the same ordinary module/model configuration rather than an independent complementary audit channel.

The self-learning mode is materially different from task-local repair. `course_learning.py` instantiates the same FRIDAY runtime together with a first-party `SelfLearner` and invokes continuous learning for a user-selected software/package/demo context. The learner model designs new course content from that external context and prior completed lessons. `SelfLearning.learn_course()` runs those prospective lessons through FRIDAY. When those lesson tasks generate successful Python capabilities, the ordinary execution path persists them in the generated-tool repository and vector index; later ordinary tasks automatically retrieve those persisted tools by similarity. The shipped tutorial demonstrates the closure explicitly: FRIDAY initially cannot complete an Excel task, learns `openpyxl` capabilities, then succeeds when the original task is rerun.

This is treated as S4 rather than generic memory because the path creates executable future capability and returns it into later S1 behavior. The operator chooses the broad learning domain/package, analogous to supplying an adaptation problem, while the first-party model chooses the course/lessons and FRIDAY implements the resulting reusable tools. The decisive adaptation-option and implementation path is therefore agent-owned in the supported learning mode rather than merely exposed as a constructor hook.

Primary evidence:

- [`README.md`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/README.md) — runnable FRIDAY computer-agent distribution and documented self-learning tutorial/operating surface.
- [`oscopilot/agents/friday_agent.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py) — task planning/execution, result-conditioned judging, repair/replanning and successful-tool persistence.
- [`oscopilot/modules/planner/friday_planner.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py) — model-driven task decomposition/replanning and dependency ordering.
- [`oscopilot/modules/executor/friday_executor.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py) — generated-code execution, in-band judgment/repair and persistent tool storage.
- [`oscopilot/agents/self_learning.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py) and [`oscopilot/modules/learner/self_learner.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/learner/self_learner.py) — model-authored course generation from software/package/demo/prior-course context and execution of generated lessons through FRIDAY.
- [`oscopilot/tool_repository/manager/tool_manager.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py) and [`oscopilot/modules/retriever/vector_retriever.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/retriever/vector_retriever.py) — persistence/vectorization and automatic retrieval of learned tools in later tasks.
- [`docs/source/tutorials/self_learning.rst`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/docs/source/tutorials/self_learning.rst) — documented before/learn/after capability demonstration.

## Operational model

A normal task starts with a user objective. FRIDAY retrieves relevant persisted tools, decomposes the objective into a dependency graph, then iterates over executable subtasks. The executor may generate code or API operations, executes them against the OS environment and returns result/error/filesystem state. The same operational loop judges the result, repairs code or replans when necessary and updates the task graph. Successful generated Python tools can be stored for later use.

A separate supported learning mode accepts a software/package/domain context and optional demo file. The learner model generates a prospective curriculum; FRIDAY executes each lesson using its normal S1 machinery. Successful capabilities are persisted into the same tool repository/vector database used by the ordinary retriever. Consequently, a later unrelated task episode can start with an expanded action repertoire.

## S1 — Operations

- State: A
- Function: autonomously plan and execute concrete computer/OS/application work needed to satisfy a user task, adapting task-local actions to returned execution state.
- Disturbance / variety regulated: heterogeneous user goals, available tools, filesystem/application state, generated-code failures, missing intermediate operations, execution outputs/errors and changing prerequisites within a task.
- Decisive decision or feedback right: choose/decompose the next substantive computer actions, generate or select executable tools, interpret returned execution state and decide whether to continue, amend or replan the active task.
- Decision owner: first-party model-driven FRIDAY planner/executor/judge path.
- Supporting / enforcement mechanisms: tool retrieval, dependency graph/topological ordering, Python/Shell/AppleScript/API execution environments, bounded repair iterations, task state, generated-tool repository and deterministic loop/control plumbing.
- Closure path: user task -> model decomposes/selects actions -> generated/retrieved tool executes against OS/application environment -> result/error/filesystem state returns -> model judges/replans/repairs -> changed action executes -> task state updates.
- Boundary reachability: `quick_start.py` and documented examples instantiate `FridayAgent`, while `FridayAgent.run()` directly invokes the credited planner/executor/refinement path.
- Why this is / is not agent-owned: deterministic code transports state and executes selected code, while substantive task decomposition, tool generation, result judgment, amendment and replanning choices are model-driven.
- Evidence: [`README.md`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/README.md); [`oscopilot/agents/friday_agent.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py); [`oscopilot/modules/planner/friday_planner.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py); [`oscopilot/modules/executor/friday_executor.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the README notes single-round conversation, but the internal execution of one task is multi-step and result-conditioned; conversational turn count does not break the operational loop.

## S2 — Coordination

- State: —
- Function: no material first-party S2 path regulating a concrete disturbance between distinct autonomous S1 units is established at the declared FRIDAY-installation recursion.
- Disturbance / variety regulated: the planner orders dependencies among subtasks and modules exchange artifacts, but those subtasks/modules are components of one operational agent rather than separately accountable S1 units producing an inter-operation oscillation/interference problem.
- Decisive decision or feedback right: none established for inter-S1 coordination.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: dependency graph, topological ordering, prerequisite-result passing, shared tool repository and sequential subtask loop.
- Closure path: task decomposition creates ordered work inside S1, but no distinct S1-A/S1-B interaction disturbance -> coordinating judgment -> changed later behavior of those S1 units loop closes.
- Why this is / is not agent-owned: sequencing dependencies is operational planning, not evidence of the VSM S2 organizational function.
- Evidence: [`oscopilot/agents/friday_agent.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py); [`oscopilot/modules/planner/friday_planner.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a deployment containing several separately accountable FRIDAY instances could create an S2 problem, but that is a different system-in-focus.

### Absence scope

- Surfaces inspected: FRIDAY agent loop, planner graph/dependencies, executor, retriever/tool repository, self-learning module and shipped examples.
- Plausible first-party paths checked: planner as coordinator; topological sorting; multiple subtasks; planner/executor/retriever module interaction; learning lessons; shared tool repository.
- Why no material first-party path remains: all checked paths compose a single S1 operation/capability or order its internal work rather than attenuating conflict/oscillation among distinct first-party S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no distinct first-party whole-system current-control function over multiple or separately managed operational units is established.
- Disturbance / variety regulated: task-local execution failures, weak outputs and missing prerequisites are regulated, but they are handled inside the same S1 episode that performs the work.
- Decisive decision or feedback right: no separate actor is evidenced with authority to form a whole-installation current view and intervene in the present operational organization beyond the active task-local plan/repair loop.
- Decision owner: none established for S3; FRIDAY's planner/judge retains task-local S1 action authority.
- Supporting / enforcement mechanisms: in-band `judge_tool`, repair loop, replanning, task graph/status, score threshold and bounded repair count.
- Closure path: execution state -> same operational agent judges/repairs/replans -> same task continues; this closes S1 recovery, not a separate management loop over the current whole.
- Why this is / is not agent-owned: model-driven replanning is real discretion, but its organizational function is local task execution/recovery rather than whole-system current control.
- Evidence: [`oscopilot/agents/friday_agent.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py); [`oscopilot/modules/executor/friday_executor.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py); [`oscopilot/modules/planner/friday_planner.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: names such as planner or orchestrating agent are not promoted to S3 without a whole-system current-view/current-control witness.

### Absence scope

- Surfaces inspected: task loop, planner/replanner, execution judgment/repair, score thresholds, tool manager and self-learning orchestration.
- Plausible first-party paths checked: planner as manager; judge as current controller; repair/replan as intervention; tool manager as resource manager; self-learning driver as manager.
- Why no material first-party path remains: each path either executes/repairs the active task, stores/retrieves capabilities or adapts future capability; none owns a distinct whole-system current-control closure.

## S3* — Complementary audit

- State: —
- Function: no first-party independent complementary-audit channel with distinct access/judgment and corrective return is established.
- Disturbance / variety regulated: FRIDAY evaluates generated code/output and may repair or replan, but this is ordinary in-band operational verification.
- Decisive decision or feedback right: no independent auditor is evidenced with a separate claim-checking path over operational reality.
- Decision owner: none established for S3*; `judge_tool` uses the ordinary executor module/model configuration inside the same task loop.
- Supporting / enforcement mechanisms: LLM judgment prompt, execution result/error/filesystem observations, score threshold and repair/replan path.
- Closure path: operation -> same in-band executor/judge evaluates -> same agent repairs/replans -> operation continues; no independent complementary path returns findings to a separate corrective owner.
- Why this is / is not agent-owned: semantic judging exists, but independence/complementary access required for S3* is absent.
- Evidence: [`oscopilot/modules/executor/friday_executor.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py); [`oscopilot/modules/base_module.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/base_module.py); [`oscopilot/agents/friday_agent.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: calling the component a judge or critic does not satisfy S3*; no separate reviewer/model/provider/evidence channel comparable to an independent audit path is configured by the standard runtime.

### Absence scope

- Surfaces inspected: executor judgment/repair, BaseModule model construction, planner/replanner, self-learning evaluation and repository tests/examples.
- Plausible first-party paths checked: `judge_tool`; score threshold before tool storage; repair loop; task completion checks; tests/benchmarks as possible auditors.
- Why no material first-party path remains: runtime checking is in-band and shares the ordinary module/model/environment path; development tests/benchmarks are outside the assessed runtime organization.

## S4 — Outside-and-then intelligence

- State: A
- Function: generate and implement prospective reusable computer capabilities from external software/package/demo context so later operational tasks can perform work the current repertoire could not.
- Disturbance / variety regulated: capability gaps exposed by unfamiliar software/application domains, new packages/APIs and task classes not covered by the existing generated-tool repository.
- Decisive decision or feedback right: choose a prospective course/lesson set for the selected external software/package context and, through lesson execution, generate reusable tools that expand the future action repertoire.
- Decision owner: first-party `SelfLearner` model for course design plus the model-driven FRIDAY lesson execution path that produces qualifying reusable tools.
- Supporting / enforcement mechanisms: software/package/demo inputs, prior-course history, model-authored course JSON, `SelfLearning.learn_course`, ordinary FRIDAY task execution, score threshold, persistent generated-tool files/JSON/Chroma vector database and retriever similarity search.
- Closure path: operator identifies a capability domain -> learner reads software/package/demo/prior-course context -> model designs prospective lessons -> FRIDAY executes lessons -> successful generated Python capabilities are persisted -> later ordinary task queries the same repository -> newly learned tool descriptions/code are retrieved and influence execution -> previously unsupported task becomes executable.
- Boundary reachability: `course_learning.py` is a shipped first-party entrypoint documented by the self-learning tutorial; no downstream code changes or custom orchestration are required to create and reuse the adapted capability.
- Why this is / is not agent-owned: the operator selects the broad learning target, while the first-party model determines the course/lessons and FRIDAY generates/qualifies the executable tools; deterministic repository code only persists and retrieves those chosen capabilities.
- External distinction: software/package context and optional demo-file contents describe capabilities outside FRIDAY's existing action repertoire; the documented example uses the external `openpyxl` library and an Excel file.
- Future / prospective distinction: the learning mode is explicitly run to acquire tools for later tasks, rather than only repairing the presently failing task; its persisted output survives the learning episode and is queried in subsequent task planning/execution.
- Adaptation option generated: a model-authored course of new capability lessons and the reusable generated tools produced by executing those lessons.
- Path back into current capability / S3: qualifying tools are written into `generated_tools.json`, code/description files and the persistent vector index; ordinary `FridayRetriever` then automatically retrieves them for later S1 task planning/code generation, changing the executable repertoire without repository-source modification.
- Evidence: [`course_learning.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/course_learning.py); [`oscopilot/agents/self_learning.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py); [`oscopilot/modules/learner/self_learner.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/learner/self_learner.py); [`oscopilot/modules/executor/friday_executor.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py); [`oscopilot/tool_repository/manager/tool_manager.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py); [`oscopilot/modules/retriever/vector_retriever.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/retriever/vector_retriever.py); [`docs/source/tutorials/self_learning.rst`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/docs/source/tutorials/self_learning.rst).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: self-learning is a separate supported operating mode rather than automatically triggered from every failed task. That affects invocation, not ownership of the adaptation option once the mode is invoked. The broad learning domain/package remains operator-supplied and is not treated as autonomous S5 policy.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy adjudication loop is established.
- Disturbance / variety regulated: user task, model/provider settings, score/repair limits, available tools and self-learning domain inputs constrain behavior, but they are task/configuration/capability controls rather than organizational identity or ultimate-policy decisions.
- Decisive decision or feedback right: none established for defining/reconciling FRIDAY's identity, ultimate purpose or legitimate highest-level policy under competing operational/adaptation demands.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: environment/configuration, prompts, thresholds, user task/learning inputs and static runtime structure.
- Closure path: configuration/task inputs directly constrain S1/S4 behavior; no identity-level issue -> legitimate ultimate authority -> authoritative policy decision -> returned governance loop is evidenced.
- Why this is / is not agent-owned: FRIDAY exercises operational and capability-adaptation discretion, but not authority to redefine its own organizational identity or ultimate policy.
- Evidence: [`README.md`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/README.md); [`oscopilot/modules/base_module.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/base_module.py); [`oscopilot/agents/friday_agent.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py); [`course_learning.py`](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/course_learning.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: user-supplied objectives/learning targets are parent inputs, but ordinary task/capability target selection is not S5=P without an identity/ultimate-policy function.

### Absence scope

- Surfaces inspected: README/quickstart, FRIDAY task loop, prompts/configuration, planner/executor/retriever, tool repository, self-learning entrypoint/module and tutorials.
- Plausible first-party paths checked: system prompt as policy; user task as purpose; tool score/repair thresholds as policy; self-learning target as identity change; project governance.
- Why no material first-party path remains: these paths define tasks, execution constraints or capability adaptation rather than a runtime identity/ultimate-policy authority and closure.

## Recursion

The system-in-focus is one FRIDAY installation across task episodes because the persistent generated-tool repository carries capability between runs. Individual subtasks and planner/executor/retriever/learner modules are not treated as separate viable organizations. S1 is the task-execution loop; the supported learning mode operates as S4 by changing the repertoire available to later S1 episodes. No separate S2/S3/S3*/S5 closures are established at this recursion.

## Variety and escalation

Task-local variety returns through concrete execution results/errors and is attenuated inside S1 by model judgment, repair and replanning. When an installed capability is absent, the supported learning mode can address the broader capability gap prospectively: external package/demo context is converted into a curriculum, lesson execution generates reusable tools, and those tools become retrievable in later operations. No distinct current-management, complementary-audit or identity-policy escalation owner was established.

## Evidence gaps

- Structural review only; no new FRIDAY or self-learning run was executed.
- The documented self-learning example establishes cross-task capability change, but the exact tools generated are stochastic.
- S4 is credited from the explicitly supported learning mode; ordinary `FridayAgent.run()` does not automatically launch that mode when a task fails.
- Self-learning currently receives operator-selected software/package/demo context. This assessment credits agent ownership of the generated adaptation option/course/tool implementation, not autonomous choice of the system's ultimate learning agenda.
- No evidence was found for an independent runtime verifier/auditor or a separate whole-installation current-control actor at the frozen revision.