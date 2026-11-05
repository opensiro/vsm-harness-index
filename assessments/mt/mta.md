---
harness_id: mta
project_name: MTA (Minimal Terminal Agent)
repository: https://github.com/Eric2i/minimal-terminal-agent
review_ref: 14147f6bbad6365a78b8112889958d109276c38b
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

# MTA (Minimal Terminal Agent)

## Review boundary

- System in focus: One runnable MTA Python terminal-task episode, with its model, `bash`/`submit` tools and throwaway Docker environment; not the hosting inference engine, remote Harbor evaluator or research team.
- Purpose and identity: Minimal reproducible model-to-terminal agent with trajectory capture for debugging/training.
- Relevant environment: User task, container filesystem, command output/exit code, API model completion, timeouts, step budget and Docker lifecycle.
- Standard-distribution boundary: `mta/{cli,agent,model,tools,environment,trajectory,config}.py`, documented `mta` CLI and Python API; optional Harbor/Modal test adapters are separate evaluator surfaces.
- Credited operating / distribution surfaces: [agent](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/agent.py), [CLI composition](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/cli.py), [tools](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/tools.py), [environment](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/environment.py), [trajectory](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/trajectory.py).
- Adjacent first-party surfaces excluded from ownership: Benchmark harness/graders, optional Harbor/Modal adapters, supplied inference server/model weights, training replay consumers and operator-created task validation; they do not install runtime organizational management roles.
- First-party modes inspected: CLI `mta` with Docker episode, Python `Agent` API with pluggable Environment, two tool calls, structured model replies, trajectory logging and step-limit/error paths.
- Recursion level: One terminal-working agent, one task per Docker episode. Multiple replay records or benchmark trials are not multiple governing S1 units.
- Reviewed revision: `Eric2i/minimal-terminal-agent@14147f6bbad6365a78b8112889958d109276c38b` (Apache-2.0 source).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`mta.cli.run` builds a configured OpenAI-compatible model client, a new Docker environment, `default_tools`, `AgentConfig(step_limit)`, and a trajectory recorder. `Agent.run` repeatedly invokes `step`: it asks the model with previous messages/tools, receives tool calls, dispatches each to `BashTool`/`SubmitTool`, appends actual outputs to the conversation, and exits on `submit`, step limit, error or cancellation. Docker uses a persistent per-episode container filesystem but separate shell sessions, then removes the container. The recorder saves model messages/tool arguments/outputs, return codes and token metadata for offline analysis; it does not independently audit whether a task was correct. [agent](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/agent.py), [tools](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/tools.py), [trajectory](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/trajectory.py).

## Operational model

The model chooses ordinary actions and termination; deterministic Python machinery mediates those decisions into Docker shell operations and provides feedback. The prompt asks the model to verify before `submit`, but that verification is performed by the same model and does not create independent oversight. Model inference happens outside the repository, but the first-party model/tool continuation route is installed and reachable through the CLI.

## S1 — Operations

- State: A
- Function: Execute a user terminal task through model-selected shell commands and subsequent observation.
- Disturbance / variety regulated: Unknown container state, command errors, dependency installation, timeout/exit codes and evolving task files.
- Decisive decision or feedback right: Model chooses `bash` arguments, next calls and `submit` completion after seeing tool results.
- Decision owner: Configured inference model acting through first-party `Agent.step`; runtime executes only selected tools.
- Supporting / enforcement mechanisms: OpenAI-compatible adapter, Docker isolated environment, `BashTool` return code/output and configured step/command-time limits.
- Closure path: User CLI task→model generation→selected `bash`→actual Docker result→`tool` message→next model choice or `submit`.
- Boundary reachability: `mta.cli.run` constructs and executes the full route against a configured model endpoint, not merely a benchmark-only stub.
- Why this is / is not agent-owned: Dynamic task action is chosen by model from observed real outputs; tool/runtime merely execute and cap work.
- Evidence: [task loop](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/agent.py), [CLI](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/cli.py), [shell tool](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/tools.py).
- Basis: Executable first-party model/tool/observation cycle with distinct task/termination decisions.
- Confidence: High for first-party source reachability; external model quality untested.
- Caveats: The model endpoint and Docker runtime must exist; this review did not execute paid API/Docker E2E.

