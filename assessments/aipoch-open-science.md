---
harness_id: aipoch-open-science
project_name: AIPOCH Open-Science
repository: https://github.com/aipoch/open-science
review_ref: b89d0e134ad65e197c2cefddda69921a5458a552
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AIPOCH Open-Science

## Review boundary

- System in focus: The pinned publicly shipped local-first Electron/TypeScript scientific research workbench. One local AIPOCH installation is the recursion, with multiple project/session scientific task operations, app-owned ACP agent launch/prompt/session lifecycle, permissions and compute/tool resources, task API/CLI and native UI current work controls, artifact provenance and its separate Reviewer/re-review subsystem.
- Purpose and identity: Let scientists launch autonomous model/agent-assisted literature, analysis, scientific-code and report tasks across local projects with persisted evidence, managed approvals and recoverable sessions; expose independent checks of agent-produced conclusions/artifacts for correction.
- Relevant environment: Scientific task prompts, external papers, local project files, browser/search/scientific data and Python/R notebooks, external ACP agent implementations and model providers, user/operators, tool permissions, remote compute and persisted research artifacts.
- Standard-distribution boundary: The supported desktop/headless CLI research-workbench, built-in TaskRunner and ACP task adapter, session manager, reviewer host and viewer controls, scientific connectors/notebook/provenance. Autonomous task-semantic reasoning and native ACP tool-loop internals are in configured third-party Claude/OpenCode/Codex agents, which operate as *reachable S1 actor dependencies* under an AIPOCH-managed session but their own internal S2–S5 are not attributed to AIPOCH. The installed Reviewer is another separately instantiated ACP model role with first-party limited evidence tools and correction integration.
- Credited operating / distribution surfaces: [README.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/README.md); [packages/open-science/CLI.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/packages/open-science/CLI.md); [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/acp/task-agent-port.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/task-agent-port.ts); [src/main/acp/agent-process.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/agent-process.ts); [src/main/acp/session-agent-target.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/session-agent-target.ts); [src/main/session-persistence/operation-scheduler.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/session-persistence/operation-scheduler.ts); [src/main/session-persistence/coordinator.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/session-persistence/coordinator.ts); [src/main/reviewer/orchestrator.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/orchestrator.ts); [src/main/reviewer/review-assessment-owner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/review-assessment-owner.ts); [src/main/reviewer/reviewer-fix-loop-owner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/reviewer-fix-loop-owner.ts); [src/main/reviewer/mcp-server.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/mcp-server.ts); [src/main/reviewer/turn-evidence.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/turn-evidence.ts); [src/main/reviewer/ipc.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/ipc.ts); [src/main/artifacts/provenance-storage.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/artifacts/provenance-storage.ts); [src/main/web-service/task-api.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/web-service/task-api.ts).
- Adjacent first-party surfaces excluded from ownership: Release/CI, model benchmarks/rankings, developers' own research or maintainer governance, tests as separate product actors, external ACP harnesses' internal cognition/orchestration, their internal subagents, external scientific data or models, OS/remote compute schedulers and externally installed plugins. No deeper nested viable system is inferred from provider process trees.
- First-party operating / deployment modes considered: Standard Electron UI research sessions, headless local Task API/CLI projects and concurrent session runs, explicit provider/backend choices, per-session permission configurations and stop/resume, optional `autoReviewEnabled` fresh-context Reviewer and three-round correction/re-review, user-selected task/control and approvals. Different operator/constructor modes are alternatives, not concurrent S3 ownership.
- Recursion level: One AIPOCH instance managing a live set of project scientific task sessions. Each ACP autonomous research session is a task outcome-producing S1 unit in the installed whole; its native reasoning implementation remains external and is not promoted as an independent first-party higher VSM owner.
- Reviewed revision: `b89d0e134ad65e197c2cefddda69921a5458a552` frozen candidate intake #186, batch #1648 row 8.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The first-party `TaskRunner.startRun` manages a real project/session Task identity with an agent configuration, selected provider, scientific prompt, allowed skill and compute targets, and a durable run journal. `createAcpTaskAgentPort` creates/resumes a bound ACP session and forwards the task prompt, history/provenance and permission mode to a configured autonomous coding/research agent. `agent-process.ts` actually launches the approved separate ACP executable/runtime under an isolated provider config. Its provider model/agent loop chooses how to investigate user research tasks and what tools to invoke; AIPOCH observes streamed messages, tool events and artifacts, updates its own session state, and supplies per-activity Notebook/connector/permission/provenance capabilities. No first-party AIPOCH alternative model/tool reasoning loop should be invented: **S1=A describes installed AIPOCH-managed external autonomous S1 cells**, and not app ownership of external ACP semantics. [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/acp/task-agent-port.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/task-agent-port.ts); [src/main/acp/agent-process.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/agent-process.ts); [README.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/README.md).

