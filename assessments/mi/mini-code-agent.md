---
harness_id: mini-code-agent
project_name: Mini-Code-Agent
repository: https://github.com/ccxxxyy/mini-code-agent
review_ref: ee8c4339b0dd04088377f0c27e04abc1bf9904b9
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Mini-Code-Agent

## Review boundary

- System in focus: the first-party Mini-Code-Agent Python terminal/headless/optional remote coding assistant, including its independently deciding child agents, team planner, local supervision commands, skill loader, memory and audit logger.
- Purpose and identity: carry out developer coding tasks through a model/tool loop, optionally decompose work among model-driven specialized children and permit operator-controlled resource/intervention modes.
- Relevant environment: user requests, repository files and conflicting edits, tests/tool failures, concurrent child agents, parent/peer messages, review conditions, operator controls and cross-session remembered preferences.
- Standard-distribution boundary: pinned PyPI-compatible v1.1.0 local install; credited code is exactly tracked under frozen `ee8c4339b0dd04088377f0c27e04abc1bf9904b9`. External model endpoints, tmux/Windows Terminal availability and Git are required infrastructure for selected modes, not independent first-party decision owners.
- Credited operating / distribution surfaces: `src/mini_agent/app.py`, `core/agent_loop.py`, `core/subagent.py`, `core/team.py`, `core/planner.py`, `core/agent_types.py`, `security/worktree.py`, `extensions/builtin_commands.py`, `tools/builtin/spawn_agents.py`, `core/mailbox.py`, `memory/`, `extensions/skills.py`, `tools/builtin/install_skill.py`, `security/audit.py` and runtime UI.
- Adjacent first-party surfaces excluded from ownership: repository benchmarks and experiments, documentation, contributor/CI/release files, developer tests/mocks, later-branch leftovers in the checkout and independently run provider services. An upstream author's development practice does not become the locally installed harness's metasystem.
- First-party operating / deployment modes considered: model-driven primary and child loops; `spawn_agents` model-selected isolation/background/type; `/team` model-written dependency plan with per-step write permissions; `/spawn --isolated` and local worktrees; `/spawn list` and `/spawn cancel <id>` human current-control path; typed fresh `verify` child; cross-agent mailbox; automatic preference memory extraction/consolidation; optional `install_skill` and operator plugin/skill configuration.
- Recursion level: one installed Mini-Code-Agent session/project plus its spawned independent S1 coding cells; not the entire upstream open-source development community or separate users' installations.
- Reviewed revision: `ee8c4339b0dd04088377f0c27e04abc1bf9904b9` (batch #1011 frozen row 8).
- License screen: root `LICENSE` grants MIT.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The primary `AgentLoop` invokes model-backed tools and revises actions from tool/event feedback. `SubAgentManager` can spawn independently deciding `SubAgent`/pane workers with separate conversations, tool subsets, budgets and optional inherited context. The model-facing `spawn_agents` tool chooses one or more child tasks, optional background operation, agent type and Git-worktree isolation. `AgentTeam` asks an independent model-backed `Planner` to assign roles, file-write flags and task dependencies; it batches ready independent steps, withholds write tools from read-only research children and passes dependency reports to later steps. Optional worktrees prevent multiple writable cells from directly overwriting the same tree; Git integration/conflicts are not automatically semantically reconciled.

The operator-facing `/spawn list` shows the entire active child cohort and `/spawn cancel <id>` or cancel-all terminates selected current commitments. The model-facing `spawn_agents` tool does not expose an equivalent list/cancel decision right, so this is a bounded parent-governed S3 mode (`P`), not S3=A. The `verify` agent type instantiates a separate read-only model loop with a verdict-specific prompt, `synthetic_output` structured findings and returned task report; it is a function-specific complementary audit constructor, but a mandatory finding-to-correction circuit is not shipped. Memory extraction, durable skill installation, session state, action audit logs and per-tool permissions are distinct from future-capability governance or ultimate identity-policy ownership.

Frozen primary evidence: [agent loop](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/agent_loop.py), [subagent manager](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/subagent.py), [team](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/team.py), [planner](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/planner.py), [agent types](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/agent_types.py), [operator commands](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/extensions/builtin_commands.py).

## Operational model

Primary and child model loops choose real coding/tool actions (`S1=A`). For a distinct multi-writer interference class, the primary model can select `spawn_agents(isolated=true)` or a model-decomposed dependency/isolation team, and gets results that can change subsequent delegation (`S2=A`, bounded to intentionally selected protected paths). An attending user sees the current whole-child roster and selectively cancels a child commitment through `/spawn` commands (`S3=P`); no identical current-control model tool is shipped. A fresh specialized verifier offers a bounded independent audit constructor (`S3*=C`). Automatic memory and a model-callable skill installer do not themselves demonstrate an external/prospective adaptive decision loop (`S4=—`); approvals, security audit and prompt identity are not ultimate governing authority (`S5=—`).

## S1 — Operations

- State: A
- Function: execute developer operations using model-decided reading, patching, shell, search, task and optionally delegated child-agent actions.
- Disturbance / variety regulated: changing code/user goals, test and tool failures, permission denials, child/peer reports and varying repository state.
- Decisive decision or feedback right: each `AgentLoop` selects and revises substantive tool operations from observed results; child models own their bounded local operational decisions.
- Decision owner: configured primary model and separately instantiated child models.
- Supporting / enforcement mechanisms: tool registry, async streaming, sandbox/permission manager, context compression, memory retrieval, event bus, tool result cache and differentiated child policies.
- Closure path: task/context → model-selected tool calls → actual tool result/denial → feedback event/conversation → next model decision or completion.
- Boundary reachability: `Application` constructs the primary loop and tool registry; `SubAgentManager` instantiates independent `AgentLoop` children for `/spawn`, model `spawn_agents` and `/team` in shipped modes.
- Why this is / is not agent-owned: model-backed loops select task-specific action and repair, unlike fixed enforcement and scheduling code.
- Evidence: [AgentLoop](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/agent_loop.py), [SubAgent](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/subagent.py), [application](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/app.py).
- Basis: frozen executable source and mock-driven script tests.
- Confidence: high for actual agent operating construction; not a live capability benchmark.
- Caveats: provider calls and real model outcomes were not executed; one native subagent test hung under the local runner.

## S2 — Coordination

- State: A
- Function: regulate interference between concurrently deciding read/write child agents and dependent coding steps by model-selected isolated workspace and planned dependency boundaries.
- Disturbance / variety regulated: parallel worker file collisions, premature execution before dependent research is complete and competing modifications of a shared repository tree.
- Decisive decision or feedback right: the primary model selects the `isolated` option and delegated work topology through `spawn_agents`; model-backed `Planner` selects per-step `depends_on`/`writes_files`, while the runtime enforces separate worktrees/read-only tool restrictions and dependency batches.
- Decision owner: primary and planning models for coordination choices, deterministic `SubAgentManager`, `AgentTeam` and `WorktreeManager` for execution/enforcement.
- Supporting / enforcement mechanisms: per-child Git worktrees, read-only child tool filtering, independent child task scheduling, dependency result gates and returned child/merge reports.
- Closure path: potential overlap/dependency → model chooses isolation/ordered plan → independent S1s execute in bounded trees/batches → output/failure and dependency reports return to parent → subsequent task assignment can change.
- Boundary reachability: shipped model tool `spawn_agents` exposes `isolated=true`, which passes `isolation='worktree'` to `SubAgentManager`; `/team` creates model-backed `Planner` plus team batches and passes dependency results to later workers.
- Why this is / is not agent-owned: selecting isolation and cross-task dependencies is discretionary model judgment, while worktree creation, tool filtering and dependency checks enforce the selected relation. This is optional and not an unconditional guarantee of global conflict-free merging.
- Evidence: [spawn tool](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/tools/builtin/spawn_agents.py), [team](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/team.py), [planner](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/planner.py), [worktree](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/security/worktree.py).
- Basis: direct frozen coordination paths and isolated mock/team/worktree tests.
- Confidence: medium-high for the bounded model-selected coordination choice and enforcement.
- Caveats: defaults permit non-isolated children; dependency planning can make poor choices and Git branch integration remains a separate source of unresolved conflicts.
- Distinct S1 units: independent model-backed `SubAgent`/pane workers running separate conversation/tool loops.
- Inter-S1 disturbance: overlapping edits in one repository tree and tasks attempted before prerequisites complete.
- Attenuating coordination relation: model-selected worktree isolation plus planned dependency batches and automatic removal of write tools from read-only team members.
- Feedback into subsequent S1 behaviour: child results and prior-step outputs enter the next team prompt or primary `spawn_agents` tool result; interference/error signals can change later work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: code explicitly changes the file-write collision topology and prevents dependency-violating/write-unauthorized peer execution rather than merely forwarding messages.

## S3 — Inside-and-now control

- State: P
- Function: provide the legitimate local operator a whole-current roster of spawned agent commitments and targeted intervention control.
- Disturbance / variety regulated: stuck, obsolete or competing-priority background children continuing to use finite time and tool/model resources.
- Decisive decision or feedback right: an attending user invokes `/spawn list`, decides which active child should stop, and calls `/spawn cancel <id>` or cancel-all.
- Decision owner: human operator as parent for the current session; fixed `SubAgentManager.cancel` implements the selected stop.
- Supporting / enforcement mechanisms: `list_active`, `get_status`, `active_snapshots`, current-agent progress board and cancel hooks propagated to child `AgentLoop`.
- Closure path: whole-current list/phase → human chooses specific running agent → `/spawn cancel <id>` → `SubAgentManager.cancel` aborts its loop/task → changed active roster/remaining commitments.
- Boundary reachability: `Application` wires the manager into first-party slash commands; `/spawn list` and `/spawn cancel <id>` are direct regular installed command handlers, independent of optional external governance.
- Why this is / is not agent-owned: the human operator decides a whole-current intervention, while the manager enforces it. The model-facing `spawn_agents` can create children and receive results, but has no equivalent first-party current full-roster/selective-cancel tool; hence P, not A(P).
- Evidence: [slash commands](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/extensions/builtin_commands.py), [manager roster/cancel](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/subagent.py), [progress UI](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/ui/board.py).
- Basis: first-party human current roster/action path and deterministic command tests.
- Confidence: medium-high for bounded session control.
- Caveats: human supervision is optional and requires attention; resource budgeting outside active child roster and independent installations is not proven.
- Whole-system current view: `/spawn list` enumerates every active child id and phase in the current session; the board displays current child snapshots and progress.
- Current-control decision scope: operator-selected cancellation of one or all current child agent commitments, changing ongoing work rather than merely gating an isolated file edit.

## S3* — Complementary audit

- State: C
- Function: provide a separate read-only model-run verifier to inspect a stated condition and issue an independent structured PASS/FAIL verdict.
- Disturbance / variety regulated: incorrect or incomplete claims from normal coder output that ordinary model self-reporting or passing task actions can overlook.
- Decisive decision or feedback right: an optional `verify` child independently reads code/runs read-only checks, calls `synthetic_output` with verdict/failures and returns its report; the parent/operator is free to act on it.
- Decision owner: separately instantiated verification model for its judgment; user/parent for optional invocation and follow-through.
- Supporting / enforcement mechanisms: distinct `verify` type prompt, restricted read-only tool list, isolated child conversation, `synthetic_output` extraction and `SubAgentResult.structured_output`.
- Closure path: user/parent selects `verify` child → separate source inspection and structured verdict → returned child output → possible parent/user correction. No mandatory or universally automatic correction gate is enforced.
- Boundary reachability: `agent_type='verify'` is a shipped `spawn_agents` input and `/spawn --type verify` command option; `SubAgent` selects `get_agent_type` policy/tools and extracts the structured result from its own transcript.
- Why this is / is not agent-owned: the auditor's model owns a distinct evidence-based verdict rather than merely formatting the coder's report, but independent audit→enforced current-control corrective closure needs explicit composition; therefore C rather than A.
- Evidence: [types/verify prompt](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/agent_types.py), [child tool/structured output](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/core/subagent.py), [spawn tool](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/tools/builtin/spawn_agents.py).
- Basis: directly exposed first-party verifier constructor, source-enforced tool restriction and offline type tests.
- Confidence: medium for meaningful optional independent review construction, not reviewed model quality.
- Caveats: reviewer is not necessarily institutionally/provider independent; a user-defined code-review skill or hash-chain audit log alone is not promoted to S3* and no mandatory audit-controlled repair was observed.
- Claim being audited: condition or correctness claim about the working project and its implementation.
- Ordinary reporting path: primary worker's own tool observations, edits/tests and completion summary.
- Complementary access path: a fresh child conversation with read-only code/tool access and a verdict-specific synthetic output instruction.
- Independence boundary: distinct child inference/context and enforced read-only policy; no organizational independence or separate provider required.
- Who acts on findings: parent/model or human may initiate repair after receiving the returned report; no first-party mandatory veto/correction obligation is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no complete agent-owned prospective external sensing, option development and adopted future-capability return loop is established.
- Disturbance / variety regulated: future tool/model/skill changes could require adaptation, but current mechanisms mainly provide session context, user configuration and task-specific retrieval.
- Decisive decision or feedback right: main agent can invoke `install_skill` for a supplied local/Git source, but no shipped autonomous prospective adaptation choice or external/future scan is connected to this as an organizational loop.
- Decision owner: operator or present-task model for explicit skill install and project preferences, fixed memory extraction/consolidation for session context retention.
- Supporting / enforcement mechanisms: `MemoryExtractor`, `MemoryConsolidator`, skill registry, `install_skill`, plugin loading and `/skill` commands.
- Closure path: user/agent may install an existing skill or extract explicit user preferences into memory; no outside-and-future distinction → adaptation alternatives → first-party adoption judgment → changed continuing capability circuit is evidenced.
- Why this is / is not agent-owned: automatic extraction of user-stated preferences is not future capability selection; a generic model-callable skill installer does not alone own the prospective judgment about which external capabilities the organization should acquire.
- Evidence: [memory extractor](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/memory/extraction.py), [consolidation](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/memory/consolidation.py), [skill install](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/tools/builtin/install_skill.py), [skills](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/extensions/skills.py).
- Basis: inspected first-party durable-memory/skill paths and their authority boundary.
- Confidence: medium for bounded negative; a stronger shipped prospective policy could change classification at a newer pinned ref.
- Caveats: skill installation materially changes available runbooks, but source acceptance and requested installation alone are not sufficient evidence for a complete adaptive S4 owner.

### Absence scope

- Surfaces inspected: session memory extraction, consolidation scheduling/recall, skills and plugin discovery/installation, model/provider config, child-agent and planning tools, operator commands.
- Plausible first-party paths checked: LLM preference extraction as learning, `install_skill` as model autonomy, `/skill install` as parent S4=P, team planning as long-horizon strategy and user-maintained plugins as future capability change.
- Why no material first-party path remains: these retain task/user context, execute current requested installations or support current task plans; no first-party prospective environment/options/adoption loop is established at this boundary.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate identity/policy decision institution and returned governing loop is established for a local Mini-Code-Agent deployment.
- Disturbance / variety regulated: ultimate purpose and legitimate cross-objective tradeoffs remain operator/developer choices external to the shipped current runtime governance.
- Decisive decision or feedback right: operator sets tactical permissions/model modes and developer rules; no separate highest-policy authority decides identity-level issues and governs later lower-system choices.
- Decision owner: user for local tool permissions/identity hints and upstream maintainers for software design, not an installed S5 body.
- Supporting / enforcement mechanisms: PermissionManager, mode rules, OS sandbox, sensitive path restrictions, append-only hash-chain action audit and prompt instructions.
- Closure path: action request → allow/ask/deny or audit record → task proceeds/fails; no identity-level policy issue → ultimate authority → return affecting organizational purpose.
- Why this is / is not agent-owned: recording tamper-evident tool actions or checking file permission is accountability/enforcement infrastructure, not deciding what the organization is ultimately for.
- Evidence: [permissions](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/security/permission.py), [audit log](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/security/audit.py), [app wiring](https://github.com/ccxxxyy/mini-code-agent/blob/ee8c4339b0dd04088377f0c27e04abc1bf9904b9/src/mini_agent/app.py).
- Basis: policy/identity and audit runtime paths inspected.
- Confidence: medium-high.
- Caveats: the operator legitimately governs local work, but shipped controls do not form S5=P without the ultimate-policy loop.

### Absence scope

- Surfaces inspected: permissions, plan/default/bypass modes, sensitive path/OS sandbox, hash-chain audit, prompts, tool/plugin configuration and upstream development governance.
- Plausible first-party paths checked: human action approval as S5=P, tamper-evident audit as accountability-governance, model-defined agent types as identity and source maintainers as shared S5.
- Why no material first-party path remains: operator checks and security rules govern individual actions; developer/maintainer direction is outside the declared local organization, with no identity-level authority and returned governing decision.

## Distributed OSS parent arrangement

The product can operate different local models and accept OSS contributors, but their independent sessions do not share a first-party higher-governance process. Human `/spawn` current control exists within the local operator's recursion, not across the upstream GitHub community.

## Self-hosted and non-human modes

The local user can view and selectively cancel active children via `/spawn list` and `/spawn cancel` (S3=P). Separately, the parent model can select isolated parallel task batches and model-backed planning decisions (S2=A) and instantiate a verifier (S3*=C); permission inheritance and action checks do not manufacture S5 or S4 parent modes.

## Recursion

Primary and independently executing child `AgentLoop` instances are S1 units at the local-session recursion. Team planning/isolated sibling work provides an internal S2 relation; an attending operator supplies bounded S3. Additional model providers, tests and OSS maintainers are not further organizational recursions of the running harness merely by association.

## Variety and escalation

Task-level tool feedback and parent mailbox results support S1 recovery. Chosen worktree isolation/dependency batches attenuate file-write interference but cannot guarantee semantic merge. Active child cancellation is a parent current-control intervention. The optional verifier offers advisory independent claims, whereas audit logging is not itself an independent judge and memory/install tools alone do not prove prospective governance.

## Evidence gaps

- Frozen revision `ee8c4339`: Python 3.12 local editable install of the pinned package, **194 PASS** across tracked targeted offline test files: agent types (12), planner (6), team (14), spawn tool (10), mailbox (42), worktree integration (15), plus task-store/audit/consolidation/memory-scheduler/skills group (95). No live model/provider calls were made.
- A full `pytest` collection initially failed because a **nontracked later-branch** `tests/unit/test_metrics.py` file was left behind when switching the freshly cloned repository from newer default HEAD to the frozen ref. That file imports a correspondingly nontracked `src/mini_agent/core/metrics.py` incompatible with this commit; both were excluded from frozen evidence. The package itself was left unmodified.
- Broad native run and one selected test file `tests/unit/test_subagent.py` did not complete within bounded time; verbose rerun identified `test_subagent_uses_tools` as the hanging case after the first test passed. A 60-second focused combination timed out. These are unverified test surfaces, not a passing full suite or evidence of autonomous model quality.
- Positive S2 is restricted to intentionally selected isolated/dependency-aware operation, not the default shared-tree background group. Positive S3=P requires an attending operator. S3*=C is a separately prompted verifier constructor, not demonstrated successful AI review or mandatory corrective authority.
- Positive owner states are based on first-party executable control wiring and deterministic mocks; no live LLM, multi-agent behavior quality or end-to-end improvement before/after measurement is asserted.
