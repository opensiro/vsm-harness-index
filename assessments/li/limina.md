---
harness_id: limina
project_name: Limina
repository: https://github.com/theam/limina
review_ref: 56a4e2f3c9c613c7bc61f6a260ade379b21cd782
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: P
---

# Limina

## Review boundary

- System in focus: one Limina mission-bound autonomous research project, including its first-party managed-runtime and template operating modes, rather than the organization developing Limina.
- Purpose and identity: turn an operator-defined measurable research challenge into hypotheses, experiments, findings, and a reviewable decision trail, including reconsideration of a failing research direction.
- Relevant environment: research literature, datasets and baselines, external services and repositories, experimental outcomes, provider engines, teammates' steering, resource limits and failures.
- Standard-distribution boundary: documented managed Codex/Claude Code project supervisor with canonical database, project-scoped research commands and provider continuations; alternative first-party generated local-repository template with AGENTS.md, kb protocol, hooks and installable companion skills. Optional template skills are credited only in the documented installed/template mode.
- Credited operating / distribution surfaces: managed src/limina_cloud/supervisor.py, runtime.py, research_service.py, service.py, operations.py and database-backed coordination; first-party AGENTS.md, templates, local research skills, setup/installation and kb scripts for the documented template mode.
- Adjacent first-party surfaces excluded from ownership: repository's own kb/ product-development research instances, docs/reviews and dogfood reports, development/test fixtures, CI, issue/governance infrastructure and hypothetical deployment extensions. A repo-local test or sample does not itself operate a user's research project.
- First-party operating / deployment modes considered: server-managed single-project Codex or Claude continuations, optional engine subagent experiment lanes, live/asynchronous parent steering and lifecycle controls, and the installed project-template mode in a user-operated Codex/Claude session.
- Recursion level: one research mission and its evidence-producing work cells; multiple unrelated Limina projects are separate units, not automatically one shared higher-level organization.
- Reviewed revision: 56a4e2f3c9c613c7bc61f6a260ade379b21cd782.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Limina has two declared distribution modes. The managed runtime owns an asynchronous project supervisor, one selected provider engine, a persisted continuation, scoped child capability, workspace, canonical H→E→F research graph and structured coordinator checkpoint. The model chooses substantive research steps and next objectives; Python and database transactions supply leasing, authorization, idempotent writes, retry scheduling and provider recovery. Codex/Claude SDKs are external engines, not a separate first-party policy organization. Multiple experiment lanes can use project-scoped capabilities but cannot claim the same experiment lease simultaneously. Human users create a mission, inspect progress and research evidence, and asynchronously steer, pause or stop current work through shared REST/CLI/MCP interfaces. The template is a separate supported local operating path: agent instructions, an editable mission/ACTIVE knowledge base, H/E/F validators, skill routing, optional installed literature and devil's-advocate skills, and a user-operated provider session. Templates for challenge and strategic reviews are optional, not evidence that a separate auditor runs automatically.

