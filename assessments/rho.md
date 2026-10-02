---
harness_id: rho
project_name: rho
repository: https://github.com/crustyrustacean/rho-coding-agent
review_ref: 172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# rho

## Review boundary

- System in focus: one first-party rho coding-agent process/session organization at frozen revision `172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c`, including `rho-core`, built-in `rho-tools`, provider/session/context machinery, optional project-local `rho-memory`, first-party extension loading, approval/sandbox/redaction gates and the headless JSON-RPC binary.
- Purpose and identity: perform local repository software-engineering work through one model-backed coding loop while keeping filesystem/shell risk, project instructions, persistence and external-provider use explicitly controlled.
- Relevant environment: user/operator prompts, steering and approvals; target project files and commands; compiler/test results; configured local/remote model endpoints; optional project/user extensions; project context files.
- Standard-distribution boundary: the rho workspace crates and shipped headless binary are inside. External model endpoints, PowerShell/host OS, target-project code, third-party MCP/frontends and the separate `rho-egui` repository are dependencies/clients.
- Credited operating / distribution surfaces: `README.md`; `rho-core/src/agent.rs`; `rho-core/src/builder.rs`; `rho-core/src/prompts/base.md`; `rho-core/src/config.rs`; `rho-tools/src/`; `rho-tools/src/memory.rs`; `rho-memory/`; `rho/src/app.rs`; `rho/src/rpc.rs`; `rho-ext/`; `docs/src/core-concepts/`; `docs/src/extensions.md`.
- Adjacent first-party surfaces excluded from ownership: CI/release hooks and development tests, deprecated/separate frontends, future-work notes and behavior appearing only after the frozen ref.
- First-party operating / deployment modes considered: persisted and ephemeral headless sessions; JSON-RPC prompt/steer/abort/approval methods; local and external model providers; project context-file loading/trust; optional memory; extension loading/reload; session resume/fork/switch surfaces.
- Recursion level: one rho-managed coding session/turn as the operational organization. Conversation branches/cursors, tool calls, extensions, shell processes and provider requests are mechanisms/state/dependencies, not separately autonomous S1 units in the frozen standard runtime.
- Reviewed revision: `172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

rho's core is one iterative model/tool state machine. A user message enters the active session cursor, the selected model produces text or tool calls, approval/policy is applied, permitted tools execute, results are appended to the durable session, and the same model receives the updated conversation until it returns a final response or a runtime limit terminates the turn.

The runtime exposes rich safety and continuity mechanisms: sandboxed files, approval gates, denylisted commands, redaction, retries, context compaction, persisted JSONL sessions, conversation branches/cursors, cancellation and mid-turn steering. These mechanisms regulate one coding actor. The frozen RPC implementation explicitly describes cursor switching as a serial MVP and notes concurrent per-cursor work as future work, so branch/session multiplicity is not promoted to a current multi-S1 organization.

Optional project-local memory is a model-facing CRUD/search knowledge base. The bundled base prompt says rho does not inherently persist memory unless information is stored via the memory tool and directs storage when the user says “remember this”. Memory can preserve design decisions, conventions and debugging discoveries across sessions, but no shipped prospective sensing/adaptation loop chooses organizational changes from future/external distinctions.

Extensions can add tools and hooks from project/user TypeScript files and can be reloaded by an RPC client. At the frozen ref, extension definitions and reload are externally supplied/configured capabilities; the base prompt may suggest authoring an extension for a missing current-task tool, but rho does not independently sense future environmental change and promote a durable adaptation into its organization.

Project context files are a stronger standing-authority path. rho scans root `AGENTS.md`, `.agents.md`, `CLAUDE.md`, `.cursorrules` and `.rho/prompt.md`, asks the user to trust first/changed content by SHA-256, and appends trusted contents to the system prompt. A legitimate project owner can therefore set durable project instructions that return into later coding turns.

## Operational model

A client submits one prompt to the active rho session. The model chooses repository/tool actions, receives execution or denial results and iterates. A client may steer the same in-flight turn, approve/deny/redirect a tool request, abort the current turn, compact context, resume a persisted session or switch the active cursor.

These controls remain single-S1 controls at the selected recursion. No first-party manager operates a population of concurrent model-backed coding S1 units, and no separate built-in reviewer/verifier actor is instantiated by the standard runtime.

## S1 — Operations

- State: A
- Function: perform environment-facing repository software-engineering work by interpreting a task, selecting coding/search/shell/memory actions, observing returned evidence and revising subsequent action.
- Disturbance / variety regulated: heterogeneous project files, incomplete requirements, compiler/test/command output, stale edit hashes, approval denials, sandbox restrictions, provider/transient errors, token-budget pressure and user steering encountered while completing a coding task.
- Decisive decision or feedback right: choose what evidence to inspect, which offered tool/action to invoke, what code/file change to attempt, how to respond to tool/approval/compiler/test outcomes and when to finish.
- Decision owner: the single model-backed rho coding actor in the active session turn.
- Supporting / enforcement mechanisms: tool registry; hashline editing; sandbox root; approval policy/gate; command denylist; secret redaction; untrusted-data framing; retries; context compaction; durable session cursor; cancellation and steering.
- Closure path: user task plus current system/project/session context → model chooses a tool/action → rho authorizes and executes or denies it → result is appended to session state → the same model receives that result and chooses the next action or final response.
- Boundary reachability: ordinary headless/JSON-RPC execution instantiates the first-party loop directly; no adopter-authored orchestration layer is required.
- Why this is / is not agent-owned: removing the model-backed actor while retaining tools, policies, session state and RPC surfaces removes the open-ended task-specific coding judgment.
- Evidence: [`README.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/README.md); [`rho-core/src/agent.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/agent.rs); [`rho-core/src/prompts/base.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/prompts/base.md); [`rho/src/rpc.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho/src/rpc.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference and host commands remain dependencies; S1 credit is for rho's first-party model/tool feedback composition.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: no standard population of independently executing model-backed coding S1 units exists inside one frozen rho organization, so no inter-S1 interference disturbance is operationalized.
- Distinct S1 units: not established. Conversation cursors/branches are persisted alternative session histories; the RPC implementation is serial and identifies concurrent per-cursor work as future work.
- Inter-S1 disturbance: not established for the frozen standard distribution.
- Attenuating coordination relation: not established.
- Feedback into subsequent S1 behaviour: not applicable.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: session branches, tool batches, observer fan-out and extension threads provide state/execution machinery but do not coordinate distinct autonomous operational units.
- Decisive decision or feedback right: none established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sequential tool execution; session/cursor persistence; cancellation; sandbox/file edit hash checks; extension isolates.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation relation → changed subsequent S1 behavior loop exists.
- Why this is / is not agent-owned: rho's model manages its own turn only; there is no first-party coordinator over multiple operational S1 cells.
- Evidence: [`rho-core/src/agent.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/agent.rs); [`rho/src/rpc.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho/src/rpc.rs); [`docs/src/core-concepts/agent-loop.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/docs/src/core-concepts/agent-loop.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: separate rho processes can be launched externally, but the repository does not package them into one coordinated organization at this boundary.

### Absence scope

- Surfaces inspected: agent loop/tool batches; session cursors/branches; RPC branch switching; extensions/observer fan-out; sandbox/edit safety; cancellation/steering.
- Plausible first-party paths checked: multiple cursors as S1 units; extension worker threads; parallel tool execution; external multiple rho processes; session branching as delegation.
- Why no material first-party path remains: the active runtime executes one model-backed turn/cursor at a time, tool/extension concurrency is mechanism-level, and concurrent per-cursor model work is explicitly not the current implementation.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-control function distinct from the single operational S1 was established.
- Disturbance / variety regulated: current tool approvals, steering, abort, token/iteration limits, session branching and phase tracking regulate one coding turn rather than a population of current S1 commitments/resources.
- Whole-system current view: no view over multiple active operational S1 units exists because only one active coding S1 is instantiated in the frozen standard runtime.
- Current-control decision scope: user approval/redirect/abort/steering can affect the active S1, but do not allocate or intervene across multiple current operational commitments.
- Decisive decision or feedback right: none established at S3 level.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: RPC approvalResponse, steer and abort; cancellation token; session phase tracking; iteration/retry budgets; cursor resume/switch.
- Closure path: not applicable; current intervention exists only within the same S1 loop, not as a whole-system S3 relation.
- Boundary reachability: all listed controls are first-party, but their existence does not change the recursion/function mapping.
- Why this is / is not agent-owned: self-management and human steering of one operational unit are not the distinct inside-and-now metasystem function.
- Evidence: [`rho-core/src/agent.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/agent.rs); [`rho/src/rpc.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho/src/rpc.rs); [`docs/src/core-concepts/approval-policy.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/docs/src/core-concepts/approval-policy.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: approval redirect is a meaningful human feedback path into S1, but the Methodology does not promote ordinary S1 steering/approval into S3 without whole-system current-control scope.

### Absence scope

- Surfaces inspected: approval gate/policy; RPC steering/abort; active cursor management; phase tracking; iteration/retry limits; session statistics/listing; extension observer events.
- Plausible first-party paths checked: human approval as parent S3; mid-turn steering; abort; branch switching; session list as whole-system view; phase tracking as manager state.
- Why no material first-party path remains: each control changes or selects the single coding S1/session rather than regulating a set of current operational units/commitments at a higher recursion.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit role with sufficiently independent access/judgment and corrective return was established.
- Disturbance / variety regulated: rho strongly encourages compile/test verification and records tool results, but the same coding model chooses, observes and interprets those checks.
- Claim being audited: implementation correctness/safety would be the relevant claim, but no separate audit actor/path is packaged.
- Ordinary reporting path: the implementing S1 runs cargo/compiler/test/file tools and receives those results in its own conversation.
- Complementary access path: none established. Extensions may observe/intercept tool calls at the Rust observer level, but standard TypeScript extension hooks at the frozen ref are notification-only for tool-call return values and do not instantiate an independent semantic code reviewer.
- Independence boundary: not established.
- Who acts on findings: not applicable; no independent audit finding path exists.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: compiler/test tools; system-prompt verification guidance; approval gate; observers/extensions; structured tool-result records.
- Closure path: not applicable; there is no distinct audit judgment → corrective-control return loop.
- Boundary reachability: ordinary rho can self-test, but no shipped reviewer/verifier actor must or can independently challenge implementation through a separate context.
- Why this is / is not agent-owned: deterministic checks and self-verification improve reliability but remain evidence inside the implementing S1.
- Evidence: [`rho-core/src/prompts/base.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/prompts/base.md); [`rho-core/src/agent.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/agent.rs); [`docs/src/extensions.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/docs/src/extensions.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a consumer embedding rho-core could provide a custom observer or external review process, but that does not establish a standard-distribution S3* closure.

### Absence scope

- Surfaces inspected: cargo/compiler/test guidance; tool-result loop; approval gate; AgentObserver/interception; TypeScript extension hooks; session branches; memory.
- Plausible first-party paths checked: compiler/test tools as auditor; human approval as audit; extension hooks as independent reviewer; separate cursor as reviewer; memory as review evidence.
- Why no material first-party path remains: no standard separate model-backed reviewer/judge is instantiated, and located safety/check mechanisms either gate actions or return evidence to the same implementing S1.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then loop was established that senses external/future-relevant change, develops adaptation options and returns a selected durable organizational adaptation into current capability/control.
- Disturbance / variety regulated: persistent memory, context compaction, provider/model selection and extensions can preserve information or change available tools, but no shipped loop interprets prospective environmental change and autonomously redesigns rho's future capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: optional `memory` CRUD/search tool; persisted sessions; compaction; provider/config selection; extension authoring/loading/reload.
- Closure path: not applicable; no external/future distinction → adaptation option → persistent organizational capability/strategy change → return into current operation loop is supplied.
- Why this is / is not agent-owned: the memory prompt primarily reacts to explicit “remember this” and current-task discoveries; extensions are project/user files whose activation requires external reload/configuration. Persistence and configurable capability are not by themselves S4.
- Evidence: [`rho-tools/src/memory.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-tools/src/memory.rs); [`rho-core/src/prompts/base.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/prompts/base.md); [`docs/src/extensions.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/docs/src/extensions.md); [`docs/src/configuration.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/docs/src/configuration.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: rho can be manually extended and can retain cross-session knowledge, but those mechanisms lack the prospective environmental sensing/selection closure required for S4.

### Absence scope

- Surfaces inspected: project-local memory store/search/update/delete/list; session persistence/resume; context compaction; provider/model switching; project/user extensions; extension reload; system-prompt extension fragments.
- Plausible first-party paths checked: memory as organizational learning; agent-authored extension as adaptation; hot reload as capability evolution; provider/model switch as strategy; persisted branch history as future intelligence.
- Why no material first-party path remains: these are current-task persistence or externally selected configuration/capability surfaces. No frozen first-party control loop owns a prospective environmental distinction and feeds an adaptation choice back into rho's organization.

## S5 — Identity / ultimate policy

- State: P
- Function: apply legitimate project-owner standing instructions as durable project policy governing later rho coding behavior.
- Disturbance / variety regulated: later sessions may otherwise diverge from project architecture, conventions, safety expectations, testing rules or other durable owner constraints.
- Identity / ultimate-policy issue: what repository-level standing instructions and authorization should govern rho when working in the selected project.
- Ultimate authority in each claimed mode: Parent (`P`) — the legitimate project owner/editor supplies project context files and confirms trust when content is first seen or changed. No first-party autonomous S5 authoring/legitimation mode is established.
- Return-to-operation path: rho scans configured project context files, requires user trust tied to their SHA-256 content, and appends trusted files to the system prompt after the base prompt; later coding decisions are made under that returned standing project authority.
- Decisive decision or feedback right: decide the semantic content of the project's durable instruction layer and whether a changed version should be trusted/applied.
- Decision owner: the human/project owner at the parent recursion.
- Supporting / enforcement mechanisms: default scan list for `AGENTS.md`, `.agents.md`, `CLAUDE.md`, `.cursorrules`, `.rho/prompt.md`; trusted-project SHA-256 store; project-level config; prompt composition.
- Closure path: project-policy issue → owner edits standing context file and confirms/reconfirms trust → rho loads the trusted revision into the composed system prompt → subsequent S1 operation follows that standing project instruction layer.
- Boundary reachability: project-context scanning/trust and prompt composition are standard first-party behavior in the headless runtime; no separate frontend is required.
- Why this is / is not agent-owned: ordinary coding tools could technically edit project files, but rho does not package an autonomous self-policy legitimation loop; trust/authority for changed project instruction content remains explicitly user-owned.
- Evidence: [`README.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/README.md); [`docs/src/core-concepts/project-context-files.md`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/docs/src/core-concepts/project-context-files.md); [`rho-core/src/config.rs`](https://github.com/crustyrustacean/rho-coding-agent/blob/172700e7dbfd6b11dc3b86177e2927cd1eeb4d1c/rho-core/src/config.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is project-recursion S5, not ownership of rho's product-level safety policy, provider configuration or external client behavior.

## Distributed OSS parent arrangement

The rho repository's maintainers govern rho itself outside the selected local coding-session recursion. The S5 parent credited here is narrower: the legitimate target-project owner whose trusted standing context files are injected into rho's runtime system prompt.

## Self-hosted and non-human modes

rho can execute S1 without continuous human decisions only to the extent allowed by configured approval policy; default write/shell behavior often requests approval. Those approval decisions remain S1 gating rather than a separate S3 function. S5 remains explicitly human/project-owner governed through trusted context-file authority.

## Recursion

At the selected recursion there is one model-backed operational S1. Sessions/cursors, extension isolates, provider requests and tools are supporting mechanisms rather than additional operational units. Without multiple S1s, S2/S3 are not established; without an independent reviewer, S3* is not established. Project-owner context authority supplies S5 at the parent recursion.

## Variety and escalation

Coding variety is absorbed by the model/tool S1. Tool risk can escalate to human approval/redirect; steering can alter the current S1 turn; cancellation terminates it. Cross-session memory can preserve useful facts, and project context can carry standing owner policy. None of these creates S2/S3/S3*/S4 at the selected recursion.

## Evidence gaps

No reviewed evidence gap requires `?`. The frozen repository exposes the agent loop, approval/steering model, context-file trust, memory and extension boundaries sufficiently to classify the absent metasystem functions directly.

## Assessment summary

rho closes autonomous coding S1 through its first-party model/tool loop. It does not package multiple operational S1s, whole-system current control, or an independent complementary reviewer, so S2/S3/S3* remain absent. Memory, sessions and extension mechanisms persist or change current-task capability but do not close a prospective outside-and-then S4 loop. Project-level standing policy remains parent-owned through hash-trusted project context files that rho injects into later system prompts.

Proposed vector: **`A · — · — · — · — · P`**.
