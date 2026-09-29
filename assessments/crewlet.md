---
harness_id: crewlet
project_name: Crewlet
repository: https://github.com/crewlet/crewlet
review_ref: 346d58ee3f3627a7f1213e441c6b0e330ab48030
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: P
---

# Crewlet

## Review boundary

- System in focus: the first-party Crewlet agent-company engine at frozen revision `346d58ee3f3627a7f1213e441c6b0e330ab48030`, including per-seat turn engines, the Execute→Review loop, organization hierarchy, native work/knowledge surfaces, delegation and colleague communication, learning, live company configuration, human seats, and fleet-wide coordination machinery.
- Purpose and identity: run a persistent organization of AI-agent and optional human seats that performs real work, allocates and reviews current commitments, learns from prior operation, and remains governed by a live mission/vision/policy document.
- Relevant environment: external model providers, users/stakeholders, chat and PM/code/knowledge surfaces, provider-managed coding agents, infrastructure nodes, and founder/operator authority.
- Standard-distribution boundary: Crewlet's engine, per-seat prompts/tool loops, organization model, native tracker/knowledge surfaces, event/coordination stores, reviewer, learning subsystem, human-seat routing, live Tier-B configuration and control-plane apply path are inside. External LLM cognition, optional Claude Code/OpenCode cognition, third-party PM/chat/code-host internals and humans themselves remain external actors even when Crewlet gives them first-party seats/authority paths.
- Credited operating / distribution surfaces: ordinary agent-seat turns; multi-seat organizations with lead-agent task allocation; supported human-lead organizations; the native tracker conflict-serialization path; mandatory Execute→Review turns; shipped post-turn learning and skill synthesis; cross-agent skill promotion; founder/operator live company configuration.
- Adjacent first-party surfaces excluded from ownership: repository development/governance, tests/CI, documentation examples as actors, dashboard observation by itself, static org-chart topology by itself, and deterministic fleet infrastructure unless tied to a specific VSM function.
- First-party operating / deployment modes considered: agent-led teams; human-led AI teams; root human founder above top agents; one-node or fleet deployment; native tracker where first-party work-conflict evidence is needed; ordinary learning-enabled agent seats.
- Recursion level: AI seats are S1 operational units at team/company recursion. A lead seat can supply team-level current control. Per-seat learning is a recursive adaptation capability that changes later operational behavior; cross-agent promotion supplies a parent-governed team-level adaptation mode. Parent modes are credited only where Crewlet explicitly wires human authority back into agent operation.
- Reviewed revision: `346d58ee3f3627a7f1213e441c6b0e330ab48030`.
- Observation date: 2026-09-29.

## Repository architecture

Crewlet runs one persistent organizational seat identity per role, but builds a fresh runner for each turn. A trigger wakes a seat into an Executor phase where the model chooses and executes tools, followed by a separate Reviewer phase with its own prompt/model surface and only a structured `submit_review` decision. Review can accept, fail, or return `self_iterate`, which starts another Executor round with an engine-recorded prior-work ledger.

The organization model is executable: lead agents receive rosters of reports and assign current work by reasoning about their profiles. Native tracker changes are recorded on a fleet-wide ordered log, and competing writes on one work item contend at that shared ordering point. Human seats are first-class hierarchy members and can lead units or sit as a root founder; their replies on ordinary work surfaces re-enter the agent notification path.

The learning subsystem consumes completed operational turns into durable diary entries, episodes, synthesized skills and counterparty models. Automated synthesis can create reusable per-seat skills for future turns, while cross-agent convergence can produce a hidden team-knowledge draft that requires a person to publish. Separately, Crewlet's live Tier-B company document is founder-owned and includes the company name, mission, vision and policies; versioned API updates propagate across the fleet without restart and are rendered into later agent prompts.

Primary evidence:

- [`README.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/README.md)
- [`docs/concepts/turn-engine.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/turn-engine.md)
- [`docs/concepts/agent-runtime.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/agent-runtime.md)
- [`docs/concepts/organization-model.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/organization-model.md)
- [`docs/concepts/task-engine.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/task-engine.md)
- [`docs/concepts/coordination.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/coordination.md)
- [`docs/concepts/agent-learning.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/agent-learning.md)
- [`docs/concepts/humans-in-the-org.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/humans-in-the-org.md)
- [`docs/concepts/configuration.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/configuration.md)
- [`docs/concepts/decision-framework.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/decision-framework.md)

## Operational model

A seat receives a routed trigger, pins the current organization epoch, and executes an agentic tool loop against its authorized surfaces. The engine checks delivery claims against its own recorded calls and then invokes a separate reviewer. In a team, a lead agent can inspect work through the shared tracker and reason over its report roster to assign or revise current commitments; report transitions and results return through normal notifications. Durable learning from completed turns can change future turns. At the parent boundary, humans can be explicit managers/founders and can change the live company definition through authenticated configuration.

## S1 — Operations

- State: A
- Function: perform real organizational work through autonomous per-seat agent turns.
- Disturbance / variety regulated: changing user/work-item requests, external tool state, provider responses, tool errors, knowledge gaps, interruptions, budget limits and results encountered while completing a seat's assigned work.
- Decisive decision or feedback right: choose the next substantive tool/action or response after observing current task context and prior tool results.
- Decision owner: the model-driven agent seat in the Executor phase.
- Supporting / enforcement mechanisms: per-seat runner, tool loop, MCP/builtin surfaces, collaboration/skill guards, budgets, delegation guards, inbox/event routing, sandbox suspension/resume and delivery verification.
- Closure path: trigger → Executor model decision → first-party tool execution → result appended to the same turn → later model decision → submitted work → reviewer/engine disposition and external result.
- Boundary reachability: this is the normal shipped seat execution path; optional external coding agents are not required for the positive S1 path.
- Why this is / is not agent-owned: deterministic engine code constrains and records execution, but the seat model owns substantive next-action choice in the work loop.
- Evidence: [`docs/concepts/agent-runtime.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/agent-runtime.md); [`docs/concepts/turn-engine.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/turn-engine.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider-side model internals remain external; credit rests on the first-party closed agent/tool execution path.

## S2 — Coordination

- State: C
- Function: attenuate conflicting concurrent mutation of shared current work among distinct agent-seat S1 units.
- Disturbance / variety regulated: two seats can race to change the same native work item, producing incompatible concurrent state if writes are accepted independently.
- Distinct S1 units: independently executing Crewlet agent seats operating against the same company's native tracker.
- Inter-S1 disturbance: concurrent writers targeting one work item compete over the same shared work state.
- Attenuating coordination relation: the native tracker publishes writes onto the item's ordered shared log; the broker arbitrates competing writes so two writers racing on one task contend at one ordering point and exactly one wins, while unrelated tasks do not contend.
- Feedback into subsequent S1 behaviour: write results expose `applied`, `pending`, or `unknown`, nodes replay the same ordered record, and subsequent reads/notifications present the serialized work state back to seats for later action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is tied to an explicit same-item concurrent-write conflict and a mechanism specifically preventing divergent acceptance, not to Crewlet's generic bus, hierarchy, task routing, or delegation.
- Decisive decision or feedback right: deterministic shared-log/broker arbitration establishes which competing mutation wins and therefore which state later S1s observe.
- Decision owner: no autonomous agent owns the arbitration decision for a concrete write race; the first-party runtime supplies the function-specific deterministic coordination path.
- Supporting / enforcement mechanisms: ordered native work log, per-object contention, applied-position tracking, operation identity and same-write read-after-apply behavior.
- Closure path: concurrent S1 writes → shared ordered arbitration → one canonical ordered state/outcome → replicated tracker state and notifications → later S1 decisions use that state.
- Boundary reachability: this path is part of the shipped `native` tracker backend, one of Crewlet's documented standard work modes.
- Why this is / is not agent-owned: S2 itself is materially closed first-party, but the collision resolution is deterministic rather than selected by an autonomous coordination actor, so constructor credit is appropriate.
- Evidence: [`docs/concepts/task-engine.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/task-engine.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: lead assignment, mailboxes and the generic coordination store are not independently credited as S2; the positive witness is the explicit concurrent shared-work collision path.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current team commitments and allocation across active operational seats, with both autonomous lead-agent and human-lead modes.
- Disturbance / variety regulated: new work, blocked work, changing report capacity/fit, parallel task progress and completed/failed results require present-tense assignment, reassignment, review or intervention for the team as a whole.
- Whole-system current view: at team recursion the lead receives a roster of direct reports and can inspect the team's current tracker/work surfaces; assignment and transition notifications return current work changes to the relevant lead/manager.
- Current-control decision scope: choose which report receives work, create/assign subtasks, react to blockers and progress, review results, revise current commitments and close/transition parent work.
- Decisive decision or feedback right: in agent-led mode the lead model reasons over roster/current work and chooses allocation/intervention; in human-led mode the human lead makes the same current-control decisions through the PM/chat surfaces and those changes wake affected agent seats.
- Decision owner: autonomous lead agent in the base mode; legitimate human lead in the first-party parent-governed mode.
- Supporting / enforcement mechanisms: executable org hierarchy, `manages`/unit lead relationships, lead roster prompt, native/external tracker routing, assignment webhooks, colleague tools, human-seat identity/routing and event delivery.
- Closure path: current work/report state → lead decision → tracker/chat assignment or intervention → affected seat wakes/changes current work → progress/transition returns to lead and informs later control.
- Boundary reachability: both agent leads and human leads are explicitly supported standard organization modes; human seats can lead units and agent work returns through the same integrated work surfaces.
- Why this is / is not agent-owned: the base task-allocation choice is explicitly described as lead-agent reasoning rather than routing code; the parent mode separately gives that decision right to a human lead and returns the result through first-party routing.
- Evidence: [`docs/concepts/organization-model.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/organization-model.md); [`docs/concepts/task-engine.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/task-engine.md); [`docs/concepts/humans-in-the-org.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/humans-in-the-org.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a lead title or one-shot delegation is not the witness; credit rests on the documented current-work allocation/review loop and its return through work-state notifications.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Lead agent model | New/current team work, blocker, progress/result | Lead reasons over roster/work state → assigns/reviews/intervenes → work-state notifications affect reports and later lead turns | organization model; task engine |
| Parent (`P`) | Human lead seat | Same team-level current-control need | Human changes/answers on PM/chat surface → inbound event/assignment wakes agent → later progress returns on shared surface | humans-in-the-org; organization model |

## S3* — Audit / monitoring

- State: A
- Function: independently challenge an operational seat's claim about completed work using a separate reviewer with direct engine-recorded evidence and return the judgment into the same turn's control.
- Disturbance / variety regulated: an Executor can claim delivery or quality that its actual tool record does not support, or can produce plausible prose while failing to reach the required external surface.
- Claim being audited: whether the round's work is actually good enough to finish and consistent with what the engine recorded as executed/delivered.
- Ordinary reporting path: Executor's own `submit_work` outcome, summary, claimed deliveries and produced text.
- Complementary access path: a separate Reviewer prompt/model receives the round's verbatim engine-recorded tool log and work text on a tool surface with no domain tools; engine-side delivery checks additionally compare claims to recorded calls and destinations.
- Independence boundary: Reviewer has its own prompt/model phase and narrower tool surface, and the evidence includes engine-recorded calls rather than only the Executor's self-report. It is therefore materially distinct from ordinary production reporting even though it is routinely invoked.
- Who acts on findings: Reviewer can return `self_iterate` or `failed`; `self_iterate` sends the turn back to a fresh Executor round with the prior-work ledger, and engine overrides can also force correction when a claimed delivery did not reach the waiting party.
- Decisive decision or feedback right: the reviewer model owns the quality judgment among `done`, `self_iterate`, and `failed`, subject to stricter deterministic delivery truth checks.
- Decision owner: autonomous Reviewer model actor.
- Supporting / enforcement mechanisms: phase-separated prompts/models, forced `submit_review`, engine-recorded call ledger, delivery `Check`/`OverrideDone`, prior-work ledger, stall/iteration guards.
- Closure path: Executor result + direct execution record → separate Reviewer judgment → `self_iterate`/failed/done → next Executor round or termination → later operation reflects the audit finding.
- Boundary reachability: Execute→Review is the documented ordinary turn engine, not a development-only evaluator.
- Why this is / is not agent-owned: deterministic checks enforce facts such as whether a write landed, while the separate reviewer model owns the substantive quality/challenge judgment that can send work back.
- Evidence: [`README.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/README.md); [`docs/concepts/turn-engine.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/turn-engine.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the positive mapping does not rely on a component merely named reviewer; it relies on separate access to engine-recorded reality plus corrective return into execution.

## S4 — Intelligence / adaptation

- State: A(P)
- Function: derive durable future-operating adaptations from completed work, with an autonomous per-seat learning mode and a parent-governed team-knowledge promotion mode.
- Disturbance / variety regulated: repeated external work patterns, failures and successful tool trajectories reveal procedures or knowledge that should change how later turns operate; cross-seat convergence can reveal team-level practice worth adopting.
- External distinction: learning consumes settled operational turns containing actual tool sequences, review outcomes, counterpart interactions and task results against the company's work environment rather than only internal planning text.
- Future / prospective distinction: synthesized skills, diary/episodes and promoted team practices are retained specifically for future turns; clustered synthesis searches repeated historical trajectories for reusable patterns not needed merely to finish the current turn.
- Adaptation option generated: auxiliary-model synthesis drafts reusable per-seat skills; cross-agent promotion distils convergence among distinct seats into a team knowledge draft.
- Path back into current capability / S3: synthesized skills are stored per seat and exposed to later turns through the skill catalogue/`use_skill`; a parent-published cross-agent draft becomes an ordinary team knowledge page reachable by future query-time search.
- Decisive decision or feedback right: in base mode an auxiliary model can draft/decline a reusable skill and first-party learning stores the admitted result; in parent mode a person/lead decides whether an auto-drafted cross-agent practice is published into live team knowledge.
- Decision owner: autonomous auxiliary learning model in the base mode; human/parent reviewer for cross-agent team-practice publication.
- Supporting / enforcement mechanisms: post-turn Reflector, episodes, PersistDecider, Synthesizer, duplicate/cap gates, clustered synthesis, Promoter, hidden auto-draft subtree, synthesized-skill store, query/prefetch and `use_skill`/`refine_skill` tools.
- Closure path: completed operational evidence → synthesis/proposal → durable skill or parent-reviewed team draft → future prompt/search/tool access → later agent behavior changes.
- Boundary reachability: post-turn learning is a shipped engine subsystem; cross-agent promotion is a shipped background duty and publication path, not repository-development learning.
- Why this is / is not agent-owned: model-based synthesis supplies autonomous future-oriented adaptation in the base mode; the separate team-promotion path deliberately holds publication for parent/human judgment rather than silently sharing agent-generated policy.
- Evidence: [`docs/concepts/agent-learning.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/agent-learning.md); [`docs/concepts/agent-runtime.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/agent-runtime.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic memory or reflection is not the witness; credit rests on evidence-derived reusable skill/practice options with explicit reuse in later operation. The team promotion path remains parent-governed because the draft is hidden until a person publishes it.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Auxiliary learning model | Settled operational turn / repeated episode pattern | Model drafts reusable skill → runtime stores it → later executor sees/uses/refines it | agent-learning |
| Parent (`P`) | Human/lead reviewer | Similar procedures converge across distinct seats | Promoter writes hidden team draft → person publishes → future team knowledge search exposes it to agents | agent-learning |

## S5 — Identity / ultimate policy

- State: P
- Function: close company identity and ultimate-policy decisions through founder/operator authority and propagate those decisions back into subsequent agent operation.
- Disturbance / variety regulated: questions that change what the company is for or what ultimate policies govern it — mission, vision, company-wide policies and top-level direction — exceed ordinary seat-level task authority.
- Identity / ultimate-policy issue: Tier-B configuration explicitly defines company `name`, `mission`, `vision` and `policies`; top agents can escalate decisions above their authority to a root human founder whose documented responsibility is to own direction/final calls.
- Ultimate authority in each claimed mode: parent-governed only — the legitimate founder/operator owns Tier-B company configuration through authenticated API/operator credentials; the founder human seat supplies the organizational escalation identity while configuration authority remains the distinct operator hat.
- Return-to-operation path: founder/operator decision → versioned `PUT/PATCH /config` or import of the Tier-B document → activation pointer/control-plane apply across nodes → new epoch → later Executor prompts render the updated mission, vision and full policy text and agents operate under it.
- Decisive decision or feedback right: decide and authorize company identity/ultimate-policy changes and activate the resulting company revision.
- Decision owner: legitimate parent human founder/operator; no autonomous Crewlet agent is shown holding ultimate configuration authority.
- Supporting / enforcement mechanisms: human founder seat at org root, escalation via normal colleague surfaces, authenticated API tokens, versioned Tier-B config, validation, activation pointer, fleet reconcile/hot reload and per-turn epoch pinning.
- Closure path: identity/policy matter reaches founder → founder decides and exercises operator configuration authority → live revision propagates → subsequent agent turns receive changed mission/vision/policies.
- Boundary reachability: root human founder seats and live founder-owned Tier-B configuration are both documented first-party deployment surfaces; the docs explicitly distinguish the founder's colleague seat from the operator credential rather than conflating them.
- Why this is / is not agent-owned: ultimate identity authority is intentionally human/parent-owned. Static mission/policy text alone would not earn S5; credit comes from the live authenticated parent decision-and-return path.
- Evidence: [`docs/concepts/humans-in-the-org.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/humans-in-the-org.md); [`docs/concepts/configuration.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/configuration.md); [`docs/concepts/agent-runtime.md`](https://github.com/crewlet/crewlet/blob/346d58ee3f3627a7f1213e441c6b0e330ab48030/docs/concepts/agent-runtime.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary task approval is not S5. The positive claim is restricted to founder-owned live identity/ultimate-policy fields and their explicit propagation into later runtime behavior.

## Recursion

Crewlet is unusually explicit about recursion: each seat is itself a durable viable work unit with local memory/learning and tools, while the team/company layer adds lead control, inter-seat work coordination, complementary review and parent governance. The assessment does not infer recursion from the org chart alone; each positive metasystem state above identifies an operating closure at its claimed level.

## Variety and escalation

Crewlet attenuates runtime variety through bounded tool rounds, token budgets, delegation slices/depth, worker safety surfaces, shared work serialization, queueing and fleet leases. Agent-detected blockers move through ordinary colleague surfaces to a manager; reviewer-detected blockers return through `self_iterate` so the next Executor round performs that outreach. Human seats form an explicit escalation terminus without inventing a separate engine-side sender.

## Evidence gaps / terminal outcome

Proposed vector: `S1=A / S2=C / S3=A(P) / S3*=A / S4=A(P) / S5=P`.

The strongest distinctions are functional rather than nominal: S2 rests on an explicit shared-work collision rather than the file named `coordination`; S3 rests on lead reasoning plus current work feedback rather than the org-chart shape; S3* rests on a separate reviewer with engine-recorded evidence and corrective return; S4 rests on durable future skill/practice adoption rather than memory alone; S5 rests on the live founder-owned identity/policy revision path rather than policy text or ordinary approvals.
