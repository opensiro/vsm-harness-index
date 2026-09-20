---
harness_id: pydantic-ai-harness
project_name: Pydantic AI Harness
repository: https://github.com/pydantic/pydantic-ai-harness
review_ref: 434649f87d34aa7e5d48c7bd26ad33c50d57cf10
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# Pydantic AI Harness

## Review boundary

- System in focus: the first-party `pydantic-ai-harness` package at pinned revision `434649f87d34aa7e5d48c7bd26ad33c50d57cf10`, including shipped Coder/Researcher runnable harnesses and capabilities for tools/workspaces, planning, subagents/dynamic workflows, memory/context controls, trajectory judging and runtime capability creation.
- Purpose and identity: equip Pydantic AI agents for long-running autonomous work with executable workspaces/tools, durable context, delegation/orchestration, live independent steering and composable self-extension while remaining a capability library that can be assembled into concrete agents.
- Relevant environment: user tasks, repositories/files/shells, web/research sources, model/tool outputs, subagent results, run trajectories, persistent memory/capability stores and host/orchestrator code that starts later runs.
- Standard-distribution boundary: first-party Harness package code, exported `coder_agent`, Coder/Researcher combined capabilities, DynamicWorkflow/SubAgents, TrajectoryJudge, CapabilityCreation and their documented runtime contracts. The `pydantic-ai` core `Agent` class/model loop and model providers are required execution substrate/dependencies; their separate metasystem features are not inherited. Adjacent repository-development agents, CI, Macroscope repository review policy and maintainer governance are excluded unless they are themselves shipped runtime capabilities.
- Credited operating / distribution surfaces: installed `pydantic-ai-harness` package; exported `pydantic_ai_harness.coder:coder_agent`; documented `Agent(..., capabilities=[Coder()/Researcher()/DynamicWorkflow()/TrajectoryJudge()/CapabilityCreation()])` modes; corresponding first-party capability code and runtime stores.
- Adjacent first-party surfaces excluded from ownership: `.agents/*` contributor/dogfood agents and skills; repository CI/release/compat workflows; `.macroscope/*` repository-development correctness rules; docs-parity reviewer; benchmark/eval/Terminal-Bench playbooks except as evidence that the packaged harness is runnable; Pydantic AI core features not wrapped or instantiated by this repository's assessed mode.
- First-party operating / deployment modes considered: packaged Coder/Researcher agents; custom Pydantic AI Agent with Harness capabilities; DynamicWorkflow team mode; TrajectoryJudge opt-in judged-run mode; CapabilityCreation self-extension mode with the documented host activation contract.
- Recursion level: one Harness-enabled agent organization. The primary Coder/Researcher agent is S1 at the base operational level. In DynamicWorkflow mode, named child `Agent.run` executions are subordinate operational S1 units coordinated/regulated by the parent orchestration agent. TrajectoryJudge is a complementary audit actor rather than an ordinary production S1.
- Reviewed revision: `434649f87d34aa7e5d48c7bd26ad33c50d57cf10`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Pydantic AI Harness is the official capability/harness library layered on Pydantic AI. Its standard package contains complete combined harnesses such as Coder and Researcher and also exposes lower-level capabilities that can be composed onto any `pydantic_ai.Agent`. The repository exports a runnable model-less `coder_agent = Agent(name='coder', capabilities=[Coder()])`; the CLI/user supplies the model while the Harness package supplies the coding role, workspace/tool capabilities and context controls. The README documents the resulting autonomous coding path and a zero-setup `clai -a pydantic_ai_harness.coder:coder_agent` entry point.

The library's multi-agent machinery is opt-in. `SubAgents` performs one isolated child-agent run per delegation. `DynamicWorkflow` goes further: the parent model sees a catalog of named agents and writes a Python program inside one `run_workflow` tool call. That generated program may fan out `Agent.run` calls, chain their results, branch/retry, score/vote and dispatch follow-up agents. Each child call is a real isolated `Agent.run` with its own model loop/history/tools. The model-authored workflow therefore supplies a supported mode where an autonomous parent owns whole-team current commitments/interventions, while the sandbox and budgets merely enforce its generated plan.

