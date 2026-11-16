---
harness_id: openvlharness
project_name: OpenVLHarness
repository: https://github.com/uclanlp/OpenVLHarness
review_ref: c080224d31774fcf1b3c0f55abb71d143f7f3501
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenVLHarness

## Review boundary

- System in focus: The installed OpenVLHarness inference runtime and its configured shared tool router.
- Purpose and identity: Answer multimodal questions by choosing tools that inspect images, search external sources and compute over observations.
- Relevant environment: Question and images, optional web sources, external model inference and shared tool/GPU backend capacity.
- Standard-distribution boundary: The openvlharness Python package and its supported tool server. Benchmark/evaluation utilities are inspected for the boundary.
- Credited operating / distribution surfaces: YAML bootstrap, MainAgent.generate, typed capabilities, per-question memory and configured service router.
- Adjacent first-party surfaces excluded from ownership: Benchmark datasets, eval-only judge/score reports, repository tests, research validation and CI.
- First-party operating / deployment modes considered: Installed Python inference API with configured local or remote model services, optional packaged tool server, and concurrent independent questions using a shared router.
- Recursion level: One deployment of independent question runs and the shared router they may use. No organization across router processes is inferred.
- Reviewed revision: `c080224d31774fcf1b3c0f55abb71d143f7f3501`
- Observation date: 2026-11-16
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

