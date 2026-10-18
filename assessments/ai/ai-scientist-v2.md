---
harness_id: ai-scientist-v2
project_name: The AI Scientist-v2
repository: https://github.com/SakanaAI/AI-Scientist-v2
review_ref: 96bd51617cfdbb494a9fc283af00fe090edfae48
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# The AI Scientist-v2

## Review boundary

- System in focus: the first-party AI Scientist-v2 research runtime at pinned revision `96bd51617cfdbb494a9fc283af00fe090edfae48`, including template-free ideation, Semantic Scholar tool use, progressive agentic tree-search experimentation, `AgentManager`, parallel experiment agents/journals, multi-seed evaluation, plotting, write-up and downstream review surfaces.
- Purpose and identity: autonomously generate a research proposal, explore and evaluate executable ML experiments through staged agentic tree search, analyze results and produce a manuscript.
- Relevant environment: researcher-supplied workshop/topic description; external scientific literature; model-provider responses; local experiment workspace/code; datasets/GPU runtime; metrics, plots and execution failures; resulting manuscript.
- Standard-distribution boundary: code shipped in `SakanaAI/AI-Scientist-v2` at the reviewed revision. External model providers, Semantic Scholar, Hugging Face datasets, CUDA/OS/container substrate and AIDE provenance not owned by the shipped code remain dependencies/environment.
- Credited operating / distribution surfaces: `ai_scientist/perform_ideation_temp_free.py`; `ai_scientist/treesearch/`; `launch_scientist_bfts.py`; first-party write-up/plot/review modules used by that entrypoint.
- Adjacent first-party surfaces excluded from ownership: paper/blog/project claims not backed by pinned code, external workshop experiment repositories, repository CI/docs, and upstream AIDE behavior not instantiated/owned by the pinned runtime.
- First-party operating / deployment modes considered: template-free idea generation followed by `launch_scientist_bfts.py` experimentation/write-up/review using the shipped BFTS configuration and agent manager.
- Recursion level: one AI Scientist-v2 research run as the system-in-focus. Parallel search workers/nodes are operational subunits; `AgentManager` is the inside-and-now control actor at this recursion.
- Reviewed revision: `96bd51617cfdbb494a9fc283af00fe090edfae48`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

AI Scientist-v2 separates prospective ideation from experimentation. The ideation agent must use a Semantic Scholar search tool before finalizing a structured proposal containing a hypothesis, related work, experiments and risks. The experiment runtime then constructs a staged `AgentManager` around parallel tree-search agents and journals. Main stages are initial implementation, baseline tuning, creative research and ablation studies; best nodes are propagated between stages.

`AgentManager` holds current stages, journals, stage history and completed-stage state. It uses model queries over current evidence/plot feedback to judge sub-stage or stage completion and to synthesize concrete next sub-stage goals from current metrics, issues and recent changes. After stage completion, the runtime runs multi-seed evaluation and plot aggregation on the best implementation before advancing. The final launcher writes the paper and may run LLM/VLM paper review, but those final review results are only persisted; no pinned path returns them into a manuscript-correction loop.

## Operational model

Parallel agents generate/modify executable experiment implementations, run them, observe metrics/errors and extend a search journal. The manager repeatedly observes the current journal/best-node evidence and decides whether to continue or advance and what the next adaptive experimental focus should be. The outside-and-then path precedes this: an ideation agent searches external literature, reflects on novelty and finalizes a proposal consumed by the experimentation runtime.

## S1 — Operations

- State: A
- Function: autonomously perform executable ML research experiments through model-driven proposal/code changes, execution and feedback-guided search.
- Disturbance / variety regulated: implementation failures, changing metrics/plots, alternative model/data choices, debugging needs and experimental outcomes across tree-search nodes.
- Decisive decision or feedback right: choose concrete experiment/code changes and search-node actions based on current task description, parent node/history and execution feedback.
- Decision owner: first-party parallel experiment/search agents instantiated by `AgentManager`.
- Supporting / enforcement mechanisms: journals/nodes, experiment executor callbacks, workspace isolation/state, stage-specific task descriptions, search budgets and GPU/process management.
- Closure path: research-stage goal/current node -> agent proposes implementation/experiment -> runtime executes it -> metrics/errors/plots are recorded in journal state -> agent/search policy chooses subsequent node/action.
- Boundary reachability: the tree-search agents are created and run by the shipped `AgentManager` used directly by `launch_scientist_bfts.py`.
- Why this is / is not agent-owned: schedulers/GPU management enforce execution resources, but the context-sensitive experimental action is selected by model-driven agents.
- Evidence: [`README.md`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/README.md), [`agent_manager.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/agent_manager.py), [`parallel_agent.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/parallel_agent.py).
- Basis: structural
- Confidence: high
- Caveats: external model/GPU/data services are substrate; credit is for the first-party experiment/search control loop.

