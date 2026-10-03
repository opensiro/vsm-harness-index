---
harness_id: autonomous-swe-platform
project_name: Autonomous SWE Platform
repository: https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform
review_ref: 057045d8c107417358416c8b97c0249d1359f18d
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Autonomous SWE Platform

## Review boundary

- System in focus: the first-party coding-agent distribution at frozen revision `057045d8c107417358416c8b97c0249d1359f18d`, including the ordinary `AICodingAgent` ReAct loop and the shipped `AgentOrchestrator` SDLC mode with planner, architect, coder, tester, debugger, security and deployment components.
- Purpose and identity: autonomously perform software-engineering work inside a workspace, including code inspection/change, test execution, iterative correction, and optional full-SDLC artifact generation.
- Relevant environment: user requirements, repository/workspace state, model responses, shell/test outputs, generated artifacts, static-security findings, deployment validation and sandbox constraints.
- Standard-distribution boundary: shipped Python CLI/runtime, `agent.py`, `agent_core/`, testing/security/deployment modules and sandbox are inside. Provider internals, host project governance and repository CI/development activity are outside.
- Credited operating / distribution surfaces: `README.md`; `main.py`; `agent.py`; `agent_core/orchestrator.py`; `agent_core/state.py`; `agent_core/workflow.py`; `agent_core/agents/coder.py`; `agent_core/agents/tester.py`; `agent_core/agents/debugger.py`; `testing/test_runner.py`.
- Adjacent first-party surfaces excluded from ownership: repository CI and test suite as development evidence; README implementation-plan prose that is not wired into runtime; contributor/release governance; generated docs/reports after they cease to affect execution.
- First-party operating / deployment modes considered: ordinary coding ReAct mode, planning/architecture/review modes, automatic coding refinement, and the CLI `--sdlc` full lifecycle routed through `AgentOrchestrator`.
- Recursion level: one user software-engineering mission. The normal model/tool coding loop is an S1. In SDLC mode, specialized lifecycle workers perform bounded operational transformations under the central deterministic orchestrator.
- Reviewed revision: `057045d8c107417358416c8b97c0249d1359f18d`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The ordinary coding path in `agent.py` is a model-driven ReAct loop. It exposes workspace file/search/edit/command/web tools, returns observations to later model steps, and intercepts a final answer after a failed verification command when automatic refinement is enabled.

The separate `AgentOrchestrator` is wired from `main.py` and runs a sequential SDLC lifecycle: requirement analysis, repository analysis, planning, architecture, code generation, test generation, test execution, debugging on failure, security validation, deployment preparation and reporting. `AgentTaskState` records current stage, steps, changed files and validation flags. The orchestrator uses test feedback to decide whether to enter the debugger loop.

The SDLC components should not be mistaken for an autonomous multi-agent organization merely because they are named agents. Execution is predominantly sequential, and `SDLCWorkflow` is a static transition graph. In particular, the default orchestrator calls `DebuggerAgent.debug_loop` without a `patch_callback`; the debugger can analyze a failure and re-run tests but its optional patch-application seam is not composed by this standard path. Security/deployment findings are recorded but do not gate the final `SUCCESS` assignment.

## Operational model

In ordinary coding mode the model owns the substantive operational decisions and the runtime executes or refuses tool calls. In SDLC mode a deterministic central controller owns stage progression and uses current test state to route into debugging. The tester obtains complementary access by running the workspace's test suite independently of the coding model's self-report; test failure changes subsequent orchestration by entering the debugger/re-test path.

