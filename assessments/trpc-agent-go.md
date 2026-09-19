---
harness_id: trpc-agent-go
project_name: tRPC-Agent-Go
repository: https://github.com/trpc-group/trpc-agent-go
review_ref: 28cb50c1d927a586521de028aed95bde2a018144
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# tRPC-Agent-Go

## Review boundary

- System in focus: one first-party tRPC-Agent-Go agent system at pinned revision `28cb50c1d927a586521de028aed95bde2a018144`, including LLMAgent/Runner execution, first-party multi-agent/team composition, session/memory/artifact/skill services, Evaluation/PromptIter facilities, and the Evolution self-learning subsystem; the shipped OpenClaw application is considered as a first-party deployment surface where it closes framework paths without adding external organizational actors.
- Purpose and identity: provide a Go runtime/framework for production agent systems that can execute model/tool loops, compose specialist agents and workflows, persist operational context, evaluate behavior, and optionally learn reusable skills from completed work for later tasks.
- Relevant environment: user requests and corrections, model/tool results, external APIs and MCP/A2A/AG-UI peers, application state, conversation/session history, evaluation datasets and metrics, completed-task outcomes, failures/recoveries, and future tasks that may reuse learned skills.
- Standard-distribution boundary: first-party packages and documented deployment surfaces in `trpc-group/trpc-agent-go` at the pinned revision, including `agent`, `runner`, `team`, `graph`, `evaluation`, `evolution`, `skill`, and `openclaw`. External model providers, application business logic, application-defined agent roles, domain evaluators/datasets, MCP servers, and operator-authored policy remain external unless a first-party path itself closes the mapped organizational function.
- Credited operating / distribution surfaces: LLMAgent plus Runner; coordinator-team member-as-tool feedback; Evolution's background review → reconcile → gate → publish loop; managed skill repositories and `skill_load`; OpenClaw's first-party Evolution wiring; and PromptIter/optimization as corroborating first-party prospective adaptation machinery.
- Adjacent first-party surfaces excluded from ownership: ChainAgent/ParallelAgent/CycleAgent sequencing by itself; generic transfer/routing/shared state; Runner cancellation/retry/lifecycle plumbing; evaluation result persistence and observability alone; HITL/approval hooks by themselves; static instructions/configuration; repository development CI and contributor workflows.
- First-party operating / deployment modes considered: ordinary LLMAgent + Runner execution; coordinator Team and other multi-agent compositions; Evolution-enabled Runner; Evolution-enabled OpenClaw with default automatic gates or optional human hold gates; offline Evolution optimization and PromptIter as supported adaptation modes.
- Recursion level: one deployed tRPC-Agent-Go agent organization. Configured member Agents can be treated as bounded S1 units inside a coordinator Team when they own separate role-specific model/tool work; merely nesting Agents, graphs, or teams does not establish lower recursive viability.
- Reviewed revision: `28cb50c1d927a586521de028aed95bde2a018144`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

tRPC-Agent-Go is a Go agent framework whose core execution abstraction is `agent.Agent`. `LLMAgent` supplies a model-driven operational loop with tools, skills, state and sub-agent visibility; `Runner` supplies sessions, memory and lifecycle plumbing around it. The model can select tools and, where configured, specialist agents; returned tool/member results become later model context.

The multi-agent layer contains Chain, Parallel, Cycle, transfer and a higher-level `team` package. The coordinator Team is stronger than bare routing: one model-driven coordinator remains in charge, chooses member calls, receives member results as tool results, may call multiple members and synthesizes the final answer. However the framework explicitly leaves specialist discovery, authorization, role definitions and application configuration to the adopter. The framework therefore exposes a complete coordination construction path, while the concrete inter-S1 disturbance and coordination policy are not supplied by tRPC-Agent-Go itself.

Evolution is a separate first-party background learning loop. On completed tasks it applies a review policy, passes qualifying transcripts to an LLM Reviewer, reconciles proposed skills, applies schema/safety/effectiveness and optional human gates, publishes accepted `SKILL.md` revisions, refreshes the shared skill repository, and makes those skills available to later agent runs through `skill_load`. OpenClaw contains first-party wiring that creates the service, revision store, gates and managed skill directory when Evolution is enabled. A separate optimization path evaluates candidate skills on feedback/validation/holdout splits before optional revision submission, and PromptIter similarly turns evaluation failures into candidate prompt patches with validation-set acceptance. These paths corroborate prospective adaptation, but ordinary Evaluation is not credited as S3*: it measures/regresses behavior and does not independently close a corrective audit path into current operations.

