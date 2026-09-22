---
harness_id: marveen
project_name: Marveen
repository: https://github.com/Szotasz/marveen
review_ref: b3f6574a76488b3367b26684f9065acca695a00f
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: C(P)
autonomy_s5: P
---

# Marveen

## Review boundary

- System in focus: one self-hosted Marveen installation at pinned revision `b3f6574a76488b3367b26684f9065acca695a00f`, including Marveen-owned fleet/team registry, per-agent state and skill surfaces, scheduling/background/heartbeat machinery, inter-agent messaging, Kanban/task state, channels/connectors, Mission Control/operator steering, approval paths, Dream Engine and skill-factory lifecycle.
- Purpose and identity: run a durable personal/team AI organization in which specialized agents can execute work, delegate, report, regulate current commitments, challenge each other's implementation claims, look outward for future opportunities and remain under the installation owner's identity and high-risk authority.
- Relevant environment: owner instructions and approvals, external services and web information, repositories and work products, channel/provider behavior, scheduled time, fleet agents, persistent memory/task state, runtime/process state and the underlying Claude Code agent engine.
- Standard-distribution boundary: Marveen-owned TypeScript runtime, dashboard, scripts, shipped docs, `skills/`, `seed-skills/`, `scheduled-tasks/` and `seed-scheduled-tasks/` that are installed or propagated by Marveen. Claude Code remains the external reasoning/agent engine; Claude Code internals and third-party MCP/channel plugins are not imported as Marveen-owned organizational decisions.
- Credited operating / distribution surfaces: `docs/agent-fleet.md`; `docs/scheduled-tasks.md`; `docs/heartbeat-autonomy.md`; `seed-scheduled-tasks/kanban-audit/SKILL.md`; `seed-skills/channel-plugin-duplicate-socket/SKILL.md`; `seed-skills/ai-fleet-project-execution/SKILL.md`; `scheduled-tasks/dream-engine/SKILL.md`; `scheduled-tasks/reggeli-napindito/SKILL.md`; `skills/skill-factory/SKILL.md`; `seed-skills/skill-management/SKILL.md`; `seed-skills/approval-request-handling/SKILL.md`; `seed-skills/self-rename/SKILL.md`; first-party dashboard/API/process/message/Kanban machinery reached by those installed procedures.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/update tests and maintainer-development activity are corroborative only unless reached by the installed runtime. Historical PRs are used as evidence of observed disturbances, not as autonomous runtime owners. Claude Code model internals, third-party channel/MCP implementations and external service behavior remain environmental.
- First-party operating / deployment modes considered: interactive channel work, multi-agent fleet execution, remote/local agents, scheduled tasks and heartbeats, progressive-autonomy levels 1-3, Kanban audit, low-risk autonomous PR review/merge, parent approval, Dream Engine/morning brief and owner-directed persona changes.
- Recursion level: one Marveen installation is the system-in-focus. Its configured specialist agents are distinct operational S1 units when they own separate delegated outcomes; the main/orchestrator agent is also an S1 actor when it performs operational work and may additionally perform metasystemic S2/S3/S3*/S4 functions at the installation recursion.
- Reviewed revision: `b3f6574a76488b3367b26684f9065acca695a00f`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Marveen is a self-hostable TypeScript harness around Claude Code. The first-party runtime keeps a fleet of separate agent sessions, routes inter-agent messages through shared first-party state/API paths, exposes start/stop/status controls, maintains Kanban commitments, persistent memory and scheduled work, and provides a dashboard for installation-wide steering. Scheduled tasks are delivered into an agent's tmux session as prompts and are processed as normal agent work; if the session is absent the runner can auto-start it and retry delivery.

The repository ships organizational procedures as skills and seeded scheduled tasks. README documentation states that fleet-level seed skills and scheduled tasks are propagated into installations, while the runtime's progressive-autonomy configuration changes whether the same control task acts autonomously, proposes for approval or only notifies. This makes the installed skills part of the assessed operating boundary rather than examples detached from runtime use.

The underlying Claude Code model/runtime supplies reasoning and tool execution, but this assessment credits only Marveen-owned wiring, procedures, state, authority relations and closed feedback paths. In particular, agent plurality is not itself used as S2 evidence; the S2 mapping rests on a concrete multi-agent channel-poller interference class and its first-party corrective coordination path.

## Operational model

The owner communicates through configured channels or the dashboard. The main agent can decompose projects, create Kanban commitments, delegate work to specialist agents and receive their results over inter-agent messaging. Specialist agents operate in separate sessions/workdirs, can continue for extended periods, update task state and produce artifacts. Scheduled tasks inject work into those same agent sessions without a contemporaneous owner turn.

