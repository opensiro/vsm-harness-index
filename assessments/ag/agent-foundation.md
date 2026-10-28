---
harness_id: agent-foundation
project_name: Agent Foundation
repository: https://github.com/converge-ai-labs/agent-foundation
review_ref: 19bef266e239bf42adf258159b6f52195daa4d01
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Agent Foundation

## Review boundary

- System in focus: a configured first-party Agent Foundation **Harness/Service** deployment executing a managed agent and, when selected, declared subagents and the built-in Finding Agent analysis path. This is not the development organization behind the OSS repository.
- Purpose and identity: expose reusable model-driven agents and managed execution through Harness, with Service owning durable runs, identity, threads, environment bindings, permissions, recovery and optional trace-based diagnosis.
- Relevant environment: application/user requests, model-provider responses, live or simulated tool environments, persistence, worker resources, external execution environments, and retained traces of completed runs.
- Standard-distribution boundary: `packages/a13n-harness` runtime, its packaged `SubagentCapability` and built-in toolsets; `packages/a13n-service` managed agents, runs, subagent operator, trace/Findings endpoints, Console review and Composer resource-edit mode. These are selectable first-party operating modes, not merely repository examples.
- Credited operating / distribution surfaces: configured Harness run stream with provider or first-party scripted model, Service managed message/worker threads, optional inline or async child agents, and operator-invoked Service Insights → Findings analysis with a separately instantiated Finding Agent. An optional capability is credited only for its evidenced selected mode; it is not presumed active for every run.
- Adjacent first-party surfaces excluded from ownership: benchmark/eval charts, development Harness UI, e2e fixtures and CI; the tests corroborate shipped call paths but do not themselves act in production. Third-party PydanticAI, external LLM inference providers, Docker/host runtime, remote MCP servers and user applications have their own boundaries; they are not silently credited as Foundation-owned higher-level organizational functions.
- First-party operating / deployment modes considered: embedded Harness, Service/Console managed runs, inline and Host-implemented async subagents, persisted thread continuations, scheduled execution, tool review, and selected-trace Finding Agent diagnosis followed by human-mediated Composer correction. Excluded: hypothetical custom plugins or independently developed multi-agent governance based only on extension points.
- Recursion level: a configured agent or child is an operational S1; the Service/Harness deployment provides supporting infrastructure and optional independent diagnostic S3* access. Cross-tenant/cloud organization, external user application and provider governance are higher or adjacent recursions.
- Reviewed revision: `converge-ai-labs/agent-foundation@19bef266e239bf42adf258159b6f52195daa4d01`; verified local `HEAD` equals frozen SHA, Apache-2.0 distribution.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Harness constructs an executable from `AgentDefinition`, `AgentSpec`, selected capabilities, model and bindings, then drives PydanticAI's `run_stream_events` inside its own stateful `HarnessRunStream._run_attempts` loop. Model-selected tool calls, streaming observations, cancellation/steering, deferred results and recovery are integrated into subsequent requests and durable state. Foundation supplies this real first-party operating integration, while the model/provider and PydanticAI implement their respective underlying inference and agent-runtime mechanics. [Harness attempt loop](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-harness/a13n_harness/_run_stream.py#L1271-L1445), [Harness README](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/README.md#L9-L17).

