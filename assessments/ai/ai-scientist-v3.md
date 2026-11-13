---
harness_id: ai-scientist-v3
project_name: AI-Scientist-v3
repository: https://github.com/SakanaAI/AI-Scientist-v3
review_ref: df8313889a004f8a44a472e19a833cd547bb828a
reviewed_at: 2026-11-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AI-Scientist-v3

## Review boundary

- System in focus: The first-party autonomous research campaign and paper generation runtime in SakanaAI/AI-Scientist-v3, including agent-driven idea generation and experimentation, parallel campaign workers, manuscript generation and the separate paper evidence-audit stage.
- Purpose and identity: Produce and substantiate a research result for a researcher-specified scientific task, using executable experiments and a manuscript.
- Relevant environment: Researcher-supplied task and rubric, experimental code/data, scientific references, compute/GPU capacity, execution errors, quantitative results, manuscript artifacts and external model providers.
- Standard-distribution boundary: Pinned repository source and supported entry scripts/configurations. External LLM providers, scientific databases, container/OS/GPU substrate and investigator-supplied research mandate remain dependencies or parent inputs.
- Credited operating / distribution surfaces: src/investigation/campaign_loop.py, idea_generation.py, parallel_helpers.py, src/scripts/run.sh and paper.sh, src/orchestrator/paper_evidence_audit.py, paper review prompts and shipped supported manuscript repair paths.
- Adjacent first-party surfaces excluded from ownership: Repository contribution governance, CI, tests as executors in their own right, public demo claims, externally hosted research tasks and model providers. The final scientific evaluator is not treated as independent organizational audit merely because it scores experiments.
- First-party operating / deployment modes considered: Standard idea/experiment campaign; supported multi-worker campaign and optional pruning; normal manuscript evidence-audit and repair stage. Host/container configuration is supporting infrastructure.
- Recursion level: One autonomous scientific research campaign and its manuscript-production work as system-in-focus; workers are subordinate research execution units, not independently viable research organizations merely due to parallel processes.
- Reviewed revision: df8313889a004f8a44a472e19a833cd547bb828a.
- Observation date: 2026-11-14.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The first-party investigation loop asks an agent to form and revise scientific ideas, executes experiment programs, records quantitative scores and failures, selects subsequent candidates and persists campaign state. Parallel helpers run separately scoped workers with cycle leases, optional per-round isolation and aggregation; the worker queue and GPU/build locks are predominantly deterministic supporting machinery. The manuscript stage creates paper artifacts and a distinct read-only agentic evidence-audit workspace. Audit verdicts and discrepancy feedback feed bounded repair rounds; exhaustion produces an incomplete-paper state rather than a fabricated success. Human researchers choose the task and research rubric; model providers and datasets remain environmental dependencies, not first-party autonomous governance.

Primary code: [campaign loop](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/campaign_loop.py), [parallel helpers](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/parallel_helpers.py), [paper pipeline](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/scripts/paper.sh), [paper evidence audit](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/orchestrator/paper_evidence_audit.py).

## Operational model

Operational output is an evidence-backed research candidate and manuscript or a recorded failed/incomplete campaign. Agent-driven experimental iterations are the relevant S1 activities. One campaign may use multiple worker processes, but dispatch, locks and shared files are not automatically an S2 or S3 decision owner. Audit findings can change subsequent authoring work. Researcher's choice of scientific topic is a parent input and not, without more, identity-level governance closure inside the assessed software organization.

## S1 — Operations

