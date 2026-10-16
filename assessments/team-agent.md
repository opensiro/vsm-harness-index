---
harness_id: team-agent
project_name: Team Agent
repository: https://github.com/Florious95/team-agent
review_ref: 1107b2881b7c55bde14a270f472db034cfefcc9a
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Team Agent

## Review boundary

- System in focus: first-party Team Agent Rust binary/library, installed team-agent skill, registered MCP team/lifecycle tools, team spec/role compiler, durable team state, local tmux transport and managed provider-backed leader/teammate seats at the exact frozen revision.
- Purpose and identity: construct and operate a persistent multi-role team of launched coding/research/review assistants, supporting task assignment, peer messaging, structured result return, session continuation and team status.
- Relevant environment: operator, workspace Git repository, supported installed provider CLI (Claude Code/Codex/Copilot and separately enabled providers), tmux/terminal panes, team roles and task state, peer message envelopes and report/result records.
- Standard-distribution boundary: shipped `team-agent` CLI/MCP daemon and installed skill/role bindings; launchable/managed agent seats and returned work are part of the *composed Team Agent team*. Vendor provider inference, Claude/Codex/Copilot's internal tools/governance and independent abilities are external dependencies and cannot donate other VSM functions.
- Credited operating / distribution surfaces: README supported launch/quick-start, `skills/team-agent/SKILL.md` and installed packaging, compiled team spec and per-worker prompts, `lifecycle::launch::spawn_agents`, `messaging::send_message/report_result`, `mcp_server::tools` team status/add-agent tools, durable team state and restart collision guards.
- Adjacent first-party surfaces excluded from ownership: `.team/artifacts` dogfood review reports, giant regression fixtures, `examples/team.spec.yaml` as non-default configuration, packaged docs describing future capabilities, upstream provider harness implementation, CI/releases/maintainer decisions.
- First-party operating / deployment modes considered: installed wrapper `team-agent claude/codex/copilot`, lead + first-party managed worker seats from a loaded team spec, optional multiple workers/tmux sockets and resume/restart, delegated peer communications, user-configured specialized reviewers; no live provider run was executed.
- Recursion level: one active Team Agent team with leader and managed specialist seats; internal provider-level subagents remain outside this level.
- Reviewed revision: `1107b2881b7c55bde14a270f472db034cfefcc9a` (frozen intake #193).
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Team Agent is a substantial first-party Rust lifecycle/communication control harness. `team-agent` wraps an installed provider CLI, creates persistent named leader and worker seats with separately compiled role/prompt and MCP tooling, drives tmux/terminal transport, records durable team state and delivers peer task/results messages. The model/tool inference inside Claude/Codex/Copilot is not implemented by this repository. The owned organization instead binds a provider-backed model actor to a named, stateful role and supplies Team Agent-specific task, teammate and session tools. The installed provider-backed role can then choose substantive work operations and return results through `report_result`, distinct from the fixed deterministic Rust launch/transport machinery ([README.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/README.md), [crates/team-agent/src/lifecycle/launch/spawn.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/launch/spawn.rs), [crates/team-agent/src/mcp_server/tools.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/tools.rs), [crates/team-agent/src/packaging/install.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/packaging/install.rs)).

Sibling worker interference has a specific **pane occupancy** hazard. On restart, `pane_conflicts_with_leader_or_other` detects if one worker's persisted pane id is already bound to another teammate or to the leader on the same tmux socket. In the supported restart path, that stale binding is not accepted as an active same-worker Noop; Team Agent forces a fresh worker spawn/ownership reconciliation instead. This suppresses *cross-seat invocation on the wrong physical process/pane*, not semantic Git merge conflicts. The running mode uses one owned logical actor per physical pane, while transport details and identity resolution are deterministic control mechanisms ([crates/team-agent/src/lifecycle/restart/agent.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/restart/agent.rs), [crates/team-agent/src/messaging/delivery.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/messaging/delivery.rs), [crates/team-agent/src/topology.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/topology.rs)).

The managed leader receives a team-level operation surface. The installed skill instructs the leader to orchestrate a live team; MCP tools include `get_team_status`, `add_agent`, `send_message`, result receipt and worker lifecycle. From the team-wide status, the model-backed leader may choose which specialist to assign, whether to add a seat, whom to message or which blocked work to redirect; these choices reach the first-party CLI/MCP and its durable state. The model chooses current organizational commitments; the Rust coordinator enforces address/identity/permission and consistency constraints. This is distinct from the externally supplied agent's own tool-level coding decisions ([skills/team-agent/SKILL.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/skills/team-agent/SKILL.md), [crates/team-agent/src/mcp_server/tools.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/tools.rs), [crates/team-agent/src/mcp_server/lifecycle_tools/state_status.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/lifecycle_tools/state_status.rs), [crates/team-agent/src/lifecycle/launch/add_agent.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/launch/add_agent.rs)).

The README also advertises an explicitly configured separate reviewer. However an added reviewer role and review prompt do not by themselves prove a *default or optional shipped* independent direct-artifact audit and binding repair/recheck response at the declared team boundary. A future independent reviewer need not be required for this Index PR; only the first-party product audit function is being evaluated. Durable team memory/restart, role configuration, result envelopes, approval and scope checks do not automatically supply S4 external/future adaptation or S5 ultimate policy.

## Operational model

The user invokes `team-agent <provider>` and asks the provider-backed leader to create/operate a team. Team Agent's own runtime compiles each seat, launches the external provider CLI in a tracked tmux pane, installs Team Agent MCP/skill paths and records identity and scoped team state. Teammates autonomously pursue assigned tasks in their provider sessions and return results; leader consumes team state and returned results to decide current team actions. If a previous pane binding overlaps another active actor, restart guards prevent reuse. No external model reasoning loop or live provider outcome was inspected or borrowed for higher functions.

## S1 — Operations

- State: A
- Function: execute bounded user software/research work via durable role-bound, Team Agent-managed autonomous specialist seats.
- Disturbance / variety regulated: assigned task uncertainty, local repository state, tool feedback, failures and peer change requests handled by each managed provider-backed actor.
- Decisive decision or feedback right: choose substantive task-specific work in response to tool/environment observations and emit a structured result to the own team.
- Decision owner: model-driven Claude/Codex/Copilot worker **as a launched Team Agent seat**; the vendor runtime supplies inference while Team Agent owns the composed operational role and result channel.
- Supporting / enforcement mechanisms: compiled agent prompt, provider adapter, tmux transport, team spec, result envelope, task routing and durable state.
- Closure path: user/leader assigns result-oriented work → first-party session launcher binds provider-backed worker and callable team tool context → autonomous worker chooses local task actions and receives environment feedback → `report_result` returns work findings to the managed team.
- Boundary reachability: documented standard `team-agent` wrapper, `quick-start`, `spawn_agents` and `report_result` are shipped installed paths rather than external operator scripts.
- Why this is / is not agent-owned: without the instantiated model-powered specialist seat, Team Agent's transport/state cannot implement code itself. Credit is limited to the first-party **composition**, not provider-internal S2–S5, model performance or a standalone Rust coding loop.
- Evidence: [README.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/README.md); [crates/team-agent/src/lifecycle/launch/spawn.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/launch/spawn.rs); [crates/team-agent/src/mcp_server/tools.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/tools.rs); [skills/team-agent/SKILL.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/skills/team-agent/SKILL.md).
- Basis: explicit installed launch and task/result structure; no witnessed live provider transcript.
- Confidence: medium-high for reachability, not empirical work correctness.
- Caveats: operation requires a compatible installed provider CLI and credentials; without these the Rust control plane cannot produce autonomous S1 work.

## S2 — Coordination

- State: C
- Function: construct a collision-safe physical/identity mapping for multiple managed S1 seat processes during restart and later message delivery.
- Disturbance / variety regulated: stale restored team state can bind two distinct workers, or a worker and leader, to the same live pane/socket, directing later commands or messages to the wrong operational actor.
- Decisive decision or feedback right: refuse reuse of an overlapping pane binding and force a new correctly owned worker seat instead of accepting stale 'already live' inference.
- Decision owner: deterministic first-party lifecycle collision/reconciliation path (constructor `C`); the model does not decide physical pane safety.
- Supporting / enforcement mechanisms: `pane_conflicts_with_leader_or_other`, socket-sensitive pane identity, live-process checks, fresh-spawn fallback, scoped message-target resolution.
- Closure path: restart inventory + persisted bindings → detect cross-seat pane ownership conflict → reject stale Noop reuse and start a distinct process → subsequent task messages/commands are applied to separately bound worker seats.
- Boundary reachability: the collision check runs in the first-party `start_agent` restart path, not just a fixture; it applies when resuming supported persistent teams.
- Why this is / is not agent-owned: this is a deterministic first-party S2-specific interference attenuator rather than mere generic mailbox delivery or arbitration by a model.
- Distinct S1 units: separate provider-backed specialist seats in the *same* Team Agent team, and the lead as a separately bound session.
- Inter-S1 disturbance: the same pane process might be treated as owned by both teammates, leading to overlapping input and misattributed actions/results.
- Attenuating coordination relation: exclusive socket-sensitive pane ownership plus fresh-spawn on detected conflicting binding.
- Feedback into subsequent S1 behaviour: restored workers with invalid claimed panebindings are restarted/placed in their own pane; following work and messages target the corrected bindings.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it directly prevents two *operational actors* from sharing a contested execution endpoint; it does not merely queue or address messages.
- Evidence: [crates/team-agent/src/lifecycle/restart/agent.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/restart/agent.rs); [crates/team-agent/src/messaging/delivery.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/messaging/delivery.rs); [crates/team-agent/src/topology.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/topology.rs).
- Basis: structural deployed restart code with a concrete collision condition and response.
- Confidence: medium for supported protection; no live pane-collision trial.
- Caveats: protects process/pane identity contention, not conflicting file edits across agents.

## S3 — Inside-and-now control

- State: A
- Function: model-led current team commitments and specialist assignment across multiple managed worker operations.
- Disturbance / variety regulated: incomplete work, mismatched expertise, changing team capacity, needs for additional specialist seats and task/result coordination.
- Decisive decision or feedback right: decide when to add a role, to whom to assign a task, what current status requires response and which current worker/leader message to send.
- Decision owner: provider-backed **managed leader agent** when operating under the shipped Team Agent skill/MCP organization; the first-party Rust runtime executes commands but does not choose the team's changing work portfolio.
- Supporting / enforcement mechanisms: team-status observation, role/spec compiler, team-scoped messaging and MCP, lifecycle add/restart/stop, durable task and result records.
- Closure path: currently registered seats/status/results → leader model chooses team-wide intervention → Team Agent MCP/CLI checks identity/scope and applies add-agent / send / lifecycle change → new worker state and returned results become visible to the leader and follow-on worker decisions.
- Boundary reachability: packaged `skills/team-agent/SKILL.md` is installed into provider skill locations; `team-agent <provider>` launches the leader, and MCP tools `get_team_status`, `send_message` and `add_agent` are backed by first-party runtime implementations.
- Why this is / is not agent-owned: the leader can choose context-dependent changes in team capacity/commitments; status persistence and command validation alone would not pick the same changes.
- Whole-system current view: scoped team roster/status, active workloads and results from registered teammates (not all external repositories/organizations).
- Current-control decision scope: select/redirect task assignment and add/alter supervised execution capacity within the team rather than only performing its own local code action.
- Evidence: [README.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/README.md); [skills/team-agent/SKILL.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/skills/team-agent/SKILL.md); [crates/team-agent/src/mcp_server/tools.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/tools.rs); [crates/team-agent/src/mcp_server/lifecycle_tools/state_status.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/lifecycle_tools/state_status.rs); [crates/team-agent/src/lifecycle/launch/add_agent.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/launch/add_agent.rs).
- Basis: shipped model-led leader composition + executable team lifecycle; not a witnessed team run.
- Confidence: medium; generic provider model behavior beyond the Team Agent-provided tool/right surface is not assumed.
- Caveats: no distinct `(P)` mode is added merely because the user can also issue shell commands or instruct the leader; a separate parent-mode current-control closure would need its own evidence.

## S3* — Complementary audit

- State: ?
- Function: specialized independently tasked reviewer is supported as a configured teammate, but complementary direct artifact access, audit judgment and corrective binding return are not fully established as one shipped role/mode.
- Disturbance / variety regulated: unsupported implementation claims and buggy patches returned by worker authors.
- Decisive decision or feedback right: an independent reviewer must challenge producer claims with direct repo/test access and cause acceptance rejection or a returned corrective action, not just send an ordinary peer message.
- Decision owner: potentially separately configured reviewer seat, but no shipped compulsory independent evidence or enforced rejection/recheck owner proven.
- Supporting / enforcement mechanisms: teammate role compiler, peer messaging, independent provider sessions, custom role files, structured result envelopes.
- Closure path: author reports output → optionally created reviewer may inspect it → messaging returns findings → **whether that finding changes a binding work acceptance decision is unverified**.
- Boundary reachability: `team-agent add-agent --role-file` and examples document reviewers, but these are configurable compositions; the standard runtime does not itself establish an independent audit protocol from name alone.
- Why this is / is not agent-owned: merely spawning a role called reviewer cannot prove separate access to raw operational reality or binding corrective closure.
- Evidence: [README.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/README.md); [examples/team.spec.yaml](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/examples/team.spec.yaml); [crates/team-agent/src/lifecycle/launch/add_agent.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/launch/add_agent.rs); [crates/team-agent/src/messaging/results.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/messaging/results.rs); [crates/team-agent/src/mcp_server/tools.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/tools.rs).
- Basis: plausible shipped composition; function-specific independent closure remains uncertain.
- Confidence: high in uncertainty, not a positive audited outcome.
- Caveats: a deliberately built multi-agent reviewer loop might qualify on its own exact first-party composition evidence.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party environmental future intelligence that chooses an adaptation of Team Agent's future operational capability is established.
- Disturbance / variety regulated: external changes in tools, roles, productivity constraints and future collaboration needs.
- Decisive decision or feedback right: detect future-relevant external difference, create/adopt a prospective capability change and return it to current operating team. Not established.
- Decision owner: user/developer can edit role files or reinstall tools, but no S4-specific first-party adaptation owner/closure is identified.
- Supporting / enforcement mechanisms: durable team state, session restart/clone, role files, user-requested seat changes, stored results.
- Closure path: messages and team state restore current work; no outside-and-then feedback loop changes future working capability through a distinct S4 decision.
- Boundary reachability: the runtime supports persistence and role composition, not autonomous environmental scanning/adaptation in the standard packaged team.
- Why this is / is not agent-owned: resuming agents or adjusting team count to satisfy today's request remains current operation/S3, not evidence of external-and-prospective S4.
- Evidence: [README.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/README.md); [crates/team-agent/src/lifecycle/restart.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/restart.rs); [crates/team-agent/src/state/persist.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/state/persist.rs); [crates/team-agent/src/lifecycle/launch/add_agent.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/launch/add_agent.rs).
- Basis: source-first standard mode absence.
- Confidence: medium-high under pinned reviewed boundary.
- Caveats: an external provider's own learning or user-installed future-intelligence skill is not credited.

### Absence scope

- Surfaces inspected: lifecycle state persistence/restart, installed team skill, role compiler, managed worker add/clone, messaging/results and startup controls.
- Plausible first-party paths checked: historical team memory, additional specialist selection, changing role specifications, session recovery and operator adaptation.
- Why no material first-party path remains: these paths restore or change current team topology and work, but do not observe external/future disturbances to develop and install a new prospective organizational capability.

## S5 — Identity and ultimate policy

- State: —
- Function: no decision-bearing ultimate identity/ethos/policy regulation beyond configured team identity/permissions has been evidenced.
- Disturbance / variety regulated: durable team mandate and ultimate goal/policy conflicts, distinct from authentication/role mapping.
- Decisive decision or feedback right: choose ultimate mission/policy and return it to govern subsequent team operation; not demonstrated.
- Decision owner: operator defines initial objective, team spec and role constraints; Rust runtime checks scoped identity/permissions but does not own ultimate policy judgment.
- Supporting / enforcement mechanisms: named team/owner key, team membership, captured MCP identity, agent-role configuration, lifecycle safety and permission flags.
- Closure path: initial human-defined team spec → binding launch/config scopes; no specific ultimate-policy dispute → legitimate parent decision → applied policy return cycle is established.
- Boundary reachability: identity and permission checks are first-party runtime paths but are insufficient for positive S5.
- Why this is / is not agent-owned: stable identity keys, enforced permissions and leadership role labels are mechanisms, not a legitimate identity-level ultimate policy decision organ.
- Evidence: [crates/team-agent/src/lifecycle/launch/identity.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/lifecycle/launch/identity.rs); [crates/team-agent/src/mcp_server/tools.rs](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/crates/team-agent/src/mcp_server/tools.rs); [skills/team-agent/SKILL.md](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/skills/team-agent/SKILL.md); [examples/team.spec.yaml](https://github.com/Florious95/team-agent/blob/1107b2881b7c55bde14a270f472db034cfefcc9a/examples/team.spec.yaml).
- Basis: structural bounded negative search under supported modes.
- Confidence: medium-high for pinned standard distribution.
- Caveats: a human operator may hold S5 for a wider project/institution; such authority is not automatically a first-party team-level `P` closure.

### Absence scope

- Surfaces inspected: team spec identity/objective, role compiler, installer skill, leader/team owner binding and MCP identity checks, CLI lifecycle/authority paths.
- Plausible first-party paths checked: leadership claims, team owner, role/permission policy, team objective persistence, user authorization, potential policy-level escalation.
- Why no material first-party path remains: checked surfaces authenticate, configure or enforce previously specified roles and operating constraints; none closes an ultimate identity/ethos policy choice with subsequent binding organizational return.

## Evidence gaps

- No live external provider interaction, managed-team coding trial or collision incident was run; assessments are limited to first-party pinned code's supported operating relationships.
- S3* stays `?` rather than assuming a ready review function from custom review roles or first-party transport reliability.
- S2 is confined to **physical seat/pane interference attenuation** during supported restart, not a claim of safe concurrent edits or semantic disagreement arbitration.
- The packaged `skills/team-agent/SKILL.md` declares a last-verified version different from the pinned Cargo package version; source-wired installed runtime and MCP tools, not that historical version label, ground reachability. A newer launch may require separate contract verification.
- External provider model internals, private user-created team specs and repository developer/dogfood artifacts are not additional first-party VSM evidence.

## Conclusion

**Proposed, not canonical.** The pinned Team Agent implementation supports role-bound provider-backed autonomous work (S1=A), guarded recovery from cross-seat physical pane collisions (S2=C), and managed model-leader whole-team current assignment/capacity control (S3=A) under its installed integration. Configurable reviewer roles leave S3* independent corrective closure unresolved (`?`); durable team state and static role/identity policy do not establish S4 or S5. Do not equate external CLI capabilities with functions delivered by Team Agent itself.