A single MainAgent instance is built from YAML and can answer independent questions. Each call begins with fresh multimodal memory. A model selects tools and sees their results and inventories. Capabilities adapt typed tool output, and the service router brokers a shared set of backends. The auxiliary code generator and executor supply bounded work inside the question. [`pyproject.toml`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/pyproject.toml#L5-L27), [`openvlharness/bootstrap.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/bootstrap.py#L260-L287), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L62-L116), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L136-L191), [`docs/runtime.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/docs/runtime.md#L1-L29), [`docs/runtime.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/docs/runtime.md#L101-L121).

## Operational model

The question-run model selects observations, computations and the final answer. Separate question runs have independent task states and can share router and backend capacity. The router serializes calls in preconfigured capacity groups. Human deployment configuration determines those groups' limits and the model/capability assembly.

## S1 — Operations

- State: A
- Function: Answer a multimodal question with selectable perception, search and computation tools.
- Disturbance / variety regulated: Unknown question-specific facts, images, web evidence, tool results and errors.
- Decisive decision or feedback right: Choose what to observe or compute next and decide when to provide the answer.
- Decision owner: The orchestrator model used by MainAgent for the question.
- Supporting / enforcement mechanisms: Model adapter, typed capabilities, configurable limits and the question-local artifact registry.
- Closure path: Tool results and a current artifact inventory enter history, allowing the next model call to choose further observations or end with an answer.
- Why this is / is not agent-owned: The router, registry and memory transport evidence. The model supplies the discretionary tool and answer decisions.
- Evidence: [`README.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/README.md#L251-L274), [`openvlharness/bootstrap.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/bootstrap.py#L260-L287), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L83-L116), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L136-L191), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L193-L216)
- Basis: structural
- Confidence: High for source-level reachability.
- Caveats: Requires model endpoints and configured tool dependencies for the selected capabilities.
- Boundary reachability: The published build_agent API returns the shipped MainAgent, whose generate path runs the model and capabilities.

## S2 — Coordination

- State: C
- Function: Attenuate shared backend contention between independent question runs through a capacity-group-specific constructor.
- Disturbance / variety regulated: Overlapping depth and camera requests compete for one GPU capacity group, and queued work could consume execution threads before acquiring the shared backend.
- Decisive decision or feedback right: Configure a shared capacity allocation and compose any adaptive allocation over the router's group-specific status and enforcement path.
- Decision owner: Deployment configuration owns the chosen capacity. The router enforces it deterministically. No autonomous coordination actor is mounted.
- Supporting / enforcement mechanisms: Depth/camera group mapping, group semaphore, pre-threadpool admission and per-group status.
- Closure path: An independently running question waits for capacity to return and receives its result or error after dispatch. Semaphore release permits the other question's pending work to advance.
- Why this is / is not agent-owned: The product supplies a conflict-specific resource gate and returns load evidence and execution outcomes. A developer would have to compose any discretionary coordination policy.
- Evidence: [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L62-L96), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L22-L29), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L95-L129), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L154-L162), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L191-L209), [`docs/runtime.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/docs/runtime.md#L112-L116), [`tests/test_services.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/tests/test_services.py#L375-L382)
- Basis: structural
- Confidence: High for the installed one-router coordination mechanism, bounded for ownership.
- Caveats: Capacity is process-local. Distributed scheduling and fairness policy are supplied externally.
- Boundary reachability: A configured tool server exposes the group gate, returned tool response and read-only backend status to shared-router deployments. Gates protect specific backends rather than asking callers to program a scheduler from generic messages.
- Distinct S1 units: Separate concurrent MainAgent question runs with fresh, autonomous model steps and isolated memory.
- Inter-S1 disturbance: A depth call from one run competes with a camera call from another for the same shared backend group.
- Attenuating coordination relation: Both backend identifiers map to one configured semaphore, acquired before execution consumes a worker.
- Feedback into subsequent S1 behaviour: The delayed call resumes after capacity returns and its result or error enters the relevant question's next decision. The dedicated load view is available to a composed coordination owner.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shared depth/camera capacity gate directly prevents simultaneous claims on the identified backend capacity.

## S3 — Inside-and-now control

- State: —
- Function: No discretionary organization-wide current-control loop was established.
- Disturbance / variety regulated: Question workloads may exceed token, iteration or backend limits or encounter degrading services.
- Decisive decision or feedback right: Runtime enforces fixed bounds and the model decides how to finish a single question. No shipped path revises whole-deployment commitments from the current view.
- Decision owner: No evidenced S3 owner. Developer selects initial configuration.
- Supporting / enforcement mechanisms: Iteration budgets, request retries and fallback, backend status, health and semaphores.
- Closure path: Limits, statuses and errors affect requests, but neither runtime nor operator readback provides a shipped decision-return path for reallocating commitments.
- Why this is / is not agent-owned: Deterministic limit enforcement and local tool selection do not establish whole-system discretionary control.
- Evidence: [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L136-L158), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L95-L129), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L131-L162), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L191-L209), [`openvlharness/bootstrap.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/bootstrap.py#L97-L127)
- Basis: structural
- Confidence: Moderate to high within the reviewed deployment.
- Caveats: A developer can use service status to build an external allocator.

### Absence scope

- Surfaces inspected: Inference stop/fallback, startup limit configuration, router health and backend status, and execution admission.
- Plausible first-party paths checked: Per-group queues as possible authority, changing a question's tool use after errors, and operator capacity supervision.
- Why no material first-party path remains: Status is read-only, capacity fixed by assembly and outcome selection is per-question. There is no sourced escalation or actor that changes deployment-level active commitments through a returned decision.

## S3* — Complementary audit

- State: —
- Function: No in-boundary complementary audit of operational answers was established.
- Disturbance / variety regulated: A prediction or tool trace may differ from the actual answer or source evidence.
- Decisive decision or feedback right: The inference loop reports a trajectory and tool-detection sidecars. Separate evaluators produce benchmark scores outside the runtime.
- Decision owner: No qualifying audit owner in the inference deployment. Offline evaluators act within the adjacent benchmark system.
- Supporting / enforcement mechanisms: Raw trace export, artifact recording, packaged benchmark evaluators and local tool output validation.
- Closure path: The scoring path evaluates saved predictions and writes diagnostic reports. It does not feed an audit finding back into the assessed runtime's operation or control.
- Why this is / is not agent-owned: Model scoring exists in the benchmark layer. The question runtime does not mount that adjudicator or consume its dispositions.
- Evidence: [`pyproject.toml`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/pyproject.toml#L26-L27), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L83-L116), [`evaluation_kit/cli.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/evaluation_kit/cli.py#L348-L349), [`evaluation_kit/cli.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/evaluation_kit/cli.py#L601-L639), [`README.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/README.md#L413-L424)
- Basis: structural
- Confidence: High for the inference versus scoring boundary.
- Caveats: Offline evaluation provides real evidence about benchmark predictions under its own system boundary.

### Absence scope

- Surfaces inspected: Model inference and result recording, raw trace, tool sidecars, eval-only and evaluation/trajectory merge paths.
- Plausible first-party paths checked: Independent judge of saved answers, native tool-output checks and whether correctness feeds retries or live control.
- Why no material first-party path remains: Evaluation writes scores and diagnostic evidence to results/trajectories. The question loop uses tool evidence and inference failure handling but never receives the judge result to revise live operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied external-and-future capability adaptation loop was established.
- Disturbance / variety regulated: Web conditions, backends and models may change across questions.
- Decisive decision or feedback right: A question agent can choose another tool using current observations. Configured model and tool capabilities are fixed for the assembled runtime.
- Decision owner: No S4 decision owner established. Developer owns new assembly decisions.
- Supporting / enforcement mechanisms: Per-question environment updates, web/search tools, configurable model profiles and evaluation presets.
- Closure path: Inventory closes the current question's feedback. Fresh question memory and static capability factory provide no shipped prospective adaptation decision.
- Why this is / is not agent-owned: Task-level use of external input and per-run state does not establish adaptation of future capability.
- Evidence: [`docs/runtime.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/docs/runtime.md#L32-L68), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L83-L96), [`openvlharness/agent/agent.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/agent/agent.py#L188-L216), [`openvlharness/bootstrap.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/bootstrap.py#L194-L216), [`openvlharness/bootstrap.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/bootstrap.py#L260-L287), [`docs/runtime.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/docs/runtime.md#L118-L121)
- Basis: structural
- Confidence: High for the chosen runtime boundary.
- Caveats: A separate product/research operator may use raw evidence to design later releases.

### Absence scope

- Surfaces inspected: Memory factory, Environment Update, fixed capability registration, web/model tool modes, benchmark outputs and profile configuration.
- Plausible first-party paths checked: Cross-run learning, environmental sensing through search, deployment changes selected from offline evaluation.
- Why no material first-party path remains: Search and inventories serve local questions and are reset across runs. The reviewed implementation does not derive or return a future capability adaptation from those results.

## S5 — Policy and identity

- State: —
- Function: No runtime identity or ultimate-policy adjudication path was established.
- Disturbance / variety regulated: Policy and capability choices such as allowed tools delimit operation.
- Decisive decision or feedback right: Startup loader validates supplied configuration; there is no supported decision-return process for unresolved identity policy.
- Decision owner: External deployer supplies configuration. No qualifying S5 decision loop is evidenced.
- Supporting / enforcement mechanisms: YAML schema, fixed agent identity field, model prompt and restrictions on task arguments.
- Closure path: A deployment change can replace setup, but the runtime surfaces do not refer an identity concern to that owner and incorporate its decision.
- Why this is / is not agent-owned: The shipped system applies preselected policy values without supplying an ultimate-policy adjudication mechanism.
- Evidence: [`openvlharness/bootstrap.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/bootstrap.py#L83-L127), [`openvlharness/services/server.py`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/openvlharness/services/server.py#L164-L178), [`docs/runtime.md`](https://github.com/uclanlp/OpenVLHarness/blob/c080224d31774fcf1b3c0f55abb71d143f7f3501/docs/runtime.md#L158-L185)
- Basis: structural
- Confidence: Moderate to high.
- Caveats: Maintainer policy and deploying institutions sit outside the declared boundary.

### Absence scope

- Surfaces inspected: Bootstrap identity/policy schema, packaged prompt and capability composition, service argument constraints and runtime ingress.
- Plausible first-party paths checked: Human deployment edit, model refusal and provider/profile policy selection.
- Why no material first-party path remains: Configuration validation and static prompts regulate operation. The assembled runtime has no sourced route for resolving and returning an ultimate identity decision.

## Distributed OSS parent arrangement

The deployer owns external configuration. No maintainer or repository governance responsibility is credited to the inference runtime.

## Self-hosted and non-human modes

The documented tool router can be deployed locally or separately with selected backends. The inferred ownership is bounded to one configured inference deployment and one router process when shared.

## Recursion

Separate question runs operate with fresh memory. An auxiliary code generator is task-local. Multiple runs can use a common backend group.

## Variety and escalation

Typed failures, retries, budgets, concurrency gates and artifact records address local disturbances. No distinct algedonic decision channel is evidenced.

## Evidence gaps

The assessment is based on the pinned source. Provider and GPU execution were not rerun. Benchmark claims, dataset scores and performance rankings are outside the assessed VSM grades.
