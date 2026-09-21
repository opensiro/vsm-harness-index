---
harness_id: yuxi
project_name: Yuxi
repository: https://github.com/xerrors/Yuxi
review_ref: 86c67dc41249c3c9cad9e976fd8a006194d39a76
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Yuxi

## Review boundary

- System in focus: one deployed Yuxi knowledge-agent platform installation at frozen revision `86c67dc41249c3c9cad9e976fd8a006194d39a76`, including its first-party ChatbotAgent runtime, run/request lifecycle, SubAgent middleware and state, workspace/sandbox/tool/Skill/MCP integration, memory, approval and multi-tenant control surfaces.
- Purpose and identity: provide self-hosted multi-user knowledge agents that perform tool-backed work over enterprise/user knowledge and can delegate bounded work to configured Yuxi subagents.
- Relevant environment: users and departments, knowledge/document stores, external websites/services and MCP tools, model providers, sandbox/filesystem state, scheduled work and administrator/operator configuration.
- Standard-distribution boundary: Yuxi-owned FastAPI/worker services, `backend/package/yuxi` runtime, built-in ChatbotAgent/SubAgent machinery, persistent AgentRun state, workspace/sandbox integration and shipped middleware. LangGraph/DeepAgents, external model providers, MCP servers, PostgreSQL/Redis/Milvus/Neo4j and external knowledge/services are dependencies rather than inherited organizational owners.
- Credited operating / distribution surfaces: `backend/package/yuxi/agents/base.py`, built-in chatbot graph/state, `agents/middlewares/subagent_task.py`, AgentRun/request worker paths documented in `ARCHITECTURE.md`, configured first-party filesystem/tool middleware and runtime context.
- Adjacent first-party surfaces excluded from ownership: knowledge/RAG evaluation dashboards, administrative CRUD/configuration, observability/audit timelines, deterministic lease/queue recovery and human approval are inspected as mechanisms but not promoted to VSM functions without function-specific closure.
- First-party operating / deployment modes considered: ordinary ChatbotAgent runs with configured first-party tools; optional configured Yuxi SubAgents executing child AgentRuns; persistent threads/checkpoints; default or always-trust tool-approval mode; optional memory/Skills/MCP/knowledge capabilities.
- Recursion level: one Yuxi root-agent run plus Yuxi-owned subordinate AgentRuns inside one installation. The root operation is S1; separately running child agents may be additional S1 units when delegated real work. The root's portfolio control is assessed separately as S3; their mere plurality is not S2.
- Reviewed revision: `86c67dc41249c3c9cad9e976fd8a006194d39a76`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Yuxi is not only a UI around LangGraph. Its first-party services persist user requests and AgentRun records, dispatch runs to an owned worker lifecycle, prepare Yuxi runtime context and then execute the configured built-in agent graph. `ChatbotAgent` constructs the model/tool graph with Yuxi filesystem, Skills, memory, SubAgent, summary, retry, steering, usage and approval middleware and a Yuxi-owned PostgreSQL-backed checkpointer.

The SubAgent path is especially relevant organizationally. A configured root agent receives four first-party lifecycle tools: `subagent_start`, `subagent_status`, `subagent_cancel` and `subagent_await`. Starting a child creates a durable child AgentRun related to the parent. Tool results update the root LangGraph state with `subagent_runs`; that state retains run identity, agent identity, status, timestamps, errors, artifacts and result/event URLs. The root can therefore observe live subordinate commitments and decide whether to create, wait for, inspect or cancel them before finalizing its own result. The shipped prompt explicitly tells the root to start independent tasks, continue its own work, query/cancel them when needed, await required results, and avoid ending while required child work remains unresolved.

That is credited as current-control S3, not as S2: the implementation regulates the live portfolio of child commitments but does not establish a specific interference/oscillation relation among distinct child operations plus a dedicated attenuation loop. Human approvals, queue leases and same-thread exclusion likewise remain enforcement/parent mechanisms.

