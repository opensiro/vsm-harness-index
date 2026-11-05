---
harness_id: jarvis-ai-council
project_name: JARVIS AI Council
repository: https://github.com/berkesecicii/free-multi-agent-ai-council
review_ref: 20a93de357da82c39255932da71dfb12aeea2f49
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# JARVIS AI Council

## Review boundary

- System in focus: one operator-installed local JARVIS AI Council application, coordinating JARVIS, VISION, FRIDAY, EDITH and other enabled role adapters within a user's project/chat.
- Purpose and identity: provide one Mac-native chat surface for dynamically coordinating AI specialists, using project/computer tools with human-defined access and verifiable deliverables.
- Relevant environment: task complexity, research/coding specialization, contention for shared model connectors, scarce quota, sequential/parallel work, misleading tool claims, user permission requirements.
- Standard-distribution boundary: first-party Swift/WKWebView frontend, Python standard-library HTTP runtime, `team_runner` and `chat_workflow`, installed agent connectors, project bridge, scheduler, human permission controls. A signed-in provider CLI is required for actual remote model work.
- Credited operating / distribution surfaces: [application and response routing](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py), [multi-role team planner and scheduler](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py), [live-chat workflow](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/chat_workflow.py), [project tool boundary](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/project_bridge.py) and [README supported modes](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/README.md).
- Adjacent first-party surfaces excluded from ownership: screenshot/demo assets, bundled test fixtures, native packaging scripts, developer builds, provider-auth internals of Codex/Claude/Gemini, third-party hosted models and their own organization/governance.
- First-party operating / deployment modes considered: shared chat with model-directed automatic handoff, direct human specialist calls, human-reviewed team plan/start, explicit fixed team workflow, multi-step team run with bounded two-way parallelism, read-only/ask/turbo project access, local/macOS control with permission.
- Recursion level: installed multi-agent team in one user workspace/chat; a model provider's own safety governance and the Mac OS entitlement authority are adjacent systems, not JARVIS internal S5.
- Reviewed revision: `20a93de357da82c39255932da71dfb12aeea2f49`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

JARVIS has a local Python HTTP server, JavaScript UI and optional Swift native shell. It composes configured Claude Code, Codex and Gemini provider CLIs/other adapters; the provider's own agent internals are not claimed as a first-party metasystem. In shared chat, rules and a JARVIS model can select specialist work, emit typed `HANDOFF` directives, constrain step count and quota, and initiate a subsequent model call. In explicit team mode, JARVIS emits a machine-readable plan (zero to three steps), the operator can start it, and `team_runner` creates isolated child chats and task packets. It can group at most two independent connector-distinct stages, persist their outcomes, supply bounded previous result and actual changed-file excerpts to next stage, and present a combined report. The Mac/project bridges offer permission cards, project tools and basic execution feedback. An application scheduler manages time-based user tasks. [README](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/README.md); [team runner](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py); [app routing](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py).

## Operational model

