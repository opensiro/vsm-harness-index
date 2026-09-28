---
harness_id: octos
project_name: Octos
repository: https://github.com/octos-org/octos
review_ref: 9f6311afd4e00324cdb89d957461cf861f4f2630
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# Octos

## Review boundary

- System in focus: one first-party Octos harness-kernel organization at pinned revision `9f6311afd4e00324cdb89d957461cf861f4f2630`, including the model/tool agent loop, durable Session/turn state, peer/sub-agent supervision, pipeline/swarm execution, backend-owned `review/start`, bundled `skill-evolve`, bootstrap identity files and OUP control surfaces reachable from the shipped gateway/serve runtime.
- Purpose and identity: provide an embeddable agent runtime that owns execution, context, memory, tools, skills, workflows, multi-agent supervision and durable runtime state while allowing applications or other controllers to drive the same runtime through OUP.
- Relevant environment: user objectives, repository/workspace state, model-provider responses, tool/MCP/plugin results, peer and child-agent outputs, external controller/operator interventions and configured channel or service events.
- Standard-distribution boundary: first-party Rust kernel crates and gateway/serve runtime plus bundled first-party skills and OUP methods that operate on kernel-owned state. External model endpoints, MCP servers, repository-specific commands, external application controllers and the separate `octoscode` / `octoscode-web` client repositories remain dependencies or adjacent systems and do not donate VSM ownership.
- Credited operating / distribution surfaces: `octos-agent`; session/turn runtime; first-party tool registry; gateway/serve peer tools and peer state; `octos-pipeline` / `octos-swarm`; backend-owned review workflow; bundled `skill-evolve`; bootstrap identity files; OUP supervision/control over runtime-owned sessions, agents and tasks.
- Adjacent first-party surfaces excluded from ownership: `octoscode` and `octoscode-web` application repositories; repository-development CI/release workflows; e2e soak fixtures and tests; contributor governance; documentation-only examples. These may corroborate reachability but do not supply an owner by themselves.
- First-party operating / deployment modes considered: ordinary autonomous turns; sub-agent execution; agent-created sovereign peers with optional worktree fencing; host-prepared peers; pipeline/swarm workflows; typed `review/start`; bundled skill evolution; gateway/serve bootstrap hot reload; human or higher-level controller intervention through OUP.
- Recursion level: one Octos runtime organization around a profile/workspace/session objective. Autonomous child agents and sovereign peer sessions are S1 units inside that boundary when they perform operational work; external model providers, tools and client applications are environment/dependencies.
- Reviewed revision: `9f6311afd4e00324cdb89d957461cf861f4f2630`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Octos ships a reusable Rust harness kernel rather than only a client shell. The first-party runtime owns agent execution and runtime state: a model-facing agent loop receives a task, sends model-visible tools, executes selected calls through the tool layer, returns observations into the conversation and repeats until completion or a runtime limit. Session state, context compaction, persistence, permissions and recovery remain kernel-owned even when inference and some environmental actions are external.

Multi-agent work is exposed in several shapes. A sub-agent is a child of the current turn. A peer is a sovereign Session with its own brief, workspace and lifecycle. The originator agent receives explicit `peer_handoff`, `peer_send_input`, `peer_gather`, `peer_list` and `peer_close` tools. `peer_handoff` can request a dedicated Git worktree on `peer/<slug>`, fencing that autonomous peer's repository activity from sibling/current workspace mutation. This positive isolation path is distinct from generic sequencing or messaging and supplies the S2 witness.

The same peer surface gives the master agent a whole-fleet current-control path: it can list every peer, gather results, inject a next turn and retire peers it created. Separately, OUP exposes runtime-owned agent/task/session state plus steer, interrupt, cancel and restart controls to a legitimate parent controller. These are alternative first-party ownership modes for the same current-control function, so S3 is `A(P)`: the autonomous master-agent mode is established, and a distinct supported parent-governed OUP mode is also closed.

