---
harness_id: herdr-core
project_name: herdr-core
repository: https://github.com/herdrdev/herdr-core
review_ref: b63ecbd1e6b6a7d63fb7bcf40f268930417723ba
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# herdr-core

## Review boundary

- System in focus: Shipped Rust `hc` headless persistent-terminal runtime and its local/remote process, command/template, input/status, agent-parent messaging and file/terminal API.
- Purpose and identity: Keep programs and coding-agent sessions alive, make them addressable and steerable, and let independently running agents delegate tasks, receive status and report back without requiring a human terminal viewer.
- Relevant environment: External interactive agents (`claude`, `pi`, Codex etc.), local shell processes, operating-system terminal lifecycle, other machines, user/agent clients and status protocol.
- Standard-distribution boundary: `crates/herdr-core` binary/server/API; shipped `hc --skill` manual, configurable Markdown role templates, agent readiness and OSC 7501 reporting, child terminal notes and `wait`/`send`/`read`/`run`. External installed model agents and user-supplied role templates are not first-party autonomous decision owners.
- Credited operating / distribution surfaces: [README](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/README.md), [CLI](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/cli.rs), [templates](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/templates.rs), [agent guide](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/SKILL.md), [parent/child notes](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/notes.rs), [status](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/status.rs), [security](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/docs/security.md).
- Adjacent first-party surfaces excluded from ownership: User-installed external agent/model executable, its system prompt/secret/model/provider, dynamically supplied role template file, prompt interpretation, external agent decisions, agent-specific status emitted over OSC, repo CI and developer/release governance.
- First-party operating / deployment modes considered: `hc run` for ordinary programs or an installed agent executable, `hc run <template> <task>`, headless persistence, structured `send`/`wait` parent-child handoff, remote machines, recovery shell and status/blocked gating; supplied reviewer template is an illustrative user-created file rather than a built-in independent reviewer.
- Recursion level: One `hc` process/control runtime hosting zero or more externally owned agent processes; no first-party cognitive S1 is resident.
- Reviewed revision: `b63ecbd1e6b6a7d63fb7bcf40f268930417723ba`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `hc` CLI starts processes in persistent pseudo-terminals, gives them stable addresses, transports messages, and exposes `get`, `events`, `read`, `wait`, `send`, `interrupt`, files and multi-machine control. The terminal process explicitly reports its own status using OSC 7501; Core stores it and does not infer cognitive states from screen text or agent brand. A user may supply a Markdown template containing an executable like `pi` and a review prompt; first-party code composes that user-authored template and task into the initial terminal input when readiness is observed. Parent processes receive typed notes from child terminals and are instructed by the shipped manual to choose follow-up behaviour. Nothing in the first-party Rust runtime itself chooses semantic task actions or reviews code. [templates.md](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/docs/templates.md), [README](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/README.md), [api.rs](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/api.rs).

## Operational model

An external client/agent or human chooses a command, optional task and template. Core runs it, waits for readiness, sends the first message and records later program-reported status and parent-child events. Any model-driven execution/coordination is performed by the separately installed agent runtime using `hc` as its execution/communication tool. Removing the external model agents and user templates leaves a powerful terminal process manager, but no first-party open-ended agent loop; following the Index autonomous-operational S1 inclusion gate, this is a proposed **exclusion**.

## S1 — Operations