No first-party concurrent multi-S1 coordination relation is established by the frozen standard path. Sequential specialized stages, a workflow edge, or a central orchestrator name are not by themselves S2.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work through a model-driven coding loop that reads/searches a workspace, chooses edits/commands/tests and reacts to observations.
- Disturbance / variety regulated: arbitrary codebase structure, failing commands/tests, implementation alternatives, diagnostics, tool failures and changing workspace state.
- Decisive decision or feedback right: choose the next substantive coding/search/command action, interpret returned evidence and revise the implementation approach.
- Decision owner: the model-backed `AICodingAgent` in ordinary coding mode.
- Supporting / enforcement mechanisms: tool registry; sandbox/path/command guards; provider adapters; max-step bounds; automatic-refinement interception; workspace file and command tools.
- Closure path: user task/workspace state → model step → selected tool → runtime execution/refusal → observation enters later model context → actor changes subsequent work or reports completion.
- Boundary reachability: `main.py` directly constructs `AICodingAgent` for supported CLI/interactive execution; no application-supplied agent loop is required.
- Why this is / is not agent-owned: removing the model actor while retaining tools/sandbox leaves deterministic capabilities but no open-ended decision over what coding action to perform next.
- Evidence: [`main.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/main.py); [`agent.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent.py); [`README.md`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the newer SDLC `CoderAgent.generate_code` returns the LLM response without itself writing that response into the target file; S1 is therefore grounded in the separately supported ordinary ReAct coding mode rather than inferred from README claims about the SDLC coder.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the declared recursion.
- Disturbance / variety regulated: no specific concurrent inter-S1 interference/oscillation with a corresponding first-party attenuation path was established.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sequential SDLC stages, state transitions, task status, sandbox/resource limits and workflow ordering.
- Closure path: not applicable; the located lifecycle ordering does not close a coordination loop among concurrently autonomous operational units.
- Why this is / is not agent-owned: specialized components are called sequentially by the orchestrator; sequencing/decomposition alone is not S2.
- Evidence: [`agent_core/orchestrator.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/orchestrator.py); [`agent_core/workflow.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/workflow.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: future parallelization could change the function, but it is not present at the frozen boundary.

### Absence scope

- Surfaces inspected: ordinary agent loop, SDLC orchestrator, workflow/state model, specialized planner/coder/tester/debugger/security/deployment components and sandbox/resource controls.
- Plausible first-party paths checked: concurrent worker execution, shared-resource collision handling, reservations/locks, negotiated plans, collision detection, independent operational queues and feedback into multiple running S1s.
- Why no material first-party path remains: the frozen full-SDLC path invokes its specialized components serially and no concurrent inter-S1 disturbance plus attenuating coordination relation was found.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current SDLC commitment when validation indicates that implementation/test work is not ready to proceed normally.
- Disturbance / variety regulated: the current implementation may fail its test suite, making continuation to later lifecycle stages inappropriate without diagnostic work.
- Decisive decision or feedback right: route the current mission from test execution into bounded debugging/re-testing when the authoritative current test result is failing.
- Decision owner: constructor/runtime logic in `AgentOrchestrator`; no autonomous whole-system S3 actor is established.
- Supporting / enforcement mechanisms: `AgentTaskState`; stage transitions; `TestResult`; `max_debug_iterations`; deterministic branch into `DebuggerAgent.debug_loop`.
- Closure path: current implementation/test state → test runner result → orchestrator inspects `passed` → failure routes current work into debugger/re-test loop and records debug iterations → resulting test state is returned to the mission state before later stages.
- Boundary reachability: `main.py --sdlc` directly instantiates and executes this orchestrator path.
- Why this is / is not agent-owned: the whole-mission routing decision is hard-coded by the constructor; removing model discretion does not remove the fail→debug route. The first-party path is S3-specific but not autonomous.
- Evidence: [`main.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/main.py); [`agent_core/orchestrator.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/orchestrator.py); [`agent_core/state.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/state.py).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: most stage progression is a static workflow and is not credited. The positive mapping is narrowly limited to current test-failure feedback changing the active commitment into bounded debugging/re-test. The debugger's patch callback is not wired by the orchestrator, limiting practical corrective strength.
- Whole-system current view: `AgentTaskState` holds the mission's current lifecycle stage, validation flags, step history and debug-iteration state; the orchestrator owns the active lifecycle.
- Current-control decision scope: whether the current mission can leave test execution normally or must divert into bounded diagnostic/re-test work before continuing.

## S3* — Complementary audit

- State: C
- Function: test the produced workspace independently of the coding actor's verbal completion claim and feed failure back into current execution.
- Disturbance / variety regulated: generated/edited code can be incorrect even when the coding actor reports success.
- Decisive decision or feedback right: accept the test run as passing or failing based on an external test-process exit result and structured failures.
- Decision owner: constructor-owned `TestRunner`/orchestrator path; no autonomous independent auditor owns the verdict in this path.
- Supporting / enforcement mechanisms: test discovery; pytest/unittest subprocess execution; timeout/error capture; structured `TestResult`; generated test report; bounded debugger loop.
- Closure path: coding/test-generation work produces workspace state → `TesterAgent.run_all_tests` executes the suite independently → `TestResult.passed` returns to orchestrator → failure causes debugger/re-test work instead of being ignored.
- Boundary reachability: `TesterAgent` and `TestRunner` are directly called by the shipped `AgentOrchestrator.execute_task` path.
- Why this is / is not agent-owned: test verdict derives from first-party deterministic execution rather than the coding model; the complementary path is real and closed into later operation, but no separate autonomous auditor owns its judgment.
- Evidence: [`agent_core/agents/tester.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/agents/tester.py); [`testing/test_runner.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/testing/test_runner.py); [`agent_core/orchestrator.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/orchestrator.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: security/deployment checks are not used as the witness because the orchestrator later sets task `SUCCESS` regardless of their boolean flags. Ordinary same-loop “run tests before finish” is also not the witness.
- Claim being audited: that the current generated/edited implementation passes the project test suite.
- Ordinary reporting path: coding work produces implementation state and the lifecycle proceeds to testing.
- Complementary access path: `TestRunner` launches pytest/unittest directly against workspace reality and captures process exit/output independently of the coding model's self-report.
- Independence boundary: verdict is based on a separate test process and deterministic exit result, not on text supplied by the coder.
- Who acts on findings: `AgentOrchestrator` routes a failure into `DebuggerAgent.debug_loop`, which then re-runs tests and returns updated pass/fail state.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop was established at the mission recursion.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Repository analysis, planning, architecture and project memory support execution of the current requirement but do not form an external-and-future intelligence loop that changes durable organizational capability/strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: repository analyzer, planning/architecture agents, project memory, generated plans/reports and provider router.
- Closure path: not applicable; no prospective environmental distinction → adaptation option → returned persistent capability/S3 change loop was established.
- Why this is / is not agent-owned: planning a current software task is operational preparation, not by itself S4.
- Evidence: [`agent_core/orchestrator.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/orchestrator.py); [`agent_core/agents/planner.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/agents/planner.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: the repository describes future platform evolution, but development roadmap text is outside the running mission boundary.

### Absence scope

- Surfaces inspected: repository analysis, planning, architecture, memory, provider routing, security/deployment stages and generated recommendations.
- Plausible first-party paths checked: environmental scanning, future-option generation, persistent self-improvement, capability/model/tool revision and return of selected adaptation into later runtime behavior.
- Why no material first-party path remains: located planning/analysis is scoped to executing the current user requirement; no first-party prospective adaptation function changes the harness's persistent capability or strategy.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established at the mission recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. `Agent.md`, execution modes, sandbox policy and user task configuration supply constraints but do not constitute a runtime identity/ultimate-policy issue-resolution loop.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: `Agent.md`; system/mode prompts; sandbox/path/command policy; CLI options; user-selected provider/mode.
- Closure path: not applicable; no identity/policy issue → legitimate ultimate authority → authoritative returned decision loop was established.
- Why this is / is not agent-owned: deterministic enforcement of configured rules does not transfer ownership of ultimate policy to the runtime or model.
- Evidence: [`agent_core/agents/coder.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/agent_core/agents/coder.py); [`main.py`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/main.py); [`README.md`](https://github.com/SurjitW/Autonomous-Software-Engineering-and-Coding-Agent-Platform/blob/057045d8c107417358416c8b97c0249d1359f18d/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user control exists, but ordinary mode/task/configuration choices are not automatically S5 parent governance.

### Absence scope

- Surfaces inspected: Agent.md loading, mode/system prompts, sandbox policy, CLI configuration, orchestrator state, report/recommendation output and user review modes.
- Plausible first-party paths checked: mission identity revision, ultimate-policy proposals, parent policy escalation/decision/return and persistent runtime governance changes.
- Why no material first-party path remains: the located surfaces configure or constrain execution but do not close an identity/ultimate-policy issue at the selected recursion.

## Recursion

The selected recursion is one software-engineering mission. The ordinary coding agent is a clear S1. In `--sdlc` mode several lifecycle components act on the same mission under a deterministic central controller; they are not assumed to be viable nested systems merely because their classes are named agents.

## Variety and escalation

The model absorbs implementation variety through tools and iterative observations. Test failure is an explicit current-control/audit signal: the orchestrator diverts into debugging and re-testing up to a fixed limit. Sandbox denials and fatal exceptions are escalation/stopping mechanisms, not separate S-functions.

## Evidence gaps

The frozen source supports the ordinary S1 strongly. S3 is intentionally narrow because most lifecycle control is static sequencing and the default debugger does not wire its optional patch callback. S3* is stronger because the test runner directly observes workspace reality and failure changes later execution. No evidence gap requires `?` for the negative S2/S4/S5 conclusions after inspecting the relevant runtime surfaces.
