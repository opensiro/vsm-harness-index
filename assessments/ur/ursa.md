---
harness_id: ursa
project_name: URSA
repository: https://github.com/lanl/ursa
review_ref: 470b841d83e88457d5677fc824aea32e2d5a5e22
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# URSA — Universal Research and Scientific Agent

## Review boundary

- System in focus: URSA's first-party Python agent and scientific-task organization at the frozen revision: named Chat, Execution, Planning, DeepReview and other agents; BaseAgent's model/tool invocation graph; configured Plan→Executor; dashboard/TUI/CLI; and the shipped optional Agent Team and Agent Symposium environments with first-party model-driven PI, separately scoped participants, peer inspection/revision and organizer synthesis.
- Purpose and identity: Perform adaptive scientific research/planning/code/tool execution and compose model agents into reproducible, revisable research deliverables.
- Relevant environment: Scientific/user questions, local code and documents, workspace files, external research data and search resources, optional MCP/RAG tools, model providers, the user/operator, incompatible or incomplete collaborating participant outputs.
- Standard-distribution boundary: The published `ursa-ai` package and optional installable dashboard environment-running worker, including shipped `AgentTeamEnvironment` and `AgentSymposiumEnvironment`, versus optional externally executed tools/providers. These are alternate first-party configurations; not a claim that all enabled modes run together by default.
- Credited operating / distribution surfaces: [src/ursa/agents/base.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/base.py), [src/ursa/agents/execution_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/execution_agent.py), [src/ursa/agents/planning_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/planning_agent.py), [src/ursa/agents/deep_review_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/deep_review_agent.py), [src/ursa/workflows/planning_execution_workflow.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/workflows/planning_execution_workflow.py), [src/ursa/environments/base.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/base.py), [src/ursa/environments/agent_team.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_team.py), [src/ursa/environments/agent_symposium.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_symposium.py), [src/ursa_dashboard/environment_worker_main.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/environment_worker_main.py), [src/ursa_dashboard/environment_run_manager.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/environment_run_manager.py), [src/ursa_dashboard/registry.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/registry.py), [src/ursa/cli/runtime.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/cli/runtime.py).
- Adjacent first-party surfaces excluded from ownership: Project paper and its reported performance, example runs/benchmarks, development/test-only fixtures, speculative model capabilities, dashboard demo agents and any non-installed experiment-only classes. They may corroborate shipped reachability but do not donate actors, independent audit, future adaptation or governance decisions. External LLM APIs, arXiv/OSTI/search services, shell/scientific binaries, MCP servers, and underlying LangGraph library primitives remain dependencies.
- First-party operating / deployment modes considered: CLI/TUI ordinary conversational/agent route; configured single Execution/Planning/DeepReview agent; published dashboard normal agent route; opt-in dashboard Agent Team with model PI and member delegation; opt-in dashboard Agent Symposium with independently instantiated participants in separate child workspaces, read/compare peer review and revised outputs.
- Recursion level: One URSA-supervised scientific task/research organization whose operative S1 units include named independent research agents/participants. Lower-level agent tool invocations belong to the invoked actor; a remote model or a shell/external scientific platform is not imported as a URSA-owned higher-level metasystem.
- Reviewed revision: `470b841d83e88457d5677fc824aea32e2d5a5e22` frozen in #186, assigned as row 2 of Index assessment batch #1648.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

URSA exposes first-party agent classes and a common `BaseAgent` with configurable model, graph state/checkpointer, workspace and tools. `ExecutionAgent` creates an agent → tool-action → agent loop, then has an ordinary structured-completion review → return-to-agent or recap branch. Its `review_work` uses `self.llm` on the same run history and employs an explicitly **fail-open** structured fallback that marks completion if review fails. This useful S1 quality loop must not itself be promoted to independent S3*. `PlanningAgent` composes reflection with revised plans; `PlanningExecutorWorkflow` runs planner steps sequentially, passing prior-step summaries to the executor; sequencing alone is not a distinct S2/S3. [src/ursa/agents/execution_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/execution_agent.py); [src/ursa/agents/planning_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/planning_agent.py); [src/ursa/workflows/planning_execution_workflow.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/workflows/planning_execution_workflow.py).