- State: —
- Function: Generic terminal/program run support and agent session lifecycle, not owned autonomous coding/review operations.
- Disturbance / variety regulated: Process start/readiness, CLI failures, terminal persistence, program status and host/remote transport.
- Decisive decision or feedback right: Select task-specific code, tool calls or investigations after interpreting the user objective and command feedback.
- Decision owner: Externally installed `claude`, `pi`, Codex or other model program; `hc` stores/processes its I/O but cannot make the substantive choice.
- Supporting / enforcement mechanisms: Pseudo-terminals and holders, `terminal.run`, user-supplied templates, first-message readiness, OSC 7501 status, send/wait/report manual.
- Closure path: Human or external parent chooses a task → `hc run` starts the external program → model/tool observations and subsequent decisions occur in that executable → hc relays output/status to caller.
- Boundary reachability: First-party launch is standard and functional; the autonomous decision loop is only reachable after configuring/starting a separate agent command (not distributed or implemented here).
- Why this is / is not agent-owned: A ready terminal and first-party prompt forwarding are a constructor for a possible external S1, not a first-party S1=A whose decisive task-action right belongs to Core.
- Evidence: [templates.rs](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/templates.rs), [docs/templates.md](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/docs/templates.md), [skill manual](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/SKILL.md).
- Basis: structural negative ownership review
- Confidence: high within first-party Rust boundary.
- Caveats: Constructor potential (`C` in a wider composed system) is not denied; it does not satisfy canonical autonomous S1 admission in this repository.

### Absence scope

- Surfaces inspected: CLI/API, template parsing, first-message dispatch, agent readiness/input, status handling, Rust runtime and bundled skill manual.
- Plausible first-party paths checked: Direct interactive agent run, reviewer template example, arbitrary command execution, skills for delegation and automatic keep recovery.
- Why no material first-party path remains: Each semantic task decision happens in a separately installed agent program; Core handles transport/session mechanics only.

## S2 — Coordination

- State: —
- Function: Terminal and message routing between independent programs, without a demonstrated autonomous cross-S1 disturbance-regulating judgment owned by Core.
- Disturbance / variety regulated: Concurrent parent/child agents need message delivery and not losing signals during process transitions; terminal input itself is serialized.
- Distinct S1 units: Externally supplied coding-agent programs in separate terminal sessions; they are not Core-native decision owners.
- Inter-S1 disturbance: Late messages, blocked child agents, parent-child notification races and typing input while another command is pasting.
- Attenuating coordination relation: Per-terminal input queue, readiness gating, typed child notes and blocked-send refusal can reduce message injection hazards.
- Feedback into subsequent S1 behaviour: External parent agent receives notes/status and independently decides what to send next; Core cannot determine semantic conflict among child tasks or repair it.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The implemented relation protects terminal input, not an explicitly mapped inter-S1 workload collision with a first-party decision-and-correction loop. It remains generic coordination infrastructure.
- Decisive decision or feedback right: Decide whether and how to rebalance/repair colliding operational agents.
- Decision owner: External parent agent or human, operating Core's communications API.
- Supporting / enforcement mechanisms: `send`, `wait --children`, parent notes, OSC status, input queue, user-owned terminal names and refusal on blocked status.
- Closure path: Child reports or status change → Core relays note to parent → external agent/human chooses new assignment or intervention → Core delivers typed message.
- Boundary reachability: Message/parent-child mechanisms are standard; no first-party autonomous S2 policy exercises the resulting external semantic choice.
- Why this is / is not agent-owned: Primitive inter-agent communication and input serialization do not by themselves own interference-specific S2 control.
- Evidence: [notes.rs](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/notes.rs), [input.rs](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/input.rs), [SKILL.md](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/SKILL.md).
- Basis: structural negative review
- Confidence: medium-high.
- Caveats: A higher-level harness such as Dori can provide S2-specific scheduling using this substrate; that autonomy does not transfer to herdr-core.

### Absence scope

- Surfaces inspected: Parent-child notes, send/interrupt/keys, status/blocked handling, input arbitration and wait replies.
- Plausible first-party paths checked: Parent-child agent collaboration, templates for reviewer/subagents, per-terminal input contention and automatic user input queuing.
- Why no material first-party path remains: These regulate message integrity and report state; external agents must interpret and correct actual inter-S1 operating disturbances.

## S3 — Inside-and-now control

