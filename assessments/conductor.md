---
harness_id: conductor
project_name: Conductor
repository: https://github.com/microsoft/conductor
review_ref: 87f7788e60c7cbb8895832b9edfb4e63f3924590
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Conductor

## Review boundary

- System in focus: one first-party Conductor workflow-run organization at pinned revision `87f7788e60c7cbb8895832b9edfb4e63f3924590`, including the workflow engine, provider-backed agent steps, workflow context, parallel / for-each execution, semantic validator, human-gate and mid-run guidance paths, checkpoint/resume machinery, web dashboard and first-party current-run control surfaces.
- Purpose and identity: execute a version-controlled multi-agent workflow whose operational steps can use LLM-backed agents while Conductor deterministically owns routing, sequencing, context transport, limits, persistence, validation hooks and operator intervention surfaces.
- Relevant environment: user/workflow inputs, target repository or application state reached by configured tools/providers, provider/model responses, external MCP/tool results, configured human gate decisions, and operator guidance during the live run.
- Standard-distribution boundary: shipped Conductor CLI/runtime, workflow engine, executor/providers, web dashboard/Fleet control surfaces, built-in step types, validator and bundled examples/documentation that describe supported runtime behaviour. External model endpoints, GitHub Copilot/Claude runtimes, MCP servers, target repositories and business services remain dependencies. Repository-development CI, contributor governance and tests are corroborating evidence only and do not donate VSM ownership.
- First-party operating / deployment modes considered: ordinary sequential provider-backed agent workflows; static parallel groups; dynamic for-each groups; optional per-agent semantic `validator:`; human gates/questions/dialog; interactive/web/web-background runs with stop/resume/kill/guidance; checkpoint/resume; Fleet discovery/control of live runs.
- Recursion level: one Conductor workflow run around one declared workflow objective. Provider-backed LLM steps are operational S1 units when they perform substantive work; parallel members are distinct concurrent S1 units for the S2 witness. Fleet-wide process management is inspected as a parent current-control surface but is not used to redefine the assessed recursion as every run on the host.
- Reviewed revision: `87f7788e60c7cbb8895832b9edfb4e63f3924590`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Conductor is a workflow runtime rather than an autonomous top-level planner. Its README explicitly describes routing as deterministic: Jinja2 expressions are evaluated in order and the first matching condition wins, with no LLM in the orchestration loop deciding what runs next. The workflow engine owns topology, context propagation, limits, retries, checkpoints, route evaluation, step dispatch and lifecycle events. Provider-backed `agent` steps are the autonomous actors inside that deterministic envelope: `AgentExecutor` renders the step prompt/tools, calls the configured provider, returns model/tool results, validates structured output and hands the result back to workflow context.

Parallel execution adds a concrete constructor-owned coordination mechanism. Before static parallel or dynamic for-each execution, the engine deep-copies the current workflow context. Every concurrent member builds its local input from that same pre-group snapshot; sibling outputs are not written into a mutable shared context while members run. Only after the group completes does the engine aggregate outputs/errors and publish the group result to workflow context. The first-party documentation states the intended regulated disturbance directly: immutable snapshots prevent race conditions and prevent concurrent agents from interfering with each other. Because the workflow author selects the parallel topology and the deterministic engine supplies the isolation, no autonomous agent owns the coordination decision; this is S2 constructor ownership.

Current control is instead strongly parent-governed. The live dashboard projects the current workflow topology and step states, while the engine/web server exposes human gates plus `stop`, `resume`, `kill` and mid-run `guidance`. Guidance is not merely recorded: `submit_guidance()` queues the operator text, `_drain_pending_guidance()` applies it at the next root loop boundary, `add_user_guidance()` inserts it into workflow context, and subsequent steps receive the changed guidance state. When an agent is paused, guidance can be applied immediately before re-execution. This gives a legitimate operator a current-run view and a returned decision path over current commitments/intervention, establishing S3 as `P`. Deterministic routing, limits and schedulers are supporting enforcement rather than an autonomous S3 owner.