The main app maintains project-scoped and all-session projections, resumable provider session targets, accepted prompts, active-run identities, permission/compute selection, lifecycle cancellation and terminal output plus versioned scientific artifacts. `TaskRunner.reserveSession` rejects a second simultaneous Run under the *same Session identity*; `SessionPersistenceOperationScheduler` serializes authoritative Project/Session identity mutations while permitting disjoint sessions/projects to progress. These are actual data-consistency/current admission guards, but one-session duplicate admission does not establish a disturbance and mutual behavioral correction among distinct S1 operations: absent an inter-S1 witness, do not inflate the lock to S2. The whole current inventory, launch/configuration/cancel and resource choices support first-party S3 primitives. An operator has a separately closed task/project/session management route via Desktop/CLI/Task API and acts on the chosen current constraints. [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/session-persistence/operation-scheduler.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/session-persistence/operation-scheduler.ts); [packages/open-science/CLI.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/packages/open-science/CLI.md); [src/main/web-service/task-api.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/web-service/task-api.ts).

AIPOCH also ships a genuinely complementary `Reviewer` chain. On enabled sessions a completed assistant turn is handed from `TaskRunner` to `Reviewer`. `runReview` / `runReviewAssessment` create a **fresh-context independently prompted ACP Reviewer session**, give it a scope-bounded and permission-restricted dedicated MCP evidence server to read exact turn/artifact/provenance/raw code and observations, and persist structured checks. In eligible full-main-session review, a warn/fail finding triggers up to three rounds of `[Auditor]` correction turns to the primary agent followed by **new separate review**; source-finding IDs remain stable and ambiguous/unaddressed/cancelled issues aren't marked passed. This is a separate evaluator acting on complementary evidence with a material actual return to subsequent operation, not just generic logs. The configuration `autoReviewEnabled` is optional/default off for Task API and failures do not universally prevent main-run completion, so this is **available conditional S3*=A**, not guaranteed scientific validity of every result. [src/main/reviewer/orchestrator.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/orchestrator.ts); [src/main/reviewer/review-assessment-owner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/review-assessment-owner.ts); [src/main/reviewer/reviewer-fix-loop-owner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/reviewer-fix-loop-owner.ts); [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts).

Scientific connectors, notebook execution, export/import and versioned provenance improve traceable research execution. The app's upgrade catalogs, selected agent models and installable scientific skills may change through externally provided developer/provider/operator updates, but no first-party future-oriented **organizational adaptation** comparison/decision and returned deployment across current agent sessions has been demonstrated. Static permission profiles, project user choices, encryption and credential isolation do not establish an ultimate identity/ethos policy authority with a distinct S5 return.

## S1 — Operations

