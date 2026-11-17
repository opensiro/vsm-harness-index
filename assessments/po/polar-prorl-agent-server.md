---
harness_id: polar-prorl-agent-server
project_name: Polar (ProRL Agent Server)
repository: https://github.com/NVIDIA-NeMo/ProRL-Agent-Server
review_ref: ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Polar (ProRL Agent Server)

## Review boundary

- System in focus: One deployed Polar rollout service with first-party gateway fleet and standard shipped agent launchers, but not an external RL trainer or a third-party agent's own policy/governance.
- Purpose and identity: Dispatch and observe real model-directed agent rollouts at scale, capture their trajectories and return evaluable results to a requesting training/client process.
- Relevant environment: Public agent executables/SDKs, configured inference endpoints, ephemeral execution runtimes, multiple gateway nodes and operator-facing fleet API.
- Standard-distribution boundary: First-party rollout server, gateways, launcher presets, model proxy, runtime setup, stage-aware scheduler and trajectory/evaluator interfaces.
- Credited operating / distribution surfaces: Shipped agent launcher modes that actually execute model-backed subprocesses; first-party scheduling, callback, status and drain paths.
- Adjacent first-party surfaces excluded from ownership: Demonstration benchmark/test scripts, Slime bridge/trainer, external RL update loop, native cognition of upstream agent CLIs, CI, research paper and GitHub maintainer governance.
- First-party operating / deployment modes considered: Packaged preset agent-run service, configurable shell/import-path variants (not independently owned agents), fleet operator drain controls and scorer/trainer callback mode.
- Recursion level: One Polar deployment's service portfolio of concurrent task-specific agent sessions, under a local operator; each launched external agent is a separate execution unit.
- Reviewed revision: ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The rollout manager expands client tasks into sessions, the pipeline places them on healthy gateways using stage-aware reservations, and each gateway prepares a runtime and executes an actual selected agent launcher. Built-in presets adapt many external coding/assistant CLIs and a generic shell harness. Model traffic passes through a proxy so calls become captured trajectories. Evaluators optionally produce reward metadata returned to the **external** trainer/client, not automatically to the next active agent. The operator-facing service exposes fleet health, task status, and node drain. [overview](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/README.md); [agent boundary](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/agent/README.md); [rollout service](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/README.md); [node scheduler](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/balancer.py); [trajectory](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/trajectory/README.md); [evaluators](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/trajectory/evaluator/README.md).

## Operational model

At the operative boundary, a launched external agent owns substantive model/tool decisions in its task, while Polar is intentionally agent-neutral: it schedules, supplies runtime and inference proxy, captures and evaluates. The first-party service nevertheless packages the mode in which model-backed agents run under its launched sessions. Shared gateway capacity is regulated by deterministic scheduler rules, and a parent operator can remove active gateway capacity using the same live scheduler. Trajectory scores and RL policy changes belong to outside trainers unless a complete first-party return path is separately proven.

## S1 — Operations

- State: A
- Function: Execute an externally supplied agent's model-directed actions for an operator-submitted task inside a Polar-prepared runtime.
- Disturbance / variety regulated: A task requires variable model-chosen steps and environmental tool observations.
- Decisive decision or feedback right: Select the agent's next model/tool action and adjust to environment observations during its own run.
- Decision owner: The launched model-backed agent subprocess selected from a shipped preset, not Polar's scheduling or inference proxy.
- Supporting / enforcement mechanisms: Bundled BaseHarness launchers, runtime setup, injected proxy endpoints, completion capture and result callback.
- Closure path: The launched agent consumes its environment/model responses and continues or ends its task; the Polar gateway captures its trajectory and returns terminal results to the requesting client.
- Boundary reachability: Polar ships actual launcher presets for Codex, Claude Code, Pi, OpenCode and others, and the first-party gateway runs their command steps in the standard deployment. An installed external agent and configured model backend are required.
- Why this is / is not agent-owned: Without the external agent subprocess, Polar can schedule and record sessions but cannot choose the next semantic action. The operational decision is agent-owned *inside the supported shipped launcher mode*, not owned by the Polar scheduler.
- Evidence: [overview](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/README.md); [agent boundary](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/agent/README.md); [base harness](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/agent/base.py); [harness factory](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/agent/factory.py); [pipeline](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/pipeline.py).
- Basis: structural
- Confidence: medium
- Caveats: This is the bounded composite agent-execution mode; Polar's native service remains intentionally agent-neutral. No live GPU/provider execution was reproduced.

## S2 — Coordination

