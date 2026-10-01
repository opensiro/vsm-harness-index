---
harness_id: agentspex
project_name: AgentSPEX
repository: https://github.com/ScaleML/AgentSPEX
review_ref: db99b7b6802fe15ef2997c82ec1d49e5228128f6
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentSPEX

## Review boundary

- System in focus: one first-party AgentSPEX harness execution at pinned revision `db99b7b6802fe15ef2997c82ec1d49e5228128f6`, including the declarative workflow interpreter, LLM/tool execution loop, supported `simple`/`plan`/`loop` run modes, agentic-loop planner/task-board/plan-execution path, checkpoint/resume/replay support, tools/submodules and sandbox/VM runtime surfaces.
- Purpose and identity: execute reproducible model/tool workflows and, in agentic-loop mode, let an LLM explore a task, decompose it, generate executable plans and drive task completion inside a bounded first-party runtime.
- Relevant environment: users/operators, YAML workflow inputs, configured model/provider endpoints, MCP/tool servers, filesystem/process/network resources, sandbox/VM state and any downstream submodules/tools.
- Standard-distribution boundary: the shipped `src/harness` runtime, execution/interpreter/agentic-loop/checkpoint/submodule surfaces and supported sandbox tools reached by the documented CLI modes are inside. External providers/models and remote MCP/tool services remain dependencies. Repository-development CI, benchmark suites, demos and standalone developer/formal-verification utilities do not donate runtime organizational ownership unless the normal execution path explicitly closes through them.
- Credited operating / distribution surfaces: `README.md`; `src/harness/run.py`; core `AgentSPEX`/LLM execution; `src/harness/agentic_loop/{loop.py,task_board.py,plan_executor.py,verifier.py,tools.py}`; workflow execution/step handlers; checkpoint/resume/replay and supported runtime tools where reached in normal operation.
- Adjacent first-party surfaces excluded from ownership: benchmark evaluators under benchmark/demo trees, application-specific demo reviewers/refiners, repository CI/release machinery, contributor/governance artifacts, dashboard/reporting utilities as independent decision owners, and the standalone Lean `verifier/` package because it is a separately invoked structural-development verifier rather than a mandatory operational feedback channel.
- First-party operating / deployment modes considered: declarative `agentspex run` execution, `simple`, `plan` and `loop` modes, agentic-loop exploration/decomposition/planning/execution, persistent VM/sandbox modes, checkpoint resume and trace replay, sub-workflows/parallel/gather constructs and episodic-memory use.
- Recursion level: one AgentSPEX task execution is the assessed organization. The LLM-driven task/agentic loop is the operational S1. Generated subtasks, YAML steps and parallel branches are work decomposition inside that task unless a separate interacting S1 organization is established.
- Reviewed revision: `db99b7b6802fe15ef2997c82ec1d49e5228128f6`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

AgentSPEX combines a YAML workflow language with a Python execution harness. The documented CLI loads a workflow/configuration and runs the first-party `AgentSPEX` engine. LLM-backed steps execute through the harness and may use tools; deterministic handlers supply control constructs such as conditions, loops, parallel blocks, gather, sub-workflows and variable propagation. Checkpoints, traces and replay provide durable execution/recovery evidence.

The optional agentic-loop mode adds LLM strategic planning around the same execution substrate. Its orchestrator explores the workspace, asks the model to decompose one user objective into subtasks, records those subtasks on a `TaskBoard`, generates plans and executes them through the standard harness before synthesizing a result. The task board and plan machinery track one goal's current work; they do not by themselves create a higher-recursion organization of independent S1 units.

Two verification families were inspected. `agentic_loop/verifier.py` performs pre-execution structural/semantic checks on generated plans so malformed workflow structure is rejected before execution. The top-level Lean `AgentVerifier` converts YAML into a mechanically checked structural graph and explicitly verifies graph/type/read-write properties while not inspecting LLM output content. These are useful correctness gates, but the generic runtime does not establish a complementary operational audit path that independently observes actual S1 behavior and returns findings into subsequent organizational control.

The sandbox VM also includes a file-backed episodic-memory tool with store/get/search/recent operations. It persists information across steps/restarts, while checkpoints and trace replay persist/reconstruct run state. None of these surfaces converts external evidence into a newly generated persistent runtime capability or strategy, so they are context/recovery rather than S4.

## Operational model

A user supplies a goal or workflow plus model/tool configuration. In ordinary execution, model-backed steps choose substantive outputs and tool actions; tool/environment results return through the first-party harness and influence later model turns/steps. In agentic-loop mode the model also explores the task, proposes decomposition and executable plans, while deterministic runtime code validates plans and executes them. Optional user approval in plan mode gates one generated plan before execution. Workflow configuration, limits, tool availability, checkpoints and replay constrain the run but do not themselves own higher VSM decisions.

