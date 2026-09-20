---
harness_id: xcientist
project_name: Xcientist
repository: https://github.com/OpenDFM/Xcientist
review_ref: 666eee404bc3cf59249dc8af0ab621cc3e804a49
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# Xcientist

## Review boundary

- System in focus: the first-party Xcientist research workflow at pinned revision `666eee404bc3cf59249dc8af0ab621cc3e804a49`, including the Survey, Idea, Experiment and Blog agent stacks, the prototype pipeline linking them, the vendored OpenHarness runtime actually used by the Experiment Agent, first-party reviewer/prefinish control code, and shared memory/configuration needed by those paths.
- Purpose and identity: turn a research topic into literature synthesis, a structured research proposal, executable controlled experiments with reviewed evidence, and downstream technical writing.
- Relevant environment: research topics; public literature and paper-graph retrieval; model-provider responses; local files and experiment workspaces; executable scientific code and datasets; generated metrics/figures/artifacts; external model/tool services.
- Standard-distribution boundary: code and resources shipped in `OpenDFM/Xcientist` at the reviewed revision. External model providers, external literature/search services, datasets, operating-system/container substrates and upstream behavior not actually vendored/wired into the repository remain environment/dependencies.
- Credited operating / distribution surfaces: `src/pipeline/`; `src/agents/survey_agent/`; `src/agents/idea_agent/`; `src/agents/experiment_agent/`; `src/agents/blog_agent/`; `src/harness/`; shared `src/memory/` and runtime configuration where those are used by the shipped workflow.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests as such, project-page/paper claims not backed by the pinned runtime, cache/build assets, and upstream OpenHarness semantics not reachable through Xcientist's vendored/integrated experiment path.
- First-party operating / deployment modes considered: individual Survey/Idea/Experiment/Blog CLI runs and the shipped prototype `Survey -> Idea -> Experiment -> Blog` pipeline; Experiment Agent code/science phases with reviewer/prefinish repair loops.
- Recursion level: one Xcientist research run as the system-in-focus. Experiment workers and the Survey/Idea/Blog stacks are internal operational/adaptive actors; external providers and the human supplying the topic are environment/Parent unless a function-specific parent loop is established.
- Reviewed revision: `666eee404bc3cf59249dc8af0ab621cc3e804a49`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Xcientist ships four research-facing agent stacks. The Survey Agent collects and clusters papers; the Idea Agent turns a topic or seed into a proposal using survey-grounded retrieval, graph-backed references and Memory-Guided MCTS; the Experiment Agent prepares a project, builds and executes controlled scientific conditions, and materializes reviewed evidence; the Blog Agent consumes experiment artifacts to produce a technical article. The repository also ships a prototype pipeline that passes Survey output to Idea, the resulting `idea_result.json` into Experiment, and experiment output into Blog.

The Experiment Agent has the strongest explicit control structure. A deterministic `MasterAgent` runs fixed code and science phases and only converges when phase reviewer reports are `PASS`, complete and ready. Inside each phase, worker outputs are subjected to deterministic hooks and separate read-only agent reviewers. Reviewer failures carry concrete `required_fix` instructions back to the same worker session; finalization verifies evidence lineage before publishing final ablation artifacts.

## Operational model

The operational transformation is executable scientific work: an agent receives a research proposal/current workspace, writes or changes code and experiment assets, runs bounded conditions, observes outputs, repairs failures and produces evidence-bearing results. The Survey/Idea path is prospective rather than merely historical memory: it samples external literature, synthesizes distinctions, generates a proposal and feeds that proposal into the Experiment Agent. Reviewers are separate read-only agent invocations with explicit audit scopes and blocking feedback; the deterministic master transports and enforces their decisions but does not itself own broad current-control discretion.

## S1 — Operations

- State: A
- Function: autonomously perform environment-facing research work by constructing and executing an experiment project and iterating from observed execution/review feedback.
- Disturbance / variety regulated: changing research proposals, incomplete project state, code/runtime failures, scientific-condition outcomes, artifacts and reviewer findings requiring context-sensitive work.
- Decisive decision or feedback right: choose concrete code/project actions and repairs needed to satisfy a work-unit/phase contract and produce executable scientific artifacts.
- Decision owner: the active first-party Experiment Agent worker/planner agent sessions.
- Supporting / enforcement mechanisms: phase runner, workspace/manifests, deterministic hooks, execution tools, phase contracts, artifact ledger and fixed master sequencing.
- Closure path: proposal/work-unit context -> agent chooses project/code action -> runtime executes or writes against the workspace -> execution/review evidence returns -> agent revises or completes the work unit.
- Boundary reachability: the Experiment Agent and its vendored harness are a documented shipped Xcientist CLI/pipeline surface, not a development-only example.
- Why this is / is not agent-owned: deterministic hooks and the master can block or transport state, but the context-sensitive scientific implementation/repair choice remains agent-owned.
- Evidence: [`README.md`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/README.md), [`src/agents/experiment_agent/README.md`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/README.md), [`src/agents/experiment_agent/runtime/phase_runner.py`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/runtime/phase_runner.py).
- Basis: structural
- Confidence: high
- Caveats: external model inference and external scientific/data services remain dependencies; credit is for Xcientist's first-party operational loop and closure.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination path is established at the reviewed recursion.
- Disturbance / variety regulated: multiple stacks/workers exist, but no specific inter-S1 interference, conflict or oscillation is identified and attenuated by a first-party coordination relation.
- Decisive decision or feedback right: no S2-specific discretionary coordination decision is established.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: sequential pipeline handoffs, planner-to-worker delegation, phase ordering, manifests and shared workspace artifacts.
- Closure path: these surfaces sequence/delegate work but do not close an interference -> coordination response -> changed subsequent S1 behaviour loop.
- Why this is / is not agent-owned: worker/reviewer plurality and pipeline topology are not themselves evidence of S2.
- Evidence: [`README.md`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/README.md), [`src/agents/experiment_agent/agents/master/entry.py`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/agents/master/entry.py).
- Basis: structural
- Confidence: high
- Caveats: later versions could add resource/conflict regulation among parallel research units; that is not credited at this frozen revision.

