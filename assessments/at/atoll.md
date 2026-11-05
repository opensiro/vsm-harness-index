---
harness_id: atoll
project_name: Atoll
repository: https://github.com/Teraverse-AI/atoll
review_ref: 741adc0cb28c89458815588d4418afe9336adcbf
reviewed_at: 2026-11-05
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

# Atoll

## Review boundary

- System in focus: Atoll's single-task accounting/finance agent runner plus its per-run workspace, native tool provider and snapshots; not Mercor Archipelago or an external evaluation operator.
- Purpose and identity: Apache-2.0 lightweight agentic task runner and evaluation-compatible environment with a standard first-party model/tool loop, run artifacts and deferred grading.
- Relevant environment: Task package instructions and workbook/PDF workspace changes, model provider responses, tool errors, Docker sandbox availability, time/token/cost budgets and evaluation input configuration.
- Standard-distribution boundary: `agents/runner/{main,loop,providers,models,llm,...}`, first-party `native_tools`, `environment/atoll_env`, task examples and CLI scripts at the reviewed commit. Source copied/adapted from Mercor is credited **only** insofar as it is actually installed and connected in the shipped Atoll runner; authorship/novelty is not inferred.
- Credited operating / distribution surfaces: [Atoll English README](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/README.en.md), [runner entry](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/main.py), [loop](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/loop.py), [native provider](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/providers/native.py), [agent docs](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/README.md), [grading status](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/grading/README.md).
- Adjacent first-party surfaces excluded from ownership: The project's unimplemented grading/verifier subsystem, sample gold answers, optional developer/CI tests, user-provided evaluation orchestration, external LLM services, and Mercor Archipelago's own operations. Pre/post snapshots are evidence storage, not a functioning independent audit controller.
- First-party operating / deployment modes inspected: `atoll-run --task ... --model ...` with native tool provider and external model (direct vendor or proxy), optional task-selected native tool families, per-run workspace snapshots, isolated model-authored Python code sandbox, budget/step/timeout constraints. MCP gateway provider is documented as a stub, not an installed alternative path.
- Recursion level: One task-performing agent with a local execution harness. Repeated benchmark runs or many native tools are not multiple jointly controlled S1 subsidiaries at this recursion.
- Reviewed revision: `Teraverse-AI/atoll@741adc0cb28c89458815588d4418afe9336adcbf` (root Apache-2.0 license and first-party distribution, incorporating disclosed Apache-2.0 upstream ports/vendoring).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`runner/main.py` loads a Harbor-style task, creates a workspace, captures an initial snapshot, builds `AgentRunInput` and native tool registry, then invokes `LoopTruncatedToolsAgent.run()`. The loop, adapted from Archipelago, presents tool schemas to the selected LLM, executes model-selected tool calls via `ToolProvider`, translates tool results/errors/images into subsequent messages, and finalizes when the model stops calling tools or enforced caps trigger. It writes final workspace snapshot, JSONL trajectory and result JSON. Direct vendor and proxy modes use the included request-adaptation code; the MCP provider alternative is a stub. The `grading/` directory explicitly says verifier execution is deferred. [entry](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/main.py), [loop](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/loop.py), [provider](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/providers/native.py), [grading](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/grading/README.md).

## Operational model

A task-specific model chooses tool actions and adjusts from the observations that the installed Atoll loop feeds back. Tool invocation and workspace isolation are deterministic host services; the LLM is an external inference provider. The benchmark operator selects tasks, models, tools and budgets. Snapshot collection and possible future scoring are outside agent task choices and presently do not close S3* or S3 control.

## S1 — Operations

- State: A
- Function: One model-driven task agent edits/reads accounting workspace artifacts, uses a published tool surface and can adjust its next action after tool outcomes.
- Disturbance / variety regulated: Task differences, spreadsheet/PDF/file state, tool errors, model context and failed/no-result calls.
- Decisive decision or feedback right: The configured inference model chooses which tool calls to emit, with what arguments, whether to continue or finalize, after receiving prior tool results.
- Decision owner: Configured task agent model through Atoll's installed `LoopTruncatedToolsAgent`; `NativeToolProvider` executes rather than deciding task strategy.
- Supporting / enforcement mechanisms: Native tool registry/schema, provider adapter, context-trim notices, refusal/spill on tool-result budget, max-steps/timeout/token-cost bounds, code sandbox and trajectory records.
- Closure path: Task package → CLI workspace creation → model call with native tool schemas → selected tool execution → text/error/image observation → next model step/final answer → persisted workspace/result.
- Boundary reachability: The CLI actually instantiates the native provider and loop and runs them, with configured real model provider option. Shipped code was adapted from Mercor, but this repo installs and executes it locally; credit is for Atoll-distributed reachability, not original algorithm ownership.
- Why this is / is not agent-owned: Model discretionary tool choice and observation-conditioned continuation make S1=A. Host budget enforcement, externally supplied model backend and fixture grader do not own those choices.
- Evidence: [entry](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/main.py), [loop](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/loop.py), [native provider](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/providers/native.py).
- Basis: Installed first-party runtime wiring and model/tool/result continuation; imported provenance explicitly bounded.
- Confidence: High for source reachability; no configured real-provider E2E exercised locally.
- Caveats: Some native tool families are documented placeholders and Docker is required for code execution. E2E task quality and comparative scores are not claimed.

