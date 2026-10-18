---
harness_id: agentteams
project_name: AgentTeams
repository: https://github.com/agentscope-ai/AgentTeams
review_ref: 88b9f3abbb4aa91d030adfb6d41dbd10d5eda255
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-21
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentTeams

## Review boundary

- System in focus: the first-party AgentTeams collaboration/control plane at pinned revision `88b9f3abbb4aa91d030adfb6d41dbd10d5eda255`, including the Kubernetes/embedded controller, Worker/Team/Manager resource contracts, Matrix collaboration fabric, shared storage, TeamHarness prompts/skills/MCP tools, project/task durable state, lifecycle and human-intervention APIs.
- Purpose and identity: organize multiple separately implemented agent runtimes into visible, durable and governable team collaboration, with a Manager/Leader role coordinating Workers, shared project/task state, Matrix rooms, storage, credentials, runtime lifecycle and human intervention.
- Relevant environment: human requesters and operators; Matrix rooms/channels; model providers and gateways; shared object/file storage; Kubernetes/Docker; external agent runtimes including QwenPaw, OpenClaw, Hermes, CoPaw and the experimental DeepSeek Harness; MCP/skill sources; task/project disturbances and runtime failures.
- Standard-distribution boundary: AgentTeams' controller, declarative resources, lifecycle reconciliation, Matrix/TeamHarness collaboration machinery, first-party prompts/skills/MCP contracts, project/task state and operator intervention surfaces are first-party. The autonomous model/tool execution loops supplied by QwenPaw, OpenClaw, Hermes, CoPaw and DeepSeek Harness remain adjacent runtimes even when AgentTeams packages images, configures them, launches their containers and supplies TeamHarness collaboration assets.
- Credited operating / distribution surfaces: `agentteams-controller`; embedded/Helm deployment; Worker/Manager/Team CRDs and reconciliation; TeamHarness runtime-neutral prompts, skills and MCP tools; durable project/task store and transition contracts; Matrix rooms; MinIO/shared workspace; `agt` and authenticated Project/lifecycle APIs.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/build workflows; tests/examples; AgentLoop evaluation/experimentation surfaces; independent Dashboard implementation where it merely visualizes controller state; external runtime internals and their private agent loops; model providers/gateways; third-party skills/MCP servers. Same-repository adapters/package material are credited only as wiring unless they transfer a decisive organizational decision into the AgentTeams boundary.
- First-party operating / deployment modes considered: local embedded installation; Kubernetes/Helm deployment; QwenPaw/OpenClaw/Hermes/CoPaw/DeepSeek-Harness-backed Manager and Worker containers; TeamHarness Project/Quick Task collaboration; authenticated human Project intervention and lifecycle control.
- Recursion level: AgentTeams collaboration/control plane. Hosted Manager and Worker runtimes may each be autonomous systems at a lower recursion, but their internal agent loops are not inherited as AgentTeams-owned S1 merely because the controller launches and coordinates their containers.
- Reviewed revision: `88b9f3abbb4aa91d030adfb6d41dbd10d5eda255`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

AgentTeams explicitly describes itself as a collaborative multi-agent runtime platform using a Manager-Workers architecture, while also drawing a sharp implementation boundary: it “does not compete with other Agent runtimes” and, instead of implementing Agent logic itself, orchestrates and manages multiple Agent containers. The supported Worker runtime field makes that external-runtime boundary concrete: a Worker selects `openclaw`, `copaw`, `hermes`, `qwenpaw` or `deepseek-harness`, and the controller reconciles container placement, state, credentials, storage, Matrix identity and runtime configuration around that selected backend.

TeamHarness is the first-party organizational layer placed inside those runtimes. Its boundary document calls it a runtime-neutral team-collaboration base containing stable role/team prompts, collaboration skills, MCP tools and runtime-adapter entrypoints. It deliberately does not own worker lifecycle, worker desired-state application, runtime hook behavior, runtime-specific credential enforcement or direct QwenPaw/Claude Code runtime mutation. The worker/runtime adapter consumes controller-written facts and exposes TeamHarness assets to the selected runtime.

