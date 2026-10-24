---
harness_id: cafleet
project_name: CAFleet
repository: https://github.com/himkt/cafleet
review_ref: a991fe8f818a5e65770f32db3867f50b178c2e73
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# CAFleet

## Review boundary

- System in focus: shipped CAFleet Rust/SQLite CLI and broker, tmux/herdr member lifecycle, embedded `cafleet` and `cafleet-design-doc` skills **installed by `cafleet setup`**, at frozen upstream `a991fe8f818a5e65770f32db3867f50b178c2e73`. One supported *skill-driven development fleet* is the assessed unit, with Director, Programmers/Testers, fleet monitor and conditional fresh Reviewer; no claim of a self-hosted coding LLM inside Rust.
- Purpose and identity: provision named external coding-agent member seats, preserve fleet-scoped identities/messages, coordinate delegated work and gate design-doc implementation through separate fresh review and user approval.
- Relevant environment: operator/user, Git working branch, approved design document, external Claude/Codex/OpenCode CLIs, tmux/herdr panes, SQLite fleet/member/message rows, tests/diffs/command replies and installation directories.
- Standard-distribution boundary: `cafleet setup` embeds and installs *both* named skills and supported coding-agent presets for available provider backends; Fleet CLI creates member panes and real associations; model agent follows installed Director/execute skill to coordinate actual work. The workflow is **agent-instruction-enforced**, not a Rust-enforced end-to-end transaction; distinguish source-supported mode from observed execution.
- Credited operating / distribution surfaces: installed `cafleet` and `cafleet-design-doc` skills; active member/monitor registry, messaging, pane spawn, per-fleet uniqueness constraints, live wake gate; conditional skill-driven Director/Tester/Programmer/fresh Reviewer and human approval/PR sequence.
- Adjacent first-party surfaces excluded from ownership: 180+ speculative/historical `design-docs/*` and `SPEC.md` prose beyond shipped implementation; bare GitHub CI; external coding agents' internal models, review logic, tools and interactive UI; other uninstalled ad hoc prompting; operations not authorized by the operator.
- First-party operating / deployment modes considered: installed model-backed agents over supported Claude/Codex/OpenCode backends; runtime fleet create + monitor/member registration; `cafleet-design-doc execute` **explicitly invoked** on an approved design document with its fresh Step 5 review, rework, Step 6 human approval, and first-party event/trace transport. Plain broker-only messaging does **not** inherit the skill's S3/S3*.
- Recursion level: one configured fleet of model-backed independent member operations and its skill-governed Director, with the monitor and Reviewer distinct from ordinary Programmer/Tester workers.
- Reviewed revision: `a991fe8f818a5e65770f32db3867f50b178c2e73`.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The installed Rust program does **not** replace Claude Code, Codex or OpenCode's own reasoning engines. It owns fleet-scoped SQLite members and message state, backend-specific pane spawn, process routing, monitor heartbeat/wake, CLI and WebUI read/write operations. Its `assets::install_agent` installs both `cafleet` and `cafleet-design-doc` first-party skills during `cafleet setup` into supported agents' skill directories. Therefore the usable agent organization is a composition of first-party executable local control/data plane **plus** first-party distributed agent instructions, operating over environmental model CLIs; mere existence of a skill file outside this install path would not establish ownership ([cafleet/src/assets.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/assets.rs), [cafleet/src/cli/setup.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/setup.rs), [cafleet/src/broker/members.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/members.rs), [cafleet/src/cli/fleet.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/fleet.rs)).

**S1** is model-backed worker execution *in the installed skill mode*. The Director chooses real members, `cafleet member create` allocates member/placement IDs and spawns an external coding-agent pane with rendered task prompt, and a worker implements/reviews/tests with feedback from Git/tests/tools. The Rust broker cannot itself accomplish coding or analysis; the configured external model executing an installed CAFleet member role makes operational decisions ([cafleet/src/cli/member.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/member.rs), [cafleet/src/cli/creation.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/creation.rs), [cafleet/src/broker/members.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/members.rs), [skills/cafleet/roles/director.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/roles/director.md), [skills/cafleet-design-doc/execute/roles/programmer.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/roles/programmer.md)).