Current control is layered. At autonomy level 3, scheduled agent procedures can archive stale completed commitments, contact owners of stalled work and escalate only after failed rounds. At lower configured levels, the same function becomes suggest/notify and the owner supplies the decisive current-control response. Higher-risk operations use an explicit approval path whose procedure states that only the paired owner may supply the approval decision.

Complementary control is supplied by cross-agent review. For multi-PR fleet work, the producing sub-agent must hand its PR to the orchestrator; the orchestrator independently inspects the diff and runs its own build/test rather than accepting the producer's claim. It may autonomously merge low-risk work after a successful review or return concrete defects for correction.

Prospective adaptation is split between a constructor path and a parent-governed closed mode. Dream Engine autonomously scans for external agent/tooling opportunities and feeds them into the morning brief; skill-factory/skill-management provide first-party capability-mutation surfaces. The frozen revision does not establish an autonomous end-to-end decision from an external opportunity through adoption into changed capability, while an owner can decide the adaptation and return that decision through the normal agent/skill mutation path.

## S1 — Operations

- State: A
- Function: execute delegated or scheduled objectives through persistent specialist/main-agent sessions and close results through tools, artifacts, Kanban state, inter-agent messages and user channels.
- Disturbance / variety regulated: heterogeneous owner goals, repository/product work, external services, tool failures, changing task state, remote-agent availability and scheduled objectives.
- Decisive decision or feedback right: choose the substantive action sequence for an admitted objective, including tool use, implementation steps, artifact production and when/how to report completion within configured constraints.
- Decision owner: the active Claude model actor in the Marveen-managed agent session.
- Supporting / enforcement mechanisms: per-agent tmux sessions/workdirs, CLAUDE/persona state, inter-agent message queue/API, Kanban state, scheduled-task runner/retry queue, channels, MCP tools and persistent memory.
- Closure path: owner/orchestrator/timer supplies objective → Marveen delivers it to an agent session → agent chooses and executes work → result/task status/artifact/message is persisted or delivered → orchestrator/owner/subsequent work consumes the result.
- Boundary reachability: first-party fleet and scheduled-task machinery starts or reaches the configured agent session and returns work through Marveen-owned messaging/task/channel surfaces; no autonomy from an external peer harness is borrowed.
- Why this is / is not agent-owned: Marveen's deterministic runtime schedules and transports work, but the material operational choices are made by the model actor running as the configured agent.
- Evidence: `README.md`; `docs/agent-fleet.md`; `docs/scheduled-tasks.md`; `seed-skills/ai-fleet-project-execution/SKILL.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Claude Code is the external reasoning engine; the positive claim is limited to agent autonomy made reachable and operationally closed by Marveen-owned harness surfaces.

## S2 — Coordination

- State: A
- Function: attenuate concrete interference among distinct Marveen agent units when more than one agent loads a single-owner channel polling/socket resource.
- Disturbance / variety regulated: competing fleet agents opening duplicate Slack Socket Mode or Telegram long-poll connections against the same workspace/bot token, causing split/lost inbound events or Telegram `409` lockfight.
- Decisive decision or feedback right: diagnose which agent sessions have unintentionally loaded the shared channel plugin, choose the designated channel-owning session, disable the plugin in competing agent projects, terminate/restart excess processes and verify a single healthy poller remains.
- Decision owner: the autonomous Marveen agent executing the shipped `channel-plugin-duplicate-socket` skill.
- Supporting / enforcement mechanisms: process/parent-chain inspection, per-project `.claude/settings.json` overrides, process restart/kill, Marveen fleet separation and verification checks.
- Closure path: sibling agent sessions contend for one channel resource → agent observes duplicate channel processes / delivery symptoms → agent identifies unintended owners and applies per-agent plugin scoping → excess pollers are removed → subsequent inbound delivery returns to a single stable owner and is verified.
- Boundary reachability: `seed-skills/channel-plugin-duplicate-socket/SKILL.md` is a Marveen seed skill; Marveen documents seed skills as fleet-level skills propagated into installations, where ordinary agent sessions can execute the diagnostic/mutation procedure.
- Distinct S1 units: separate Marveen agent/Claude Code sessions in the same fleet, each capable of loading the same globally enabled channel plugin.
- Inter-S1 disturbance: Slack duplicate sockets split inbound events across agents; Telegram duplicate `getUpdates` pollers compete for the same bot token and kick one another out with `409 Conflict`. Merged PR #210 documents and live-verifies the Telegram instance of this fleet-level interference.
- Attenuating coordination relation: agent-owned inspection and per-project plugin scoping designate one channel-owning S1 and suppress competing plugin instances in sibling S1 projects.
- Feedback into subsequent S1 behaviour: after settings/process correction, non-designated agents stop polling the shared channel while the designated agent continues, restoring reliable inbound delivery; the skill explicitly verifies the remaining process ownership.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mapping is tied to an evidenced interference relation among sibling S1 units competing for one shared external coordination resource; generic inter-agent messaging or delegation is not counted.
- Why this is / is not agent-owned: deterministic settings and process controls enforce the result, but the shipped procedure requires the model actor to inspect runtime evidence, identify the competing sessions and choose/apply the corrective coordination relation. That material coordination judgment is agent-owned.
- Evidence: `seed-skills/channel-plugin-duplicate-socket/SKILL.md`; `docs/agent-fleet.md`; merged upstream PR #210 (`fix(telegram): prevent sub-agents from stealing the Telegram poller + heartbeat answers direct messages`); README seed-skill distribution description.
- Basis: explicit + structural + observed disturbance.
- Confidence: high.
- Caveats: static plugin configuration alone would not justify `A`; the positive ownership claim rests on the installed agent-executed diagnosis/correction loop around the concrete fleet collision.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the installation's current commitments and exceptions by maintaining a whole-board view, detecting stalled/obsolete work, intervening with responsible agents and escalating when local correction fails.
- Disturbance / variety regulated: stale completed cards, stalled `in_progress` commitments, unowned/delegation gaps and current task obligations that stop moving while the fleet continues operating.
- Decisive decision or feedback right: in autonomous mode, choose current corrective intervention (archive, contact responsible agent, continue local recovery, escalate after failed rounds); in parent mode, present the same current-control action for owner approval or notification according to configured autonomy level.
- Decision owner: level-3 mode — scheduled main-agent actor; level-1/2 mode — installation owner as legitimate parent.
- Supporting / enforcement mechanisms: installation-wide Kanban board, scheduled Kanban audit, persisted audit state, inter-agent messaging, progressive-autonomy configuration and owner approval/notification path.
- Closure path: current board state → scheduled agent audit detects exception → autonomous intervention or returned parent decision → Kanban/message/escalation state changes → subsequent fleet work proceeds under the corrected current commitment state.
- Boundary reachability: the first-party schedule runner delivers `kanban-audit` into the configured main agent as normal agent work; `heartbeat-autonomy` defines levels for the same installed control categories, and the Kanban audit implements the corresponding level-specific actions.
- Why this is / is not agent-owned: the level-3 current-regulation judgment is made by the agent after inspecting live board state; lower levels deliberately transfer the decisive right to the parent instead of merely changing deterministic thresholds.
- Evidence: `docs/en/kanban.md`; `docs/heartbeat-autonomy.md`; `docs/scheduled-tasks.md`; `seed-scheduled-tasks/kanban-audit/SKILL.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary task assignment/scheduling is not used as S3 evidence; the positive mapping is the installation-wide exception/control loop over current commitments.
- Whole-system current view: Kanban audit reads the fleet board across commitments/assignees and carries persisted prior-audit state needed to distinguish stalled current work from ordinary progress.
- Current-control decision scope: archive obsolete completed obligations, challenge owners of stalled work, detect delegation gaps and escalate unresolved commitments to the owner.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | scheduled main-agent actor | level-3 Kanban audit reaches a live exception | agent archives/pings/rechecks and escalates after failed rounds; later board/agent behaviour reflects the intervention | `seed-scheduled-tasks/kanban-audit/SKILL.md`; `docs/heartbeat-autonomy.md` |
| Parent (`P`) | installation owner | same current-control category configured to suggest/notify / approval-required mode | proposed intervention is returned to owner; owner decision is applied or withheld and subsequent current operation follows it | `docs/heartbeat-autonomy.md`; `seed-skills/approval-request-handling/SKILL.md` |