The TeamHarness contract is materially stronger than a generic message bus. The Leader role plans work, delegates ready tasks, checks submitted results, accepts/rejects them, advances dependencies and reports accepted outcomes. Workers execute assigned tasks and submit structured results. Project Work persists DAG/Loop state across sessions; only accepted results advance dependencies; continuation and submission identities prevent conflicting retries; trusted-Leader checks prevent Workers from accepting or cancelling their own work. Human/controller APIs can separately create, pause, resume, replan and complete projects or cancel tasks, with intervention history and pre-change snapshots.

Those mechanisms supply durable organizational state, role constraints and closure paths around hosted agents. They do not, however, supply the autonomous actor that chooses a plan, interprets a Worker result, decides acceptance or selects the next substantive action. The Manager/Leader actor performing those discretionary steps is a QwenPaw/OpenClaw/Hermes/etc. runtime selected and hosted by AgentTeams. Removing that adjacent runtime while keeping AgentTeams' controller, TeamHarness prompts/MCP, Matrix, project store and transition engine leaves no autonomous task-level decision/action loop.

Primary evidence:

- [`README.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/README.md) — explicit product boundary, Manager-Workers architecture, statement that AgentTeams does not implement Agent logic, supported external runtimes, shared collaboration/control surfaces and human intervention model.
- [`agentteams-controller/api/v1beta1/types.go`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/agentteams-controller/api/v1beta1/types.go) — Worker CRD runtime selection (`openclaw | copaw | hermes | qwenpaw | deepseek-harness`), desired lifecycle state, container management, credentials/MCP and runtime configuration contracts.
- [`docs/design/teamharness/boundary-and-contracts.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/docs/design/teamharness/boundary-and-contracts.md) — explicit TeamHarness ownership and non-ownership boundary between collaboration assets, controller, worker desired-state loop and concrete agent runtime.
- [`plugins/teamharness/prompts/team/TEAMS.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/prompts/team/TEAMS.md) — Leader/Worker collaboration contract, Direct/Quick/Project flows, DAG/Loop delegation, result acceptance and requester reporting.
- [`plugins/teamharness/prompts/manager/AGENTS.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/prompts/manager/AGENTS.md) — Manager role as control-plane coordination rather than direct task execution.
- [`plugins/teamharness/skills/team/project-management/SKILL.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/skills/team/project-management/SKILL.md) — trusted-Leader planning/acceptance, DAG/Loop progression and requester closure contract.
- [`docs/design/teamharness/project-task-runtime-design.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/docs/design/teamharness/project-task-runtime-design.md) — durable ProjectMeta/TaskMeta, submission fences, trusted-Leader terminal decisions, continuation resolution and Controller-authorized cancellation.

## Operational model

A requester message reaches a Manager/Leader runtime through AgentTeams' collaboration surface. TeamHarness instructions tell that runtime whether to answer directly, create one bounded Quick Task or establish durable Project Work. For project work the Leader creates DAG/Loop state, selects ready nodes and delegates them to Worker runtimes through Matrix task rooms. Worker runtimes execute their assigned work using their own agent logic and submit structured results. The Leader runtime checks the result, owns the discretionary accept/revise/block decision, advances eligible dependencies and reports state back to the requester. AgentTeams supplies persistence, role fencing, routing, transition validation and lifecycle/controller enforcement around that process.