- State: A
- Function: Produce distinct research task outputs in user project environments through active, model-directed autonomous ACP scientific/coding sessions launched and supervised by AIPOCH.
- Disturbance / variety regulated: Ambiguous scientific questions, changing local literature/data, code/execution results, permission requests, tool errors and subsequent user clarification.
- Decisive decision or feedback right: The configured autonomous external ACP agent (Claude/OpenCode/Codex or compatible supported target) chooses task-local model/tool actions, responds to tool and Notebook/connector results and produces a final research report/artifact while AIPOCH owns agent-session admission and feedback/report transport.
- Decision owner: External model-backed autonomous ACP agent actually launched by AIPOCH first-party supported product path. AIPOCH owns the containing local research-cell session and control-plane boundary, not the agent's implementation details.
- Supporting / enforcement mechanisms: TaskAgentPort, ACP session create/resume and prompt forwarding, streamed tool observation, sandbox/Notebook/connector bridge, permission broker, project artifact collection, failure/stop/restart controls.
- Closure path: User project research goal → AIPOCH app creates configured ACP task Session and forwards prompt → model agent chooses scientific analysis/tool use → actual external/local tool observations return to provider agent → agent adjusts task actions/report → AIPOCH records outputs/provenance and later task continuation.
- Boundary reachability: `TaskRunner.startRun` and `executeRun` call `TaskAgentPort.prompt`; shipped ACP adapter calls `runtime.sendPromptObserved` or `sendPrompt` on attached provider session. Desktop/headless CLI `open-science run` uses same service. No optional private plugin required for this app-owned session/actor relation.
- Why this is / is not agent-owned: Substantive next-action choice occurs in the running autonomous ACP agent; without that dependency TaskRunner remains a session/permission/persistence controller, not a scientist. Ownership claim includes only the reachable S1 research work cell, not upstream agent-native subroles/plans.
- Evidence: [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/acp/task-agent-port.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/task-agent-port.ts); [src/main/acp/agent-process.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/agent-process.ts); [packages/open-science/CLI.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/packages/open-science/CLI.md).
- Basis: First-party source-attested launch/prompt/observation relation plus supported external autonomous agent as operational S1; internal agent semantics not directly reviewed.
- Confidence: High for reachable autonomous operating relation; bounded on underlying external agent capabilities.
- Caveats: Research agent's model/tool-selection loop is not authored inside AIPOCH; different configured backends may differ and external ACP actor must be installed/authenticated.


## S2 — Coordination

- State: —
- Function: No source-demonstrated mutual disturbance regulation between **distinct** independently operating S1 scientific research sessions beyond persistence/duplicate-identity admission.
- Disturbance / variety regulated: Overlapping runs could target the same Session identity or mutate the same persisted project metadata, creating conflicting transcript writes; the reviewed protection applies to identical Session or Project *records* rather than two interacting independent scientific task units.
- Decisive decision or feedback right: Session admission `session_busy` and operation-scheduler serialization guard same-identity persistence consistency; no source-backed inter-S1 contention assessment and coordinated sibling behavioral adjustment was found.
- Decision owner: First-party deterministic reservation/persistence scheduler enforcing prewritten identity contracts.
- Supporting / enforcement mechanisms: `activeRunBySession` reservation and release, session identity scope tails, version/revision conflict guards, global mutation barrier, task progress ledger.
- Closure path: Second start on same Session id is rejected or same-key metadata mutation awaits lock; no distinct operational sibling S1 activity observes a conflict and receives an S2 coordination response that changes its scientific operation.
- Distinct S1 units checked: Two different ACP research sessions can exist across projects; same-session two prompt attempts instead address *one* operational identity. Same-file/project concurrent agents and inter-task resource arbitration weren't shown through these reviewed guards.
- Inter-S1 disturbance candidate checked: Duplicate access to a live Session transcript and shared project storage; identity scheduling is about authoritative record consistency, not task-operational interference demonstrated between different ongoing agents.
- Why this is / is not agent-owned: A deterministic lock does not automatically make a constructor-owned S2 function. S2 requires a specific inter-S1 variety/feedback witness, not simply generic session locking.
- Evidence: [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/session-persistence/operation-scheduler.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/session-persistence/operation-scheduler.ts); [src/main/session-persistence/coordinator.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/session-persistence/coordinator.ts); [src/main/session-persistence/operation-scheduler.test.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/session-persistence/operation-scheduler.test.ts).
- Basis: Bounded negative after checking strongest actual admission/lock path.
- Confidence: Medium-high for this installed organization boundary.
- Caveats: These are genuine safety/correctness controls; a separate compute scheduling or workspace-conflict function could change S2 if it demonstrated a specific cross-session operational interference and response.

