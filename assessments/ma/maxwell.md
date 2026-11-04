---
harness_id: maxwell
project_name: Maxwell
repository: https://github.com/AshyIsMe/maxwell
review_ref: 9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Maxwell

## Review boundary

- System in focus: The shipped local Common Lisp coding-agent runtime, including named concurrently running conversations and the operator's `/chat` control plane.
- Purpose and identity: Carry out user-directed programming tasks through a persistent interactive Lisp workspace, with separately addressable task conversations and restartable session memory.
- Relevant environment: User requests, local source tree, live Lisp process and files, model-provider responses, concurrent conversation activity, persisted sessions and memory summaries.
- Standard-distribution boundary: First-party SBCL runtime and terminal interface, one model-call/tool loop per conversation, background worker threads, inboxes and resume/checkpoint functions; user provides model credentials and workspace.
- Credited operating / distribution surfaces: [README](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/README.md), [`src/runtime.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/runtime.lisp), [`src/agent.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/agent.lisp), [`src/conversations.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/conversations.lisp), [`src/threads.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/threads.lisp), [`src/compactor.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/compactor.lisp).
- Adjacent first-party surfaces excluded from ownership: Developer test runners and PTY fixtures, repository CI and maintainers, external LLM provider, operating-system permissions, hypothetical loaded Lisp roles/policies not shipped as an organizational control function.
- First-party operating / deployment modes considered: Interactive single `main` agent; optional multiple named live conversations with human operator delegation, note/wake and stop; local persistent image and verified restart; non-interactive prompt/ephemeral modes.
- Recursion level: One user's Maxwell process as a small multi-conversation task system; its distinct S1 conversations are separate task cells but share Lisp definitions, filesystem and process privileges.
- Reviewed revision: `9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Maxwell is an SBCL coding-agent executable with a single `COMMON_LISP` tool: each model-selected form is evaluated in a live Lisp image, returning observations to subsequent requests. `src/agent.lisp` creates model/tool turns, supports steering while running and appends tool outcomes to a private chat. A binary-tree compactor summarizes historical messages and `zoom` retrieves their details. `src/conversations.lisp` adds independently named chats, copied model-client configurations, per-conversation workers, attributed inbox notes, `report-to` results and an explicit wake flag. The terminal exposes `/chat` list, select, create, fork, run, note, ask and stop; `/model` and `/effort` operate on the selected conversation. Conversation registry and chat contents survive tested checkpoints and verified restart. Threads and chat locks protect runtime integrity; all workers share code and files, with an explicit README warning against concurrent self-modification. [README named conversations](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/README.md), [conversation implementation](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/conversations.lisp), [restart test](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/tests/conversations-pty.py).

## Operational model

Each conversation's model selects Lisp code and task replies, and reacts to execution and user-steering feedback (S1). A parent conversation can autonomously start a child, request a result or deliver an attributed note, but the runtime deliberately does not supply isolation, team roles or conflict policy. In the shipped multi-conversation interactive mode a human operator can see all task cells, inspect their transcripts, change assignments/model settings and stop a current worker; this provides a narrowly scoped parent-owned current-control mode (S3 P), not automatic agent-led supervision. Restart/compaction preserve context; they are not independent strategy or audit.

## S1 — Operations

- State: A
- Function: Execute a coding task through model-selected Common Lisp evaluations and observed feedback.
- Disturbance / variety regulated: Unknown source state, compilation/evaluation results, user corrections, provider failures and growing chat context.
- Decisive decision or feedback right: Choose which Lisp forms to evaluate, which findings to act on and what task answer to return after tool responses.
- Decision owner: The model-bearing agent associated with each active conversation; host Lisp evaluates the instructions.
- Supporting / enforcement mechanisms: `COMMON_LISP` tool schema, live SBCL workspace, conversation-local history, steering, provider transport, binary memory compaction.
- Closure path: User or delegated task → model-produced Lisp expression → evaluated result and error/output → model's next tool or response; subsequent turns retain accessible conversation memory.
- Boundary reachability: Both the terminal `main` session and `start-conversation` call the shipped `start-turn` agent loop; no external orchestrator is necessary to invoke the operational cell.
- Why this is / is not agent-owned: The model chooses substantive code and actions; provider transport, locks and user input constrain but do not make those choices.
- Evidence: [`src/runtime.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/runtime.lisp), [`src/agent.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/agent.lisp), [`src/conversations.lisp#L113-L140`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/conversations.lisp#L113-L140).
- Basis: explicit + structural
- Confidence: high for first-party loop ownership.
- Caveats: No external model quality or actual-task success guarantee follows from the implementation.

## S2 — Coordination

- State: —
- Function: No shipped inter-S1 interference regulator beyond message transport and deterministic runtime thread safety.
- Disturbance / variety regulated: Concurrent conversations can modify the same files or Lisp definitions and interfere with one another.
- Decisive decision or feedback right: Detect an inter-conversation collision, settle competing claims and feed a coordinated change back into affected workers; no such first-party right is provided.
- Decision owner: Individual models may pass messages or ask for results; user can intervene; locks serialize internal data mutation without resolving shared-workspace conflicts.
- Supporting / enforcement mechanisms: Inbox note IDs, per-conversation workers, worker/chat locks, result reporting and explicit README concurrency warning.
- Closure path: Messages arrive on the next turn and child completion returns a note, but the runtime has no identified conflict signal → cross-unit arbitration → corrective coordination loop.
- Why this is / is not agent-owned: Delegation, notes, a shared process and thread mutexes are not an S2-specific interference attenuator.
- Evidence: [`src/conversations.lisp#L90-L157`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/conversations.lisp#L90-L157), [`src/threads.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/threads.lisp), [README named conversations](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/README.md).
- Basis: explicit + structural
- Confidence: medium-high within the shipped process.
- Caveats: User-authored Lisp coordination may be possible but is not an installed S2 function.

### Absence scope

- Surfaces inspected: Conversation create/start/send/stop/service, worker locks, shared filesystem documentation, tests and CLI.
- Plausible first-party paths checked: Attributed notes, non-waking results, wake requests, background completion and shared-lock protections.
- Why no material first-party path remains: None detects and adjudicates the stated cross-cell workspace/definition interference and returns a regulating decision to the involved cells; the distribution instead warns the user to isolate worktrees.

## S3 — Inside-and-now control

- State: P
- Function: Human-owned oversight of the active portfolio of named Maxwell conversations in interactive multi-conversation mode.
- Disturbance / variety regulated: Which child task is currently running, the worker state and backlog, divergent work priorities, overactive or stalled conversations, model/effort selection.
- Decisive decision or feedback right: Inspect the live conversation roster and transcript, start/delegate/stop a worker, select a conversation or change its model/effort; these commands alter its subsequent current operation.
- Decision owner: Human terminal operator, not a self-governing supervisory model or merely the worker scheduler.
- Supporting / enforcement mechanisms: `/chat` status display with ID/name/state/model/pending count, selectable per-conversation transcripts, `/chat run`, `/chat stop`, per-conversation model/effort, background result notes.
- Closure path: All-conversation status listing and transcript inspection → operator's current-task allocation/intervention → `start-conversation`/`stop-conversation` or configuration command → changed running cell state and later status/result for renewed inspection.
- Boundary reachability: Shipped interactive CLI calls `conversation-command`/`service-conversations`; `README` documents human use and the PTY integration test exercises status, switching, delegation and restart. This is a supported parent mode at the local Maxwell process recursion.
- Whole-system current view: `/chat` lists the entire active local conversation registry, task work states and pending inbox counts, while selection exposes each cell's transcript for investigation of current commitments.
- Current-control decision scope: The operator can prioritize and assign a new worker task, stop an existing worker, inspect results and change a worker's active model/effort, returning those choices directly into the runtime; no automatic portfolio optimizer is claimed.
- Why this is / is not agent-owned: The supervisory current-control selection is explicitly made by the user. Individual models can delegate, but no agent receives and arbitrates a whole-current system roster with that authoritative right.
- Evidence: [`src/conversations.lisp#L147-L207`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/conversations.lisp#L147-L207), [README named conversations](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/README.md), [`tests/conversations-pty.py`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/tests/conversations-pty.py).
- Basis: explicit + structural
- Confidence: medium; bounded to the human-operated multi-conversation process, not an autonomous organizational controller.
- Caveats: The roster is operationally shallow and control remains manual. This is not an S3 claim in single-conversation/one-shot mode and does not imply resource scheduling or automatic conflict mediation.

## S3* — Complementary audit

- State: —
- Function: No independent, complementary operational audit judgment returned to current control.
- Disturbance / variety regulated: Incorrect model claims and code outcomes could be inspected by another chat or tests, but neither is an installed independent auditor.
- Decisive decision or feedback right: Obtain direct operational evidence separately from ordinary reporting, challenge it and return a binding corrective judgment; not supplied.
- Decision owner: User may open another conversation or inspect logs, but independent audit rights and mandated correction are not defined.
- Supporting / enforcement mechanisms: Separate chats, snapshots, inspectable transcripts, developer PTY tests, persisted conversation state.
- Closure path: Optional reviewer conversation can send a note, with no required independence boundary, evidence-access contract or audit-to-control correction loop.
- Why this is / is not agent-owned: Context separation and routine testing alone do not establish complementary audit.
- Evidence: [`src/conversations.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/conversations.lisp), [`tests/conversations-pty.py`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/tests/conversations-pty.py), [README](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/README.md).
- Basis: structural
- Confidence: medium-high for the boundary; a user can construct a review role separately.
- Caveats: Separate conversations share execution and files, so private context by itself is not operational independence.

### Absence scope

- Surfaces inspected: Conversation role and result APIs, private context, tests, memory and operator status UI.
- Plausible first-party paths checked: Child review chat, context snapshot, attributed note, direct Lisp inspection and developer verification tests.
- Why no material first-party path remains: Shipped routes can carry optional opinions but supply neither an independent evidence-taking auditor with a defined judgment right nor an obligatory return of findings for S3 correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: No established future-facing environment scan and prospective capability adaptation loop.
- Disturbance / variety regulated: Incoming new user tasks, model/provider choices and context overflow are handled in currently requested work.
- Decisive decision or feedback right: Form adaptation options about the future environment and return a selected strategic change into present capabilities; not found.
- Decision owner: Each coding agent performs ordinary task reasoning; operator selects provider/model; maintainer may change Lisp code externally.
- Supporting / enforcement mechanisms: Context compactor, persistent image, model selection, snapshot conversations and restart verification.
- Closure path: The compactor preserves task memory and restart reloads code/state; neither identifies a prospective environment challenge and returns a strategic option through a governing channel.
- Why this is / is not agent-owned: Long memory, provider switching and task planning support ongoing S1, not S4 adaptive governance.
- Evidence: [`src/compactor.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/compactor.lisp), [`src/runtime.lisp`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/runtime.lisp), [README verified restart](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/README.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: A user can instruct an S1 agent to investigate future technology, but that ad hoc task is not a shipped S4 decision-return institution.

### Absence scope

- Surfaces inspected: Runtime prompt, model/client configuration, compactor, session persistence, restart, conversation fork and README.
- Plausible first-party paths checked: Snapshot branching, model switching, code reload, compaction retention and developer-controlled source changes.
- Why no material first-party path remains: The reviewed functions manage present tasks or session reliability without a distinct prospective environment-to-capability closure owned by the harness.

## S5 — Policy and identity

- State: —
- Function: No identified ultimate-policy or enduring identity decision/return loop in the runtime.
- Disturbance / variety regulated: User instructions, shared-process risks and model execution privileges are set by initial prompt, OS and operator-controlled configuration.
- Decisive decision or feedback right: Resolve an identity-level policy conflict, authorize a binding policy and return it to govern subsequent agent behaviour; no first-party path was identified.
- Decision owner: Operator supplies instructions and credentials; built-in system prompt describes runtime behaviour but does not constitute an S5 adjudication authority.
- Supporting / enforcement mechanisms: Base system prompt, per-conversation copied client settings, terminal operator and OS filesystem permissions.
- Closure path: Local instruction/configuration becomes model input or process settings; no identity-level issue → legitimate policy decision → authoritative return cycle is shipped.
- Why this is / is not agent-owned: A model can alter its live Lisp environment, yet this is task-level programmability, not a separately owned identity/ultimate-policy institution.
- Evidence: [`src/runtime.lisp#L3-L128`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/runtime.lisp#L3-L128), [`src/conversations.lisp#L35-L59`](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/src/conversations.lisp#L35-L59), [README](https://github.com/AshyIsMe/maxwell/blob/9d8a04976d24b0c706fb1c8f8c8b290e5a4e9acc/README.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: User-loaded Lisp can implement organizational rules, but a hypothetical policy extension is outside the delivered mode.

### Absence scope

- Surfaces inspected: System prompt, client/config settings, terminal commands, conversation hierarchy, runtime security notes and resume paths.
- Plausible first-party paths checked: Human system instruction, parent/child metadata, model/effort assignment, stop/restart, OS process authorization.
- Why no material first-party path remains: These afford task initiation, configuration and runtime safety, with no supplied ultimate-policy matter decided by a legitimate S5 owner and returned to alter continuing governance.

## Distributed OSS parent arrangement

Contributors' commits and tests are external maintainer activity. The credited S3 parent is one human operating one Maxwell process and its visible named conversations; this does not confer organization-wide supervisory rights across unrelated OSS user installations.

## Self-hosted and non-human modes

The local executable can run single or multiple conversations using self-selected providers. Multiple autonomous worker conversations do not automatically become an autonomous S3 or S2. The human terminal's specific control commands establish the narrow parent-current-control mode; ephemeral one-shot use has only its operative S1 loop.

## Recursion

Named conversations have stable identities, distinct agents and histories and optional parent pointers, but all share process privileges, Lisp definitions and files. Parent/child nesting and task delegation do not establish recursively viable independent organizations or a conflict arbitration mechanism.

## Variety and escalation

The live Lisp interpreter and persistent memory amplify an agent's action variety; compacted memory attenuates context length, and worker/chat locks protect internal consistency. At the assessed parent level, human `/chat` listing, stopping and retasking allow operational intervention. Automatic restart refuses while conversations are active and interrupted tool calls are not replayed; none of these controls silently acquires S3*, S4 or S5 ownership.

## Evidence gaps

- SBCL was not installed in the assessment environment, so first-party Lisp and PTY integration tests could not be executed here. Source and test design were reviewed at the pinned SHA; no real provider calls were run.
- No integrated cross-conversation conflict policy, independent audit contract, or higher organizational governance should be inferred from the general ability to evaluate arbitrary Lisp.