## S3* — Complementary audit

- State: A
- Function: challenge implementation-completion claims from producing sub-agents through an independent orchestrator review path with direct access to the proposed artifact and its build/test reality.
- Disturbance / variety regulated: latent defects or incomplete validation that can survive a producer's own task-specific tests and status report, including changes that fail the installation-wide TypeScript build after the producer reported tests passing.
- Decisive decision or feedback right: accept a reviewed change as sound enough to merge, or reject it with concrete defects and require another producer iteration.
- Decision owner: the orchestrator model actor, distinct from the sub-agent that produced the reviewed PR in the documented multi-agent workflow.
- Supporting / enforcement mechanisms: producer/orchestrator role separation, `gh pr diff`, independent local build/test, explicit no-self-merge rule for multi-PR delegation, inter-agent defect feedback and low-risk autonomous merge path.
- Closure path: producer sub-agent reports PR ready → orchestrator independently reads diff and runs its own build/test → orchestrator judges pass/fail → on failure returns numbered defects and producer revises; on acceptable low-risk work orchestrator may merge and dispatch subsequent work.
- Boundary reachability: `seed-skills/ai-fleet-project-execution/SKILL.md` is a shipped fleet procedure used by the orchestrator for team projects; its review rule explicitly separates producer and reviewer roles and requires direct artifact/build access.
- Why this is / is not agent-owned: the complementary finding is not a deterministic CI status and is not delegated back to the producer. A different model actor inspects evidence and owns the review judgment; deterministic build/test only supplies complementary observations.
- Evidence: `seed-skills/ai-fleet-project-execution/SKILL.md`.
- Basis: explicit + structural + documented incident.
- Confidence: high.
- Caveats: generic audit logs, routine tracing and same-agent self-checks are not counted. The positive claim is specifically the cross-agent producer/orchestrator review relation.
- Claim being audited: the producing sub-agent's claim that its delegated implementation/PR is complete and safe enough to integrate.
- Ordinary reporting path: producer sub-agent updates Kanban/inter-agent status and reports its PR/tests to the orchestrator.
- Complementary access path: orchestrator directly inspects `gh pr diff` and runs its own build/test, including full `npx tsc` for orchestrator-repository changes rather than relying on producer-local targeted tests.
- Independence boundary: producer and reviewer are separate Marveen agent sessions/roles; the reviewer consumes the artifact and raw build/test result rather than merely relaying the producer's report.
- Who acts on findings: the orchestrator returns corrective findings to the producer or, for an acceptable low-risk change, merges and advances subsequent work.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: sense external/future-relevant changes, develop adaptation options for the installation and provide a path by which those options can become present capability changes.
- Disturbance / variety regulated: changing external agent/tooling ecosystem, emerging useful repositories/skills, tomorrow's likely priorities and gaps between current skill capability and potentially useful future capability.
- Decisive decision or feedback right: base constructor mode exposes external opportunity selection plus capability-mutation primitives but does not close autonomous adoption; parent mode lets the owner decide whether an identified opportunity should become a present skill/workflow/capability.
- Decision owner: base `C` — no single autonomous owner closes adoption at the pinned revision; parent `P` — installation owner owns the adaptation decision.
- Supporting / enforcement mechanisms: Dream Engine external-opportunity WebSearch and filtering, persisted `DREAM.md`, morning brief, skill-factory and skill-management create/patch paths, normal owner channel and agent execution.
- Closure path: external ecosystem/future context → Dream Engine forms an adaptation option → morning brief returns it to the installation's current control/owner → owner selects/rejects adaptation → agent uses first-party skill/workflow mutation machinery → subsequent operation can use the changed capability.
- Boundary reachability: Dream Engine and morning brief are shipped scheduled tasks executed by the main agent; skill-factory is a first-party installed skill that writes reusable skills and updates the skill index. The autonomous path stops before adoption, while the owner-mediated path can close through ordinary Marveen interaction.
- Why this is / is not agent-owned: the model actor autonomously performs external sensing and option generation, and Marveen supplies first-party capability mutation primitives, but the frozen evidence does not establish a first-party autonomous authority that decides to adopt the external option and closes that decision into changed capability. That supports `C`, not `A`, for the base mode; the owner-mediated closure supports `(P)`.
- Evidence: `scheduled-tasks/dream-engine/SKILL.md`; `docs/dream-engine.md`; `scheduled-tasks/reggeli-napindito/SKILL.md`; `skills/skill-factory/SKILL.md`; `seed-skills/skill-management/SKILL.md`.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: internal retrospective/self-learning alone is not used as S4 evidence. The S4 mapping specifically depends on Dream Engine's fresh external-opportunity sensing plus the return path toward present capability.
- External distinction: Dream Engine periodically searches for fresh Claude Code/agentic-AI/productivity repositories and filters them by recency, popularity and relevance rather than only mining internal memory.
- Future / prospective distinction: the external-opportunity and tomorrow-priority buckets are generated for prospective usefulness and are delivered in the next morning brief, where stale completed recommendations are explicitly rechecked.
- Adaptation option generated: a bounded external repository/tool/skill recommendation with relevance, alongside skill suggestions and fleet-health options.
- Path back into current capability / S3: `DREAM.md` → morning brief/current owner view → owner adoption decision → agent skill/workflow mutation through skill-factory/skill-management → later tasks can trigger the new/changed skill.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | constructor path; autonomous adoption owner not established | scheduled Dream Engine external scan / identified prospective gap | first-party agent generates option and first-party skill mutation primitives exist, but the pinned distribution does not wire an autonomous adoption decision through to capability mutation | `scheduled-tasks/dream-engine/SKILL.md`; `skills/skill-factory/SKILL.md` |
| Parent (`P`) | installation owner | Dream/morning brief presents a prospective adaptation option | owner selects/rejects; accepted option returns as an instruction and the agent can create/patch reusable skill capability used by later operation | `scheduled-tasks/reggeli-napindito/SKILL.md`; `skills/skill-factory/SKILL.md`; `seed-skills/skill-management/SKILL.md` |