`TrajectoryJudge` supplies a materially separate audit loop. On cadence, a second model receives a bounded raw transcript of the live run—including user/assistant messages, tool calls and tool results—and returns `AllGood` or `Steer`. A `Steer` verdict is enqueued into the running parent's conversation at ASAP priority and reaches the next model request. The judge can be a distinct full Agent/model/instruction set and is kept independent from ordinary task production.

`CapabilityCreation` supplies a different type of path. A running agent can notice that its host lacks a needed behavior, author a Python capability, validate it and persist it. The repository explicitly fixes activation to a future boundary: the capability is available only on a later run. However the docs also say the host orchestrator owns the one-line integration contract that loads active authored capabilities and passes them into the next `agent.run`. Thus the repository exposes an S4-specific autonomous option-generation path but does not itself close activation without composition; this is constructor ownership (`C`) rather than autonomous `A`.

Primary evidence:

- [`README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/README.md) — product boundary, autonomous Coder/Researcher stacks, DynamicWorkflow, TrajectoryJudge and CapabilityCreation capability inventory.
- [`pydantic_ai_harness/coder/_agent.py`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/coder/_agent.py) — packaged runnable `coder_agent` first-party path.
- [`pydantic_ai_harness/dynamic_workflow/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/dynamic_workflow/README.md) — model-owned whole-team workflow generation, isolated `Agent.run` children, fan-out/chaining/voting/retry control and budgets.
- [`pydantic_ai_harness/trajectory_judge/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/trajectory_judge/README.md) — separate-model live trajectory audit and `Steer` return into the parent run.
- [`pydantic_ai_harness/capability_creation/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/capability_creation/README.md) — agent-authored validated persistent capability creation, next-run activation boundary and explicit host-orchestrator integration contract.

## Operational model

In the standard Coder mode, Harness exports an actual Agent object configured with Coder. The user/CLI supplies a model and task. The running model then autonomously investigates repository state, selects file/shell tools, edits, verifies and returns a result. Harness capabilities provide the workspace, persistent shell, repository orientation, context controls and safety/budget machinery; these mechanisms support the model-owned operational loop rather than replacing its discretion.

In DynamicWorkflow mode, the parent agent owns a catalog of named child agents and receives a `run_workflow` tool. The parent model writes the orchestration program. The program can launch several isolated subagent S1 runs, inspect their returned values, select or retry work and dispatch further agents. The current-control policy originates in model-written code and is enforced by the workflow sandbox/runtime. This establishes S3 at the team recursion. It does not by itself establish S2: fan-out, chaining, voting and delegation show choreography and selection, but the reviewed standard path does not establish a concrete interference/conflict/oscillation among S1 units plus a distinct attenuation relation satisfying the stricter S2 witness.

In TrajectoryJudge mode, a separate judge model receives a complementary trace of the operational run and can inject a corrective steering message into the parent's next request. That is a closed S3* path. In CapabilityCreation mode, the production agent can generate an adaptation artifact for future use, but activation still depends on the documented surrounding loop calling `store.load_active()` and feeding those capabilities to the next run. That leaves S4 as a constructor path.

## S1 — Operations

