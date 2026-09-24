---
harness_id: leviath
project_name: Leviath
repository: https://github.com/GEMISIS/leviath
review_ref: 0d519eec063876c53e83bb94c7942df0f67f2701
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Leviath

## Review boundary

- System in focus: one first-party Leviath shared-world runtime/daemon organization at pinned revision `0d519eec063876c53e83bb94c7942df0f67f2701`, including the stable embedded `AgentWorld`, `WorldHost`/`PipelineWorld`, bundled agent blueprints, staged model/tool execution, shared inference/tool lanes, fan-out/sub-agent support, runtime watchdogs, interaction points, persistence/restore and live daemon control surfaces.
- Purpose and identity: run one or more autonomous model-driven agent workflows against user tasks and workspaces while preserving bounded execution, shared-resource coordination, current daemon health/control, recoverability and first-party review/recovery paths.
- Relevant environment: user tasks and interventions, workspaces/files/test commands, model/provider responses, tool results, shared provider/tool capacity, persisted run state, configuration/policy files and external MCP/model services.
- Standard-distribution boundary: first-party runtime, CLI daemon, bundled blueprints and documented self-hosted/embedded operation shipped by `GEMISIS/leviath` at the pinned revision. External model providers, MCP servers, user repositories and operator-authored custom blueprints remain external unless a first-party Leviath path itself supplies the relevant organizational relation.
- Credited operating / distribution surfaces: `AgentWorld`; `WorldHost` and `PipelineWorld`; staged autonomous inference/tool/transition runtime; shared per-model/per-provider inference pools and tool lane; daemon lane-health/relief loop; live `[limits]` reload into running worlds; bundled `coder` implementation/review/reassess flow; runtime stuck/workspace watchdogs; persistence/recovery and interaction infrastructure where they support those credited paths.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor workflows for developing Leviath; docs generators and tests as evidence-only surfaces; telemetry/logging when merely observational; static blueprint/config/policy text without a live organizational closure; provider/MCP implementations external to the running Leviath organization; examples/custom blueprints that are not shipped supported modes.
- First-party operating / deployment modes considered: the standard background daemon hosting multiple runs in one shared `PipelineWorld`; the stable embedded `AgentWorld`; bundled first-party agents including `coder`; attended operation with interaction points/tool approvals; and unattended/autonomous operation where the bundled blueprint permits it.
- Recursion level: the shared Leviath runtime/daemon is the primary system-in-focus. Individual autonomous runs are treated as S1 operational units at this daemon recursion when several coexist. Fan-out workers/sub-agents are counted only where their own model-driven work and parent relation are material; spawning alone is not treated as a lower viable recursion.
- Reviewed revision: `0d519eec063876c53e83bb94c7942df0f67f2701`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Leviath is a Rust agent runtime whose daemon hosts every loaded run inside one ECS `PipelineWorld`. Each run carries blueprint/stage state, context, model configuration and tool state. The world ticks a chained pipeline to dispatch model inference and tools, collect their results, update context, resolve stage outcomes and, where a stage exposes multiple ordinary edges, ask the model which stage should run next. The stable `AgentWorld` embedding surface assembles the same machinery without the CLI daemon.

The runtime is explicitly multi-run. A world-level `InferencePools` resource limits concurrent model requests across every agent by model and optionally by provider; agents unable to acquire capacity remain ready and retry after permit release wakes the world. A shared tool lane similarly bounds tool work. These are concrete cross-S1 coordination mechanisms because concurrent autonomous runs compete for the same finite upstream/tool capacity and the shared gates change when each run may next act.

`WorldHost` adds a daemon-wide current-control surface. It samples agent/lane occupancy and a whole-world progress fingerprint. When a tool lane remains saturated with queued work while no run moves for enough safety re-drives, the host automatically grants bounded extra tool capacity and later reclaims it after healthy cycles. The daemon also exposes this health through `lev ps`. Separately, the operator can change global `[limits]` such as inference pools, tool concurrency, watchdogs and fan-out ceilings; the daemon hot-reloads those settings into the running world without restart. The automatic path is deterministic rather than agent-owned, while the live operator path is an explicit parent-governed S3 mode.

