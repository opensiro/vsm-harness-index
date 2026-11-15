---
harness_id: lemma
project_name: Lemma
repository: https://github.com/lemma-work/lemma-platform
review_ref: 56dc83dd583821be83e01561b00484ac9efcf454
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Lemma

## Review boundary

- System in focus: One deployed Lemma pod provisioned for a team outcome, using the repository's standard first-party in-process agent and workflow runtime.
- Purpose and identity: Run the configured team work and recurrent service in a scoped pod, preserving a durable owner-directed mandate and observable tool/approval paths.
- Relevant environment: Team users and owners, external requests and recurring tasks, pod work records, connected tools, configured model inference and agent hosts.
- Standard-distribution boundary: FastAPI/worker, in-process model harness, authenticated pod controls, workflows, memory and packaged tools. Optional Agent Host is a separate execution mode; its external agent internals do not supply the attributed owner.
- Credited operating / distribution surfaces: Model/turn runtime, authorized Pod tools, post-run memory pass, workflow and schedule state, pod roster/outcome and current operator surfaces.
- Adjacent first-party surfaces excluded from ownership: Upstream CI and development, hosted service operations not evidenced in this tree, the downstream team beyond the pod, and externally installed Agent Host model/tool loops.
- First-party operating / deployment modes considered: Local/Desktop and self-hosted compose with the built-in model-backed runtime; owner-configured pod outcomes and recurring work. Agent Host only as explicitly scoped integration.
- Recursion level: One pod with named/default agent S1 operations. Higher organization-wide management and other pods are adjacent.
- Reviewed revision: 56dc83dd583821be83e01561b00484ac9efcf454.
- Observation date: 2026-11-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Lemma provisions a durable team pod with agent definitions, app data, named users/roles, functions and workflow graphs. API and worker share persisted work claims and results. For the in-process mode, Lemma itself streams provider model requests, invokes authorized tools and maintains later model history across tool calls, pauses and resumed runs. Workflow graph nodes can invoke agents and functions or branch on a typed model answer. A separate host mode delegates agent execution to a paired runtime. Local pods have model-backed post-turn memory and de-duplicated worker delivery for committed facts.

Evidence: [ARCHITECTURE.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/ARCHITECTURE.md), [agent.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/agent.md), [workflow.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/workflow.md), [pod.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/pod.md), [harness.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/infrastructure/harness/lemma/harness.py).

## Operational model

Named/default agents use the built-in loop to perform explicit team work through configured tools. Durable work events return artifacts and results to conversations or workflow runs. Owner roles determine pod objectives, resource permissions and approval authority. Post-turn memory jobs share the pod knowledge index, which feeds later operational context.

## S1 — Operations

- State: A
- Function: Perform configured pod work from requests and scheduled or workflow stimuli.
- Disturbance / variety regulated: New requests and current tool/data outcomes call for varying choices about the next step.
- Decisive decision or feedback right: Choose and evaluate the subsequent tool/action or final response in the operating loop.
- Decision owner: First-party model-backed in-process agent.
- Supporting / enforcement mechanisms: AgentTurn work claims, provider port, authorized tool contexts, durable logs and pause/resume.
- Closure path: Tool calls, results and interactions enter the replayable model history and guide later operations.
- Boundary reachability: The standard server supplies the in-process harness, not just a call to an independent coding CLI. The model provider supplies inference.
- Why this is / is not agent-owned: The agent determines task actions from the context, while the worker and tool gates execute and persist them.
- Evidence: [agent.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/agent.md), [harness.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/infrastructure/harness/lemma/harness.py), [node_loop.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/infrastructure/harness/lemma/node_loop.py).
- Basis: structural
- Confidence: high
- Caveats: The separate paired Agent Host mode is not the basis for this A.

## S2 — Coordination