## S2 — Coordination

- State: —
- Function: No independent task-operating S1 work units are mutually coordinated within one Atoll run.
- Disturbance / variety regulated: Concurrent tool calls and task input/workspace conflicts are possible but handled as one model-run sequence, not observed cross-S1 policy attenuation.
- Decisive decision or feedback right: A single model initiates tool calls; native provider dispatches them; operator selects mounted tool families.
- Decision owner: Same task model for local steps and deterministic provider/CLI for routing.
- Supporting / enforcement mechanisms: Namespaced native tool schemas, tool provider registry, per-step batch results and workspace isolation.
- Closure path: Model tool batch → provider results → same model. No two S1 units → an inter-unit conflict signal → S2 balancing authority → revised operation in both.
- Why this is / is not agent-owned: Many tools or parallel tool calls are resources of one S1 agent, not two independently deciding agents requiring coordination.
- Evidence: [loop](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/loop.py), [provider](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/providers/native.py), [agent README](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/README.md).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: An external benchmark farm could orchestrate many independent runs; that operation is outside the published per-run system boundary.

### Absence scope

- Surfaces inspected: Runner entry/registry, loop multi-tool handling, native tool provider, environment workspace creation and documented mode matrix.
- Plausible first-party paths checked: Parallel tool dispatch as S2, multiple native tool servers as S1 cells, many independent task invocations as a coordinated hierarchy.
- Why no material first-party path remains: No installed first-party decision maker resolves task-level conflicts among distinct autonomous S1 work units and feeds attenuation back to them.

## S3 — Inside-and-now control

- State: —
- Function: No whole-portfolio present management chooses priorities, budgets or corrective action for distinct S1 units.
- Disturbance / variety regulated: Model time, token/cost budget, run errors, context-window exhaustion and overlarge tool results.
- Decisive decision or feedback right: Operator-provided caps and deterministic code warn/stop/truncate/spill one run; they do not allocate a current operating portfolio autonomously.
- Decision owner: Benchmark config/CLI operator and predefined local loop conditions.
- Supporting / enforcement mechanisms: max_steps, timeout, cost/token budget warnings, result budgeting, status output and per-run metrics.
- Closure path: Budget threshold → warning/final turn or failure; no whole-system resource-monitoring authority → reprioritization → multiple S1 behavioural corrections.
- Why this is / is not agent-owned: Rich telemetry and deterministic per-run cap enforcement are local S1 constraints, not a separate whole-current S3 manager.
- Evidence: [main config](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/main.py), [loop budgets](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/loop.py), [agent docs](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/README.md).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Externally operated scheduler or grading engine could use these outputs for decisions; none is installed as controlling authority here.

### Absence scope

- Surfaces inspected: CLI configuration, budget code, status/usage collection and per-run snapshots/results.
- Plausible first-party paths checked: Cost accounting as S3, max-step cap as portfolio control, run status dashboard as whole-system management, evaluation runner as director.
- Why no material first-party path remains: Each only enforces/records one task's limits, without cross-S1 decision ownership and returned portfolio-level resource correction.

## S3* — Complementary audit

- State: —
- Function: No independent audit checks the real agent output using a separate evidence channel and returns findings to management.
- Disturbance / variety regulated: Errors in final workbooks, task completion or model claims could be assessed through snapshots/gold answer, but the published verifier/grading engine is explicitly deferred.
- Decisive decision or feedback right: Runner captures initial/final snapshots and trajectory; no implemented verifier renders an independent correctness verdict during the deployed workflow.
- Decision owner: None for installed S3*; potential future grading code, human evaluator or benchmark operator lies outside the executing agent.
- Supporting / enforcement mechanisms: Pre/post workspace snapshots, JSONL trajectory, sample `gold_answer.json` and verifier schema definitions; no live scoring feedback path.
- Closure path: Agent run → saved snapshots/results → possible future offline evaluation; **missing** independent audit observation, verdict and control return.
- Why this is / is not agent-owned: Evidence artifacts are inputs an auditor might use; their existence, and tests against fixtures, do not itself constitute an independent complementary audit function.
- Evidence: [grading deferred](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/grading/README.md), [runner output](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/main.py), [examples](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/examples/README.md).
- Basis: Explicit absent implementation and bounded first-party return path.
- Confidence: High.
- Caveats: The project aims for Archipelago-compatible benchmarking, but future plans and compatibility claims are not evidence of a deployed S3*.