Primary evidence:

- [`docs/mkdocs/en/agent.md`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/docs/mkdocs/en/agent.md) — LLMAgent/Runner operational unit, tools/state and execution model.
- [`agent/llmagent/llm_agent.go`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/agent/llmagent/llm_agent.go) — first-party model/tool execution implementation.
- [`docs/mkdocs/en/multiagent.md`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/docs/mkdocs/en/multiagent.md) — sub-agent construction, Chain/Parallel/Cycle semantics, application-owned discovery and delegation boundaries.
- [`docs/mkdocs/en/team.md`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/docs/mkdocs/en/team.md) — coordinator Team, member-as-tool result feedback, shared history and synthesis behavior.
- [`docs/mkdocs/en/evolution.md`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/docs/mkdocs/en/evolution.md) — asynchronous self-learning architecture, review policy, Reviewer/Reconciler/gates/Publisher, revision lifecycle, future skill loading, rollback and offline optimization.
- [`runner/runner.go`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/runner/runner.go) — `WithEvolutionService` integration of completed sessions with the learning service.
- [`openclaw/app/evolution_runtime.go`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/openclaw/app/evolution_runtime.go) — first-party deployment wiring for managed skills, immutable revisions and automatic quality gates.
- [`docs/mkdocs/en/evaluation/index.md`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/docs/mkdocs/en/evaluation/index.md) — evaluation assets, metrics, LLM Judge/static evaluators and result persistence.
- [`docs/mkdocs/en/promptiter.md`](https://github.com/trpc-group/trpc-agent-go/blob/28cb50c1d927a586521de028aed95bde2a018144/docs/mkdocs/en/promptiter.md) — evaluation-constrained future prompt adaptation with failure attribution, candidate generation and validation acceptance.

## Operational model

The ordinary S1 is a model-driven LLMAgent executing a bounded request through reasoning/model generation, tool calls, returned observations and eventual final response. Runner supplies the execution membrane but does not own the model's substantive operational choices.

When a coordinator Team is selected, member Agents can form distinct S1 work cells. The coordinator has a first-party feedback channel because member results become tool results in its subsequent context, but the framework intentionally leaves the actual specialist set, role boundaries and cross-unit coordination objective to application code. That is a constructor relation rather than autonomous framework-owned S2.

Evolution operates outside the current task path and changes future capability. Completed execution history and correction/recovery signals trigger a Reviewer; accepted reusable procedures become managed skills visible to later runs. This is prospective adaptation rather than ordinary persistence. Neither the Runner nor Evaluation package supplies a whole-system current-control authority, and the reviewed evaluators do not independently intervene in the current production loop, so S3 and S3* remain absent at this boundary.

## S1 — Operations

- State: A
- Function: execute bounded agent tasks through model-driven reasoning, tool/sub-agent selection, observation of returned results and final response generation.
- Disturbance / variety regulated: request ambiguity, model uncertainty, tool/environment results, tool failures, session state and new information returned during execution.
- Decisive decision or feedback right: choose model-generated next actions and tool calls, decide whether to delegate to an exposed specialist, use returned observations in later turns and terminate with a final answer.
- Decision owner: the configured model-driven LLMAgent.
- Supporting / enforcement mechanisms: Runner, tool execution, session/memory/state services, skill repository, callbacks/plugins, model generation bounds and cancellation/retry plumbing.
- Closure path: user/application input enters Runner → LLMAgent evaluates context and emits response/tool/delegation choices → first-party runtime executes the selected callable path → results return into model context → LLMAgent continues or emits the final result.
- Boundary reachability: LLMAgent and Runner are the documented primary execution path and require no adopter-authored control actor beyond selecting/configuring a model, tools and task instruction.
- Why this is / is not agent-owned: Runner constrains execution and transports state, but substantive tool/delegation/final-response choices are produced by the model agent rather than a fixed workflow alone.
- Evidence: `docs/mkdocs/en/agent.md`, `agent/llmagent/llm_agent.go`, `runner/runner.go`.
- Basis: explicit + structural
- Confidence: high
- Caveats: graph-only deployments can move decision rights into application-authored deterministic topology; the positive state rests on the first-party LLMAgent operating mode.

## S2 — Coordination

- State: C
- Function: provide a first-party coordinator-Team construction path that can regulate interaction among multiple specialized member Agents by selecting member work, receiving their outputs and feeding those outputs into subsequent coordinator/member behavior.
- Disturbance / variety regulated: independently produced specialist analyses can require combination, review, revision, shared context or ordering before one coherent answer can be produced.
- Decisive decision or feedback right: within a configured coordinator Team, the coordinator model chooses which member(s) to call and how to synthesize/use returned results; the adopter still defines the specialists, role boundaries and concrete coordination objective.
- Decision owner: model-driven coordinator Agent for runtime member selection/synthesis; application author for the organizational construction and disturbance-specific coordination contract.
- Supporting / enforcement mechanisms: `team.New`, AgentTool wrappers, member result aggregation, configurable shared parent history, parallel member calls, `WithSubAgents`, transfer and agent interfaces.
- Closure path: application supplies coordinator plus distinct members → coordinator selects members → members execute separate S1 work → results return as tool responses/shared history → coordinator can use the changed context for later member calls or final synthesis.
- Boundary reachability: all runtime machinery for coordinator/member feedback is first-party and directly composable, but a qualifying S2 organization requires the adopter to supply distinct S1 roles and an actual interference/coordination contract.
- Why this is / is not agent-owned: the framework owns the feedback mechanism and coordinator runtime, but not the organizational distinction that makes member interference material; therefore the path is constructor-owned rather than an autonomous packaged S2 organization.
- Evidence: `docs/mkdocs/en/team.md`, `docs/mkdocs/en/multiagent.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ChainAgent, ParallelAgent, CycleAgent, Swarm handoff and generic delegation are not credited as S2 on their own.
- Distinct S1 units: two or more configured member Agents, each capable of its own model/tool execution for a role-specific assignment.
- Inter-S1 disturbance: specialist outputs may be incomplete, inconsistent or require review/revision/integration, but the concrete disturbance must be defined by the application's roles and coordinator instruction.
- Attenuating coordination relation: the coordinator receives member outputs as tool results in shared context and can select additional member calls or synthesize/revise the combined answer.
- Feedback into subsequent S1 behaviour: a member's returned result becomes coordinator context and can influence subsequent model choices, including another member invocation with updated context where the application has configured that relation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party Team supplies a coordinator-mediated closed feedback surface suitable for multi-member review/integration, but the framework intentionally leaves the concrete interference policy to the adopter; hence `C` instead of treating bare routing as S2 or claiming `A`.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control function was established for the deployed agent organization.
- Disturbance / variety regulated: Runner handles active invocation lifecycle, cancellation, retries and session state, but the reviewed first-party paths do not maintain an organizationally meaningful whole-system view of current commitments/resources and then choose interventions over them.
- Decisive decision or feedback right: none established for qualifying S3 current-control decisions.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Runner lifecycle, context cancellation, retry controls, CycleAgent termination, graph checkpoints/HITL and session state were inspected as mechanisms rather than S3 ownership.
- Closure path: not applicable; these mechanisms execute or stop configured work but do not form a whole-system current-state → prioritization/resource/intervention → changed operations loop.
- Why this is / is not agent-owned: coordinator Agents can choose specialist calls inside a task, but that is task-level orchestration/coordination rather than authority over the organization's current portfolio of commitments and resources.
- Evidence: `docs/mkdocs/en/agent.md`, `docs/mkdocs/en/multiagent.md`, Runner/graph documentation inspected at the pinned revision.
- Basis: explicit + absence review
- Confidence: high
- Caveats: application code can build a manager/controller using these primitives; that downstream system would require its own assessment.

### Absence scope

- Surfaces inspected: Runner run control and lifecycle, LLMAgent execution, Team/coordinator patterns, Chain/Parallel/Cycle, graph checkpoint/HITL surfaces, session/memory state, Evaluation and Evolution service plumbing.
- Plausible first-party paths checked: coordinator Team as manager, CycleAgent escalation/termination, Runner cancellation/retry, graph workflow controls, and Evolution worker/revision management.
- Why no material first-party path remains: each candidate path either governs one active task/workflow, provides deterministic lifecycle enforcement, or belongs to future adaptation; none closes whole-system current-control over present organizational commitments/resources.

## S3* — Complementary audit

- State: —
- Function: no material first-party operational complementary-audit loop was established at the reviewed boundary.
- Disturbance / variety regulated: tRPC-Agent-Go can evaluate outputs/traces and review completed sessions, but the reviewed built-in paths do not independently challenge an operational unit's current claims and return findings into corrective current control.
- Decisive decision or feedback right: none established for a qualifying S3* audit function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Evaluation metrics, LLM Judge/static evaluators, Evolution Reviewer, effectiveness/safety/spec gates, revision audit logs and PromptIter validation are retained as evaluation/adaptation mechanisms.
- Closure path: not applicable for S3*; Evaluation produces persisted regression results, while Evolution/PromptIter use review signals for prospective skill/prompt change rather than a complementary current-control correction loop.
- Why this is / is not agent-owned: some evaluators can use separate judge models, but independence of a scorer is insufficient when its organizational function is offline evaluation/adaptation and no first-party path returns audit findings into current operational correction.
- Evidence: `docs/mkdocs/en/evaluation/index.md`, `docs/mkdocs/en/evolution.md`, `docs/mkdocs/en/promptiter.md`.
- Basis: explicit + absence review
- Confidence: high
- Caveats: an adopter may wire Evaluation into an independent release/runtime assurance membrane; that would be a separate constructor/downstream system and is not inferred here.

### Absence scope

- Surfaces inspected: static and LLM-Judge evaluators, evaluation set/metric/result managers, tool-trajectory evaluation, Evolution Reviewer and gates, immutable revision/audit storage, offline optimization holdout verification and PromptIter validation.
- Plausible first-party paths checked: judge-model evaluation, completed-session review, effectiveness gating, holdout evaluation, revision rollback and prompt acceptance.
- Why no material first-party path remains: these paths measure, gate or improve candidate/future behavior but do not independently inspect the current operating unit and drive a distinct corrective current-control response inside the assessed organization.

## S4 — Outside-and-then intelligence

- State: A
- Function: learn reusable future-facing operating procedures from completed interactions and make accepted adaptations available to subsequent agent tasks.
- Disturbance / variety regulated: repeated exploration cost, user corrections, recovered errors, recurring tool workflows, operational pitfalls and changes revealed by completed-task experience.
- Decisive decision or feedback right: decide whether a completed-session delta merits review, extract a reusable skill candidate from transcript evidence, reconcile it with existing skills, accept/reject/hold it through quality gates, publish accepted revisions and expose them to later runs.
- Decision owner: the Evolution subsystem, with LLM Reviewer owning semantic skill extraction and first-party review/gate/publisher machinery owning qualification and activation; optional HumanGate can deliberately move a configured promotion decision to a parent, but an autonomous no-human-gate mode is first-party and complete.
- Supporting / enforcement mechanisms: `DefaultReviewPolicy`, LLM Reviewer, Reconciler, SpecGate, SafetyGate, EffectivenessGate, optional HumanGate, immutable revision store/active pointer, Publisher, shared skill repository, `skill_load`, rollback and OpenClaw Evolution wiring.
- Closure path: completed task/session and correction/recovery/tool-use distinctions → review policy → LLM Reviewer extracts reusable workflow → reconcile/gates qualify revision → Publisher writes managed skill and repository refresh exposes it → a later similar task loads the skill and changes operational behavior.
- Boundary reachability: Runner directly accepts `WithEvolutionService`; the documented minimal path is first-party, and OpenClaw additionally ships first-party configuration/wiring for managed directories, revision store and automatic gates. No adopter-authored learning algorithm or return channel is required once the supported mode is enabled.
- Why this is / is not agent-owned: storage and gates constrain the process, but the semantic adaptation candidate is generated from environment-derived execution evidence by a dedicated reviewer model and automatically returned into future agent capability through the shared skill repository.
- Evidence: `docs/mkdocs/en/evolution.md`, `runner/runner.go`, `openclaw/app/evolution_runtime.go`, `docs/mkdocs/en/promptiter.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary memory/history is not the positive witness. Offline optimizer and PromptIter are corroborating adaptation paths; the canonical `A` can already be established by the online Evolution loop. Configuring a HumanGate creates a parent-assisted deployment mode but does not erase the first-party autonomous mode.
- External distinction: completed-session transcript evidence including multi-step tool use, explicit user correction and recovered errors; optional outcomes/evaluation evidence can further qualify candidate revisions.
- Future / prospective distinction: the Reviewer abstracts reusable workflows/pitfalls from past executions specifically so later similar tasks avoid repeated exploration and failure.
- Adaptation option generated: a structured managed `SKILL.md` revision (or, in separate first-party optimization modes, an improved skill/prompt candidate) with qualification state and revision history.
- Path back into current capability / S3: after publish and repository refresh, the same repository used by LLMAgent exposes the managed skill to future runs through skill overview/`skill_load`, directly changing the operational context and available proven procedure.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity or ultimate-policy decision loop was established at the reviewed system boundary.
- Disturbance / variety regulated: instructions, tool/sub-agent authorization, graph policy, Evolution gates and optional human approval can constrain behavior, but they do not constitute a first-party legitimate ultimate-authority process for deciding system identity/policy conflicts.
- Decisive decision or feedback right: none established for qualifying S5 identity/ultimate-policy closure.
- Decision owner: none established.
- Supporting / enforcement mechanisms: LLMAgent instruction/system prompt, application-owned agent/sub-agent construction, tool authorization, configuration, Evolution HumanGate and graph HITL were inspected as policy inputs/enforcement or parent hooks.
- Closure path: not applicable; the first-party framework consumes configured policy/approval decisions but does not itself establish an identity issue → ultimate authority → authoritative policy decision → returned operation loop.
- Why this is / is not agent-owned: prompts and approval callbacks may encode or solicit policy, but the framework explicitly leaves application configuration/authorization to the adopter and does not infer ultimate authority from a human gate.
- Evidence: `docs/mkdocs/en/agent.md`, `docs/mkdocs/en/multiagent.md`, `docs/mkdocs/en/evolution.md`.
- Basis: explicit + absence review
- Confidence: high
- Caveats: a downstream application can place organizational policy/identity authority above tRPC-Agent-Go; that parent system must be assessed separately.

### Absence scope

- Surfaces inspected: instructions/system prompts, dynamic agent/sub-agent configuration, tool authorization boundaries, graph HITL/interrupts, Evolution HumanGate/approval/rollback and OpenClaw configuration.
- Plausible first-party paths checked: human approval as ultimate authority, application-owned configuration, self-learning skill promotion, prompt optimization and runtime instruction changes.
- Why no material first-party path remains: all inspected surfaces either receive externally supplied policy, enforce configured constraints or govern a bounded candidate change; none establishes the reviewed agent organization's own legitimate ultimate-policy/identity authority and closure loop.

## Recursion

tRPC-Agent-Go can nest Agents, Teams and graphs, including Team-inside-Team arrangements, but structural nesting is not sufficient evidence of VSM recursion. Member Agents can be distinct S1 work cells at the parent team boundary when they own role-specific operations. The pinned first-party evidence does not establish that each configured nested member automatically closes its own S2-S5 metasystem and identity/environment relation, so no lower viable recursion is credited generically.

## Variety and escalation

Operational variety is attenuated through model instructions, tool/skill visibility, session/memory context, graph/team structure and configured execution bounds, while model-driven tool/member choices amplify response capacity. In a coordinator Team, member results return to the coordinator rather than remaining isolated, enabling adopter-defined review/integration loops.

CycleAgent's `EscalationFunc`, Runner cancellation and HITL interrupts are bounded execution controls; they are not promoted to S3/S5. Human Evolution gates can hold a candidate revision for approval, but that is an optional parent intervention into S4 promotion rather than evidence that the framework owns S5.

Evolution preserves longer-term variety by turning corrections, recovered errors and complex tool-use histories into reusable skills. Gate failures, pending evaluation/approval, immutable revision history and rollback bound that adaptation without changing its functional classification.

## Evidence gaps

- Coordinator Team provides a closed runtime feedback mechanism, but tRPC-Agent-Go intentionally leaves specialist discovery, role boundaries and concrete cross-unit disturbance/coordination policy to application code; S2 is therefore `C`, not `A`.
- No generic S3 is inferred from Runner lifecycle, retry/cancel, graph execution, CycleAgent stopping or coordinator delegation because none establishes whole-system current-control at this boundary.
- Evaluation and separate judge models are not promoted to S3*: the reviewed first-party return paths serve regression and prospective Evolution/PromptIter adaptation rather than independent corrective current control.
- Evolution is opt-in, but once enabled it has a first-party autonomous closure path, including in shipped OpenClaw wiring. The default HumanGate is disabled; deployments that enable one deliberately introduce parent control over selected promotions.
- Application-supplied datasets/evaluators in offline optimization/PromptIter are not needed for the positive S4 finding; the online completed-session Evolution loop independently closes S4.
- Static prompts, application authorization and human approval hooks were inspected but do not establish S5.