- State: C
- Function: Attenuate interference when different pod agents retain compatible work knowledge through the same shared index.
- Disturbance / variety regulated: Simultaneous post-turn keepers for distinct pod agents could overwrite or act on a stale shared index.
- Decisive decision or feedback right: Coordinate application of memory changes in a shared pod namespace and expose the resulting context to later agents.
- Decision owner: Shipped worker's constructor-specified per-pod serialization policy. No autonomous ordering discretion is established.
- Supporting / enforcement mechanisms: Completion outbox, one work item per run, shared per-pod concurrency key, bounded updates and cache invalidation.
- Closure path: Serial keepers read/update scoped notes and pointers. Their committed notes invalidate affected brief material and the next runs load the shared up-to-date index.
- Boundary reachability: The packaged in-process MEMORY capability has a post-turn pass with a concurrency key deliberately shared by pod agents.
- Why this is / is not agent-owned: The key and serialized order are provided by the code. Learning models decide what to retain inside that order, without owning the scheduling choice.
- Distinct S1 units: Different independently invoked named/default agents doing assigned pod work and retaining relevant outcomes.
- Inter-S1 disturbance: They share /memory/AGENTS.md. Overlapping updates from those agents can interfere, including superseding a pointer that another keeper had just committed.
- Attenuating coordination relation: One post-turn learning job per pod can update the common index at a time; the policy is specific to this shared operational knowledge path.
- Feedback into subsequent S1 behaviour: Committed updates invalidate affected entry caches and later agent briefs include the resolved shared index.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The path targets competing updates to the same pod-shared evidence and returns the serialized knowledge to future operational units. It is narrower than generic workflow routing.
- Evidence: [agent-memory.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/docs/architecture/agent-memory.md), [run_followups.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/services/run_followups.py), [memory_pass.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/application/background/memory_pass.py), [agent.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/agent.md).
- Basis: structural
- Confidence: medium
- Caveats: C is bounded to the post-turn inter-agent memory path. The deterministic envelope has no installed autonomous coordination decision owner and does not cover every possible write path.

## S3 — Inside-and-now control

- State: ?
- Function: Examine pod-wide current regulation over concurrently active agent and workflow commitments.
- Disturbance / variety regulated: A pod's distinct activities can consume shared capacity or continue after priorities change.
- Decisive decision or feedback right: Select pod-wide resource allocation, commitments and corrective interventions using a whole-pod current operating view.
- Decision owner: Unresolved for the whole pod boundary. Workflow operators and parent agents own decisions within individual runs or child groups.
- Supporting / enforcement mechanisms: Run history, stop/retry, queued work admission, subordinate conversation status and pod standing API.
- Closure path: The workflow engine cancels active waits and propagates cancellation for an identified run. A pod-wide synthesis-to-intervention route across its other independent runs was not established.
- Why this is / is not agent-owned: Scoped supervision and state reads are material. Evidence does not support a positive whole-pod owner or bounded absence of that combined supported path.
- Evidence: [workflow.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/workflow.md), [engine.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/workflow/execution/engine.py), [subagent_service.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/services/subagent_service.py), [outcome_controller.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/datastore/api/controllers/outcome_controller.py).
- Basis: structural
- Confidence: medium
- Caveats: Unresolved path: whether the default pod agent or an owner has one supported pod-wide active-work decision loop over multiple independent workflows and schedules.

## S3* — Complementary audit

- State: —
- Function: Test whether the shipped pod audits ongoing management claims through a separate observation and corrective channel.
- Disturbance / variety regulated: Routine reports may diverge from actual pod operations or measured service.
- Decisive decision or feedback right: Independently adjudicate the management claim from raw operation evidence and return a correction.
- Decision owner: No first-party auditor with a regulating return at the assessed boundary was established.
- Supporting / enforcement mechanisms: Fenced execution steps, ordinary run logs, outcome standing view, separate weekly table-measure job and general child agents.
- Closure path: Pod measures enter standing/history as readings; there is no built-in judgment and returned organizational correction tied to an audit of management reports.
- Why this is / is not agent-owned: The database reading is complementary access to a measure. The observed path is ordinary outcome monitoring, without evidence of a shipped audit adjudicator that acts on a discrepancy.
- Evidence: [agent.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/agent.md), [subagent_service.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/services/subagent_service.py), [outcome_controller.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/datastore/api/controllers/outcome_controller.py), [outcome_week_work.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/datastore/events/outcome_week_work.py).
- Basis: structural
- Confidence: medium
- Caveats: A user-authored check could use the measured data. Generic child invocation and records are not a supplied audit loop.

### Absence scope

- Surfaces inspected: Run and workflow history, direct standing measure, independently scheduled measure sampling and subordinate session tools.
- Plausible first-party paths checked: Report versus saved history, independent raw-table observation, weekly measurements and possible verifier-role composition.
- Why no material first-party path remains: Readings are stored/displayed without a built-in comparison to a management report, independent adjudication, or resulting corrective operation. Child agency is general-purpose.

## S4 — Outside-and-then intelligence

