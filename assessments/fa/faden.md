---
harness_id: faden
project_name: faden
repository: https://github.com/nogo/faden
review_ref: e59833d32c775b86c7b35b2ca1b3cd1b042b5886
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# faden

## Review boundary

- System in focus: The embeddable Go `faden.Runner`, its first-party `llama` model/tool loop, durable event/attempt/cursor stores and backend handover; not independent Claude/Codex provider internals or the host app's organizational decisions.
- Purpose and identity: Run one agent turn durably across process restarts and optionally resume a session under another authorized model backend.
- Relevant environment: Host-submitted input, model responses, tool outputs, prior session events, backend availability and interrupted processes.
- Standard-distribution boundary: A host constructs the library with a Store and explicitly configured backends. Standard packages include a native `llama` agent loop that independently selects and executes function/tool calls; `claude` and `codex` are bridge adapters to existing coding agents. One active turn per session and store-based resumption are first-party runtime behavior.
- Credited operating / distribution surfaces: [runner.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/runner.go), [llama/llama.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/llama/llama.go), [llama/tools.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/llama/tools.go), [handover/handover.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/handover/handover.go), [attempt.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/attempt.go), [README.md](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/README.md).
- Adjacent first-party surfaces excluded from ownership: Host apps' scheduling, workspaces, container lifetime, permissions, credentials and higher-level goals; upstream Claude Code/Codex cognition; test fixtures, design notes and comparative survey as operational owners.
- First-party operating / deployment modes considered: Embedded `llama` native tool loop with a host-provided model and Go tool functions; durable single-session turn queue; CLI backend resume; backend handover; JSONL/SQLite/in-memory stores.
- Recursion level: One durable conversation/session task, with backend choices and persistence but no first-party federation of independently managed S1 work units.
- Reviewed revision: `e59833d32c775b86c7b35b2ca1b3cd1b042b5886`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Runner.Open` reads unfinished turns, records the new attempt before retry and resumes in background. It stores all user/model/tool events, restricts a session to one running turn and allows a host to choose which backend receives a new turn. Claude/Codex backends resume native sessions supplemented with a bounded selection of missing events. The first-party `llama.Backend.Run` is a genuine model/tool loop: rebuilds model messages from events, obtains completion, persists assistant tool calls before execution, executes host-provided functions or built-in tools, persists results and repeats until final. Interrupted unsafe tools are not blindly replayed. [runner.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/runner.go), [llama/llama.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/llama/llama.go), [handover/handover.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/handover/handover.go).

## Operational model

A human or host app submits a session, input and named backend; faden stores the request before execution. In native llama mode, the model adaptively chooses configured tools based on feedback, while the Runner and Store provide durable bookkeeping. On crash the system reconstructs the same operational context; on handover the next model gets selected prior events. No first-party agent chooses whole-system priorities, creates policy, independently audits other agents or evaluates an external future for organizational adaptation. [README.md](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/README.md), [runner.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/runner.go).

## S1 — Operations

- State: A
- Function: Execute a user request through a first-party model/tool decision-feedback loop.
- Disturbance / variety regulated: Unknown task steps, returned tool data, model/tool errors and interrupted progress.
- Decisive decision or feedback right: Select tool calls, arguments and next model action after observing outcomes.
- Decision owner: The configured model operating through faden's own `llama.Backend` tool loop (and alternatively existing external agents through adapters, without claiming their internals).
- Supporting / enforcement mechanisms: `Run`/`complete`/`execute`, host-registered Go tools, durable transcript events and replay safety controls.
- Closure path: Host `Submit` → persisted turn → llama completion selects tool → faden records/executes result → model sees returned result and chooses next step or final answer → persisted completion.
- Boundary reachability: `llama` is a shipped first-party package with `New`/`Run`, shown in the documented quick-start and wired through standard `faden.Open` backends; no external coding-agent SDK must furnish the loop.
- Why this is / is not agent-owned: The model selects actions and interprets tool outputs; event persistence, oldest-first queue and crash retry merely keep that operation durable.
- Evidence: [llama/llama.go, `Run` and `execute`](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/llama/llama.go), [llama/tools.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/llama/tools.go), [README.md, quick start](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/README.md).
- Basis: explicit + structural.
- Confidence: high for native shipped loop; no live model server execution in this review.
- Caveats: Host selects backend/model, workspace and actual function permissions. Model intelligence is external, but tool loop and persistence are first-party.

## S2 — Coordination

- State: —
- Function: No evidenced distinct inter-S1 mutual adjustment within the first-party runner.
- Disturbance / variety regulated: Duplicate request IDs and competing turns in one session are prevented by deterministic serialization, not agent mediation of distinct workers.
- Decisive decision or feedback right: Interpret collisions between separate agents and change their reciprocal task commitments; absent.
- Decision owner: Host selects backend; `Runner` locks and orders submissions mechanically.
- Supporting / enforcement mechanisms: Per-session active-turn map, request-ID idempotency, FIFO turn selection and backend cursor handover.
- Closure path: Runner serializes a single session and preserves events; no inter-agent conflict finding is interpreted by an S2 decision owner and returned to S1 peers.
- Why this is / is not agent-owned: A session switching sequentially between backends is not two simultaneously interacting S1 units; locks and ordering alone are not S2 autonomy.
- Evidence: [runner.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/runner.go), [README.md](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/README.md), [handover/handover.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/handover/handover.go).
- Basis: structural.
- Confidence: high at declared session recursion.
- Caveats: Host apps could build their own multi-agent coordination above faden; it is not in this boundary.

### Absence scope

- Surfaces inspected: Runner per-session scheduling, backend mapping, handover context, worker lifecycle and storage locking.
- Plausible first-party paths checked: Multiple backend names, concurrent sessions, duplicate submission idempotency, queue order and resume cursors.
- Why no material first-party path remains: No shipped owner interprets a conflict between distinct agents and adapts their mutual commitments; these facilities serialize or restore tasks.

## S3 — Inside-and-now control

- State: —
- Function: No separate agent-owned whole-system current resource/commitment management is established.
- Disturbance / variety regulated: Restarted turns, queue backlogs and backend availability are runtime failure/recovery signals, not managed by a whole-system model policy.
- Decisive decision or feedback right: Reassign priorities, budgets and multiple operational units from an integrated current view; absent.
- Decision owner: Host app names the backend, input and workspace; Runner deterministically processes one turn per session and bounded attempts.
- Supporting / enforcement mechanisms: `Open`/`Submit`, store cursor and attempts, `Drain`/`Wait`, max attempts and context selection.
- Closure path: Process restart → Runner reloads events and resumes the same assigned task, without deciding organizational commitments or allocating new priorities.
- Why this is / is not agent-owned: Resilient scheduling is significant infrastructure but not a substantive whole-system agent decision right; S1 continuity does not imply S3.
- Evidence: [runner.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/runner.go), [faden.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/faden.go), [README.md](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/README.md).
- Basis: structural.
- Confidence: high for reviewed first-party scheduler/runner.
- Caveats: A host could create an agentic supervisor, but the public faden API does not attribute that supervisor to faden.

### Absence scope

- Surfaces inspected: Runner store state, current pending turns, model backend configuration, failure/retry and handover logic.
- Plausible first-party paths checked: Multi-session `Runner`, durable attempts, pause/drain/restart and per-session turn ordering.
- Why no material first-party path remains: These mechanisms are deterministic continuity controls; no agent or parent makes an ongoing whole-system resource/commitment decision through them.

## S3* — Complementary audit

- State: —
- Function: No independently owned claim audit/correction path across ordinary agent reports and underlying evidence.
- Disturbance / variety regulated: Missing tool results or interrupted turns are reconstructed for continuity rather than treated as potentially false operational claims to independently check.
- Decisive decision or feedback right: Independently inspect the underlying artifact, challenge agent completion and return an enforceable correction; absent.
- Decision owner: Model continues its own turn; host may inspect store events, but no separate auditor is allocated.
- Supporting / enforcement mechanisms: Stored event transcripts, tool pre/post events, crash-safe replay, test fixtures and `read_thread`.
- Closure path: Replayed event history returns to the original/next agent for work continuity; no independent reviewer judgment → rejected claim → corrective S1 path.
- Why this is / is not agent-owned: Auditable event logs are evidence access, not a first-party model/auditor with a mandate and independent return channel.
- Evidence: [llama/llama.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/llama/llama.go), [attempt.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/attempt.go), [handover/handover.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/handover/handover.go).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Event logs make external audits possible but the harness does not assign the S3* task to an independent decision owner.

### Absence scope

- Surfaces inspected: Runner completion status, tool event validation, event stores, read-thread access and test scenarios.
- Plausible first-party paths checked: Replay correctness checks, unsafe-tool interruption, stored evidence, external CLI resume and crash tests.
- Why no material first-party path remains: All feed integrity and resumption, not an independent challenge of an agent's success report followed by mandatory repair.

## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct externally prospective capability-learning/adaptation owner is evidenced.
- Disturbance / variety regulated: Backend switching, loss of tool context and restart state are present task-continuity disturbances.
- Decisive decision or feedback right: Generate, select and enact future organizational capability options from external developments; absent.
- Decision owner: Host preselects backend and model per turn; faden creates bounded catch-up from past events mechanically.
- Supporting / enforcement mechanisms: Handover cursors, budgeted context selection, prior transcript retention and library backend injection.
- Closure path: Historic messages → context slice → next model turn; no future-oriented proposal/evaluation/authorized persistent capability change is returned.
- Why this is / is not agent-owned: Moving an active task from Claude to llama is host-selected execution continuity, not prospective environmental adaptation.
- Evidence: [handover/handover.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/handover/handover.go), [runner.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/runner.go), [README.md](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Host applications can learn from transcripts; faden itself does not implement their future strategy.

### Absence scope

- Surfaces inspected: Handover algorithm, crash restoration, model backend setup, stored event transcript and library API.
- Plausible first-party paths checked: Cross-model task continuation, budgeted history retrieval, persistent conversation memory and retry conditions.
- Why no material first-party path remains: The evidence is repackaged for the present turn and backend chosen by a host, without an owned future capability option and authorized return.

## S5 — Policy and identity

- State: —
- Function: No built-in ultimate-purpose/policy governance or legitimate parent constitutional adjudication is established.
- Disturbance / variety regulated: Tool side effects, host credentials, retention and retry limits, not identity/policy conflicts.
- Decisive decision or feedback right: Authoritatively change binding purpose or resolve a contested ultimate policy and return it to operations; absent.
- Decision owner: Host controls tools, workspace, models, credentials, permissions and overall user intent; faden only enforces local safe-replay boundaries.
- Supporting / enforcement mechanisms: Host-configured `Tool.Safe`, runtime setup, max attempts, failed-turn status and passed-in system instructions.
- Closure path: Unsafe interrupted tool is not automatically retried; status returns to host. No policy conflict is decided at a legitimate internal/parent authority and carried back to the agent.
- Why this is / is not agent-owned: Deterministic safety and error outcomes do not constitute S5 purpose decision rights.
- Evidence: [llama/llama.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/llama/llama.go), [runner.go](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/runner.go), [README.md](https://github.com/nogo/faden/blob/e59833d32c775b86c7b35b2ca1b3cd1b042b5886/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Different host organizations may have external S5 controls, beyond the assessed library boundary.

### Absence scope

- Surfaces inspected: Runtime tool policy, backend setup, host responsibilities, failure/stop handling, library interface and stored events.
- Plausible first-party paths checked: Safe-tool re-execution, host-defined system prompts, CLI permissions, fatal-error termination and backend switching.
- Why no material first-party path remains: These are operational constraints and host choices, not a shipped ultimate-policy authority with an accountable return path.

## Distributed OSS parent arrangement

Open-source users embed faden in separate local applications with their own stores. The upstream repository does not provide shared parent governance over those deployments. Host ownership of application policy does not make parent-governed S3/S4/S5 a first-party faden function.

## Self-hosted and non-human modes

The native llama backend can operate against a locally hosted OpenAI-compatible model; Claude/Codex alternatives require installed external runtimes. Storage may be JSONL, caller-owned SQLite or memory. Autonomous tool decisions remain S1 only; the embedding host supplies all upper-recursion governance.

## Recursion

Session continuity, backend swaps and durable turns are one S1 operational stream. Distinct host applications or model vendors are not independently viable recursions within faden.

## Variety and escalation

The model handles task uncertainty, and faden absorbs crash/replay variety with append-only evidence and safe retry boundaries. Errors, exhausted attempts and provider mismatches return to the host; no separate S2/S3/S3*/S4/S5 agent escalation loop is shipped.

## Evidence gaps

- No live local llama-server, Claude or Codex turn was run in this review. Go tests could not execute because Go is unavailable in this environment.
- The ability for host apps to compose advanced supervisory/audit agents is not attributed to the faden library itself.
- Durable resume and handover demonstrations are documentation/test evidence, not measured VSM metasystem effectiveness.