The bundled `coder` blueprint supplies a materially independent audit path. Its autonomous `review` stage has read/list/bash but no write/edit tools, reads the implementation/changelog, directly re-opens changed files, reruns the verification commands, compares results with the recorded baseline, and either approves or routes specific required fixes back to `implement`. That direct workspace/test access can challenge the implementing stage's ordinary self-report and changes subsequent operation, so the supported `coder` mode establishes S3* rather than merely generic logging or same-path tracing.

Leviath also has strong runtime recovery and policy mechanisms: stuck detection from measured iteration/time/tool/edit signals, workspace-health checks, persistence/restore, provider/model fallbacks, config/policy hot reload, interaction points and tool approvals. These materially strengthen current operation but do not by themselves establish outside-and-then adaptation or identity/ultimate-policy closure.

Primary evidence:

- [`README.md`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/README.md) — shared-world daemon, staged agents, model routing, structured context, fan-out, interactions and operator surfaces.
- [`crates/leviath-runtime/src/lib.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/lib.rs) — stable `AgentWorld`, `WorldHost`/`PipelineWorld` layering and public runtime capabilities.
- [`crates/leviath-runtime/src/world.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/world.rs) — one ECS world over all agents, tick pipeline, world/lane snapshots and fixed-point execution.
- [`crates/leviath-runtime/src/pipeline/transition_choice.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/pipeline/transition_choice.rs) — explicit model inference owns ordinary multi-edge stage-choice decisions.
- [`crates/leviath-runtime/src/inference_pool.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/inference_pool.rs) — per-model/per-provider concurrency coordination across every agent in the world and retry-on-release closure.
- [`crates/leviath-runtime/src/host/health.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/host/health.rs) — whole-daemon lane/progress sensing, wedge detection, bounded relief and decay.
- [`crates/leviath-cli/src/daemon/live_limits.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/live_limits.rs), [`config_reload.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/config_reload.rs) and [`setup.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/setup.rs) — operator-selected daemon-wide limits hot-reload into live operation.
- [`crates/leviath-cli/src/commands/ps.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/commands/ps.rs) — operator-facing whole-daemon health, run progress and lane-pressure view.
- [`crates/leviath-cli/agents/coder/agent.leviath`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/agents/coder/agent.leviath) — bundled autonomous implement/review/reassess organization and read-only direct-evidence reviewer.
- [`crates/leviath-runtime/src/pipeline/watchdog.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/pipeline/watchdog.rs) — direct workspace checks, runtime-measured stuck detection and feedback into recovery transitions.
- [`crates/leviath-cli/src/daemon/policy_reload.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/policy_reload.rs) — live taint/policy enforcement, treated as constraint machinery rather than S5 ownership.

## S1 — Operations

- State: A
- Function: execute a user task through a model-driven staged agent loop that reads context, chooses tool actions and stage outcomes, absorbs returned environment/tool evidence and produces an operational result.
- Disturbance / variety regulated: task ambiguity, workspace state, tool/test output, model responses, runtime errors, newly discovered implementation facts and stage-specific completion conditions.
- Decisive decision or feedback right: within autonomous stages, select substantive tool actions and completion behavior and, when multiple ordinary next-stage choices exist, choose the next stage through a dedicated model inference.
- Decision owner: the model-driven Leviath agent running the selected first-party blueprint/stage.
- Supporting / enforcement mechanisms: `PipelineWorld` ECS schedule, inference/tool bridges, context regions, stage limits, transition parser, persistence, watchdogs, gates and provider/tool adapters.
- Closure path: task/context enters a model stage → model chooses actions/tools → first-party runtime executes/collects observations → context changes → the model continues or chooses a stage transition/completion → final output returns to the caller.
- Boundary reachability: bundled agents and the model/tool/stage pipeline are shipped through the standard daemon and `AgentWorld` surfaces; no downstream organizational actor must be added to obtain this loop.
- Why this is / is not agent-owned: deterministic runtime machinery constrains and transports the loop, but the operational next-action and ordinary multi-edge transition decisions are explicitly delegated to model inference rather than selected by the scheduler itself.
- Evidence: [`README.md`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/README.md); [`world.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/world.rs); [`transition_choice.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/pipeline/transition_choice.rs); [`coder/agent.leviath`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/agents/coder/agent.leviath).
- Basis: explicit + structural
- Confidence: high
- Caveats: condition edges such as `stuck`, hard iteration caps, gates and permissions are deterministic support/enforcement. They do not become agent-owned merely because they affect the run.

## S2 — Coordination

- State: C
- Function: damp cross-run resource interference among multiple autonomous S1 runs sharing the same daemon by serializing/bounding access to common inference-provider/model and tool capacity.
- Disturbance / variety regulated: concurrently active runs can collectively exceed model/provider concurrency, rate/spend capacity or shared tool-lane capacity, causing request stampedes, queue starvation or unbounded in-flight work.
- Decisive decision or feedback right: determine the coordination regime that bounds shared capacity and changes which S1 may proceed when common resources are saturated.
- Decision owner: the standard distribution supplies the S2-specific pool/lane relation and deterministic enforcement, but it does not supply an autonomous agent that owns revision of the cross-S1 coordination regime; configured/operator-selected limits remain outside autonomous S2 ownership.
- Supporting / enforcement mechanisms: per-model semaphores, optional provider-wide semaphores, shared tool-lane permits, `ReadyToInfer` retention on failed acquisition, wake-on-release and world-level occupancy accounting.
- Closure path: concurrent S1s request shared inference/tool capacity → the world-level pool/lane admits only permitted work and leaves excess work queued/ready → release of capacity wakes the world → waiting S1s are retried and subsequent behavior changes.
- Boundary reachability: the cross-agent pools and shared lanes are installed by the standard daemon/`PipelineWorld`, explicitly apply across every agent in the world and require no adopter-defined coordination primitive.
- Why this is / is not agent-owned: the function and feedback path are first-party and S2-specific, but the decisive capacity/coordination policy is configured and deterministically enforced rather than selected/revised by an autonomous coordinating agent. That supports `C`, not `A`.
- Evidence: [`inference_pool.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/inference_pool.rs); [`world.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/world.rs); [`host/health.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/host/health.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: queues/semaphores alone would not establish S2. The positive mapping relies on explicit world-wide cross-agent model/provider/tool contention and on the first-party backpressure relation designed to regulate it.
- Distinct S1 units: two or more independently model-driven Leviath runs hosted simultaneously in the shared daemon world, each pursuing its own task/workspace outcome.
- Inter-S1 disturbance: those runs contend for the same bounded provider/model request capacity and shared tool lane; without common attenuation, aggregate concurrency can exceed upstream/tool capacity even when each run is locally valid.
- Attenuating coordination relation: world-level model/provider pools and the shared tool lane cap simultaneous use and hold excess S1 work in a retryable queued/ready state rather than allowing every run to dispatch.
- Feedback into subsequent S1 behaviour: a run without a permit stays `ReadyToInfer`/queued; permit release wakes the tick loop so that run is retried later, directly changing when its next operational action occurs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is explicitly scoped to contention among all agents for common finite inference/provider/tool resources and exists to prevent unbounded concurrent pressure, not merely to move messages or order a workflow graph.

## S3 — Inside-and-now control

- State: C(P)
- Function: maintain a current whole-daemon view of active operations and intervene in shared resource/constraint settings when aggregate operation is wedged or when a parent operator changes the current operating regime.
- Disturbance / variety regulated: whole-daemon lack of progress under saturated lanes, excessive or inappropriate concurrency, provider/resource pressure, runtime watchdog settings and current fan-out/tool/inference limits that affect multiple S1 runs.
- Decisive decision or feedback right: choose/revise daemon-wide current resource and intervention parameters and apply them to current/subsequent S1 execution; in the constructor base, the runtime exposes a function-specific whole-world health/relief path but owns only deterministic rule execution.
- Decision owner: base `C` mode — no autonomous S3 decision owner is packaged; `WorldHost` deterministically executes configured health/relief rules. Parent `P` mode — the self-hosting operator owns live daemon-wide limit/policy choices exposed through first-party configuration/control surfaces.
- Supporting / enforcement mechanisms: `LaneSnapshot`, per-run progress fingerprint, dead-cycle counter, bounded automatic tool-lane relief/decay, `lev ps` health reporting, `ConfigReloader`, `LiveLimits`, ECS resource replacement and daemon housekeeping.
- Closure path: daemon-wide current state is observed → either the deterministic relief rule fires under the configured regime or an operator changes current `[limits]` after observing the daemon → first-party reload/apply code changes world pools/lanes/watchdogs/fan-out settings → later/current S1 execution runs under the new regime.
- Boundary reachability: both the automatic whole-world health/relief path and the operator live-limit reload path are wired into the standard daemon. `build_host` installs `LiveLimits` and a housekeeper that reapplies the latest config to the running world.
- Why this is / is not agent-owned: Leviath has real S3 current-control structure, but its autonomous base does not contain an AI agent that decides whole-daemon resource priorities/interventions. Deterministic relief therefore supports `C`; the separately operational self-hosting operator path establishes `(P)` rather than upgrading the base to `A`.
- Evidence: [`host/health.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/host/health.rs); [`commands/ps.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/commands/ps.rs); [`live_limits.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/live_limits.rs); [`config_reload.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/config_reload.rs); [`setup.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/setup.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: static concurrency values, watchdogs and gates are enforcement rather than S3 ownership. The positive function rests on the whole-world state/intervention relation; parent credit rests on the live operator→reload→current-operation path, not merely on editability of a config file.
- Whole-system current view: `WorldHost` reads counts/status across all hosted agents, per-model/per-provider occupancy, tool busy/queued/parked state, provider circuits and a progress fingerprint spanning the currently emitted run state; `lev ps` exposes the corresponding run/daemon health to the operator.
- Current-control decision scope: automatic base intervention may widen/reclaim shared tool-lane capacity under whole-daemon wedge/health conditions; the parent mode may revise shared inference/tool concurrency, watchdogs, circuit/retry settings, fan-out ceiling and other live limits that govern current and next actions across runs.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | No autonomous agent owner is packaged; deterministic `WorldHost` executes the configured relief/current-control relation | Whole-daemon lane saturation plus no observable run progress for the configured dead-cycle threshold | `relieve_if_wedged` widens shared tool capacity; healthy cycles reclaim granted permits, changing subsequent S1 access | `crates/leviath-runtime/src/host/health.rs`, `world.rs` |
| Parent (`P`) | Self-hosting Leviath operator | Operator observes current run/daemon state and changes global `[limits]`/related live settings | config reload → `LiveLimits::apply`/housekeeper → pools, lanes and world resources change without daemon restart → subsequent/current S1 operation follows the new regime | `crates/leviath-cli/src/commands/ps.rs`, `daemon/config_reload.rs`, `daemon/live_limits.rs`, `daemon/setup.rs` |

## S3* — Complementary audit

- State: A
- Function: independently challenge an implementation-stage claim that work is complete/correct by inspecting the actual changed workspace and rerunning verification before allowing the bundled `coder` organization to finish.
- Disturbance / variety regulated: the implementing stage can incorrectly report completion, omit verification, introduce regressions, violate the plan/original task or miss defects visible in the files/tests rather than in its own narrative.
- Decisive decision or feedback right: judge the changed implementation from direct artifact/test evidence and decide whether it is approved or must return to `implement` with required fixes.
- Decision owner: the autonomous model-driven `review` stage in the shipped `coder` blueprint.
- Supporting / enforcement mechanisms: read-only review tool repertoire (`read_file`, `list_dir`, `bash`, `context_read`), persisted `changelog`/`implementation`/`workflow`/`baseline` regions, graph transition back to `implement` and deterministic runtime/tool transport.
- Closure path: implement stage records/claims completion → separate review inference reads the claimed changes and directly inspects files/reruns tests → reviewer judges `APPROVED` or `NEEDS CHANGES` → failing review chooses the `implement` transition carrying compacted required fixes → implementation changes and is re-reviewed before completion.
- Boundary reachability: `coder` is a bundled first-party agent and its autonomous review stage is wired into the standard implement→review flow; an adopter does not have to compose an external evaluator to obtain this path.
- Why this is / is not agent-owned: the runtime enforces tool separation and routing, but the audit judgment about correctness/regression and the approve/revise choice belong to a model inference. The review stage is deliberately unable to repair what it audits, reducing self-certification coupling.
- Evidence: [`coder/agent.leviath`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/agents/coder/agent.leviath); [`transition_choice.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/pipeline/transition_choice.rs); [`pipeline/watchdog.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-runtime/src/pipeline/watchdog.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: not every custom Leviath blueprint necessarily includes this audit. The `A` claim is for the shipped supported `coder` mode. Runtime stuck/workspace watchdogs provide additional complementary direct-state checks but are deterministic and are not the autonomous owner credited here.
- Claim being audited: that the implementation satisfies the original task/approved plan and verification workflow without regressions or significant correctness/security defects.
- Ordinary reporting path: the implementing stage's own `implementation`/`changelog`, `decisions` and `test_results` records plus its assertion that work is ready for review.
- Complementary access path: the reviewer directly re-opens changed files with read tools, can inspect repository structure, and reruns the prescribed test commands via `bash`, comparing them with the stored baseline rather than trusting the implement-stage report.
- Independence boundary: review is a distinct autonomous inference stage reached after implementation, has no write/edit tools, and is explicitly instructed not to repair its own findings; its evidence access is direct to workspace/tests rather than limited to the producer's summary.
- Who acts on findings: the review model decides approval versus required changes; on failure the graph returns the findings to the model-driven `implement` stage, which changes the workspace and must pass review again.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop for the Leviath organization is established in the reviewed standard distribution.
- Disturbance / variety regulated: changing external model/provider capabilities, user needs, tools, policies and future threats/opportunities are encountered by the runtime, but no packaged path converts such distinctions into future-oriented organizational adaptation options and returns them into present capability as S4.
- Decisive decision or feedback right: none established for prospective adaptation of the Leviath organization.
- Decision owner: none established.
- Supporting / enforcement mechanisms: provider capability priming/reload, policy/config hot reload, persistence/restore, context compaction, runtime stuck/reassess recovery, dynamic tool/provider state and first-party task-level research/planning stages.
- Closure path: no external/future sensing → adaptation-option development → return into current capability/S3 loop was found.
- Why this is / is not agent-owned: task-level prototype/reassess stages adapt the route for the current user task, while reload/persistence mechanisms react to present configuration/environmental state. Neither establishes a prospective organizational intelligence conversation with current capability.
- Evidence: [`README.md`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/README.md); [`coder/agent.leviath`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/agents/coder/agent.leviath); [`daemon/setup.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/setup.rs); [`daemon/live_limits.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/live_limits.rs).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: downstream users can author research/adaptation stages in Leviath's general blueprint language. Generic extensibility does not establish a first-party S4 constructor path without S4-specific semantics.

### Absence scope

- Surfaces inspected: runtime world/pipeline and provider/tool reload paths; bundled `coder` discover/plan/prototype/implement/review/reassess flow; persistence/restore; configuration and policy hot reload; provider capability setup; documented fan-out/research and interaction surfaces.
- Plausible first-party paths checked: provider capability discovery/fallback; dynamic tool/provider refresh; current-task prototype and reassessment; persisted context/learning-like state; configuration/policy reload; telemetry/health feedback.
- Why no material first-party path remains: the inspected mechanisms either regulate current task execution/current environment or store/reload existing state. None supplies future/environment modeling that develops organizational adaptation options and feeds them back into present capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the shared Leviath runtime/daemon recursion.
- Disturbance / variety regulated: ordinary tool-risk, data-taint, plan-approval, sandbox, resource-limit and operator intervention questions are regulated, but no identity-level or ultimate-policy conflict is classified and closed as S5.
- Decisive decision or feedback right: none established for identity/ultimate-policy questions.
- Decision owner: none established.
- Supporting / enforcement mechanisms: static and scripted taint policy, tool permissions/approvals, sandbox/network/read-path constraints, interaction points, operator configuration and ordinary run pause/resume/kill controls.
- Closure path: no identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → return-to-operation governance loop was found.
- Why this is / is not agent-owned: policy files, gates and task-level human approvals constrain execution, but they do not themselves decide what Leviath's identity/ultimate policy is. The operator's S3 current-control mode concerns live resource/operating constraints, not S5 authority.
- Evidence: [`daemon/policy_reload.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/daemon/policy_reload.rs); [`coder/agent.leviath`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/agents/coder/agent.leviath); [`commands/ps.rs`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/crates/leviath-cli/src/commands/ps.rs); [`README.md`](https://github.com/GEMISIS/leviath/blob/0d519eec063876c53e83bb94c7942df0f67f2701/README.md).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: an adopter can encode identity/policy decisions in a custom blueprint or surrounding institution. That specialization is a separate system-in-focus and cannot donate S5 to the reusable standard distribution.

### Absence scope

- Surfaces inspected: taint/policy reload and gate machinery; tool permissions and approvals; interaction points including plan approval; daemon/operator config/control; blueprint stage/transition semantics; bundled `coder` human checkpoints.
- Plausible first-party paths checked: human plan approval; tool/taint clearance; policy.toml/scripted gate decisions; config edits; pause/resume/kill; stage transition authority.
- Why no material first-party path remains: all inspected parent/human paths concern ordinary task acceptance, permissions, safety constraints or current daemon operation. None identifies an identity/ultimate-policy matter and routes it to a legitimate ultimate authority whose returned decision governs subsequent operation as S5.

## Recursion

At the assessed daemon recursion, concurrently hosted autonomous runs are operational S1 units coupled through shared world resources. A bundled fan-out worker or sub-agent can itself be model-driven, but Leviath's spawn relation alone is not evidence that every child is a viable lower recursion with its own complete metasystem. The assessment therefore credits only function-specific parent/child evidence and does not infer recursive viability from nesting.

## Variety, escalation and closure

Leviath attenuates operational variety through stage-local tool/model/context declarations, structured context regions, shared concurrency pools, gates, retries and watchdogs. It amplifies regulatory capacity through model-driven stage transitions, sub-agents/fan-out, direct human interaction points, persistence/recovery and the bundled review/reassess loops.

Exceptional current-operation conditions have concrete return paths: a runtime-measured stuck condition writes evidence into `stuck_report` and routes to `reassess`; failed independent code review routes back to `implement`; whole-daemon lane wedge detection can alter shared tool capacity; operator limit edits are hot-reloaded into current operation. These paths are classified by the organizational functions they actually perform rather than treated as a separate VSM function.

## Evidence gaps

No material evidence gap remains that requires `?` at this pinned boundary. The main boundary-sensitive conclusions are explicit: `S2=C` depends on the shared-daemon recursion, `S3=C(P)` separates deterministic constructor/current-control machinery from the operator-owned live mode, and `S3*=A` is credited specifically to the bundled `coder` mode rather than assumed for arbitrary custom blueprints.