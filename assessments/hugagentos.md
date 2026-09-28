---
harness_id: hugagentos
project_name: HugAgentOS
repository: https://github.com/ZJU-REAL/HugAgentOS
review_ref: 9436fcb77261bc995e6e7a45cdc5e192eae9bc74
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# HugAgentOS

## Review boundary

- System in focus: one supported HugAgentOS Community Edition deployment at pinned revision `9436fcb77261bc995e6e7a45cdc5e192eae9bc74`, including its FastAPI backend, AgentScope-backed ReAct runtime, first-party tool/sandbox/MCP integration, callable sub-agents, autonomous-loop driver/reviewer, memory/evolution paths, project context and supported background/automation surfaces.
- Purpose and identity: provide a local-first AgentOS in which model-driven agents perform substantive user/project work with tools, delegate bounded work to sub-agents, continue long-running tasks, preserve memory and expose controlled local/remote operation.
- Relevant environment: user/project files, configured LLM providers, MCP/external services, browser and command execution environments, sandbox state, user approval, task/project history and provider/tool failures.
- Standard-distribution boundary: public Community Edition code and ordinary supported opt-in capabilities present at the pinned revision. Enterprise-only or explicitly target-architecture surfaces are not used to establish a positive function merely because related public modules are present in the monorepo.
- Credited operating / distribution surfaces: ordinary chat/ReAct execution; callable sub-agent execution; the built-in autonomous-loop path and its read-only reviewer; project-scoped runtime and memory; Community Edition personal-evolution path where relevant to negative-boundary analysis.
- Adjacent first-party surfaces excluded from ownership: repository contributor organization, CI/release machinery, tests except as corroboration, future/target architecture, Enterprise-only fleet governance, ontology control-plane claims not shown to be a completed ordinary Community Edition operating path, and upstream AgentScope/provider internals.
- First-party operating / deployment modes considered: standard chat, project chat, callable sub-agent dispatch, autonomous long-running loop, supported background work and opt-in automation, personal memory/evolution.
- Recursion level: one HugAgentOS deployment/project is the system-in-focus. Model-driven main/sub-agent executions that own substantive task outcomes are S1 operations; lower-level tool calls are not separate S1s merely because they execute concurrently.
- Reviewed revision: `9436fcb77261bc995e6e7a45cdc5e192eae9bc74`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

HugAgentOS owns the first-party assembly around AgentScope's `ReActAgent`: request context, project/memory injection, prompt/tool surfaces, model/provider selection, sandbox/MCP execution, streaming, logging and persistent chat/project state. The resulting actor iterates reasoning, tool selection, observations and later actions, so the deployment contains a substantive model-driven S1 rather than only an evaluation shell or UI.

The same runtime exposes callable sub-agents. A dispatched child receives its own model context and can perform substantive delegated work through the same agent/tool machinery. The first-party `call_subagent` implementation deliberately executes each child in a separate worker thread with its own event loop because MCP/AnyIO cancellation scopes otherwise create cross-task runtime errors. This gives a narrow but concrete S2 path: distinct S1-capable children can interfere through shared asynchronous runtime mechanics; the constructor separates those scopes so subsequent child execution can proceed without sibling cancellation-scope corruption. Generic @mention routing, delegation and the thread pool are not credited by themselves.

Long-running autonomous work has an explicit driver-owned requirement ledger. The driver injects one unfinished requirement at a time, persists checkpoints/handoffs, enforces hard anti-runaway limits and asks a distinct reviewer before marking a requirement passed. Those mechanisms are strong task-level control, but at the selected deployment/project recursion they do not establish a separate whole-system current-control function over the portfolio of active S1 resources, commitments, priorities and synergy. The driver controls one bounded autonomous-loop line of work rather than acting as the deployment's S3.

Complementary audit is explicit in `orchestration/subagents/loop_reviewer.py`. The autonomous-loop worker may report completion, but the driver does not trust that report. It starts a different, read-only reviewer agent with the same project sandbox, gives it the requirement/acceptance criteria rather than the worker conversation, and requires it to inspect the real files/commands itself. `done` is accepted only with evidence and is independently checked again before the driver flips the requirement to passed; non-done findings feed later work. This closes S3* in a standard first-party path.

HugAgentOS also contains genuine adaptation machinery. Community Edition personal evolution mines one user's historical episodes, identifies repeated successful tool sequences, uses a semantic judge, creates candidate skills and can install an owner-approved private skill. This is real capability change, but its evidence source is the system's own historical operational episodes. It does not establish the Profile's distinct outside-and-then environmental model or a separate S3↔S4 current/future conversation, so it is not mapped to S4 here.

