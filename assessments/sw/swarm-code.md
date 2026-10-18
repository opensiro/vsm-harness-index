---
harness_id: swarm-code
project_name: swarm-code
repository: https://github.com/skyblanket/swarm-code
review_ref: 53007abac1d521e32c2508af5328412bd6bbb67b
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# swarm-code

## Review boundary

- System in focus: swarm-code's first-party terminal coding-agent composition at frozen revision `53007abac1d521e32c2508af5328412bd6bbb67b`, including its `Agent` model/tool loop, first-party coding tools and execution policy, sessions/search, skills, background process tracking, `/flows` parallel-workflow controller, scheduler, memory and the experimental council wrapper.
- Purpose and identity: perform repository-facing coding work and expose first-party operational mechanisms for bounded subagent execution, parallel multi-agent workflows, recurring headless jobs and repository-aware advisory review.
- Relevant environment: user prompts, repository/filesystem state, tool/shell results, model-provider responses, child-process status/logs, flow definitions and phase/task state, configured skills/MCP/hooks, persistent memory/session state and operator-authored permissions/trust configuration.
- Standard-distribution boundary: swarm-code's own `sw` application and the concrete use it makes of swarmrt primitives are inside. `swarmrt` remains a framework/runtime dependency and does not donate generic behavior that the pinned product does not instantiate. External model endpoints, MCP servers and user-authored hooks/skills are dependencies/configuration.
- Credited operating / distribution surfaces: `README.md`; `src/agent.sw`; `src/Flows.sw`; `src/background.sw`; `src/ToolExecutor.sw`; `src/ToolRegistry.sw`; `src/scheduler.sw`; `scripts/council.sh`; first-party session/memory/skills modules and the standard interactive/headless entrypoints.
- Adjacent first-party surfaces excluded from ownership: tests and review documents as authority by themselves, release/contributor workflows, generic swarmrt capabilities not concretely invoked by swarm-code, external provider behavior, and user-authored flow/skill/hook content beyond the product's runtime semantics.
- First-party operating / deployment modes considered: interactive REPL; headless `-p`/JSON runs; synchronous `task` subagents; `/flows` multi-process workflows; recurring scheduler jobs; MCP integration; persistent sessions/memory; experimental `scripts/council.sh`.
- Recursion level: the assessed organization is one swarm-code product instance plus the full headless swarm-code child processes instantiated by `/flows`. Those child processes each run the same first-party model/tool coding loop and therefore qualify as distinct subordinate S1 units at this recursion. The synchronous in-process `task` subagent path is additional delegated operation but is not required for the positive simultaneous-S1 findings.
- Reviewed revision: `53007abac1d521e32c2508af5328412bd6bbb67b`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`src/agent.sw` owns the repository-facing coding loop. The model receives the current message history and tool schemas, emits structured tool calls, swarm-code executes them through the shared `ToolExecutor` policy boundary, appends tool results to history and calls the model again until no tool calls remain or a bounded stop condition is reached. This is a first-party operational loop; provider endpoints are transport/model dependencies rather than the owner of tool execution.

The built-in `task` tool runs a bounded synchronous subagent loop with a fresh guardrail table and execution-context-specific tool allow-lists. That path supplies isolated delegated reasoning but does not by itself establish simultaneous S1 interaction.

`/flows` is materially different. `src/Flows.sw` turns a workflow definition into phases containing task commitments. Each task is launched through `Background.launch` as a separate headless `swarm-code -p ... --no-resume` subprocess. A phase may therefore contain multiple simultaneously active complete swarm-code S1s. The controller maintains explicit per-task state (`pending`, `running`, terminal status, child id, timestamps and log statistics), polls all phases every 500 ms, computes the current number of running and queued tasks, admits only as many queued tasks as the configured concurrency cap permits and refills capacity as running tasks terminate. Default maximum parallelism is four unless `SWARM_CODE_FLOWS_MAX_PARALLEL` changes it.