- State: A
- Function: Conduct an autonomous scientific experiment campaign that chooses and revises candidate research implementations.
- Disturbance / variety regulated: Uncertain hypothesis quality, changing experiment feedback, runtime errors, variable metrics and competing candidate designs.
- Decisive decision or feedback right: The research agent chooses ideas, modifications and further attempts after evaluating feedback within a task mandate.
- Decision owner: First-party invoked scientific research agent; the experiment executor and scoring code are enforcement/evidence mechanisms rather than the owner of idea generation.
- Supporting / enforcement mechanisms: Experiment runner, model tools, persisted campaign state, score/manifest files, worker processes, compute reservation and checkpoint/resume.
- Closure path: A selected idea is executed; metrics and failures are returned to the campaign loop; the agent changes the next experiment or selects the candidate to write up.
- Boundary reachability: Standard shipped campaign entry path invokes the idea-generation and experiment loop and persists outputs usable by later iterations.
- Why this is / is not agent-owned: Removing the agent retains execution and scoring but not adaptive scientific hypothesis selection or iterative source changes.
- Evidence: [campaign_loop.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/campaign_loop.py), [idea_generation.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/idea_generation.py), [main_entry.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/main_entry.py).
- Basis: structural
- Confidence: high
- Caveats: This is autonomy within a researcher-defined task. No live scientific performance or experiment replication was executed for this assessment.

## S2 — Coordination