The installed optional dashboard can launch `AgentTeamEnvironment` and `AgentSymposiumEnvironment` as worker-run environments (not merely a hypothetical API). Agent Team constructs a real model-driven PI from configured first-party agent classes, supplies named member delegation tools and a whole-team roster/goals prompt, invokes members, and returns their independent results to the PI. The PI dynamically chooses assignments and follow-up from combined current work, not a static for-loop scheduler. The graph is not a persistent project-wide resource optimizer; its S3 current-control claim is limited to the configured **task/team recursion** and prompt-mediated accountable commitments. [src/ursa/environments/agent_team.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_team.py); [src/ursa_dashboard/environment_worker_main.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/environment_worker_main.py); [examples/environments/agent_team.yaml](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/examples/environments/agent_team.yaml).

The separately shipped Agent Symposium is the stronger evidence for inter-S1 conflict attenuation and complementary audit. It instantiates distinct participant agents in **separate child workspaces** using `BaseEnvironment._member_workspace` and `_build_symposium_participant`; participants operate concurrently via `asyncio.gather`. The separate writable defaults reduce the concrete risk that two independent participants overwrite the same generated report, code or intermediate files. This is a scoped first-party **constructor** for file-workspace interference among participants; it is neither an OS sandbox nor a guarantee that an agent with arbitrary filesystem tools cannot write outside its assigned child directory. Agent Team's shared workspace does not gain this S2 property merely by sharing a repository. [src/ursa/environments/base.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/base.py); [src/ursa/environments/agent_symposium.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_symposium.py).

In Symposium review, each reviewer (selected by shipped `reviewer: bool = True` default for configured members) receives **the other members' actual writeups**, is prompted to assess methods, evidence and reproducibility, and temporarily gets the parent symposium workspace for child-artifact inspection. Review is separate from a submitter's ordinary report, and the reviewer is a separately instantiated participant relative to the *other* submitters; the model evaluates competing evidence and reports criticisms, then each original producer receives the other reviewers' critiques and must revise its own writeup before synthesis. **Limitations:** reviewers may also critique their own work, may use the same model provider, and read-only review / no-edit constraints are **prompt-level**, not filesystem ACL enforcement. No protection against collusion or provider-correlated mistakes is claimed. [src/ursa/environments/agent_symposium.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_symposium.py); [src/ursa/environments/config.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/config.py); [examples/environments/agent_symposium.yaml](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/examples/environments/agent_symposium.yaml).

The standalone DeepReviewAgent also cycles hypothesizer, critic and stakeholder prompts with workspace/read-file tools and applies critique on later iterations. However these roles use one shared accumulated messages channel and model binding. This is supplementary task-level review, **not** by itself the decisive independent S3* witness; the cross-participant, cross-artifact Symposium review path above is independently traced instead. [src/ursa/agents/deep_review_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/deep_review_agent.py).

## Operational model

In the simplest mode a configured URSA model performs user-selected research/tool operations; code/file/tool output returns into the first-party invocation graph. In an Agent Team mode a model-driven PI receives the goal and live roster, selects a team member by calling a first-party delegation tool, inspects returned evidence, chooses new/revised commitments where needed, and synthesizes outcomes. In the distinct opt-in Symposium mode, members carry out original tasks in own workspaces, peer reviewers inspect actual writeups (and optionally child files/code) from a complementary path, write independent findings, the first-party workflow returns these findings to each producer's next revision turn, and a separate organizer produces the deliverable. These are **source-attested runnable code paths**, not claims of having paid for or run a live model/research experiment.

## S1 — Operations