For complementary audit, Octos ships a backend-owned `review/start` workflow rather than relying only on ordinary implementer reporting or a deterministic validator. The server resolves and launches specialist agents, keeps their child contexts fork-scoped/sanitized, projects their lifecycle/artifacts independently, and runs a model-generated master review join whose final answer is persisted to the Session. That review evidence is produced through a separate specialist path and returned to the controlling Session, establishing autonomous S3*.

Octos also ships a concrete adaptive S4 loop through the bundled `skill-evolve` app-skill. An `after_tool_call` hook detects failed plugin-tool interactions, maps the failure back to its owning skill, asks an LLM for an instruction intended to prevent recurrence and queues that proposal. The same first-party skill exposes a model-visible `skill_evolve` tool; the agent can inspect the queue and decide to `apply`, which writes the learned instruction into the target `SKILL.md`. Skill instructions are part of the model-facing skill guidance on later operation. Because the decisive apply/discard choice is available to the autonomous agent rather than being hard-coded by the hook, the positive ownership state is `A`, not merely constructor-owned adaptation.

Finally, Octos supplies an explicit parent-governed identity surface. `.octos/IDENTITY.md` is documented as the custom identity definition and `.octos/SOUL.md` as personality/values; bootstrap files are loaded into the system prompt and hot-reloaded after edits. The legitimate workspace/operator authority therefore can make an identity/ultimate-policy decision and have the running agent subsequently governed by it without borrowing ownership from an external client implementation. No first-party evidence establishes the agent itself as the legitimate ultimate authority over these identity files, so S5 is `P`, not `A(P)`.

Primary evidence:

- [`README.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/README.md) — shipped kernel boundary, OUP lifecycle, task/agent supervision, peers, workflows, goals/loops/monitors and host/controller separation.
- [`docs/ARCHITECTURE.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/docs/ARCHITECTURE.md) — first-party runtime composition, agent loop, bundled skills and model-facing skill loading.
- [`book/src/multi-agent.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/book/src/multi-agent.md) — sovereign peer Sessions, originator agent controls, worktree fencing and peer lifecycle.
- [`docs/OCTOS_UI_PROTOCOL_CHANGE_REQUEST_UPCR_2026_019_AGENT_SUPERVISION.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/docs/OCTOS_UI_PROTOCOL_CHANGE_REQUEST_UPCR_2026_019_AGENT_SUPERVISION.md) — accepted/implemented backend-owned supervised-agent and `review/start` contract.
- [`crates/app-skills/skill-evolve/src/main.rs`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/crates/app-skills/skill-evolve/src/main.rs) and [`manifest.json`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/crates/app-skills/skill-evolve/manifest.json) — failure-derived adaptation proposal generation and model-visible list/apply/discard tool.
- [`book/src/memory-skills.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/book/src/memory-skills.md) — runtime identity/value bootstrap files and hot-reload return into the system prompt.

## Operational model

The ordinary S1 is a model-driven Octos Agent operating inside a Session: it owns substantive tool/response choices while the kernel owns execution, policy enforcement, persistence and observation delivery. Child agents and sovereign peers become additional S1 units when they perform delegated or independent operational work. A master agent may create and supervise those units through model-visible first-party tools; alternatively, a human/application/higher-recursion controller may exercise parent current control through OUP without becoming part of the kernel's autonomous S1.

Constructor/runtime mechanisms such as budgets, retry caps, provider failover, workflow topology, permission gates, queue ordering and durable replay are treated as support/enforcement unless a function-specific decision/feedback right is independently established. Likewise, external clients and model providers do not receive ownership credit merely because Octos exposes protocol surfaces to them.

## S1 — Operations

- State: A
- Function: transform user objectives into task/repository/application outcomes through repeated model decisions, first-party tool execution and returned observations; child agents and peers can independently execute bounded operational work.
- Disturbance / variety regulated: open-ended user goals, changing workspace state, tool/MCP/plugin results and failures, model-provider responses, delegated subtasks and multi-turn task state.
- Decisive decision or feedback right: choose substantive response/tool actions and choose subsequent actions after observing tool results within the configured policy boundary.
- Decision owner: the configured model-driven Octos Agent or autonomous child/peer Agent for its local operational task.
- Supporting / enforcement mechanisms: `octos-agent` loop, first-party tool registry, session/context state, sandbox and permission policy, model adapters, persistence, budgets, cancellation and recovery.
- Closure path: objective enters a Session → model receives context/tools → model chooses response/tool calls → first-party runtime executes allowed calls → results are returned into model-visible history → model chooses the next action or completion → durable Session/task state receives the outcome.
- Boundary reachability: the model/tool loop is the standard execution kernel used by the shipped CLI/gateway/serve runtime and by first-party child/peer execution paths; it does not depend on an external orchestrator to select each substantive next action.
- Why this is / is not agent-owned: removing the model decision maker removes the open-ended substantive action selection; deterministic runtime policy can constrain or terminate work but does not reproduce those decisions.
- Evidence: [`README.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/README.md); [`docs/ARCHITECTURE.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/docs/ARCHITECTURE.md); [`book/src/multi-agent.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/book/src/multi-agent.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: external model endpoints supply inference and external tools may own environmental side effects; they do not own Octos' first-party operational feedback organization.

## S2 — Coordination

- State: A
- Function: prevent concurrent autonomous peer repository work from destructively interfering through one shared checkout by assigning a peer to its own fenced Git worktree.
- Disturbance / variety regulated: two or more sovereign peer S1s may perform repository mutations in parallel; if they share one checkout, one peer's writes/index/branch state can contaminate another peer's observations and work.
- Decisive decision or feedback right: when handing off autonomous work, decide whether the peer receives a dedicated worktree/branch so later repository actions are isolated from sibling/current workspace mutation.
- Decision owner: the originator Octos Agent invoking the model-visible `peer_handoff` tool with the `worktree` option.
- Supporting / enforcement mechanisms: per-peer durable directories, originator identity, optional Git worktree on `peer/<slug>`, separate peer Session/workspace and lifecycle.
- Closure path: master Agent identifies parallel peer work → invokes `peer_handoff` with worktree fencing → first-party runtime stages a sovereign peer in the dedicated checkout → that peer's later repository observations/actions occur in its fenced workspace → sibling/current checkout mutations do not become its live working state.
- Boundary reachability: `peer_handoff` is a first-party agent tool in gateway/serve mode, and the documented `worktree` argument is part of the supported peer lifecycle at the pinned revision.
- Distinct S1 units: sovereign peer Sessions each run their own `session/open` + `turn/start` lifecycle and perform independent operational tasks with their own brief/workspace/state.
- Inter-S1 disturbance: concurrent repository mutation through a common checkout would couple peer filesystem/Git state and can invalidate or overwrite another peer's work or observations.
- Attenuating coordination relation: originator-selected per-peer Git worktree/branch fencing separates the mutation domains of the autonomous peer S1s.
- Feedback into subsequent S1 behaviour: after staging, each fenced peer's subsequent file/shell/repository observations and actions resolve against its dedicated worktree, changing what that S1 sees and can interfere with.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanism is not `peer_gather`, message delivery, fleet size, scheduling or delegation topology; it attenuates the concrete cross-S1 disturbance of concurrent repository-state interference.
- Why this is / is not agent-owned: the runtime implements worktree isolation, but the originator model has the supported decision right to request the fenced mode for the peer it creates; the same substantive coordination choice is therefore not fixed solely by a constructor policy.
- Evidence: [`book/src/multi-agent.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/book/src/multi-agent.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: plain peer creation without `worktree` and generic swarm parallelism are not independently credited as S2. The positive witness is specifically the model-selected fenced-worktree mode for plural repository-operating peers.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain current control over the active multi-agent/task organization by inspecting the whole current peer/task set and changing live commitments or interventions through steer/close/cancel/restart controls.
- Disturbance / variety regulated: peers/children can be running, done, failed, stalled or producing divergent results; ongoing commitments may require new instructions, retirement, cancellation or targeted restart as current evidence changes.
- Decisive decision or feedback right: decide which current workers continue, receive new instructions, are retired/cancelled or are restarted, based on whole-set current status/output.
- Decision owner: base `A` mode — the master Octos Agent through model-visible peer supervision tools; parent `P` mode — the legitimate human/application/higher-recursion controller through first-party OUP supervision and intervention methods.
- Supporting / enforcement mechanisms: `peer_list`, `peer_gather`, `peer_send_input`, `peer_close`; backend agent/task lifecycle projections; `agent/list`, `agent/status/read`, `agent/output/read`, task inspection, `turn/steer`, `turn/interrupt`, `task/cancel` and `task/restart_from_node` where supported.
- Closure path: current workers/tasks execute → first-party runtime retains statuses/outputs/artifacts → decisive owner inspects the current set → owner selects an intervention or continuation decision → runtime applies the steer/close/cancel/restart action → subsequent current execution reflects that returned decision.
- Boundary reachability: autonomous peer supervision tools are available to the originator Agent in shipped gateway/serve mode; OUP exposes the corresponding runtime-owned state/control surfaces to a supported parent controller without requiring ownership from `octoscode` itself.
- Whole-system current view: in the autonomous peer mode, `peer_list` enumerates every staged peer and `peer_gather` reads named or all peer results; in the parent mode, OUP projects current agent/task/session state and retained outputs/artifacts from the same runtime.
- Current-control decision scope: alter current worker commitments and priorities by injecting follow-up work, retiring a peer, interrupting a turn, cancelling a task or restarting a terminal task/node rather than merely enforcing a fixed concurrency or token limit.
- Why this is / is not agent-owned: in the base mode, the master model chooses when and how to use the peer controls after reading current state. The parent mode remains distinct because OUP also permits an authorized external parent to inspect and intervene directly; deterministic runtime mechanics only execute the chosen action.
- Evidence: [`book/src/multi-agent.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/book/src/multi-agent.md); [`README.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/README.md); [`docs/OCTOS_UI_PROTOCOL_CHANGE_REQUEST_UPCR_2026_019_AGENT_SUPERVISION.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/docs/OCTOS_UI_PROTOCOL_CHANGE_REQUEST_UPCR_2026_019_AGENT_SUPERVISION.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: swarm retry caps, max concurrency, deterministic pipeline order and permission gates are not separately credited as S3 ownership.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Master Octos Agent | Current peer status/output indicates another steer, retirement or synthesis decision is needed | Model calls first-party peer supervision tool; runtime changes peer commitment/state and later operation reflects it | `book/src/multi-agent.md` |
| Parent (`P`) | Authorized human/application/higher-recursion controller | Current OUP agent/task/session state indicates intervention/recovery is needed | Parent issues supported OUP steer/interrupt/cancel/restart action; kernel applies it to runtime-owned state | `README.md`; UPCR-2026-019 |

## S3* — Complementary audit

- State: A
- Function: independently review current repository/work-product claims through backend-owned specialist agents and return a joined review into the controlling Session.
- Disturbance / variety regulated: an ordinary implementation agent may omit defects, policy violations or risky changes from its own report; relying only on the same execution/reporting path would leave those claims unchecked.
- Decisive decision or feedback right: specialist review agents autonomously inspect the selected review target and produce findings; the master review join autonomously synthesizes those findings into the Session's final review result.
- Decision owner: first-party model-driven review specialists plus the model-driven master review join.
- Supporting / enforcement mechanisms: typed `review/start`, server-resolved specialist list, separate child runtimes, fork-scoped/sanitized child context, independent lifecycle/artifact projection and final joined review persistence.
- Closure path: review target is selected → server launches backend-owned specialists separate from ordinary implementation reporting → specialists inspect target and return findings/artifacts → master review join synthesizes them → final review is persisted into the Session → subsequent master/parent control can act on the findings.
- Boundary reachability: `review/start` is an accepted and implemented first-party OUP/runtime feature at the pinned revision, and the same backend can schedule supervised specialists from an ordinary review request.
- Claim being audited: correctness/safety/quality of a current repository change or other supported review target, beyond the implementer's own completion report.
- Ordinary reporting path: normal Agent/child output, tool events, task summaries and artifacts produced while doing the work.
- Complementary access path: separately launched review specialists inspect the review target in their own supervised child contexts and return review-specific findings/artifacts through the backend review workflow.
- Independence boundary: review children are separate runtimes with fork-scoped/sanitized context and server-resolved policies rather than merely re-labeling the implementer's self-report; the final join consumes their separate outputs.
- Who acts on findings: the master review join returns the synthesized result to the controlling Session, after which the autonomous master or legitimate parent can change subsequent work using the established current-control surfaces.
- Why this is / is not agent-owned: deterministic task supervision and artifact retention support the audit, but the substantive review judgments and final synthesis are model-driven specialist/master decisions.
- Evidence: [`docs/OCTOS_UI_PROTOCOL_CHANGE_REQUEST_UPCR_2026_019_AGENT_SUPERVISION.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/docs/OCTOS_UI_PROTOCOL_CHANGE_REQUEST_UPCR_2026_019_AGENT_SUPERVISION.md); [`README.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: the ordinary aggregate validator in swarm/pipeline execution is not independently credited as S3*; the positive witness is the separate specialist review path.

## S4 — Outside-and-then intelligence

- State: A
- Function: adapt reusable skill instructions from observed plugin-tool failures so future agent/tool interactions can avoid a recurring failure mode.
- Disturbance / variety regulated: failures and interface mismatches encountered while operating first-party plugin tools can reveal that current skill guidance is insufficient for future successful use.
- Decisive decision or feedback right: choose whether a failure-derived proposed instruction should be applied to the target skill's durable `SKILL.md` guidance or discarded.
- Decision owner: the autonomous Octos Agent invoking the model-visible `skill_evolve` tool; an LLM-backed hook generates proposals, while the agent owns the apply/discard decision in the credited mode.
- Supporting / enforcement mechanisms: bundled `after_tool_call` hook, reverse mapping from failed plugin tool to skill, LLM suggestion generation, per-skill `evolutions.json`, `skill_evolve` list/apply/discard/consolidate actions and durable `## Learned Notes` writes to `SKILL.md`.
- Closure path: plugin-tool operation fails → bundled hook captures tool/error evidence → LLM generates an instruction intended to prevent recurrence → proposal is stored → Agent inspects pending evolution patches → Agent chooses `apply` → first-party tool rewrites target `SKILL.md` with learned guidance → later skill loading/model guidance changes future operational capability.
- Boundary reachability: `skill-evolve` is one of the bundled app-skills auto-installed by the shipped gateway runtime, and its manifest exposes `skill_evolve` as a standard model-visible plugin tool rather than a repository-development-only script.
- External distinction: the adaptation begins from an observed plugin-tool interaction failure at the system/environment interface, not from a static roadmap or maintainer backlog.
- Future / prospective distinction: the generated suggestion is explicitly framed as an instruction that would prevent recurrence; it is queued as a durable change proposal rather than used only to retry the current call.
- Adaptation option generated: an LLM-generated one-line correction to the owning skill's model-facing instructions, with optional consolidation of accumulated learned notes.
- Path back into current capability / S3: applying the proposal writes durable skill guidance used by the harness' skill-loading/model-prompt path, changing how subsequent Agent operation approaches that tool; S3/master operation can then use the adapted skill under the new instruction.
- Why this is / is not agent-owned: proposal generation is automated but explicitly does not apply patches by itself. The positive `A` claim rests on the separate first-party model-visible tool through which the Agent itself can inspect the queue and choose apply/discard; without that decision path the hook alone would not justify autonomous S4.
- Evidence: [`crates/app-skills/skill-evolve/SKILL.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/crates/app-skills/skill-evolve/SKILL.md); [`crates/app-skills/skill-evolve/manifest.json`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/crates/app-skills/skill-evolve/manifest.json); [`crates/app-skills/skill-evolve/src/main.rs`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/crates/app-skills/skill-evolve/src/main.rs); [`docs/ARCHITECTURE.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/docs/ARCHITECTURE.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: memory refresh, monitors, loops and adaptive provider routing are not independently credited as S4 here. The positive witness is the failure-derived prospective skill-change loop with an agent-owned apply/discard right. Failures that carry no environment-relevant lesson would not themselves establish S4; the credited path is the supported mode where the failure yields a reusable future-facing correction.

## S5 — Policy and identity

- State: P
- Function: establish and amend the runtime Agent's authoritative identity/personality/value layer that governs subsequent operation.
- Disturbance / variety regulated: the current identity, personality or value definition may no longer match the legitimate workspace/operator's intended organizational identity and policy.
- Decisive decision or feedback right: decide the authoritative contents of the custom identity/value bootstrap files that are injected into subsequent model-visible system context.
- Decision owner: legitimate parent workspace/operator authority editing `.octos/IDENTITY.md` and/or `.octos/SOUL.md`.
- Supporting / enforcement mechanisms: bootstrap-file loader, `.octos/IDENTITY.md` custom identity definition, `.octos/SOUL.md` personality/values and hot reload into the system prompt.
- Closure path: parent identifies an identity/value policy change → parent edits the authoritative bootstrap file → first-party runtime detects/reloads bootstrap content → subsequent Agent turns receive the new identity/value definition in their system prompt → operation proceeds under the returned parent decision.
- Boundary reachability: bootstrap identity files are a documented shipped runtime surface created by `octos init`; their hot-reload path operates inside the standard runtime and does not require `octoscode` or repository-maintainer governance to enforce the decision.
- Identity / ultimate-policy issue: what identity, personality and values the runtime Agent is to operate under for the workspace/profile.
- Ultimate authority in each claimed mode: parent `P` mode — the legitimate workspace/operator authority that owns the bootstrap identity/value files. No autonomous ultimate-authority mode is established.
- Return-to-operation path: edited bootstrap content is hot-reloaded and injected into the model-visible system prompt, so subsequent Agent behavior is governed by the new parent decision.
- Why this is / is not agent-owned: generic filesystem capability does not make the operating Agent the legitimate ultimate authority over its own identity. The documented governance surface assigns definition to workspace bootstrap files edited by the parent/operator; therefore only `P` is credited.
- Evidence: [`book/src/memory-skills.md`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/book/src/memory-skills.md); [`crates/octos-cli/src/config_watcher.rs`](https://github.com/octos-org/octos/blob/9f6311afd4e00324cdb89d957461cf861f4f2630/crates/octos-cli/src/config_watcher.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic `system_prompt`, tool policy, permission profiles, approvals and arbitrary writable files are not independently credited as S5. The positive witness is the explicit identity/value bootstrap surface plus its first-party return-to-operation path.

## Recursion

The assessment is fixed at one Octos runtime organization around a profile/workspace/session objective. Ordinary Agents, child agents and sovereign peers are operational S1 units within that recursion when they act on delegated work. A human/application OUP controller is treated as legitimate parent authority only for the explicit S3 parent mode; it remains outside the autonomous S1 boundary. External providers, MCP services and client applications are environment/dependencies.

## Variety and escalation

Octos attenuates operational variety through sandbox/tool policy, durable session state, context compaction, task supervision, budgets, retries and workflow topology. Those mechanisms are not promoted to metasystem ownership merely because they are deterministic. The positive metasystem findings rely on narrower function-specific closures: peer worktree fencing for S2; current fleet/task intervention for S3; specialist review for S3*; failure-derived skill adaptation for S4; and hot-reloaded parent identity/value definitions for S5.

Escalation can move from autonomous operation to a parent through approvals, questions and OUP intervention. That generic escalation path is treated as support unless it closes one of the function-specific loops above.

## Evidence gaps

- S2 depends on the supported agent-created peer mode with `worktree` fencing; ordinary non-worktree peers and generic swarm parallelism do not establish the same anti-interference relation.
- S3 parent mode is credited at the runtime/OUP boundary, not to any specific external client implementation; client-side policy remains outside the assessment boundary.
- S3* is established through the shipped backend-owned code-review workflow. This assessment does not generalize every validator, pipeline gate or specialist configuration into complementary audit.
- S4 is established through `skill-evolve`; no claim is made that memory refresh, monitoring, loops or provider routing independently satisfy outside-and-then intelligence.
- S5 credits the explicit identity/value bootstrap authority. The review found no first-party evidence that the autonomous Agent is itself the legitimate ultimate authority entitled to amend that identity, so no `A` base mode is published.