### Absence scope

- Surfaces inspected: top-level pipeline, four agent stacks, Experiment Agent master/phase runner, reviewer/hook architecture and shared workspace/manifests.
- Plausible first-party paths checked: multi-agent stack plurality, planner/worker delegation, shared experiment workspace, sequential code/science phases and reviewer routing.
- Why no material first-party path remains: the strongest paths are delegation, validation and sequential handoff; none identifies a cross-S1 disturbance and an attenuation relation that feeds back into the affected S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no agent-owned whole-system current-control function is established at the reviewed recursion.
- Disturbance / variety regulated: phase readiness, incomplete evidence and failed checks are regulated, but through fixed rules/gates rather than discretionary whole-system current control over shared commitments/resources/priorities.
- Decisive decision or feedback right: the master computes `RUN_CODE`, `RUN_SCIENCE` or `CONVERGED` from fixed phase status conditions; no autonomous actor is shown revising organization-wide current commitments or priorities from a whole-system view.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: deterministic `MasterAgent`, phase reports, readiness flags, blocking issues and fixed code-then-science ordering.
- Closure path: deterministic phase state -> fixed gate decision -> run/stop/advance; this is lifecycle enforcement, not a discretionary S3 control conversation.
- Why this is / is not agent-owned: removing the master leaves no phase enforcement, but the organizational choice is encoded in fixed logic rather than owned by an autonomous agent.
- Evidence: [`src/agents/experiment_agent/agents/master/entry.py`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/agents/master/entry.py).
- Basis: structural
- Confidence: high
- Caveats: this negative state does not deny that deterministic gating is operationally useful; it separates enforcement from S3 decision ownership.

### Absence scope

- Surfaces inspected: master orchestration, phase reports/readiness, worker/planner roles, pipeline ordering and reviewer gates.
- Plausible first-party paths checked: `MasterAgent` as supervisor, phase planner agents, reviewer-blocked progression and final convergence logic.
- Why no material first-party path remains: planner agents own local phase work, reviewers own audit judgments, while the only whole-run phase-control right is fixed deterministic logic. No autonomous whole-system current-control owner is established.

## S3* — Complementary audit

