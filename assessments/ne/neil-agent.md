---
harness_id: neil-agent
project_name: Neil-Agent
repository: https://github.com/zyohhh/Neil-Agent
review_ref: ae4919fe88b9da9f072697221f09cf081bb42d3f
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Neil-Agent

## Review boundary

- System in focus: the first-party installed Neil-Agent local coding assistant, including its Python model/tool loop, supported CLI/non-interactive/Web hosts, optional one-shot read-only child, operator interfaces and integrated security/runtime services.
- Purpose and identity: execute bounded local development and repository-exploration tasks using a configured model, repository tools, current instructions and user approvals.
- Relevant environment: requested code changes, local project files/Git state, model/provider results, workspace instructions, tool failures, operator decisions, optional Windows Sandbox, and transient child research requests.
- Standard-distribution boundary: the frozen v0.1.0 Python package and bundled Web interface at commit `ae4919fe88b9da9f072697221f09cf081bb42d3f`, Python >=3.13. The configured external inference provider and optional certified OS sandbox supply services, not independent first-party governance owners.
- Credited operating / distribution surfaces: `src/neil_agent/agent.py`, `host_runtime.py`, `subtask.py`, `tools/subtask.py`, `task.py`, `cli.py`, `noninteractive.py`, `web/controller.py`, `web/service.py`, `tools/`, `skills.py`, `instructions.py`, `security.py`, `audit.py`, `approval.py` and shared session/event/configuration machinery.
- Adjacent first-party surfaces excluded from ownership: contributor instructions for agents developing the Neil-Agent repository, `DevelopmentRecords.md`, project roadmap, external comparative reviews, evaluation fixtures, benchmark runners, unit tests, CI and release operations. Development and testing actors do not become organizational functions inside an end user's installed coding session.
- First-party operating / deployment modes considered: interactive CLI; one-shot non-interactive read/write; local Web Workbench; `standard`, `web-safe`, `benchmark-minimal` and one-shot `readonly-subtask` runtime profiles; Web human control and model switching; optional security observation, audit, skill loading and workspace project-instruction modes.
- Recursion level: one installed coding session and any bounded read-only model subtask it instantiates; not a shared governing organization spanning separate installations or upstream contributors.
- Reviewed revision: `ae4919fe88b9da9f072697221f09cf081bb42d3f` (batch #1011 frozen row 9).
- License screen: root `LICENSE` grants MIT.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`build_host_runtime()` registers workspace tools, narrowly scoped Git/shell operations, plan and skill tools, permission/approval hooks, and optionally a certified Windows command tool. `Agent.stream_chat()` feeds first-party tool schemas and results into a configurable model and repeats decisions until response or bounded stop. CLI, non-interactive and Web entries use this common assembly, with distinct operator/session semantics. For CLI/Web standard modes, the model can invoke `run_readonly_subtask`, which constructs a new model-driven `Agent` using `RuntimeProfile.READONLY_SUBTASK`: read-only filesystem operations, a finite deadline, limited invocations and tool rounds, then a bounded result returned synchronously to the parent. There is no durable multi-worker scheduling, arbitration, shared-write collaboration or standalone child control plane in the shipped mode.

`TaskTracker` stores one current sequential plan and latest quality-check result, but is not a manager of a current cohort of independent operations. Web `WorkbenchController` owns one active turn, a control lease, human cancellation, tool-approval requests and session switching; the snapshot/review panels project current task, Git changes, check reports and security status. `SecurityShield` and `project_security_boundary_watch` deterministically monitor/flag posture differences; neither directly adjudicates coding claims or sends independent findings to an enforcement/correction owner. Workspace `AGENTS.md`, `load_skill` and model allowlists supply current configuration/context rather than prospective organizational adaptation or identity-policy arbitration.

Frozen primary source: [agent loop](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/agent.py), [host runtime](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/host_runtime.py), [child runtime](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/subtask.py), [Web controller](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/web/controller.py), [runtime profile design](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/docs/runtime-profile.md).

## Operational model

The parent `Agent` is the ordinary S1 coding unit: it chooses read/write/review/check actions from model observations. The one-shot read-only child has its own short model/tool loop for delegated exploration, but returns synchronously through one parent tool invocation. No in-boundary controller dynamically coordinates peer operational interference, governs the current whole of competing agent commitments, conducts a separately deciding complementary operational audit, acquires prospective external capabilities, or decides ultimate identity policy. Human acceptance, UI status, cancellation, security instrumentation and project-supplied skills are important support mechanisms but require function-specific decision ownership and returned closure before positive S3/S3*/S4/S5 publication.

## S1 — Operations

- State: A
- Function: produce local coding/repository investigation outcomes through model-selected tools and revisions in response to returned evidence.
- Disturbance / variety regulated: changed user requirements, differing repository state, tool approval refusals, failing quality checks, errors and provider/tool responses.
- Decisive decision or feedback right: model responses choose actual registered file/Git/quality-check/child-exploration tools and subsequent action from resulting tool feedback.
- Decision owner: configured parent inference model, and an independent model invocation within each optional one-shot read-only child.
- Supporting / enforcement mechanisms: `ToolRegistry`, `HostRuntime`, security approvals, limited tool rounds, bounded context, project instructions, model adapters and session persistence.
- Closure path: request and active workspace context → model tool choice → real or denied tool result → next model response/action or completion. The read-only child similarly explores files and returns a bounded report to the parent.
- Boundary reachability: CLI, Web and non-interactive hosts instantiate `Agent` with registered production tool schemas; CLI/Web standard hosts additionally register and run the model-facing read-only subtask tool.
- Why this is / is not agent-owned: the model selects task-relevant operations and repairs; runtime permission checks enforce constraints but do not choose the coding solution.
- Evidence: [Agent](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/agent.py), [tool registry](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/tools/registry.py), [host runtime](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/host_runtime.py), [subtask](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/subtask.py).
- Basis: direct frozen first-party executable paths plus deterministic native mocks.
- Confidence: high for model-operated S1 construction, not live coding success.
- Caveats: no live provider call or LLM quality experiment was run; capabilities depend on selected profile and operator permissions.

## S2 — Coordination

- State: —
- Function: a substantive inter-S1 conflict/oscillation attenuation relation is not established in the standard supported mode.
- Disturbance / variety regulated: a parent and an optional read-only exploration child could need consistent results and bounded resource use, but the child is one-shot, synchronous and never competes for writable workspace ownership; no evidenced concurrent peer S1 write conflict is regulated.
- Decisive decision or feedback right: parent may delegate a read-only research question; developer-configured profile restricts child tools, invocations, duration and budgets. Neither is an S2-specific inter-worker adjustment decision.
- Decision owner: parent model for delegation; fixed runtime for the read-only limits.
- Supporting / enforcement mechanisms: `RuntimeProfile.READONLY_SUBTASK`, child deadline/cancel, parent linkage, filtered tool registry and bounded returned summary.
- Closure path: child exploration results return to the parent tool call; no separate first-party coordination response regulating an evidenced interaction between multiple simultaneously acting S1s.
- Why this is / is not agent-owned: the independent child is genuine S1-style operation, but delegation, one-way result passing and static capability restriction do not by themselves close coordination among competing work cells.
- Evidence: [subtask](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/subtask.py), [subtask tool](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/tools/subtask.py), [profile registration](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/host_runtime.py).
- Basis: frozen source control flow, explicit one-shot design and relevant offline tests.
- Confidence: medium-high within supported shipped modes.
- Caveats: one could build a multi-agent coordinator using future extensions, but that is not the current installed topology.

### Absence scope

- Surfaces inspected: host/agent/subtask construction and tool registration, execution budget/cancel, task plan, Web controller/observer, runtime profiles and related tests/docs.
- Plausible first-party paths checked: read-only child fan-out as S2, sequential task plan as shared scheduling, event/subtask parent IDs as mutual feedback, per-turn invocation limits as coordination, and Web one-turn lease as conflict prevention.
- Why no material first-party path remains: each is task delegation, serialized one-turn control, fixed permission/resource enforcement or observability; no evidenced cross-S1 interference-specific attenuation with coordination result returned into later peer behaviour exists.

## S3 — Inside-and-now control

- State: —
- Function: no separately owned current whole-system management/control loop over distinct operational commitments is established.
- Disturbance / variety regulated: stuck turns, approvals, stale sessions and limited context are present, but the user-facing controller supervises one active turn rather than bargaining and intervening over the whole current set of independently committed S1s.
- Decisive decision or feedback right: Web user can cancel the active turn and approve a preview-bound tool action; model can update its own single-task plan. Neither decision governs a whole current operational portfolio.
- Decision owner: human over the single active Web turn/approval, task model over its own step order, fixed runtime for limits and lease enforcement.
- Supporting / enforcement mechanisms: `WorkbenchController` control lease, `cancel_turn`, current-state snapshot, `TaskTracker`, child cancel propagation and CLI status/cockpit views.
- Closure path: local stop/approve/deny changes the one task's execution; a whole-current portfolio view → supervisory commitment/resource choice → returned cross-unit regulation path is not present.
- Why this is / is not agent-owned: substantive coding choices remain S1, while operator stop/approval and a deterministic one-turn lease lack the broader current-management function required for S3=P or S3=A.
- Evidence: [Web controller](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/web/controller.py), [task tracker](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/task.py), [host matrix](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/docs/host-runtime.md).
- Basis: frozen command/controller paths and native tests.
- Confidence: medium-high for bounded negative at this recursion.
- Caveats: a user can exercise external managerial judgment over multiple manually launched installations, but that is not wired into this installation's first-party whole-current loop.

### Absence scope

- Surfaces inspected: Web controller/DTO and snapshot services, CLI status/cockpit, activity DAG, task plan, host resource capabilities, child lifecycle and operator cancellation.
- Plausible first-party paths checked: `cancel_turn` as parent S3=P, Web control lease as allocation, `set_task_plan` as model S3=A, live dashboard/current security posture as whole-system view and child budgets as S3 enforcement.
- Why no material first-party path remains: each scope is one foreground turn or delegated one-shot child, and none closes a separate whole-of-current-operations decision across competing S1 commitments.

## S3* — Complementary audit

- State: —
- Function: no independently judging complementary audit of ordinary coding claims with a control return is established in the shipped session.
- Disturbance / variety regulated: faulty code and security boundary degradation can be made visible, but quality checks, raw Git reviews and security posture signals are fixed test/observation functions rather than a separate auditing judgment actor.
- Decisive decision or feedback right: the parent model optionally invokes tests; Web UI presents Git diff and latest check outcome; `SecurityShield` projects runtime safeguards and deterministic warnings. No independent auditor makes a coding verdict that enters corrective supervision.
- Decision owner: task model/user for ordinary checks and any voluntary manual review; fixed projection routines for security warnings.
- Supporting / enforcement mechanisms: `run_quality_check`, `WorkbenchSnapshotService.review`, security boundary observation/alerts, audit JSONL, events and checkpoints.
- Closure path: reports and alerts are displayed or given back to the same task flow; no separately warranted complementary audit finding → separate corrective authority → changed subsequent work chain is shipped.
- Why this is / is not agent-owned: access to Git diff and security evidence can inform a person, but neither tracing nor deterministic display constitutes a distinct material audit judgment and return.
- Evidence: [Web service/review](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/web/service.py), [security boundary watch](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/security.py), [task/quality status](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/task.py).
- Basis: direct audit/review/security projection paths.
- Confidence: medium for bounded negative.
- Caveats: a manually composed independent reviewer could consume the UI, but no such separate first-party auditor/decision loop is packaged.

### Absence scope

- Surfaces inspected: Web Review Git diff/quality metadata, `run_quality_check`, security boundary watcher, JSONL audit hooks, events, sandbox certification, evaluation scripts and readonly-subtask policy.
- Plausible first-party paths checked: Web Review as raw independent evidence, `SecurityShield` downgrade alerts as complementary audit, test/eval fixtures as reviewer, read-only child as potential fresh verifier and tamper-evident/rotating logs as evidence of separate findings.
- Why no material first-party path remains: none is an exposed separately deciding/auditing authority that reaches operational reality independently and returns findings to a corrective control circuit; child prompts focus on repository exploration, not auditing prior worker claims.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported agent-owned or operationally closed parent-owned prospective environmental sensing → adaptation alternatives → adopted present-capability change circuit.
- Disturbance / variety regulated: provider/tool changes and future tasks could require adaptation, but current mechanisms configure sessions or load existing local instructions/skills.
- Decisive decision or feedback right: the task model can `load_skill` from a pre-existing user workspace; an attending Web user can switch among a fixed same-provider allowlist while idle; neither develops or adopts prospective external alternatives.
- Decision owner: operator for allowed runtime selection and external skill provisioning, ordinary task model for opportunistic context loading.
- Supporting / enforcement mechanisms: workspace instructions, `SkillTools`, runtime profiles, sessions/compaction, `runtime_models` and model-switch transaction checks.
- Closure path: an existing local skill is read into present tool context or a configured model is selected; no autonomous or parent-governed external/future distinction → option generation → capability adaptation loop was found.
- Why this is / is not agent-owned: task planning, context retention and installing nothing new through skill reading are not future-facing organizational intelligence.
- Evidence: [skill loader](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/skills.py), [skill tool](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/tools/skills.py), [Web controller](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/web/controller.py), [profile roadmap](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/docs/runtime-profile.md).
- Basis: frozen current-mode wiring and explicit non-goals.
- Confidence: medium-high for bounded negative.
- Caveats: future planned optional session goals and Plan DSL are development ideas, not shipped evidence at this ref.

### Absence scope

- Surfaces inspected: project instruction initialization/hot reload, local skills, model/provider switching, runtime profiles, memory/compaction, roadmap and task plans.
- Plausible first-party paths checked: local `load_skill` as capability adoption, model allowlist switching as parent S4=P, user AGENTS.md updates as strategic learning, context checkpoints as adaptation and optional roadmap phases as shipped S4.
- Why no material first-party path remains: these react to current user/operator configuration or retain task context; no present first-party path actively distinguishes external futures, develops options and returns a selected adaptive capability to operations.

## S5 — Policy and identity

- State: —
- Function: no internal or parent-returned ultimate policy/identity decision loop exists at the local installed-harness boundary.
- Disturbance / variety regulated: actions may threaten safety boundaries or user expectations, but current approvals/security limits govern individual operations rather than authoritative reconsideration of the system's purpose or identity.
- Decisive decision or feedback right: user approves/rejects individual tool previews, developers define fixed path and runtime safety rules; no identity-level issue is escalated to a separately recognized ultimate authority and fed back as a governing decision.
- Decision owner: user/developer for static preferences, permissions and host configuration, not a shipped S5 institution.
- Supporting / enforcement mechanisms: `ApprovalStore`, `sensitive_paths`, sandbox/certification checks, `SecurityShield`, model allowlists, project instructions and audit hooks.
- Closure path: tool action → security/approval check → action allowed/denied, with no identity/policy dispute → legitimate ultimate authority → governing return to future operation.
- Why this is / is not agent-owned: constraints and even reported boundary downgrade alerts are monitoring/enforcement, not ultimate constitutional choice.
- Evidence: [approval](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/approval.py), [sensitive paths](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/sensitive_paths.py), [security](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/security.py), [instruction scope](https://github.com/zyohhh/Neil-Agent/blob/ae4919fe88b9da9f072697221f09cf081bb42d3f/src/neil_agent/instructions.py).
- Basis: source-enforced first-party trust/approval/identity boundaries.
- Confidence: medium-high for bounded negative.
- Caveats: the operator remains the legitimate external owner of what work to request, but ordinary action approval does not constitute S5=P.

### Absence scope

- Surfaces inspected: permission binding, OS/app security constraints, runtime profiles, system/project prompts, Web lease/approval, model selection, security watcher, audit and public development governance.
- Plausible first-party paths checked: manual tool approval as S5=P, Web model switching as identity decision, project instructions as a constitution, security downgrade alerts as policy escalation and upstream maintainers as distributed parent S5.
- Why no material first-party path remains: none routes an actual identity/ultimate-policy matter to a legitimate within-boundary decision holder and returns that ruling into subsequent governance. Upstream maintainers govern product development, a separate recursion from the installed user session.

## Distributed OSS parent arrangement

The upstream repository may be maintained by several independent human contributors, and users can run separate local installations. No first-party session boundary joins their private execution state or delegates current/governing decisions to the public development organization. Repository contributor instructions and evaluation practices are not credited as operational S3/S4/S5 parent modes.

## Self-hosted and non-human modes

The human Web/CLI operator can stop or approve individual actions, inspect raw Git diffs and choose a configured model; these are important first-party supervision/support surfaces but do not close the broader S3/P, S4/P or S5/P function tests. The model does autonomously select coding operations (S1=A), while the child is a bounded task-specific read-only assistant rather than a higher independent metasystem.

## Recursion

The parent coding Agent and one-shot read-only child have independent model-driven tool loops and bounded local tasks; spawning a child alone does not establish its self-sustaining metasystem or recursively viable organization. The unit of publication remains the local installed session.

## Variety and escalation

Tool failures, rejected previews, quality-check results and scoped instructions enter the next S1 decision; a child summary expands local investigation without a peer conflict-control loop. Security boundary degradation reaches a status panel and human perception but no autonomously corrective audit/governance circuit. Routine exceptions are handled in S1 or by tactical human authorization.

## Evidence gaps

- Frozen SHA `ae4919fe88b9da9f072697221f09cf081bb42d3f`; native Python 3.13.16, pinned `uv.lock` environment. **211 deterministic offline test cases PASS** across 16 tracked files: agent (34), read-only subtask (16), host runtime (20), skills (10), task (8), security (17), approval (15), audit (9), context (19), context projection (2), runtime events (8), security projection (2), non-interactive mode (17), runtime models (2), offline eval (10), Git security (22). No live LLM/provider runs.
- The entire frozen 59-file offline test suite did **not** complete in a bounded 120-second run (timed out after approximately 32% progress). An additional multi-file subset also timed out, and the large tracked `tests/test_web_workbench.py` did not finish within a separate 25-second per-file bound. Passing entire native suite or model quality is **not** claimed.
- Switching the fresh clone from its newer default HEAD to the frozen revision left untracked newer-branch files (including `execution_journal`, `evaluation/` and newer tests); all source and reported test files were selected from `git ls-files` at the frozen revision. These untracked files are not credited as the shipped frozen runtime.
- The positive S1 conclusion is an executable model/tool control-path claim supported by mocked tests, not evidence of successful autonomous code repair in production.
- Bounded negative results account for shipped Web Review and security posture monitoring rather than assuming a missing function from component names alone.