- State: —
- Function: No agent-owned whole-current manager of several operating commitments in the Core runtime.
- Disturbance / variety regulated: Users may have many active/blocked remote terminals and children, but Core monitors process health rather than task allocation priorities.
- Decisive decision or feedback right: Choose task assignment, resource trade-offs, rebriefing and admission/closure across active agent units.
- Decision owner: Human or external parent agent interpreting `ls`/`get`/child messages; Rust runtime enforces process control.
- Supporting / enforcement mechanisms: `hc ls`, `get`, `events`, `wait --children`, terminal labels, machine mapping, run/kill and state persistence.
- Closure path: Core status → external manager decides → CLI starts/stops/steers a terminal → Core reports next status; not first-party autonomous S3 closure.
- Why this is / is not agent-owned: Viewing all terminals or killing one is a control surface, not a Core-owned task-management decision process.
- Evidence: [CLI](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/cli.rs), [notes.rs](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/notes.rs), [SKILL.md](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/SKILL.md).
- Basis: structural
- Confidence: high at Core recursion.
- Caveats: Higher-level agent harnesses can implement their own S3 using `hc` and should be assessed at their boundary.

### Absence scope

- Surfaces inspected: `get`/`ls`/`events`, run/terminate, child grouping, machine management and CLI skill guidance.
- Plausible first-party paths checked: Process-wide terminal list, waiting for all children, shell keep recovery and remote-machine controls.
- Why no material first-party path remains: None chooses semantic whole-current commitments or returns corrective work reassignment without an external decision maker.

## S3* — Complementary audit

- State: —
- Claim being audited: A worker's externally claimed task or code change is correct.
- Ordinary reporting path: External agent emits terminal output/status or a child `hc send` note; Core stores/forwards them.
- Complementary access path: User may install a `reviewer.md` template, but the example is not bundled as an executed auditor or linked to a corrective merge/admission gate.
- Independence boundary: Any separate reviewer would be a separately installed model program and configured role; Core supplies terminal isolation but not independent evidence acquisition or judgement.
- Who acts on findings: External parent agent/human, if they voluntarily run a review and interpret its text.
- Function: No first-party complementary audit with independent check and enforced return to correcting operational action.
- Disturbance / variety regulated: Unverified claims can be observed in terminal messages; Core does not independently test their truth.
- Decisive decision or feedback right: Judge actual task evidence against worker claims and require correction.
- Decision owner: Outside reviewer model/human chosen by client, not the first-party terminal runtime.
- Supporting / enforcement mechanisms: Example reviewer template, terminal text/read, child notes and optional blocked state.
- Closure path: Optional reviewer external model output → Core relays message → external manager may decide remediation; no core-owned audit verdict/return gate.
- Boundary reachability: Template parser can run arbitrary user review agents, but no fixed first-party independent review path is automatically exercised in normal use.
- Why this is / is not agent-owned: A sample role template and generic status relay cannot establish audited independence or independent first-party audit closure.
- Evidence: [docs/templates.md](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/docs/templates.md), [templates.rs](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/templates.rs), [notes.rs](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/notes.rs).
- Basis: negative structural review
- Confidence: high.
- Caveats: External agents may conduct excellent reviews; they are not Core's first-party audit decision owner.

### Absence scope

- Surfaces inspected: Template parser/first-message submission, reviewer example documentation, program status, child-parent notification, headless terminal lifecycle and CLI command references.
- Plausible first-party paths checked: User-written reviewer role, parent-led independent second agent, terminal isolation, per-program statuses and typed child report notes.
- Why no material first-party path remains: No shipped first-party review decision actor is invoked as a standard obligation, and no independent reviewer verdict is connected to an enforced remediation or admission gate; external users and agent models must compose the review themselves.

## S4 — Outside-and-then intelligence

- State: —
- Function: No environmental scanning and strategic option selection returning to present capabilities.
- Disturbance / variety regulated: Remote machine availability and lost process recovery are immediate terminal lifecycle events, not strategic outside futures.
- Decisive decision or feedback right: Anticipate external changes and choose durable organization capability adaptation.
- Decision owner: User and external applications, not Core.
- Supporting / enforcement mechanisms: Machine list, SSH connectivity/reconnect, keep recovery, explicit `hc update`.
- Closure path: Loss → deterministic restart shell/reconnect/status; no forecast-to-adaptation option loop.
- Why this is / is not agent-owned: Operational recovery and updater are deterministic process utilities.
- Evidence: [README](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/README.md), [security](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/docs/security.md), [machine](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/machines.rs).
- Basis: structural
- Confidence: high.
- Caveats: External agents may read future-facing data through Core file/network tools, which does not itself assign S4 to the runtime.