## S2 — Coordination

- State: —
- Function: no material agent-owned S2 coordination path is established among the parallel S1 search workers.
- Disturbance / variety regulated: workers share finite execution resources and contribute nodes to experiment search, but no agent-owned interference/oscillation detector and attenuation relation is established.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: parallel worker scheduling, GPU manager/allocation, journals and tree-search selection.
- Closure path: resource/scheduling code assigns/releases execution capacity and search code selects nodes; this is deterministic orchestration rather than an S2 conflict-regulation conversation.
- Why this is / is not agent-owned: worker plurality and GPU allocation are not promoted to S2 without an agent-owned response to a concrete inter-S1 disturbance.
- Evidence: [`parallel_agent.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/parallel_agent.py), [`agent_manager.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/agent_manager.py).
- Basis: structural
- Confidence: high
- Caveats: deterministic resource arbitration is operationally useful but does not establish autonomous S2 ownership.

### Absence scope

- Surfaces inspected: `AgentManager`, parallel-agent/tree-search implementation, journals, GPU management, stage transitions and multi-seed evaluation.
- Plausible first-party paths checked: parallel workers, shared journal/tree state, GPU assignment/release and best-node selection.
- Why no material first-party path remains: the inspected mechanisms schedule resources or select search nodes; none identifies and autonomously attenuates a concrete cross-S1 conflict/oscillation with feedback to the affected workers.

## S3 — Inside-and-now control

- State: A
- Function: maintain a whole-experiment current view and adaptively control stage completion, continuation and next experimental focus on behalf of the research run.
- Disturbance / variety regulated: incomplete or unstable implementations, insufficient dataset coverage, weak progress, missing stage criteria, changing best-node evidence and current experimental issues.
- Decisive decision or feedback right: judge whether the current sub-stage/stage is complete and generate measurable next sub-stage goals/focus from current experiment evidence; advance or continue the staged research program accordingly.
- Decision owner: the model-driven feedback/control queries executed by the first-party `AgentManager` over its whole current stage/journal state.
- Supporting / enforcement mechanisms: stage/journal state, best-node selection, VLM plot feedback, structured completion function schemas, hard bounds/fallback rules, checkpointing and stage-transition machinery.
- Closure path: current journals/best node/metrics/plot feedback -> manager control query judges completion or identifies missing criteria -> manager continues current stage or creates a new focused sub-stage/main stage -> subsequent agents receive the revised stage goals and operate under them.
- Boundary reachability: `AgentManager` is instantiated by the standard BFTS experiment path and its `run()` loop directly creates worker agents and applies the completion/focus decisions.
- Why this is / is not agent-owned: fixed stage ordering and max-iteration bounds are deterministic support, but the materially adaptive completion/focus judgments are model queries that change subsequent whole-run experiment commitments.
- Whole-system current view: current stage, all stage journals/history, best implementation, success counts/metrics, VLM feedback, tested datasets and current issues/progress at the declared experiment-run recursion.
- Current-control decision scope: whether to continue/complete the current stage and what concrete goals/focus the next sub-stage should impose on all subsequent experiment workers.
- Evidence: [`agent_manager.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/agent_manager.py), [`perform_experiments_bfts_with_agentmanager.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/perform_experiments_bfts_with_agentmanager.py).
- Basis: structural
- Confidence: high
- Caveats: some stage transitions/termination rules remain hard-coded; S3 credit is for the model-owned adaptive completion/focus control that is enforced by the manager, not for those deterministic limits.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit loop returning sufficiently independent findings into the S3 current-control path is established at the reviewed revision.
- Disturbance / variety regulated: VLM plot analysis, multi-seed evaluation and final paper review provide evaluation signals, but their roles do not establish a separate operational audit channel with corrective return to S3.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: plot/VLM feedback, multi-seed evaluation, LLM text review and image/caption/reference review.
- Closure path: VLM/metric feedback is consumed as part of ordinary manager evaluation; final paper reviews are written to files after write-up and are not returned into a correction/re-control loop.
- Why this is / is not agent-owned: evaluator agents/models exist, but evaluation naming or separate inference alone is insufficient without a complementary independence-and-corrective-return closure.
- Evidence: [`agent_manager.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/agent_manager.py), [`launch_scientist_bfts.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/launch_scientist_bfts.py).
- Basis: structural
- Confidence: high
- Caveats: this classification does not deny the scientific value of multi-seed/VLM evaluation; it distinguishes ordinary evaluation/control evidence from S3* complementary audit.

