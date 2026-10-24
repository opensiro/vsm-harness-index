---
harness_id: fractale
project_name: fractale
repository: https://github.com/converged-computing/fractale
review_ref: b62ff1bce01e191828b90c5fa468f81197629e32
reviewed_at: 2026-10-17
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

# fractale

## Review boundary

- System in focus: The frozen, installable fractale Python CLI and native state-machine orchestration system, including its in-repository model-driven WorkerAgent, ManagerAgent, HelperAgent, first-party Plan/Step compilation, state transition execution, MCP/local-tool dispatch and result tracking. The scientific/HPC task domain is the environment, not evidence of a separate organizational recursion.
- Purpose and identity: Execute user-supplied or dynamically generated scientific/MCP workflows through a first-party model/tool-feedback agent loop, with explicit plan-state transitions and optional specialist endpoints.
- Relevant environment: User and scientific task requirements; local/remote MCP tools and prompts; provider-hosted models; scientific/HPC schedulers, research systems and external tools; runtime errors and step outputs.
- Standard-distribution boundary: Shipped `fractale run`, `fractale prompt` and `fractale agent` CLI paths, installed native Engine, Plan/Step/Manager/Worker and model-backend interfaces; optional configured MCP endpoint and local registry. No credit for a separately deployed MCP server's own agent, an external scientific service or the vendor model internals.
- Credited operating / distribution surfaces: [fractale/cli/run.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/run.py), [fractale/cli/prompt.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/prompt.py), [fractale/cli/agent.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/agent.py), [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py), [fractale/engines/native/state_machine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/state_machine.py), [fractale/engines/native/agent/worker_agent.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/agent/worker_agent.py), [fractale/agents/manager.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/manager.py), [fractale/agents/base.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/base.py), [fractale/core/plan/plan.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/plan/plan.py), [fractale/core/plan/step.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/plan/step.py).
- Adjacent first-party surfaces excluded from ownership: Research/usage examples and sample YAML workflows demonstrate interfaces but do not prove unobserved independent audit, policy authority or future adaptation; CLI documentation is corroborating only; provider libraries and tool-serving MCP projects remain external. No benchmark results or live scientific job success attributed.
- First-party operating / deployment modes considered: Direct human-authored `fractale run` Plan with prompt/tool/agent steps; `fractale prompt` convenience path; `fractale agent` planner-mediated specialist task; optional interactive human plan approval; configured Gemini or OpenAI-compatible model backend and local/remote MCP tools.
- Recursion level: One fractale-managed scientific task/workflow. Specialist/tool executions can be delegated, but external MCP-hosted agent internals and HPC systems do not become in-scope lower-level first-party VSM functions merely through the adapter.
- Reviewed revision: `b62ff1bce01e191828b90c5fa468f81197629e32` (candidate intake #186, assessment batch #1648).
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI entry point selects `get_engine()` for a user plan or prompt, supplying backend configuration, maximum attempts and a database adapter. The native `Manager` loads/validates available MCP tools/prompts, constructs a `WorkflowStateMachine`, and repeatedly evaluates step callbacks until terminal state or the configured loop bound. `Plan` compiles YAML into typed Step states, transitions, defaults and validation. For `prompt` steps the engine instantiates `WorkerAgent`; for `tool` and `agent` types it invokes the tool/agent endpoint (the latter is treated as a tool call), records result and determines a transition from explicit rules or a model-based result classifier. [fractale/cli/run.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/run.py); [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py); [fractale/engines/native/state_machine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/state_machine.py); [fractale/core/plan/plan.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/plan/plan.py).

The first-party `WorkerAgent.process_loop` sends instructions to its configured LLM backend, receives model-selected tool calls, invokes them using the first-party local registry or remote MCP client and returns tool observations as context for further model decisions. It can return on explicit transition rules, final model content or the loop limit. This is an actual implemented agentic operation path **without assuming** any external MCP server or vendor API supplies an already-built agent harness. [fractale/engines/native/agent/worker_agent.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/agent/worker_agent.py); [fractale/agents/base.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/base.py); [fractale/agents/backends/backend.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/backends/backend.py).

Dynamic `plan` steps delegate to `ManagerAgent` for tool-informed, model-generated Step specifications; the path validates generated steps and asks the user to accept the plan. Explicit rule matches and model result checks route to success/failure transitions. State-machine loop and result persistence are first-party bookkeeping/enforcement, **not by themselves an additional S3, S3*, S4 or S5 owner**. Other models and scientific programs remain configured execution dependencies. [fractale/agents/manager.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/manager.py); [fractale/engines/native/state_machine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/state_machine.py); [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py); [fractale/db/memory.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/db/memory.py).

## Operational model

A user invokes a pinned CLI workflow or asks for a prompt/specialist task; fractale resolves the required engine and configured model, obtains tool/prompt descriptions, executes a model-driven worker step or model-assisted planning step, routes actual tool calls, feeds observations into the next decision, and records step transitions and final outputs. A user can accept/reject a generated plan before continuation. Supported program paths demonstrate viability at the code level; **this assessment does not claim a provider-backed live run or successful HPC job**. A model's choice of a scientific command is an S1 task decision; a deterministic FSM's switch among next states is not automatically organization-wide S3. [README.md](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/README.md); [fractale/engines/native/agent/worker_agent.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/agent/worker_agent.py); [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py).

## S1 — Operations

- State: A
- Function: Model-guided execution of a scientific/MCP task through repeated task decisions, tool interactions, observations and continuation.
- Disturbance / variety regulated: Task-specific natural-language requirements, incomplete scientific/tool information, failed or changed tool observations and the need to select further operations.
- Decisive decision or feedback right: Within the configured instruction/tool scope, the first-party WorkerAgent-connected model decides whether and which tools to invoke, supplies tool arguments and determines subsequent response or continuation from returned observations. Human-authored plan bounds remain separate.
- Decision owner: fractale's own installed model-driven WorkerAgent loop; remote provider supplies inference but not a separately authored harness-level decision loop.
- Supporting / enforcement mechanisms: Plan/Step configuration, AgentBase local/MCP tool dispatch and schema discovery, backend selection, max iterations, state transitions and result storage.
- Closure path: task instruction → configured LLM action/tool selection → first-party tool dispatch → tool result returned to backend context → next choice/final output → next workflow step/recorded result.
- Boundary reachability: `fractale run` constructs the first-party native Engine, `prompt` or planned `prompt` steps call `Manager.run_prompt`, and that instantiates and runs in-repo WorkerAgent; `fractale prompt` is also a supported CLI route. No separate external agent process is needed to supply the first-party loop.
- Why this is / is not agent-owned: The LLM picks concrete operations and iterative continuation in first-party code, rather than the FSM merely replaying fixed commands. The outside model's weights and the remote MCP server's tool implementations are not borrowed VSM actors.
- Evidence: [fractale/cli/run.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/run.py); [fractale/cli/prompt.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/prompt.py); [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py); [fractale/engines/native/agent/worker_agent.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/agent/worker_agent.py); [fractale/agents/base.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/base.py); [fractale/tools/calls.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/tools/calls.py).
- Basis: Explicit first-party source trace, structurally installed model/tool-feedback cycle.
- Confidence: High for reachable model-controlled S1 path; no first-party live scientific run witnessed.
- Caveats: Requires a configured provider and supporting tool environment for practical scientific commands; a plain tool-only plan is less autonomous, and external specialist reasoning is not inherited.


## S2 — Coordination

- State: —
- Function: No separate first-party attenuation loop for actual conflict/oscillation among distinct S1 units was established.
- Disturbance / variety regulated: Possible ordering and handoff errors among plan steps; these are task sequencing, not demonstrated inter-S1 interference.
- Decisive decision or feedback right: No S2-specific choice about competing independent work units shown; the FSM chooses transitions for one plan.
- Decision owner: Plan author, deterministic engine and per-step model worker for their own scopes; no distinct S2 owner.
- Supporting / enforcement mechanisms: Step graph, default transitions, endpoint registry and output reference mapping.
- Closure path: Step output can inform a following step, but no separate interference diagnosis, corrective coordination and subsequent multi-S1 feedback path is evidenced.
- Why this is / is not agent-owned: Several named manager/worker/specialist roles do not show mutual operational interference or compensating coordination; a sequential graph is not independently sufficient.
- Evidence: [fractale/core/plan/plan.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/plan/plan.py); [fractale/engines/native/state_machine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/state_machine.py); [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py); [fractale/core/plan/step.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/plan/step.py).
- Basis: Bounded negative structural review of core plan, native engine and agent/endpoint dispatch.
- Confidence: Medium-high within shipped native runtime.
- Caveats: A separately deployed MCP agent may coordinate its own workers, but is not credited to fractale.

### Absence scope

- Surfaces inspected: Plan compilation, native FSM, Manager/Worker/Helper implementation, typed agent/tool steps, MCP and local tool registry paths.
- Plausible first-party paths checked: Multiple Step agents, a manager plus workers, reusable specialist endpoints, state transitions and results passing.
- Why no material first-party path remains: The inspected shipped paths schedule/serialize/delegate work in one workflow without observing and regulating distinct S1 units' inter-operation interference and corrective feedback.


## S3 — Inside-and-now control

- State: —
- Function: No separately established whole-system current-resource/commitment regulation was found at the declared fractale workflow recursion.
- Disturbance / variety regulated: Current task progression, tool failures and individual plan amendments, handled by task execution, fixed state transitions and operator interactions.
- Decisive decision or feedback right: A human can approve a dynamically generated plan; the engine can apply transition rules or a model result-classifier. Neither shows an owner choosing among competing whole-system current operational commitments/resources.
- Decision owner: Per-task Worker/Manager model for planning and execution; deterministic engine for transition enforcement; human for local plan acceptance.
- Supporting / enforcement mechanisms: Plan validator, loop caps, per-step retry paths, `ask_validate_user`, model result check.
- Closure path: A tool/result outcome advances or changes the *task* step; there is no established independent whole-system current-control decision → reallocation/operational return loop.
- Why this is / is not agent-owned: A class named `Manager` and model-generated workflow plan are not proof of dedicated S3 authority. Local human approval alone is not a qualified S3=P parent mode.
- Evidence: [fractale/agents/manager.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/manager.py); [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py); [fractale/engines/native/state_machine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/state_machine.py); [fractale/cli/run.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/run.py).
- Basis: Bounded negative source review with parent-mode alternative considered.
- Confidence: Medium; higher-level deployment governance might exist outside the assessed source but is not credited.
- Caveats: Do not conflate adaptive task planning/step gating with standing inside-and-now control over the system-in-focus.

### Absence scope

- Surfaces inspected: Model planner user-approval path, FSM transitions, manager execution and loop controls, native CLI engine wiring.
- Plausible first-party paths checked: Per-workflow Manager, tool result adjudication, human plan acceptance, step state transitions and limits.
- Why no material first-party path remains: All observed decisions close within the local task plan; no shipped first-party whole-current commitments/priorities/resource-allocation regulatory arrangement with decisive owner and return across the declared operational system was evidenced.


## S3* — Complementary audit

- State: —
- Function: No materially independent complementary challenge loop with actionable corrective return was established.
- Disturbance / variety regulated: Tool-call errors and generated plan validity, evaluated inside ordinary execution.
- Decisive decision or feedback right: The execution pathway invokes model-based success/failure classification and validates generated step specifications, but neither is a separable independent audit owner.
- Decision owner: Ordinary plan manager/helper/worker or validators participating in the execution path.
- Supporting / enforcement mechanisms: `check_tool_call`, `StepsValidator`, ordinary step rules and debug prompt.
- Closure path: Error/check results steer task retries or step transitions, but no independently accessed claim, challenger evidence or institutional corrective audit return is supplied.
- Why this is / is not agent-owned: A different prompt or helper-agent class is insufficient for an independent S3*; direct output self-checks are operational quality control.
- Evidence: [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py); [fractale/agents/manager.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/manager.py); [fractale/engines/native/agent/helper_agent.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/agent/helper_agent.py); [fractale/tools/calls.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/tools/calls.py); [fractale/core/plan/validate.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/plan/validate.py).
- Basis: Bounded negative inspection of available review/verification paths.
- Confidence: Medium-high within pinned default distribution.
- Caveats: No assertion that third-party validators or external MCP services lack audit functions.

### Absence scope

- Surfaces inspected: Manager's plan validation, tool result checking, Helper/DebugAgent, Step rules, logging and result persistence.
- Plausible first-party paths checked: Helper model, tool error classifier, step schema validation, debug-assisted retries and user plan approval.
- Why no material first-party path remains: No distinct complementary access route/independent challenger separate from ordinary task execution that can return findings to change subsequent governance/operation is installed.


## S4 — Outside-and-then intelligence

- State: —
- Function: No installed future/environment-facing adaptation of fractale's organizational capability was established.
- Disturbance / variety regulated: Current task data and tool outcomes; not prospective environmental change requiring new capability.
- Decisive decision or feedback right: No first-party future adaptation option-selection/right evidenced beyond current planning.
- Decision owner: Current task planner and developer/operator for any manual future software changes.
- Supporting / enforcement mechanisms: Prompt/plan regeneration and retained step results can inform local task continuation.
- Closure path: No source-evidenced external intelligence → proposed organizational adaptation → validated changed capability → subsequent operating cycle.
- Why this is / is not agent-owned: Research applications, experiments, memory persistence, and iterative scientific optimization are not automatically adaptation of the harness organization.
- Evidence: [README.md](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/README.md); [fractale/agents/manager.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/agents/manager.py); [fractale/db/memory.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/db/memory.py); [fractale/engines/native/engine.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/engines/native/engine.py).
- Basis: Bounded negative inspection of shipped run, planner and state/result persistence surfaces.
- Confidence: Medium-high for reviewed package.
- Caveats: Third-party scientific optimization tools may adapt scientific target parameters but are not first-party fractale organizational adaptation.

### Absence scope

- Surfaces inspected: CLI/Engine, manager planning, worker feedback, stored runs, README claims and example scientific optimizations.
- Plausible first-party paths checked: Model-driven plan revision, result/history retention, iterative science/optimization and developer TODO.
- Why no material first-party path remains: These act on the present task or future human development only; none supplies a retained environment-facing organizational adaptation decision/return path in the shipped runtime.


## S5 — Policy and identity

- State: —
- Function: No installed ultimate identity/policy authority deciding and returning first-party organizational policy was established.
- Disturbance / variety regulated: Tool/provider configuration and plan/workflow constraints are ordinary operating inputs rather than evidenced ultimate identity decisions.
- Decisive decision or feedback right: No model, parent institution or autonomous component in the assessed runtime is shown resolving and returning ultimate organizational identity or governing-policy choices.
- Decision owner: Human/developer may configure models and tools, but this is not demonstrated S5=P at fractale workflow recursion.
- Supporting / enforcement mechanisms: CLI flags, environment variables and Plan schema/validation.
- Closure path: No credible authority/matter → ultimate-policy decision → returned binding operational change path identified.
- Why this is / is not agent-owned: Configuration and tool prompt authority do not confer a first-party S5 governing function.
- Evidence: [fractale/core/config.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/config.py); [fractale/core/plan/plan.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/core/plan/plan.py); [fractale/cli/run.py](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/fractale/cli/run.py); [README.md](https://github.com/converged-computing/fractale/blob/b62ff1bce01e191828b90c5fa468f81197629e32/README.md).
- Basis: Bounded negative inspection of configuration, plan policy and runtime choices.
- Confidence: Medium-high for task-level runtime.
- Caveats: Open-source contributor governance or a customer's institutional policy must not be imputed to this operational recursion without explicit supported closure.

### Absence scope

- Surfaces inspected: Configuration/provider selection, Plan schema and validation, CLI/operator steps, readme/release/ownership context.
- Plausible first-party paths checked: Human plan acceptance, model/provider configuration, static constraints and repository/project identity.
- Why no material first-party path remains: No first-party, runtime-reachable function-specific S5 ultimate authority or returned policy/identity decision was observed at the declared fractale operational boundary.


## Distributed OSS parent arrangement

This is a publicly maintained open-source Python package, not a shared organization whose contributor governance automatically supplies runtime S3/S4/S5. A local operator approving a planned task does not demonstrate the OpenSiro-style project-level parent recurrence or institutional identity closure. No positive parent modifier is claimed.

## Self-hosted and non-human modes

The CLI runs locally with a selected provider and optionally a locally reachable MCP server; developer-configured prompt/schema/iteration limits bound activity. A model-mediated workflow can run with task-level user consent, but the inspected surface does not implement a separate parent-owned current-control, S4 capability-adaptation or S5 policy loop. No positive parent mode is inferred from the user's installation or API token.

## Recursion

The assessed level is the first-party fractale-managed workflow. Model-picked MCP calls, specialist tool endpoints and scientific resources participate operationally; an MCP server, an HPC batch scheduler or provider inference stack remains its own system at another recursion. Repeating a plan or recursively generating steps is computational control flow, not proof that distinct nested viable organizational layers exist.

## Variety and escalation

Relevant task variety comes from heterogeneous scientific tools, unknown runtime resources, API/tool errors and changing task outcomes. The worker addresses this by repeated model-mediated tool selection; the FSM attenuates allowed progression via rule-based success/failure transitions and bounded iteration. Plan-generation uncertainty may escalate locally to a user for approval, but this is not a whole-current-regulation or ultimate-policy authority witness. There is no independent algedonic pathway evidenced simply by displaying errors, logging, or retrying.

## Evidence gaps

- No live Gemini/OpenAI/MCP/HPC execution was performed. Source-level reachability of the installed first-party worker loop supports S1=A, not performance, reliability or production readiness.
- If first-party inter-agent contention regulation, independent audit, whole-current commitment control or prospective harness adaptation exists in an installed mode not visible in the reviewed source, a later evidence-backed same-ref correction can revisit the negative states. The default frozen review does not assume such hidden behavior.
- Manager/worker/tool-role separation and model-based error adjudication are deliberately not converted into S2/S3/S3* without the missing function-specific distinction, decisive owner and corrective return.
- `S2/S3/S3*/S4/S5=—` are **bounded shipped-path judgments**, not assertions of universal impossibility, and the supported source paths above were checked explicitly for each plausible function.