The counterfactual owner test is decisive at this boundary. With QwenPaw/OpenClaw/Hermes/etc. removed, TeamHarness still contains detailed instructions and deterministic state transitions but no autonomous actor remains to interpret arbitrary work, choose plans/actions or exercise Leader judgment. With the external runtime retained but AgentTeams removed, the external agent runtime still has an autonomous model/tool loop, although it loses AgentTeams' team organization. Therefore the standard AgentTeams distribution does not establish a first-party autonomous S1 decision/action loop and is proposed for the Index exclusion state rather than receiving a forced `S1=C` or borrowing hosted-runtime autonomy.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational decision/action loop is established inside the AgentTeams collaboration/control-plane boundary.
- Disturbance / variety regulated: AgentTeams regulates team membership, routing, shared state, lifecycle, credentials, task/project persistence and collaboration structure; arbitrary task/environment variety is interpreted and acted on by hosted external agent runtimes.
- Decisive decision or feedback right: interpret the current task and observations, choose the next substantive plan/tool/action, and revise action after returned results.
- Decision owner: the selected hosted runtime's agent (QwenPaw, OpenClaw, Hermes, CoPaw or DeepSeek Harness), outside AgentTeams' first-party agent-logic ownership.
- Supporting / enforcement mechanisms: Manager/Worker CRDs, controller reconciliation, TeamHarness prompts/skills/MCP, Matrix rooms, project/task state, shared filesystem, runtime config, lifecycle controls and gateways.
- Closure path: requester/team event → AgentTeams collaboration/control surfaces → hosted runtime agent interprets and acts → TeamHarness/controller persist and route resulting state/messages → hosted runtime agent chooses subsequent action. The autonomous operational discretion closes in the external runtime.
- Why this is / is not agent-owned: first-party AgentTeams deliberately supplies organization around agents rather than the agent logic itself; its Worker spec selects separately implemented runtimes and TeamHarness describes itself as runtime-neutral infrastructure consumed by those runtimes.
- Evidence: [`README.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/README.md), [`agentteams-controller/api/v1beta1/types.go`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/agentteams-controller/api/v1beta1/types.go), [`docs/design/teamharness/boundary-and-contracts.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/docs/design/teamharness/boundary-and-contracts.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a deployed AgentTeams installation contains autonomous hosted agents; this assessment keeps ownership repository-relative and does not deny those runtimes' independent S1 qualification.

### Absence scope

- Surfaces inspected: README/product boundary; Worker runtime CRD; controller/runtime ownership contract; TeamHarness prompts, skills and MCP boundary; project/task durable state; Manager role and human intervention surfaces.
- Plausible first-party paths checked: Manager role as S1; TeamHarness project engine as S1; controller reconciliation as S1; Matrix/room flow as S1; packaged Worker images as transfer of runtime ownership.
- Why no material first-party path remains: every generic task-level discretionary loop still requires a separately implemented selected agent runtime; first-party AgentTeams mechanisms constrain, persist, coordinate and govern that loop but do not implement its autonomous actor.

## S2 — Coordination

- State: —
- Function: AgentTeams exposes substantial coordination machinery, but no S2 function among first-party AgentTeams-owned S1 units is established at the declared recursion because the operational agent units are adjacent runtimes.
- Disturbance / variety regulated: TeamHarness explicitly addresses assignment ping-pong, duplicate/invalid assignment, dependency order, stale project context, self-acceptance and conflicting result/cancellation retries among hosted Workers and Leaders.
- Decisive decision or feedback right: decide how to partition work, which ready Worker/task to delegate, whether a result is accepted/revised/blocked, and how to alter subsequent assignments.
- Decision owner: the external Manager/Leader runtime agent; deterministic TeamHarness state and transition machinery transports/enforces its decisions.
- Supporting / enforcement mechanisms: Matrix task rooms, team roster, ready-node queries, DAG dependencies, submission IDs/digests, trusted-Leader fences, project/task state and requester routes.
- Closure path: hosted Leader chooses delegation/acceptance → TeamHarness validates and persists state → Worker runtimes receive assignments/results → later Leader/Worker behavior changes. The organizational coordination loop spans external S1 actors rather than closing among first-party AgentTeams-owned S1 units.
- Why this is / is not agent-owned: the first-party machinery is purpose-built for coordination, but the decisive coordinating discretion belongs to a hosted runtime AgentTeams explicitly does not implement. Without first-party S1 units, the assessment does not promote generic organizational scaffolding to `S2=C` merely because it can coordinate external agents.
- Evidence: [`plugins/teamharness/prompts/team/TEAMS.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/prompts/team/TEAMS.md), [`plugins/teamharness/skills/team/project-management/SKILL.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/skills/team/project-management/SKILL.md), [`docs/design/teamharness/project-task-runtime-design.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/docs/design/teamharness/project-task-runtime-design.md).
- Basis: structural absence at declared ownership boundary.
- Confidence: high.
- Caveats: at a wider assembled deployment boundary that intentionally includes the external runtime agents as constituent S1 units, the same TeamHarness machinery could be evidence for S2; that is a different system-in-focus.

### Absence scope

- Surfaces inspected: team collaboration contract; project/task transitions; Matrix task rooms; ready-node/dependency handling; result acceptance; shared state and Worker roster.
- Plausible first-party paths checked: deterministic DAG/Loop scheduling; task-room coordination; trusted-Leader acceptance; anti-ping-pong/mention rules; shared workspace and TeamHarness message/project/task MCP tools.
- Why no material first-party path remains: the concrete coordination decisions are exercised by hosted external Leader/Worker agents, while AgentTeams itself supplies the coordination substrate and enforcement around actors outside its autonomous S1 ownership boundary.

## S3 — Inside-and-now control

- State: —
- Function: AgentTeams supplies a strong whole-team current-control surface, but no first-party autonomous S3 owner over first-party S1 operations is established at this boundary.
- Disturbance / variety regulated: current project progress, Worker availability/state, ready/blocked tasks, runtime lifecycle, team membership, skill/config state and operator interventions.
- Decisive decision or feedback right: choose current priorities/delegations, accept or revise results, replan active work, pause/resume/complete projects, cancel tasks or change runtime desired state.
- Decision owner: autonomous choices are made by the hosted external Manager/Leader runtime; authenticated humans separately own intervention decisions; controller reconciliation enforces declared state.
- Supporting / enforcement mechanisms: project DAG/Loop state, Controller APIs, `agt`, Dashboard-backed state, Worker desired `Running/Sleeping/Stopped`, Kubernetes/Docker reconciliation, intervention history and snapshots.
- Closure path: external Leader or authenticated human chooses a current-control change → first-party TeamHarness/controller records/enforces it → Worker/project operation changes. The return path is real, but the decisive owner is not an AgentTeams-owned autonomous actor and the controlled S1 units are adjacent runtimes.
- Why this is / is not agent-owned: “Manager” naming does not transfer ownership; the Manager is itself a selected external runtime. Human intervention is meaningful governance but does not cure the missing first-party S1 boundary or create an autonomous base state for the excluded harness.
- Evidence: [`README.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/README.md), [`plugins/teamharness/prompts/manager/AGENTS.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/prompts/manager/AGENTS.md), [`plugins/teamharness/skills/team/project-management/SKILL.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/skills/team/project-management/SKILL.md), [`agentteams-controller/api/v1beta1/types.go`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/agentteams-controller/api/v1beta1/types.go).
- Basis: explicit + structural absence at declared ownership boundary.
- Confidence: high.
- Caveats: the first-party human Project APIs demonstrate operationally closed current-control interventions over the assembled deployment, but Methodology publication for this autonomous-harness boundary is not used to preserve an otherwise excluded system by assigning metasystem states without S1.

### Absence scope

- Surfaces inspected: Manager prompt; Leader project workflow; Controller/Worker desired-state contracts; human Project/lifecycle controls; current project/task/Worker views and intervention history.
- Plausible first-party paths checked: Manager as S3 agent; controller as S3 owner; human intervention as S3 parent mode; runtime desired-state reconciliation; project replanning and task cancellation.
- Why no material first-party path remains: discretionary current-control ownership belongs either to external runtime agents or humans, with AgentTeams controller/state machinery enforcing their choices over adjacent hosted operations; no first-party autonomous S3 owner over first-party S1 operations remains.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit judgment with a findings-to-control loop is established inside AgentTeams.
- Disturbance / variety regulated: audit metadata, project history, Worker checkpoint status, runtime observability and AgentLoop integrations can expose discrepancies or failures.
- Decisive decision or feedback right: none established for an independent auditor that interprets complementary evidence and returns a corrective judgment into AgentTeams-owned operations.
- Decision owner: no first-party independent audit actor established.
- Supporting / enforcement mechanisms: intervention audit trail, pre-change snapshots, project timeline, Worker checkpoint graph/status, controller status and optional AgentLoop observability/evaluation integration.
- Closure path: telemetry/history can inform a human or hosted agent, but no standard first-party alternative evidence path → independent audit judgment → corrective-control loop is established.
- Why this is / is not agent-owned: auditable rooms and checkpoint/history surfaces improve transparency, but Methodology requires complementary access plus an independent judgment path; logging, history and evaluation integration by themselves are not S3*.
- Evidence: [`README.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/README.md), [`docs/design/teamharness/project-task-runtime-design.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/docs/design/teamharness/project-task-runtime-design.md).
- Basis: explicit + structural absence.
- Confidence: medium-high.
- Caveats: an operator may use checkpoints/history for diagnosis, and AgentLoop may provide external evaluation capabilities, but no boundary-reachable independent auditor judgment and feedback ownership was established in the reviewed standard distribution.

### Absence scope

- Surfaces inspected: README auditing/AgentLoop claims; Project intervention history; pre-change snapshots; Worker checkpoints; controller/status views; TeamHarness result checking.
- Plausible first-party paths checked: audit timeline as S3*; Worker checkpoints as complementary access; `check_task` as verifier; AgentLoop integration as auditor.
- Why no material first-party path remains: these surfaces provide provenance, diagnostics or ordinary result validation; none establishes a sufficiently independent first-party audit actor whose findings feed a corrective decision back into operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally and prospectively oriented adaptation loop is established for AgentTeams at the declared recursion.
- Disturbance / variety regulated: runtime/model/skill availability, external service changes and future team capability can be changed by operators or external runtimes, but no first-party S4 intelligence function is evidenced.
- Decisive decision or feedback right: choose prospective adaptations to AgentTeams capability from environmental/future distinctions.
- Decision owner: no first-party autonomous owner established; users/operators select runtimes, models, AgentSpec packages, skills and configuration, while hosted agents may request or use capabilities inside their own runtime.
- Supporting / enforcement mechanisms: runtime selection, skills ecosystem/registry, AgentSpec packages, model/MCP configuration, reconciliation and package/application paths.
- Closure path: configuration/package decisions can change future capability, but no standard environmental sensing → prospective option generation → adaptation choice → present-capability return loop is established inside AgentTeams.
- Why this is / is not agent-owned: package/skill/runtime flexibility and continuous-optimization integrations are capability mechanisms, not by themselves S4. The TeamHarness boundary explicitly leaves AgentSpec application and direct runtime mutation to worker/runtime layers.
- Evidence: [`docs/design/teamharness/boundary-and-contracts.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/docs/design/teamharness/boundary-and-contracts.md), [`agentteams-controller/api/v1beta1/types.go`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/agentteams-controller/api/v1beta1/types.go), [`README.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: external runtimes or humans may independently perform adaptation; this assessment does not borrow their prospective intelligence into AgentTeams.

### Absence scope

- Surfaces inspected: runtime/model/package/skill configuration; TeamHarness boundary; AgentLoop optimization claim; Worker desired-state/reconciliation and Project workflow.
- Plausible first-party paths checked: skill discovery/update; AgentSpec package changes; runtime/model switching; AgentLoop continuous optimization; project replanning.
- Why no material first-party path remains: these are configuration, external integration or present-task replanning paths without a first-party external-and-prospective intelligence owner and closed return into AgentTeams capability.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy closure is established at the AgentTeams collaboration/control-plane recursion.
- Disturbance / variety regulated: static role contracts, credential rules, RBAC, human visibility/intervention and selected AgentSpec/SOUL/runtime configuration bound operation.
- Decisive decision or feedback right: settle an identity- or ultimate-policy-level issue for the AgentTeams organization and return that authoritative choice into subsequent operation.
- Decision owner: no such first-party autonomous or operationally closed parent path was established; operators configure identity/policy surfaces and external runtimes consume them.
- Supporting / enforcement mechanisms: CRD identity/soul/agents fields, TeamHarness credential-safety rules, RBAC, gateway credential isolation, human access controls and runtime/package selection.
- Closure path: ordinary configuration or intervention changes operation, but no evidenced identity/policy dispute → legitimate ultimate authority decision → returned organization-wide policy closure is supplied as a first-party runtime loop.
- Why this is / is not agent-owned: static prompts, SOUL/identity fields, credential policy and authenticated approvals constrain operation but are not themselves S5. Human final say over a Project/task intervention remains current control rather than automatic identity/ultimate policy.
- Evidence: [`plugins/teamharness/prompts/team/TEAMS.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/plugins/teamharness/prompts/team/TEAMS.md), [`agentteams-controller/api/v1beta1/types.go`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/agentteams-controller/api/v1beta1/types.go), [`README.md`](https://github.com/agentscope-ai/AgentTeams/blob/88b9f3abbb4aa91d030adfb6d41dbd10d5eda255/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a particular enterprise deployment can place ultimate authority in its human governance organization; that deployment-specific parent system is not established as an AgentTeams first-party S5 mode merely by exposing configuration/intervention controls.

### Absence scope

- Surfaces inspected: TeamHarness role/credential policy; Worker identity/Soul/Agents configuration; RBAC/access; human Project intervention; gateway credential isolation and deployment/operator configuration.
- Plausible first-party paths checked: Manager as ultimate authority; SOUL/AGENTS text as S5; human Project intervention as S5 parent mode; credential/RBAC rules; runtime/package selection.
- Why no material first-party path remains: reviewed paths either constrain ordinary operation or configure adjacent runtimes; none closes an identity/ultimate-policy decision at the AgentTeams organization boundary.

## Distributed OSS parent arrangement

The public repository has normal maintainer/contributor governance, but that development organization is adjacent to the deployed AgentTeams control plane under Methodology 0.3.5. Repository merge/release decisions are not used as runtime S3/S4/S5 ownership. The deployed product does expose human operational intervention; those rights are mapped by their actual current-control function rather than promoted to S5 merely because a human has final say.

## Self-hosted and non-human modes

AgentTeams is explicitly self-hostable and supports strong operator visibility/intervention. Those modes can produce human-owned current-control decisions over the assembled deployment, but they do not create the missing first-party autonomous S1 actor. Conversely, a deployment can minimize human intervention and let the hosted Manager/Leader agent coordinate Workers; the autonomous owner in that mode is still the selected external runtime rather than an AgentTeams-implemented agent loop.

## Recursion

Manager and Worker containers are distinguishable operational actors and may themselves be viable systems, but their internal autonomy/metasystems belong to QwenPaw/OpenClaw/Hermes/CoPaw/DeepSeek-Harness and require separate evidence. AgentTeams' nested Team/Project/Task structures and spawned subagents demonstrate orchestration and decomposition, not by themselves VSM recursion owned by AgentTeams.

## Variety and escalation

AgentTeams attenuates substantial collaboration variety through TeamHarness modes, task rooms, durable DAG/Loop state, ready-node calculation, trusted-Leader fences, submission identities, Matrix routing, shared storage and controller reconciliation. Exceptions can surface as blocked/revision/cancelled states, Project interrupts or human interventions. These are strong transduction and enforcement channels; they do not alter the ownership conclusion that hosted runtimes supply the autonomous actors deciding how to absorb task variety.

## Evidence gaps

No evidence gap is material to the proposed exclusion: primary first-party documentation explicitly separates AgentTeams organization/control from external Agent logic, and the CRD makes runtime substitution a standard feature. A wider assessment that deliberately defines the installed AgentTeams-plus-QwenPaw/OpenClaw assembly as one system-in-focus could map the TeamHarness coordination/current-control relations differently, but that would no longer be the repository-relative first-party AgentTeams boundary used by this Index review.
