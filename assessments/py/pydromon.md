---
harness_id: pydromon
project_name: pydromon
repository: https://github.com/sgeos/pydromon
review_ref: 65671672b812b1d4c88f8e7633fdd3a1e50bb5f0
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# pydromon

## Review boundary

- System in focus: One deployed Dromon Python project daemon with configured engine-backed session lines and its local operator.
- Purpose and identity: Keep project agent lines alive, communicating and governable across turns, sessions and model-provider constraints.
- Relevant environment: Local project worktrees/resources, subscribed/API-backed external agent engines, operator clients and optional peers/tools.
- Standard-distribution boundary: Implemented pydromon distribution, daemon/scheduler/event model, actual supported engine adapters, operator client and role/lease/run protocols at the exact pin.
- Credited operating / distribution surfaces: src/dromon daemon/scheduler/engine/adapters, eventlog/model/roles, project/line configuration, leases and local operator CLI/protocol.
- Adjacent first-party surfaces excluded from ownership: Repository process/roadmap/dogfood agent organization, developer review rounds, test fixtures and live probes; proposed later ports and unimplemented/explicitly refused engine modes do not own product functions.
- First-party operating / deployment modes considered: Configured Claude/Codex-backed lines, project operator supervision, declared resource leases/roles, optional supported peers and supervised runs. Nominal/prospective adapters are not borrowed as successful modes.
- Recursion level: One project organization containing operational lines/roles; the operator is its parent, external engine organizations remain outside.
- Reviewed revision: `65671672b812b1d4c88f8e7633fdd3a1e50bb5f0`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

A private-socket asyncio daemon is the sole SQLite event-log writer. Its tick scheduler delivers mail, starts nonbusy eligible lines and records work outcomes without blocking other lines. First-party drivers construct external engine sessions with configured tools/access. Local tools include mail/questions, named leases, role status/handoff/recovery, brief/context management and supervised runs. Role and lease invariants survive replay; operator commands inspect every line and revise budgets, configuration, models, owners and hold state. Current limits can hold a line and ask the operator; an operator reply resumes future operation. Generic proposals are private untrusted patch records, never automatically applied. Optional teacher code manages Ollama process/model availability and never consumes teacher output. See [scheduler][R1], [daemon][R3], [project configuration][R7] and [role design][R6].

## Operational model

Engine-backed lines are the discretionary operational actors; Dromon owns their first-party project composition and local control tools. Role names alone are not functions. Agent-mediated lease acquisition/release and write-owner handoffs provide concrete bounded coordination; the human project operator owns whole-project current resource/commitment intervention. Deterministic scheduler, exclusivity rules and automatic failover are enforcement/support rather than agent metasystem owners.

## S1 — Operations

- State: A
- Function: Configured session lines produce project work and exchange results through their first-party daemon composition.
- Disturbance / variety regulated: User tasks, local workspace changes, messages, background runs and engine/tool failures.
- Decisive decision or feedback right: Choose local tools, communications, work actions and whether to continue or end a turn.
- Decision owner: The model-backed session-line actor; external Claude/Codex/Pi engines supply inference/tool-loop dependencies rather than autonomous Dromon metasystem judgments.
- Supporting / enforcement mechanisms: First-party driver construction, tool exposure, mailbox/event log, wake scheduler, sandbox/settings composition and persisted engine sessions.
- Closure path: Queued mail/wake → line prompt and configured engine → chosen tools/messages/work → recorded turn outcomes → later line turns.
- Boundary reachability: The distributed daemon creates configured session lines with first-party Dromon tools and driver/engine wiring. The supported Claude/Codex-backed composition is executable without implementing a new harness.
- Why this is / is not agent-owned: Without the model-backed line actors, the daemon transports messages and enforces policy but cannot choose meaningful project work. Dromon does not receive credit for unrelated engine features.
- Evidence: [Scheduler][R1], [engine composition][R2], [daemon][R3], [line configuration][R4], [README][R5].
- Basis: structural.
- Confidence: high.
- Caveats: No live subscribed engine or paid model was run; engine independence and operational quality are not claimed.