The same controller also owns current workflow progression. It knows every phase/task commitment, launches the first phase, continuously refreshes child statuses, waits until all tasks in the current phase are terminal, then starts the next phase; after the last phase it marks the workflow done. A stop-file can abort the flow. This is deterministic current-control over a subordinate operational population rather than a model-owned task-allocation decision: the user supplies the workflow definition, while code executes the live admission and phase-transition policy.

The scheduler is a separate recurring-execution mechanism. It stores operator/model-created prompt schedules, and the heartbeat deterministically dispatches due headless swarm-code processes. Jobs are fire-and-forget and their output is written to telemetry files. Scheduling therefore extends when an S1 runs, but no future-facing intelligence actor senses external conditions, evaluates strategic alternatives and changes current organizational capability.

The experimental council is an advisory review surface. `scripts/council.sh` launches three bounded read-only repository-aware panel agents (`architect`, `skeptic`, `operator`) in parallel and then supplies their independent summaries to a no-tools judge, which produces consensus, contradictions, blind spots, a recommendation and confidence. This is meaningful independent review evidence, but the frozen product does not wire the judge verdict back into the primary Agent or `/flows` controller as a corrective command/commitment. The script prints the synthesis to its caller, so complementary-audit return closure is not established.

Primary evidence:

- [`README.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/README.md)
- [`src/agent.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/agent.sw)
- [`src/Flows.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw)
- [`src/background.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/background.sw)
- [`src/ToolExecutor.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/ToolExecutor.sw)
- [`src/ToolRegistry.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/ToolRegistry.sw)
- [`src/scheduler.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/scheduler.sw)
- [`scripts/council.sh`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/scripts/council.sh)

## Operational model

In the ordinary coding mode, one model-backed swarm-code S1 chooses and executes repository/tool actions. In a `/flows` run, the product instantiates a bounded population of additional full swarm-code S1 processes from a user-supplied workflow. The runtime maintains the live state of that population, prevents more than the configured number from running at once, launches queued commitments as capacity becomes free and moves the organization between workflow phases only when the prior phase's commitments are terminal.

The positive S2 and S3 findings therefore arise from two different deterministic responsibilities. S2 is the feedback controller that attenuates simultaneous resource demand by limiting the number of active full S1 processes and refilling slots only from observed current capacity. S3 is the broader whole-flow commitment controller that maintains the current phase/task view and decides which queued commitments are admitted now, when the organization may transition to the next phase and when the workflow is complete or aborted.

## S1 — Operations

- State: A
- Function: perform environment-facing coding work by interpreting a user/task objective, selecting repository/tool actions, executing them and revising later action from returned evidence.
- Disturbance / variety regulated: repository state, implementation alternatives, shell/file/network/tool results, provider uncertainty, context pressure, tool failures and changing task evidence.
- Decisive decision or feedback right: choose the next task-specific tool action and revise that choice from returned tool/model evidence.
- Decision owner: the model-backed swarm-code Agent in an interactive/headless parent or `/flows` child process.
- Supporting / enforcement mechanisms: structured tool-call loop; `ToolExecutor`; `ToolRegistry`; permissions/guardrails; sessions/context compaction; skills/MCP; provider adapters; crash recovery; step bounds.
- Closure path: current task/history → model selects tool/action → first-party executor performs/denies it → result is appended to history → same model actor chooses another action or final answer.
- Boundary reachability: the shipped interactive and headless entrypoints instantiate this loop directly; `/flows` launches the same product binary as subordinate S1 processes.
- Why this is / is not agent-owned: removing the model actor while retaining the executor, sessions and tool registry leaves enforcement machinery but removes the open-ended task-specific decision of what coding action to take next.
- Evidence: [`src/agent.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/agent.sw); [`README.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: headless and dangerous actions remain constrained by first-party permission/hard-deny policy; those constraints do not replace the model's ordinary coding discretion.

## S2 — Coordination

- State: C
- Function: attenuate runtime-resource interference among multiple simultaneously active subordinate swarm-code S1 processes by bounding the active population and feeding observed completion/capacity back into subsequent admission.
- Disturbance / variety regulated: a workflow phase may contain more full coding-agent commitments than should execute simultaneously; unbounded spawning competes for CPU, memory, model/provider capacity and other host resources. The implementation explicitly replaced behavior that could fork an entire large phase at once with bounded queued admission.
- Distinct S1 units: every launched `/flows` task is a separate headless `swarm-code` subprocess running the product's complete Agent/model/tool loop, with its own prompt/model/process lifecycle.
- Inter-S1 disturbance: concurrently running full agent processes consume the same host/provider resource envelope; excessive simultaneous execution creates resource contention/oversubscription even when their semantic tasks are independent.
- Attenuating coordination relation: `flows_max_parallel()` defines the active cap; `launch_quota()` counts current running and queued tasks and computes free capacity; `fill_phase_slots()` starts only the allowed queued subset; the render loop re-polls status and refills slots after child termination.
- Feedback into subsequent S1 behaviour: child process status is refreshed every polling cycle. A running child occupies a slot and prevents further queued S1 admission; once it becomes terminal, the observed free slot permits a later queued S1 to start. The relation therefore changes which S1 is active as a function of current inter-S1 resource occupancy.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive claim is not based on having several agents or a workflow queue. It is based on a concrete dynamic attenuation path over simultaneous S1 resource demand: observe active population → compute capacity → admit/withhold another S1 → observe completion → refill.
- Decisive decision or feedback right: determine from live task occupancy whether another subordinate S1 may enter the active set now.
- Decision owner: deterministic first-party `/flows` controller.
- Supporting / enforcement mechanisms: `Background.launch`; per-task process/status records; `flows_max_parallel`; `count_running`; `count_queued`; `launch_quota`; `fill_phase_slots`; 500 ms status polling.
- Closure path: current child-process statuses → running/queued counts → free-slot computation → launch or withhold queued child → changed active population → next poll observes the resulting occupancy.
- Boundary reachability: `/flows` is a documented shipped product command and launches first-party swarm-code binaries; no application-authored coordinator is required beyond supplying workflow data.
- Why this is / is not agent-owned: the user/model supplies prompts/workflow content, but the material attenuation decision is mechanically derived from current occupancy and the configured cap. Removing all model judgment does not remove the admission controller, so the function is code-owned.
- Evidence: [`src/Flows.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw); [`README.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the credited S2 relation is resource/concurrency attenuation. No claim is made that `/flows` autonomously negotiates semantic conflicts, filesystem overlap or contradictory goals among concurrently running children.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current set and lifecycle of subordinate workflow commitments by maintaining the whole `/flows` phase/task state, admitting queued commitments into execution, advancing phases only after current commitments terminate and marking the organization complete or aborted.
- Disturbance / variety regulated: current workload population, queued versus running commitments, child completion/failure, phase dependencies/order, active-capacity changes and user-requested workflow abort.
- Whole-system current view: `Flows` state contains the complete workflow phase list and every task's label, prompt/model, child id, current status, exit code, timing and execution statistics. `refresh_all_phases` polls the status of all launched tasks across all phases before current-control decisions are made.
- Current-control decision scope: the controller launches the first/current phase, selects which queued commitments become active under the current cap, detects when all tasks in the current phase are terminal, starts the next phase, declares the whole flow done after the last phase, and changes the organizational state to aborted on the supported stop signal.
- Decisive decision or feedback right: determine which current workflow commitments execute now and when the organization may transition between current operational phases based on observed child state.
- Decision owner: deterministic first-party `/flows` controller operating over an operator/user-authored workflow definition.
- Supporting / enforcement mechanisms: `init_state`; per-phase/task state; `spawn_phase_tasks`; `fill_phase_slots`; `refresh_all_phases`; `all_agents_done`; phase transition logic; stop-file abort; `Background` process records/logs.
- Closure path: all-current task/process state → deterministic controller refreshes and evaluates phase/capacity conditions → launch/withhold/advance/done/abort decision → child/phase state changes → next controller poll observes the changed whole-flow current state.
- Boundary reachability: `/flows` is a standard documented execution surface implemented in the pinned repository and launches the product's own headless runtime.
- Why this is / is not agent-owned: the workflow author supplies objectives/order, but current lifecycle decisions do not require a model to judge whether a phase is complete or which queued task fits a free slot; code owns those decisions from live state. The function is therefore `C`, not `A`.
- Evidence: [`src/Flows.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw); [`src/background.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/background.sw); [`README.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a workflow-current-control S3, not an autonomous strategic manager. The workflow topology/prompts are supplied ahead of time, and current decisions are deterministic lifecycle control over that declared commitment structure.

## S3* — Complementary audit

- State: —
- Function: no material boundary-reachable complementary audit function with both sufficiently independent challenge and a returned corrective-control closure was established.
- Disturbance / variety regulated: the experimental council can surface architecture, risk and operational disagreements, but no S3*-specific corrective-return loop is closed into production control.
- Decisive decision or feedback right: not established for a complementary auditor whose verdict changes current operational commitments.
- Decision owner: not established at S3*.
- Supporting / enforcement mechanisms: `scripts/council.sh`; three bounded read-only panel agents; no-tools judge; council-specific ToolRegistry execution contexts; tests/review scripts and ordinary coding/test tools.
- Closure path: incomplete. Independent panels → judge synthesis → printed advisory output is established; judge verdict → authoritative corrective change in the primary Agent or `/flows` controller is not wired in the frozen product.
- Why this is / is not agent-owned: the council supplies real independent model judgments, but independence alone is insufficient. A human or some separate caller must interpret/use the final recommendation; swarm-code does not first-party route that result back into a corrective operational decision.
- Evidence: [`scripts/council.sh`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/scripts/council.sh); [`src/ToolRegistry.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/ToolRegistry.sw); [`README.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the council is stronger evidence than ordinary unit tests because its panelists are independent model actors with narrowed direct repository access; the negative state is specifically due to missing returned corrective closure, not lack of review independence.

### Absence scope

- Surfaces inspected: experimental council runner; council panel/judge execution contexts; `/flows`; synchronous typed subagents; hooks; tests/review tooling; README architecture/security descriptions.
- Plausible first-party paths checked: council judge as corrective auditor; review flow examples; independent read-only subagent review; tests/verification; post-tool hooks; review/audit documents and user-invoked advisory commands.
- Why no material first-party path remains: all inspected review paths either remain advisory/output-only or belong to ordinary production/tool verification. No default product path consumes an independent audit verdict and returns it into current operational control without an external human/application decision owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective intelligence loop that develops and adopts adaptations to swarm-code's present organizational capability was established.
- Disturbance / variety regulated: scheduling, web access, memory/session search, skills, profiles, MCP and recurring prompts can broaden present execution or defer it in time, but they do not close future-oriented organizational adaptation.
- Decisive decision or feedback right: not established for an S4 actor.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `Scheduler`; persistent memory; session FTS; skills; web tools; MCP; provider profiles; cron prompts; trajectory export.
- Closure path: no environment/future sensing → prospective option generation/evaluation → adopted change to current organizational capability/S3 loop was found. The scheduler merely compares time against operator-authored schedules and fire-and-forgets a predetermined prompt.
- Why this is / is not agent-owned: current-task search/memory and scheduled execution reuse configured capabilities. They do not create a separate actor that observes emerging external/future conditions, develops an organizational adaptation and closes its adoption into current control.
- Evidence: [`src/scheduler.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/scheduler.sw); [`README.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/README.md); session/memory/skills modules in the pinned tree.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user can schedule a prompt such as "review open PRs" and a model may reason prospectively inside that future S1 run; this is not a persistent first-party S4 closure over the product organization itself.

### Absence scope

- Surfaces inspected: scheduler/heartbeat; memory and optional embeddings; session search; skills; web tools; MCP; provider profiles; trajectory export; `/flows`; council; hooks.
- Plausible first-party paths checked: external condition monitoring, future-scenario modeling, autonomous capability scouting, skill/provider/MCP adoption, recurring strategic review, learned organizational policy and return of a prospective adaptation into current S3 control.
- Why no material first-party path remains: the mechanisms execute preset prompts, retrieve past/current evidence or use configured extensions. No first-party actor owns a closed outside-and-then adaptation cycle that changes the organization's present capability or strategy.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: trust decisions, permissions, execution contexts, hard command denies, remote-endpoint opt-in, project configuration restrictions and hook/tool policies bound operation but do not constitute runtime identity/ultimate-policy authority.
- Decisive decision or feedback right: not established for S5-level identity or ultimate policy.
- Decision owner: developer/operator-authored configuration and trust choices remain outside a qualifying runtime S5 actor.
- Supporting / enforcement mechanisms: `ToolExecutor`; `ToolRegistry`; trust/untrust configuration; project-config restriction; hardline command blocklist; context allow-lists; permissions/hooks; `SWARM_CODE_ALLOW_REMOTE` and other environment/config flags.
- Closure path: absent at S5 level. Externally authored policy → deterministic enforcement is present; runtime identity/policy issue → legitimate ultimate authority → authoritative policy revision → returned organization-wide policy is not.
- Why this is / is not agent-owned: models and deterministic controllers operate inside the policy envelope but do not own the legitimate right to redefine swarm-code's identity or ultimate constitutional rules. Operator trust/permission choices are external governance rather than product-owned S5.
- Evidence: [`src/ToolExecutor.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/ToolExecutor.sw); [`src/ToolRegistry.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/ToolRegistry.sw); [`README.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/README.md); [`SECURITY.md`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/SECURITY.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: strict fail-closed enforcement is important safety infrastructure but enforcement strength is not equivalent to S5 ownership.

### Absence scope

- Surfaces inspected: tool execution policy; execution contexts; permission resolution; hard-deny command rules; remote-endpoint gate; trust/untrust/project configuration; hooks; profiles; scheduler/flow control; repository-governance adjacency.
- Plausible first-party paths checked: runtime constitutional revision, ultimate-policy adjudication, identity-level escalation, legitimate autonomous changes to trusted-project/permission policy, durable authoritative policy return into all subordinate S1s and repository governance as a parent identity function.
- Why no material first-party path remains: the running system enforces rules selected by developers/operators. It does not establish an internal actor with legitimate ultimate-policy/identity closure.

## Recursion

`/flows` child tasks are separate full headless swarm-code processes and therefore distinct S1 units at the recursion used for S2/S3. The review does not infer that each child recursively instantiates the entire `/flows` metasystem during ordinary execution. The synchronous `task` subagent path is bounded and specifically blocks nested subagent spawning, reinforcing that no stronger recursive-viability claim is needed.

## Variety and escalation

swarm-code attenuates operational variety through `ToolExecutor` policy, context-specific allow-lists, command/path guards, bounded subagents, flow concurrency caps, deterministic phase gates, headless dangerous-command denial and session/context recovery. It amplifies capability through tools, skills/MCP, memory/search, provider profiles, parallel workflows and recurring headless jobs.

Escalation from subordinate `/flows` operation to deterministic current control is explicit: every child process is represented in the complete flow state, its status/log statistics are refreshed, capacity feedback controls later task admission and all-terminal feedback controls phase transition. Complementary council findings, by contrast, stop at advisory synthesis and are not first-party escalated back into corrective current control.

## Evidence gaps

- The positive S2 claim is limited to active-process/resource-capacity attenuation; no semantic conflict or shared-file arbitration among children is claimed.
- S3 is deterministic lifecycle control over a user-authored workflow. No model-owned organization-wide current manager is claimed.
- The council has meaningful independent challenge but no verified automatic corrective-return path into the primary Agent or flow controller.
- Scheduler/memory/skills/profile mechanisms do not establish a prospective adaptation loop at the reviewed boundary.
- Generic swarmrt functionality not instantiated by the pinned swarm-code composition was deliberately excluded from evidence.