- State: —
- Function: Attenuate operational disturbance between distinct coequal autonomous research S1 units.
- Disturbance / variety regulated: Parallel workers may race over shared results, GPU resources or duplicate investigative effort; this is a potential concrete interference to check, not proof of an agent-owned coordination function.
- Decisive decision or feedback right: No shipped S2-specific discretionary coordinator and returned inter-S1 corrective decision was established in the campaign boundary.
- Decision owner: Deterministic worker scheduler, cycle lease and host build-lock code; no independently evidenced S2-specific agent owner.
- Supporting / enforcement mechanisms: Thread locks, worker leases, per-round results isolation, shared-memory files and advisory file lock.
- Closure path: Scheduling and locking avoid runtime collisions but do not show an autonomous coordination decision that redirects mutually interfering S1 units.
- Why this is / is not agent-owned: A worker lease assigns execution slots without organizational discretion over relations between separate operations.
- Evidence: [parallel_helpers.py#L1619-L1754](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/parallel_helpers.py#L1619-L1754), [runtime_build_coordination.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/runtime_build_coordination.py).
- Basis: structural
- Confidence: medium
- Caveats: Cross-worker conclusions are exchanged; their relevance to research feedback does not establish a standalone organizational S2 without a function-specific conflict/authority witness.

### Absence scope

- Surfaces inspected: Investigation campaign loop, parallel helper worker queues, shared-memory isolation and host-wide runtime-build coordination.
- Plausible first-party paths checked: Dynamic one-cycle worker leasing, pruning rounds, GPU/build capacity locks, aggregation, shared conclusions and worker seed updates.
- Why no material first-party path remains: The inspected paths allocate and isolate work within one research campaign but do not expose the specialized agent-owned or constructible organizational right to resolve an inter-S1 disturbance with a returned coordination decision.

## S3 — Inside-and-now control

- State: —
- Function: Govern current whole-system research commitments and resource allocations on behalf of several operational units.
- Disturbance / variety regulated: CPU/GPU scarcity, failed workers and competing experiment candidates create operational control demands.
- Decisive decision or feedback right: No supported autonomous or parent-governed whole-system current-control decision distinct from campaign/task execution and fixed resource enforcement is established.
- Decision owner: Task configuration/researcher sets experiment budget; deterministic scheduler and pruning routines enforce it.
- Supporting / enforcement mechanisms: Worker count, max cycles, GPU pool selection, queue stop flags, score-based pruning and persisted campaign manifests.
- Closure path: Runtime budgeting changes how a single campaign proceeds, but an organizational whole-system current-control loop over multiple obligations is not evidenced.
- Why this is / is not agent-owned: Internal experiment selection and fixed budget enforcement are S1 work or infrastructure, not proof of S3 authority.
- Whole-system current view: No established S3 actor has a governed view of multiple independent ongoing research commitments beyond single-campaign scheduling.
- Current-control decision scope: No established independent S3 intervention right; the inspected scheduler may stop or assign cycles according to preselected rules.
- Evidence: [parallel_helpers.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/parallel_helpers.py), [campaign_loop.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/campaign_loop.py).
- Basis: structural
- Confidence: medium
- Caveats: A research administrator may choose global resources outside the reviewed software; do not borrow that parent system's operation without a returned first-party S3 path.

### Absence scope

- Surfaces inspected: Parallel executor, campaign state, resource locks, candidate scoring/pruning, user/researcher configuration and experiment pipeline.
- Plausible first-party paths checked: Multi-worker allocation, dynamic lease failure handling, GPU resource restrictions, cross-round selection and operator-defined run settings.
- Why no material first-party path remains: Those paths operate within the research task or enforce static capacity; they do not expose whole-system organizational current-control ownership or a first-party parent-return path.

## S3* — Complementary audit

- State: A
- Function: Complement routine scientific manuscript reporting with a sufficiently independent inspection of the supporting research evidence.
- Disturbance / variety regulated: A manuscript may contain unsupported claims or misrepresent data even if routine paper generation and output validation pass.
- Decisive decision or feedback right: A distinct evidence-audit agent judges research claims against assembled evidence, issuing pass/fail findings and requested corrections.
- Decision owner: Independent audit-stage agent; parsing, hash checking and loop gates are runtime enforcement rather than the owner of the substantive audit judgment.
- Supporting / enforcement mechanisms: Read-only audit workspace, claim/evidence packet, input SHA-256 verification, validation JSON, failure-code handling and bounded repair rounds.
- Closure path: Audit findings are merged into validation feedback; the paper runner revises the manuscript and reruns the audit or records incomplete status after exhaustion.
- Boundary reachability: Standard shipped paper.sh calls run_agentic_evidence_audit_gate, builds a read-only workspace and runs a separate auditor stage before accepting manuscript completion.
- Why this is / is not agent-owned: Removing the independent audit agent leaves ordinary paper checks but removes the substantive alternative judgment over primary research evidence.
- Claim being audited: Manuscript claims accurately and sufficiently reflect the experimental and source evidence.
- Ordinary reporting path: Researcher's/author agent's manuscript, metrics, validation output and final evaluation.
- Complementary access path: Separate read-only workspace and evidence-audit packet assembled from paper inputs and source evidence.
- Independence boundary: Fresh audit stage cannot simply edit manuscript files, and hashes detect changed inputs after audit preparation; it is not only the manuscript author's self-reported score.
- Who acts on findings: Paper runner converts findings into validation feedback and triggers repair or incomplete status, followed by audit rerun where allowed.
- Evidence: [paper.sh#L3510-L3610](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/scripts/paper.sh#L3510-L3610), [paper.sh#L4042-L4090](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/scripts/paper.sh#L4042-L4090), [paper_evidence_audit.py#L1819-L1879](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/orchestrator/paper_evidence_audit.py#L1819-L1879).
- Basis: structural
- Confidence: high
- Caveats: This is manuscript-evidence audit, not a certification of scientific correctness or of every upstream dataset and not an independent execution of the experiments in this assessment.

## S4 — Outside-and-then intelligence

- State: —
- Function: Detect external/future changes relevant to the research organization and adapt the harness's future operating capability in conversation with current S3.
- Disturbance / variety regulated: New scientific papers, research directions and method changes could motivate adaptation beyond the immediate research task.
- Decisive decision or feedback right: No shipped distinct adaptation-to-harness-capability loop was established; scientific idea generation belongs to the research S1 at this chosen recursion.
- Decision owner: Research agent owns task-level hypotheses; researcher/developers outside this runtime choose changes to its organizational mission/capability.
- Supporting / enforcement mechanisms: Literature retrieval, idea history, agent reflection and experiment results.
- Closure path: Research feedback changes individual experiment choices but no separately established external-and-prospective option is returned to whole-system present capability/S3.
- Why this is / is not agent-owned: Novel idea search is the declared S1 research service, not automatically S4 adaptation of the service provider's organization.
- External distinction: Available scientific literature and model/tool opportunities are task inputs, but no separate meta-organizational environmental sensing right was confirmed.
- Future / prospective distinction: Future scientific opportunities could matter, but the inspected loop optimizes a bounded research campaign.
- Adaptation option generated: None shown to update the harness's organizational capability at the declared recursion.
- Path back into current capability / S3: None established beyond task-level experiment iteration.
- Evidence: [idea_generation.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/idea_generation.py), [idea_retry_feedback.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/idea_retry_feedback.py), [campaign_loop.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/campaign_loop.py).
- Basis: structural
- Confidence: medium
- Caveats: Different system-in-focus selection could treat scientific exploration as environmental intelligence of a parent organization, which is not the assessed boundary.

### Absence scope

- Surfaces inspected: Research ideation, campaign feedback, experiment scoring, manuscript generation and external scientific-reference consumption.
- Plausible first-party paths checked: Literature novelty cues, idea retries, global memory, parallel worker shared conclusions, paper review and task-specific rubric updates.
- Why no material first-party path remains: These paths close scientific production and its quality checks; none closes a distinct prospective adaptation decision that changes the harness's future organization/current capability.

## S5 — Policy and identity

- State: —
- Function: Establish and revise ultimate identity-level scientific policy and resolve unresolved S3/S4 tension at the research-system recursion.
- Disturbance / variety regulated: A disputed research aim, forbidden methodology or changed institution-level mandate could require ultimate policy judgment.
- Decisive decision or feedback right: No first-party organizational constitutional/identity revision path was identified; researcher task/rubric selection is input configuration.
- Decision owner: Researcher/provider policy outside this assessed harness; no qualified internal S5 or closed first-party parent authority path established.
- Supporting / enforcement mechanisms: Task descriptions, paper-writing instructions, configuration, validation gates and externally set parameters.
- Closure path: Agent obeys existing parameters, but an identity-level dispute is not surfaced and closed through legitimate authority to govern later operation.
- Why this is / is not agent-owned: Merely changing task instructions or criteria is not legitimate ultimate-policy closure under the Profile.
- Identity / ultimate-policy issue: Mission-level dispute, changes to what science the organization is permitted to conduct or the constitutive rules of the research harness.
- Ultimate authority in each claimed mode: None demonstrated as an in-boundary S5 mode; external researcher/developer governance is not borrowed.
- Return-to-operation path: No explicit first-party identity-level escalation and authoritative policy return was established.
- Evidence: [main_entry.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/main_entry.py), [paper.sh](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/scripts/paper.sh), [paper_finalize.py](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/orchestrator/paper_finalize.py).
- Basis: structural
- Confidence: medium
- Caveats: Research mandate and ethics remain human/institutional concerns outside the inspected first-party organizational closure.

### Absence scope

- Surfaces inspected: Task/rubric configuration, agent instructions, campaign policy parameters, manuscript review gates and researcher-facing entry points.
- Plausible first-party paths checked: Researcher parameter changes, paper policy checks, final evaluator, agent escalation via failure/incomplete result and manual re-run with new instructions.
- Why no material first-party path remains: These regulate task compliance or operational success; no shipped identity-level proposal, legitimate ultimate authority decision and return-to-subsequent-operation path is evidenced.

## Distributed OSS parent arrangement

Project maintainers own upstream software releases but contributor governance and upstream PR merges are outside the assessed first-party research-campaign recursion. No organization-level parent S3/S4/S5 ownership is credited merely from OSS collaboration.

## Self-hosted and non-human modes

The runtime may execute on investigator-managed infrastructure and support parallel workers, but operator options set task budgets and research scope rather than establishing qualified additional S3/S4/S5 parent-governed modes. No separate non-human S5 authority is claimed.

## Recursion

One research campaign contains operational idea/experiment cycles, plus manuscript authoring and complementary audit. A process worker is not automatically a viable S1 suborganization; the paper auditor is a complementary access/feedback function, not a second research operating business.

## Variety and escalation

Experimental errors and unexpected scores are fed back to the research loop. Paper evidence findings return to author repair with limited retries; persistent failure returns an incomplete result to the researcher. No algedonic channel or separate S3/S4/S5 function is inferred solely from failure status.

## Evidence gaps

- Source-only assessment: no runtime execution, benchmark replication, or model provider reliability observation was performed.
- Cross-worker conclusions and shared-memory protocol could support more precise S2 investigation in a separately bounded multi-campaign organization, but no specific first-party S2 organizational owner/closure was established in this reviewed campaign.
- Future independent re-review could test the full read-only auditor invocation, result authenticity and paper repair return on one pinned run. These unexecuted tests do not invalidate the structural first-party S3* path.
