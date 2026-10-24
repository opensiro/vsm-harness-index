---
harness_id: pooled
project_name: Pooled
repository: https://github.com/Nehanth/pooled
review_ref: b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Pooled

## Review boundary

- System in focus: Pooled's first-party browser Code mode under `harness/` at frozen revision `b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4`, including the `Agent` model/tool loop, coding tools, project/workspace state, preview server/sandbox, session persistence and host approval path.
- Purpose and identity: let the room model build and repair a small static web application in the host browser by editing project files, executing the result in a sandboxed preview, observing runtime evidence and iterating.
- Relevant environment: user objective, host project files, preview/browser runtime, console errors/warnings, host approval decisions, saved Code sessions, model output and tool results.
- Standard-distribution boundary: `harness/agent.js`, Code prompt/tools/workspace/projects, preview server/frame/tools, sessions and normal Code-mode wiring are inside. The distributed WebGPU/WebRTC inference pipeline is the model-compute substrate and does not donate organizational functions. External CDNs, browser/OS and room peers performing model layers are environment/dependencies.
- Credited operating / distribution surfaces: `README.md`; `harness/agent.js`; `harness/code-prompt.js`; `harness/codetools.js`; `harness/preview-tools.js`; `harness/preview.js`; `harness/preview-frame.js`; `harness/workspace.js`; `harness/sessions.js`; `docs/design/harness-app.md`; `SECURITY.md`.
- Adjacent first-party surfaces excluded from ownership: distributed layer assignment/re-deal, speculative decoding and kernel verification; repository CI/evals; roadmap/research documents except where they describe shipped Code-mode behavior; room participants as inference workers.
- First-party operating / deployment modes considered: scratch browser projects; host-selected real folders with approval; normal Code mode; saved/restored sessions; sandboxed preview and console capture.
- Recursion level: one Code-mode coding session. The room model acting through `Agent` is the focal S1. Preview/browser execution is a complementary constructor evidence path, not a second production S1.
- Reviewed revision: `b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Pooled Code mode has a compact first-party agent loop independent of the distributed-inference implementation. `Agent.run` sends the accumulated conversation to a supplied model generator, parses model-authored tool calls, runs the matching Code tools, appends `<tool_response>` evidence and repeats for up to the configured step bound. It includes cancellation, context compaction, repeated-call guards, tool-result recovery hints and a terminal response path.

The coding toolset reads/searches/writes/edits a browser workspace. Mutating tools pass through `approve`; a real disk folder requires host approval and exposes a before/after preview, while browser scratch projects can apply directly.

Code mode also closes a separate runtime-check path. Its system prompt explicitly instructs the model to serve the app and fix every error before finishing. The first-party `serve` tool builds the current workspace into a sandboxed preview, waits for the preview frame, captures console errors/warnings from the actually executed revision and returns those findings as a tool result. `preview_logs` exposes subsequent console evidence. The agent then receives that evidence in its ordinary feedback loop and can repair the files. The preview's execution-derived evidence is independent of the coding model's prose or self-report, but no separate autonomous reviewer owns the verdict, so this is constructor S3* rather than agent-owned S3*.

Primary evidence:

- [`harness/agent.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/agent.js)
- [`harness/code-prompt.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/code-prompt.js)
- [`harness/codetools.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/codetools.js)
- [`harness/preview-tools.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/preview-tools.js)
- [`SECURITY.md`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/SECURITY.md)

## Operational model

A Code-mode request enters `Agent.run`. The model sees the system prompt, conversation and tool definitions, chooses file/search/edit/serve operations, and receives each result as the next user-side tool-response turn. File mutations update the current workspace and any served preview revision.

When the model calls `serve`, Pooled executes the current application in the preview sandbox instead of trusting the model's claim that the generated code works. The preview reports whether it loaded and returns actual errors/warnings with source/line information. Those findings return to the same coding actor, which can edit and serve/check again.

## S1 — Operations

- State: A
- Function: build and repair a static web application in the host's project workspace through iterative model-selected coding and preview actions.
- Disturbance / variety regulated: heterogeneous user requests, current project files, malformed/ambiguous model tool calls, edit conflicts, runtime errors, context pressure, repeated failures and host approval decisions.
- Decisive decision or feedback right: choose which file/tool/preview action to execute next, what code to write or edit, how to react to returned tool/runtime evidence and when the task is complete.
- Decision owner: the model-backed Pooled Code-mode actor running through first-party `Agent`.
- Supporting / enforcement mechanisms: coding tools; tool-call parser/argument repair; project workspace; approvals; recovery cards; context compaction; repeated-failure/stuck guards; preview tools; saved sessions.
- Closure path: user objective + project/session state → model selects a Code tool → Pooled executes or approval-gates it → result enters conversation → model selects next action or finishes.
- Boundary reachability: normal room Code mode directly instantiates this first-party loop; the model-compute implementation can be distributed or local without changing the organizational loop.
- Why this is / is not agent-owned: removing the model actor leaves deterministic tools/workspace/preview machinery but removes the open-ended coding judgment that chooses and sequences actions.
- Evidence: [`harness/agent.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/agent.js); [`harness/codetools.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/codetools.js); [`README.md`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the WebGPU/WebRTC room supplies model inference; it is not separately credited as an organizational actor.

## S2 — Coordination

- State: —
- Function: no material same-recursion inter-S1 coordination function was established in Code mode.
- Disturbance / variety regulated: not established at S2 level. The distributed peers split neural-network layers but do not operate as distinct production S1s performing independent coding work.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: room layer allocation/re-deal; host/peer transport; project/preview synchronization.
- Closure path: not applicable; no distinct coding-S1 interference → attenuation decision → changed subsequent S1 behavior loop was found.
- Why this is / is not agent-owned: distributed inference is implementation-level computation for one model decision process, not organizational coordination among autonomous operational units.
- Evidence: [`README.md`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/README.md); [`docs/architecture.md`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/docs/architecture.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: multiple browser peers are physical compute participants, not multiple coding S1s at this recursion.

### Absence scope

- Surfaces inspected: Code-mode agent; room host/peer model split; project/preview synchronization; host/peer Code views; layer re-deal.
- Plausible first-party paths checked: peer plurality; file synchronization to peers; inference layer partitioning; room host role.
- Why no material first-party path remains: these paths distribute computation or replicate read-only presentation and do not create distinct operational coding actors with an interference-specific coordination relation.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-organization current-control function was established beyond the focal S1 loop and deterministic runtime guards.
- Disturbance / variety regulated: step budget, context budget, repeated failures, cancellation and current preview state are controlled, but no portfolio of distinct production S1 commitments/resources is managed.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: max steps; context compaction; stuck/repeat detection; cancellation; session/project state; host approval.
- Closure path: not applicable; no whole-system current view plus substantive organization-wide intervention loop exists at the assessed recursion.
- Why this is / is not agent-owned: current-task execution choices remain S1; deterministic guards bound that same loop rather than supply a distinct management function.
- Evidence: [`harness/agent.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/agent.js).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: robust loop control is not the same as VSM S3 whole-current control.