### Absence scope

- Surfaces inspected: machine/reconnect, keep/recovery, status, remote file operations, updater and user-facing agent manual.
- Plausible first-party paths checked: Cross-machine state, update checks, process monitoring and lost program restart.
- Why no material first-party path remains: All are present-state management, lacking an external-prospective strategy decision and return to organizational capability.

## S5 — Policy and identity

- State: —
- Function: No closed ultimate-policy/organizational-identity judgment or binding revision of agent operating rights.
- Disturbance / variety regulated: Broad account-level access and risky agent commands are user-trust and OS permission concerns.
- Decisive decision or feedback right: Determine mission, resolve identity/policy conflicts and return binding policy changes into the operational hierarchy.
- Decision owner: User/OS account and external agent platform, not Core.
- Supporting / enforcement mechanisms: Local socket ownership, Windows pipe ACL/integrity, SSH transport, explicit blocked status refusal, no automatic sandbox or permission broker.
- Closure path: OS/user permission config and external agent policies govern command availability; Core executes them without ultimate policy arbitration.
- Why this is / is not agent-owned: Static local trust boundary and release/update process are not an S5 model/human governance return implemented in the runtime.
- Evidence: [security.md](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/docs/security.md), [SKILL.md](https://github.com/herdrdev/herdr-core/blob/b63ecbd1e6b6a7d63fb7bcf40f268930417723ba/crates/herdr-core/src/SKILL.md).
- Basis: explicit + structural
- Confidence: high.
- Caveats: Local privilege risks are real and important, but no S5 autonomy should be inferred from basic security properties.

### Absence scope

- Surfaces inspected: Security/trust documentation, socket/pipe access, remote machine trust, agent-blocked sends, updater and CLI permissions.
- Plausible first-party paths checked: Blocked status, account ACL, isolation sessions, reviewer permission, signed release and installation scripts.
- Why no material first-party path remains: None gives Core a legitimacy-bearing ultimate-policy owner with a returned policy decision.

## Distributed OSS parent arrangement

Public maintainers develop herdr-core and users control their OS accounts. No distributed OSS parent decision process is part of the shipped terminal runtime. Parent-child terminal relationships are process ancestry, not VSM parent S3/S4/S5 governance.

## Self-hosted and non-human modes

Self-hosted and cross-machine Core modes run entirely without a human viewer once a command is supplied. Autonomous model decisions still come from separately installed programs; running headless does not make Core itself agentic.

## Recursion

Multiple child terminals are independently running programs. An external agent in a terminal may be an S1 of a *composed* higher-level harness, while Core remains a shared substrate. Process ancestry and status notes alone do not construct viable S1/S3/S5 recursion at the Core boundary.

## Variety and escalation

Stable terminal addresses, state persistence, parent-child notification and remote transport expose/attenuate process variety. Agent status is program-reported and Core avoids guessing from screens; blocked needs human/external intervention, and `keep` restores a shell rather than rerunning a lost task. These are lifecycle safeguards with no first-party semantic work or governance decision.

## Evidence gaps

Source-pinned inspection; local environment lacks Rust/Cargo/Zig, so no source test suite was executed. User-supplied templates and external model providers were not launched; their quality and autonomy are outside this first-party review. Negative evidence is bounded to supplied Rust CLI/runtime/docs, not claims about all integrations built on hc.

## Verdict

**Propose exclusion (`excluded-no-agentic-vsm`).** Herdr-core is an OSS terminal and inter-agent communication substrate explicitly designed for external autonomous coding tools, but does not own a first-party autonomous operational S1. Optional user-authored agent templates, `hc --skill`, event/status routing and child-process hierarchy do not transfer an external model's decisive rights into this Core runtime. Canonical publication should preserve this assessment with six absent autonomy states and no catalog/signature entry.