## S5 — Policy and identity

- State: P
- Function: resolve durable installation identity/persona changes under legitimate owner authority and return the resulting identity into subsequent agent operation without corrupting internal service identity.
- Disturbance / variety regulated: requests to change how the main agent identifies/presents itself while preserving stable internal installation/service identifiers and excluding unauthorized identity changes.
- Decisive decision or feedback right: choose the new displayed/persona identity and authorize the identity-level change.
- Decision owner: the paired installation owner; the shipped self-rename procedure explicitly refuses non-owner initiation.
- Supporting / enforcement mechanisms: owner-gated `self-rename` skill, `CLAUDE.md`/`SOUL.md` persona mutation, `BRAND_NAME`, protected internal identifiers and restart/reload procedure.
- Closure path: owner requests identity change → agent verifies owner context and applies persona/brand mutation → display/runtime reload/restart path takes effect → subsequent sessions load and operate under the new persona identity while internal service identity remains stable.
- Boundary reachability: `seed-skills/self-rename/SKILL.md` is a first-party seed skill installed into the operating skill library and directly mutates the installation's persona/brand files reached by later sessions.
- Why this is / is not agent-owned: the agent executes and safeguards the change but does not own the ultimate identity choice; the procedure requires the owner to supply that decision and refuses strangers/non-owners.
- Evidence: `seed-skills/self-rename/SKILL.md`; README branding/persona description.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary prompts/configuration are not counted as S5. The positive claim is limited to the durable owner-authorized identity mutation and return-to-operation loop.
- Identity / ultimate-policy issue: what durable displayed/persona identity the installation's main agent operates under.
- Ultimate authority in each claimed mode: installation owner only.
- Return-to-operation path: owner decision → persona/brand files changed → relevant service/session reload → later agent operation consumes the updated persona identity.