## S2 — Coordination

- State: A
- Function: Declared resource leases and role-seat ownership regulate concrete shared-resource/write collisions among operational lines.
- Disturbance / variety regulated: Two active lines may try to use the same named project resource; role seats sharing a worktree must avoid competing writers and stale ownership transitions.
- Decisive decision or feedback right: A line chooses when to acquire/release a resource lease and can hand off or recover role ownership subject to observed eligibility.
- Decision owner: Configured agent lines own invocation/release/handoff choices; the operator declares permitted resource names/role terms, and deterministic state validates exclusivity.
- Supporting / enforcement mechanisms: Lease holder/expiry events, refusal with holder/expiration feedback, non-renewal/TTL, role owner invariants, engine access rebuilding and journaled handoff.
- Closure path: Contender calls acquire → receives grant or current-holder/expiry refusal → adjusts later resource use; release/expiry enables another acquisition. Role handoff records a note, transfers authority, wakes the successor and rebuilds the former owner's access.
- Boundary reachability: acquire_lease/release_lease and seat ownership tools are supplied to running lines by Scheduler; project-config leases/roles enable the shipped path, not a custom conflict resolver.
- Why this is / is not agent-owned: The actors decide when to reserve/release/pass work; the log and guards enforce those decisions. This credits that bounded agent-mediated coordination mode, not generic messaging or the scheduler itself.
- Evidence: [Lease tool and role tool implementations][R1], [role invariants/one-writer boundary][R6], [project enablement][R7], [line tool semantics][R4].
- Basis: structural.
- Confidence: medium.
- Caveats: Resource leases are cooperative: unmanaged external processes or ignored lease conventions are not forcibly excluded. Deterministic automatic failover is support, not autonomous discretion.

- Distinct S1 units: Independently configured session lines; different operational roles may contend for a shared resource, and seats can attempt conflicting access to a role worktree.
- Inter-S1 disturbance: Simultaneous use of a declared shared resource or competing writers/ownership transitions on a shared role worktree.
- Attenuating coordination relation: Exclusive resource lease with holder/expiry refusal and a single-writer role ownership protocol.
- Feedback into subsequent S1 behaviour: Lease errors tell a line who holds the resource and until when; releases permit retry. Handoff wakes and briefs the successor and removes former-owner write privilege where the engine supports it.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The tool/state path explicitly names shared-resource contention and conflicting worktree writers and changes who may proceed; mere mailbox delivery is not the credited witness.


## S3 — Inside-and-now control

- State: P
- Function: The project operator regulates the whole current set of session lines, role capacity, budgets and continuing commitments.
- Disturbance / variety regulated: Runaway autonomous turns/cost, held or failed lines, exhausted provider plans, conflicting current staffing and engine availability.
- Decisive decision or feedback right: Review project-wide state and choose line/role/budget/hibernation/rebind/interruption/release changes or answer a held line.
- Decision owner: The authenticated local project operator, acting as the legitimate parent of the project run. No first-party autonomous whole-project controller is established.
- Supporting / enforcement mechanisms: Private operator socket, all-line status summaries, durable events, operator-attributed messages, hold notices/question queue, CLI commands and scheduler/engine enforcement.
- Closure path: Whole-project status or held-line notice → operator current-control choice → daemon command/event → scheduler applies limits, ownership, model, hold or interruption changes → subsequent turns run under the returned decision.
- Boundary reachability: Daemon.execute serves operator-authority status/settings/role/budget/configure/release/interrupt commands, and status includes every line. The first-party scheduler routes hold questions and operator answers back into later operation.
- Why this is / is not agent-owned: Removing the operator leaves fixed limits and failover machinery, not discretionary whole-system resource/commitment revision. P describes the supplied supervised mode; enforcement does not become A or C.
- Evidence: [Operator protocol dispatch/current status][R3], [holds and operator-answer scheduler][R1], [project limits/roles][R7], [role runtime updates][R6], [client protocol][R8].
- Basis: structural.
- Confidence: high.
- Caveats: The parent boundary is this local project, not the public OSS organization; operator socket access is an explicit trust assumption.