### Absence scope

- Surfaces inspected: manager VLM/completion feedback, multi-seed evaluation, plot aggregation, final LLM/VLM paper review and launcher control flow.
- Plausible first-party paths checked: VLM feedback as independent audit, multi-seed evaluation as challenge, final peer review as audit and write-up retry logic as corrective return.
- Why no material first-party path remains: VLM/multi-seed signals are embedded in ordinary experimentation/control, while final paper reviews are terminal artifacts. No separate challenge path with findings returned to S3 or an operational correction loop is established.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense external literature and prospective scientific opportunity, generate/refine a future research proposal, and return that option into current experiment execution.
- Disturbance / variety regulated: prior literature may make ideas non-novel; alternative hypotheses/experiments may differ in feasibility, impact and relation to existing work.
- Decisive decision or feedback right: choose search queries, incorporate retrieved literature into reflection, and finalize a structured future proposal/hypothesis/experiment plan.
- Decision owner: first-party ideation LLM agent using the shipped Semantic Scholar tool loop.
- Supporting / enforcement mechanisms: `SemanticScholarSearchTool`, action/tool protocol, reflection loop, structured `FinalizeIdea` schema and JSON handoff to launcher.
- Closure path: workshop/topic description -> ideation agent searches external literature -> retrieved results alter reflection/proposal -> agent finalizes structured idea -> `launch_scientist_bfts.py` consumes that idea and executes the experiment program.
- Boundary reachability: `perform_ideation_temp_free.py` is the documented first step for generating the JSON consumed by the standard experiment launcher.
- Why this is / is not agent-owned: the search tool supplies evidence, but the prospective research-option synthesis and finalization are agent decisions.
- External distinction: Semantic Scholar literature and related-work evidence.
- Future / prospective distinction: novelty, feasibility, risks and which hypothesis/experiments should be pursued next.
- Adaptation option generated: structured research proposal containing hypothesis, related work, experiments and limitations.
- Path back into current capability / S3: generated idea JSON becomes the task description for `AgentManager` and its experiment stages.
- Evidence: [`perform_ideation_temp_free.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/perform_ideation_temp_free.py), [`README.md`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/README.md), [`launch_scientist_bfts.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/launch_scientist_bfts.py).
- Basis: structural
- Confidence: high
- Caveats: S4 credit is for the external-literature-to-proposal-to-experiment closure, not for tree search or journal persistence by themselves.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure is established.
- Disturbance / variety regulated: workshop/topic descriptions, stage goals, risk-factor prompts, model choices and BFTS configuration constrain research, but they do not form an identity-level ultimate-authority loop.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: workshop description, proposal schema, hard-coded main-stage goals, YAML search configuration and CLI arguments.
- Closure path: configuration/prompt policy directly constrains the run; no identity/ultimate-policy issue is escalated to an authoritative actor and returned as governing policy.
- Why this is / is not agent-owned: the agent manager can adapt current experimental focus, but it is not given authority to redefine the system's identity or ultimate research policy.
- Evidence: [`agent_manager.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/treesearch/agent_manager.py), [`perform_ideation_temp_free.py`](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/ai_scientist/perform_ideation_temp_free.py).
- Basis: structural
- Confidence: high
- Caveats: research-topic authorship and fixed stage policies are task/governance inputs, not S5 closure.

### Absence scope

- Surfaces inspected: ideation protocol, `AgentManager` stage policy, BFTS configuration, launcher/model choices, paper review and runtime termination.
- Plausible first-party paths checked: experiment manager as ultimate authority, workshop description as identity, hard-coded stage goals as policy and final review as policy approval.
- Why no material first-party path remains: these mechanisms select/adapt research work within a pre-existing mission. None closes an identity/ultimate-policy question and returns that authoritative decision into operation.

## Recursion

One research run is the viable system. Tree-search workers/nodes are S1 subunits; `AgentManager` controls current experiment organization at S3; the separate ideation process supplies S4 options before/currently into that experiment organization. Moving the boundary to a single search worker would remove the whole-system S3 mapping.

## Variety and escalation

Worker-level execution variety is absorbed by experiment/search loops. Current whole-run variety escalates to `AgentManager`, which can change stage completion/focus. External scientific variety is handled by the ideation/literature tool loop before the proposal is committed. Final manuscript review does not close back into this control hierarchy at the pinned revision.

## Evidence gaps

- Structural review only; no new AI Scientist-v2 run was executed.
- S3 depends on the shipped model-driven completion/focus queries being reachable under the selected BFTS configuration; deterministic fallback/max-iteration paths are not themselves credited.
- External provider/tool quality and upstream AIDE semantics are outside the assessed ownership boundary.