- State: A
- Function: URSA-configured model agents autonomously investigate, plan, write or execute scientific work, calling tools and revising from live results.
- Disturbance / variety regulated: Open-ended research/engineering questions, uncertain search data and computational errors, incomplete or failing tool results.
- Decisive decision or feedback right: Model-driven ExecutionAgent chooses tool calls and continuation; named participating agents produce task-relevant results from their individual workspaces and tool feedback.
- Decision owner: First-party URSA model/tool agent graph; configured backend model supplies inference rather than a separately authored external research harness.
- Supporting / enforcement mechanisms: LangGraph execution/checkpoint wrappers, named agent configuration, workspace, session state, tool registry, sandbox/safety checks, provider invocation and optional RAG/MCP support.
- Closure path: prompt/task → model decides code/tool action → first-party tool node executes → workspace/tool observation returned → next model decision / final task result.
- Boundary reachability: Installed `ursa` runtime registers and invokes named first-party agents; dashboard registry builds ExecutionAgent/other shipped agents; Agent Team and Symposium use these installed classes for their members and PI.
- Why this is / is not agent-owned: The agent's configured LLM picks concrete operations based on observed tool state, rather than only executing a fixed static plan. Shell tools/search models remain dependencies.
- Evidence: [src/ursa/agents/base.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/base.py); [src/ursa/agents/execution_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/execution_agent.py); [src/ursa/cli/runtime.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/cli/runtime.py); [src/ursa_dashboard/registry.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/registry.py).
- Basis: Explicit first-party installed model/tool loop; structural source, not a live provider receipt.
- Confidence: High for reachable code path.
- Caveats: Requires model/API and actual scientific tools/data for practical work; no task success/performance measured.


## S2 — Coordination

- State: C
- Function: Attenuate conflicting concurrent writable output ownership by multiple independent research S1 agents in the shipped optional Symposium mode.
- Disturbance / variety regulated: Simultaneously executing researchers writing common filenames, scripts, reports and intermediate scientific artefacts could overwrite/confound each other's work.
- Decisive decision or feedback right: The first-party Symposium constructor assigns each configured participant its own child workspace `<symposium_workspace>/<member_name>` before concurrent invocation, rather than allowing default shared-writable member workspace.
- Decision owner: Deterministic first-party workspace-topology constructor under configured member identity; no autonomous model-owned inter-S1 arbitration claimed.
- Supporting / enforcement mechanisms: `BaseEnvironment._member_workspace`, member factory, named/group state, initial `asyncio.gather` and revision participant workspaces.
- Closure path: Distinct S1 member identity → per-member child work path selected → member's subsequent tool/code operations run against its own default workspace → independent results returned to Symposium → next participant revision again in member workspace.
- Boundary reachability: A supported `agent_symposium` launch via dashboard environment worker instantiates this first-party default; direct `AgentSymposiumEnvironment` API and packaged sample configuration also exercise it.
- Why this is / is not agent-owned: The concrete coordination choice is built into first-party topology; an agent is not shown dynamically choosing anti-collision strategy. This is **C**, not A, and not generic message transport.
- Distinct S1 units: At least two separately instantiated configured Symposium member agents/nested teams with independent research outputs.
- Inter-S1 disturbance: Concurrent conflicting writes or result overwrites if distinct S1 participants share the same default working directory and filenames.
- Attenuating coordination relation: Per-member child workspaces localize each participant's default write target; review temporarily switches to parent workspace only for a declared inspection phase.
- Feedback into subsequent S1 behaviour: Path context passed to each configured member's subsequent run directs its tools/output to its own child path; revised artefacts remain scoped and visible for later review.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The assessed relation changes conflicting writable resource ownership for **parallel** separate researchers, not merely who receives a prompt or when the next step runs.
- Evidence: [src/ursa/environments/base.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/base.py); [src/ursa/environments/agent_symposium.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_symposium.py); [src/ursa_dashboard/environment_worker_main.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/environment_worker_main.py); [examples/environments/agent_symposium.yaml](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/examples/environments/agent_symposium.yaml).
- Basis: Structural first-party conflict attenuation in shipped optional operating mode.
- Confidence: Medium for bounded default-workspace collision reduction.
- Caveats: Not a security sandbox or enforced cross-member write prohibition; arbitrary filesystem tools could cross directories. Shared-workspace Agent Team mode does not inherit this claim.


## S3 — Inside-and-now control

