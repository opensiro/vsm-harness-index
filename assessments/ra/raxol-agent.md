---
harness_id: raxol-agent
project_name: Raxol Agent
repository: https://github.com/DROOdotFOO/raxol-agent
review_ref: e5b500988139674f39d957309b1db34988edc08a
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: C
autonomy_s5: —
---

# Raxol Agent

## Review boundary

- System in focus: One deployed first-party Raxol Agent/Console managed-agent cohort with configured Stream ReAct and optional MCP owner controls, not the wider Raxol rendering/runtime repository or OMP organization.
- Purpose and identity: Provide an OTP-backed agent application host, optionally managed over MCP, with model/tool tasks, persistent skill tools and bounded scheduler.
- Relevant environment: User apps, model/backend/provider services, MCP server, skills directories, authorized operator and external OMP if configured.
- Standard-distribution boundary: Shipped `packages/raxol_agent` and integration seams in the same pinned public repository, including supported optional scheduler and Console wiring.
- Credited operating / distribution surfaces: ReAct tool-loop, sessions, Team, owned MCP fleet controls, procedural skills actions/Store, scheduler Fire and authorization hooks.
- Adjacent first-party surfaces excluded from ownership: Removed legacy coding harness, SelfImprove/Curator/Turn, future ADR wishlists, external OMP cognitive/organizational authority and separate parent Raxol runtime source.
- First-party operating / deployment modes considered: Configured ReAct/Stream agent, MCP-owned sessions with allowlisted apps, optional Team supervisor, scheduler+skills provider, external OMP host not imported as owner.
- Recursion level: One managed agent cohort and its agent tasks; nonowned Team members and external OMP are outside the asserted MCP whole-fleet current view.
- Reviewed revision: e5b500988139674f39d957309b1db34988edc08a.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Raxol Agent is an OTP/TEA application kit that still ships an AI model-tool loop, agent sessions, Team supervision, Comm routing, MCP tools to create/list/ask/status/stop owned agents, optional persisted cron scheduler, and managed skills. Crucially the 2026-11-13 ADRs remove older self-improvement curator, Turn recorder and delegate_task implementation; code and amended status govern, not historic promises. Scheduler Fire invokes Stream and injects configured skills; permissions and spend gates enforce externally supplied authority. [ADR narrowing](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/docs/adr/0042-lean-on-omp.md); [package](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/README.md); [MCP controls](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/mcp_tools.ex).

## Operational model

Configured model-backed ReAct agents conduct S1 work. Team supervisor and messages do not establish concrete inter-agent conflict regulation. Within a narrow MCP-owned cohort, the exposed roster/status/start/stop path is a first-party whole-current-control constructor, but Raxol does not itself provide an autonomous fleet manager. Editable skills can become future capability in a composed mode; the automatic after-turn self-improvement path named in older ADRs is not present. Tool approval/safety and journaling are not imported as S5 or complementary audit.

## S1 — Operations

- State: A
- Function: Execute model-guided tasks through a first-party Elixir ReAct agent with tool feedback and typed outputs.
- Disturbance / variety regulated: Open prompts, changing tool response data, unexpected tool failures and model-selected next actions.
- Decisive decision or feedback right: In Raxol.Agent.Stream.react or Strategy.ReAct the model selects tool calls, adapts to tool results and stops or continues.
- Decision owner: The configured model-backed first-party stream/strategy operating an agent in the supported session or scheduler mode.
- Supporting / enforcement mechanisms: OTP session, provider adapters, tool converter, command hooks, authorization, journals and optional scheduler.
- Closure path: Prompt/observations → model-selected tool → guarded executor result → next model action/final response.
- Boundary reachability: Shipped Stream.react, packaged strategy and optional Console scheduler fire are first-party runnable agent paths, not development-only examples.
- Why this is / is not agent-owned: The model owns choice of task action; fixed scheduler/OTP services are supporting enforcement and recovery.
- Evidence: [ReAct loop](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/stream.ex); [strategy](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/strategy/react.ex); [scheduled runner](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/scheduler/fire.ex)
- Basis: structural
- Confidence: high for code presence and supported modes
- Caveats: Provider or OMP configuration is required; default mock backend is not evidence of real task capability.


## S2 — Coordination

- State: —
- Function: No first-party S2-specific agent interaction/regulation loop established at the selected managed-agent fleet boundary.
- Disturbance / variety regulated: Agent processes could compete for files, objectives or communications; the shipped supervisor focuses on crash recovery and message routing.
- Decisive decision or feedback right: No first-party arbitration of a concrete inter-agent conflicting commitment was found beyond identity and lifecycle checks.
- Decision owner: Not established as an S2 decision maker.
- Supporting / enforcement mechanisms: Agent.Team supervisor rest_for_one, Registry and Comm routes, per-session ownership and spawn-id guard.
- Closure path: An OTP restart or message delivery occurs, but it does not choose among competing S1 commitments or return a conflict-resolution intervention.
- Boundary reachability: The team/communication primitives ship, but generic supervision is not automatically S2.
- Why this is / is not agent-owned: A user-written coordinator callback could negotiate, but no standard coordinator-agent rule observing conflict and changing teammate behavior was identified.
- Evidence: [team supervision](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/team.ex); [team comm](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/docs/features/AGENT_FRAMEWORK.md); [owned session restrictions](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/mcp_tools.ex)
- Basis: structural
- Confidence: medium bounded negative
- Caveats: OTP failure containment is real but should not be conflated with inter-S1 variety attenuation.