### Absence scope

- Surfaces inspected: TaskRunner concurrent run admission, activeRunBySession, Task Agent Port, Project/Session operation scheduler, revision conflicts, task inventory, compute host selection and session history.
- Plausible first-party paths checked: Same-session double run, different-session shared project persistence, simultaneous task runs, shared compute and delegations.
- Why no material first-party path remains: The observed guards handle one Session identity or generic storage/workload capacity; no concrete current independent-agent collision paired with returned mutual behavioral coordination is attested.


## S3 — Inside-and-now control

- State: C(P)
- Function: A first-party current-project/session control plane over a live portfolio of research operations: select current tasks, configure model/provider and resources/permissions, start/resume/cancel active runs and inspect or intervene on their status.
- Disturbance / variety regulated: Research project tasks may be active/failed/interrupted/stale, pending approval, require compute/permissions, need cancellation or a configuration/continuation decision, or risk incorrect session ownership.
- Decisive decision or feedback right: Task API/Desktop/CLI display the whole local project/session run set and expose functions to create task sessions, continue/start research, modify selected compute hosts and permission/delegation profile, cancel/stop tasks, review outputs and resume. Operator owns **which** current work/limits to apply, while the first-party system handles approved changes and persists state. There is no packaged autonomous *whole-of-project manager* choosing those interventions by default.
- Decision owner: Base constructor mode: function-specific TaskRunner/TaskAgent APIs that a developer could compose into an autonomous current-control actor; human/operator parent mode: Desktop/CLI/Task API user selects current work and intervenes from project/session/run status.
- Supporting / enforcement mechanisms: Durable projects/run journal, listProjects/listSessions/getRun/status/progress, startRun/cancelRun, session configuration revision checks, task admission constraints, compute host selection, approvals/permissions and agent pause/restart.
- Closure path: Whole project/session current state → caller chooses start/resume/adjust active agent/compute/permission/cancel → TaskRunner applies command to ACP session and persists mutation/terminal state → displayed status, artifacts and subsequent task running state change.
- Whole-system current view: All project records, sessions and active run identities with status/progress/outputs/selected compute/permission and provenance; not full provider-internal intentions or scientific quality.
- Current-control decision scope: Multiple concurrent live research session commitments and their admission/current resources, continuation, cancellation and operator/parent-controlled configuration.
- Boundary reachability: Packaged `open-science run`, `run status`, `run cancel`, `session status/config update`, local Task API and GUI use TaskRunner's real current-control methods; not a developer-only test surface.
- Why this is / is not agent-owned: The host exposes/enforces whole-current actions but no first-party autonomous manager/optimizer chooses the system-wide current work plan; `C` for composable manager path. A legitimate operator owns current decisions in the shipped parent console path, hence `(P)`. Neither tool-permission approval alone nor startRun in isolation would establish this.
- Evidence: [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/acp/task-agent-port.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/task-agent-port.ts); [src/main/web-service/task-api.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/web-service/task-api.ts); [packages/open-science/CLI.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/packages/open-science/CLI.md); [src/main/session-persistence/coordinator.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/session-persistence/coordinator.ts).
- Basis: Implemented current multi-session portfolio and command-path source plus user-facing control documentation.
- Confidence: Medium-high on parent current-work control and constructor; no automatic dynamic priority negotiation or lab-wide business management.
- Caveats: The parent human may not be present in all unattended modes; classification records supported alternatives, not simultaneous ownership.