- State: A
- Function: The model-driven Agent Team PI regulates current team-level research commitments and correction among currently available member agents.
- Disturbance / variety regulated: Divergent partial research results, missed commitments, mismatched specialist expertise and need to reassign/follow up while satisfying the shared current goal.
- Decisive decision or feedback right: From a whole-team roster, overall goal and returned member outputs, PI chooses current member assignment, follow-up work or direct synthesis to address gaps.
- Decision owner: Configured first-party model-driven PI agent with delegated member tools, not dashboard background scheduler or static script.
- Supporting / enforcement mechanisms: Team config, named agent/member registry, first-party dynamic delegate_to tools, per-member call/result events, optional nested teams and provider model.
- Closure path: overall goal + roster → PI discretionary member commitment choice → first-party delegation tool → member tool/model execution → outcome and evidence returned to PI → PI can choose follow-up/revised assignment and final integration.
- Boundary reachability: The shipped dashboard worker starts `AgentTeamEnvironment`; `_build_pi` actually attaches delegation tools to `ExecutionAgent`, and `_ainvoke` calls PI with whole-team instructions. These are installed, configured first-party behaviors, not external supervisor CLI assumptions.
- Why this is / is not agent-owned: The model PI selects and revises team current commitments conditional on returned results. The observation is **bounded to task/team scope**, not lasting across independent projects or resource budgets; deterministic dispatch executes its choices.
- Whole-system current view: Declared task and full configured team roster, plus member results and evidence of previous dispatches in PI conversation context.
- Current-control decision scope: Which present team agent tackles a research subproblem, whether to ask a member for correction/additional work, and when the integrated task can close.
- Evidence: [src/ursa/environments/agent_team.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_team.py); [src/ursa/environments/base.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/base.py); [src/ursa_dashboard/environment_worker_main.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/environment_worker_main.py); [examples/environments/agent_team.yaml](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/examples/environments/agent_team.yaml).
- Basis: Explicit reachable opt-in whole-team model decision right with action/return.
- Confidence: Medium: prompt-mediated scheduling and follow-up, not guaranteed intervention in every execution or durable institution-wide commitments.
- Caveats: A default single Chat/ExecutionAgent has no proven whole-team S3. Static PlanningExecutor step sequencing alone would be insufficient. No preemption of in-flight member calls or sophisticated resource/budget bargaining is claimed.


## S3* — Complementary audit

