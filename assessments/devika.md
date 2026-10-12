---
harness_id: devika
project_name: Devika
repository: https://github.com/stitionai/devika
review_ref: 80bb343cbe4a4e5f5a0ba08d2524920139baceb6
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Devika

## Review boundary
- System in focus: the frozen first-party Devika Python software-engineering agent launched through its Flask/Socket.IO API, central Agent class, model-backed planning/research/coding/action/runner/patcher helpers and project browser/workspace operations.
- Purpose and identity: autonomously turn a user's project instruction into a plan, gather task-relevant context and write/change code with optional follow-up execution and repair.
- Relevant environment: user messages, project files, LLM-provider responses, web research pages, shell errors, sandbox/runtime constraints, project records and explicitly supplied follow-up requests.
- Standard-distribution boundary: shipped `devika.py` endpoint → `src/agents/agent.py` and first-party helper modules; no provider-native agent organization, external GitHub/Netlify organization or aspirational roadmap behavior attributed ([README.md](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md); [devika.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/devika.py#L68-L103)).
- Credited operating / distribution surfaces: [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py); [src/agents/planner/planner.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/planner/planner.py); [src/agents/researcher/researcher.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/researcher/researcher.py); [src/agents/coder/coder.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/coder/coder.py); [src/agents/action/action.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/action/action.py); [src/agents/runner/runner.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/runner/runner.py); [src/agents/patcher/patcher.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/patcher/patcher.py); [src/browser/interaction.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/browser/interaction.py); [src/state.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/state.py).
- Adjacent first-party surfaces excluded from ownership: unused/experimental expert examples, user scripts not called by the installed agent, docs/roadmap wishes, raw LLM provider internals, external user approval organization and external deployment-service workflows.
- First-party operating / deployment modes considered: initial plan/research/write-code execution; follow-up Action dispatch to run/feature/bug/report/deploy; browser-crawling model loop; optional code-run-and-patch feedback mode.
- Recursion level: one Devika project/session operating agent with sequential specialized prompt roles; neither each Python helper nor each Flask thread is presumed an independent organizational S1.
- Reviewed revision: `80bb343cbe4a4e5f5a0ba08d2524920139baceb6`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The first-party Socket.IO handler invokes `Agent.execute` on a fresh task or `Agent.subsequent_execute` on a follow-up; a new Thread is just a host execution mechanism. The initial central agent synchronously sequences model-backed Planner, Researcher, browser/search, Coder and writes files into one project workspace. The follow-up Action model selects a supported task (answer, run, feature, bug, deploy or report) and invokes the corresponding module. Specialized Python classes call the same configured model abstraction and return structured values; they are not separately concurrently operating worker-agent organizations merely because docs call them sub-agents. [devika.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/devika.py#L68-L103); [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L179-L268); [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L270-L365).
The Runner follow-up can execute saved code with `subprocess.run`, read actual return codes/output, ask a model for rerun/patch and rerun commands after patching. This is a real observational feedback path, but it is tied to the ordinary task-execution/repair workflow rather than a demonstrated independently sampling complementary reviewer of producing S1 results. [src/agents/runner/runner.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/runner/runner.py#L70-L180); [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L195-L248).

## Operational model
Devika's central single operating session uses LLM decisions in planning, web research and code production; the host calls specialized prompt stages in a largely serial program. Follow-up requests can initiate real execution and limited repair. Project state and action dispatch are not automatically superior systems managing distinct independent operating S1 units. Distinguish real error feedback from independent S3* access.

## S1 — Operations
- State: A
- Function: Model-directed software-engineering task work, web research, code generation and task-conditioned follow-up actions using environment feedback.
- Disturbance / variety regulated: Unstructured user software requests, changing web content, project file contents, command failures and tool/provider errors.
- Decisive decision or feedback right: Choose task plan, search queries, code modifications and follow-up action class based on input and observed task state.
- Decision owner: Devika's configured LLM-driven central coding agent, via first-party Planner/Researcher/Coder/Action modules.
- Supporting / enforcement mechanisms: Flask/Socket.IO controller, sequential model prompt stages, Browser/Crawler, ProjectManager, persisted AgentState, Runner/Patcher.
- Closure path: User request → LLM-generated plan/research/code → files and tool outputs → optional follow-up action/repair and updated project results.
- Boundary reachability: The shipped server calls the central agent execution on user messages, and the agent actually invokes first-party model-facing work modules and project writing ([devika.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/devika.py#L68-L103); [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L270-L365)).
- Why this is / is not agent-owned: The plan, task-specific code and follow-up choices are model-generated, rather than a deterministic list of static responses.
- Evidence: [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py); [src/agents/planner/planner.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/planner/planner.py); [src/agents/coder/coder.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/coder/coder.py); [src/agents/action/action.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/action/action.py).
- Basis: structural
- Confidence: high
- Caveats: No live LLM-backed software task was executed; code reachability is source-backed, not a performance claim.

## S2 — Coordination
- State: —
- Function: No material first-party path for regulating concrete interference among distinct independently acting S1 units in the declared installed coding session.
- Disturbance / variety regulated: Possible overlapping requests or file conflicts are risks, not a demonstrated distinct-agent contention controller.
- Decisive decision or feedback right: No S2-specific inter-S1 arbitration choice is shipped in examined central agent execution.
- Decision owner: Not established for S2; central host serially invokes specialized model prompt functions.
- Supporting / enforcement mechanisms: Planner/Researcher/Coder/Runner pipeline, project state and host Threads.
- Closure path: Specialized stages pass data serially to one central task owner; no conflict sensor → attenuation → adjusted independent worker path.
- Why this is / is not agent-owned: Multiple model-prompt classes and endpoint threads are not independently allocated, colliding, concurrent S1 workers with coordination feedback.
- Evidence: [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L270-L365); [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L179-L268); [devika.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/devika.py#L68-L103); [src/state.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/state.py).
- Basis: structural
- Confidence: medium
- Caveats: Bounded negative is at the supported installed central-agent/project scope; external user-managed concurrent sessions are excluded.
### Absence scope
- Surfaces inspected: server user-message handler and thread admission, the central agent's initial/follow-up dispatch, specialized model stages, project/session persistence and runner.
- Plausible first-party paths checked: independent worker creation, concurrent autonomous task delegation, collisions between project-mutating units and workspace reservation/coordinator feedback.
- Why no material first-party path remains: model-backed helpers are synchronous substages of the same root operation; host threads can overlap but have no separately acting, coordinated agent ownership with a concrete regulated inter-S1 disturbance.

## S3 — Inside-and-now control
- State: —
- Function: No separate whole-current operational control across a plurality of autonomous S1 units is provided by the assessed first-party coding-session mode.
- Disturbance / variety regulated: Current code task progress and errors are absorbed within one S1 task cycle; no larger operating portfolio evidenced.
- Decisive decision or feedback right: A model selects task steps/actions but not whole-system multi-S1 resource commitments or interventions.
- Decision owner: The central task agent for task-level work; no higher-recursion S3 owner established.
- Supporting / enforcement mechanisms: Project state, optional Action model, user input, sequential pipeline and threaded server.
- Closure path: Single project task state → model continuation; no independent operating-unit reports → parent resource/priority bargaining → revised commitments.
- Why this is / is not agent-owned: A Planner, ProjectManager or host runner is not S3 solely by naming or by selecting next action for the same task.
- Evidence: [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py); [src/state.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/state.py); [src/project.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/project.py); [src/agents/planner/planner.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/planner/planner.py).
- Basis: structural
- Confidence: medium
- Caveats: Does not deny that a human user may coordinate multiple independent Devika deployments outside this boundary.
### Absence scope
- Surfaces inspected: entry/server and project controls, Agent orchestration, Planner, Action routing, AgentState and persisted project interaction.
- Plausible first-party paths checked: controlling multiple active independent agent operations, cross-worker commitment allocation, operational feedback/whole-current views, human-parent governance.
- Why no material first-party path remains: each task's model stages operate under one Agent and no shipped first-party team-level decision right is reconstructed.

## S3* — Complementary audit
- State: ?
- Function: Runner may access executed project code via subprocess and feed observed error results into a patch cycle; whether this constitutes complementary independently controlled audit rather than routine S1 execution/recovery is unresolved.
- Disturbance / variety regulated: False code-correctness/completion claims, failed commands or task defects.
- Decisive decision or feedback right: User-follow-up Action may select Runner; Runner consumes actual process results, and Patcher can generate corrections.
- Decision owner: Follow-up task agent/user; no separately mandated audit actor or sampling policy established.
- Supporting / enforcement mechanisms: `subprocess.run` exit status, repeated command execution, Rerunner prompt, Patcher, ProjectManager.
- Claim being audited: The generated project code operates correctly.
- Ordinary reporting path: Coder writes files and reports task completion to project/user.
- Complementary access path: A separate follow-up run executes actual code and sees process return status rather than only Coder's success text.
- Independence boundary: Separate task stage and raw process evidence are present, but no distinct sampling/audit authority over the producing operation is established.
- Who acts on findings: Rerunner/Patcher model can repair based on command failures, under a user-triggered follow-up.
- Closure path: Produced code → optional run → process failure → model patch/re-run; may be ordinary requested execution/repair, so cannot unambiguously credit S3*.
- Why this is / is not agent-owned: Actual code execution is independent evidence, but a routine code-run/check/repair loop is not automatically complementary S3* without organizational audit separation.
- Evidence: [src/agents/runner/runner.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/runner/runner.py#L70-L180); [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L195-L248); [src/agents/coder/coder.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/coder/coder.py).
- Basis: unknown
- Confidence: low
- Caveats: Further source-grounded adjudication of independently controlled sampling and corrective authority is needed before `C` or bounded `—`.

## S4 — Outside-and-then intelligence
- State: —
- Function: No longer-horizon system-capability adaptation controller driven by external environmental foresight found in shipped Devika task operation.
- Disturbance / variety regulated: Future opportunity/threat/capability changes beyond the present coding request are not an operational function in the assessed mode.
- Decisive decision or feedback right: Model selects immediate web research and coding plan, not prospective organizational capability redesign.
- Decision owner: No first-party S4 owner; user sets models/environment and Developer/CLI configuration.
- Supporting / enforcement mechanisms: Researcher, web search/browser, memory/RAG knowledge base, planning prompts and follow-up actions.
- Closure path: Task-related research → more relevant current code; no explicit future external option → adopted capability change returning to current operational system.
- Why this is / is not agent-owned: Web research and iterative planning are near-term S1 task capabilities rather than outside-and-then adaptation.
- Evidence: [src/agents/researcher/researcher.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/researcher/researcher.py); [src/agents/agent.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/agents/agent.py#L270-L365); [src/memory/knowledge_base.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/memory/knowledge_base.py); [src/browser/interaction.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/browser/interaction.py).
- Basis: structural
- Confidence: medium
- Caveats: Shipped generic web research differs from future-oriented organizational adaptation; no claim about third-party plugins.
### Absence scope
- Surfaces inspected: Researcher and search pipeline, knowledge-base/RAG reuse, Planner and Action, project persistence and browser autonomous interaction.
- Plausible first-party paths checked: environment scanning, adaptation option formulation, decision to alter future persistent tooling/skills/organization, and feedback into active operational capability.
- Why no material first-party path remains: research/search and memory are invoked for immediate requested tasks; no owner selects future strategic capability changes or installs them into ongoing agent organization.

## S5 — Policy and identity
- State: —
- Function: No first-party ultimate identity/policy decision-and-return function for a higher Devika organization shown in shipped central agent runtime.
- Disturbance / variety regulated: Operator trust/tool/model choice and permitted execution scope are controlled by static configuration and user APIs.
- Decisive decision or feedback right: User configures models and triggers projects and actions; no autonomous or parent S5 function governing organizational purpose is established.
- Decision owner: User/developer out of the evaluated one-agent boundary; deterministic host configuration does not own ultimate-policy judgments.
- Supporting / enforcement mechanisms: `src/config.py`, model provider selection, project creation, optional sandbox/Firejail and external service settings.
- Closure path: Static choices and per-task action bounds guide task execution; no purpose/identity challenge → policy decision → returned governance for ongoing organization.
- Why this is / is not agent-owned: Model configuration or sandboxing alone is not organizational identity or ultimate authority.
- Evidence: [src/config.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/config.py); [devika.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/devika.py); [src/project.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/project.py); [src/sandbox/firejail.py](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/src/sandbox/firejail.py).
- Basis: structural
- Confidence: medium
- Caveats: Human developer's out-of-scope organization may exercise S5, but not through a first-party supported parent mode here.
### Absence scope
- Surfaces inspected: config and provider policy, Flask API/project management, state and agent loop, sandbox/runner, user follow-up action handlers.
- Plausible first-party paths checked: team identity/purpose authority, revising policy decisions in response to organizational feedback, parent/human-governed ultimate-policy return loop.
- Why no material first-party path remains: only project/model/permission configuration and task-level user requests are reachable; no separate organizational purpose authority or policy-governance feedback path found.

## Recursion
At the declared first-party boundary, Devika is one model-driven operational coding agent whose specialized model-backed classes are internal tool-like subtasks. Independent users/threads and separately hosted provider models are outside the organizational recursion. No multi-unit metasystem is inferred from class names.

## Variety and escalation
Model-directed planning, web research and code writing absorb changing software requirements. Direct process execution can expose actual errors, and model-backed rerun/patch adapts current work when invoked. No cross-S1 contention, whole-current organizational control, prospective external intelligence or identity-level policy loop is established by the inspected first-party distribution.

## Evidence gaps
Static primary-source review of pinned revision only; no online provider execution. S3* is deliberately unknown because the actual subprocess error/patch path may be complementary but appears integrated into optional ordinary execution without a separately controlled audit right. All negative judgments are bounded to the enumerated inspected first-party session modes and document substantive absence scopes.