No qualifying S5 closure is established. Users/admins can configure models, agents, prompts, skills, approval modes and project context, and evolution candidates can require owner approval. These are meaningful configuration/governance controls, but the reviewed Community Edition boundary does not establish a distinct ultimate identity/policy function whose authoritative decision closes through an S5-specific organizational path rather than ordinary product configuration or per-capability approval.

## S1 — Operations

- State: A
- Function: perform substantive user/project work through model-driven iterative reasoning, tool use and observation-driven continuation.
- Disturbance / variety regulated: ambiguous tasks, changing project/file state, tool and service results, browser/command outcomes, model uncertainty and evolving user context.
- Decisive decision or feedback right: choose task-specific reasoning/tool actions and revise subsequent actions from returned observations until the bounded task/turn is complete.
- Decision owner: the model-driven ReAct actor assembled and executed through HugAgentOS's first-party runtime.
- Supporting / enforcement mechanisms: `orchestration/workflow.py`, `core/llm/agent_factory.py`, AgentScope integration, tool registry, sandbox/MCP execution, project/context/memory injection, streaming and approval controls.
- Closure path: user/project objective + assembled context → model-driven agent selects a tool/action → HugAgentOS executes it through the permitted tool/sandbox/service path → result returns to the agent → later model action changes in response → task/turn progresses to a substantive outcome.
- Boundary reachability: ordinary first-party chat/project/background paths instantiate the ReAct runtime directly; no contributor-only actor is required.
- Why this is / is not agent-owned: removing the model actor while retaining FastAPI, tools, persistence and sandbox leaves execution infrastructure but removes the task-specific discretionary action choice.
- Evidence: [`README.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/README.md); [`src/backend/orchestration/workflow.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/workflow.py); [`src/backend/core/llm/agent_factory.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/llm/agent_factory.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: AgentScope and model/provider internals are dependencies. `A` credits the model actor reached through HugAgentOS's supported first-party harness path, not organizational functions internal to those dependencies.

## S2 — Coordination

- State: C
- Function: attenuate a concrete runtime interference mode between concurrently dispatched S1-capable sub-agents by isolating each child's asynchronous execution/cancellation scope.
- Disturbance / variety regulated: multiple child agents using MCP/AnyIO machinery can otherwise place cancellation scopes across tasks/event loops and trigger cross-task runtime errors, disrupting sibling operation.
- Decisive decision or feedback right: determine the execution isolation boundary for each dispatched child so one sub-agent's asynchronous/cancellation lifecycle cannot corrupt another child's task scope.
- Decision owner: deterministic first-party HugAgentOS constructor/runtime policy in `call_subagent`; no autonomous coordination agent chooses this isolation relation.
- Supporting / enforcement mechanisms: dedicated `ThreadPoolExecutor`, one event loop per child thread, child execution/cancellation bridge, isolated MCP clients and inherited-but-separated agent runtime construction.
- Closure path: main agent dispatches distinct S1-capable children → potential shared async/MCP cancellation-scope interference is structurally separated by per-child thread/event-loop isolation → each child can continue its own tool/model lifecycle → results return independently to the parent for subsequent operation.
- Boundary reachability: `call_subagent` is a shipped first-party tool and the isolation is in its ordinary implementation at the pinned revision.
- Why this is / is not agent-owned: the anti-interference relation remains if the model agents are replaced; deterministic runtime code decides and enforces the per-child isolation boundary. Therefore S2 is constructor-owned `C`, not `A`.
- Distinct S1 units: concurrently dispatched main/child or multiple child model-driven agents capable of substantive delegated task work.
- Inter-S1 disturbance: cross-task AnyIO/MCP cancellation-scope interactions can produce runtime errors and interrupt sibling child execution when async lifecycles share an unsafe task boundary.
- Attenuating coordination relation: each child executes in its own worker thread with its own event loop and isolated MCP/client lifecycle, keeping cancellation scopes inside the task that owns them.
- Feedback into subsequent S1 behaviour: isolated children remain able to execute their later model/tool steps and return independent results to the parent instead of failing from sibling cancellation-scope corruption.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on a named cross-task failure mode and a specific first-party isolation mechanism added to remove that interference. @mention routing, delegation and the existence of a pool are not independently treated as S2.
- Evidence: [`src/backend/core/llm/subagent_tool.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/llm/subagent_tool.py); [`src/backend/orchestration/workflow.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/workflow.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a narrow technical coordination function at the assessed deployment recursion. It does not imply that all sub-agent routing, batching or delegation is S2.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established at the assessed deployment/project recursion.
- Disturbance / variety regulated: individual long-running loops regulate requirement progress, retries, checkpoints, reviewer findings, stalls and hard limits; automation/batch paths regulate their own jobs. These are lower-scope execution controls rather than a distinct deployment-wide S3.
- Decisive decision or feedback right: no qualifying whole-system current-control decision over the deployment's active operational resources, commitments, priorities or synergy is established.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: autonomous-loop requirement ledger, deterministic one-requirement-at-a-time driver, checkpoints, replan hooks, budget/runaway breakers, background task lifecycle, batch orchestration and user approvals.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: planner/worker/reviewer agents make bounded task decisions while deterministic drivers enforce one loop/job's progression. Neither demonstrates a separate agent-owned or constructor-owned whole-deployment S3 at the selected recursion.
- Evidence: [`src/backend/orchestration/autonomous_loop.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/autonomous_loop.py); [`src/backend/orchestration/batch_orchestrator.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/batch_orchestrator.py); [`README.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: at a narrower recursion one autonomous-loop driver is a strong controller of its own worker/reviewer process. This assessment deliberately does not lift that local task controller into deployment-level S3 without the Profile's whole-system control path.

### Absence scope

- Surfaces inspected: autonomous-loop driver and reviewer; batch orchestration; callable sub-agents; automation/background execution; task lifecycle; model/provider routing; approval and project/runtime context paths.
- Plausible first-party paths checked: requirement ledger as supervisor; planner/replanner as manager; automation scheduler; batch orchestrator; worker pool; background task manager; provider/model control; HITL approval surfaces.
- Why no material first-party path remains: the inspected mechanisms regulate one task, loop, dispatch or configured job, or expose local/operator controls. None establishes a distinct current whole-system view plus authority over the deployment/project's operational portfolio on behalf of the whole.

## S3* — Complementary audit

- State: A
- Function: independently verify whether a worker's claimed autonomous-loop requirement is actually implemented by inspecting the real project output through a separate read-only agent path, then return findings into correction.
- Disturbance / variety regulated: worker self-report can claim completion when the underlying files/output do not satisfy the requirement; ordinary worker conversation therefore can hide implementation defects or absent deliverables.
- Decisive decision or feedback right: inspect real produced files/command evidence independently and return `done`, `continue`, `off_track` or `need_human` for the requirement.
- Decision owner: the separate model-driven loop reviewer agent instantiated by the first-party autonomous-loop driver.
- Supporting / enforcement mechanisms: separate reviewer context, read-only capability policy, same project sandbox for direct artifact access, explicit acceptance criteria, structured verdict/evidence, first and independent second-pass review, persisted sub-agent logs and deterministic driver handling.
- Closure path: worker attempts requirement and produces files/summary → driver starts independent reviewer with requirement/criteria but not worker conversation → reviewer directly reads/searches/runs read-only checks against the actual project → findings/verdict return to driver → non-done findings guide subsequent worker action; only evidence-backed review lets the driver mark the requirement passed.
- Boundary reachability: `autonomous_loop.py` calls `review_requirement` in the standard autonomous-loop path at the pinned revision; the reviewer is a built-in first-class sub-agent rather than a development-only test fixture.
- Why this is / is not agent-owned: the substantive audit judgment is produced by a distinct model-driven reviewer. Deterministic read-only/tool restrictions and driver routing enforce the boundary but do not decide whether the output satisfies the requirement.
- Claim being audited: the worker's claim that the current requirement is complete and its produced project artifacts satisfy the requirement/acceptance criteria.
- Ordinary reporting path: worker summary, its ordinary model/tool trajectory and machine evidence generated during the work iteration.
- Complementary access path: separate reviewer agent personally opens/searches the same project sandbox and may run read-only commands rather than trusting the worker's summary.
- Independence boundary: reviewer and worker use distinct contexts/agent executions; the reviewer does not reuse the worker conversation, is explicitly read-only and is deterministically spawned by the driver rather than by the worker being judged.
- Who acts on findings: the autonomous-loop driver; `continue`/`off_track`/`need_human` feed the loop/replanning/escalation path, while only accepted evidence-backed completion permits the requirement ledger to advance.
- Evidence: [`src/backend/orchestration/autonomous_loop.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/autonomous_loop.py); [`src/backend/orchestration/subagents/loop_reviewer.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/subagents/loop_reviewer.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ontology committee/review code was not needed for this positive mapping. The credited S3* path is the directly reachable autonomous-loop reviewer, avoiding dependence on enterprise/target-architecture ontology surfaces.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established at the assessed deployment/project recursion.
- Disturbance / variety regulated: HugAgentOS can preserve memory, observe tools/services and adapt private capabilities from accumulated operational episodes, but the reviewed standard path does not maintain a distinct model of the outside/future environment and return adaptation choices through a separate current-control conversation.
- Decisive decision or feedback right: no qualifying S4 prospective adaptation judgment/feedback right is established.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: three-tier memory, project context, automation/triggers, personal evolution, historical-episode mining, semantic SOP judge, private skill candidates and owner approval.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: personal evolution genuinely changes capability, but it mines the user's own historical operating episodes for repeated successful patterns. That is internal learning from past operations, not enough by itself to establish Profile S4's external-and-prospective intelligence function.
- Evidence: [`src/backend/core/evolution/personal.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/evolution/personal.py); [`README.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: this negative finding does not deny that the product evolves. It distinguishes operational/history-driven capability adaptation from the specific outside-and-then organizational function required for S4.

### Absence scope

- Surfaces inspected: memory retrieval/storage; personal evolution and candidate promotion; automation/triggers; external tools/browser/MCP; project context; planner/replanning; ontology/runtime governance; model/provider configuration.
- Plausible first-party paths checked: evolving memory as S4; personal skill evolution as S4; automation/event reaction; external research tools; loop replanning; provider changes; ontology updates.
- Why no material first-party path remains: memory/evolution is grounded primarily in internal historical episodes; event-triggered work and external research remain S1 task execution unless connected to a distinct prospective adaptation function; no separate S3↔S4 current/future organizational conversation is established at the selected recursion.

## S5 — Policy and identity

- State: —
- Function: no material S5 identity/ultimate-policy closure is established for the assessed Community Edition deployment/project boundary.
- Disturbance / variety regulated: users/admins can configure agents, prompts, models, skills, approval modes, project context and accept private evolution candidates, but these controls do not by themselves establish the deployment's ultimate identity/policy function.
- Decisive decision or feedback right: no qualifying S5-specific ultimate identity/policy decision right is established.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: user agent definitions/system prompts, skill configuration, project instructions, platform configuration, human approval, personal-evolution candidate approval and capability/edition controls.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: configuration and approval surfaces alter particular agents/capabilities, but no reviewed standard path demonstrates a distinct ultimate-policy issue → legitimate S5 decision → authoritative identity/policy change → subsequent whole-system operation closure.
- Evidence: [`README.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/README.md); [`src/backend/orchestration/workflow.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/workflow.py); [`src/backend/core/evolution/personal.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/evolution/personal.py).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: this follows the Profile rule that prompts, generic human approvals and editable configuration are not automatically S5. A narrower recursion centered on one explicitly governed agent persona could pose a different question, but that is not the system boundary assessed here.

### Absence scope

- Surfaces inspected: agent/system-prompt configuration; skills and project context; model/provider configuration; approval modes; personal-evolution approval; Community/Enterprise edition boundaries; ontology policy/review code; admin/capability configuration.
- Plausible first-party paths checked: editable system prompt as policy; user-defined agent persona; project instructions; human approval; personal skill promotion; ontology packs as ultimate policy; platform admin configuration.
- Why no material first-party path remains: each inspected path is agent/task/capability configuration, lower-scope approval or an enterprise/target control-plane surface whose ordinary Community Edition closure is not established. None provides the required ultimate identity/policy closure for the selected deployment/project recursion.

## Distributed OSS parent arrangement

The public repository's maintainer/contributor organization is outside the assessed deployment boundary. Repository governance, release authority and enterprise product governance therefore do not donate S5 to a running HugAgentOS deployment.

## Self-hosted and non-human modes

HugAgentOS is local-first and supports remote/background operation. Human approval can constrain destructive actions and owners can approve private evolution candidates. Those controls are classified according to the functions they actually serve; generic HITL does not create S3/S4/S5 by itself.

## Recursion

A deployment can contain a main agent, multiple callable child agents, autonomous-loop worker/reviewer executions, automation jobs and tool subprocesses. This assessment treats substantive model-driven agents as S1 operations where they own bounded task outcomes. Nested processes are not automatically separate viable systems merely because they are spawned or concurrent.

## Variety and escalation

HugAgentOS attenuates operational variety with sandboxing, scoped tools/MCP, context management, explicit approvals, per-child runtime isolation, persistent loop ledgers and independent review. It amplifies response variety through multiple models, skills, sub-agents, browser/tool access and memory. Escalation appears in approval prompts, reviewer `need_human`, autonomous-loop hard guards and failed background work; these remain mechanisms within their mapped functions rather than standalone VSM functions.

## Evidence gaps

- S2 is intentionally narrow: it credits a documented cross-task cancellation-scope interference and first-party child isolation, not multi-agent naming, delegation, queues or parallelism generally.
- The autonomous-loop driver is powerful but remains a bounded task controller at this assessment recursion; no deployment-wide S3 is inferred from it.
- S3* is based on the standard loop reviewer path, not the ontology trust-control-plane target architecture.
- Personal evolution is acknowledged as real capability adaptation but is not promoted to S4 without external/prospective environmental distinction and an S3↔S4 organizational loop.
- No S5 is inferred from editable prompts, project instructions or owner approvals alone.