Primary architecture evidence: [README modes and research loop](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/README.md#L25-L149), [managed runtime architecture and human contract](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/docs/cloud-runtime-architecture.md#L1-L48), [project supervisor and private continuation](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L227-L259), [agent checkpoint and return path](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L351-L479), [project-template research contract](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/AGENTS.md#L1-L90).

## Operational model

The base operational output is an evidence-grounded research decision. The model forms and tests hypotheses and publishes findings through project-scoped tools, or writes corresponding kb artifacts in template mode. The managed project has one top-level discretionary agent session, but its internal experiment lanes can produce independent observations and compete for mutable experiment claims. Database leasing and serialized top-level strategy guard the shared current state without becoming independent policy agents. The operator retains the ultimate mission/authorization boundary. For S3 and S4, operator-supervised modes are classified separately from autonomous base decisions.

## S1 — Operations

- State: A
- Function: perform the research transformation by selecting hypotheses, experimental approaches, evidence collection, analysis and findings in the mission environment.
- Disturbance / variety regulated: uncertain mechanisms, failed or conflicting experiments, variable baselines and unanticipated research obstacles.
- Decisive decision or feedback right: select a concrete hypothesis/experiment, interpret results and decide the next research action.
- Decision owner: autonomous Codex/Claude project research agent in managed mode, or the user-started agent in the installed template.
- Supporting / enforcement mechanisms: H/E/F validation, canonical artifact IDs, workspace, engine continuation, database transactions, guardrails, mission limits and local templates.
- Closure path: model-selected commands create/complete H/E/F and return evidence into the next research checkpoint/ACTIVE plan; the next model turn consumes durable state.
- Boundary reachability: default managed runtime calls the first-party research service with a project-scoped capability; template AGENTS instructions and kb scripts operate from the generated project.
- Why this is / is not agent-owned: the model decides substantive research hypotheses, procedure and interpretation; the runtime enforces transaction requirements but cannot select these research judgments with comparable discretion on its own.
- Evidence: [agent mission prompt and research tools](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L710-L735), [hypothesis and experiment creation](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/research_service.py#L31-L211), [finding publication after evidence](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/research_service.py#L319-L454), [template research loop](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/AGENTS.md#L62-L90).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: the objective and limits originate with the parent; H/E/F file creation alone is not an autonomous judgment.

## S2 — Coordination

- State: C
- Function: damp destructive concurrent experiment writes among separate research work cells.
- Disturbance / variety regulated: two experiment lanes attempting to claim or mutate the same E artifact, stale versions overwriting newer evidence, or competing top-level strategic decisions.
- Decisive decision or feedback right: grant or reject a per-experiment claim, isolate concurrent writes, and return lease conflicts to the agent lane for reallocation.
- Decision owner: deterministic first-party database lease/CAS mechanism makes the immediate claim decision; a first-party specific coordination feedback path is supplied, but no separate autonomous S2-level conflict-resolution policy/agent is required or shown by the standard distribution.
- Supporting / enforcement mechanisms: per-experiment work leases, per-project coordinator lease, per-kind atomic ID counters, append-only observations, compare-and-swap decisions and scoped agent lane identity.
- Closure path: rejected conflicting claims prevent the competing lane from writing; the caller receives a conflict and can select another E, wait or hand off. Successful separate experiment claims proceed concurrently.
- Boundary reachability: managed runtime documents SDK subagent lanes and exposes the authenticated experiment.claim and experiment completion path to model/tool calls in the shipped server.
- Why this is / is not agent-owned: lease adjudication is configured deterministic machinery, not an independently evidenced discretionary coordination agent; the provider may decide what to do after a conflict, but agent-owned S2 arbitration across lanes is not established as an operating requirement.
- Distinct S1 units: independently operating experiment/subagent lanes, each conducting a bounded experiment and producing own observations.
- Inter-S1 disturbance: duplicate claims and non-serializable edits to the same running experiment or stale findings.
- Attenuating coordination relation: exclusive E-scoped leases, versioned completion and separate leases for distinct E artifacts.
- Feedback into subsequent S1 behaviour: a failed claim/invalid version is returned by first-party research commands; only the lease owner may complete its experiment, enabling retry/reallocation without clobbering observations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the claim/lease is keyed to a demonstrated concrete concurrent evidence-writing conflict, not just to the order of tool calls or dispatch.
- Evidence: [architecture coordination matrix and subagent lanes](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/docs/cloud-runtime-architecture.md#L116-L145), [claim-experiment lease](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/research_service.py#L213-L268), [completion owner check](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/research_service.py#L319-L382), [lease conflict and CAS implementation](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/service.py#L620-L739).
- Basis: structural and explicit.
- Confidence: medium.
- Caveats: a single-agent template project need not instantiate parallel S1 units; C is credited from the supported managed multi-lane constructor, not generic provider subagent capability.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate a research project's active commitments, objectives, running/waiting state and practical allocation of current attention under a coherent mission.
- Disturbance / variety regulated: parallel experimental work diverging from the current priority, resource or provider failures, stalled decisions, unsatisfied access prerequisites, and operator reprioritization.
- Decisive decision or feedback right: choose the next substantive whole-project objective/step and whether research is RUNNING, WAITING, or COMPLETE; in parent mode, interrupt, reprioritize, pause or resume whole-project work.
- Decision owner: base mode — project research model returns structured current_objective/next_step/status; parent mode — authenticated human OWNER/EDITOR reviews current state and supplies binding runtime lifecycle or high-priority guidance.
- Supporting / enforcement mechanisms: coordinator lease, versioned checkpoint, database/continuation store, retry backoff, runtime capability, human inbox and CLI/REST/MCP transport.
- Closure path: agent checkpoint persists and becomes the next prompt/current research direction. Authenticated user intervention is sequenced into the durable inbox and delivered live or on wake; pause/stop interrupts and changes subsequent runtime execution.
- Boundary reachability: all paths occur in the normal managed project supervisor and public project-operations layer, not dogfood-only governance.
- Why this is / is not agent-owned: deterministic retries and hard lifecycle controls are support/parent authority; the model owns the discretionary research-priority checkpoint and cannot be replaced by the lease service without losing the same judgment.
- Whole-system current view: project mission, ACTIVE snapshot, current coordinator/inbox, resource state, findings and project review status.
- Current-control decision scope: present experiments, current objective, next step, blocker, active-turn interruption and commitment to completion/waiting.
- Evidence: [snapshot and model-owned structured checkpoint](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L383-L472), [provider-independent decision schema](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/runtime.py#L68-L109), [authenticated steering/lifecycle operations](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/operations.py#L228-L288), [inbox return](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L136-L164).
- Basis: explicit and structural.
- Confidence: high for base; medium-high for separately owned parent mode.
- Caveats: automatic failure retry alone would not qualify as autonomous S3.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | project research agent | normal evidence checkpoint and next objective | model decision becomes durable coordinator state and next prompt | [supervisor](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L419-L472) |
| Parent (`P`) | authenticated operator/editor | whole-project pause, resource/priority conflict or explicit steer | accepted guidance reaches active/future turn; pause/stop changes runtime state | [operations](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/operations.py#L228-L288) |

## S3* — Complementary audit

- State: —
- Function: complementary, sufficiently independent access to operative evidence that can challenge routine experiment/reporting claims.
- Disturbance / variety regulated: potential self-reporting or measurement overstatement in a research finding.
- Decisive decision or feedback right: no first-party independent auditor with a separately governed corrective feedback path is established in the shipped managed or template mode.
- Decision owner: not established; the producing research agent or ordinary human viewer can re-read/review evidence, but no independent audit ownership is wired.
- Supporting / enforcement mechanisms: event telemetry, evidence revisions, review endpoints, validation scripts and optional devil's-advocate CR note templates.
- Closure path: evidence review and challenge can change an agent's ordinary direction, but source does not require a materially independent complementary audit actor feeding the control loop.
- Why this is / is not agent-owned: the research-devil-advocate instruction asks the same model/session to criticise its current approach; this is reflective production judgment rather than an independent S3* path. The public review endpoint only exposes existing H/E/F state.
- Evidence: [review endpoint returns project status and records](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/operations.py#L290-L313), [devil's-advocate same-agent review skill](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/skills/research-devil-advocate/SKILL.md#L1-L110), [runtime feedback and telemetry](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L473-L495).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: separately composed human/agent auditors could use exported raw data, but are not automatically shipped and closed as a first-party independent mode here.

### Absence scope

- Surfaces inspected: managed supervisor and operations review path, research graph/event models, tests, template review forms, AGENTS.md and bundled research-devil-advocate workflow.
- Plausible first-party paths checked: separate model review role, template CR reviewer metadata, direct raw-data inspection, replay/telemetry and human project review; no materially independent reviewer scope or autonomous audit-to-current-control loop is implemented by these surfaces.
- Why no material first-party path remains: the supported review/critique features either reuse the producer's operating model or expose records to an external reader without a specified independent audit owner and returned corrective authority. The presence of a reviewer field and routine validation cannot supply this missing independence by themselves.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: investigate external research mechanisms and future options, challenge current strategic ceilings, and revise the project research capability/direction in dialogue with current work.
- Disturbance / variety regulated: changing state of the art, unforeseen external constraints, invalid assumptions and future inadequacy of the present approach.
- Decisive decision or feedback right: select an externally informed alternative mechanism/strategy and decide to continue, narrow, reset or pivot after comparing it with current evidence.
- Decision owner: autonomous research agent in the installed template mode exercises the research-direction decision via external SOTA search and CR/SR; authenticated parent operator can separately steer future direction after viewing H/E/F evidence.
- Supporting / enforcement mechanisms: installable exploratory-sota-research and research-devil-advocate skills, L/CR/SR notes, mission/ACTIVE links, managed guidance and stored findings.
- Closure path: external literature/challenge evidence generates prospective alternative H/SR; model commits revised direction into ACTIVE/next research objective and selects the next E. In parent mode, operator strategy decision enters durable guidance and is incorporated into the next model checkpoint, changing future work.
- Boundary reachability: shipped template's AGENTS.md routes explicit research and strategic review through bundled skills when installed by first-party install_skills workflow; managed first-party runtime also accepts outside inputs and persistent steering without borrowing repo-development dogfood.
- Why this is / is not agent-owned: the model generates and judges candidate future directions, not just stores an external event or summarizes literature. A human can initiate a distinct supervisory future-direction decision through the supported review/steer path.
- External distinction: landscape of mechanisms, external benchmark/reproducibility claims, risk and alternative approaches rather than only the current local task list.
- Future / prospective distinction: whether a research strategy will generalize or plateau under future conditions, which mechanism family could replace it.
- Adaptation option generated: CR/SR recommendation to pivot, reset, narrow or redesign experiments.
- Path back into current capability / S3: revise kb/ACTIVE.md/current_objective and subsequent H/E/F plan based on the external option and parent/agent decision.
- Evidence: [skill routing and strategic review flow](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/AGENTS.md#L69-L90), [external SOTA candidate research to persisted artifacts](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/skills/exploratory-sota-research/SKILL.md#L23-L131), [devil's-advocate pivot and ACTIVE update](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/skills/research-devil-advocate/SKILL.md#L45-L129), [strategic review direction template](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/templates/strategic-review.md#L1-L35), [human steer delivery](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L136-L164).
- Basis: explicit supported template mode, structural feedback.
- Confidence: medium; scope is adaptation of the mission's research strategy, not proof that Limina autonomously rewrites its own product runtime.
- Caveats: ordinary hypothesis selection alone is S1 rather than S4; this state is supported by the separate external/prospective research-and-pivot route. Some template skills require the documented installation step and are not silently assumed to be installed by every managed deployment.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | template-mode research agent | external landscape contradiction, plateau or future approach risk | external evidence → CR/SR option → ACTIVE pivot → next experiment | [SOTA skill](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/skills/exploratory-sota-research/SKILL.md#L23-L131), [review skill](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/skills/research-devil-advocate/SKILL.md#L45-L129) |
| Parent (`P`) | human project editor/owner | strategic review, changed constraints or human mandate to redirect research | review/steer decision → agent checkpoint/ACTIVE → changed research plan | [README](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/README.md#L327-L360), [operations](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/operations.py#L253-L288) |

## S5 — Policy and identity

- State: P
- Function: retain ultimate authority for the mission's identity, success criteria, risk boundaries and unresolved policy choices at parent recursion.
- Disturbance / variety regulated: a research outcome or new option conflicts with the human-defined mission, permitted resources, stopping conditions or evidence trust threshold.
- Decisive decision or feedback right: decide whether mission purpose, non-negotiable boundaries or blocked-stop authority should change; this is deliberately not delegated to autonomous research.
- Decision owner: parent human creating and governing the project, not the Codex/Claude model and not the database validator.
- Supporting / enforcement mechanisms: mission CHALLENGE.md, project success criteria, auth roles, escalation/steering inbox, user review, session recovery contract and runtime limits.
- Closure path: first-party template instructs the agent to stop and ask for mission/strategic decisions; parent decides and changes authoritative challenge/boundaries or supplies durable guidance; on recovery/next prompt the agent rereads the challenge/accepted input and operates under it. In managed mode, original project identity is stored by user at kickoff and editable only in CREATED state; general steer is not mistaken for a guaranteed post-start database mission rewrite.
- Boundary reachability: the template installation asks the operator for objective/boundaries/stopping conditions, runs in the generated project, and AGENTS.md instructs asking for mission decisions and reconstructing identity from CHALLENGE. This parent loop exists in documented first-party template mode without borrowing developer governance.
- Why this is / is not agent-owned: the model may surface a policy choice but cannot legitimately redefine the user's research mission; system configuration and stored text enforce/transport a decision rather than owning ultimate authority.
- Identity / ultimate-policy issue: change permitted research scope, success criteria, ethical/resource boundary, or stop condition when discovery invalidates the original agreement.
- Ultimate authority in each claimed mode: authenticated project owner / legitimate human sponsor in the template/managed project, no first-party autonomous S5 claimant.
- Return-to-operation path: explicit question/blocker → parent decision → updated authoritative mission/guardrail or accepted guidance → model re-grounding and subsequent plan.
- Evidence: [first-party install skill collects mission and blocked stop](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/skill/SKILL.md#L38-L110), [AGENTS mission authority, ask and recovery](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/AGENTS.md#L21-L63), [agent prompt asks for mission decisions](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/supervisor.py#L710-L725), [project identity stored at creation](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/project_service.py#L36-L85), [draft identity fields locked post-start](https://github.com/theam/limina/blob/56a4e2f3c9c613c7bc61f6a260ade379b21cd782/src/limina_cloud/collaboration.py#L221-L260).
- Basis: explicit parent-governed project/template contract and structural closure.
- Confidence: medium.
- Caveats: one-time mission setup or generic approval alone would not be enough; the credited parent mode includes escalation and returned identity-level decision. No automatic project-wide self-governance is claimed.

## Recursion

The assessed project is itself a viable research work unit at a higher user/team level. Nested experiment lanes are S1 work cells within that project when the parallel managed configuration is used; a portfolio of unrelated Limina projects is not inferred to possess shared S3/S5 solely because they run on one server. The operator is the parent authority for mission identity and current/future intervention. Codex/Claude provider SDK internals are environment/services, not automatically independent first-party organizational units.

## Variety and escalation

Uncertainty in mechanisms and evidence is handled through H→E→F, optional SOTA search, adversarial reconsideration and current-objective checkpoints. Resource/auth failures, provider transient errors and stale leases become explicit WAITING/FAILED/retry outcomes; these are deterministic support signals, not autonomous policy judgments. Human guidance is durable and can interrupt current execution. A limited or invalid experiment is not automatically a mission failure. Exceptional blocker alerts are signal paths, not a seventh VSM function or standalone S5 proof.

## Evidence gaps

- Source-pinned static and deterministic review, not a provider-backed live research mission. Actual distribution of model-selected subagent lanes, external searches and strategy pivots varies by mission and installed skills.
- The first-party S2 lease path is verified, but the standard distribution does not require a dedicated autonomous conflict mediator, hence C rather than A.
- Optional CR/SR reflective reviews do not establish a separately independent complementary auditor; any externally composed independent auditor would require separate boundary evidence.
- Managed mission fields are not freely rewritten after kickoff; S5=P is grounded in the explicitly supported operator-governed template escalation/update/re-grounding path, not assumed live server database mission mutation.
- Local deterministic upstream checks: seven focused tests passed (goal generation 2, kb-goal validation 4, contract checksum 1). Managed runtime test module ran 22 tests with two errors due missing local claude_agent_sdk dependency; not reported as full native suite PASS or upstream defect.