- State: C
- Function: Attenuate shared gateway capacity and lifecycle contention among concurrent agent session units.
- Disturbance / variety regulated: Parallel sessions can overload a gateway's run/init/post-run worker pools and compete with draining or unhealthy nodes.
- Decisive decision or feedback right: Select a healthy non-draining node under stage-aware capacity; reject excess admission and retry/reassign failed dispatch.
- Decision owner: Configured deterministic NodeScheduler manages immediate placement. An independently deciding agent for inter-session resource coordination would require further composition.
- Supporting / enforcement mechanisms: Heartbeat freshness, stage-specific pressure, dispatch reservations, drain handling and gateway callbacks.
- Closure path: An admitted session changes reservations and node pressure, influencing where subsequent sessions dispatch. Failed gateway dispatch releases the reservation and leads to another eligible node or timeout.
- Boundary reachability: The scheduler runs in the packaged rollout server; every session passes through pipeline.acquire_node and corresponding response/health handling.
- Why this is / is not agent-owned: The bounded regulation is real and function-specific, but placement is selected by a fixed algorithm rather than an autonomous organizational decision-maker.
- Distinct S1 units: Distinct agent-run sessions distributed across gateway nodes, each performing its own model-directed task.
- Inter-S1 disturbance: Concurrent sessions contend for initialization, inference/run slots and postrun capacity; unhealthy or draining nodes can disrupt unrelated runs.
- Attenuating coordination relation: Stage-aware pressure and reservation gates regulate shared capacities and exclude unsuitable nodes.
- Feedback into subsequent S1 behaviour: Reservations, heartbeat metrics and node drains alter later admission/placement; failed dispatch is retried against a fresh eligible node.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The relation explicitly regulates cross-session resource interference using observed pool pressure and reservations, rather than only forwarding RPC calls.
- Evidence: [node scheduler](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/balancer.py); [pipeline](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/pipeline.py); [rollout service](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/README.md); [server API](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/server.py).
- Basis: structural
- Confidence: high
- Caveats: Only distributed gateway scheduling interference is established. The scheduler does not negotiate semantic task conflicts.

## S3 — Inside-and-now control

- State: P
- Function: Expose and apply present fleet control over active and pending agent rollouts.
- Disturbance / variety regulated: Current gateway conditions may require withholding new work, draining a node or changing the available execution fleet.
- Decisive decision or feedback right: Inspect whole-fleet/node and task status, decide to drain a specified node, and thereby change subsequent scheduling.
- Decision owner: The legitimate operator of the Polar deployment using the first-party fleet API; the NodeScheduler only enforces the selected drain condition.
- Supporting / enforcement mechanisms: Health, per-stage node metrics, GET /rollout/status, GET /nodes and DELETE /nodes/{id}, scheduler draining flag.
- Closure path: Operator DELETE to drain node → NodeScheduler marks it draining → later acquire_node excludes it until in-flight work completes and the node is removed.
- Boundary reachability: The production FastAPI server publishes this operator-facing path, which directly updates the same scheduler used by the live pipeline.
- Why this is / is not agent-owned: The operator chooses which node to remove from present capacity; deterministic scheduling applies that decision without owning it.
- Whole-system current view: The server exposes live nodes and aggregated task/rollout progress for one deployed Polar cluster.
- Current-control decision scope: Admission and drain of current gateway resources rather than the contents of an externally supplied agent's task.
- Evidence: [server API](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/server.py); [node scheduler](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/balancer.py); [rollout service](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/README.md).
- Basis: structural
- Confidence: medium
- Caveats: No autonomous S3 supervisor is established and current-control decisions are limited to cluster resource operation, not external trainer strategy.

## S3* — Complementary audit

- State: —
- Function: No integrated, first-party, independent corrective audit of an operational agent's claims was established at the Polar rollout boundary.
- Disturbance / variety regulated: A returned trajectory or reward may be inaccurate, but the shipped service's reward/evaluation surface is primarily task scoring for an external trainer.
- Decisive decision or feedback right: No distinct in-boundary auditor with an authority path returning independent corrective findings to the ongoing agent or Polar current-control system is established.
- Decision owner: Not established; external evaluation and trainer authority remain separate.
- Supporting / enforcement mechanisms: Trajectory builders, task evaluators, optional rubric judge and captured completion records are data/scoring surfaces.
- Closure path: An evaluation score returns via the rollout result to the client/trainer; no first-party corrective-audit decision is shown changing a subsequent Polar operation at the declared boundary.
- Why this is / is not agent-owned: Scoring a benchmark or rubric is not enough for S3* absent a complementary evidence path, independent audit ownership and corrective feedback into the assessed organization.
- Evidence: [trajectory](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/trajectory/README.md); [evaluators](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/trajectory/evaluator/README.md); [rollout service](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/README.md).
- Basis: structural
- Confidence: medium
- Caveats: A downstream trainer may build a separate learning/audit process; its decision path is outside this server boundary.

### Absence scope

- Surfaces inspected: Trajectory/evaluator interfaces and implementations, rollout callbacks and manager/pipeline return path.
- Plausible first-party paths checked: Rubric judge, test-on-output, SWE-bench/Harbor verification, completion capture and client callback.
- Why no material first-party path remains: These emit scores or traces to external training/evaluation clients; no included complementary auditor makes a corrective organizational decision that returns to regulate the next Polar agent session.

