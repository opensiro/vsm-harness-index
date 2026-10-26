---
harness_id: onecli
project_name: OneCLI
repository: https://github.com/onecli/onecli
review_ref: 6eaf8780f6310587ae86906eb9573ab531e92c12
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# OneCLI

## Review boundary

- System in focus: A self-hosted OneCLI workspace running one or more first-party hosted agent sandboxes, their conversations and team-facing operational controls. A BYO registered external agent without the hosted runtime is not enough for the positive S1 evidence.
- Purpose and identity: Give people separate persistent, sandboxed agents able to perform delegated work with gateway-controlled credentials, human-granted connections, agent-to-agent collaboration and durable memory; retain a common workspace control surface.
- Relevant environment: Human instructions and agent peers, provider responses and tool outputs, credentials and external APIs, stalled conversations/background jobs, unauthorized requests, scarce runner capacity, changing agent configuration and test regressions.
- Standard-distribution boundary: Apache-2.0 hosted stack: web dashboard, API control plane, gateway, outbound runner, sandbox supervisor, bundled jcode adapter, platform tool bridge, workspace policy, inter-agent link/task controls and available agent eval UI. A self-hosted operator must enable a runner and configure an actual model grant. Paid `ee/` organization-wide policy, IdP/SSO governance and adjacent CI/e2e implementation are not credited.
- Credited operating / distribution surfaces: [hosted stack and components](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/README.md), [runner operating loop](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/runner/README.md), [sandbox supervisor and adapter](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/README.md), [first-party agent tool roster](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/src/capabilities/agents.ts), [workspace brief update](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/agent-service.ts), [agent evals and judge](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/agent-eval-service.ts).
- Adjacent first-party surfaces excluded from ownership: `apps/hosted-e2e/` black-box testing, development live-proof scripts, fake backend/adapters, project maintainer CI, enterprise-only `ee/` org controls, and external Hermes/OpenClaw/NanoClaw agent implementations. The bundled `@1jehuang/jcode-sdk` provides reasoning/execution transport and native swarm behavior, not a new first-party OneCLI inter-agent metasystem merely by association.
- First-party operating / deployment modes considered: Hosted self-host with Docker runner/network isolation and jcode supervisor; optional per-agent scheduled work, agent-to-agent peer task with two-sided approvals, workspace owner dashboard/policy, and optional per-agent on-demand/scheduled eval runs. Bare installation without a runner or provider key, BYO-only registration and paid-only organization policy are distinguished.
- Recursion level: One workspace's ongoing hosted-agent work. Individual agent sandboxes are operational S1 units; their vendor-native helper sessions may be a lower recursion. The company operating OneCLI SaaS and upstream OneCLI maintainers are not this work organization.
- Reviewed revision: `onecli/onecli@6eaf8780f6310587ae86906eb9573ab531e92c12` (`main`).
- Observation date: 2026-10-26; immutable repository source, no live LLM/provider/browser tests.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The web dashboard creates/configures hosted agents and displays conversations, workspace access, activity, peer relationships and per-agent evals. The API stores conversation and turn state, schedules and policy/grant decisions. An outbound-only runner long-polls API work and starts/reaps network-isolated sandboxes; inside each is the supervisor implementing the `@onecli/agent-protocol` interface. The shipped `jcode` adapter launches a bundled model-backed agent runtime, translates its tool and event protocol, exposes limited platform tools and retains durable agent home/memory across restarts. A separate Rust gateway enforces already-decided access and injects credentials the guest never sees. [Architecture](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/README.md#architecture), [real adapter](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/src/harness/jcode.ts), [runner](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/runner/src/runner.ts).

When enabled, agents can ask peers to handle person-originated tasks using `message_agent` and later report through `complete_task`; the platform maintains bilateral consent, one active peer task per pair, bounded FIFO, per-side message budgets and a recovery close line. A separate built-in eval service asks an agent known-answer questions through its normal turn path, checks raw answers and tool attribution, and optionally obtains criterion-by-criterion model judgments. The user authors test criteria and may schedule checks, inspect reports and manually revise an agent. This is not the normal agent's own independent self-correction controller. [Agent links](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/channels/agent-link-service.ts), [peer task](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/channels/peer-task-service.ts), [eval service](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/agent-eval-service.ts).

## Operational model

The active agent's model, not the long-poll loop or credential gateway, chooses the contents of task/tool actions within its brief and effective grants. Platform runtime enforces current permissions, resume, background liveness, task serialization and memory materialization. Agent peers can make distinct work decisions, while owner consent and bounded-turn interlocks regulate pairwise collaboration. Workspace owner chooses effective cross-agent access, briefs and workspace-wide policies; runtime enforces those selections. An optional independent eval model judges saved raw responses against authored criteria, but the evaluative output is surfaced to the operator and is not automatically an agent-owned correction of the live platform.

## S1 — Operations

- State: A
- Function: Carry out each person's ongoing task through a persistent model-backed sandbox agent, producing conversations, external tool operations, generated files, scheduled results and peer-task reports.
- Disturbance / variety regulated: Varied user requests, observed tool/API replies, interrupted/background execution, missing context, changing external information and new conversation steering.
- Decisive decision or feedback right: The hosted model-backed agent chooses task interpretation, tools, subsequent reasoning/actions, memory updates and response content within granted scope.
- Decision owner: Running bundled jcode-backed agent in each hosted OneCLI sandbox; the external model/Jcode engine supplies inference, while OneCLI provides a first-party supported operational deployment and protocol adapter.
- Supporting / enforcement mechanisms: Hosted agent model selection, API turn queue, supervisor/jcode adapter, transport, durable home, toolbox, runner resource limits and gateway authorization/injection.
- Closure path: Human or scheduled request → API dispatched turn → runner sandbox/supervisor → model-directed action and platform tools → external feedback → further action/report persisted to the conversation and readable by the user.
- Boundary reachability: Default documented self-hosted setup provisions the agent image/runner, first-party supervisor uses real `jcode` rather than fake adapter, and deployed agent receives explicitly configured grants. The functionality is not inferred from an adjacent development/e2e test.
- Why this is / is not agent-owned: Without the activated model actor, supervisor and gateway still route, reject and record requests but do not decide the work to perform.
- Evidence: [hosted operator mode](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/README.md#the-agent); [supervisor real harness contract](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/README.md); [adapter launch](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/src/harness/jcode.ts); [tool and peer capabilities](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/src/capabilities/agents.ts).
- Basis: Explicit first-party supported hosted model loop and operational closure through real platform tools.
- Confidence: High for source wiring; no claimed observed live-provider effectiveness.
- Caveats: The standalone BYO/gateway-only mode is not an autonomous first-party hosted S1; an operator must enable a runner, sandbox image, provider and granted tools.

## S2 — Coordination

- State: C
- Function: Attenuate repeated agent-to-agent conversational oscillation, parallel asks to a busy agent pair and uncontrolled cross-agent message bursts while retaining task return to the initiating person.
- Disturbance / variety regulated: Two separate agents can start a cyclic message exchange, a second person task may collide with the pair's existing active task, or unanswered repeated sends can multiply approval holds.
- Decisive decision or feedback right: Peer agents choose what to say and when to finish; the first-party peer-task contract supplies one-active-per-pair admission, bounded FIFO, per-side message budgets, timeout/close/recovery and human continuation. The bound and queuing policies are deterministic rather than an autonomously revised coordination judgment.
- Decision owner: First-party API policy and pair state for conflict-specific attenuation, with operator consent/continuation; a separate autonomous conflict-resolution owner is not built by the pair state alone. Agents can compose their own higher-level coordination under the shipped specific `complete_task`/feedback path.
- Supporting / enforcement mechanisms: `PeerTask` unique pair/open index, conditional spend, pending-hold limits, app-turn cap, bilateral link access decisions, `message_agent`, `complete_task`, sweep and report materialization.
- Closure path: Agent A's person-sourced request reaches agent B → active task fence serializes competing pair tasks, turn budget limits ping-pong and return notices instruct A/B to finish → A's report (or terminal close notice) reaches the initiating person's conversation; queued task can then begin.
- Boundary reachability: The agent roster exposes `message_agent` and `complete_task` for actual hosted agents; both services are wired through API and platform tool bridge, with pair lifecycle also handled by normal turn-service. Unlike bare generic message transport, this is a shipped disturbance-specific loop backstop.
- Why this is / is not agent-owned: Agents own message content and completion decisions but the decisive *interference attenuation* rules are deterministic/human-controlled; thus the first-party S2-specific construction path supports C, not automatic A.
- Distinct S1 units: Two separately configured hosted agents with a first-party `AgentLink` relationship.
- Inter-S1 disturbance: Runaway two-way model chatter, repeated pending approval cards, or multiple person-originated tasks competing for the same active pair.
- Attenuating coordination relation: Per-pair open-task invariant, FIFO admission, budgets/cap, bilateral consent and close/report protocol.
- Feedback into subsequent S1 behaviour: Agent receives explicit refusal/remaining-budget/close notice, stops or completes its peer conversation; queued task starts only after prior pair task closes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The code names and controls actual paired-agent ping-pong, competing concurrent pair tasks and repeated holds; the closing report returns to task initiator, rather than merely passing a message.
- Evidence: [agent link coordination and loop backstop](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/channels/agent-link-service.ts), [task uniqueness/budgets/FIFO](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/channels/peer-task-service.ts), [bounded agent tools](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/src/capabilities/agents.ts).
- Basis: Explicit conflict/oscillation-specific pair-state control; constructor-level autonomous coordination, not demonstrated model-owned conflict adjudication.
- Confidence: Medium-high for structural witness, medium for autonomous composition of conflict response.
- Caveats: A generic agent message is not S2, and the gateway policy's generic API authorization is not S2 by itself. No distinct first-party autonomous mediator is shown.

## S3 — Inside-and-now control

- State: P
- Function: Maintain the workspace's current capacity, access and operational coherence across hosted agents under one legitimate workspace operator.
- Disturbance / variety regulated: Multiple agents' simultaneous resource demand, inappropriate access to team connections and secrets, stalled/current background work, changing agent assignments and revoked grants.
- Decisive decision or feedback right: The authenticated workspace owner/operator chooses or revises the current agent complement, each agent's brief/model, connection grants and workspace policy; the runner schedules/limits what executes and the gateway enforces effective policy without selecting the original constraints.
- Decision owner: Legitimate workspace owner in the documented operator dashboard mode. No agent-owned workspace-wide current-resource/budget allocator is established by the deterministic runner.
- Supporting / enforcement mechanisms: Workspace overview/activity, agent management, grants/policy engine, runner placement and sandbox limit, gateway denial/injection, agent brief update and home-sync.
- Closure path: Owner sees workspace agent/current background status or access requirement → revises agent membership, brief, model or policy/grant → API persists the decision → home-sync/runner/gateway changes subsequent agent actions or accessible resources.
- Boundary reachability: Workspace operator dashboard, API and runtime enforcement are a supported core self-hosted mode, unlike optional enterprise-only organization-wide policy/SSO. Real hosted agents receive live instruction changes and constraints.
- Why this is / is not agent-owned: Hard gateway policy and runner cap have no authority to choose revised current obligations; those return from workspace operator. The individual S1 agent's choice of a tool within policy is not the S3 decision.
- Whole-system current view: Workspace overview supplies current agent count/background activity and recent access events; agent list/policy exposes individual current units and their grants.
- Current-control decision scope: Add/remove/reconfigure running agent, revise effective shared resource/connection constraints and workspace obligations, with immediate or next-turn enforcement.
- Evidence: [workspace overview](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/web/src/app/%28dashboard%29/w/%5BworkspaceId%5D/overview/_components/overview-content.tsx), [workspace policy backend](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/policy-service.ts), [current control and home-sync](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/agent-service.ts), [runner ceilings and operator mode](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/runner/README.md).
- Basis: Explicit first-party workspace operator mode with actual whole-current resources and returned enforcement.
- Confidence: Medium; current control is operator-owned rather than autonomously optimized across agents.
- Caveats: A workspace's global access policy is not a self-updating agentic S3, and this does not import paid organization-wide EE roles. Status dashboards alone would not suffice without owner decisions and live return.

## S3* — Complementary audit

- State: C
- Function: Supply separately scored, question-specific checks of actual hosted-agent answers and tool use beyond the ordinary agent's own completion report.
- Disturbance / variety regulated: Silent regressions after changes in model/data/brief, plausible but incorrect answers, and false claims of external app usage.
- Decisive decision or feedback right: A separate optional test job obtains new direct agent-turn output and compares it with owner-authored reference criteria; for custom checks, a model judge decides per criterion in isolated no-tools context. The operating owner must choose any subsequent brief/permission/capability fix from dashboard evidence.
- Decision owner: User-authored eval criteria and operator remediation; an isolated first-party model-judge constructor can supply autonomous audit judgments in the optional eval mode, but auto-correction/current-control return is not fully wired.
- Supporting / enforcement mechanisms: Agent Eval question and run rows, regular agent turn entry, raw answer/app event attribution, deterministic numeric/text checks, criterion-specific `eval-judge.ts`, schedule cron, run history/previous comparison and evals UI.
- Closure path: User defines test criteria → manual or scheduled ordinary agent test turn → independent check/judge reads actual answer and app evidence → stored pass/fail and comparison exposed to owner → owner may revise brief/model/grants in ordinary dashboard → next runtime turn/next evaluation reflects that change. Automatic autonomous corrective selection is not demonstrated.
- Boundary reachability: These features are in the standard hosted agent's Evals page and server-side job path, not merely developer CI; the optional judge uses a model key available to the same hosted agent with a separate constrained prompt.
- Why this is / is not agent-owned: The optional judge's independent per-answer classification is model-mediated, while the decisive remediation remains an owner action; this is a function-specific construction and evidence-return surface, not established closed autonomous S3* operation.
- Claim being audited: The hosted agent's response satisfied a question's known expected facts and used specified external apps.
- Ordinary reporting path: The agent's user-visible answer and its own self-report in the conversation.
- Complementary access path: A separate eval conversation gets a fresh response, server collects actual turn answer/gateway app attribution; model judge sees raw answer and authored criteria, without the agent's normal tool authority.
- Independence boundary: The audit model executes in a separate server-side constrained call with no tools, but may use the **same configured model** as the S1 actor; neither provider independence nor independent human ownership is claimed.
- Who acts on findings: Operator reviewing persisted eval results, scheduling regression checks and manually editing agent brief/model/settings; the runtime does not automatically patch an agent from failed test results.
- Evidence: [real-turn scoring](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/agent-eval-service.ts), [independent no-tools model judge](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/eval-judge.ts), [scheduled regression tests](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/eval-schedule-service.ts), [hosted eval dashboard](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/web/src/app/%28dashboard%29/w/%5BworkspaceId%5D/agents/%5BagentId%5D/evals/_components/evals-section.tsx).
- Basis: Explicit first-party audit-specific construction surface; no claimed closed independent autonomous corrective return.
- Confidence: Medium; model judge and saved evidence are wired, but feedback from findings to actual corrected operation is owner-mediated.
- Caveats: Not every numeric check or CI test is a model audit; this assessment does not run paid provider judging or measure judge efficacy. Treating eval verdict as automatic agent improvement would overstate source.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would sense future/outside changes, create adaptation options for the workspace's agent capability and return a selection into current S3 operations.
- Disturbance / variety regulated: Prospective model/provider, business environment and tooling changes rather than known requests or recent answer quality.
- Decisive decision or feedback right: Agents can receive new instructions, schedule future work and update retained memory, and evals can detect regressions; no separately chartered outside-and-then adaptation owner/choice/whole-workspace return is wired.
- Decision owner: Human operator controls model/brief/permissions; current agent pursues tasks within those inputs.
- Supporting / enforcement mechanisms: Model-override config, memory, schedule tools, test regression UI, ordinary project release updates.
- Closure path: A scheduled task returns a result or a regression test alerts its owner, possibly prompting a future manual edit; there is no evidenced systematic externally prospective option generation and commitment into workspace S3 capability.
- Boundary reachability: The cited schedule/eval mechanisms are shipped, but their declared roles are current work/test execution, not a standing future-environment intelligence subsystem.
- Why this is / is not agent-owned: The ability to do later work or edit model selection is not by itself S4 regulation of outside future variety.
- Evidence: [agent scheduled tasks](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/src/capabilities/crons.ts), [scheduled eval scope](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/eval-schedule-service.ts), [operator model and brief edits](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/agent-service.ts).
- Basis: Bounded negative at the team workspace recursion, not impossibility of future custom extensions.
- Confidence: Medium-high.
- Caveats: A user can create externally focused scheduled tasks, but generic goal expressiveness is not a first-party standing S4 mandate.

### Absence scope

- Surfaces inspected: Current sandbox capability registry, scheduled task semantics, memory persistence, owner model/brief controls, per-agent eval cron and workspace settings.
- Plausible first-party paths checked: Autonomous model/provider scouting, prospective external trend capture, strategy alternative comparison and returned cross-agent capacity change; optional parent future-strategy decision versus ordinary per-agent reconfiguration.
- Why no material first-party path remains: The inspected shipping modes provide task execution, current regression monitoring and operator-set configuration, but no distinct outside-and-then future-strategy decision cycle that closes into the current workspace metasystem.

## S5 — Policy and identity

- State: —
- Function: Would adjudicate an ultimate workspace mission/constitutional identity dispute, have legitimate binding authority decide it, and return the decision to govern later operation.
- Disturbance / variety regulated: Fundamental organizational purpose/legitimacy conflicts, as opposed to API request safety, individual agent brief content or ordinary task permission.
- Decisive decision or feedback right: The operator authors the agent's brief and workspace access policy. The agent may suggest a brief edit, and the platform enforces a human change, but there is no first-party identity/ultimate-policy **dispute and governing decision** path at the workspace recursion.
- Decision owner: Humans outside the agent workspace supply the mission and its limits; the runtime does not arbitrate their legitimacy or negotiate the organization's ultimate identity.
- Supporting / enforcement mechanisms: Read-only generated agent brief, authenticated operator edits, workspace policy/grant rules, human approval cards and gateway enforcement.
- Closure path: Operator changes an agent's standing brief/policy → home-sync or gateway changes its next actions. This closes an ordinary subordinate identity/configuration edit, **not** an evidenced constitutional identity dispute of the workspace as a whole.
- Boundary reachability: Agent brief editing and policy are shipped in the core OSS workspace mode, but no ultimate-policy deliberation/legitimacy mechanism is present simply because these settings are editable.
- Why this is / is not agent-owned: Current task routing, grant approval and changing one worker's persona do not establish system-level legitimate policy arbitration. Human custody alone is not sufficient for S5=P.
- Evidence: [agent identity/brief source](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/sandbox-supervisor/src/home/renderer.ts), [ordinary operator brief UI](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/apps/web/src/app/%28dashboard%29/w/%5BworkspaceId%5D/agents/%5BagentId%5D/_components/instructions-section.tsx), [API update and home return](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/agent-service.ts), [workspace policy enforcement](https://github.com/onecli/onecli/blob/6eaf8780f6310587ae86906eb9573ab531e92c12/packages/api/src/services/policy-service.ts).
- Basis: Bounded no-path conclusion for ultimate team identity-policy return.
- Confidence: Medium.
- Caveats: At a **single individual agent** recursion, operator authoring of its fundamental brief would merit its own S5 assessment; it is not imported to the workspace-level system without evidence of a whole-workspace identity question and closure.

### Absence scope

- Surfaces inspected: Operator-authored agent identity/brief instructions, agent's suggestion permission, API update path, workspace/enterprise policy boundary and approval/grant governance.
- Plausible first-party paths checked: Escalation of ultimate workspace purpose, competing authority/constituency claims, parent adjudication and durable returned policy over all agents versus ordinary security/configuration edits.
- Why no material first-party path remains: Available decisions concern one agent's brief, product-granted permissions, routine human approvals and workspace resource controls; no evidenced first-party constitutional/legitimacy decision loop at this team recursion is established.

## Distributed OSS parent arrangement

The OneCLI project contributors, vendor organization and EE licensing policy govern development/distribution, not a particular user's hosted workspace. Operators of multiple self-hosted installations do not share a parent current-control or identity loop merely through the public repository. Workspace S3=P is local operator control, not an imported maintainer S5.

## Self-hosted and non-human modes

An operator can self-host the Apache core and keep human S3 decisions while hosted agents perform individual tasks. Native jcode swarm helpers are vendor-level recursive workers visible to the OneCLI supervisor, not by themselves cross-agent workspace S2/S3 owners. A BYO-only configuration lacks the credited first-party OneCLI hosted operational loop. Paid `ee/` organization policy is not part of the selected OSS shipped mode. None of these modes warrants `(P)` on a positive autonomous base state without a separately closed parent mode.

## Recursion

Each hosted sandbox is a local agent work unit, potentially with vendor helpers as subunits. OneCLI workspace control spans those units through human configuration, pair communication fences and common runtime. Upstream product development and an employer's corporate strategy are higher, outside recursions.

## Variety and escalation

The agent absorbs task variety by model-directed tools in an isolated environment. Cross-agent repeated/colliding requests are damped by pair-specific bounded commitments, while human owners settle communication consent and grant exceptions. Current resource constraints and policy are enforced by gateway and runner, with decisions reserved to operator. Eval disagreement is an evidence signal to an operator, not automatically a repaired agent. Permission denial, missing model key, exhausted pair budget, lack of runner and an inconclusive judge must remain visible as genuine limits.

## Evidence gaps

- No live agent/provider/browser execution was performed for this assessment; real installed behavior was traced from first-party pinned source and the tested/designated runtime entry points.
- Distinct S1 agent collaboration is documented, but automatic agent-selected **conflict-specific** coordination resolution is not; hence S2 is narrowly C for shipped inter-agent oscillation controls.
- S3=P relies on a legitimate workspace operator using a whole-current dashboard/policy mode, not autonomous orchestration or EE organization controls.
- An isolated optional model judge can use the same base model and has no automatic fix wire; S3*=C is a constructor-level audit path, not proven independent autonomous correction.
- This assessment did not install monorepo dependencies or run upstream provider-required/live/e2e suites; version-pinned Index contract and deterministic repository checks remain the publication gate.