- State: A
- Function: independently challenge ordinary Experiment Agent work claims before phase completion and return blocking findings into corrective execution.
- Disturbance / variety regulated: semantically wrong but superficially executable code, idea/protocol mismatch, scientific-invariant violations, weak integration evidence, reproducibility gaps and stale/unclean implementation paths.
- Decisive decision or feedback right: issue an independent `PASS`/`FAIL` judgment with blocking issues and required fixes after reading work artifacts and deterministic-hook evidence.
- Decision owner: separate first-party read-only reviewer agents selected by reviewer role (`idea_alignment`, `implementation_correctness`, `scientific_invariants`, `protocol_semantics`, `integration_smoke`, `reproducibility`, `code_cleanliness`, with analogous science review paths).
- Supporting / enforcement mechanisms: deterministic hooks, review schemas, checked-artifact capture, immutable attempt reports, prefinish contracts and phase gate enforcement.
- Closure path: worker claims completion -> deterministic evidence is materialized -> separate read-only reviewer inspects independent artifact/context surface -> `FAIL` findings include `required_fix` -> same worker session receives the fix request and revises -> reviewer/gate is rerun before completion.
- Boundary reachability: reviewers and prefinish hooks are built into the shipped Experiment Agent phase runner and are required for phase completion, not benchmark-only code.
- Why this is / is not agent-owned: hooks enforce invariant checks, but the non-formal semantic review judgment is made by a distinct reviewer agent; the phase runner transports that judgment back to the worker.
- Claim being audited: that the current experiment work unit correctly implements the idea/protocol and is sufficiently integrated/reproducible to advance.
- Ordinary reporting path: worker final report plus normal execution/hook outputs.
- Complementary access path: reviewer receives read-only access to the idea, shared review context, hook findings, worker report and relevant project artifacts and is instructed to inspect them independently.
- Independence boundary: reviewer is a separate read-only agent invocation with a dedicated review role and cannot repair files; the audited worker owns implementation.
- Who acts on findings: the Experiment Agent worker session, under phase-runner enforcement.
- Evidence: [`src/agents/experiment_agent/agents/code/reviewer.py`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/agents/code/reviewer.py), [`src/agents/experiment_agent/runtime/phase_runner.py`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/runtime/phase_runner.py), [`src/agents/experiment_agent/README.md`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/README.md).
- Basis: structural
- Confidence: high
- Caveats: the classification credits the explicit Experiment Agent reviewer/repair closure; it does not generalize every Blog/Survey quality check into S3*.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense external/future-relevant scientific distinctions, develop a research option, and return the selected option into present experimentation.
- Disturbance / variety regulated: changing external literature, related-work structure, novelty/feasibility distinctions and alternative research hypotheses that should alter what the experiment organization attempts next.
- Decisive decision or feedback right: synthesize surveyed literature/retrieval/memory into a structured proposal and choose/refine prospective research ideas through the Idea Agent's model-driven process.
- Decision owner: first-party Survey/Idea agent stack, especially the Idea Agent (LigAgent) operating over survey-grounded retrieval and Memory-Guided MCTS.
- Supporting / enforcement mechanisms: paper retrieval/clustering, graph-backed references, shared memory, structured `idea_result.json` handoff and pipeline runner.
- Closure path: external literature/topic -> Survey synthesis/retrieval state -> Idea Agent generates/refines a prospective proposal -> `idea_result.json` -> Experiment Agent consumes the proposal and changes present scientific work.
- Boundary reachability: Survey, Idea and the pipeline handoff are documented first-party CLI/runtime surfaces and are directly connected to Experiment in the shipped prototype pipeline.
- Why this is / is not agent-owned: retrieval and pipeline serialization support the loop, but the prospective research-option synthesis/refinement is agent-owned.
- External distinction: papers, topic clusters, graph-backed related work and other retrieved scientific context.
- Future / prospective distinction: whether a candidate research direction is sufficiently differentiated/interesting and how it should be formulated for future experiment work.
- Adaptation option generated: a structured research proposal/idea with experimental direction.
- Path back into current capability / S3: pipeline handoff from Survey -> Idea -> Experiment causes the current Experiment Agent to build and run a project for the selected proposal.
- Evidence: [`README.md`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/README.md), [`src/cli.py`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/cli.py).
- Basis: structural
- Confidence: high
- Caveats: this is a research-direction S4 loop at the declared research-run recursion; generic persistence/memory by itself is not being credited.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure is established for the Xcientist organization.
- Disturbance / variety regulated: topic, model/provider, experiment configuration and reviewer contracts constrain a run, but they do not constitute an identity-level conflict-resolution loop.
- Decisive decision or feedback right: none established for identity/ultimate policy.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: configuration files, research topic/idea inputs, phase contracts, reviewer policies and CLI parameters.
- Closure path: configuration constrains execution directly; no identity/ultimate-policy issue -> authoritative decision -> return-to-operation loop is evidenced.
- Why this is / is not agent-owned: no agent is shown owning the final authority to redefine or reconcile Xcientist's organizational identity/ultimate policy during operation.
- Evidence: [`README.md`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/README.md), [`src/agents/experiment_agent/agents/master/entry.py`](https://github.com/OpenDFM/Xcientist/blob/666eee404bc3cf59249dc8af0ab621cc3e804a49/src/agents/experiment_agent/agents/master/entry.py).
- Basis: structural
- Confidence: high
- Caveats: user authorship of the research topic is environmental/parent input, not a demonstrated first-party S5 mode.

### Absence scope

- Surfaces inspected: top-level workflow/configuration, Survey/Idea/Experiment/Blog responsibilities, master control, reviewer contracts and CLI/pipeline handoffs.
- Plausible first-party paths checked: topic/config as policy, reviewer rules as policy, master convergence as final authority and user-supplied research intent.
- Why no material first-party path remains: each candidate is operational, methodological or task-scoping policy. None is an identity/ultimate-policy dispute with a first-party authoritative closure path.

## Recursion

This assessment fixes one Xcientist research run as the viable system. Experiment workers are operational subunits; Survey/Idea supply prospective intelligence to that run; reviewer agents form a complementary challenge channel. Reclassifying an individual worker as the whole system would change the mapping, so evidence is not transferred across recursion levels without reanalysis.

## Variety and escalation

Operational variety is absorbed first by worker agent reasoning and tool/code execution, then by deterministic hooks and independent reviewer challenge. External scientific variety is handled upstream by Survey/Idea. Blocking reviewer findings return to workers; evidence that passes all experiment gates reaches deterministic phase completion. No separate identity-level escalation path was found.

## Evidence gaps

- The assessment is structural at the pinned revision; no new execution trace was generated as part of this review.
- Some Survey/Idea internals are large and retrieval-heavy; S4 credit relies on the documented shipped pipeline plus code-level handoff surfaces, not a claim that every internal retrieval/memory component is autonomous.
- Upstream OpenHarness semantics are credited only where vendored/wired Xcientist code makes the actor and closure reachable inside the assessed boundary.