**S2** is a *narrow* first-party interference attenuator for monitor ownership in a live fleet, not ordinary message transport. A fleet's operational monitor is itself a model-backed member expected to run the liveness/wake loop. The broker rejects concurrent active monitor registration by an immediate SQLite transaction/unique partial index and `monitor_tick` stops on loss of ownership-checked heartbeat. This suppresses two competing monitor members simultaneously claiming the single fleet-wide wake right and disturbing other work/Director signaling. It does not prevent parallel Programmers from editing overlapping files, nor does fleet namespace/message filtering alone prove S2 ([cafleet/migrations/V8__unique_active_monitor.sql](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/migrations/V8__unique_active_monitor.sql), [cafleet/src/broker/members.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/members.rs), [cafleet/src/monitor/mod.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/monitor/mod.rs), [skills/cafleet/reference/supervision.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/reference/supervision.md)).

**S3** belongs to the operating model Director in the installed `cafleet-design-doc execute` mode, not to the deterministic broker. The Director reads complete design tasks/test evidence, chooses members and assigns work, handles failures/denied commands, decides retry/escalation/recovery/replacement and advances phases after feedback. `cafleet message send/poll/ack`, captured pane state and member create/ping commands form first-party effects/return, but the strategic present-choice owner is the model running the Director role via a supported backend. In broker-only installations with no role skill invocation, no S3=A is claimed ([skills/cafleet-design-doc/execute/execute.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/execute.md), [skills/cafleet/roles/director.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/roles/director.md), [cafleet/src/broker/messaging.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/messaging.rs), [cafleet/src/cli/member.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/member.rs)).

**S3*** is a *conditional autonomous complementary audit workflow* within the same **installed skill**. After implementation and optional E2E verification, the Director creates a **fresh reviewer** that is forbidden to write implementation/test code. It reads the design document and **full Git branch diff** rather than merely the Programmer's status, runs separate read-only quality checks, and returns file/line-tagged findings. The Director assigns corrections, reruns review **without an attempt cap**, and does not proceed to separate user approval until the reviewer returns `approved (doc)`. Reviewer judgment is owned by a distinct model-backed agent under a shipped role/prompt; the workflow's decision-and-return is instruction-enforced, not a hard-coded broker validator. This is S3*=A **only for explicitly invoked design-doc execution**, not an all-purpose independent audit automatically applied to `cafleet message send` ([skills/cafleet-design-doc/execute/execute.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/execute.md), [skills/cafleet-design-doc/execute/roles/reviewer.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/roles/reviewer.md), [skills/cafleet-design-doc/reference/coordination.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/reference/coordination.md), [cafleet/src/assets.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/assets.rs)).

The monitor tracks and wakes live members; that is current liveness/control assistance, not direct independent quality verification of produced code. Continuous model catalog refresh or model-selection tips and design-doc feature requests do not constitute an executable future/external environment adaptation loop. Likewise backend permissions, member identity and human approval are current operating constraints, not a separately evidenced ultimate identity/ethos policy decision organ ([skills/cafleet/reference/supervision.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/reference/supervision.md), [skills/cafleet/roles/director.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/roles/director.md), [cafleet/src/cli/setup.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/setup.rs)).

## Operational model

After `cafleet setup`, a supported user agent can invoke the installed design-doc execute skill. That agent assumes Director and uses broker/CLI to create a fleet, register members and monitor, orchestrate Programmer/Tester/Verifier work and receive persisted messages. Two monitor launch attempts contend for a uniquely owned live monitoring slot. Once code changes exist, a separately spawned Reviewer inspects actual Git diff and evidence and either requests rework (returning to implementers) or approves the handoff; the human then separately decides publication. Model decisions and prompt compliance are not empirically witnessed here; this is a first-party source-backed supported mode.

## S1 — Operations

