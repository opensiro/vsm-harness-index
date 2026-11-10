---
harness_id: frognano
project_name: FrogNano
repository: https://github.com/microsoft/FrogNano
review_ref: 880dc674c075d7425908757b334eaca7c9e3185f
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# FrogNano

## Review boundary

- System in focus: the first-party Leaf repository-level coding-agent harness in FrogNano, executed against an isolated task environment by the shipped evaluation CLI. The model actor participates through an OpenAI-compatible endpoint; the harness owns the model-to-tool-to-observation loop.
- Purpose and identity: solve repository software-engineering tasks by model-selected file inspection, edits, commands and iterative verification. FrogNano also distributes an evaluation runner, but benchmark scoring is not the ongoing agent's organizational control.
- Relevant environment: checked-out task repository, task instructions and tests, task Kubernetes pod, configured model endpoint, operator-provided cluster and benchmark datasets.
- Standard-distribution boundary: installed `frognano-eval run` → `run_evaluation` / `_run_job` → `LeafAgent.run` → `LeafEnvironment` / five tool implementations; source-shipped defaults and configuration. The evaluation CLI is the entry point, not a general interactive multi-agent team product.
- Credited operating / distribution surfaces: [CLI](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/cli.py), [job entry and wiring](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/runner.py), [Leaf agent](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/agent.py), [environment and pod recovery](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/environment.py), [five tool schemas](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/tools.py), [in-pod execution](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/tool_runner.py), [Kubernetes task runtime](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/runtimes/kubernetes.py).
- Adjacent first-party surfaces excluded from ownership: dataset adapters, image/digest locks, benchmark reward/scoring and aggregate metrics, WandB tracking, CI, evaluation fixtures/tests and model-specific reinforcement-learning claims. These help evaluate or run Leaf; they do not themselves become agent-owned S2–S5 loops. TaskPilot training and Qwen/FrogNano model weights are outside this repository's shipped online harness control.
- First-party operating / deployment modes considered: published Python evaluation CLI with configurable model, workers, seeds, time limits, retries and Kubernetes task pods; one Leaf instance per task/seed; optional concurrent independent task instances. No first-party general team/supervisor mode was found.
- Recursion level: one Leaf coding-agent task session as an operational S1 inside the evaluation harness, with multiple task/seed sessions when the evaluation runner is used concurrently. A task pod/tool call is not automatically a viable recursive organization.
- Reviewed revision: `880dc674c075d7425908757b334eaca7c9e3185f` (pinned in Index intake #3035).
- Observation date: 2026-11-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [README](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/README.md) and [package entry point](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/pyproject.toml) distribute `frognano-eval`, whose `run` command loads a dataset/configuration and calls `run_evaluation`. Its thread pools dispatch task/seed jobs into separate Kubernetes task runtimes; jobs instantiate `LeafEnvironment` and `LeafAgent`. The first-party agent seeds system/user messages, queries a configured chat model with tool schemas, acts on selected `Read`, `Write`, `Edit`, `Glob` or `Bash` calls, returns real observations to the next model turn and finishes with a patch/trajectory. The environment copies a tool runner into each task pod and has bounded pod recreation plus replay of prior mutating actions. Checkpoints, retry, max-step/context/time limits, and summary/reward recording provide infrastructure reliability and experiment bookkeeping. [Runner](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/runner.py), [agent](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/agent.py), [environment](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/environment.py).

The dataset/benchmark task, Kubernetes resources, tool execution OS and model endpoint are external environment or supporting substrates. The README's TaskPilot/model-training discussion is not an installed S4 capability of the assessed Leaf runtime. Evaluation reward is computed after the agent result, not returned as a separately governed corrective-audit decision for the ongoing Leaf agent.

## Operational model

- Actual outcome: a task-specific repository change/answer, with model-chosen investigations, edits and command execution in an isolated working copy.
- S1 units: one `LeafAgent.run` loop per task/seed, receiving task observations and choosing later actions; concurrent jobs are independent instances, not automatically coordinated operational teams.
- Ownership split: the model-backed agent chooses coding actions; Python dispatch, Kubernetes pods, recovery/replay, fixed worker limits, timeouts and scoring execute developer/operator-selected parameters. The operator configures endpoints, dataset, budget and Kubernetes permissions. The benchmark test evaluator is separate from agent decision ownership.

## S1 — Operations

- State: A
- Function: an agentic repository task unit transforms code and test state toward the requested task outcome.
- Disturbance / variety regulated: unfamiliar repository structure, test feedback, tool errors and evolving code changes.
- Decisive decision or feedback right: choose the next file/command/tool operation or completion after seeing observations.
- Decision owner: the model-backed Leaf agent in `LeafAgent.run`, not the deterministic dispatcher or benchmark scorer.
- Supporting / enforcement mechanisms: `OPENAI_TOOLS` schema, in-pod tool runner, environment interface, Kubernetes isolation, fixed step/time limits and pod replay.
- Closure path: task instruction → model-selected tool call → `environment.execute` → observation appended as a tool message → next `client.complete` call; final answer and patch exit the task session.
- Boundary reachability: `frognano-eval run` calls `_run_job`, constructs `LeafAgent` with the configured model and `LeafEnvironment`, then directly calls `agent.run`; the full loop and tools are shipped, not only demonstrated by a test fixture.
- Why this is / is not agent-owned: the model chooses code actions from observations; removing model discretion leaves fixed execution tools but no equivalent task-solving decisions. This establishes S1 autonomy despite deterministic tool execution.
- Evidence: [runner `_run_job`](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/runner.py), [agent loop](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/agent.py), [tool executor](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/tool_runner.py).
- Basis: structural.
- Confidence: high for source-wired action/feedback ownership; no model-backed execution was performed in this review.
- Caveats: the agent depends on a configured external model/cluster; its coding quality and real benchmark success are not independently validated here.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 interference regulation with a distinct coordination decision/feedback loop is established at this boundary.
- Disturbance / variety regulated: multiple task/seed jobs may contend for global worker capacity, but concrete S1-to-S1 conflict/oscillation and a material S2-specific response are not established by configured pool concurrency alone.
- Decisive decision or feedback right: no evidenced first-party agentic inter-S1 adjustment; the operator sets `max_workers` and optional per-seed pool limits.
- Decision owner: developer/operator configuration for job count, deterministic thread pool for dispatch.
- Supporting / enforcement mechanisms: `ThreadPoolExecutor`, isolated Kubernetes task pods, static job slicing, per-job retries and locks on result-file writes.
- Closure path: no demonstrated feedback from a conflict between S1s into their subsequent coordination decisions; thread pool admission and JSONL append are infrastructure transitions.
- Why this is / is not agent-owned: concurrent independent Leaf tasks do not negotiate or adjust one another; scheduler limits are static enforcement, not model-owned coordination.
- Evidence: [runner concurrency and result lock](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/runner.py), [Leaf per-task model loop](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/agent.py), [config](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/config.py).
- Basis: structural.
- Confidence: medium-high within the shipped per-task/evaluation modes.
- Caveats: external Kubernetes scheduling can regulate infrastructure resource contention, but does not donate first-party S2 at this chosen recursion.

### Absence scope

- Surfaces inspected: evaluation runner, config/CLI, task pod/runtime boundaries, Leaf agent/environment/tool loop and readme-supported modes.
- Plausible first-party paths checked: pooled task dispatch, seed-specific worker caps, result-file lock, isolated task pod creation, retry/replay and model parallel tool-call handling.
- Why no material first-party path remains: these paths bound execution capacity or protect records inside independent tasks, without a sourced coordination response and feedback for a specific inter-S1 interference; parallel tool calls belong to one S1, not distinct S1 conflict regulation.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control discretionary loop over operational commitments is supplied for Leaf sessions.
- Disturbance / variety regulated: task failures, runtime limits and concurrent job execution are handled by fixed retry/cap mechanisms rather than supervisory judgment over a portfolio.
- Decisive decision or feedback right: no first-party agent/parent making substantive current resource/priority/exception decisions using a whole-current view.
- Decision owner: human-authored evaluation config and deterministic runner control flow; each Leaf agent owns only its local coding steps.
- Supporting / enforcement mechanisms: fixed workers, `max_attempts`, budget/timeout stops, job status tracking, optional WandB telemetry.
- Closure path: runner records failures and summaries and retries by configured rules; no whole-system discretionary reallocation or intervention returns into active S1s.
- Why this is / is not agent-owned: aggregate status and runtime limits do not show an autonomous supervisor choosing current system-wide commitments. Ordinary CLI parameter selection does not establish S3=P.
- Evidence: [runner job pools, failures and summary](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/runner.py), [configuration](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/config.py), [telemetry](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/wandb.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: an external operator could manage the evaluation system, but no first-party complete S3 parent decision/return mode was found.

### Absence scope

- Surfaces inspected: CLI, evaluation runner, config, per-task Leaf loop, runtime recovery, telemetry and evaluation-result lifecycle.
- Plausible first-party paths checked: job summary, failure retries, stop signal, max-worker enforcement, WandB reports and operator CLI options.
- Why no material first-party path remains: no supported whole-current supervisory view plus discretionary allocation/intervention with returned operational closure; observed mechanisms execute fixed parameters or report outcomes.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary, sufficiently independent audit path that reports a distinct judgment into ongoing Leaf control is established.
- Disturbance / variety regulated: repository-task output correctness is measured by external benchmark reward/tests after a run, not independently audited as a continuing S3 corrective channel within the agent organization.
- Decisive decision or feedback right: no separate first-party auditor with operational-artifact access and feedback authority over subsequent Leaf decisions.
- Decision owner: dataset/task evaluator outside the assessed agent control loop; the agent may itself choose ordinary tests/verification via Bash.
- Supporting / enforcement mechanisms: `compute_reward`, `get_patch`, result JSONL, trajectory checkpoints and benchmark reports.
- Closure path: reward and test output are recorded after the Leaf result, used for evaluation metrics; they are not fed to an independent auditor that changes the originating agent's control decisions.
- Why this is / is not agent-owned: the first-party agent can inspect its own work with commands, but no claim-relative independent audit judgment/feedback channel is wired. Post-hoc benchmark grading is adjacent evaluation, not autonomous S3*.
- Evidence: [runner reward path](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/runner.py), [environment `compute_reward`](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/environment.py), [agent termination and checkpoint](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/agent.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: benchmark tests may be independent of the model output in a scientific evaluation sense; that does not by itself establish the required ongoing organizational corrective-audit return path.

### Absence scope

- Surfaces inspected: agent prompt/loop/tools, environment reward and replay, runner evaluation path, datasets and trajectory/reporting behavior.
- Plausible first-party paths checked: model's Bash tests, after-run reward, patch capture, trajectory checkpoints and retry-on-agent-infrastructure-error.
- Why no material first-party path remains: ordinary self-testing and post-run score reporting do not create a separately owned complementary audit judgment with findings influencing subsequent first-party control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported first-party prospective environmental sensing/options/adaptation return loop for future harness capability is evidenced.
- Disturbance / variety regulated: task-specific issues change the current coding task; model training and future evaluation research are outside the running Leaf harness.
- Decisive decision or feedback right: no Leaf agent or parent receives external future distinctions and decides reusable capability adaptations in a supported mode.
- Decision owner: external model/training work and operator/developer choices, not an installed S4 decision right.
- Supporting / enforcement mechanisms: task history and checkpoints, dynamic in-task tool use, fixed prompt and configured model endpoint.
- Closure path: current task observations return to the same task's S1 loop; no outside-and-then proposal affects durable future capability of the harness.
- Why this is / is not agent-owned: solving a changing coding task and replaying actions are immediate operations; README training/evaluation achievements do not become runtime S4.
- Evidence: [fixed tool/prompt schema](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/tools.py), [Leaf history loop](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/agent.py), [README training separation](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: future externally supplied model revisions could improve capability, but no first-party future adaptation closure was found in this source release.

### Absence scope

- Surfaces inspected: README, config, agent loop, tool schemas, evaluation runner, checkpoint/replay and dataset/scoring integrations.
- Plausible first-party paths checked: in-task plan/test revision, persistent trajectory files, model selection and benchmark-derived feedback.
- Why no material first-party path remains: the shipped runner records experiments and runs a fixed model/tool contract; it does not transform outside/future observations into selected reusable harness capability changes that feed back into operation.

## S5 — Policy and identity

- State: —
- Function: no operational first-party identity/ultimate-policy decision closure at Leaf-agent recursion is evidenced.
- Disturbance / variety regulated: run configuration, tool bounds and cluster access are preselected constraints, not live identity-level dilemmas with legitimate authority/return.
- Decisive decision or feedback right: no supported runtime entity decides constitutional purpose/policy or sends such an issue to a parent authority for return.
- Decision owner: developer/operator outside the agent loop sets fixed prompt, tools, endpoint, dataset, budgets and permissions.
- Supporting / enforcement mechanisms: system prompt, tool list, Kubernetes namespace/permissions, max-step/context/time caps, CLI config and fixed execution policies.
- Closure path: operational tool results return to S1, but no ultimate-policy issue/authoritative decision/return path is present.
- Why this is / is not agent-owned: a system prompt and human-created configuration constrain work; neither is a first-party S5=A or closed S5=P mode without policy-level return.
- Evidence: [tool prompt/schema](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/tools.py), [agent config](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/harness/leaf/agent.py), [CLI/config](https://github.com/microsoft/FrogNano/blob/880dc674c075d7425908757b334eaca7c9e3185f/frognano/cli.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: project-maintainer governance is an adjacent development organization, not first-party runtime S5 at this boundary.

### Absence scope

- Surfaces inspected: prompt/tool contracts, CLI/config, Leaf loop, environment enforcement, repo release/governance README and task runtime.
- Plausible first-party paths checked: human/operator configuration, agent tool discretion, runtime stop limits, model endpoint selection and maintainer policy documentation.
- Why no material first-party path remains: no identity/ultimate-policy matter reaches a legitimate runtime/parent decision owner and returns as authoritative future operation policy. Operational limits and test evaluation do not substitute for this loop.

## Recursion

Each Leaf job has its own task, workspace and autonomous coding decision loop. Parallel isolated jobs are S1-like units within the evaluation batch, but their process nesting/pod boundary alone does not establish each as a self-governing viable recursion with independent metasystem. The benchmark orchestration and research project are adjacent to the standard Leaf task agent rather than imported higher-function owners.

## Variety and escalation

File/tool/model errors and unknown repository code flow to the S1 agent as observations or terminal failure. Fixed time/context/step budgets and infrastructure retries attenuate computational variety. Pod recreation replays mutating operations and rejects differing replay outcomes; this is a deterministic recovery mechanism, not an agent-owned S3/S5 decision. Operators must handle exhausted retries, missing cluster/model capability and wider environment change outside the agent's authority. No exceptional algedonic governance channel is claimed from job failure status alone.

## Evidence gaps

- Source-first static inspection only: no authenticated Kubernetes cluster, external model execution, benchmark replay, or real task outcome was attempted; behavioral success and production operations remain unverified.
- Optional configurations beyond the documented CLI/config/Leaf paths were not independently executed. The bounded negative assessments concern the shipped first-party distribution at this pinned revision, not every possible user extension.
- The repo contains benchmark and model-training claims, but they are not independent evidence of a first-party S4/S3* runtime control channel.
