---
harness_id: orchestrator-harness
project_name: Orchestrator Harness
repository: https://github.com/dhoelzer/AgentOrchestrator
review_ref: 33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded
reviewed_at: 2026-11-08
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Orchestrator Harness

## Review boundary

- System in focus: the self-hosted Python/OpenHands-SDK multi-project Orchestrator Harness application, its durable board, repeating model-backed root orchestrator, worker/reviewer agents, tool executors, deterministic scheduler, router and human web/API console.
- Purpose and identity: develop and deliver software projects through a long-running model-directed portfolio coordinator with specialist child workers and board-mediated review.
- Relevant environment: operator project instructions and uploads, project workspaces and files, model endpoints, OpenHands SDK tools, turn/concurrency budgets and delivery consumers.
- Standard-distribution boundary: the shipped `python -m agent_harness.main` or one-cycle startup with configured model endpoint, first-party task tools, orchestrator loop and scheduler. Tests use simulated runtimes; no paid model E2E claim is inferred.
- Credited operating / distribution surfaces: `agent_harness/main.py`, `orchestrator.py`, `scheduler.py`, `runtime.py`, `tools.py`, `store.py`, `prompts.py`, `web/api.py` and supported JSON configuration/board persistence.
- Adjacent first-party surfaces excluded from ownership: docs/wiki, test fixtures, CI/release procedures and ancillary static web assets; OpenHands SDK, LiteLLM, third-party LLM server decisions and model internals are treated as dependencies rather than additional first-party metasystem actors.
- First-party operating / deployment modes considered: continuously running orchestrator with configured LLM; model-authored task dependency/worker plans; autonomous worker execution; default reviewer creation/dispatch; explicitly reconfigured reviewer with `record_review` access; operator pause/config/directive modes.
- Recursion level: one installed portfolio orchestrator governing independent project/task S1 specialists. Model-backed subagents, including reviewers, are operational/audit cells; no nested complete viable system is assumed for every child agent.
- Reviewed revision: `dhoelzer/AgentOrchestrator@33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded`.
- Observation date: 2026-11-08. Generated/current Profile `0.2.4`, Methodology `0.3.7`.

## Repository architecture