- State: A
- Function: agent members complete assigned coding, tests or code review operations against a real repository via installed scoped role instructions.
- Disturbance / variety regulated: requirements ambiguity, code/test errors, tool or source feedback and local decisions about task implementation.
- Decisive decision or feedback right: actual model-backed assigned Programmer/Tester/Verifier chooses substantive tool/code/test actions within role constraints and returns results.
- Decision owner: external model-backed agent instantiated and role/prompt-scoped through first-party CAFleet skill and member creation; its general model internals are not owned by CAFleet.
- Supporting / enforcement mechanisms: Rust CLI member registration/pane creation, embedded skills/presets, durable fleet-scoped message ledger, role-specific task prompt, actual user Git repository/working branch.
- Closure path: designated code/test task → first-party member spawn with role prompt → model-backed member interacts with files/tests and adjusts work → persisted `cafleet message send` result and artifacts → Director sees status.
- Boundary reachability: Rust `member create` with rendered prompt and `setup` installed roles; supported external Claude/Codex/OpenCode CLIs required as environmental inference executors.
- Why this is / is not agent-owned: removing the operating model agent leaves only deterministic broker/pane mechanics and cannot complete coding work.
- Evidence: [cafleet/src/assets.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/assets.rs); [cafleet/src/cli/member.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/member.rs); [cafleet/src/broker/members.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/members.rs); [skills/cafleet-design-doc/execute/execute.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/execute.md); [skills/cafleet-design-doc/execute/roles/programmer.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/roles/programmer.md).
- Basis: first-party shipped/invocable composition and real command implementation.
- Confidence: medium-high source reachability; no live inference witnessed.
- Caveats: bare broker/CLI sessions without model-backed members or design-doc skill cannot inherit these positive functions.

## S2 — Coordination

- State: C
- Function: prevent multiple operational monitor cells from concurrently claiming the single live fleet monitoring/wake responsibility.
- Disturbance / variety regulated: duplicate monitor/wake loops could compete and flood or cross-trigger Director/member attention, confusing sibling operations.
- Decisive decision or feedback right: hold/reject active monitor registration and stop monitor ticks without the valid owner heartbeat.
- Decision owner: first-party Rust/SQLite monitor ownership constructor (not discretionary LLM regulator).
- Supporting / enforcement mechanisms: unique active-monitor index, immediate registration transaction, ownership-checked runtime heartbeat.
- Closure path: two would-be monitor member registrations within fleet → unique constraint permits only one active monitor → only owner loop maintains heartbeat and issues batched wake → other candidate fails or stops, leaving unique coordination channel.
- Boundary reachability: `fleet create` bootstraps a monitor and `monitor_tick` is the actual running monitor-loop implementation, not merely specification.
- Why this is / is not agent-owned: deterministic gating of competing monitor operations, distinct from messaging reliability.
- Distinct S1 units: model-backed operational monitor members, potentially attempted concurrently; one retained active slot.
- Inter-S1 disturbance: two independently initiated monitors both try to wake/support the same live fleet and perturb active worker/Director behavior.
- Attenuating coordination relation: transaction-backed exclusive monitor identity and tick ownership heartbeat.
- Feedback into subsequent S1 behaviour: only the valid monitor supplies Director wake context and all other launched monitor attempts receive explicit errors/stop.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it excludes physically conflicting current regulatory operations by enforcing exclusive live responsibility.
- Evidence: [cafleet/migrations/V8__unique_active_monitor.sql](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/migrations/V8__unique_active_monitor.sql); [cafleet/src/broker/members.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/members.rs); [cafleet/src/monitor/mod.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/monitor/mod.rs); [cafleet/src/cli/fleet.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/fleet.rs).
- Basis: shipped code, unique constraint and monitor semantics.
- Confidence: medium: narrow constrained mode; no observed live monitor collision test claimed beyond source tests.
- Caveats: no evidence of automatic cross-member Git conflict suppression or worktree isolation.

## S3 — Inside-and-now control

- State: A
- Function: decide and regulate currently pending/blocked fleet work assignments and interventions across the installed design-doc execution.
- Disturbance / variety regulated: unresolved tasks/tests/reviews, failed/spinning members, uneven member availability and user interruptions.
- Decisive decision or feedback right: model Director decides who to spawn, which current phase/step to release or retry, how to arbitrate defects or escalate, and when work is ready for review.
- Decision owner: active model-backed Director using installed `cafleet-design-doc` skill; broker provides command effects and read-back.
- Supporting / enforcement mechanisms: fleet/member list, captures, persisted message send/poll/ack, worker roles, Director rule set, monitor wake.
- Closure path: current design-doc/task/member/review state → Director chooses intervention/assignment → real `cafleet member create/message send/member ping` commands → member actions/new reports/captures return to next Director decision.
- Boundary reachability: `cafleet setup` installs Director/execute skills, and Rust implements the invoked CLI effects; explicit skill invocation required.
- Why this is / is not agent-owned: Director prompt delegates whole-fleet current judgment to an active model, not simple deterministic queued routing.
- Whole-system current view: active members, issue/doc state, test results, messages and observer member pane state of one fleet.
- Current-control decision scope: membership and task routing, retry/review escalation, work hold, acceptance handoff and shutdown; never tenant-global ultimate policy.
- Evidence: [skills/cafleet-design-doc/execute/execute.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/execute.md); [skills/cafleet/roles/director.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/roles/director.md); [cafleet/src/cli/member.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/member.rs); [cafleet/src/broker/messaging.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/messaging.rs); [cafleet/src/monitor/mod.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/monitor/mod.rs).
- Basis: installed agent instructions plus executable effects.
- Confidence: medium in supported workflow, not empirically observed autonomy performance.
- Caveats: Rust broker alone does not choose present commitments; workflow is prompt-compliance dependent.