## S2 — Coordination

- State: —
- Function: No balancing of disturbances between separate autonomous S1 operations.
- Disturbance / variety regulated: Multiple commands may conflict inside one container, but they are decisions of the same serial S1 episode.
- Decisive decision or feedback right: The single model selects sequential commands; no inter-agent priority/resource arbitration actor.
- Decision owner: Single S1 model and static Docker lifecycle settings.
- Supporting / enforcement mechanisms: Ordered tool calls, container boundary and timeout.
- Closure path: A tool's result returns to the same model; no two distinct S1 actors→coordination decision→revised commitments.
- Why this is / is not agent-owned: A list of tools, trajectories or benchmark parallel runs is not a coordinating system.
- Evidence: [agent](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/agent.py), [environment](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/environment.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: External infrastructure could schedule many independent MTA jobs, outside this distribution boundary.

### Absence scope

- Surfaces inspected: CLI composition, agent loop, default tools, Docker environment, trajectory record and Harbor integration boundary.
- Plausible first-party paths checked: Multiple shell commands as S1 peers, Docker process management as S2, benchmark parallelism as coordination.
- Why no material first-party path remains: The reachable shipped task route has only one independently deciding S1; no inter-S1 disturbance sensing and balancing return.

## S3 — Inside-and-now control

- State: —
- Function: No separately owned present-time organizational oversight of multiple autonomous operations.
- Disturbance / variety regulated: Task overruns, failures and token cost are bounded only at a single episode level.
- Decisive decision or feedback right: Fixed step limits and timeout/exception handlers terminate or record status; no model-driven resource negotiation or portfolio reallocation.
- Decision owner: CLI operator sets task and caps; program implements deterministic guardrails.
- Supporting / enforcement mechanisms: `AgentConfig.step_limit`, timeout, `exit_status`, cancellation and Docker disposal.
- Closure path: Over-limit or exception→terminal trajectory status, not S3 whole-system control/reassignment.
- Why this is / is not agent-owned: A static maximum and error record constrain S1 but do not create a discretionary S3 manager.
- Evidence: [run control](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/agent.py), [CLI configuration](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/cli.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Users may manage multiple runs manually; such activity is not packaged first-party S3.

### Absence scope

- Surfaces inspected: Limits/exit states, recorder, Docker lifecycle, CLI flags, bench adapter.
- Plausible first-party paths checked: Step budget as S3 resource choice, trajectory telemetry as present oversight, Docker lifecycle as S3 management.
- Why no material first-party path remains: There is no first-party portfolio view and decision owner able to adjust independent S1 commitments in response to current operational evidence.

## S3* — Complementary audit

- State: —
- Function: No independently owned runtime challenge of a worker's reported task completion.
- Disturbance / variety regulated: Inaccurate `submit`, misleading command output and task-result gaps.
- Decisive decision or feedback right: `submit` ends an episode on model request; recorder logs that event, not a contrary inspection/judgment.
- Decision owner: Same S1 model for any verification command; external evaluator/operator for later correctness checks.
- Supporting / enforcement mechanisms: Full trajectory, tool exit metadata, replay fields, benchmark Harbor adapters and final status.
- Closure path: Worker self-check→`submit`→record; no separate evidence acquisition→independent audit verdict→corrective S3 control.
- Why this is / is not agent-owned: Capturing trace/logprobs is not an independent inspector with a return route; terminal-benchmark grading is outside normal first-party operation.
- Evidence: [submit/tool schema](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/tools.py), [recording](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/trajectory.py), [agent](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/agent.py).
- Basis: Bounded absence review of trace/replay and submit paths.
- Confidence: High.
- Caveats: An external evaluator could grade stored episodes afterward; absent installed corrective return.

### Absence scope

- Surfaces inspected: Model prompt, `submit`, tool/result record, trajectory replay, optional Harbor integration.
- Plausible first-party paths checked: Model self-check as reviewer, trajectory recorder as auditor, Harbor benchmark grading as complementary audit.
- Why no material first-party path remains: No installed independent auditor can challenge a running claim from separate operational reality evidence and return findings into current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environment intelligence and capability adaptation control over future agent organization.
- Disturbance / variety regulated: Model endpoint changes, tool capabilities, future tasks and reproducibility settings.
- Decisive decision or feedback right: Human/configuration provides model endpoint, image and optional tools; task model solves current request.
- Decision owner: Operator/researcher, not a separate strategic actor in MTA.
- Supporting / enforcement mechanisms: Provider-agnostic config, Docker image selection and recorded token data for offline research.
- Closure path: Operator config or offline research may improve a future release; no shipped future scanning→option decision→governed operational adaptation.
- Why this is / is not agent-owned: Providing replay/training data is an input to outside research, not an in-runtime foresight decision system.
- Evidence: [config](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/config.py), [CLI](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/cli.py), [trajectory](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/trajectory.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: An external researcher may train a better model; not a first-party live S4 loop.

### Absence scope

- Surfaces inspected: Endpoint config, CLI options, trajectory/benchmark recording, model client and agent loop.
- Plausible first-party paths checked: Dynamic endpoint support as strategic adaptation, token-level replay as continuous learning, benchmark feedback as future sensing.
- Why no material first-party path remains: None autonomously selects and operationally applies future organizational changes from an environment forecast.

## S5 — Policy and identity

- State: —
- Function: No legitimate ultimate organizational identity/policy decision cycle.
- Disturbance / variety regulated: Shell risk, network access, task instructions and user trust.
- Decisive decision or feedback right: CLI operator sets Docker network/image/limits and prompt, not an autonomous policy body.
- Decision owner: External operator/developer; static system prompt and Docker arguments encode constraints.
- Supporting / enforcement mechanisms: Docker isolation, optional `--network none`, max steps and standard system prompt.
- Closure path: User configuration→bounded task execution; no identity dilemma→legitimate mandate choice→enforced policy return.
- Why this is / is not agent-owned: A prompt telling the model to act safely and a container boundary are not ultimate self-governance.
- Evidence: [system prompt](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/agent.py), [Docker config](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/environment.py), [CLI](https://github.com/Eric2i/minimal-terminal-agent/blob/14147f6bbad6365a78b8112889958d109276c38b/mta/cli.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: External institutional policies can constrain deployment; not part of the reviewed first-party harness.

### Absence scope

- Surfaces inspected: Task system prompt, Docker/network parameters, model environment config, error handling and CLI.
- Plausible first-party paths checked: Prompt as charter, Docker network isolation as policy decision, user limits as parent-assisted S5.
- Why no material first-party path remains: No distinct legitimate first-party policy owner arbitrates identity or mandate and returns a binding organizational decision.

## Recursion

One configurable model-driven shell agent inside a single task sandbox; changing the model, running more trials or keeping multiple trajectories does not yield another governed VSM recursion.

## Variety and escalation

Terminal command repertoire supplies S1 action variety; time, step and network limits attenuate risk. Errors and exit codes feed the next model call. Reaching a budget or cancel/error ends an episode and stores a record, rather than escalating to independent higher-function management.

## Evidence gaps

- No configured model endpoint or Docker runtime was used for a live paid inference task; source-level execution route and existing tests are the evidence.
- The model's self-instruction to check correctness is not a separately owned S3* audit, and externally consumed RL/SFT traces are not S4 organizational intelligence.
- The assessment is bounded to the shipped single-agent library/CLI, not downstream fleet orchestration written by users.