- State: A
- Function: autonomously execute a bounded coding/research task using first-party Harness tools, workspace/context capabilities and model-driven action selection.
- Disturbance / variety regulated: repository/web/task ambiguity, file and shell state, tool results, test failures, retrieved evidence, long-horizon context pressure and intermediate errors encountered while completing the task.
- Decisive decision or feedback right: choose the next substantive investigation/tool/edit/research action and iterate from resulting observations until the assigned task is completed or otherwise concluded.
- Decision owner: the model-driven Pydantic AI Agent configured and exported through the Harness's first-party Coder/Researcher path.
- Supporting / enforcement mechanisms: Coder/Researcher combined capabilities, filesystem/shell/web tools, repository context, context compaction/output limits, memory, guardrails/spend controls and the Pydantic AI Agent execution substrate.
- Closure path: user task → packaged Harness-enabled Agent → model-selected tool/actions → file/shell/web/tool observations → further model decisions → result/changes/evidence.
- Boundary reachability: the repository ships a runnable `pydantic_ai_harness.coder:coder_agent` and documents zero-setup CLI execution; users may also instantiate `Agent(..., capabilities=[Coder()])` directly. The assessed actor is therefore wired into a supported first-party Harness mode rather than existing only in examples/dogfood.
- Why this is / is not agent-owned: first-party capabilities constrain and expose actions, but the autonomous model decides which actions to take from current operational evidence; deterministic tool/runtime machinery does not preselect the task solution.
- Evidence: [`README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/README.md), [`pydantic_ai_harness/coder/_agent.py`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/coder/_agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Pydantic AI core provides the generic Agent loop as a dependency; this assessment does not import unrelated core metasystem capabilities. S1 credit rests on this repository's shipped concrete Harness agent/capability composition and documented autonomous operating path.

## S2 — Coordination

- State: —
- Function: no sufficiently evidenced S2-specific inter-S1 conflict/oscillation attenuation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: no concrete cross-S1 interference witness meeting the Profile threshold is established.
- Decisive decision or feedback right: none established for an S2-specific attenuation relation.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: SubAgents and DynamicWorkflow provide named delegation, isolation, fan-out, chaining, voting, retry control and result transport; budgets bound child execution.
- Closure path: no qualifying inter-S1 conflict/oscillation → S2-specific attenuation → returned change in later S1 behaviour loop established.
- Why this is / is not agent-owned: the parent model can coordinate in the ordinary software sense, but the Methodology requires more than routing/delegation/sequencing/shared results. Parallel alternatives, critic scoring and workflow dependencies do not by themselves prove that distinct S1 units are interfering and that a separate coordination relation attenuates that interference.
- Evidence: [`pydantic_ai_harness/dynamic_workflow/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/dynamic_workflow/README.md), [`README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/README.md).
- Basis: explicit absence after function-first review.
- Confidence: medium-high.
- Caveats: a downstream workflow can define a real S2 disturbance and relation, but general DynamicWorkflow expressiveness is not enough for a repository-level positive S2 claim.

### Absence scope

- Surfaces inspected: SubAgents and DynamicWorkflow documentation, child-agent isolation/`Agent.run` semantics, fan-out/chaining/voting/retry examples, workflow budgets and parent/child result flow.
- Plausible first-party paths checked: concurrent child agents, tournament/voting examples, reviewer/editor chains, retry-on-failed-review workflows and generic delegation.
- Why no material first-party path remains: all inspected standard paths demonstrate task decomposition/choreography/selection but do not establish a specific inter-S1 interference/conflict/oscillation plus a first-party S2-specific attenuation relation and behavioural feedback distinct from generic workflow control.

## S3 — Inside-and-now control

- State: A
- Function: in DynamicWorkflow mode, regulate the current whole-team portfolio of subordinate agent calls, dependencies, retries and result-conditioned follow-up commitments.
- Disturbance / variety regulated: changing intermediate subagent results, failed review outcomes, alternative candidate quality, fan-out resource needs and dependencies that require deciding which child work to launch, retry, chain, select or stop.
- Decisive decision or feedback right: choose the workflow program that allocates child-agent calls and conditionally changes subsequent team commitments based on current returned results.
- Decision owner: the parent orchestration agent model, which writes the `run_workflow` Python program from the current task and available subagent catalog.
- Supporting / enforcement mechanisms: DynamicWorkflow capability, Monty sandbox, named-agent catalog, isolated child `Agent.run` calls, `asyncio` fan-out, result values, hard `max_agent_calls` and usage/resource limits.
- Closure path: current task + available team catalog → parent model writes workflow → child S1 runs return live results → model-authored program branches/selects/retries/dispatches later children → final team output returns to parent operation.
- Boundary reachability: `DynamicWorkflow` is a shipped documented Harness capability. Supplying a catalog of named Pydantic AI agents gives the parent model the standard `run_workflow` tool; no downstream scheduler/control-plane implementation is required for the autonomous parent to write and execute current-control logic.
- Why this is / is not agent-owned: the sandbox and budgets deterministically execute/enforce the generated program, but the discretionary whole-team choreography and conditional intervention logic is authored by the parent model for the current task.
- Evidence: [`pydantic_ai_harness/dynamic_workflow/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/dynamic_workflow/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this positive S3 applies to the supported DynamicWorkflow team mode, not every single-agent Coder run. Preconfigured hard budgets and sandbox resource limits are supporting enforcement, not the ownership basis.
- Whole-system current view: the generated workflow program holds the set of team members it can call and receives intermediate results from all child runs used in that workflow, allowing later calls/selection/retry to depend on current team outcomes.
- Current-control decision scope: allocate/fan out child calls, sequence dependencies, compare/select candidate outputs, retry failed/reviewed work and launch follow-up agents from current intermediate evidence.

## S3* — Complementary audit

- State: A
- Function: independently review the live operational trajectory with a second model and return corrective steering into the running production agent.
- Disturbance / variety regulated: instruction drift, unsupported claims, scope creep, hallucination/security concerns and other run-level deviations that may not be detected by the production agent's ordinary self-report.
- Decisive decision or feedback right: judge the bounded recent trajectory as `AllGood` or produce a specific `Steer(message)` correction.
- Decision owner: the separate model-driven TrajectoryJudge agent/model instance.
- Supporting / enforcement mechanisms: cadence/window hooks, bounded transcript rendering, concurrent judge evaluation, enforced verdict output type, `RunContext.enqueue(..., 'asap')`, attribution and run usage/failure accounting.
- Closure path: live production trajectory → separate judge receives raw recent transcript/tool evidence → independent `AllGood`/`Steer` verdict → `Steer` enqueued to production conversation → next model request receives correction → subsequent production behaviour changes.
- Boundary reachability: `TrajectoryJudge` is a shipped documented capability that can be added directly to an Agent with its own model/instructions or a full distinct judge Agent; the steering enqueue path is supplied by the capability itself.
- Why this is / is not agent-owned: the audit judgment is made by a second autonomous model rather than by deterministic validation or the same production actor; the runtime only schedules the review and transports the verdict.
- Evidence: [`pydantic_ai_harness/trajectory_judge/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/trajectory_judge/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the judge sees a rendered recent trajectory rather than independently executing the environment itself; the complementary path is direct access to user/assistant/tool-call/tool-result evidence rather than relying on the production agent's final summary.
- Claim being audited: the live agent run remains on-task, evidence-grounded and otherwise compliant with the judge's specified concern.
- Ordinary reporting path: the production agent's own messages, final output and normal task/tool loop.
- Complementary access path: the judge receives a bounded raw transcript including user messages, assistant messages, tool calls and tool results on an independent cadence while the run is still active.
- Independence boundary: a separate model or full Agent instance owns its own instructions/model configuration and cannot be replaced by the production agent's self-evaluation without removing the credited judge actor.
- Who acts on findings: the Harness capability enqueues `Steer` into the running production conversation, and the production agent receives it on the next model request and changes subsequent action accordingly.

## S4 — Outside-and-then intelligence

- State: C
- Function: expose a first-party path by which an agent can detect a missing host behavior during operational work, generate and validate a new reusable capability, and persist that adaptation for future activation.
- Disturbance / variety regulated: task/environment requirements reveal that the current host lacks a needed guardrail, instruction, tool or lifecycle hook that would improve future operation.
- Decisive decision or feedback right: decide what new capability to author and generate its Python implementation from the observed need; activation of that authored capability in later operation still requires host/orchestrator composition.
- Decision owner: the running agent owns adaptation-option generation; the complete future-capability closure is not autonomous because the surrounding orchestrator/application must load and pass active authored capabilities into later runs.
- Supporting / enforcement mechanisms: `author_capability`, import/construction/static-getter validation, persistent source files + `manifest.json`, listing/disabling and `store.load_active()`.
- Closure path: current task exposes missing host behavior → agent authors/validates/persists capability → active capability store records option → documented host integration loads active capability into a subsequent `agent.run` → future capability changes. The final activation edge requires composition, which is why state is `C` rather than `A`.
- Boundary reachability: `CapabilityCreation` is a shipped Harness capability with default agent-facing guidance and persistence/validation machinery. The S4-specific option-generation path is first-party; only the documented next-run activation loop remains for the developer/orchestrator to compose.
- Why this is / is not agent-owned: option discovery/authorship is agent-owned, but the library explicitly states that capabilities cannot enter the live run and that the orchestrator owns the integration contract for loading them on subsequent runs; therefore autonomous S4 closure is incomplete.
- Evidence: [`pydantic_ai_harness/capability_creation/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/capability_creation/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a downstream application that implements the documented load-active loop may close autonomous S4 for that separate composed system-in-focus, but that composition is not credited back to this repository assessment.
- External distinction: during a coding/operational task the agent discovers that the host lacks a needed behavior such as a guardrail, tool, instruction or hook.
- Future / prospective distinction: authored capabilities cannot affect the already-running execution; they are explicitly intended for activation on the next run or a later loop iteration.
- Adaptation option generated: a validated persistent `AbstractCapability` implementation authored by the agent and recorded in the capability store/manifest.
- Path back into current capability / S3: `store.load_active()` returns persisted active capabilities for the host to pass into a later `agent.run`; this is a function-specific return path but requires the host/orchestrator integration edge to close.

## S5 — Policy and identity

- State: —
- Function: no first-party identity / ultimate-policy decision loop is established at the reviewed agent-organization recursion.
- Disturbance / variety regulated: no qualifying identity/ultimate-policy disturbance established.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: system instructions, guardrails, spend/tool limits, tool approval, permission/configuration and capability composition constrain behaviour but do not constitute ultimate-policy ownership.
- Closure path: no identity/policy issue → legitimate ultimate authority → authoritative decision → returned governance of subsequent organization loop established.
- Why this is / is not agent-owned: model-owned task planning/workflow control and self-extension remain operational/current-control/adaptation functions. They do not show the agent deciding the organization's ultimate identity/policy, and user-authored constraints do not become S5 merely because they are authoritative configuration.
- Evidence: [`README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/README.md), [`pydantic_ai_harness/capability_creation/README.md`](https://github.com/pydantic/pydantic-ai-harness/blob/434649f87d34aa7e5d48c7bd26ad33c50d57cf10/pydantic_ai_harness/capability_creation/README.md).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: tool approval and operator configuration can represent legitimate human authority over particular actions without establishing a complete parent S5 loop.

### Absence scope

- Surfaces inspected: Coder/Researcher instructions/capability stacks, guardrails/spend/tool-approval controls, DynamicWorkflow orchestration, TrajectoryJudge steering, CapabilityCreation self-extension and package configuration surfaces.
- Plausible first-party paths checked: system instructions, user/tool approvals, capability selection/disablement, self-authored capabilities, workflow policies and judge steering.
- Why no material first-party path remains: the inspected paths regulate task execution, current team control, audit or future capability adaptation; none reconstructs a genuine identity/ultimate-policy issue with a first-party S5 owner and authoritative return governing the organization as a whole.

## Distributed OSS parent arrangement

Repository maintainer/contributor governance, CI and `.agents` dogfood are outside the assessed runtime boundary and are not used to infer parent modes. The assessment concerns installed Harness-enabled agents. A downstream user can configure models, capabilities, approvals and instructions, but generic configuration/approval does not independently establish S3/S4/S5 parent governance under Methodology 0.3.5.

## Self-hosted and non-human modes

The library is locally composable and model/provider agnostic. Positive states are credited only where the first-party package supplies the relevant autonomous actor/path after normal capability configuration. The optional nature of DynamicWorkflow or TrajectoryJudge does not transfer their decision ownership to the human; when enabled, the parent orchestrator and judge models own those decisions. CapabilityCreation is intentionally left at `C` because its own docs place next-run activation responsibility on the surrounding host/orchestrator.

## Recursion

A simple Coder/Researcher run has one operational S1 agent. DynamicWorkflow introduces a higher team recursion: named isolated child `Agent.run` instances are operational units and the parent model owns team-level current-control choreography. TrajectoryJudge is an independent complementary audit relation to the production run. A downstream application that wires persistent authored capabilities into repeated runs becomes a distinct composed system-in-focus for any stronger S4 claim.

## Variety and escalation

Harness absorbs operational variety through executable tools/workspaces, context management, memory and delegation. DynamicWorkflow expands regulatory variety by allowing the parent model to generate task-specific team control logic rather than relying on a static DAG. TrajectoryJudge introduces independent challenge and immediate corrective steering. CapabilityCreation exposes future adaptation options while deliberately keeping activation inspectable and host-controlled. Human tool approvals/Ask User are escalation mechanisms but are not automatically promoted to parent VSM states.

## Evidence gaps

The strongest semantic uncertainty is S3 versus ordinary workflow orchestration. The positive S3 finding relies specifically on DynamicWorkflow's model-authored whole-team program being able to condition later agent commitments on current intermediate results, not on the `orchestrator` label or generic delegation. No evidence establishes the stricter inter-S1 conflict witness required for S2. S4 is intentionally conservative at `C` because the repository explicitly assigns next-run capability activation to surrounding host/orchestrator code.