Conductor also ships a dedicated semantic-verification constructor. A per-agent `validator:` block triggers a second LLM call implemented as a synthetic validator agent with its own system rubric, structured `{passed, issues}` result and no ordinary tools. A failed judgment can append actionable `Validation feedback` and re-run the primary agent once, so the audit-to-correction edge is closed. However, the built-in validator uses the primary provider and receives only the rendered primary task plus primary output; it has no first-party read-only repository/environment evidence path of its own. A different validator model may be configured, but sufficiently independent operational access still depends on how the workflow/deployment defines the audited artifact or composes evidence. Conductor therefore supplies an S3*-specific constructor, not an independently closed autonomous auditor: `S3*=C`.

The review did not find an S4 loop. The strongest apparent path is the bundled `skills-self-improving-workflow.yaml`, but its own first-party comments say it is a building block that a future `conductor watch` would chain into a closed generate-review-fix loop; the current example performs one workflow-authoring task and does not observe external change, persist a prospective capability adaptation and feed that adaptation back into later Conductor operation. Update checks, retries, context compaction and skill discovery likewise do not close outside-and-then intelligence.

No S5 path is established. Workspace instructions, `system_prompt`, workflow YAML, limits and human gates can constrain ordinary operation, but the pinned runtime does not expose an identity/ultimate-policy issue that is escalated to legitimate authority and returned to govern the same organization. Mid-run guidance is current operational steering and therefore S3, not S5; static instruction files remain prompt/configuration inputs rather than a live identity-policy closure.

Primary evidence:

- [`README.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/README.md) — deterministic orchestration boundary, provider-backed agents, parallel execution, human-in-the-loop, web dashboard, Fleet Manager and workspace-instruction surfaces.
- [`src/conductor/executor/agent.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/executor/agent.py) — provider-backed agent execution and return of model/tool output into the first-party workflow runtime.
- [`src/conductor/engine/workflow.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/engine/workflow.py) — workflow loop, immutable parallel/for-each context snapshots, group-output publication, validator retry closure and guidance return into current workflow context.
- [`docs/parallel-execution.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/parallel-execution.md) — explicit no-race/no-interference rationale and immutable snapshot semantics for concurrent agents.
- [`src/conductor/engine/validator.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/engine/validator.py) and [`docs/workflow-syntax.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/workflow-syntax.md) — second-LLM semantic validator, rubric, independence limits and corrective retry behaviour.
- [`src/conductor/web/server.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/web/server.py) and [`docs/fleet.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/fleet.md) — live current-run state, stop/resume/kill/gate/guidance controls and Fleet visibility.
- [`examples/skills-self-improving-workflow.yaml`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/examples/skills-self-improving-workflow.yaml) — first-party statement that the demonstrated one-pass author/review/fix pattern is only a building block for a future closed iterative watcher.
- [`docs/cli-reference.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/cli-reference.md) — workspace instruction discovery/injection and operator runtime-control interfaces.

## Operational model

A workflow definition establishes deterministic control structure. Within that structure, an LLM-backed `agent` step receives model-visible prompt/context/tools and owns the substantive task judgment appropriate to that step. The engine then validates/transports the output, evaluates deterministic authored routes and starts the next configured step. Parallel members can perform independent S1 work simultaneously while seeing isolated pre-group context. Human/operator controls can intervene in the live run; those controls are classified by the function they close rather than being promoted simply because a human is present.

Static workflow authorship, route expressions, retry policies, iteration/time limits, checkpoint machinery, tool allowlists and provider configuration are treated as construction/support/enforcement unless a function-specific organizational decision right is separately established.

## S1 — Operations

- State: A
- Function: perform substantive model-driven work for a workflow step by interpreting the rendered task/context, choosing model/tool actions through the configured provider runtime and producing an operational result consumed by the workflow.
- Disturbance / variety regulated: open-ended user/workflow tasks, changing task context, provider/model reasoning, tool/MCP results, target repository/application state visible through configured tools and validation/retry feedback.
- Decisive decision or feedback right: choose the substantive content/tool actions needed to satisfy the current agent step and revise that work from returned model/tool feedback within the provider-backed agent loop.
- Decision owner: the configured provider-backed LLM agent executing the Conductor `agent` step.
- Supporting / enforcement mechanisms: `AgentExecutor`, prompt/context renderer, provider adapter, resolved tools/skills/MCP configuration, structured-output parser, retries, timeouts, usage accounting and workflow context transport.
- Closure path: deterministic workflow dispatches an agent step → Conductor renders context/prompt/tools → provider-backed agent performs model/tool work → result returns to `AgentExecutor` → first-party runtime validates/records the output → workflow context receives the result and subsequent operation can consume it.
- Boundary reachability: provider-backed `agent` is a standard first-party step type used by ordinary `conductor run`; the credited model decision path is reached through the shipped executor/provider interfaces at the frozen revision, not through a repository-development test or adjacent benchmark.
- Why this is / is not agent-owned: removing the model-driven actor while leaving routing, limits, context and persistence intact removes the substantive open-ended task decision. The deterministic workflow engine can still sequence steps but does not recreate the operational judgment.
- Evidence: [`src/conductor/executor/agent.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/executor/agent.py); [`README.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: external provider/model runtimes supply inference and may own their internal tool loop; the assessment credits the autonomous operational actor reached through Conductor's standard provider-backed agent mode, not Conductor's deterministic router as an autonomous planner.

## S2 — Coordination

- State: C
- Function: attenuate concurrent S1 interference through immutable pre-group workflow-context snapshots and delayed aggregation of sibling results.
- Disturbance / variety regulated: multiple provider-backed S1 agents in one parallel group can otherwise observe/write evolving shared workflow state concurrently, producing race-dependent sibling inputs or cross-agent context interference.
- Decisive decision or feedback right: select a parallel/for-each coordination topology whose members execute against a frozen pre-group context rather than a live mutable sibling-shared context.
- Decision owner: workflow author/configuration chooses the topology; deterministic Conductor runtime implements the dedicated coordination primitive. No autonomous agent is evidenced as deciding whether or how to apply the isolation relation.
- Supporting / enforcement mechanisms: `copy.deepcopy(self.context)`, per-member `build_for_agent(...)`, prohibition on same-group sibling references, `asyncio.gather`, structured group output/error aggregation and post-group context publication.
- Closure path: workflow reaches parallel group → engine deep-copies current context → distinct S1 members execute concurrently against the snapshot → sibling writes cannot alter another member's live input → engine gathers outputs/errors → group result is published into workflow context → downstream S1 behaviour can consume the coordinated aggregate.
- Boundary reachability: static parallel and dynamic for-each groups are documented and implemented first-party workflow constructs at the frozen revision and execute through the normal workflow engine.
- Distinct S1 units: provider-backed agents named in a static parallel group, or runtime-created per-item instances of a provider-backed for-each agent, each performing an independent operational task against its local input context.
- Inter-S1 disturbance: concurrent members would otherwise share mutable workflow context during execution, allowing race-dependent sibling observation/mutation; first-party documentation explicitly describes immutable snapshots as preventing race conditions and agent interference.
- Attenuating coordination relation: every concurrent member receives a context derived from the same deep-copied pre-group snapshot, and sibling outputs are withheld from common workflow context until aggregation after concurrent execution.
- Feedback into subsequent S1 behaviour: after the parallel/for-each group completes, Conductor publishes the aggregated outputs/errors as the group result; downstream steps can then read that coordinated state deterministically.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive witness is the explicit anti-race isolation relation between plural concurrent S1 units, not the fact that agents are parallel, routed, named or able to exchange results.
- Why this is / is not agent-owned: Conductor supplies the S2-specific isolation and closure, but the runtime/configuration fixes it. The standard distribution does not show an autonomous agent making the coordination judgment or revising the attenuation relation from live inter-S1 disturbance, so the correct publication state is constructor `C`.
- Evidence: [`src/conductor/engine/workflow.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/engine/workflow.py); [`docs/parallel-execution.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/parallel-execution.md); [`docs/dynamic-parallel.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/dynamic-parallel.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic sequencing, route expressions, dependency declarations, concurrency limits and MCP transport locks are not independently credited as S2. The claimed constructor is specifically the first-party context-isolation relation for plural operational agents.

## S3 — Inside-and-now control

- State: P
- Function: let a legitimate run operator inspect the current workflow organization and intervene in current execution/commitments through guidance, gate decisions, pause/resume or termination controls.
- Disturbance / variety regulated: the live run may be following an unsuitable current path, an active agent may need redirection, a human gate may need a current commitment decision, or the run may need to pause, resume or terminate as current evidence changes.
- Decisive decision or feedback right: decide whether the current run should receive new guidance, resolve a gate one way or another, pause/re-execute, continue, or terminate.
- Decision owner: the legitimate human/operator controlling the live Conductor run through the first-party dashboard/CLI/Fleet surfaces.
- Supporting / enforcement mechanisms: workflow event history/DAG projection, current-step state, run records, `/api/guidance`, `context.user_guidance`, `/api/stop`, `/api/resume`, `/api/kill`, gate response queue, checkpoints and Fleet live-run discovery.
- Closure path: current workflow/step state is projected → operator judges a current intervention → first-party control endpoint accepts guidance/gate/stop/resume/kill decision → engine applies the returned decision to live runtime state → next step or re-executed agent observes the changed guidance/gate/current-control state, or the run pauses/terminates.
- Boundary reachability: the web dashboard, CLI guidance/gate commands and Fleet controls are shipped runtime surfaces wired to the same workflow engine/event/control objects used by ordinary `run`/`resume` modes; the parent loop does not rely on Microsoft repository-maintainer governance.
- Whole-system current view: for the assessed workflow-run recursion, the dashboard exposes the workflow topology and live step/agent states; the Fleet surfaces additionally discover every live Conductor process on the host and can drill into per-run current status.
- Current-control decision scope: parent guidance changes context consumed by subsequent work; gate responses select current branches/commitments; stop/resume/kill changes whether current work continues and whether a paused agent is re-executed.
- Why this is / is not agent-owned: the first-party runtime has no model-driven top-level controller that receives the whole current run and autonomously decides these interventions. README explicitly states orchestration/routing is deterministic rather than LLM-decided. Limits/schedulers enforce authored rules; the closed discretionary current-control owner evidenced here is the parent operator, so S3 is standalone `P`.
- Evidence: [`src/conductor/engine/workflow.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/engine/workflow.py); [`src/conductor/web/server.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/web/server.py); [`docs/fleet.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/fleet.md); [`README.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Fleet is used only as corroborating parent visibility/control. The assessed recursion remains one workflow run; cross-run portfolio prioritization is not claimed as a separate autonomous S3 organization.

## S3* — Complementary audit

- State: C
- Function: challenge a provider-backed agent's semantically valid-looking output through a separate LLM grading pass and return concrete rejection findings into a corrective primary-agent re-run.
- Disturbance / variety regulated: the primary agent can produce output that satisfies structural schema while remaining semantically wrong, incomplete, fabricated or off the workflow author's acceptance rubric.
- Decisive decision or feedback right: a synthetic validator LLM judges `passed` versus failed rubric criteria and emits actionable `issues`; on failure the engine decides from that verdict whether to perform the configured corrective retry.
- Decision owner: Conductor supplies the dedicated validation/grading primitive and synthetic model call, but does not guarantee sufficiently independent access to operational reality in the built-in mode. The developer/workflow must compose an audit situation whose grader has independence appropriate to the claim, so the publication state is `C` rather than `A`.
- Supporting / enforcement mechanisms: `OutputValidator`, separate synthetic `AgentDef`, dedicated validator system prompt/rubric, structured `{passed, issues}` schema, optional different validator model, separate usage/events, `max_retries`, `## Validation feedback` construction and primary-agent re-execution.
- Closure path: primary agent produces candidate output → second LLM validator receives the rendered primary task + candidate and issues pass/fail findings → failed findings become `Validation feedback` → Conductor re-runs the primary agent once → corrected candidate becomes the effective output when the retry succeeds.
- Boundary reachability: `validator:` is a documented first-party `agent` field implemented in the normal workflow engine and demonstrated by `examples/validator.yaml`; it is not a CI-only evaluator or repository-development benchmark.
- Claim being audited: whether the current provider-backed agent output satisfies a deployment-defined semantic acceptance rubric before that output is accepted as the effective result.
- Ordinary reporting path: the primary agent returns its normal provider/model output through `AgentExecutor` into the workflow engine.
- Complementary access path: a separate synthetic validator agent receives the primary task and output after primary completion, executes another LLM judgment with its own validator system rubric and returns a structured verdict/issues object outside the primary agent's normal completion call.
- Independence boundary: call/context identity is separate and the validator has no ordinary tools, but the first-party built-in path uses the same provider object, defaults to the same model and sees only the primary rendered task/output. A workflow may select another validator model, yet Conductor does not itself supply independent repository/environment evidence access. Sufficient operational independence therefore remains deployment-dependent.
- Who acts on findings: deterministic Conductor validator plumbing injects failed issues into a new primary-agent turn/re-run; the primary model then owns the substantive corrected operational output.
- Why this is / is not agent-owned: the grading verdict itself is model-generated, but `A` requires the complete complementary-audit function, including sufficient independence. Because that independence is not guaranteed by the shipped built-in validator, the first-party dedicated primitive is credited as constructor `C` rather than autonomous S3*.
- Evidence: [`src/conductor/engine/validator.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/engine/validator.py); [`src/conductor/engine/workflow.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/engine/workflow.py); [`docs/workflow-syntax.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/workflow-syntax.md); [`examples/validator.yaml`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/examples/validator.yaml).
- Basis: explicit + structural
- Confidence: high
- Caveats: a deployment that audits only a self-contained text artifact may obtain adequate practical independence from a separate model call; conversely, claims about external files/actions require independent evidence the stock validator cannot gather. The assessment therefore credits the dedicated constructor without assuming deployment-specific independence.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then adaptation loop is established within the reviewed standard-distribution boundary.
- Disturbance / variety regulated: not established for S4. Current-task retries, human guidance, update notices and one-pass workflow author/review/fix examples regulate present work or software maintenance rather than a prospective environment-facing adaptation function for the running organization.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: skill discovery/injection, workflow examples, retries, semantic validator feedback, provider/runtime diagnostics, release update check, context compaction and ordinary workflow loops are present but remain below S4 under the reviewed boundary.
- Closure path: not applicable; no first-party path was found that observes an external/future distinction, generates a persistent adaptation option and returns the adopted change into later current capability of the assessed workflow organization.
- Boundary reachability: negative finding covers the shipped workflow engine, skills/runtime configuration, bundled examples, update/diagnostic surfaces and current-run operator controls at the frozen revision.
- Why this is / is not agent-owned: no qualifying S4 organizational function is established, so there is no S4 decision owner to classify.
- Evidence: [`examples/skills-self-improving-workflow.yaml`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/examples/skills-self-improving-workflow.yaml); [`README.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/README.md); [`docs/workflow-syntax.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/workflow-syntax.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Conductor is expressive enough for a user to author future-oriented workflows; generic workflow composability is not itself an S4 constructor under the Methodology.

### Absence scope

- Surfaces inspected: workflow engine and routing; provider-backed agent execution; validator/retry path; skills and skill discovery; bundled self-improving-workflow example; context compaction; update check; checkpoint/resume; Fleet/dashboard and human guidance; workflow/instruction configuration.
- Plausible first-party paths checked: self-improving workflow as S4; skill learning/persistence; external-update detection; validator-driven capability improvement; retries/refinement loops; model/provider adaptation; operator guidance as parent S4.
- Why no material first-party path remains: the strongest apparent self-improvement example explicitly says its current one-pass author/review/fix flow is only a building block for a future `conductor watch` closed loop. Other mechanisms handle current execution, static skill/config selection or Conductor software updates and do not close external observation → prospective adaptation option → persistent capability change → later operational use at the assessed recursion.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy governance function is established within the reviewed standard-distribution boundary.
- Disturbance / variety regulated: not established at identity/ultimate-policy level. Workflow instructions, prompts, limits, approval gates and operator guidance regulate ordinary tasks/current execution but do not evidence a live issue about who the organization is or what ultimate policy it is legitimately permitted to change.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: workflow YAML, `system_prompt`, `--instructions`, `--workspace-instructions`, `AGENTS.md`/`CLAUDE.md`/Copilot instruction discovery, human gates/questions, tool/provider configuration and current-run guidance.
- Closure path: not applicable; no identity/ultimate-policy issue → legitimate authority → authoritative decision → return-to-operation path was found.
- Boundary reachability: negative finding covers the documented and implemented prompt/instruction, gate, guidance, configuration and runtime-control surfaces at the pinned revision.
- Why this is / is not agent-owned: the absence conclusion is functional rather than about autonomy. No qualifying S5 decision path is established for either an agent or parent owner.
- Evidence: [`docs/cli-reference.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/cli-reference.md); [`docs/workflow-syntax.md`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/docs/workflow-syntax.md); [`src/conductor/web/server.py`](https://github.com/microsoft/conductor/blob/87f7788e60c7cbb8895832b9edfb4e63f3924590/src/conductor/web/server.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: project/workspace owners can edit static instruction files and workflow YAML, but the Profile explicitly does not treat a system prompt or policy file alone as S5. The pinned runtime supplies no first-party policy-level escalation/amendment protocol that distinguishes ultimate policy from ordinary configuration.

### Absence scope

- Surfaces inspected: workflow-level and per-agent system prompts; explicit/workspace instruction discovery; human gates/questions/dialog; mid-run guidance; route/limit/provider/tool policy; checkpoints/resume; Fleet/dashboard controls; validator criteria and workflow authoring examples.
- Plausible first-party paths checked: parent-authored workspace instructions as S5; `system_prompt` as identity; workflow YAML/limits as ultimate policy; human gates as parent governance; mid-run guidance as policy amendment; semantic validator rubric as success-policy governance.
- Why no material first-party path remains: these paths either statically configure S1 behaviour, validate current output or let a parent intervene in current execution. None identifies an identity/ultimate-policy issue, segregates legitimate authority for that issue, records an authoritative policy decision and returns it through a specific S5 closure into subsequent operation. Parent current-run guidance is already accounted for as S3.

## Recursion

The assessment fixes recursion at one Conductor workflow run. Provider-backed agent steps are operational S1 units; static/dynamic parallel execution can contain multiple simultaneous S1s. The deterministic workflow engine is the organizing substrate and does not become an autonomous S3 merely because it sequences those units. The human/operator sits at the parent boundary for the evidenced S3 mode. Fleet can observe multiple independent workflow runs on one host, but the assessment does not combine those runs into a higher-recursion organization without evidence of shared mission/current-control semantics beyond process management.

## Variety and escalation

Conductor attenuates operational variety through authored workflow topology, context modes, schema validation, retries, time/iteration limits, isolated parallel snapshots and provider/tool configuration. Those mechanisms remain construction/enforcement unless the relevant organizational discretion is independently established. Parallel snapshotting specifically attenuates cross-S1 context races. Semantic validation exposes a dedicated challenge/retry seam but leaves sufficient audit independence to deployment composition. Exceptional current-run situations can reach the parent through human gates, dashboard/Fleet state and direct operator intervention; guidance returns into workflow context at the next control boundary. That is an S3 parent loop rather than generic S5 escalation.

## Evidence gaps

- S2 is deliberately narrow: only the immutable context-snapshot / delayed-aggregation relation is credited. Concurrency limits, route ordering and ordinary dependencies are not independently counted as coordination.
- S3 publishes only the parent mode. Deterministic authored routing, retry and limit enforcement do not establish a separate `C` or `A` S3 owner without discretionary whole-run current-control judgment.
- S3* is constructor-owned because the stock validator's second model call lacks independent first-party access to repository/environment evidence. A deployment that supplies a materially independent audited artifact/ground-truth relation could realize the constructor more strongly, but that deployment-specific independence is not silently imported.
- S4 remains absent even though first-party examples use “self-improving” language: the pinned example explicitly defers the closed iterative watcher to future work.
- S5 remains absent despite durable instructions/configuration because no identity/ultimate-policy issue and governance return loop is implemented at the assessed recursion.