### Absence scope

- Surfaces inspected: `grading/README.md`, main run artifacts, environment snapshots, examples/answer keys and agent tests.
- Plausible first-party paths checked: Snapshot as alternate-reality witness, sample gold answers as an audit judge, unit tests as independent assessor, external benchmark scoring as Atoll S3*.
- Why no material first-party path remains: The repository explicitly defers verifier execution and has no separate audit verdict owner and correction-to-S3 path.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective external-environment intelligence selects future operating adaptations for the harness.
- Disturbance / variety regulated: Future provider changes, tool-family availability, model context budgets and benchmark task design.
- Decisive decision or feedback right: Operator configures task/model/tools and developers update vendor ports; the model addresses its assigned current task.
- Decision owner: Human evaluation operator or maintainer for future changes; not an installed autonomous future-management function.
- Supporting / enforcement mechanisms: Task TOML config, model adapters, optional future gateway provider stub, response-surgery compatibility fixes and manual upstream resync.
- Closure path: Current task → present tool work/result; code/config update → next run when human changes it. No prospective environmental signal → autonomous adaptation policy → adopted new capability.
- Why this is / is not agent-owned: Provider compatibility retries and vendored resync are tactical/repository-level mechanisms, not agency choosing a future viable operating model.
- Evidence: [agent docs](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/README.md), [runner](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/main.py), [Atoll fixes](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/atoll_fixes.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Model may plan long-horizon steps within a finite task; that is not separately installed organizational S4.

### Absence scope

- Surfaces inspected: Task/config parser, model adapters, ported LLM compatibility and retry paths, agent instructions and environment setup.
- Plausible first-party paths checked: Dynamic context trimming as S4, model retry as adaptation, provider-choice switch as strategic forecasting, future MCP/grade plans as implemented S4.
- Why no material first-party path remains: These are present-run reaction or human design/configuration, with no installed prospective intelligence owner, option selection and S3-facing feedback.

## S5 — Policy and identity

- State: —
- Function: No distinct identity/ultimate policy decision authority closes a mandate back into the agent's operation.
- Disturbance / variety regulated: Benchmark validity, sandbox safety, tool access and financial-workspace data boundaries.
- Decisive decision or feedback right: Operator supplies task, prompt and network/tool safety configuration; static code limits execution and writes artifacts.
- Decision owner: Human deployment maintainer/evaluation operator; not an installed S5 body or recognized parent-assisted policy cycle.
- Supporting / enforcement mechanisms: Static accounting assistant prompt, task TOML, per-run sandbox/network boundary and repository license/NOTICE.
- Closure path: External setup rules → current run constraints; no agent identity-level issue → legitimate policy authority judgment → returned organizational mandate.
- Why this is / is not agent-owned: Safety isolation and license compliance are essential but do not constitute agent-owned ultimate governance or a closed parent S5 decision right.
- Evidence: [runner prompt](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/agents/runner/main.py), [readme](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/README.en.md), [environment docs](https://github.com/Teraverse-AI/atoll/blob/741adc0cb28c89458815588d4418afe9336adcbf/environment/README.md).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: The project developer controls product identity, but their repository decisions are outside the observed task runtime.

### Absence scope

- Surfaces inspected: System prompt, task settings, code sandbox and environment constraints, repository ownership/license policy and output contract.
- Plausible first-party paths checked: Docker network isolation as identity governance, static prompt as S5 charter, license/NOTICE as ultimate policy, benchmark scoring contract as mandate.
- Why no material first-party path remains: No first-party current-run identity conflict reaches an authorized policy decision maker and returns as an authoritative revised operational mandate.

## Recursion

One task model is S1. Many files, native tool modules, run artifacts and parallel benchmark instances do not automatically create a recursively viable management organization. A future evaluation platform may surround Atoll; its governance cannot be imported into this single installed runner.

## Variety and escalation

Task-configured native tools and model choices amplify the agent's available actions; isolation, tool budgets, output truncation/refusal, token/cost/step limits attenuate risky or unbounded behavior. Failures surface in status/trajectory, but no independent algedonic path to installed S3/S4/S5 governance exists. Grading is deferred, so a saved failure is not a closed audit or management intervention.

## Evidence gaps

- Local `python -m pytest agents/tests -q` was not executable because `pytest` was absent; external model API keys, compatible Python dependencies and Docker sandbox were not provisioned for a live run.
- Upstream Archipelago code is explicitly embedded/adapted; scope credits the concrete shipped Atoll implementation and first-party composition, not originality or operations of the upstream project.
- The grading/verifier component is explicitly unimplemented, and benchmark-comparable performance or independent S3* audit is not claimed.