- Whole-system current view: Daemon.status returns project/daemon health, event-log and question state, all line summaries, scheduler faults and peer/relay information; operator role/budget/settings views expand it.
- Current-control decision scope: Operator controls line limits/configuration, hold/release/interrupt/hibernate, role seats/owners, provider budgets and model rebinding over current project operations.


## S3* — Complementary audit

- State: —
- Function: No installed complementary independent audit judgment-and-corrective-return loop is supplied.
- Disturbance / variety regulated: Incorrect work-completion claims, stale notes, disclosure mistakes and engine-reporting errors.
- Decisive decision or feedback right: No separate audit-specific actor or constructor adjudicates operational truth and returns corrective control.
- Decision owner: Lines report their work; runtime observes process/session/log facts. Read-only seats are configured by users without a supplied audit workflow.
- Supporting / enforcement mechanisms: Daemon-stamped commit hashes, role journals, activity/event logs, raw transport evidence/replay and disclosure checks.
- Closure path: Facts can be inspected by an operator or peer; the standard product has no audit verdict/corrective-action protocol for a particular completion claim.
- Why this is / is not agent-owned: Independent fact capture is useful evidence but is not itself discretionary complementary audit; tests, developer reviews and optional advisory seats do not supply an installed audit function.
- Evidence: [Scheduler status/journal/check tools][R1], [engine transport evidence][R2], [evidence store][R9], [role design][R6], [line tools][R4].
- Basis: structural.
- Confidence: high.
- Caveats: A user can organize reviewer lines through general messages; that application would need separate function/independence/closure evidence.

### Absence scope

- Surfaces inspected: src/dromon/scheduler.py, daemon.py, engine.py, roles.py, model.py, eventlog.py, proposals.py, evidence.py, teacher.py, limits.py, projectconfig.py and lineconfig.py; README, protocol LINE_CONFIG/PROJECT_CONFIG/TEACHER/CLIENT and architecture ROLES/RUNS; deterministic test surfaces
- Plausible first-party paths checked: Checked read-only/advisory seats, role notes stamped by daemon, output digests, line_status, evidence/replay, disclosure checks, operator questions and supervised-run receipts for an independently owned audit verdict and enforced corrective return.
- Why no material first-party path remains: These paths are ordinary reporting, ground-fact recording, safety checks or generic communications. No first-party audit-specific challenge-to-current-control loop remains at the product boundary.


## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation loop is supplied.
- Disturbance / variety regulated: Provider budget changes, new model choices and suggested project patches are available current inputs.
- Decisive decision or feedback right: No shipped intelligence actor develops future-oriented capability options and closes their return into current capability.
- Decision owner: Operator chooses reconfiguration/upgrades; ordinary lines may submit untrusted patch proposals.
- Supporting / enforcement mechanisms: propose_change storage, project reload/rebind, provider-budget failover and optional local teacher lifecycle.
- Closure path: Proposals are explicitly never applied by Dromon; teacher code only loads/unloads a local model. Rebinding/failover responds to present availability rather than prospective adaptation.
- Why this is / is not agent-owned: A future roadmap, a model called teacher, context handoff or a current capacity switch is not S4. Generic operator patch handling does not create a function-specific parent adaptation loop.
- Evidence: [Proposal no-apply contract][R10], [teacher boundary][R11], [role failover][R6], [reload/rebind][R3].
- Basis: structural.
- Confidence: high.
- Caveats: Repository-development/dogfood decisions and future Rust/Keleusma ports are adjacent.

### Absence scope

- Surfaces inspected: src/dromon/scheduler.py, daemon.py, engine.py, roles.py, model.py, eventlog.py, proposals.py, evidence.py, teacher.py, limits.py, projectconfig.py and lineconfig.py; README, protocol LINE_CONFIG/PROJECT_CONFIG/TEACHER/CLIENT and architecture ROLES/RUNS; deterministic test surfaces
- Plausible first-party paths checked: Inspected proposal generation/storage, local teacher, model/strategy rebinding, provider-budget handoff, context/brief retention and roadmap/design documents for external/future distinctions, adaptation options and capability-return closure.
- Why no material first-party path remains: The shipped mechanisms maintain current project execution or collect suggestions; they do not establish an outside-and-then adaptation judgment and returned current-capability change.