### Absence scope

- Surfaces inspected: Agent.Team, Comm, session registry, MCP-owned spawn/stop and task scheduling.
- Plausible first-party paths checked: Crash restart strategy, team broadcast, duplicate-id refusal, shared task suggestions and removed delegate_task path.
- Why no material first-party path remains: These mechanisms supervise processes or route calls; none closes an S2-specific conflict of independent operational units in shipped default configuration.


## S3 — Inside-and-now control

- State: C
- Function: Provide a fleet-scoped current agent roster, status inspection, start/stop and resumed work controls for an MCP-managed ownership cohort.
- Disturbance / variety regulated: Managed agents may be absent, running, stalled or no longer needed; current capacity and task commitments need supervisory intervention.
- Decisive decision or feedback right: Inspect and choose which managed agent to spawn, query or stop and change the active managed-agent population.
- Decision owner: MCP caller/host or explicitly assembled supervisory model, not a first-party agent supervisor in the default Raxol process.
- Supporting / enforcement mechanisms: MCP agent_list/status/ask/spawn/stop, session owner checks, journal retention, OTP supervisor and optional scheduler.
- Closure path: Agent roster/status → external supervisor's decision to spawn/stop/ask → owned session starts/stops or receives new task; later MCP status reflects outcome.
- Boundary reachability: Only when built-in MCP tools are enabled in a supported registered mode; they restrict visibility/stop to this server's owned agents, excluding foreign/team members.
- Why this is / is not agent-owned: The first-party S3-specific current-state/action path exists, but a model with authority over the fleet and closed supervisory discretion must be composed by the embedding operator/host; the runtime cannot choose it.
- Whole-system current view: agent_list and status for the *MCP-owned cohort*; a different owner or Team child is not part of this current-control claim.
- Current-control decision scope: Start/stop/ask and monitor current operational agents within server ownership, not arbitrary host-wide scheduling or policies.
- Evidence: [bounded fleet controls](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/mcp_tools.ex); [owned session lifecycle](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/session.ex); [MCP mode](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/README.md)
- Basis: structural
- Confidence: medium
- Caveats: C is narrow and boundary-relative. A generic agent_status API outside an operational cohort would not qualify; no autonomous S3=A mode or parent-specific P mode is claimed.


## S3* — Complementary audit

- State: —
- Function: No first-party independent operational-claim audit loop demonstrated in the installed managed agent runtime.
- Disturbance / variety regulated: Incorrect model claims and incomplete action outcomes might require complementary primary evidence.
- Decisive decision or feedback right: No shipped autonomous auditor with separate evidence access and returned judgement of an S1 result established.
- Decision owner: Not established.
- Supporting / enforcement mechanisms: Session journal and activity records, authorized tool gates and result streams; developers can write a CodeReviewAgent example.
- Closure path: Messages/journal return work information, but no separate verifier sees different operational evidence and returns an authoritative correction.
- Boundary reachability: `team` sample and logging are available, not a first-party completed S3* audit mode.
- Why this is / is not agent-owned: A `:reviewer` label in example team is a user-supplied module and not evidence of independent agent audit or S3 feedback.
- Evidence: [custom reviewer team](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/examples/agents/agent_team.exs); [generic supervisor](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/team.ex); [communication and model view](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/docs/features/AGENT_FRAMEWORK.md)
- Basis: structural
- Confidence: medium bounded negative
- Caveats: Audit-capable custom embedding could be built but is not credited at frozen boundary.

### Absence scope

- Surfaces inspected: Core Stream and Strategy output, Session journaling, Team examples and permissions.
- Plausible first-party paths checked: Tool policy/approval, user-defined reviewer module, registry/journal views, removed independent turn recording.
- Why no material first-party path remains: Neither a shipped complementary operational observation nor claim-relative independent judgement returned to a manager is evidenced.


## S4 — Outside-and-then intelligence