- State: A
- Function: A separate Symposium participant challenges another agent's research/output claims by independently examining cross-member work, then returns evidence-backed criticism for revision.
- Disturbance / variety regulated: Unverified self-reported research correctness, erroneous code or weak evidence that can survive an author-only status and ordinary completion check.
- Decisive decision or feedback right: Reviewer model judges validity, strength, reproducibility and needed corrections of **other participants'** submitted writeups/artefacts; author model then decides revised work informed by review.
- Decision owner: Separately instantiated configured reviewer participant model(s) in the opt-in Agent Symposium environment, for claims made by **different** producer agents.
- Supporting / enforcement mechanisms: Reviewer membership default `reviewer: true`, actual complete writeup collection, review-only instruction, parent-workspace inspection, independent participant invocation, first-party mapping of review results to each next revision prompt.
- Closure path: ordinary member output/writeup → separate reviewer gets other participants' output + parent child-artifact access → reviewer develops challenges/evidence → critique per review round → first-party revision prompts to original writers → changed subsequent member submissions → organizer synthesis.
- Boundary reachability: Dashboard environment worker actually creates AgentSymposium from packaged class/config; `_ainvoke` runs initial participant work, explicitly chooses review-enabled members, invokes them on cross-member materials, collects critiques, and executes further revision rounds. The example config has multiple members, including an independent research path.
- Why this is / is not agent-owned: Review judgment is discretionary to a separate model-driven member; the deterministic round scheduler and presenter only transmit findings. A mere `review_work` call on ExecutionAgent or same-channel DeepReview role swap was not used for the positive claim.
- Claim being audited: Another participant's scientific/code writeup is adequate, evidence-based and reproducible.
- Ordinary reporting path: Original writer's answer, file outputs and internal completion review to Symposium.
- Complementary access path: Peer model gets all actual participant writeups (including other workers') and, during review, parent-workspace view of other participants' child files; can inspect or run referenced code to assess reproducibility.
- Independence boundary: Distinct configured agent instances, participant identities and task workspaces, reviewed by a different author/participant. Not a separate model vendor by requirement, not a cryptographic or physical write-protect boundary: reviewers may inspect their own outputs, the same provider/model may be reused and no-edit is instruction-only.
- Who acts on findings: The Symposium constructor distributes review text to every original participant via their revision prompt; those model agents revise their own submitted writeups, then the organizer receives updated outputs.
- Evidence: [src/ursa/environments/agent_symposium.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_symposium.py); [src/ursa/environments/base.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/base.py); [src/ursa/environments/config.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/config.py); [src/ursa_dashboard/environment_worker_main.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/environment_worker_main.py); [examples/environments/agent_symposium.yaml](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/examples/environments/agent_symposium.yaml); [src/ursa/agents/execution_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/execution_agent.py); [src/ursa/agents/deep_review_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/deep_review_agent.py).
- Basis: Source-attested cross-actor complementary read/review/revise feedback loop in installed optional mode.
- Confidence: Medium for first-party prompt-enforced agent independence and corrective return. Low for any stronger claim of immutable artifacts, clean-room evidence, adversarial non-collusion or robust gate.
- Caveats: No empirical reviewer accuracy, run-time contamination controls, code immutability or guaranteed finding acceptance. The single-agent fail-open completion reviewer is expressly excluded.


## S4 — Outside-and-then intelligence

- State: —
- Function: No substantiated future/environment-oriented adaptation that changes URSA's organizational capability and returns it to subsequent operation.
- Disturbance / variety regulated: Task-level research uncertainty, new web/RAG results, changing plan/task hypotheses; those are operational problem-solving rather than future harness adaptability.
- Decisive decision or feedback right: No first-party model, constructor or eligible parent mode shown selecting longer-horizon change to URSA's organizational capabilities in response to external trends.
- Decision owner: Research-task models for evolving research answers; package maintainers/operator for non-runtime manual changes.
- Supporting / enforcement mechanisms: Planning reflection, DeepReview iterative solution refinement, optimisation agents and session/checkpoint persistence.
- Closure path: These can refine current research output, but no future/environment sensing → proposed change of agent/workflow capability → adopted operational configuration → later run is evidenced.
- Why this is / is not agent-owned: Scientific hypothesis evolution, optimization and internal benchmark tasks are not inherently VSM S4 adaptation of the URSA organization.
- Evidence: [src/ursa/agents/planning_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/planning_agent.py); [src/ursa/agents/deep_review_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/deep_review_agent.py); [src/ursa/agents/optimization_agent.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/agents/optimization_agent.py); [src/ursa/cli/runtime.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/cli/runtime.py); [src/ursa/environments/agent_team.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_team.py).
- Basis: Bounded absence after checking opt-in team/symposium and adjacent adaptive task sources.
- Confidence: Medium-high for current supported operational scope.
- Caveats: If an actually installed cross-run capability change loop is evidenced at same pin, re-assess rather than extrapolate from naming.

### Absence scope

- Surfaces inspected: Agent/workflow implementations, model/checkpointer/memory, optional team/symposium, scientific optimization and available CLI/dashboard configuration.
- Plausible first-party paths checked: Planning reflection, iterative DeepReview research answer revision, optimisation loops, persistent agent sessions and optional scientific-research environment.
- Why no material first-party path remains: All examined feedback changes the current problem's content or fixed workflow results, not a prospective organization-level capability/structure based on external-future distinctions with adopted return to later operation.


## S5 — Policy and identity

- State: —
- Function: No supported first-party ultimate identity/policy determination returned to govern the scientific-task organization.
- Disturbance / variety regulated: Configured workspace scope, selected models, shell safety checks, dashboards/users and team config; these are policy inputs and task gates, not evidenced ultimate identity settlement.
- Decisive decision or feedback right: User/developer specifies local settings and research goals; no installed model/constructor or eligible parent authority resolves an ultimate organization-level policy/identity conflict and returns binding policy to activity.
- Decision owner: Task owner chooses settings; no function-specific S5 owner evidenced in the shipped assessed recursion.
- Supporting / enforcement mechanisms: Security checks, validation, model/tool configuration, named agent/team member metadata and optional dashboard auth.
- Closure path: No first-party identity/policy issue → recognized ultimate authority → returned authoritative decision → governed next operation was identified.
- Why this is / is not agent-owned: Named groups, access credentials, human research approvals and selection of provider/agent parameters do not automatically establish S5.
- Evidence: [src/ursa/environments/config.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/config.py); [src/ursa/cli/runtime.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/cli/runtime.py); [src/ursa/security.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/security.py); [src/ursa_dashboard/security.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa_dashboard/security.py); [src/ursa/environments/agent_team.py](https://github.com/lanl/ursa/blob/470b841d83e88457d5677fc824aea32e2d5a5e22/src/ursa/environments/agent_team.py).
- Basis: Bounded negative review of shipped policy/configuration/operational paths.
- Confidence: Medium-high within declared task-level recursion.
- Caveats: Los Alamos organizational policy, repository project maintainership, or external credentials are distinct authorities not imported into this task harness.

### Absence scope

- Surfaces inspected: Agent/team/symposium config, provider and access control, dashboard security, task user routing, research source and package governance.
- Plausible first-party paths checked: Project configuration, static team roles, login/sandbox protections, human choices and nested team policies.
- Why no material first-party path remains: No evidence of a distinct ultimate-policy/identity decision loop with first-party owner and operational return beyond ordinary chosen task/configuration.


## Distributed OSS parent arrangement

The source is a public scientific Python package. Contributor/maintainer governance and LANL ownership do not establish runtime-wide parent S3/S4/S5 at the assessed URSA scientific-task recursion. In a configured Agent Team, the model PI (not a GitHub maintainer) chooses active work; in a Symposium, first-party reviewed member output changes subsequent in-run tasks. Nothing here claims the public OSS maintainers govern every self-hosted team's runtime.

## Self-hosted and non-human modes

An operator can run CLI/TUI locally or deploy a dashboard with different agent/group/model/tool configurations; some support configured assistants or approval-like interactions. This does not prove parent-governed S3/S4/S5 ownership in the absence of a whole-system parent-authority loop. The positive `A` and `C` modes are bounded to installed first-party options; agent-team current-control and peer audit are not asserted for bare single-agent CLI sessions.

## Recursion

The principal analyzed system is a configured URSA task/research group. `ExecutionAgent` and peer participants are distinct S1 operations when orchestrated, and a team PI is current-control at that group's scope. Symposium peer review provides cross-participant complementary access and corrective return. A nested Agent Team as one Symposium member can form an additional task level, but simply nesting Python classes or providers does not establish a higher VSM viable recursion.

## Variety and escalation

URSA amplifies problem-solving variety through tools, scientific knowledge acquisition, execution and multiple specialist models. It attenuates **specific sibling write-path interference** in opt-in Symposium through child workspaces and attenuates claim-quality uncertainty through cross-member reviewer evidence and revised work. Agent Team exposes current commitments to the PI, who chooses follow-up decisions. Safety checks and tool failures can constrain S1; there is no claim of an institution-wide algedonic escalation channel, and optional dashboard governance should not be promoted to S5 without owner closure.

## Evidence gaps

- No external model API/scientific job was invoked for this review, and no benchmark/paper claimed metric was used as classification evidence. Code-level reachability and function-specific closure are assessed, not successful real-world performance.
- For `S2=C`, child paths are operating defaults rather than OS-level cross-write isolation; absolute noninterference is **not** claimed. The normal Agent Team shared workspace does not gain S2 through mere delegation.
- For `S3=A`, the current scope is the configured team task/roster with model-directed assignments and returned results, not durable budgeting, interrupting running agents or governance across unrelated projects.
- For `S3*=A`, peer reviewers are distinct model actors relative to other participants and may read peer work, but default reviewer instruction does not prove that raw evidence is immutable or that a human-independent protected gate exists. Same-vendor correlated errors and self-review coexist with peer-review function. The fail-open in-agent completion review and same-channel DeepReview are *not* counted as separate positive S3* evidence.
- `S4=—` and `S5=—` are negative judgments about traced first-party standard-distribution paths under the frozen revision, not claims of universal impossibility. A later evidence-based correction at that ref remains possible.