## S5 — Policy and identity

- State: —
- Function: No function-specific identity/ultimate-policy decision-return loop is supplied.
- Disturbance / variety regulated: Access/disclosure rules, operator messages, project instructions and role terms.
- Decisive decision or feedback right: No identity-level issue is specifically adjudicated and returned by ultimate authority as a new governing policy.
- Decision owner: Operator configures the project and its permission/disclosure boundaries; agents have explicitly bounded local tools.
- Supporting / enforcement mechanisms: Operator/line address attribution, private socket trust, disclosure checks, tool/recipient policies, protected state and role rules.
- Closure path: Configuration and operator answers alter current execution, but no identity/ultimate-policy issue/decision protocol or S3–S4 balance closure is supplied.
- Why this is / is not agent-owned: The operator is a real parent for S3 current control; that does not promote all configuration or question replies to S5.
- Evidence: [Operator and line authority split][R3], [line tools/policy][R4], [project configuration][R7], [scheduler trust and question semantics][R1].
- Basis: structural.
- Confidence: high.
- Caveats: First-party development documents record human design decisions, but those are not an installed policy actor in an arbitrary user project.

### Absence scope

- Surfaces inspected: src/dromon/scheduler.py, daemon.py, engine.py, roles.py, model.py, eventlog.py, proposals.py, evidence.py, teacher.py, limits.py, projectconfig.py and lineconfig.py; README, protocol LINE_CONFIG/PROJECT_CONFIG/TEACHER/CLIENT and architecture ROLES/RUNS; deterministic test surfaces
- Plausible first-party paths checked: Inspected ask_operator/send_message issue type, operator-only role/config changes, disclosure rules, recipient restrictions, identity/authentication and development governance for a specific ultimate-policy issue reaching authority with a governing return.
- Why no material first-party path remains: Only generic communication, current project supervision and pre-authored constraints remain. No product-level identity/ultimate-policy loop is evidenced.


## Distributed OSS parent arrangement

The 0BSD repository's public maintainer and dogfood process are adjacent. Positive parent ownership is limited to the documented local project operator acting through its daemon socket; no organization-level VSM claim is inferred.

## Self-hosted and non-human modes

The daemon runs under the operator's user and trusts operator-socket clients; line/external-agent tools have narrower authority. This supplied supervised mode supports S3=P. No separately evidenced autonomous whole-project control, parent adaptation or parent ultimate-policy mode is claimed.

## Recursion

Roles and seats carry durable work/ownership but have no evidenced complete local metasystem. Federation and nested engine sessions do not by themselves establish viable recursion.

## Variety and escalation

Mailbox/context bounds, tool policies and sandbox composition attenuate operational variety; role journals, handoff briefs and durable mail preserve distinctions across session/provider changes. Leases attenuate shared-resource collisions. Held-line notices/questions can reach a real operator current-control authority, but a status or issue-kind message alone is not labelled an algedonic function.

## Evidence gaps

Static pinned-source review; no paid model, subscription probe, multi-agent E2E, teacher load or sandbox security experiment was run. Lease coordination is cooperative, and read-only/write enforcement depends on the documented engine capability. Future/nominal adapters and first-party dogfood review rounds are excluded from ownership.

[R1]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/src/dromon/scheduler.py
[R2]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/src/dromon/engine.py
[R3]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/src/dromon/daemon.py
[R4]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/docs/protocol/LINE_CONFIG.md
[R5]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/README.md
[R6]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/docs/architecture/ROLES.md
[R7]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/docs/protocol/PROJECT_CONFIG.md
[R8]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/docs/protocol/CLIENT.md
[R9]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/src/dromon/evidence.py
[R10]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/src/dromon/proposals.py
[R11]: https://github.com/sgeos/pydromon/blob/65671672b812b1d4c88f8e7633fdd3a1e50bb5f0/docs/protocol/TEACHER.md