## S4 — Outside-and-then intelligence

- State: —
- Function: No built-in prospective adaptation loop with Polar-owned judgment and capability return was found.
- Disturbance / variety regulated: New model releases, provider reliability and future rollout/training needs might require capability adaptation.
- Decisive decision or feedback right: No shipped S4-specific agent or parent decision/return path in Polar chooses prospective changes from environmental intelligence.
- Decision owner: External trainer, developer and deployment owner decide future changes; not represented as a closed first-party adaptive function.
- Supporting / enforcement mechanisms: Health feedback, load scheduling, reusable registries, configurable agent launchers and returned trajectories.
- Closure path: No prospective adaptation closure is established; task scoring is returned for external training and is not automatically installed as Polar capability.
- Why this is / is not agent-owned: Fixed reactive gateway scheduling and an external RL training pipeline cannot be converted into an autonomous Polar adaptation judgment.
- Evidence: [overview](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/README.md); [trajectory](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/trajectory/README.md); [evaluators](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/trajectory/evaluator/README.md); [node scheduler](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/balancer.py); [topology](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/config/README.md).
- Basis: structural
- Confidence: high
- Caveats: RL policy training can exist downstream; the selected system boundary deliberately excludes its authority.

### Absence scope

- Surfaces inspected: Root roadmap, topology, rollout manager/scheduler, builder/evaluator registries and external trainer interfaces.
- Plausible first-party paths checked: Model reward feedback, dynamic load balancing, gateway recovery, custom harness/evaluator registration and roadmap.
- Why no material first-party path remains: Returned reward and trajectories do not themselves select and apply a future deployment/capability change; surrounding trainer and developer actors are external.

## S5 — Policy and identity

- State: —
- Function: A standing ultimate-policy identity decision and return path is not established for the Polar rollout service.
- Disturbance / variety regulated: Different users may choose accepted agents, runtime topology and evaluation criteria.
- Decisive decision or feedback right: The task requester chooses per-run agent/evaluator, while deployment configuration selects fixed node capacities; no identified in-boundary institution adjudicates identity-level policy and returns it to govern later operations.
- Decision owner: Task client and deployment configurator for narrower choices, not an evidenced S5 function at this recursion.
- Supporting / enforcement mechanisms: Strict Pydantic topology, task schema, endpoint policies, and evaluator registry.
- Closure path: Configuration affects launch and per-request execution; no first-party identity-level matter → legitimate authority → binding decision → future-operation cycle is demonstrated.
- Why this is / is not agent-owned: A configuration schema or hard parameter gate is a supporting mechanism, not evidence that Polar owns or supplies an S5 identity/ultimate-policy decision path.
- Evidence: [topology](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/config/README.md); [agent boundary](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/agent/README.md); [server API](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/server.py); [rollout service](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/blob/ff9a83605ba0b44fed1331ec60cc9d9f31b1e1d1/src/polar/rollout/README.md).
- Basis: structural
- Confidence: medium
- Caveats: A real organization operating Polar can have external S5 governance, which this artifact does not assess.

### Absence scope

- Surfaces inspected: Topology configuration, public API, agent/evaluator selectors, roadmap and runtime modes.
- Plausible first-party paths checked: Owner-authored topology, per-task configuration and registry extensions, external RL policy source.
- Why no material first-party path remains: These expose low-level constraints and task parameters but no in-boundary standing ultimate-authority issue/decision/returned organizational closure.

## Distributed OSS parent arrangement

The authority to deploy and drain one local Polar fleet belongs to that deployment's operator. The upstream NVIDIA project maintainers, external agent developers and trainer authors do not govern a specific private deployment's live sessions by default.

## Self-hosted and non-human modes

The service and gateway are self-hosted and agent-neutral. Its first-party launchers work only when configured upstream agent binaries and a model backend are actually available. The operator can supervise the fleet and drain nodes. External trainers and any learning policy are separate from this runtime mode.

## Recursion

Each actual agent-run session is an S1 operational unit for the defined service portfolio; its semantic agent decisions belong to the provider-backed subprocess. Polar's first-party scheduler coordinates shared gateway resources; the local operator owns fleet control. This does not imply that the rollout daemon is an internally planning agent or a fully viable organization.

## Variety and escalation

Heartbeat, stage pressure and dispatch reservations attenuate shared-resource contention. Session timeouts, callbacks, node failures and duplicate-dispatch evidence are handled by bounded runtime recovery. The parent operator may drain a gateway and thereby change future admission. No automatic transfer of autonomy or future training results into current Polar policy is credited.

## Evidence gaps

Source-first structural review only: no live multi-GPU/model run, no external trainer or independent reviewer executed. Inclusion credits a **supported shipped integration mode** with real model-directed agents launched as first-party task subprocesses, not model autonomy within the Polar scheduler. S3* evaluators are outcome/reward scorers; an externally controlled trainer may add independent audit, learning or S5 governance beyond the assessed distribution.