## Recursion

The assessment fixes one Marveen installation as the recursion. Specialist agents are S1 units when they produce distinct delegated outcomes. The main/orchestrator agent can itself be operational S1 for direct work while also carrying metasystemic functions over the fleet: collision attenuation (S2), current-commitment regulation (S3), independent producer review (S3*) and prospective option generation (S4). Those roles are mapped by function rather than by the name `orchestrator`.

Federation or another Marveen installation is not treated as a parent recursion for this assessment. The local owner is the legitimate parent in the supported S3/S4/S5 parent modes.

## Variety and escalation

Operational variety is absorbed first by specialized agents, durable task state, skills/tools and asynchronous scheduling. Inter-agent messaging and Kanban make obligations visible across units. Concrete channel-resource interference is attenuated through a first-party diagnostic/corrective coordination procedure. Current exceptions are handled locally by the Kanban audit and responsible agent; unresolved stalls can escalate after repeated failed rounds. High-risk actions and lower-autonomy configurations return decisions to the owner through explicit approval/control paths.

## Evidence gaps

- S2 autonomy is established for the documented shared-channel collision class; this assessment does not generalize that one relation into a claim that every possible fleet interference has an autonomous S2 controller.
- S3* is established for the documented multi-agent implementation/PR workflow. Generic logs and routine tracing are not treated as complementary audit.
- S4 autonomous adoption is not established. Dream Engine's external sensing and first-party skill mutation surfaces support a constructor path, while the evidenced closed adoption mode remains owner-governed; a future revision with an autonomous opportunity-selection/adoption/capability-return loop could change this state.
- Claude Code internals remain outside the ownership boundary throughout; model reasoning is credited only where Marveen's first-party operating path invokes it and closes the resulting organizational function.