### S3 control modes

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Downstream composed autonomous current-control actor **not shipped** | Typed multiple-session running/idle/failed/approval/compute state indicates a current intervention | Actor would use existing `TaskRunner` start/cancel/config/continue commands; app enforces and returns current run statuses, but no deciding manager agent is packaged | [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/web-service/task-api.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/web-service/task-api.ts) |
| Parent (`P`) | Researcher/operator through shipped Desktop/CLI | Operator observes multiple active/pending/stopped project sessions and changes immediate research commitments | Human issues shipped run/task/session actions (start/resume/cancel/permission/compute host) → TaskRunner updates real ACP sessions and persists reflected current state | [packages/open-science/CLI.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/packages/open-science/CLI.md); [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts) |

## S3* — Complementary audit

- State: A
- Function: Challenge autonomous research agent's outputs and scientific artifact claims with a fresh-context, separately model-directed, scope-limited complementary evidence-access path and return unresolved warnings into corrective activity.
- Disturbance / variety regulated: Agent conclusions may cite unsupported sources, conceal action failures, claim generated charts/data without reproducible trace, omit risk limitations, misread original files or report a flawed scientific task outcome.
- Decisive decision or feedback right: Independently prompted Reviewer ACP model uses allowed read-only reviewer-specific evidence tools, checks the actual turn/artifact/trace and submits structured pass/warn/fail check findings rather than using the main agent's self-assessment. Fresh Reviewer judgment determines what to challenge.
- Decision owner: A separate autonomous ACP Reviewer model invoked through first-party `Reviewer` architecture and its bounded MCP evidence bridge; the host decides lifecycle, scope, persistence and bounded correction orchestration.
- Supporting / enforcement mechanisms: Turn-scope snapshot and digest, raw evidence resolver, immutable artifact version/provenance readers, read-only Reviewer MCP server, structured findings schema/IDs, reviewer ACP session lifecycle, correction prompt / fix-loop limits.
- Closure path: Completed ordinary agent output and artifact claims → first-party scope-bounded independent Reviewer session reads alternative raw/provenance/trace evidence → Reviewer emits structured warn/fail/pass findings → host injects [Auditor] request to main session and re-reviews each correction up to limit → findings resolved or explicitly remain unaddressed.
- Claim being audited: The produced scientific output, cited sources, tool execution correctness and artifact-specific provenance for a given completed run/turn.
- Ordinary reporting path: Original ACP agent's answer/plan/tool events and published artifacts, persisted as session run result.
- Complementary access path: Fresh ACP Reviewer session with separately scoped MCP read_turn/real artifact files and provenance, test/trace evidence, external to original agent's own selective narrative; no ordinary write-tools granted to reviewer.
- Independence boundary: Distinct session and controlled evidence interface with bounded rights, but same host process and potentially same upstream provider/model, not guaranteed separate security realm/human.
- Who acts on findings: First-party `runReviewWithSession` detects warn/fail and calls `runReviewerFixLoop`, which sends correction to main agent; independent re-review tracks stable sourceFindingId and unresolved outcomes.
- Boundary reachability: `TaskRunner` after a persisted completed agent output invokes `reviewer.review` if `autoReviewEnabled === true`; `Reviewer` IPC/manual run supports same path. `runReviewAssessment` creates actual Reviewer ACP session; `runReviewerFixLoop` sends correction and re-review to the main ACP session.
- Why this is / is not agent-owned: The audit finding is selected by an independent model reading complementary evidence; deterministic storage, gates and correction scheduling do not make the finding only constructor-owned. Thus S3*=A in enabled Reviewer mode.
- Evidence: [src/main/reviewer/orchestrator.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/orchestrator.ts); [src/main/reviewer/review-assessment-owner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/review-assessment-owner.ts); [src/main/reviewer/mcp-server.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/mcp-server.ts); [src/main/reviewer/reviewer-fix-loop-owner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/reviewer-fix-loop-owner.ts); [src/main/reviewer/turn-evidence.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/reviewer/turn-evidence.ts); [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts).
- Basis: Source-attested bounded separate model audit with real main-agent correction return.
- Confidence: High for installed conditional correction wiring; no empirical scientific review accuracy tested.
- Caveats: Reviewer auto-invocation is opt-in and appears default false for Task API; Reviewer errors do not invalidate an already completed task; fix loop limited to three rounds and can mark unresolved; evidence access is scoped and not guaranteed complete.


## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party owned externally/prospectively driven change of the research installation's future capabilities/options with selected return into S3 established at pinned boundary.
- Disturbance / variety regulated: Changing scientific data, tool catalog, external provider/model choices and skills could affect later work but current features are configurable/developer or vendor governed.
- Decisive decision or feedback right: Operator chooses current installed model, skill and connector; app can discover/pull updates and reuse artifact histories, but no demonstrated first-party actor systematically compares external future scenarios and selects a capability adaptation returned to active project control.
- Decision owner: Vendor/developer/operator for offered dependencies, installed features and model/provider selection; first-party runtime transmits/applies configurations.
- Supporting / enforcement mechanisms: Scientific connector catalogs, skill marketplace/install, model settings, reusable research history, artifact provenance, product update engine.
- Closure path: External scientific search/current data → present S1 research tasks; configurable future model/skill availability → operator updates app manually. No S4-owned environmental scanning → prospective alternatives → measured choice → returned organization-wide changed capability cycle.
- Why this is / is not agent-owned: Scientific work about future research is S1's user task, not AIPOCH's *own* future ability to perform it. Installing a connector/model version is not evidence of institutional intelligence selection.
- Evidence: [README.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/README.md); [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts); [src/main/acp/session-agent-target.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/session-agent-target.ts); [packages/open-science/CLI.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/packages/open-science/CLI.md).
- Basis: Bounded negative review of model/connector/skill and external data paths.
- Confidence: Medium; first-party future adaptation decision could exist in additional capabilities outside inspected candidate paths.
- Caveats: Does not deny model-provider choice, new data ingestion or update distribution; only their insufficiency to establish the specific organizational S4 function.

### Absence scope

- Surfaces inspected: Runtime model/provider selection, specialist/skills, scientific connectors/notebook environment, Artifact Provenance/Reviewer, project history and update/release config.
- Plausible first-party paths checked: External scientific search, selected model changes, software/skill marketplace updates, session continuity, provenance replay and training from previous tasks.
- Why no material first-party path remains: These serve user task research or manually selected tool changes; no reviewed present first-party future-option analysis/adoption returned as a governing adaptation across operations.


## S5 — Policy and identity