## S3* — Complementary audit

- State: A
- Function: separate fresh agent quality review of real code changes against design acceptance with binding rework before operator approval.
- Disturbance / variety regulated: incorrect or incomplete implementer claims, missing behavior, defects or code/test mismatch unnoticed by implementers.
- Decisive decision or feedback right: independently inspect the whole branch diff and quality checks, report annotated defects or `approved (doc)`; Director follows mandatory re-review workflow.
- Decision owner: a fresh model-backed Reviewer spawned separately after implementation by a model-backed Director, with read-only role constraints; human operator separately controls final publication.
- Supporting / enforcement mechanisms: installed `cafleet-design-doc execute` Step 5, `roles/reviewer.md`, Director's issue-marker protocol, git diff, read-only test tools, message ACK/status, Step 6 human approval.
- Closure path: code+tests complete → *new distinct Reviewer* reads full branch diff and design criteria → Reviewer sends source-line findings → Director dispatches fixes → reviewer rechecks without cap → only `approved (doc)` permits user acceptance and publication steps.
- Boundary reachability: built-in `setup` skill installation, conditionally invoked `execute` skill; executable member creation, messaging, prompts and real checkout. Not a default broker-wide transaction.
- Why this is / is not agent-owned: a first-party shipped role binds a genuinely distinct model-backed Reviewer to independent original code evidence; review does not merely repeat implementer self-report. The binding phase sequence is first-party skill instruction rather than hard backend enforcement.
- Claim being audited: implementer has delivered requirements-compliant work with passing tests/ready for approval.
- Ordinary reporting path: Programmer/Tester results and step completion messages to Director.
- Complementary access path: fresh Reviewer reads actual full Git diff, design spec and runs targeted read-only tests, returning explicit source-anchored issues.
- Independence boundary: fresh model role has no code authorship/commit permission in the skill and sees diff not just implementer summary; no guarantee of independence across model weights/providers or perfect compliance.
- Who acts on findings: model Director sends fixes to Programmer/Tester, repeats separate Reviewer gate and only then asks operator.
- Evidence: [cafleet/src/assets.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/assets.rs); [skills/cafleet-design-doc/execute/execute.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/execute.md); [skills/cafleet-design-doc/execute/roles/reviewer.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/roles/reviewer.md); [skills/cafleet-design-doc/reference/coordination.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/reference/coordination.md).
- Basis: mode-bounded first-party installed skill autonomous audit return.
- Confidence: medium; unobserved reviewer invocation and prompt compliance.
- Caveats: not a Rust-enforced hard gate, no global automated quality guarantee, operator may use ordinary CAFleet as generic broker with no `execute` role.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped fleet-level externally informed prospective organizational capacity adaptation path established.
- Disturbance / variety regulated: longer-term changes in coding provider capabilities, tool landscape and work requirements.
- Decisive decision or feedback right: decide and implement future system adaptations based on external sensing, not evidenced in installed paths.
- Decision owner: the human or model can pick member model/roles for current task, but this is deployment/current S3 rather than a separate prospective organ.
- Supporting / enforcement mechanisms: model catalog guidance, role presets, cost-mode choice, historical messages/design docs, per-fleet config.
- Closure path: current task spawns may select models, but no proven external prospecting → changed future fleet capability → applied new organizational capacity feedback.
- Boundary reachability: inspected bundled install, model selection, docs planning and monitor signals; these concern present execution or maintenance.
- Why this is / is not agent-owned: a model choosing a cheaper reviewer for this session is not long-horizon S4 future adaptation.
- Evidence: [skills/cafleet/roles/director.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/roles/director.md); [skills/cafleet/reference/coding-agents.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/reference/coding-agents.md); [cafleet/src/assets.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/assets.rs); [cafleet/src/monitor/mod.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/monitor/mod.rs).
- Basis: bounded negative after checking likely shipped paths.
- Confidence: medium.
- Caveats: humans may create new skills/models outside assessed package.