## S1 — Operations

- State: A
- Function: transform a user task/workflow objective into an answer or tool-mediated environmental result through model-driven reasoning/planning/action with returned execution feedback.
- Disturbance / variety regulated: task ambiguity, workspace/environment state, tool results/errors, model outputs, variable/context state, plan failures and bounded execution conditions encountered while completing one objective.
- Decisive decision or feedback right: choose substantive model outputs, next task actions/tool calls, and in agentic-loop mode the decomposition/plan content used to pursue the current objective.
- Decision owner: the configured autonomous LLM actor invoked by AgentSPEX's first-party execution/agentic-loop paths.
- Supporting / enforcement mechanisms: `AgentSPEX`, LLM executor, workflow interpreter, tool registry/MCP integration, agentic-loop exploration/decomposition/planning, task board, plan verifier/executor, checkpoints, traces, limits and sandbox/runtime support.
- Closure path: user goal/current context → first-party runtime calls the model → model selects output/tool action or task plan → runtime validates/executes permitted work → tool/environment/step results return into workflow/agent context → model revises/continues or synthesizes the final result.
- Boundary reachability: the documented `src/harness/run.py` entry directly selects normal modes or `loop` mode and invokes the shipped runtime. No downstream orchestration package is needed beyond a configured model/provider and external tools.
- Why this is / is not agent-owned: removing the model actor while retaining the deterministic interpreter, plan validator and tool executor removes the substantive task/decomposition/next-action judgment; those host mechanisms enforce or apply decisions rather than substitute the same judgment.
- Evidence: [`README.md`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/README.md); [`src/harness/run.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/run.py); [`src/harness/agent.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agent.py); [`src/harness/agentic_loop/loop.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/loop.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference and external tools may be outside the repository, but the first-party distribution concretely closes their decisions/results inside the supported task execution loop.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 disturbance-attenuation function is established at the assessed task recursion.
- Disturbance / variety regulated: no concrete interaction-generated conflict/oscillation between distinct credited sibling S1 units is established.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: YAML `parallel`, `gather`, `for_each`, sub-workflows, task-board ordering, variable dependencies, isolated sandboxes and concurrency controls can schedule/combine work but do not establish S2 by themselves.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: generated subtasks and branches are decomposition of one objective. The reviewed runtime does not identify peer-S1 interference and feed an attenuation decision back into those peer operations.
- Evidence: [`docs/workflow-language.md`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/docs/workflow-language.md); [`src/harness/agentic_loop/loop.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/loop.py); [`src/harness/agentic_loop/task_board.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/task_board.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: downstream workflows can compose multiple agents, but generic composition/fan-out is not credited without a concrete S2 disturbance-and-attenuation witness owned by AgentSPEX.

### Absence scope

- Surfaces inspected: declarative control-flow language, parallel/gather/submodule handlers, agentic-loop decomposition/task board, tool/MCP execution, sandbox isolation, checkpointing and demo/benchmark multi-step compositions.
- Plausible first-party paths checked: parallel branches as multiple S1s, task-board dependencies as coordination, gather/join as attenuation, submodules as sibling operations and shared variables/workspace as an inter-S1 conflict surface.
- Why no material first-party path remains: these mechanisms sequence, isolate or aggregate one task's work. No supported path supplies two distinct coupled operational S1 units plus a specific interaction disturbance, S2-specific attenuation relation and returned feedback changing later peer behavior.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control function is established above the single task/workflow organization.
- Disturbance / variety regulated: current subtask state, step dependencies, retries, plan validity, token/tool limits, checkpoints and optional plan approval are regulated locally within one objective rather than through a higher whole-organization control loop.
- Decisive decision or feedback right: no distinct whole-system judgment over current resources, commitments, priorities, constraints or cross-S1 intervention is established at the declared recursion.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: task board, generated plan, deterministic interpreter/control flow, plan verifier, configuration limits, checkpoint/resume, user plan approval and execution lifecycle events.
- Closure path: not applicable for the negative finding.
- Whole-system current view: `TaskBoard` exposes the current decomposition/status/results for one user objective, but that is the operating agent's own task state rather than a distinct metasystem view over multiple autonomous operational commitments.
- Current-control decision scope: current plan/subtask sequencing and bounded execution of one task; no separate current resource/commitment authority at a higher recursion is established.
- Why this is / is not agent-owned: LLM decomposition/planning is part of S1 task pursuit. Deterministic status tracking, workflow scheduling and a human approval gate do not establish a separate S3 function or parent S3 mode.
- Evidence: [`src/harness/agentic_loop/loop.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/loop.py); [`src/harness/agentic_loop/task_board.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/task_board.py); [`src/harness/agentic_loop/plan_executor.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/plan_executor.py); [`src/harness/run.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/run.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the word “plan” or task-board visibility is not treated as S3 when it is internal decomposition/control of one S1 objective.

### Absence scope

- Surfaces inspected: agentic-loop planner/decomposer/task board, plan execution/verification, workflow scheduler/control handlers, concurrency/limits, checkpoints/resume/replay, dashboard/events and user plan-approval mode.
- Plausible first-party paths checked: task board as whole-system control, planner as S3 manager, user plan approval as parent S3, parallel branch scheduling as resource control, retry/checkpoint machinery as intervention and dashboard/trace state as a current-control surface.
- Why no material first-party path remains: reviewed paths regulate the internals/lifecycle of one task execution or expose observation/approval for it. No distinct higher-recursion owner observes a set of autonomous S1 commitments and returns a substantive current resource/priority/commitment decision.

## S3* — Complementary audit

- State: —
- Function: no material complementary operational-audit loop is established at the standard runtime boundary.
- Disturbance / variety regulated: structural workflow defects and ordinary runtime errors are checked/recorded, but no independent path is shown auditing actual operating claims and returning complementary findings into later organizational control.
- Decisive decision or feedback right: no qualifying independent audit judgment-and-return right is established.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: agentic-loop `PlanVerifier`, standalone Lean AgentVerifier, checkpoints/traces/replay, dashboard/structured events, benchmark evaluators and demo-specific reviewers/refiners.
- Closure path: not applicable; no standard runtime path closes ordinary operational evidence → complementary independent access → audit finding → returned corrective/control decision.
- Claim being audited: not established as a runtime organizational claim distinct from ordinary execution validity.
- Ordinary reporting path: model/workflow outputs, tool results, task-board/status events and execution traces.
- Complementary access path: no qualifying standard operational path established. PlanVerifier and Lean verification inspect plan/workflow structure rather than independently observing actual S1 behavior.
- Independence boundary: not established for a runtime audit loop. Benchmark/demo evaluators may have separate criteria but are adjacent application/evaluation systems rather than a generic standard runtime feedback owner.
- Who acts on findings: no qualifying complementary findings path is established; structural validation blocks malformed plans before execution and ordinary runtime errors remain on the normal control path.
- Why this is / is not agent-owned: structural verification and telemetry can support correctness/observability but do not establish the S3* function without an independent observation/claim path and return closure.
- Evidence: [`src/harness/agentic_loop/verifier.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/verifier.py); [`verifier/README.md`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/verifier/README.md); [`src/harness/run.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/run.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the standalone Lean verifier can prove structural graph properties and a downstream benchmark can separately grade an AgentSPEX workflow, but neither is credited as a standard complementary operational feedback loop at this boundary.

### Absence scope

- Surfaces inspected: pre-execution PlanVerifier, top-level Lean AgentVerifier, checkpoint/trace/replay, dashboard/events/logging, benchmark evaluation folders and demo-specific reviewer/refiner workflows.
- Plausible first-party paths checked: structural plan verification as audit, Lean theorem checking as complementary access, trace replay as independent reconstruction, benchmark graders as runtime audit and demo reviewers as reusable S3*.
- Why no material first-party path remains: the two verifier families validate static/generated workflow structure before execution; telemetry/replay follows the ordinary execution path; benchmark/demo reviewers are adjacent application/evaluation compositions. No standard generic runtime mode supplies independent operational observation plus findings returned into subsequent S1/control behavior.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established that turns prior environmental evidence into a persistent changed AgentSPEX capability or control strategy for later operation.
- Disturbance / variety regulated: current task state, stored episodic information, checkpoints, trace data and within-task planning can influence continued work, but no distinct future-facing capability adaptation is generated and durably applied.
- Decisive decision or feedback right: no first-party actor is established selecting a persistent future runtime/harness change from accumulated external evidence.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: episodic memory store/search/retrieve, checkpoints, resume, trace replay, workspace state, LLM plan revision and reusable YAML/submodule definitions.
- Closure path: not applicable; no observed external evidence → prospective adaptation option → durable capability/strategy mutation → later operation path is established.
- Why this is / is not agent-owned: memory and recovery preserve information/current work; planner revisions pursue the current objective. They do not modify the future harness or generate a persistent adaptation option from environmental evidence.
- Evidence: [`src/sandbox_vm/tools/memory/episodic.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/sandbox_vm/tools/memory/episodic.py); [`src/harness/run.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/run.py); [`src/harness/agentic_loop/loop.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/agentic_loop/loop.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: persistent episodic data can improve later context if a workflow chooses to retrieve it, but Methodology 0.3.6 does not equate durable memory/context reuse with S4 capability adaptation.

### Absence scope

- Surfaces inspected: episodic memory, checkpoints/durable execution, trace/replay, agentic-loop plan revision, YAML/submodules, tools, workspace persistence, benchmark/demo learning-looking surfaces and configuration.
- Plausible first-party paths checked: memory as learned capability, checkpoints/replay as adaptation, task-board history as organizational learning, plan revision as future strategy change and demo-specific refinement/reviewer loops as core self-improvement.
- Why no material first-party path remains: stored data/state is retrieved or resumed, while model planning adapts only within the current task. No normal core path autonomously converts external evidence into a new persistent harness/tool/policy/strategy that later executions load as changed capability.

## S5 — Policy and identity

- State: —
- Function: no closed first-party runtime loop is established for deciding or reaffirming AgentSPEX's ultimate identity, purpose or foundational policy.
- Disturbance / variety regulated: YAML/system prompts, tool availability, model/configuration, runtime limits, sandbox constraints and optional user plan approval shape operation, but they are externally authored inputs/gates.
- Decisive decision or feedback right: no first-party actor receives an identity/ultimate-policy issue and returns an authoritative foundational decision governing subsequent operation.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: workflow configuration, system prompts, tool/MCP registration, environment variables, sandbox/VM restrictions, plan approval and structural workflow validation.
- Closure path: not applicable; no identity/policy issue → legitimate ultimate authority → authoritative decision → returned operation path is established.
- Why this is / is not agent-owned: the LLM can plan/decompose work within a supplied objective and workflow/tool boundary, but no supported path lets it own the mandate itself. Human approval of one plan is a bounded action gate rather than a runtime S5 identity-policy loop.
- Evidence: [`README.md`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/README.md); [`src/harness/run.py`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/src/harness/run.py); [`docs/workflow-language.md`](https://github.com/ScaleML/AgentSPEX/blob/db99b7b6802fe15ef2997c82ec1d49e5228128f6/docs/workflow-language.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: strong static rules/configuration and human gating can enforce policy but do not establish ownership of ultimate policy/identity under the Profile closure test.

### Absence scope

- Surfaces inspected: workflow/system configuration, agentic-loop prompts/goals, tool/MCP permissions, sandbox limits, user plan approval, structural verifier policy, environment variables, repository governance and supported run modes.
- Plausible first-party paths checked: planner changing its mandate, plan approval as parent S5, YAML as identity authority, tool permissions as ultimate policy, verifier rules as policy governance and repository maintainers as runtime parent authority.
- Why no material first-party path remains: foundational objectives/configuration are supplied before execution and enforced by deterministic runtime boundaries. No first-party runtime process escalates a foundational policy/identity question to a legitimate authority and returns a new authoritative mandate into operation.

## Distributed OSS parent arrangement

Repository maintainers govern AgentSPEX development/releases, while each user/operator supplies workflows, providers, tools and runtime configuration. That OSS governance is adjacent to an executing task and is not imported as parent S3/S4/S5 ownership without a function-specific runtime return loop. No parent modifier is claimed.

## Self-hosted and non-human modes

AgentSPEX supports local/container/VM-oriented execution and can run model/tool workflows or the agentic loop without continuous human involvement. Optional plan-mode approval introduces a bounded pre-execution human gate; it does not create a complete parent S3 or S5 mode.

## Recursion

At the assessed recursion, one task/workflow execution is the organization. LLM reasoning/planning/tool work closes S1. Generated subtasks, parallel blocks and submodules remain decomposition/composition within that S1 unless independent interacting operational units and a higher regulation loop are separately established. Static verification, memory and observability are support mechanisms rather than independent higher VSM functions.

## Variety and escalation

AgentSPEX absorbs task variety through LLM planning/reasoning, tools, sub-workflows and flexible control flow while deterministic schema/plan verification, limits, sandboxing, checkpoints and replay bound execution failures. Current problems can cause plan revision, retry or resume inside the same task. The reviewed distribution does not escalate these into separate S2/S3/S3*/S4/S5 organizational loops.

## Evidence gaps

- S2 is not inferred from `parallel`, `gather`, submodules or task decomposition.
- S3 is not inferred from the task board, planner, current workflow state or one-plan human approval.
- S3* is not inferred from structural PlanVerifier/Lean checks, traces/replay or adjacent benchmark/demo evaluators because no standard complementary operational observation-and-return loop is established.
- S4 is not inferred from episodic memory, checkpoints, replay or within-task plan revision because no persistent capability adaptation from external evidence closes.
- S5 is not inferred from YAML/system prompts/tool boundaries/static verification or bounded human approval because no identity/ultimate-policy authority loop closes.