### Absence scope

- Surfaces inspected: agent step/context/stuck guards; project/session lifecycle; host approvals; preview lifecycle; room host role.
- Plausible first-party paths checked: host as manager; preview state as whole-current view; recovery cards; repeated-failure guard.
- Why no material first-party path remains: all located controls govern one coding loop/environment and do not manage multiple operational commitments as a distinct metasystem function.

## S3* — Complementary audit

- State: C
- Function: challenge the coding actor's implicit claim that the generated application works by executing the current files in a separate sandboxed browser-preview path and returning runtime errors/warnings for correction.
- Disturbance / variety regulated: generated HTML/CSS/JavaScript can be syntactically valid-looking or verbally declared complete while failing at runtime, loading missing assets or emitting browser errors.
- Decisive decision or feedback right: the constructor-owned preview path independently observes actual page load/runtime behavior and reports the presence and concrete content/location of errors and warnings.
- Decision owner: first-party deterministic preview server/frame/log-capture machinery; no separate autonomous reviewer owns the audit verdict.
- Supporting / enforcement mechanisms: `serve`; sandboxed preview frame; build/rewrite pipeline; revision tracking; initial 500 ms/2 s load observation; console error/warning capture; `preview_logs`; system instruction to serve and fix errors.
- Closure path: coding S1 mutates project files → model calls the standard serve/check path → Pooled executes the current revision in the sandbox → runtime errors/warnings are captured independently → evidence returns as the tool result → coding S1 edits/fixes and can re-run the preview.
- Boundary reachability: `serve` and `preview_logs` are standard Code-mode tools and the shipped system prompt explicitly tells the agent to serve and fix every error.
- Why this is / is not agent-owned: the independent evidence is generated by deterministic browser execution and log capture, not by a distinct model auditor. It therefore establishes constructor-owned complementary audit, not autonomous S3*.
- Evidence: [`harness/preview-tools.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/preview-tools.js); [`harness/code-prompt.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/code-prompt.js); [`harness/agent.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/agent.js); [`SECURITY.md`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/SECURITY.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the preview primarily audits runtime behavior of the static web app, not full semantic satisfaction of every user requirement.
- Claim being audited: that the current generated/edited web application is runnable and free of the runtime/console failures visible to the shipped preview path.
- Ordinary reporting path: the model's coding/tool loop produces files and eventually would report completion.
- Complementary access path: Pooled independently executes the current files in a sandboxed preview and reads browser-generated load/console evidence rather than trusting model prose.
- Independence boundary: preview execution, browser parsing/runtime and captured console events are causally separate from the model's self-report and can contradict it; final semantic repair judgment remains with the same coding model.
- Who acts on findings: the Code-mode model receives the serve/log evidence as a tool response and performs subsequent edits/rechecks.

## S4 — Intelligence / adaptation

- State: —
- Function: no material autonomous outside-and-future intelligence/adaptation loop was established.
- Disturbance / variety regulated: sessions and project files persist, and recovery cards/compaction improve current execution, but no process prospectively models environmental change and selects a persistent organizational adaptation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: saved sessions; project persistence; recovery cards; context compaction; runtime evidence.
- Closure path: not applicable; no external/future distinction → adaptation option → persistent capability/strategy change → later operation loop was found.
- Why this is / is not agent-owned: retaining files/history and repairing the current app is operational learning/context, not the stronger prospective S4 function.
- Evidence: [`harness/agent.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/agent.js); [`harness/sessions.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/sessions.js).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project persistence can carry useful artifacts into later work without constituting an adaptation function.

### Absence scope

- Surfaces inspected: sessions; projects; compaction; cards/recovery hints; preview-derived correction; model/inference configuration.
- Plausible first-party paths checked: cross-session learning; self-improvement from preview errors; persistent prompt/tool adaptation.
- Why no material first-party path remains: evidence supports persistence and current-task correction, not autonomous prospective capability/strategy redesign.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy loop was established.
- Disturbance / variety regulated: host approval, workspace restrictions, preview CSP/sandbox and Code-mode instructions constrain actions, but they are operating/safety policy.
- Decisive decision or feedback right: not established for an identity/ultimate-policy issue.
- Decision owner: host/user plus deterministic browser/runtime enforcement.
- Supporting / enforcement mechanisms: per-edit approval for real folders; task-scoped approval; workspace path restrictions; opaque-origin preview; CSP; Code system prompt.
- Closure path: not applicable at S5 level; no identity conflict → legitimate ultimate authority → authoritative identity/policy decision → returned organizational operation loop was found.
- Why this is / is not agent-owned: the model acts inside host-selected and browser-enforced constraints; it does not own the ultimate identity/policy boundary.
- Evidence: [`SECURITY.md`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/SECURITY.md); [`harness/agent.js`](https://github.com/Nehanth/pooled/blob/b749f99c524f7a7c51f9e8c539e6b001dfdcdcd4/harness/agent.js).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: human approval is a strong safety control but is not automatically VSM S5.

### Absence scope

- Surfaces inspected: edit approval; preview sandbox/CSP; project/workspace constraints; Code prompt; room host role.
- Plausible first-party paths checked: host as parent authority; task-wide allow-edits choice; security policy; room ownership.
- Why no material first-party path remains: these surfaces approve/enforce operational actions rather than adjudicate a genuine identity/ultimate-policy issue.

## Distributed OSS parent arrangement

Public repository governance and room membership are not imported as runtime metasystem functions. The host approves real-folder edits and controls the room, but this remains task/safety governance rather than a function-specific S3/S4/S5 closure.

## Self-hosted and non-human modes

Pooled runs entirely in browser tabs and may execute the coding loop without per-tool human intervention for scratch projects. Real-folder writes can require host approval. Autonomous S1 and constructor S3* remain identifiable across these modes.

## Recursion

The focal recursion is one Code-mode coding session. Several physical devices may jointly execute the model's neural layers, but that remains one model decision process. The preview runtime is a complementary evidence channel, not another production S1.

## Variety and escalation

Pooled attenuates operational variety through tool argument repair, result caps, compaction, repeated-failure detection, approvals, workspace constraints, sandboxing and preview execution. Preview-derived errors are escalated back into the same coding loop, creating the constructor S3* closure.

## Evidence gaps

No `?` state is required at the frozen revision. Exact-ref implementation clearly establishes the first-party S1 loop and the preview audit closure, while the distributed inference, session persistence and safety controls can be bounded without promoting them to S2/S3/S4/S5.

## Assessment summary

Pooled Code mode closes autonomous S1 through its first-party browser model/tool coding loop and constructor-owned S3* through independent sandboxed preview execution whose runtime errors return to the coder for correction. Its distributed inference peers are compute substrate rather than coding S1s; no whole-current S3, prospective S4 or identity-level S5 closure is established.

**Vector:** A · — · — · C · — · —