Selected `SubagentCapability` gives a parent model the inline `delegate`/`resume_subagent` tools, with nested child run execution, state, event attribution and results. Its async variant exposes `delegate`, `info`, `wait`, `steer`, `cancel` and `resume` through a Host-supplied `SubagentOperator`; Service supplies a concrete `ChildRuns` operator. These are real task delegation and lifecycle mechanisms, but their existence alone is not an S2 disturbance circuit or S3 whole-system decision. [Inline delegation implementation](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-harness/a13n_harness/toolsets/delegation.py#L35-L157), [async subagent tools](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-harness/a13n_harness/toolsets/subagents.py#L37-L201), [Service child operator](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/subagents.py#L92-L270).

In a distinct selected Service mode, `Insights → Findings` admits trace-range or one-trace analysis, creates a separate managed Finding Agent run and equips that agent with read-only trace/span/executed-config tools plus a bounded `POST /findings` submission right. The target agent cannot be the Finding Agent itself. Findings have evidence citations, review values and notes; a person may inspect them and invoke Composer to propose a changed agent revision, whose write requires approval. Finding Agent has no repair/publish power. [Analysis creation and target exclusion](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/findings/analysis.py#L90-L125), [separate analysis run](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/findings/analysis.py#L215-L290), [bounded audit tools](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/findings/preset.py#L5-L49), [operating workflow](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/docs/a13n-service/agents-and-runs.md#L430-L443).

## Operational model

The main agent absorbs user-task variety through model judgment over tool choices, observations and continuations, within configured permissions and infrastructure. Optional children are separate model-driven operational cells; the parent chooses tasks and can consume their results. Service workers serialize contested updates to a *single thread* and preserve FIFO messages across attempts; this protects execution history but is not a demonstrated correction of interference **between two autonomous S1 units**. Finding Agent instead samples independent retained evidence of ordinary operational claims and produces reviewable diagnoses; operator/Composer can feed accepted corrections into a new revision. No live provider-dependent run was executed for this assessment; source and first-party scripted-model tests support the structural mapping.

## S1 — Operations

- State: A
- Function: perform substantive user/application tasks by selecting tools and responding to task feedback; this includes separately declared model-backed child operations when activated.
- Disturbance / variety regulated: changing requests, partial external information, tool failures, context/history and environment responses.
- Decisive decision or feedback right: the selected model chooses the next action/tool arguments or final response using recent returned observations; a child model separately decides inside its delegated task.
- Decision owner: configured parent/child model-backed agent for local semantic task discretion; provider and PydanticAI implement inference/tool-turn substrate, while Harness/Service defines the usable operating and recovery contract.
- Supporting / enforcement mechanisms: `HarnessRunStream`, capability bindings, tool permission gate, environment mounts, state restoration, deferred results, usage limits, worker ownership, inbox and session records.
- Closure path: task input → model-generated tool action → Harness/Service execution under configured gates → observation/deferred result/history → next model choice or final response; a child similarly returns output and may trigger the parent's next run.
- Boundary reachability: `HarnessBuilder` and Service managed agents instantiate this run-stream path in standard supported deployment; e2e scripted-model child exercise covers real Service thread/result delivery, not just a README possibility.
- Why this is / is not agent-owned: removing the model choice leaves fixed capability dispatch, permission checks and storage, not task-specific behavior; runtime protection is not semantic ownership.
- Evidence: [run-stream model event loop](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-harness/a13n_harness/_run_stream.py#L1271-L1450), [parent-child Service e2e](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/e2e/service/test_subagents.py#L1-L60), [delegation source](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-harness/a13n_harness/toolsets/delegation.py#L100-L157).
- Basis: structural, corroborated by repository-provided deterministic e2e/test setup; no live inference efficacy measurement.
- Confidence: high for selectable model/tool continuation paths.
- Caveats: an external application owns its higher-level goals, credentials, persistence contract and operator policies; scripted-model tests prove wiring, not autonomous provider reliability.

## S2 — Coordination

- State: —
- Function: no bounded path is established that detects and attenuates a **specific inter-S1 interference/oscillation** among two distinct autonomous work cells.
- Disturbance / variety regulated: duplicate/concurrent inputs on the same thread and child lifecycle bookkeeping are real technical disturbances, but not in themselves conflict between autonomous S1 units at this boundary.
- Decisive decision or feedback right: Service worker/inbox lock deterministically serializes one thread; parent model chooses tasks or child steering messages, without an evidenced corrective inter-S1 collision rule.
- Decision owner: Service runtime for thread serialization; configured parent for assignment; neither is credited with an S2-specific mutual-adjustment choice from the observed paths.
- Supporting / enforcement mechanisms: advisory locks, FIFO inbox ordering, child IDs, result routing, context inheritance and `SubagentOperator` status calls.
- Closure path: worker contention → single-thread run ownership/FIFO → subsequent messages in order, or child result → parent continuation; neither demonstrates an inter-S1 coordination adjustment caused by conflict between separate operating cells.
- Why this is / is not agent-owned: delegation, queues, parent-child messages and serialized updates protect a run and carry outputs, but the cited tests do not supply an inter-cell interference witness plus corrective feedback.
- Evidence: [contention e2e two workers, one thread](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/e2e/service/test_contention.py#L1-L77), [async subagent calls](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-harness/a13n_harness/toolsets/subagents.py#L74-L201), [Service child operator](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/subagents.py#L92-L270).
- Basis: structural negative with explicit interference test.
- Confidence: medium-high in reviewed supported modes.
- Caveats: a consumer can design application-specific multi-agent coordination on Foundation, but that composition is not automatically shipped as an S2 relation.

### Absence scope

- Surfaces inspected: Harness inline/async delegation toolsets, Service ChildRuns operator, concurrent message/thread tests, supported subagent and state documentation.
- Plausible first-party paths checked: multiple child runs, parent steering/wait/cancel, shared borrowed environment, concurrent workers, inbox conflict/FIFO and child-result delivery.
- Why no material first-party path remains: the concrete contention witness is among claimants to **one** thread, while distinct children are delegated and reported without a cited inter-child conflict/oscillation and S2-specific corrective adjustment. Generic extensibility cannot fill that missing relation.

## S3 — Inside-and-now control

- State: —
- Function: whole-system current control across independently operating S1 commitments/resources is not demonstrated as a discretionary management loop.
- Disturbance / variety regulated: individual run interruption, exhausted usage, pending approval, worker handoff, child completion and queue contention; these are bounded run controls.
- Decisive decision or feedback right: parent model can select, query or steer its own children; operator sets policies, budgets and Service resources. Neither path establishes a current **whole-deployment** view plus actual cross-cell resource/prioritization intervention.
- Decision owner: parent model for its selected task/child; host/admin for resource policy; deterministic Service for concurrency and run enforcement. No separately qualified S3 owner at the declared deployment recursion.
- Supporting / enforcement mechanisms: child `info`/`wait`/`steer`/`cancel`, worker claims, retry/recovery and usage limits, Console run monitoring and permission review.
- Closure path: local action/stop and child result return to the invoking session; they do not evidence a whole-system manager rebalancing competing active S1 commitments and returning changed constraints.
- Why this is / is not agent-owned: a model's task delegation and lifecycle commands may be meaningful local S1 choices without constituting parent S3; a scheduler or kill switch alone cannot own resource bargaining.
- Evidence: [async child tools](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-harness/a13n_harness/toolsets/subagents.py#L120-L202), [Service process contention](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/e2e/service/test_contention.py#L1-L77), [run monitoring semantics](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/docs/a13n-service/agents-and-runs.md#L380-L389).
- Basis: structural negative.
- Confidence: medium-high for shipped current-control surfaces.
- Caveats: a specific client built atop these APIs could establish a new higher-recursion S3; it was not present as a first-party selected management system here.

### Absence scope

- Surfaces inspected: Service managed execution, permissions, async subagents, worker ownership and monitoring routes; Harness run lifecycle and Service e2e.
- Plausible first-party paths checked: parent/child status and steering, admin Console, concurrency controls, usage policies, run recovery and resource claims.
- Why no material first-party path remains: available decisions stop/continue one run or task tree and enforce configured limits; no first-party agent or parent-loop evidence integrates a whole-service current state, competing S1 resource tradeoff and enacted corrective allocation.

## S3* — Complementary audit

- State: A
- Function: independently sample retained execution reality to challenge normal agent success/quality claims and supply findings for corrective oversight.
- Disturbance / variety regulated: unsupported success claims, incorrect tool use, hidden recoveries, instruction/tool design issues and divergence between a target agent's reported answer and actual trace/span/tool evidence.
- Ordinary reporting path and claim: an operational target agent produces a run answer and ordinary status/results; those may be misleading or omit relevant failure.
- Claim being audited: the target agent's asserted task completion, tool-use correctness and answer quality against recorded actions and effects.
- Ordinary reporting path: target Run answer, status and normal tool-result messages forwarded to its caller and stored in the managed thread.
- Complementary access path: **separate Finding Agent** reads selected trace roots, raw spans, span content and the target's executed revision configuration via limited read APIs; analysis cannot target the Finding Agent itself. Its output is a cited structured finding, not a copy of the target's self-report.
- Independence boundary: Finding Agent executes as a distinct managed agent/revision, cannot target itself, obtains selected trace/spans directly from the Service trace backend and has no permission to edit target configuration.
- Decisive decision or feedback right: Finding Agent model chooses whether trace evidence warrants a diagnosis/finding, its category, limitations and citations; user reviews a finding and can explicitly send it to Composer for a proposed config revision.
- Decision owner: separately instantiated Finding Agent for model-owned audit judgment; user owns selecting analysis and accepting/configuring the downstream correction; Composer models a proposed change but cannot unilaterally publish it.
- Who acts on findings: workspace reviewer records a confirmation or rejection and, if useful, routes evidence to Composer, evaluates its proposed configuration and explicitly approves the target agent's new revision.
- Supporting / enforcement mechanisms: bounded trace selection, read-only endpoint allowlist, `POST /findings`, strict workspace/agent-revision verification, analysis history, assessment notes and explicit approval of configuration writes.
- Closure path: normal target run/answer → independently selected trace evidence → Finding Agent investigation and submitted diagnosis → saved reviewer assessment → selected finding to Composer → human-approved agent revision → later runs use corrected configuration. The optional workflow is real but not automatic for every run.
- Boundary reachability: Service ships `Finding Agent` preset, analysis routes/managed run and Console workflow; an ordinary authenticated user can select `Analyze traces` in an installed Service with trace backend. This is a first-party supported operation, not only an evaluator fixture.
- Why this is / is not agent-owned: the diagnosis is a separate model's discretionary comparison against complementary artifacts. Deterministic selection, filtering and validation merely constrain the audit; human review owns publication, not the Finding Agent's diagnostic judgment.
- Evidence: [Finding Agent tool rights](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/findings/preset.py#L5-L49), [separate-target guard and Finder selection](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/findings/analysis.py#L90-L120), [analysis run initiation](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/runs/findings/analysis.py#L215-L285), [diagnostic/feedback instructions](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/resources/agents/instructions.py#L25-L67), [human review and Composer workflow](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/docs/a13n-service/agents-and-runs.md#L430-L443).
- Basis: explicit supported mode, structurally traced into Service analysis dispatch and review path.
- Confidence: high for configured audit pathway, medium for effectiveness of diagnoses without live trace/provider tests.
- Caveats: depends on configured trace backend and operator invocation; trace retention/selection may be incomplete; independent access is relative to the *target* agent, not independent security verification of the Service itself. The finding does not automatically repair or publish a change.

## S4 — Outside-and-then intelligence

- State: —
- Function: no selected first-party agent loop takes external/future environmental changes, develops options and returns prospective adaptation into current service capability.
- Disturbance / variety regulated: internal run outcomes, tool errors, memory/context and historical diagnosis rather than modeled external opportunities/threats or future capability options.
- Decisive decision or feedback right: the user/application chooses new model/provider, agent settings, tools and deployments; Composer can propose configuration changes based on user prompts and findings, subject to human authorization.
- Decision owner: administrator/application for future deployment policy; target/Finding/Composer agents for their bounded operational or diagnostic tasks, not a demonstrated Service S4 capability.
- Supporting / enforcement mechanisms: model/provider catalog, memory, usage analytics, Findings, Composer config tools and revision publishing.
- Closure path: selected past-run finding can influence user-approved revision; it is internal quality remediation rather than an external-and-prospective S4–S3 adaptation conversation.
- Why this is / is not agent-owned: trace analysis is evidence about past operations, and ordinary user-directed editing is not an autonomous environmental intelligence function.
- Evidence: [Findings scope and change path](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/docs/a13n-service/agents-and-runs.md#L430-L443), [Composer deployment-owned guidance](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/resources/agents/instructions.py#L7-L26), [Harness capability catalog](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/docs/a13n-harness/capabilities.md).
- Basis: structural negative.
- Confidence: medium-high within selected standard distribution.
- Caveats: a user can ask a general-purpose agent to research the environment, but that task does not itself install a recurring whole-system adaptation loop.

### Absence scope

- Surfaces inspected: Service Insights/Findings/Composer, model and capability configuration, Harness memory/context, managed agent revision and schedule descriptions.
- Plausible first-party paths checked: diagnosis of repeated issues, instruction improvement, user-triggered configuration changes, model switching, memory and future schedule runs.
- Why no material first-party path remains: all evidenced selected loops handle internal quality, local task planning or externally initiated configuration; none joins systematic prospective outside sensing to a governed S3-capability response.

## S5 — Policy and identity

- State: —
- Function: no first-party, returned **identity/ultimate-policy** deliberation loop is established for the deployed autonomous agent organization.
- Disturbance / variety regulated: ordinary tool permissions, workspace identity, run access, model credentials and agent revision authority; these are substantial controls but not evidenced resolution of S3–S4 identity tensions.
- Decisive decision or feedback right: human workspace administrators and the embedding application set identity, capabilities, service and security policy; a user approves ordinary Composer edits. No agent has legitimate ultimate identity authority in the reviewed standard operating contract.
- Decision owner: human/application outside the credited autonomous decision owner; runtime enforces registered constraints and authorization.
- Supporting / enforcement mechanisms: organization/workspace IAM, permission policies, agent defaults/revisions, audit trails, approval decisions, worker validation and config save.
- Closure path: operator settings bind subsequent runs and authorizations, but no specifically identity-level issue is routed to a legitimate parent S5 deliberation and returned as governing resolution.
- Why this is / is not agent-owned: credentials, prompt text, a predefined permission review and admin approval are not themselves S5.
- Evidence: [permission review semantics](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/docs/a13n-service/agents-and-runs.md#L80-L98), [built-in Composer limited authority](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/packages/a13n-service/a13n_service/resources/agents/instructions.py#L7-L26), [Service agent configuration](https://github.com/converge-ai-labs/agent-foundation/blob/19bef266e239bf42adf258159b6f52195daa4d01/docs/a13n-service/agents-and-runs.md#L24-L40).
- Basis: structural negative.
- Confidence: medium-high for ordinary shipped modes.
- Caveats: an operating organization using Service may have external human governance, but repository presence of IAM and permission workflows is insufficient evidence of an S5 parent-mode closure.

### Absence scope

- Surfaces inspected: agent configuration/revisions, permission/approval flows, workspace administration, Service built-in agents and selected Findings → Composer path.
- Plausible first-party paths checked: admin policy, approval of tool/config writes, identity/organization settings, runtime safety instructions and higher-authority delegation.
- Why no material first-party path remains: these enforce or update normal operating constraints without a defined identity-level tension, legitimate deliberative owner and feedback return specifically closing S5 at the assessed recursion.

## Recursion

An embedded Harness agent or a Service-managed child has its own task environment, history and model-backed decisions and can be an S1 at a narrower recursion. The managed Service provides run infrastructure; not every worker, tool, session or child becomes a viable organization with independent S2–S5. The separately instantiated Finding Agent is a complementary audit path against target S1 claims when the selected deployment uses Findings; it is not an automatic auditor in ordinary embedded Harness use. External applications and organizational administrators may realize their own higher recursion, which is not imported by default.

## Variety and escalation

- Local variety: model chooses tool calls and responses; child models can specialize within declared definitions and inherited constraints.
- Attenuation/enforcement: permissions, policy review, usage/recovery limits, selected environment providers, thread serialization, bounded trace selection and saved state.
- Amplification: selectable tools/capabilities, retrieved evidence, model choice, child agents and per-run steering; these do not automatically establish distinct metasystem functions.
- Escalation: an approval/deferred request can reach a person, run failures are exposed in Service, and selected audit findings can reach human review and Composer. These are channels, not automatically S3/S4/S5 or algedonic closure.
- Homeostasis/recursion limit: no supported end-to-end whole-system S3–S4–S5 loop was established; the included finding is agent-owned S1 with a selected complementary S3* audit mode, not a claim that the platform is empirically viable.

## Evidence gaps

- First-party source SHA checked. No live paid provider, external MCP service, Docker-managed Service, production trace backend or browser Console was operated; semantic outcomes and diagnosis quality are not performance-verified.
- Findings-to-revision closure is an explicit first-party operator workflow, but no full production correction trial was run. The observed link is source plus documentation, not a measurement of successful repairs.
- The S3* positive is mode-qualified: a user-selected trace analysis of **another** Agent using retained traces. A basic embedded Harness run without Service trace backend/Finding Agent has no such audit.
- The negative S2/S3/S4/S5 states bound the standard distribution and its inspected supported modes. Future custom applications or integrations can change the system boundary; no unresolved first-party positive path was found that justifies `?` in this review.
- Native deterministic `a13n-harness` subagent operator target: `uv run --locked --package a13n-harness --group test python -m pytest packages/a13n-harness/tests/test_subagent_operator.py -q` passed **7/7** (non-fatal pytest configuration/deprecation warnings). The Service Finding target could not collect: `uv run --locked --package a13n-service --with pytest python -m pytest packages/a13n-service/tests/test_findings.py -q` stopped while importing its `conftest.py` because optional `testcontainers` was absent. No Finding test pass is claimed; the source-confirmed analysis path is not a live E2E validation.