The user states the goal and permission envelope. Specialist models independently decide how to research, implement and review assigned work using their configured access. In the automatic shared-chat mode, the first-party JARVIS prompt and post-response handoff parser construct an agent-selected division and initiate the next role automatically; the human can separately use the explicit team-plan mode to approve which specialists will act. Provider contention and parallel stages are bounded by host runtime rules, not negotiated autonomously. The auxiliary model reviewer may receive a constructed, separately read file-excerpt channel, but no independently protected auditor workspace or assurance guarantee is provided. [Handoff policy and receiver](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L823-L910); [team planner and run](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py#L4-L144).

## S1 — Operations

- State: A
- Function: attached specialist agents independently execute coding, web-research, reading or review tasks and return task results and observations.
- Disturbance / variety regulated: codebase state, provider tool results, user questions, web evidence and unexpected errors within each assigned specialist responsibility.
- Decisive decision or feedback right: role model decides its research or code steps, tool requests and content after observing context/tool outputs; host controls access approval and routing.
- Decision owner: selected model-backed specialist (VISION/Claude CLI, FRIDAY/Codex, EDITH/Gemini or other installed supported agent), not the deterministic Python routing rules.
- Supporting / enforcement mechanisms: CLIs/adapters, project-command/patch/search, browser/desktop bridge, role-scoped chat context, saved task/output state and human permissions.
- Closure path: user/JARVIS assigns task → first-party launcher reaches signed-in provider agent and approved tools → model consumes tool observations and delivers artifact/findings → host records output → later team stage or user consumes it.
- Boundary reachability: providers are explicitly wired by first-party adapters and runtime launch; team runner selects their actual connector and creates a bounded child chat/task rather than only naming hypothetical specialists.
- Why this is / is not agent-owned: provider-backed agents choose task-specific actions after observations, while local approval prompts and quotas do not themselves create agent discretion.
- Evidence: [shipped connectors and task semantics](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/README.md); [task launch](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py#L22-L59); [live provider launching](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L1061-L1331).
- Basis: source-reachable supported model execution modes.
- Confidence: medium-high for structure; external paid/subscription models not exercised.
- Caveats: the first-party host cannot prove the quality of any third-party proprietary model's internal reasoning.

## S2 — Coordination

- State: C
- Function: first-party grouping and connector-busy guards attenuate incompatible overlapping work across specialist runs while returning completed producer context to a later specialist.
- Disturbance / variety regulated: simultaneous role workers attempting the same constrained provider connector, or a dependent role acting before a producer output exists.
- Decisive decision or feedback right: human/model step plans indicate dependencies or independent stages; host accepts at most two same-group jobs and refuses two concurrent uses of a connector; it defers dependent stages until the current group's work is collected.
- Decision owner: static coordinator constructor and plan authors, not an agent capable of negotiating runtime contention or autonomously repairing a conflicted schedule.
- Supporting / enforcement mechanisms: `model_jobs` provider-busy check, `threading.Lock`, same-connector rejection, parallel grouping, grouping barriers, bounded prior-stage packet, and failure/cancellation statuses.
- Closure path: candidate parallel group is tested for connector conflict → only nonconflicting roles launch; the next group waits for current completion → collected result is returned as bounded context to subsequent role; if provider already busy, the team exits with explicit error instead of colliding.
- Boundary reachability: `team_runner` executes these checks directly before invoking first-party configured model adapters, and persists the workflow state visible to the user.
- Why this is / is not agent-owned: interference attenuation is specific to *distinct* S1 agents sharing provider capacity and result dependencies; its selection policy is configured/deterministic, requiring further autonomous composition for S2=A.
- Distinct S1 units: enabled EDITH research, VISION coding and FRIDAY review/development workers operating in the same team request.
- Inter-S1 disturbance: overlapping role calls compete for shared provider capacity; a consumer role can act on an incomplete producer result.
- Attenuating coordination relation: connector-distinct parallel group admission and completed-group barrier with packet return.
- Feedback into subsequent S1 behaviour: conflict prevents launch and surfaces team error; completion unlocks subsequent stage and provides its result, so downstream work waits for producer evidence.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is runtime prevention of a *specific conflicting simultaneous provider use* plus an explicit inter-role completion barrier, not the fact that prompts mention other agents.
- Evidence: [group building, connector checks and barrier](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py#L22-L106); [shared runtime job and quota guards](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L720-L744).
- Basis: first-party structural constructor path.
- Confidence: medium.
- Caveats: no agent-level merge conflict resolution or general distributed work scheduling is claimed; configured write permissions/isolated chats prevent some interactions without solving arbitrary semantic conflicts.

## S3 — Inside-and-now control

- State: A(P)
- Function: JARVIS assigns present team work to available specialists and constrains who executes next; in a separate supervised mode the human approves and starts a proposed multi-role plan.
- Disturbance / variety regulated: mismatch between request and expertise, specialist availability/quota, excessive handoff depth and pending current workload.
- Decisive decision or feedback right: in automatic chat mode the JARVIS model chooses to hand an actionable brief to another specialist, and host executes it within a two-handoff current chain; in explicit plan mode the operator decides whether the proposed role/effort/step commitments begin.
- Decision owner: autonomous JARVIS coordinator model in the active auto-handoff configuration; legitimate Mac user/operator in the first-party reviewed-plan and direct-call configurations.
- Supporting / enforcement mechanisms: role/connector availability and quota scans, model-authored `HANDOFF` parser, `fit_handoff` corrections, hop/visited limits, `team-plan` and `team-start`, task/role progress and user-visible review card.
- Closure path: **base A:** coordinator sees current request and available agents → selects next specialist/brief → host validates target, quota and hop bound → launches next model into the same team turn → completed work returns for coordinator synthesis. **parent P:** operator inspects the proposed team steps/roles → confirms start or selects agents directly → `start_team` executes selected commitments, returns results and gives operator stop/rework control.
- Boundary reachability: auto handoff is a shipped default (`auto_handoff` true), `split_handoff` and continuation call the actual model launch; the explicit reviewed plan path is offered by first-party `team-plan`/`team-start` actions and takes effect on real role runs.
- Why this is / is not agent-owned: the agent can select the next current work commitment in the autonomous configured mode, while the operator has a genuinely distinct authorization path in the explicit-team mode. Deterministic caps merely bound both decisions.
- Whole-system current view: the coordinator is briefed on callable team roles, their available connector/quota, the current shared chat and prior outputs; the human sees the complete team plan and current task/agent statuses in the app.
- Current-control decision scope: current division of requested work among available team members, next assignment and effort, task-step commitment and interruption, not a company-wide financial/resource allocation claim.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | JARVIS model coordinator | Task requires a different available specialist | Model chooses `HANDOFF`, parser enforces role/quota, runtime launches role; result returns to shared team chat | [handoff decision and execution](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L823-L910), [runtime continuation](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L1307-L1332) |
| Parent (`P`) | Local human | Explicit plan and proposed specialist/effort set | User `team-start` approves step commitments; team executor launches them and reports; human can stop/adjust | [plan and approval](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py#L105-L144), [plan start/stop actions](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L1966-L1996) |

- Evidence: [README coordination modes](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/README.md); [JARVIS handoff and role availability](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L720-L910); [human-reviewed plan execution](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py).
- Basis: distinct shipped automatic vs explicit human-approved operating modes.
- Confidence: medium; current-control mapping is at the single team/chat recursion only.
- Caveats: provider quotas and file scopes are hard guards rather than agent-owned priorities; the planned team mode is human-approved and should not be relabeled autonomous on that basis alone.

## S3* — Complementary audit

- State: C
- Function: the shipped build→review team shape can provide a distinct model reviewer with a host-read snippet of actual changed files, separate from the implementer's prose report.
- Disturbance / variety regulated: implementer reports success without grounding it in actual changed content or a second critique.
- Decisive decision or feedback right: the plan or default `FRIDAY` review stage chooses the review function; a model may give a critique, but the host constructs the limited separate artifact-evidence packet, and no mandatory independent review acceptance gate is shipped.
- Decision owner: constructed reviewer role with model critical judgment, invoked only in selected plans; human controls whether that optional stage is included and acted on.
- Supporting / enforcement mechanisms: default `FRIDAY` review stage, separate child chat, previous-stage report packet and host `ProjectBridge` reads of approved changed-file excerpts.
- Closure path: build specialist reports completion → host reads approved changed files from attached project and supplies excerpt alongside untrusted implementation report → distinct reviewer model critiques it → critique enters team results and final JARVIS presentation for the user / next current action.
- Boundary reachability: `start_team` defines a real default `FRIDAY` reviewer after `VISION`; `collect` reads actual project paths and appends changed-file excerpts; the runner invokes the reviewer using its own connector, when enabled and configured. Not every dynamic or explicitly planned workflow elects review.
- Why this is / is not agent-owned: the reviewer can judge content independently of the implementer's wording, but first-party code only constructs a bounded evidence packet and optional review; the reviewer does **not** automatically receive independent command execution in `kind=review`, so `C` is safer than a strong autonomous audit owner claim.
- Claim being audited: code implementation and claimed changed-file result from the prior build stage.
- Ordinary reporting path: model-authored stage output saved as a team task result, then passed to downstream roles.
- Complementary access path: host `ProjectBridge.path(...).read_text()` for approved changed-file requests, packaged as `Changed file excerpts` to the next review stage.
- Independence boundary: separate model agent with actual file excerpts not supplied by model prose; however excerpts are partial, only for recorded approved requests, and reviewer has no independent project tool rights in this review stage.
- Who acts on findings: reviewer returns concrete failure/missing checks through team presentation to the user; no automatic veto or remediation is claimed.
- Evidence: [default review stage and excerpt construction](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py#L4-L106); [review role prompt](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/chat_workflow.py#L17-L27); [bounded project file access](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/project_bridge.py).
- Basis: constructor-specific alternate evidence path; no guarantee of mandatory audit or outcome correctness.
- Confidence: medium-low due optional stage and incomplete raw-artifact coverage.
- Caveats: the default team plan omits unavailable roles and a model-generated plan may omit reviewer entirely; source snippets are the same worktree the implementer can change, not an isolated verifier workspace.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental-sensing and capability-adaptation loop is closed at the installed team recursion.
- Disturbance / variety regulated: future model/provider or external market changes are not transformed into a selected capability change by a shipped S4 decision process.
- Decisive decision or feedback right: research specialist answers current tasks, while operator adjusts config; there is no routine future-option evaluation and adopted update path.
- Decision owner: not supplied as a distinct adaptation authority.
- Supporting / enforcement mechanisms: web search/research role, quotas, scheduled chat tasks, local role settings.
- Closure path: task-local research may feed immediate work, but no exterior/future intelligence → alternative adaptation → approved capability revision loop is implemented.
- Why this is / is not agent-owned: live web search and code building within a user brief are S1; a scheduled task or quota warning alone is not future-oriented organization adaptation.
- Evidence: [research and code routing](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L892-L929); [team planner](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/team_runner.py#L105-L145); [scheduler](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/scheduler.py).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: human can ask a research→build sequence to improve the software, but that does not create a first-party enduring S4 procedure at this recursion.

### Absence scope

- Surfaces inspected: README capabilities, app handoff/agent availability, planner, team run, scheduler and settings.
- Plausible first-party paths checked: EDITH web searches, research-before-build pipeline, quota notices, scheduled task types and role customization.
- Why no material first-party path remains: all are direct user-task or present resource handling, without shipped prospective external distinction, adaptation selection and return of a capability change to the team as a continuing policy.

## S5 — Policy and identity

- State: —
- Function: no distinct ultimate-identity or policy-conflict decision transaction is closed through a legitimate internal parent authority and return path.
- Disturbance / variety regulated: conflicting purpose/ultimate-policy demands are not represented as a governable S5 issue by the application.
- Decisive decision or feedback right: user grants OS/project permissions and configures agents, but no built-in exceptional identity/policy adjudicator is invoked and returned.
- Decision owner: external Mac user and OS entitlement authorities for ordinary permissions, not a first-party S5 loop.
- Supporting / enforcement mechanisms: per-chat permission tiers, explicit risky-command approvals, prohibited app/action checks, selected role charters and user settings.
- Closure path: user approves a requested tool action and it executes or is refused; that is local operation permission, not identity issue → final legitimate policy decision → governed future activity under a new policy resolution.
- Why this is / is not agent-owned: hard safety rails and permission consent are fixed constraints for S1/S3 operation; they are not a viable organization's policy/identity decision right.
- Evidence: [README permission and safety rails](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/README.md); [permission mode and work decision routing](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/app.py#L1987-L2008); [project bridge](https://github.com/berkesecicii/free-multi-agent-ai-council/blob/20a93de357da82c39255932da71dfb12aeea2f49/project_bridge.py).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: this denies a first-party closure path, not the existence of legitimate human or OS-level authority outside the assessed recursion.

### Absence scope

- Surfaces inspected: README user-mode design, agent prompts, settings/actions, permissions, native and project tool boundaries.
- Plausible first-party paths checked: changing permission tiers, explicit action approval, user override/stop, quotas, hardcoded role charter, OS security permissions.
- Why no material first-party path remains: each path directly constrains present tasks/roles and tools; none surfaces and resolves a competing ultimate organizational identity issue with a distinct authoritative decision and returned governance feedback.

## Recursion

The chosen recursion is one user-operated Mac team/chat. Each subscribed specialist is an S1 operating unit, even if the external CLI has a richer internal agent hierarchy. A separate chat/team run or scheduled chat does not automatically form a new complete VSM recursion. Human permission/plan control is a supported parent mode over the same installed team, not evidence of centralized organization-level governance of several independent installations.

## Variety and escalation

The model planner attenuates work variety through task kind, specialist selection, effort and bounded steps; host caps handoffs and incompatible concurrency, and surfaces quota/approval/exception cards to the user. A paused conversation or failed provider blocks subsequent work rather than silently pretending success. The reviewer receives a limited raw-file channel and can criticize, but cannot assert an all-code proof. Exceptional permission decisions are present-work gates, not an evidenced S5 channel.

## Evidence gaps

- Pinned source and 294 passing Python `unittest` cases (two skips) were reviewed; no macOS native UI, proprietary provider subscription or live computer-control E2E run was performed.
- The S3 autonomous mode is *shared-chat local team allocation*, not a full institution's resource or identity governance. A human-reviewed explicit plan is a distinct parent mode; model proposal alone is not counted as its autonomous start.
- S3* uses separately read file excerpts and an optional second model critique; it lacks mandatory independent diff/test execution and a protected reviewer worktree. Accordingly only constructor-mode evidence is credited.
- S2 is limited to connector capacity/conflict and dependent-group waiting; no repository-wide merge conflict resolution or negotiation is claimed.