### Absence scope

- Surfaces inspected: available model catalogs, role creation choices, skill install/update flow, monitoring/telemetry and design-doc workflows.
- Plausible first-party paths checked: cost efficiency mode, replacement or re-spawn using better model, agent role reassignment, monitor health feedback.
- Why no material first-party path remains: these adapt the **current fleet workload** or deliver fixed packaged assets, not prospectively assess changing external demands and return enduring fleet capacity changes.

## S5 — Identity and ultimate policy

- State: —
- Function: distinct legitimate fleet identity/ethos/ultimate policy choice and governing return not demonstrated.
- Disturbance / variety regulated: unresolved organizational purpose, ethical mandate and conflicting long-term versus current demands.
- Decisive decision or feedback right: settle ultimate organizational identity commitments and return new policy into the fleet; not evidenced.
- Decision owner: operator/user owns publication and higher-authority decisions outside the broker; that is not automatically S5.
- Supporting / enforcement mechanisms: fleet registry/slug and Director identity, model backend choice, role instructions, human approval, command allow/deny/escalation.
- Closure path: user approves changes or commands; no distinct ultimate policy issue and authority settlement governing both present and prospective functions.
- Boundary reachability: shipped fleet create, identity, deny-command decision surface and Step 6 user approval inspected.
- Why this is / is not agent-owned: ordinary code approval, permissions and naming do not establish model or parent-owned organizational ultimate identity regulation.
- Evidence: [skills/cafleet/roles/director.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet/roles/director.md); [skills/cafleet-design-doc/execute/execute.md](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/skills/cafleet-design-doc/execute/execute.md); [cafleet/src/broker/fleets.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/broker/fleets.rs); [cafleet/src/cli/fleet.rs](https://github.com/himkt/cafleet/blob/a991fe8f818a5e65770f32db3867f50b178c2e73/cafleet/src/cli/fleet.rs).
- Basis: bounded negative for assessed recursion.
- Confidence: medium-high within assessed mode.
- Caveats: real human organizations necessarily have governance outside CAFleet, not credited as first-party S5.

### Absence scope

- Surfaces inspected: fleet identity and membership, role/scoped permissions, human approval, escalations and publication policy.
- Plausible first-party paths checked: Director command refusal, user approval before push, backend model selection, initial fleet naming and skill instructions.
- Why no material first-party path remains: these are current execution/review/permission constraints, not a recorded final policy-identity decision with returned normative authority over the whole fleet.

## Evidence gaps

- Pinned first-party source assessment only; no actual external coding-agent runs, independent fresh reviewer sessions, live tmux monitor collisions or user approval observed.
- S3 and S3* are **instruction-enforced** first-party packaged skill functions, not Rust code making those discretionary decisions. A generic broker-only installation is not claimed autonomous at either function.
- S2 narrowly protects the unique operational monitor seat; does not solve ordinary same-file writes from Programmers.
- All positive claims rely on supported configured mode. Skill compliance and runtime effectiveness have not been independently empirically established. The terminal step is an operator approval, not agent S5.
- Historical design-doc prose, maintainer CI, source comments and provider-side capabilities were not silently promoted to the assessed fleet.

## Conclusion

**Proposed, not canonical:** in the bundled `cafleet-design-doc execute` skill mode with live model-backed agents and real Rust/SQLite broker, `S1=A / S2=C / S3=A / S3*=A / S4=— / S5=—`. The program instantiates external model-agent member operations, attenuates competing monitor ownership, and the installed Director/Reviewer role contract offers an agent-owned whole-current control path and genuinely fresh direct-diff audit/rework cycle before human publication. All decisions are source-supported but not empirically witnessed, and the broker-only mode does not inherit the optional workflow's ownership.
