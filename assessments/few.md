---
harness_id: few
project_name: Few
repository: https://github.com/moloo4ni/few
review_ref: c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Few

## Review boundary

- System in focus: the first-party Rust Few terminal coding agent with one configured model/tool loop, four native coding tools, deterministic post-edit verification, permissions, sessions and markdown memory.
- Purpose and identity: transform user coding requests into real file edits, command execution and tested deliverables within the active local project.
- Relevant environment: code repository files, shell outputs and tests, local path/command authority, project-specific instructions, session continuity, user/operator and external inference provider.
- Standard-distribution boundary: native Few executable from the frozen Rust repository; user-provided test suites, model provider backends and software maintainer CI are not first-party higher VSM actors.
- Credited operating / distribution surfaces: `src/agent/mod.rs`, `src/agent/exec.rs`, `src/tools.rs`, runtime `src/app.rs`, `src/perms.rs`, `src/agent/verify.rs`, session and memory modules as wired to the product executable.
- Adjacent first-party surfaces excluded from ownership: release CI, external provider live compatibility samples, repository contribution workflow, development scripts, README test claims not routed to runtime, and user-created separate harness configurations not present in the standard binary.
- First-party operating / deployment modes considered: default build coding mode with shell/write asks; auto-approve; nonmutating plan mode; terminal session resume; automatic project-local test verification after changes and bounded retry; memory/context preservation; user-permission intervention.
- Recursion level: installed per-project coding session with a single agent operating S1 cell. Native tools, shell processes, queued human inputs and memory files do not constitute separate autonomous operational units.
- Reviewed revision: `c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Few is a compact first-party Rust coding-agent executable, not a terminal wrapper around an external coding loop. Its native Agent runs an iterative model/tool cycle with four actual code/shell tools (`read`, `write`, `edit`, `shell`), returning file and command observations into the same provider conversation. A project-scoped permission engine controls execution, including sensitive files, shell policy and plan/build/auto mode. Sessions and two markdown memory scopes are persisted locally, and old rounds can be compacted for context continuity.

After the model emits a final text turn following source modification, a configured or autodetected project verifier invokes the ordinary shell execution/approval path. A failed result is appended to the original model's conversation with an instruction to repair before finishing; repeating the same signature to a configured threshold stops with an honest incomplete outcome. This is an implemented useful quality-feedback loop but not, by itself, independent complementary audit S3*: there is no separately owned auditor examining the operations and returning its autonomous judgment. No code path in the standard distribution launches a second decision-making coding agent, so generic tool calls do not establish inter-S1 S2.

The examined project scope excludes separate operating systems of repository maintainers, external model providers and user-specific CI/test owners. Modes and persisted permission grants are local action governance, not a first-party S5 identity authority; markdown memory does not create prospective S4 intelligence.

Pinned primary source anchors: [src/agent/mod.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/mod.rs); [src/agent/exec.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/exec.rs); [src/agent/verify.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/verify.rs); [src/perms.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/perms.rs); [src/tools.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/tools.rs).

## Operational model

One model directs source-transforming operations, and the first-party Rust runtime preserves and returns observations. Deterministic test failures loop into the **same** coding actor for bounded repair. Separate S1 peers, a metasystem current manager, a complementary autonomous auditor, a prospective intelligence actor and ultimate-policy governance do not form material first-party operating paths at the assessed revision.

## S1 — Operations

- State: A
- Function: The native model-directed coding loop edits, inspects and tests the current user project.
- Disturbance / variety regulated: Code/test failures, changing user requirements, unfamiliar files and tool result variability.
- Decisive decision or feedback right: Choose read/write/edit/shell tools, inspect their returns and decide repair/finish.
- Decision owner: A single configured LLM acting inside Few's first-party Rust Agent, with authority bounded by runtime permissions.
- Supporting / enforcement mechanisms: Four native tools, asynchronous model streaming, task history, mode prompts, permission engine, automatic verify feedback.
- Closure path: User request → agent provider reply with native tool calls → Few handlers operate on project files/shell → tool result appended to model conversation → next model action; post-edit verify failure also returns evidence to that same operating loop.
- Boundary reachability: `src/main.rs`/`src/app.rs` construct the packaged executable agent whose `Agent::run` in `src/agent/mod.rs` invokes native tool dispatch in `src/agent/exec.rs`; no third-party coding agent loop is required.
- Why this is / is not agent-owned: The agent chooses contingent coding actions. Human approvals and Rust permission checks enforce rather than choose the detailed operational response.
- Evidence: [src/agent/mod.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/mod.rs); [src/agent/exec.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/exec.rs); [src/tools.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/tools.rs); [src/main.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/main.rs); [src/app.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/app.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Model is a configured external inference provider; live task success rates are not established by structural source evidence..


## S2 — Coordination

- State: —
- Function: No distinct coordination relation among at least two code-producing S1 units exists at the distributed standard Few coding-session boundary.
- Disturbance / variety regulated: The standard run has one decision-making coder. Sequential read/write/edit/shell calls do not create a second autonomous operational work cell whose behavior could oscillate or collide with a peer.
- Decisive decision or feedback right: No inter-S1 collision decision exists. The user's sequential command stream and deterministic tool policy are within single S1 execution.
- Decision owner: Absent in the selected single-agent packaged coding runtime.
- Supporting / enforcement mechanisms: One native tool dispatcher, permission gates, single conversation and user-input queues.
- Closure path: Tools and turn results return to one agent; this is S1 local feedback, not inter-S1 stabilization.
- Why this is / is not agent-owned: Tasks, tools, queued user messages and modes are not distinct independently acting S1 units.
- Evidence: [src/agent/mod.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/mod.rs); [src/agent/exec.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/exec.rs); [src/tools.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/tools.rs); [src/app.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/app.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Separate unrelated Few processes could edit the same workspace, but first-party coordination across those processes is not demonstrated or credited..

### Absence scope

- Surfaces inspected: The sole `Agent::run` loop, tool execution, asynchronous TUI input queue, session recording, permissions and relevant tests.
- Plausible first-party paths checked: Native dispatch versus independently spawned worker/agent loops; file-edit concurrency claims; locks/reservations or negotiation among multiple active operational units.
- Why no material first-party path remains: The shipped standard coding run exposes one model/tool S1; no real second S1 or inter-S1 interference-management/feedback path is implemented.


## S3 — Inside-and-now control

- State: —
- Function: No metasystem controller that observes several active S1 commitments and makes substantive inside-and-now resource/priority decisions.
- Disturbance / variety regulated: Budget steps, verify failures, session interruptions and approvals affect the current single coding task, not the current performance/priority balance of a multi-S1 organization.
- Decisive decision or feedback right: Runtime applies preset step ceilings and repeated-failure stop rules; user grants tool rights and may stop execution.
- Decision owner: Deterministic runtime / human task operator; no distinct first-party agent that owns S3 judgement.
- Supporting / enforcement mechanisms: `TaskOutcome`, `RetryTracker`, `RunCtx::step_limit_reached`, TUI progress/status and saved sessions.
- Closure path: Ceiling stops the task or verify failure returns to the same coder; no independent whole-current regulatory decision flows back to multiple S1 cells.
- Why this is / is not agent-owned: A single agent's retry limit or refusal is local quality/safety enforcement rather than central current-system supervision.
- Evidence: [src/agent/mod.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/mod.rs); [src/agent/verify.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/verify.rs); [src/app.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/app.rs); [src/session.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/session.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: A wider human engineering team can supervise Few, but that external parent is not implemented as a first-party S3 mode..

### Absence scope

- Surfaces inspected: The complete agent loop, task outcome routing, automatic verification, TUI controls, sessions and permission settings.
- Plausible first-party paths checked: Whole-current resource/priority controller, independent managerial decision-maker, multi-task arbitration, operator exception-handling return path.
- Why no material first-party path remains: All recognized stops and approvals act on the single coder/task. They do not constitute a system-level current-control decision and return across operational work cells.


## S3* — Complementary audit

- State: —
- Function: Automatic tests provide task-local checking and repair prompts but no complementary independently owned audit organization of operating S1.
- Disturbance / variety regulated: A coder could leave incorrect edits; independent tests offer evidence of failure but the same model receives them as ordinary task feedback.
- Decisive decision or feedback right: The runtime chooses a configured or autodetected shell command, checks exit status, and sends failure text to the original coding model; it does not give a separate agent/auditor a material independent judgment or audit discretion.
- Decision owner: Deterministic `resolve_verify`, ordinary permission-gated shell test and same S1 coding actor; no independent S3* audit owner.
- Supporting / enforcement mechanisms: Auto `cargo test`, `go test`, `npm test`, `pytest` resolution; error signature and bounded repeated-failure tracker.
- Closure path: Changed files → `finish_text_turn` invokes ordinary shell verification → when it fails, `[few verify]` failure is appended to the **same** model's conversation → same S1 fixes or stops after threshold. This is honest local S1 feedback but lacks complementary independent audit ownership.
- Why this is / is not agent-owned: Verification is not automatically S3*: only the same agent repairs and the deterministic check has no independent audit mandate/organizational autonomy.
- Evidence: [src/agent/mod.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/mod.rs); [src/agent/verify.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/verify.rs); [src/agent/exec.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/exec.rs); [src/perms.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/perms.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: If a user's project supplies strong tests, those can be useful external evaluation evidence but do not make Few itself own an independent complementary audit actor..

### Absence scope

- Surfaces inspected: Verify-plan resolver, shell verifier execution, repair/retry branch, test modules and the TUI single-agent topology.
- Plausible first-party paths checked: Separate reviewer model, independent source-data path, concurrent adversarial audit, independent audit decision authority and binding corrective escalation.
- Why no material first-party path remains: The actual returned test evidence is fed to the original S1 loop under ordinary shell permissions; no separately owned complementary audit organization or decision return is present.


## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party forward-looking environment study and strategic renewal authority beyond local memory, context compaction and task-directed edits.
- Disturbance / variety regulated: Future tooling, market, capability or environment changes would require prospective sensing, alternatives and deliberate organizational adaptation.
- Decisive decision or feedback right: Memory files and context summaries preserve previously seen facts; the user owns project goals/model selection.
- Decision owner: No prospective S4 decision owner in standard shipped runtime.
- Supporting / enforcement mechanisms: Markdown global/project memory, context compaction triggered by token usage, session restore, configuration and plan mode.
- Closure path: Notes and summaries may inform later turns, but do not generate/evaluate future environmental alternatives then enact an organizational capability change.
- Why this is / is not agent-owned: Storing context and preserving sessions is not by itself future intelligence/renewal.
- Evidence: [src/memory.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/memory.rs); [src/agent/compact.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/agent/compact.rs); [src/session.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/session.rs); [src/config.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/config.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: The actual software repository may evolve under human maintainers; its development organization is outside the installed coding-agent recursion..

### Absence scope

- Surfaces inspected: Model context and compaction, memory read/write, sessions/restore, provider configuration and TUI plan mode.
- Plausible first-party paths checked: Environment intelligence loops, autonomous future-capability selection, persistent revised strategy and closure into operational changes.
- Why no material first-party path remains: No prospective adaptation decision channel with a first-party owner and binding future-operation return is exposed by the inspected standard run.


## S5 — Policy and identity

- State: —
- Function: No highest-level mission/identity-purpose decision and policy ratification closure for an autonomous coding organization.
- Disturbance / variety regulated: Tool safety, path trust and auto-approve modes affect current action authority rather than the organization's constitutive policy/identity.
- Decisive decision or feedback right: The user chooses mode and scope and grants/denies individual tool rights; deterministic policy engine enforces.
- Decision owner: Human owner of local preferences, not a first-party S5 governance actor.
- Supporting / enforcement mechanisms: `Mode::Plan|Build|Auto`, capability matrix, sensitive-path deny list, durable user grants.
- Closure path: Human approval → action allowed/denied, or mode changes tool posture; no identity/purpose issue is deliberated and returned as a binding policy decision for the whole system.
- Why this is / is not agent-owned: Capability enforcement or `plan` mode does not establish legitimate ultimate organizational authority.
- Evidence: [src/perms.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/perms.rs); [src/config.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/config.rs); [src/app.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/app.rs); [src/sysprompt.rs](https://github.com/moloo4ni/few/blob/c7dd1b9f6eeec1c4af7e3a0ee7c80132cf2b06be/src/sysprompt.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: The maintainers' software licensing and governance are separate external systems, not shipped end-user coding policy..

### Absence scope

- Surfaces inspected: Permission engine/modes, config, prompting layers, user approvals, sensitive file handling and local project history.
- Plausible first-party paths checked: Ultimate purpose/identity debate, parent ratification, policy evolution, independently authorized policy return across operational cells.
- Why no material first-party path remains: Only task/tool-level human approvals and static constraints are implemented; no ultimate-policy decision role or closure exists at selected recursion.


## Distributed OSS parent arrangement

First-party maintainer workflows and GitHub CI affect the Few software development organization, not installed users' individual coding sessions. An external user organization may supply test cases, operator approvals or instructions but cannot donate its own S3/S3*/S4/S5 to this repository's packaged coding runtime.

## Self-hosted and non-human modes

Few can call different model providers through its own first-party tool cycle. Auto-approve allows actions without repeated human grants, while default interactive mode can require permission for writing/execution. None of these modes changes the single-S1 topology. An external model completes inference but the first-party loop and tool envelopes remain owned by Few.

## Recursion

The system-in-focus is the local coding session. S1 is the autonomous model/tool coder. Its file/shell calls, verification command, permissions and memory are supporting components within that session, not independently viable organizational S1 cells. A wider human team can use Few, but that team's metasystem was not first-party deployed in this revision.

## Variety and escalation

Tool failures return to model decisions; automatic verification failure is observed before a task may honestly conclude, with capped repetition and accurate `GaveUpRepeated` outcome. User permission denials and interrupts constrain actions. The return is useful local task feedback, not proof of independent complementary audit or whole-current management.

## Evidence gaps

- No tested productivity/quality measurement is inferred from example live provider results or structural self-tests.
- Negative higher-function mappings are bounded to the frozen first-party single-agent runtime and documented potential paths above, not a universal claim about arbitrary external multi-agent workflows built around Few.
- Configured verifier quality depends on each user's test suite, which is not evaluated as part of the autonomous organizational owner at this boundary.