## Operational model

A normal request is persisted as an AgentRunRequest and dispatched to a Yuxi worker, which obtains the run lease, prepares the configured agent context and executes the Yuxi-built LangGraph. The model chooses substantive tool steps from current observations and can use filesystem, knowledge, Skill/MCP and sandbox-backed operations according to configuration.

When SubAgents are available, the same root model can distribute independent work into child AgentRuns. Each start/status/cancel/await action returns structured feedback into root state. Subsequent root decisions therefore condition on current child execution state and results, and parent completion cancels still-live child runs. The control loop is inside the normal shipped execution path rather than a downstream application that must invent portfolio control.

## S1 — Operations

- State: A
- Function: perform user-directed knowledge, analysis and artifact-producing work through a first-party model/tool execution loop.
- Disturbance / variety regulated: heterogeneous user requests, retrieved knowledge, files/workspace state, tool/API results, sandbox execution outcomes, model/tool errors and changing conversation/task context.
- Decisive decision or feedback right: select substantive next actions/tools and decide when available operational evidence is sufficient to continue, delegate or return a result.
- Decision owner: the running Yuxi model agent.
- Supporting / enforcement mechanisms: Yuxi `ChatbotAgent`, configured runtime tools, composite filesystem/sandbox backend, checkpointer, request/run worker lifecycle, retries, context summarization, Skills/MCP and knowledge integration.
- Closure path: persisted request → prepared Yuxi agent graph → model-selected tool/action → first-party execution → ToolMessage/observation → subsequent model decision → final persisted result.
- Boundary reachability: the standard Yuxi API/worker path directly instantiates and executes `ChatbotAgent`; no downstream custom harness is required to obtain the model/tool operational loop.
- Why this is / is not agent-owned: LangGraph executes graph mechanics and external providers supply model inference, but the model actor owns the discretionary operational choices while Yuxi owns the executable loop, tools/context and durable run path.
- Evidence: [`ARCHITECTURE.md`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/ARCHITECTURE.md), [`backend/package/yuxi/agents/base.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/base.py), [`backend/package/yuxi/agents/buildin/chatbot/graph.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/buildin/chatbot/graph.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic LangGraph/DeepAgents capabilities not assembled and exposed by Yuxi are not inherited.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes attenuation of a concrete interference, conflict or oscillation among at least two distinct Yuxi S1 units.
- Disturbance / variety regulated: not established as S2 at the reviewed recursion.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: child AgentRun lifecycle, same-thread no-concurrent-write rule, FIFO request queues, run leases, shared runtime/workdir, parent cancellation and delegation exist but are not credited as coordination by topology or serialization alone.
- Closure path: not applicable.
- Why this is / is not agent-owned: the root can manage child commitments, but evidence inspected does not identify a concrete cross-child disturbance and an S2-specific attenuation relation whose feedback changes subsequent child behavior.
- Evidence: [`ARCHITECTURE.md`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/ARCHITECTURE.md), [`backend/package/yuxi/agents/middlewares/subagent_task.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/middlewares/subagent_task.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: shared workspaces can create potential interaction, but potential collision is not evidence that Yuxi ships a concrete S2 attenuation loop.

### Absence scope

- Surfaces inspected: root/child AgentRun state, same-thread busy handling, FIFO request dispatch, run leases, shared Workdir/runtime, parent-child cancellation and SubAgent lifecycle tools.
- Plausible first-party paths checked: delegation as S2; same-thread serialization as S2; request FIFO as S2; child-run hierarchy as S2; shared workspace controls as S2.
- Why no material first-party path remains: these surfaces serialize, dispatch, isolate or control execution but do not establish the Methodology-required distinct-S1 disturbance → attenuation → feedback relation.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current portfolio of subordinate Yuxi agent commitments during a root-agent run.
- Disturbance / variety regulated: incomplete, delayed, failed, unnecessary or still-running subordinate tasks; changing need for specialist work as child results arrive; risk of finalizing while required delegated work remains unresolved.
- Decisive decision or feedback right: decide what child work to start, inspect current child status/progress, await results when needed, cancel a child, continue root work in parallel and condition subsequent commitments/finalization on current child state and returned results.
- Decision owner: the root Yuxi model agent.
- Supporting / enforcement mechanisms: Yuxi SubAgent middleware; durable parent/child AgentRun relation; `subagent_start`, `subagent_status`, `subagent_cancel`, `subagent_await`; `ChatBotState.subagent_runs`; child ownership verification; cancellation/request services; persistent run/result state.
- Closure path: root identifies current need → starts one or more configured subordinate operations → child run state/result returns as ToolMessage plus `subagent_runs` state → root inspects/awaits/cancels/launches further work as current conditions require → subsequent root action/final answer changes accordingly; remaining live children are cancelled when parent ends.
- Boundary reachability: standard configured ChatbotAgent construction automatically installs the SubAgent middleware whenever visible/configured Yuxi subagents exist; the root receives the current-control tools directly in its normal model loop.
- Whole-system current view: the root graph state accumulates structured summaries for each child run keyed by `run_id`, including current status, agent identity, timing/error/artifact/result fields; explicit status/await calls refresh individual commitments before the root acts.
- Current-control decision scope: start new subordinate commitments, continue prior child threads when idle, inspect their progress/results, wait for required completion, cancel no-longer-wanted work and decide whether the root can safely finalize.
- Why this is / is not agent-owned: repositories/services enforce ownership and durable state, but the root model decides which current commitments exist and how their live evidence changes ongoing portfolio action. Removing the model leaves lifecycle mechanics but no discretionary whole-run allocation/control decision.
- Evidence: [`backend/package/yuxi/agents/buildin/chatbot/graph.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/buildin/chatbot/graph.py), [`backend/package/yuxi/agents/buildin/chatbot/state.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/buildin/chatbot/state.py), [`backend/package/yuxi/agents/middlewares/subagent_task.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/middlewares/subagent_task.py), [`ARCHITECTURE.md`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/ARCHITECTURE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this mapping is conditional on the standard supported mode with configured/visible SubAgents; a single-agent configuration still retains S1 but does not instantiate a multi-unit portfolio.

## S3* — Complementary audit

- State: —
- Function: no material first-party path establishes a sufficiently independent complementary challenge to operational reality with corrective return into S1/S3.
- Disturbance / variety regulated: not established as S3*.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: model/tool audit events, Langfuse integration, run/debug timelines, knowledge/RAG evaluation, human tool approval, retries and child status/results all exist but serve ordinary execution, evaluation or parent governance.
- Closure path: not applicable.
- Why this is / is not agent-owned: child outputs are production inputs to the root, not a structurally independent audit channel; dashboard/evaluation evidence does not by itself exercise corrective operational authority; human approval is Parent intervention rather than S3*.
- Evidence: [`ARCHITECTURE.md`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/ARCHITECTURE.md), [`backend/package/yuxi/agents/tool_approval.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/tool_approval.py), [`backend/package/yuxi/agents/middlewares/subagent_task.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/middlewares/subagent_task.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a separately configured reviewer subagent could be constructed downstream, but role naming or constructibility is not a shipped independent audit closure.

### Absence scope

- Surfaces inspected: AgentRun model/tool audit stream, Langfuse hooks, RAG/agent evaluation surfaces, human approval middleware, child result/status paths, retries and persistent history.
- Plausible first-party paths checked: subagent as independent reviewer; evaluation dashboard as S3*; audit logs as S3*; approval as S3*; retries/error checks as S3*.
- Why no material first-party path remains: no standard-distribution path establishes organizationally independent operational-reality access plus a distinct challenge judgment that returns into corrective S1/S3 action.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path establishes autonomous or parent-governed prospective environment-facing adaptation of Yuxi organizational capability.
- Disturbance / variety regulated: not established as S4.
- Decisive decision or feedback right: not established for prospective capability adaptation.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: knowledge/RAG retrieval, persistent checkpoints, user Memory, dynamically activated Skills, configurable models/tools/MCP and reusable agent/subagent definitions broaden available capability but do not themselves decide and integrate a future organizational adaptation from environmental distinctions.
- Closure path: not applicable.
- Why this is / is not agent-owned: the memory middleware explicitly writes long-term memory only when the user asks it to remember; Skills are selected/configured resources and dynamic activation occurs within the present run. Persistence/reuse is not prospective S4 closure.
- Evidence: [`README.md`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/README.md), [`backend/package/yuxi/agents/middlewares/memory.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/middlewares/memory.py), [`backend/package/yuxi/agents/middlewares/skills.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/middlewares/skills.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: administrators/users can change knowledge, agent, Skill, MCP and model configuration, but generic external configuration does not establish Parent-governed S4 without a qualifying S4 issue/option/decision/return path.

### Absence scope

- Surfaces inspected: user Memory, knowledge/RAG and graph pipelines, Skills activation/dependencies, model/tool/MCP configuration, agent/subagent definitions, checkpoints/history, evaluation surfaces.
- Plausible first-party paths checked: memory as learning; RAG/knowledge growth as S4; dynamic Skill activation as S4; administrator extension as parent S4; evaluation results as adaptation input.
- Why no material first-party path remains: inspected paths retain information or expose/configure capabilities, but do not close a prospective environment distinction → adaptation option → legitimate decision → changed future organizational capability loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party path establishes identity- or ultimate-policy-level adjudication that closes unresolved present/future tension for the Yuxi organization.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: not established for identity/ultimate policy.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: multi-tenant RBAC, administrator configuration, agent prompts/descriptions, tool approval mode, model/resource visibility and human approvals constrain operation.
- Closure path: not applicable.
- Why this is / is not agent-owned: these are access/configuration and parent safety controls. The reviewed repository does not establish a function-specific identity/ultimate-policy issue and an authority that adjudicates it and returns the decision into operation.
- Evidence: [`README.md`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/README.md), [`ARCHITECTURE.md`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/ARCHITECTURE.md), [`backend/package/yuxi/agents/tool_approval.py`](https://github.com/xerrors/Yuxi/blob/86c67dc41249c3c9cad9e976fd8a006194d39a76/backend/package/yuxi/agents/tool_approval.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: super-admin/operator authority is real product governance but does not become VSM S5 without the identity/ultimate-policy organizational function.

### Absence scope

- Surfaces inspected: user/department/admin RBAC, agent/model/tool/Skill/MCP configuration, tool approval, prompts/descriptions, team-management and dashboard controls.
- Plausible first-party paths checked: admin as S5; RBAC as S5; human approval as parent S5; agent prompt/persona as identity S5; team policy as S5.
- Why no material first-party path remains: all inspected paths configure or constrain operation rather than adjudicate an identified ultimate-policy/identity tension through a qualifying S5 closure loop.

## Overall finding

Yuxi is a first-party autonomous knowledge-agent harness rather than merely a LangGraph wrapper. Its built-in agent loop closes S1, and its shipped SubAgent lifecycle gives the root model genuine inside-and-now portfolio control: child commitments have durable status/state, and the model can start, inspect, await and cancel them before deciding subsequent work or finalization. That supports S3=A.

The surrounding mechanisms do not justify additional positive functions. FIFO/leases/thread exclusion are execution controls rather than demonstrated S2 attenuation; audit/evaluation/approval surfaces lack an independent corrective S3* path; Memory/RAG/Skills provide persistence and configurable capability without prospective S4 closure; and RBAC/prompts/admin authority do not establish S5 identity/ultimate-policy adjudication.

**Proposed autonomy vector:** `A — A — — —`.