- State: —
- Function: No first-party ultimate value/identity/ethos conflict settlement authority shown beyond permissions and prechosen local trust settings.
- Disturbance / variety regulated: Sensitive local/private scientific data, untrusted tools and connector capabilities, network exposure, remote compute permissions, unsafe shell/edit action and credential handling.
- Decisive decision or feedback right: Users choose permission mode, delegated task allow/deny, project model and tools; app enforces typed permissions, stores protected credentials and can cancel dangerous work. It does not adjudicate ultimate institutional policy goals or expose a legitimate S5 settlement loop.
- Decision owner: Human research institution/operator for actual ethics/research identity outside the app, project developer for fixed security primitives.
- Supporting / enforcement mechanisms: Ask-for-approval/auto/full profile, trust-scoped grants, local secrets, reviewer permission restrictions, compute policy, project/session config and audit/provenance records.
- Closure path: Preselected permission and trust rule → tool/run gate, task continues/pauses/rejects. There is no distinct values dispute → ultimate legitimate institutional decision → binding policy change returned through S3–S4.
- Why this is / is not agent-owned: Manual approving a notebook command is a safety/authorization step, not higher-level identity/mission governance; keeping sensitive data local does not create S5.
- Evidence: [README.md](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/README.md); [src/main/acp/permission-profile-controller.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/permission-profile-controller.ts); [src/main/acp/permission-broker.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/acp/permission-broker.ts); [src/main/tasks/task-runner.ts](https://github.com/aipoch/open-science/blob/b89d0e134ad65e197c2cefddda69921a5458a552/src/main/tasks/task-runner.ts).
- Basis: Bounded negative of highest plausible policy/trust owners and their actual return paths.
- Confidence: Medium-high at local first-party software boundary.
- Caveats: A deploying laboratory or scientific ethics board might exercise genuine S5 outside the assessed AIPOCH installation.

### Absence scope

- Surfaces inspected: Trust/permission profiles, credential isolation, delegated specialists, project task/agent configuration, Reviewer rights and local provenance storage.
- Plausible first-party paths checked: Project-owner permission choices, context/trust changes, stop/cancel, data retention/trust and default policy text.
- Why no material first-party path remains: No first-party ultimate institutional-policy dispute decision or closed return is implemented; those choices are task/resource permissions or external governance.


## Distributed OSS parent arrangement

The active research organization is a local research workbench plus real configured ACP autonomous research sessions. External ACP agents own each task's semantic tool reasoning and may bring internal native subagents, but their separate coordination, auditor and governance internals are not inherited. The operator is an explicit first-party current task/project management parent at S3 in the shipped GUI/CLI; no first-party policymaker for the user's laboratory is claimed.

## Self-hosted and non-human modes

The Electron desktop app or local headless daemon serves Task API and CLI clients. Local projects/sessions persist independently of which backend is selected. Real provider processes require installed/authenticated backend, can be local or remote inference, and permission modes constrain enabled tools. Optional per-session auto-review or manual review creates a separate critic ACP session and limited evidence MCP server, with model-generated criticism and repair. Operator presence is required for some permission profiles but not for unattended tasks.

## Recursion

At one AIPOCH installation, separately configured autonomous ACP research sessions are S1 current operational units. The app exposes whole project/session/current-task status and current-control changes as composable constructor S3 and direct operator parent S3. Reviewer is an explicitly separate complementary audit channel; its limited evidence scope and optional correction distinguish it from provider-native model self-reflection. Generic same-session locks do not establish inter-S1 S2, nor do model catalogs/scientific task search or safety permission profiles establish S4/S5.

## Variety and escalation

Scientific data sources, full model agents, tools and notebooks amplify task ability; session/provider identity isolation, permissions, typed task admission, immutable provenance and audit scope attenuate unsafe ambiguity. Unapproved actions escalate to a human; reviewer findings escalate to main agent correction with bounded retry. These are not automatically a legitimate institutional S5 authority and do not prove complete scientific reproducibility.

## Evidence gaps

- Pinned source and first-party reachability reviewed; no live external ACP research/model inference, scientific notebook, reproduced benchmark or measured reviewer precision/recall.
- `S1=A` credits **launched external ACP actors** as research cells at AIPOCH local-installation recursion, not as AIPOCH-native agent loop logic. Removing external ACP leaves a functional manager, not research-reasoning operation.
- `S2=—` is bounded by the observed same-Session reservation / Project persistence scope; it does not assert no concurrency control anywhere in the code or deny future inter-S1 coordination.
- `S3=C(P)` records supported alternative typed constructor and actual operator whole-current controls, not a preinstalled autonomous manager (A) or automatic scheduling of a research portfolio.
- `S3*=A` is an **opt-in** fresh-context reviewer, with bounded re-review and error isolation. It does not universally block publication of reports; absence of a passed check is not an assurance of correctness.
- `S4=—` and `S5=—` are bounded source findings for the installed organization rather than absence of a model marketplace, lab strategy, human ethics or external providers.
