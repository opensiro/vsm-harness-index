---
harness_id: edict
project_name: Edict
repository: https://github.com/cft0808/edict
review_ref: 14a207557719c046af0f993a7bff1cc5a5015b33
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Edict

## Review boundary

- System in focus: Edict's **full OpenClaw-installed** multi-role task execution, not its no-OpenClaw dashboard demo or a hypothetical stand-alone model runtime.
- Purpose and identity: Turn a user's edict into a reviewed plan, ministry work allocation and completed deliverables through specialized agent roles with dashboard-visible state.
- Relevant environment: Open-ended user instructions, incomplete plans, risk and feasibility uncertainty, heterogeneous execution work, absent evidence, unavailable OpenClaw agents and stalled tasks.
- Standard-distribution boundary: The first-party installer copies bundled `SOUL.md` roles and agent permission matrix into an **already installed external OpenClaw runtime**, and ships task/state update scripts, dashboard, status sync and operational start scripts. Decision-making model loops are run by external OpenClaw and its configured models; Edict supplies deliberate first-party specialization and feedback integration.
- Credited operating / distribution surfaces: [full-install boundary](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/README_EN.md#L190-L217), [actual role/workspace installer](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L92-L184), [role-to-role review and feedback](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/menxia/SOUL.md#L1-L87), [model-directed assignment of ministries](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/shangshu/SOUL.md#L1-L59), [task transition script](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/scripts/kanban_update.py).
- Adjacent first-party surfaces excluded from ownership: Docker demo image and `docker/demo_data` fixtures that can display simulations without a real OpenClaw agent; screenshots/GIF and scripted demos; experimental/deployable separate `edict/backend` Redis/Postgres event workers not launched by the documented legacy `start.sh`; local tests, benchmarks, CI, project maintainer governance, and external OpenClaw's own autonomous systems beyond the installed configured roles.
- First-party operating / deployment modes considered: Installed OpenClaw with role workspaces/allowed subagent calls, synchronized file-backed Kanban and dashboard; optional external provider/model choice; Docker demo-only dashboard; separately packaged experimental/backend Redis dispatch stack. Positive ownership uses the installed composed OpenClaw role mode, not demo data or unverifiable backend availability.
- Recursion level: One user-issued edict with planning/review/assignment and separately acting ministry S1 units; not the entire OpenClaw vendor fleet or Edict's independent contributors.
- Reviewed revision: `14a207557719c046af0f993a7bff1cc5a5015b33`, pinned in [#2012](https://github.com/opensiro/vsm-harness-index/issues/2012) and [#2013](https://github.com/opensiro/vsm-harness-index/issues/2013).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The installer checks for an existing OpenClaw CLI/config, creates dedicated agent workspaces, copies distinct first-party department `SOUL.md` role prompts, registers an `allowAgents` delegation matrix and synchronizes data and cross-session visibility. In the ordinary `start.sh` path, a status-refresh loop starts only if OpenClaw is found, alongside a local Python dashboard. Otherwise the dashboard is explicitly read-only; Docker can display a simulated showcase without operating real agents. These boundaries matter: Edict **composes** model-backed roles but does not implement its own independent language-model runtime. [installer](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L31-L47), [agent registration](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L124-L185), [start/no-OpenClaw behavior](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/start.sh#L54-L96), [demo disclaimer](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/README_EN.md#L43-L56).

Edict also includes a more explicit Redis Streams event-state pipeline (`edict/backend/`): it maps task states to agent dispatch, forwards messages to `openclaw agent`, retries failures and includes per-agent semaphores/duplicate-task suppression. That code is an alternative implementation surface, **not proof that the documented standard `start.sh` exercises it**. No agentic function is credited solely from this worker's type names or recovery policy. [event orchestrator](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/edict/backend/app/workers/orchestrator_worker.py#L1-L67), [dispatcher](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/edict/backend/app/workers/dispatch_worker.py#L370-L415).

## Operational model

In the installed role mode a human issues a bounded goal. An external OpenClaw model runs the installed Taizi/Zhongshu roles to classify and decompose the task; the separate Menxia role audits the proposed plan, and a rejected plan returns to Zhongshu. Once admitted, the Shangshu model selects executing departments, delegates work and gathers their results through OpenClaw's configured subagent calls. Edict's scripts record flow/progress/state for visibility and another agent step. The fixed permission matrix restricts which roles may call which; it does not by itself own any of those decisions. [overview](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/docs/task-dispatch-architecture.md#L27-L104), [review](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/menxia/SOUL.md#L1-L87), [execution](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/shangshu/SOUL.md#L1-L68).

## S1 — Operations

- State: A
- Function: Execute a scoped ministry task (engineering, docs, analysis, testing or infrastructure) and return an observed outcome.
- Disturbance / variety regulated: Tool and code errors, variable repository state, incomplete outputs and other task-specific uncertainties.
- Decisive decision or feedback right: A supported installed model-backed ministry agent chooses task actions/tools and adjusts behavior after observations and results.
- Decision owner: The model-backed installed OpenClaw ministry agent; Edict supplies its bundled role and task-state interface, not the external model runtime's entire governance.
- Supporting / enforcement mechanisms: Installed role `SOUL.md`, OpenClaw agent workspace, subagent permission matrix, file-backed task/log commands and progress reporting.
- Closure path: Assigned task → ministry agent tool work and observation → further action or completion → returned result and Edict task/progress state.
- Boundary reachability: `install.sh` packages role prompts and configures the existing OpenClaw agents; ministry roles and delegation are an explicit supported full-install workflow.
- Why this is / is not agent-owned: Choices of implementation, testing and task-specific actions are model-directed in the composed installed mode; deterministic state files and dashboard do not themselves make choices.
- Evidence: [installer roles](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L92-L184), [work allocation and return contract](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/shangshu/SOUL.md#L20-L60), [one ministry role](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/bingbu/SOUL.md).
- Basis: Shipped provider-composed agent feedback/action mode.
- Confidence: Medium-high for install path and role capability; no live task execution measured.
- Caveats: Running the demo-only Docker dashboard does not yield this state.

## S2 — Coordination

- State: —
- Function: No distinct closed first-party cross-ministry interference attenuation path is established beyond role assignment and fixed task routing at the reviewed installed recursion.
- Disturbance / variety regulated: Multiple ministry S1 workers could duplicate edits, compete for tools or produce incompatible changes, but a clear inter-S1 conflict detector and feedback resolution mechanism is not shown in the credited mode.
- Decisive decision or feedback right: Not established as S2-specific in the first-party installed path. The model-backed Shangshu assigns **what** to each ministry at S3, and the gate reviews plans; ordinary messages and permissions do not show a conflict-driven coordinator relation.
- Decision owner: No separate S2 owner evidenced. Experimental Redis dispatch semaphores are mechanical agent/task capacity and duplicate-delivery control, not autonomous inter-S1 conflict judgment.
- Supporting / enforcement mechanisms: Department jurisdiction table, subagent `allowAgents` matrix, task/flow logs, status board and optional event-worker per-agent semaphore.
- Closure path: Normal delegation and collection return to Shangshu, but no demonstrated cross-S1 interference signal → resolution → changed sibling operations is independently closed.
- Why this is / is not agent-owned: A division of ministries, shared data and an execution queue are not sufficient under Methodology 0.3.7 without the specific inter-S1 disturbance witness.
- Evidence: [ministry routing](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/shangshu/SOUL.md#L16-L43), [fixed OpenClaw permissions](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L135-L150), [separate backend dispatch limit](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/edict/backend/app/workers/dispatch_worker.py#L387-L402).
- Basis: Bounded negative: role routing is not independently evidenced S2 conflict attenuation.
- Confidence: Medium.
- Caveats: User-specific OpenClaw subagent extensions might implement stronger conflict management; those are not attributed to Edict.

### Absence scope

- Surfaces inspected: Role prompts, installer permission matrix, main scripts/dashboard workflow, optional Redis dispatch worker and routing docs.
- Plausible first-party paths checked: Specialized ministry assignment, OpenClaw allowed-call restrictions, event-worker per-agent semaphore and duplicate-task discard, progression through Menxia review.
- Why no material first-party path remains: None inspected explicitly observes *interaction-generated conflict between distinct operating ministries* and returns a first-party attenuating decision to change sibling S1 behavior; the alternatives are routing, single-agent capacity/retry or plan review.

## S3 — Inside-and-now control

- State: A
- Function: Govern current commitments of one edict by selecting ministry assignments, monitoring their progress and deciding how to integrate or re-dispatch current work.
- Disturbance / variety regulated: Heterogeneous workload, partially finished ministry outputs, misassigned tasks, missing results and current delivery failures.
- Decisive decision or feedback right: The installed model-backed Shangshu dispatch role decides which ministries undertake subtasks and how to respond to their results; the planning role can revise the current plan after gate rejection.
- Decision owner: The composed OpenClaw Shangshu/Zhongshu control actors, distinct from the fixed transition script and operator dashboard.
- Supporting / enforcement mechanisms: Plan/todo state, assigned ministries, shared task files, progress reports, allowAgents, dashboard status and OpenClaw subagent call return.
- Closure path: Whole-edict task/plan view → selected dispatch across specialized S1 cells → progress/results from ministries → Shangshu synthesizes and returns to Zhongshu/user or requests further work.
- Boundary reachability: The first-party installer wires all referenced roles and their allowable delegations; bundled Shangshu instructions explicitly require progress inspection, assignment and aggregate response.
- Why this is / is not agent-owned: Selection of the department portfolio for a particular edict is agent discretion; predetermined state ordering and dispatch event handling are only carriers.
- Whole-system current view: The edict's agreed plan, department task assignments, cross-ministry progress updates and result summaries under one edict ID; not every independent deployment or organization-wide roadmap.
- Current-control decision scope: Departmental resource commitments, who acts now, synthesis and return of ongoing work, plus bounded recovery/replanning of the same edict.
- Evidence: [Shangshu current-control instructions](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/shangshu/SOUL.md#L1-L67), [role composition](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L135-L150), [task-state map](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/edict/backend/app/models/task.py#L15-L87).
- Basis: Shipped control-role discretion returned into current multi-ministry activity.
- Confidence: Medium; no actual model-driven portfolio decision was tested.
- Caveats: Scope is one edict, not project-level whole-portfolio S3. Manual stop/cancel/resume does not separately justify `(P)`.

## S3* — Complementary audit

- State: A
- Function: Audit proposed operational plan claims independently of the planning actor before releasing the task to execution.
- Disturbance / variety regulated: Unworkable steps, missing subtasks, underestimated risks and inaccurate planning assumptions.
- Decisive decision or feedback right: The separately configured Menxia review agent decides to approve (`准奏`) or veto (`封驳`) and return concrete corrective objections; rejection routes back to Zhongshu.
- Decision owner: Model-backed Menxia agent in a separate installed OpenClaw role/workspace, not the Zhongshu planner whose claims it audits.
- Supporting / enforcement mechanisms: Review rubric, command to return task state to Zhongshu or advance to Assigned, flow logs, allowAgents and finite retry guidance.
- Closure path: Zhongshu plan → Menxia's separate feasibility/completeness/risk/resource inspection → veto/approval → re-planning or authorized execution.
- Boundary reachability: Menxia workspace and role are installed by the standard script and permitted in the Zhongshu delegation chain; its `SOUL.md` gives executable board/return commands.
- Why this is / is not agent-owned: Menxia owns the plan-quality verdict, while transition scripts only record/enforce the chosen result. Reviewer independence is role/workspace and contrary authority, not proven unrelated model weights or institution.
- Claim being audited: The planning department's proposed decomposition is sound and executable.
- Ordinary reporting path: Zhongshu writes planning steps/todos and presents its proposed scheme.
- Complementary access path: Separate Menxia role reviews the proposal under feasibility, completeness, risk and resource criteria and writes its own review result.
- Independence boundary: Different installed agent identity, workspace, prompt and assigned role, with explicit veto even against the planner. It remains inside the same operator/provider ecosystem.
- Who acts on findings: Zhongshu revises after a veto; approvals permit Shangshu to allocate work.
- Evidence: [Menxia audit criteria and executable veto](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/menxia/SOUL.md#L1-L87), [first-party role installation and permissions](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L92-L150), [process architecture](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/docs/task-dispatch-architecture.md#L53-L101).
- Basis: A distinct review actor judges another controller's operational claim with direct return to the current control cycle.
- Confidence: Medium; prompt-described veto is not a measured runtime guarantee.
- Caveats: Menxia instructions **force approval on the third review round**; that seriously bounds the integrity of the gate and must not be described as an unconditional permanent veto. No live review efficacy study.

## S4 — Outside-and-then intelligence

- State: —
- Function: No evidenced first-party loop that turns sensed external/future environmental changes into adopted future delivery-system capability decisions.
- Disturbance / variety regulated: Emerging models, news, tooling and external requirements; the separately bundled news official can collect world/AI headlines, but news delivery is not yet an adaptation decision for Edict's task organization.
- Decisive decision or feedback right: No S4-specific actor with option/adoption authority evidenced. User-triggered model changes and routine retrospective task choices remain separate paths.
- Decision owner: Humans manually choose model assignments and skills; the brief agent selects news items, not Edict's future operating strategy.
- Supporting / enforcement mechanisms: News briefing official, headlines script, dashboard model selection, skill management and change application/restart script.
- Closure path: News → digest for emperor does not show prospectively developed organizational options → authoritative adoption → changed future capability. Directly applying a user's selected model is configuration, not external intelligence.
- Why this is / is not agent-owned: Even a model-produced daily external digest need not constitute S4 unless its distinctions influence a future-oriented capability/strategy decision.
- Evidence: [news brief role](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/agents/zaochao/SOUL.md#L1-L49), [operator model-change script](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/scripts/apply_model_changes.py#L43-L113).
- Basis: Bounded negative after inspecting plausible external-sensing and future-change surfaces.
- Confidence: Medium-high.
- Caveats: Another external workflow could consume the daily brief and choose organizational adaptations, but none is shown as an operating first-party Edict mode.

### Absence scope

- Surfaces inspected: News/brief roles, planning and ministerial prompts, model/skill configuration dashboard, change-apply script and task recovery scheduler.
- Plausible first-party paths checked: Global news digest, technology updates, recommended model changes, administrative model swap, current plan revisions and learned rules.
- Why no material first-party path remains: The news output is informational and prospective capability choice is missing; configuration changes come from separate operator selection, not a connected intelligence → option → adopted strategic adjustment loop.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy dispute handling and authoritative returned decision is established at the user-edict organization recursion.
- Disturbance / variety regulated: Disagreement over organizational mandate, legitimacy or immutable operating principles might arise, but installed role permissions handle delegation and task scope instead.
- Decisive decision or feedback right: No actual ultimate-policy right exercised through a first-party agent or human parent escalation workflow is shown. The Emperor/user issues objectives and can intervene operationally, not evidenced identity-policy settlements.
- Decision owner: Outside operator sets initial requirements, role allowlists and model preferences; no first-party S5-specific governing channel.
- Supporting / enforcement mechanisms: Role permission matrix, separation-of-powers prompts, dashboard stop/cancel/resume, task final approval and local OpenClaw configuration.
- Closure path: These mechanisms change one task or allowlist, but no identity-level conflict → legitimate authority → ultimate decision → standing subsequent policy loop is supplied.
- Why this is / is not agent-owned: Invoking imperial titles, vetting one plan or applying an operational safety rule does not establish governance of organizational identity.
- Evidence: [installer permissions](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/install.sh#L135-L150), [README intervention feature](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/README_EN.md#L59-L123), [task transition model](https://github.com/cft0808/edict/blob/14a207557719c046af0f993a7bff1cc5a5015b33/edict/backend/app/models/task.py#L24-L58).
- Basis: Bounded absence of identity/ultimate-policy closure, including parent path.
- Confidence: Medium-high.
- Caveats: An external human institution operating Edict may legitimately maintain S5, but the integration is not shown in these supported role/board paths.

### Absence scope

- Surfaces inspected: Emperor/dashboard intervention, all role descriptions, OpenClaw allowlists, task transitions, administration and backend recovery code.
- Plausible first-party paths checked: Human final acceptance, STOP/cancel/resume, role veto, hard delegation matrix and model/skill configuration.
- Why no material first-party path remains: All inspected decisions concern current task authorization, personnel routing or runtime setup, not an escalated organizational identity dispute with legitimate binding higher-order resolution.

## Distributed OSS parent arrangement

Edict's GitHub contributors maintain the project, while users run isolated OpenClaw-based deployments. The package does not give project maintainers identity-level control over users' live edict organizations; public release governance is not imported as parent S5. A user issuing/accepting edicts is operational parent input but no qualifying separately closed S3/S4/S5 `(P)` mode is inferred from isolated UI actions.

## Self-hosted and non-human modes

Edict supports a local installation with a user's existing OpenClaw agent runtime and self-hosted dashboard. Model-backed execution is possible under the installed role mode; the Docker/no-OpenClaw simulated dashboard is not a non-human organization or live agent test. Explicit separation of six ministry workspaces does not by itself guarantee successful independent model reasoning or noninterference.

## Recursion

Ministry agents perform S1 tasks; Shangshu conducts bounded S3 across the ministries for one edict, with Menxia supplying complementary audit of the planner before assignment. Edict's entire contributor community, the upstream OpenClaw platform and national/government analogies are outside the selected operational recursion.

## Variety and escalation

An execution difficulty returns to the ministry agent, planning omissions to Menxia → Zhongshu, delivery assignment/aggregation to Shangshu, and task-level intervention to the human. No distinct cross-ministry collision-management path or future environmental-capability/ultimate-policy mechanism is established by that succession of role labels.

## Evidence gaps

- No live OpenClaw/model/provider or dashboard interaction was run. Role behavior is inferred from installable first-party configuration and source; effectiveness, compliance with prompts and independent review accuracy are unmeasured.
- The new Redis worker code is inspected but is not represented as running under ordinary `start.sh`; optional backend deployment wiring has not been independently demonstrated here.
- Menxia's third-round forced approval weakens veto integrity. Positive S3* describes availability of a contrary actor/return path, **not** unlimited rejection authority or independent evaluative reliability.
- A different user's additional OpenClaw plugins may add S2/S4/S5 paths; external additions are outside the frozen first-party credited mode.