- State: C
- Function: Expose procedural skill creation/modification for adaptation to future task varieties, without a fully installed autonomous after-turn improvement owner.
- Disturbance / variety regulated: New tasks may expose missing procedures and outdated skill content needed in later scheduled or interactive runs.
- Decisive decision or feedback right: An embedding agent/operator can create/patch first-party managed SKILL.md procedures through skill_manage, to be retrieved/injected into later work.
- Decision owner: The calling model or human in a developer-composed mode; standard runtime does not independently decide when experiences warrant future skill revision.
- Supporting / enforcement mechanisms: Skills.Store, skill_manage, read-only external skill dirs, versioned SKILL.md disk persistence, scheduler's skill-block injection.
- Closure path: New skill gap and deliberately invoked skill_manage → durable managed skill → later list/view or scheduled-run injection. The missing detection/independent prospective judgement must be composed.
- Boundary reachability: First-party actions appear when an agent supplies skills_provider; documented callback defaults nil and must be configured.
- Why this is / is not agent-owned: A function-specific future-capability constructor exists, but removed SelfImprove/Curator and Turn recorder mean no ordinary completed agent-owned feedback cycle; C not A.
- External distinction: A newly encountered task requirement or outside skill source compared with currently indexed procedural assets.
- Future / prospective distinction: Saved SKILL.md is durable across runs and can alter later prompts/available routines, not simply a one-turn memory buffer.
- Adaptation option generated: A created or edited procedural skill with typed metadata and body in managed skills root.
- Path back into current capability / S3: Skills.Store subsequently supplies the changed skill to agent tools or scheduler Fire system-prompt composition.
- Evidence: [skill construction](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/actions/skills/manage.ex); [persistent reusable skills](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/skills/store.ex); [future run injection](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/scheduler/fire.ex); [explicitly narrowed ADR](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/docs/adr/0021-self-improving-agents-skills-curation.md)
- Basis: structural
- Confidence: medium
- Caveats: ADR-0021 once claimed automatic curator/self-improve but 2026-11-13 amendment says removed; that historical design is excluded from A.


## S5 — Policy and identity

- State: —
- Function: No native ultimate-identity/policy tension and authoritative ratification with returned rule revision established.
- Disturbance / variety regulated: Conflicting standing mission or constitutional limits are different from tool-call approval, scope and spend safety.
- Decisive decision or feedback right: No in-boundary ultimate-policy adjudication path evidenced.
- Decision owner: External operator supplies permissions and manifests; enforcement remains deterministic.
- Supporting / enforcement mechanisms: Authorization.Engine ALLOW/ASK/DENY, root/session remembered approval, MCP authorizer, allowlisted applications and spending constraints.
- Closure path: A tool ASK can be approved and remembered at action/session scope; no identity-level decision changes subsequent organizational purpose.
- Boundary reachability: Policy modules are shipped but have no S5 deliberation-and-return mode.
- Why this is / is not agent-owned: Approval of a tool call and failure-closed limits do not constitute ultimate-policy ownership or future constitutional settlement.
- Evidence: [tool approval engine](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/authorization/engine.ex); [bounded actor ownership](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/packages/raxol_agent/lib/raxol/agent/mcp_tools.ex); [current narrowed architecture](https://github.com/DROOdotFOO/raxol-agent/blob/e5b500988139674f39d957309b1db34988edc08a/docs/adr/0042-lean-on-omp.md)
- Basis: structural
- Confidence: medium bounded negative
- Caveats: No private Raxol or external OMP organization's policies imported into the assessed boundary.

### Absence scope

- Surfaces inspected: Authorization engine/Policy, MCP tool registration, session owner and spend/sandbox limits.
- Plausible first-party paths checked: ASK remembered per session/root, authorizer and allowlist enforcement, user-controlled process lifecycle.
- Why no material first-party path remains: All paths are action permission or execution safety; no first-party identity conflict → legitimate ultimate authority → returned policy settlement.

## Distributed OSS parent arrangement

GitHub maintainer/release choices belong to the development organization and are not part of this managed cohort. OMP is an optional external agent host with separate authority, not a first-party Raxol S3/S4 owner.

## Self-hosted and non-human modes

The package runs as a configured self-hosted OTP application. Native model-backend/tool mode counts for S1 when configured; the MCP server's ownership restriction is a positive boundary condition, not a blanket claim over every Team agent. No parent P mode is asserted without an evidenced parent decision loop.

## Recursion

A managed cohort is the whole for S3=C. Individual session agents are S1. The Team supervisor is a process lifecycle mechanism. OMP and the developer supply higher recursion outside the reviewed autonomous harness.

## Variety and escalation

Model-chosen tools absorb task-level variety, OTP restarts reduce process failures, and MCP ownership guards prevent unauthorized fleet mutation. Skills management provides a bounded possible future-capability path when coupled with a developer-supplied trigger/decision. Authorization ASK does not become S5 deliberation; neither journal logging nor a reviewer-named example become S3*.

## Evidence gaps

- No provider-backed integration execution or first-party independent S3* reviewer run was performed.
- MCP fleet current-control constructibility is limited to agents that the same server owns; Team member status/stop may be explicitly refused.
- The deliberate 2026-11-13 removal of self-improvement/Turn/delegate_task blocks claiming their earlier documented autonomy.
- Source static review supports a constructor, not evidence of autonomous capacity adaptation in a standard connected deployment.