- State: P
- Function: Turn recurring external team demand into a confirmed persistent capability for future work.
- Disturbance / variety regulated: Repeated requests or a manually maintained list reveal work the pod could take on on a continuing basis.
- Decisive decision or feedback right: Confirm whether the pod should adopt a new standing operational plan and the cadence, trigger or scheduled capability that supports it.
- Decision owner: Pod owner or legitimate responsible team member decides whether the proposed future change is adopted.
- Supporting / enforcement mechanisms: Default-agent recurring-work proposal, bundled setup skill, editable plan and persisted schedule/trigger and workflow definitions.
- Closure path: Accepted responsibilities lead to a durable plan and authorized recurring task/schedule. The worker later starts the configured work on matching occurrences.
- Boundary reachability: The default installed agent is instructed to spot recurring work and propose a durable responsibility, and the bundled setup and runtime support act on the owner’s decision.
- Why this is / is not agent-owned: A background model can choose what notes to retain. The credited binding future work/capability decision here is the owner's, with verified operational setup after acceptance.
- External distinction: Actual repeated team requests and manually tracked work observed across interactions.
- Future / prospective distinction: Whether to service recurring work beyond the current request, with future invocation and explicit result type.
- Adaptation option generated: A new planned responsibility and a matching first-party schedule, trigger or workflow configuration.
- Path back into current capability / S3: Owner approval returns through setup into persisted work that the ordinary job runtime executes on later inputs.
- Evidence: [teammate.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/prompts/teammate.md), [SKILL.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-skills/lemma-setup/SKILL.md), [schedules-and-triggers.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-skills/lemma-builder/references/schedules-and-triggers.md), [agent-memory.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/docs/architecture/agent-memory.md), [ARCHITECTURE.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/ARCHITECTURE.md).
- Basis: structural
- Confidence: medium
- Caveats: Unattended retention of conventions can influence future prompts. It is not by itself evidence of autonomous choice of a new durable operating strategy.

## S5 — Policy and identity

- State: P
- Function: Set what the pod is for, what standing outcome it owns, and the durable authority that governs its actors.
- Disturbance / variety regulated: A series of tasks or proposed recurring responsibility may conflict with the established team mission and delegated authority.
- Decisive decision or feedback right: Choose or replace the pod's enduring responsibility, outcome/measure and authority envelope.
- Decision owner: Legitimate pod owner or authorized parent steward. The agent can configure a measure in the delegated setup path after authority is provided.
- Supporting / enforcement mechanisms: Pod role/permission claims, outcome service with readback and policy validation, tool capability, config events and runtime-brief projection.
- Closure path: The owner's returned policy persists in the Pod, appears in later runtime brief and plan reference, and governs future work and permission/timing boundaries.
- Boundary reachability: The same operating deployment has the outcome and permission APIs and reads that configured organizational purpose directly into each agent's context.
- Why this is / is not agent-owned: The base teammate role proposes a new responsibility and waits for a positive answer. A grant-gated setter is a way to return that decision and its validated measure, without evidence that the installed agent may choose a new ultimate purpose independently.
- Identity / ultimate-policy issue: What work the pod takes responsibility for over time and which authority the team delegates to actors in that pod.
- Ultimate authority in each claimed mode: Legitimate owner or authorized steward. Governing pod decisions stay at the parent recursion in the credited mode.
- Return-to-operation path: Outcome/permissions updated and validated through the first-party path; later runtime briefs, plans and grant decisions use the saved outcome.
- Evidence: [pod.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/docs/modules/pod.md), [pod_outcome_tool.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/infrastructure/tools/pod/pod_outcome_tool.py), [teammate.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/prompts/teammate.md), [agent_brief.py](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/lemma-backend/app/modules/agent/services/context_brief/agent_brief.py), [sharing-and-permissions.md](https://github.com/lemma-work/lemma-platform/blob/56dc83dd583821be83e01561b00484ac9efcf454/docs/product/journeys/sharing-and-permissions.md).
- Basis: structural
- Confidence: medium
- Caveats: Human approval of one tool call is not this claim. The evidence concerns the durable mission and the way it enters subsequent work.

## Distributed OSS parent arrangement

The distributed Lemma repository maintainers are outside the assessed pod recursion. Local authorized stewards decide what the pod owns and what access it can use.

## Self-hosted and non-human modes

The in-process agent and worker are supplied by the repository. Optional Agent Host is supported separately and is not required for the first-party task loop cited here.

## Recursion

A pod is one Team-work recursion that can contain multiple independent agent roles and workflow runs. Parent/child sessions exist but their relative control does not prove management of the whole pod.

## Variety and escalation

Rate limits, leases and scoped grants bound execution. Operator decisions can return through persisted approvals. An audit-grade source read or transfer of delegated authority is not inferred from an event log.

## Evidence gaps

No provider, self-hosted instance, subgroup workload or unattended delivery was run. The pod-wide present-control loop remains unresolved despite concrete per-run intervention and pod-level read APIs. Workable in-process and Agent Host arrangements should not be pooled in a later comparison without naming the selected boundary.