`main.py` registers first-party board tools, configures a model router and runs `Orchestrator.run_forever`. The root model receives per-project board/attention/capacity briefings and can create tasks, assign/reconfigure/retire specialist agents, launch work, coordinate review and close delivery. Its OpenHands SDK conversation chooses tool calls; first-party executors mutate durable `Store` state. `Scheduler.sweep` expressly performs deterministic consequences for *already assigned* tasks; it does not choose task owners. Project/task/agent metadata is persisted in `state.json`, with events and individual conversations separated ([entrypoint](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/main.py#L57-L127), [cycle](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/orchestrator.py#L739-L767), [dispatch split](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/scheduler.py#L1-L34)).

## S1 — Operations

- State: A
- Function: specialists perform model-chosen work on project workspace files, commands and tracked deliverables; the root orchestrator is also a model-operated agent, but its regulatory decisions are credited under S2/S3 rather than double-counted as production operations.
- Disturbance / variety regulated: concrete implementation/test/file problems and tool results encountered while completing assigned cards.
- Decisive decision or feedback right: the specialist model chooses tool actions and reports completion/partial/blocking evidence inside its bounded assignment.
- Decision owner: model-backed specialist agent, through OpenHands SDK conversation and first-party tool wiring.
- Supporting / enforcement mechanisms: terminal/file-editor/task-tracker SDK tools, project sandbox, concurrency/turn ceilings, message and event ledger.
- Closure path: the specialist changes real project files and returns results to its conversation/parent; the board captures execution/review state, which triggers further activity.
- Boundary reachability: the shipped root `main.py` constructs the runtime and orchestrator; `RunAgentExecutor` calls `_dispatch`, which passes tools to `AgentRuntime.run` and records subsequent outcomes.
- Why this is / is not agent-owned: action selection resides with the model-backed specialist; deterministic scheduler and SDK executor transport/enforce choices but do not pick the coding actions themselves.
- Evidence: [worker and orchestrator tool registry](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L25-L63), [runtime dispatch](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L642-L745), [SDK run](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/runtime.py#L785-L869).
- Basis: structural source, supported startup and mocked tool/board tests.
- Confidence: high for an installed agent-action path; no credentialed external-provider success run is claimed.
- Caveats: OpenHands SDK and external LLM are required; their internal control planes are outside the first-party assessment boundary.

## S2 — Coordination

- State: A
- Function: keep independently operating specialist tasks from simultaneously interfering on shared project files and blocked dependencies.
- Disturbance / variety regulated: two otherwise parallel workers touching the same file or a downstream worker starting against unfinished upstream output.
- Decisive decision or feedback right: the root model decides task separation/dependency edges and can re-plan task relationships from each fresh board/attention briefing; the scheduler subsequently enforces the chosen edges mechanically.
- Decision owner: root orchestrator agent for the conflict-prevention plan; deterministic scheduler for execution of that model-authored plan.
- Supporting / enforcement mechanisms: `depends_on` task fields, sequential readiness, project-level slot cap, task statuses, generated briefings and tool-mediated updates.
- Closure path: orchestrator chooses dependencies for overlapping work; scheduler refuses to start a dependent task until all predecessor cards are `done`; completion produces an unblock and new agent dispatch, while blocker/rework feedback allows the next orchestrator cycle to change the plan.
- Boundary reachability: the root system prompt explicitly commands `depends_on` when parallel tasks would touch the same files, `CreateTaskExecutor` stores model-chosen edges, and the shipping scheduler checks them on every sweep.
- Why this is / is not agent-owned: conflict-sensitive choice of edges is a model tool call, not an authored static DAG. The runtime's bare dependency check is not independently S2=A, and evidence does not establish automatic real-time file-lock conflict detection.
- Distinct S1 units: separately created project specialists, with each one owning a model/file workspace execution stretch.
- Inter-S1 disturbance: named shared-file collision between parallel task workers, together with downstream use of unfinished upstream files.
- Attenuating coordination relation: model-authored `depends_on` serializes the interfering work while leaving unrelated cards eligible for concurrent execution.
- Feedback into subsequent S1 behaviour: predecessor `done` releases a card to `ready`, next scheduler dispatch injects task/dependency notes and prior review feedback; root receives current board statuses for re-planning.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the supplied orchestrator prompt ties dependency choice to a *particular inter-worker file collision*, and the dependency gate actively controls conflicting worker start; generic task order alone would not support this claim.
- Evidence: [root planning rule](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/prompts.py#L38-L52), [task edges/edit](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L260-L370), [dependency scheduler](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/scheduler.py#L64-L117), [dependency test](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/tests/test_scheduler_and_stuck_cycles.py#L241-L295).
- Basis: explicit operating prompt, source-enforced dependency return, local stub tests.
- Confidence: medium: the intended shared-file interference is explicit, but live model identification of correct dependency edges was not observed.
- Caveats: no actual file-overlap detector or automatic cross-task lock. A model that omits needed edges can still cause collision; mere slot caps are not credited as the agent-owned S2 decision.

## S3 — Inside-and-now control

- State: A
- Function: maintain a whole-project current board and regulate allocations, staffing, blocked recovery, review and delivery decisions across worker cells.
- Disturbance / variety regulated: unstaffed work, spent budgets, project stalls, failed models, review/rework queues and imbalanced worker/endpoint capacity.
- Decisive decision or feedback right: the root model chooses task decomposition, worker assignment, budget extension versus reconfiguration/splitting, current plan edits, reviewer dispatch and explicit delivery signal from new board feedback.
- Decision owner: the continuously reused root orchestrator model/agent; human edits, pause and config controls impose constraints and may override but do not constitute the credited autonomous path.
- Supporting / enforcement mechanisms: persisted Store board, `detect()` attention, `cycle_briefing`, `create_task`, `assign_task`, `extend_agent`, `reconfigure_agent`, `retire_agent`, config reload, slot gate and deterministic `Scheduler.sweep`.
- Closure path: issue/change/block appears in Store; the next root cycle receives a cross-card and capacity briefing, issues a chosen mutation through board tools, and tasks are dispatched/reviewed/blocked accordingly; later results return to that same Store and next-cycle decisions.
- Boundary reachability: `main.py` launches the never-ending loop; `_run_cycle` checks live attention, `_run_project_cycle` uses root SDK model and passes the root board tools, and scheduler runs both before and independently of the root cycle.
- Why this is / is not agent-owned: staffing and recovery choices disappear when the root model is removed. Automatic capacity accounting and status transition are supporting controller mechanics, not the entire S3 claim.
- Whole-system current view: per-project board, dependencies, agents, blockers, reviewer status, cost/capacity and user messages in fresh root briefings, across the managed specialist S1 cells.
- Current-control decision scope: project portfolio task and worker commitments, resourcing, rework direction and delivery timing; no claim that the model autonomously rewrites system-level policy/LLM infrastructure.
- Evidence: [attention/blocked detection](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/orchestrator.py#L309-L451), [cycle and project control](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/orchestrator.py#L739-L928), [orchestrator authority tools](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L25-L56), [root discipline](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/prompts.py#L17-L122).
- Basis: shipped loop, named board decisions and tests of blocking/dispatch.
- Confidence: high for architectural agent-owned project regulation.
- Caveats: global cross-project cycle is sequential per project; no separate autonomous cross-domain S3 beyond the installed project portfolio is inferred.

## S3* — Complementary audit

- State: C
- Function: a distinct reviewer agent independently inspects actual files/testable results against task acceptance criteria and returns a corrective verdict on worker output.
- Disturbance / variety regulated: erroneous implementation or unsupported worker claims surviving routine completion reporting.
- Decisive decision or feedback right: in a configured reviewer mode, a separate model reviewer decides `approved` versus `changes_requested` after reading files; `RecordReviewExecutor` translates that judgment into `done` or `rework` and the root re-dispatches on corrective feedback.
- Decision owner: a separate model reviewer **when explicitly equipped with the `record_review` tool**; the orchestrator remains parent control of staffing/response.
- Supporting / enforcement mechanisms: distinct reviewer task link, reviewer assignment prompt, read-file/terminal SDK tools, `reconfigure_agent`, review rounds, feedback persistence and rework board transitions.
- Closure path: worker finishes to `review`; parent creates/attaches reviewer; reviewer opens independent file read, checks criteria and records verdict; failing work moves to `rework` with review feedback in the next worker run.
- Boundary reachability: default shipping tool registry permits a root to reconfigure a newly created reviewer with `record_review`, then dispatch `run_agent(review=true)`; the tool writes verdict and rework state. However `CreateSubAgentExecutor` validates `action.tools` but **fails to assign it to `AgentSpec.tools_override`**, while the default worker tool set omits `record_review`. The advertised one-step reviewer creation does not itself close a direct verdict. This is a **composable, not reliably default** mode.
- Why this is / is not agent-owned: distinct reviewer model rather than creator's same tool state can inspect actual files and choose a verdict; it needs explicit tool wiring, and default root self-inspection alone is not counted as independent S3*.
- Claim being audited: a worker's claim that named project deliverables satisfy task-specific acceptance criteria.
- Ordinary reporting path: worker's `report_to_parent` and normal task completion/summary, which are not themselves independent proof.
- Complementary access path: reviewer `read_file`/`terminal` reads workspace artifacts and may run tests independently from worker's self-report.
- Independence boundary: different child agent/conversation and reviewer pointer from worker's `assigned_agent_id`; both share first-party project files, so no stronger sandbox/process isolation is inferred.
- Who acts on findings: reviewer verdict switches board `done`/`rework`, with orchestrator/scheduler returning failure feedback to the next worker stretch.
- Evidence: [reviewer prompts](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/prompts.py#L170-L189), [creation tool omission](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L404-L474), [reconfigure tool/registry](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L807-L852), [review submission](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L948-L994), [reviewer scheduler](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4dcd0e7267391b45a2d4edded/agent_harness/scheduler.py#L71-L150).
- Basis: source-level executable mode and mocked board tests, no live reviewer provider run.
- Confidence: medium for the explicitly equipped mode; low for author claims of out-of-box automatic reviewer finalization.
- Caveats: reviewer creation's `tools` argument is presently a no-op at the pin, and `reviewer_prompt` is defined but not automatically selected by `CreateSubAgentExecutor`. Default prompts alone must not be treated as verified independent adjudication.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate agent-owned environmental scanning, future-option generation and implemented organizational adaptation loop was identified in the installed distribution.
- Disturbance / variety regulated: potential future tool/platform/model change would require a prospective response, but the observed scheduler chiefly handles *current* throughput and present user cards.
- Decisive decision or feedback right: none evidenced for autonomous outside/then strategy; endpoint selection and automatic timeouts are current deterministic transport tuning.
- Decision owner: user changes configured LLM servers and task goals; root agent replans current work but is explicitly told not to change harness configuration itself.
- Supporting / enforcement mechanisms: config reload, model endpoint router health signals, new user-input attention, arbitrary specialist prompts.
- Closure path: no first-party agent-origin external trend/forecast option is chosen and carried into a durable future capability or strategy change. A user-set configuration may reload but is not such a loop.
- Why this is / is not agent-owned: endpoint tuning and iterative project replanning are S1/S3 current-control support, not evidence of an independently closed S4 function.
- Evidence: [config reload](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/orchestrator.py#L69-L184), [do not reconfigure rule](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/prompts.py#L53-L69), [current-attention routing](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4dcd0e7267391b45a2d4edded/agent_harness/orchestrator.py#L309-L451).
- Basis: shipped model action inventory, operating prompt and selected state/endpoint paths.
- Confidence: medium-high within specified first-party runtime modes.
- Caveats: this is not a claim that human maintainers cannot plan future versions outside the harness.

### Absence scope

- Surfaces inspected: runtime, root prompt, configuration watcher, LLM router/health reporting, task tools, user API, project planning and tests.
- Plausible first-party paths checked: future-sounding replan language in new user input, project delivery readiness, new specialist creation, config/endpoint hot reload and adaptive timeout/routing.
- Why no material first-party path remains: all inspected paths react to current project instructions or transport failures, or expose operator-authored configuration; no separate external-future intelligence option/decision/return closes inside the reviewed application.

## S5 — Policy and identity

- State: —
- Function: no legitimate first-party ultimate identity/constitutional policy authority is exposed as a separately closed S5 decision process.
- Disturbance / variety regulated: competing portfolio purposes or permanent policy contradictions would require legitimate identity-level arbitration, but observed choices are task/agent instructions and runtime configuration.
- Decisive decision or feedback right: none evidenced beyond task-level human direction and root-controlled specialist prompt/mission changes.
- Decision owner: static installed root `ORCHESTRATOR_SYSTEM_PROMPT` and the human software owner define core identity; the model can create/reconfigure subagent instructions but not set the harness's own ultimate policy.
- Supporting / enforcement mechanisms: frozen system prompt, config fields, project scope, human UI pause/manual delivery, per-agent `system_prompt` overrides.
- Closure path: no first-party policy dispute adjudicator with changed identity fed back into the root runtime; changes to child missions remain subordinate S3 control.
- Why this is / is not agent-owned: a root's ability to author a new worker prompt is delegation/operational policy, not legitimate authority to rewrite its own constitutional identity; static operator settings do not imply a distinct parent S5 mode.
- Evidence: [fixed root identity](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/prompts.py#L17-L130), [root spec creation](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4edded/agent_harness/orchestrator.py#L198-L228), [child prompts/reconfiguration](https://github.com/dhoelzer/AgentOrchestrator/blob/33fce2cc0d0b3dd4dcd0e7267391b45a2d4dcd0e7267391b45a2d4dcd0e7267391b45a2d4dcd0e7267391b45a2d4edded/agent_harness/tools.py#L404-L464).
- Basis: first-party identity/prompt tooling search and source inspection.
- Confidence: medium-high for absence in the supported runtime boundary.
- Caveats: external repository governance by maintainers is not part of the installed agent application assessment.

### Absence scope

- Surfaces inspected: root identity creation, tools to create/reconfigure child agents, web task/settings UI, root prompt and config reload.
- Plausible first-party paths checked: root system prompt, arbitrary `CreateSubAgentAction.system_prompt`, root `reconfigure_agent` calls, human pause and operator-defined project goals.
- Why no material first-party path remains: these support fixed root authority or bounded per-task child policies, not an independent ultimate identity policy change with legitimate authority and closed return into the root agent's constitutive rules.

## Recursion

The root supervises many model-backed child workers and an optional reviewer. Tasks/children do not possess separate independent S3/S4/S5 authority; recursive delegation depth is an execution tree, not automatically nested viable systems. A portfolio can have multiple user-created projects, but their joint root owns the S3 claim.

## Variety and escalation

The model expands specialist variety by selecting expertise/assignments; task edges and project slots attenuate collision/capacity disturbance. The deterministic scheduler runs previously chosen work without another model call. A reviewer verdict can send work to `rework` in an explicitly configured mode; repeated review failures, budget exhaustions and model outages escalate through root attention to reconfigure/split/hold rather than autonomously repairing a dead endpoint.

## Evidence gaps

- No real model endpoint was exercised; source paths and local tests establish capabilities, not observed agent reliability.
- The `CreateSubAgentExecutor` tool-override omission and reviewer prompt mismatch materially limit the out-of-box S3* claim; a reviewer with manually reconfigured tool permissions is a composable path, not proven default autonomy.
- `depends_on` serializes only dependencies the model or operator correctly identifies. No automatic file-overlap detector or runtime lock was found; S2 is a bounded agent-authored prevention path.
- No repository-level maintainer governance or OpenHands dependency internals were imported into first-party S4/S5 ownership.
