---
harness_id: chad
project_name: chad
repository: https://github.com/nathansutton/chad
review_ref: a5f7a47166005ef9aa3a3ddc2c035479b75911cb
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# chad

## Review boundary

- System in focus: the first-party chad coding runtime at frozen revision a5f7a47166005ef9aa3a3ddc2c035479b75911cb, including its tightly coupled model/tool loop, locally owned inference engine path, built-in coding tools, prompt/context/session state, ambient result-channel state, verification/syntax/guardrail machinery, edit checkpoints, permissions/modes, MCP/skills and terminal UI.
- Purpose and identity: operate as one local coding agent on an Apple Silicon workstation, choosing repository actions, edits and verification steps while the harness owns the local model execution path and execution safeguards.
- Relevant environment: user requests and approvals, repository files, shell/test/tool results, local model generation, context pressure, resumed session history, MCP services, project instructions, skills and OS/sandbox state.
- Standard-distribution boundary: shipped chad runtime and repository-owned inference/agent/tool/session/safety code. Host shell/toolchains, external MCP servers, user repositories and optional remote llama-compatible endpoints remain dependencies; owning local inference does not by itself donate a higher VSM function.
- Credited operating / distribution surfaces: src/chad/agent.py, tools.py, prompt.py, ambient.py, guardrails.py, syntaxgate.py, checkpoint.py, compaction.py, session.py, TUI/configuration and supported local/remote backend execution.
- Adjacent first-party surfaces excluded from ownership: benchmarks, dev instrumentation, CI/release tooling, anti-slop development utilities and test fixtures unless the corresponding mechanism is wired into ordinary runtime operation.
- First-party operating / deployment modes considered: ordinary interactive coding; normal/auto/yolo/plan permission modes; resumed sessions; local MLX engine; optional llama-compatible backend; MCP/skills; edit undo/restore and user cancellation.
- Recursion level: one chad coding conversation. No separate standard operational agent unit is instantiated at this frozen boundary.
- Reviewed revision: a5f7a47166005ef9aa3a3ddc2c035479b75911cb.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

chad centers one model-backed Agent loop that renders conversation state, generates a model turn, parses tool calls, executes first-party tools and appends results back into the same conversation until the model stops calling tools. The harness owns a tightly coupled local inference path but can also use a compatible remote backend.

The runtime includes substantial deterministic supporting machinery: context packing/compaction, result clipping/spill, todo tracking, syntax checks, destructive-command screening, sandboxing, credential filtering, checkpoints, resume/forked sessions, repetition/tool-call repair and a finish verification re-grounding nudge. The ambient result channel records session facts such as environment manifests, touched files and verification baselines and can persist them with a resumed session.

Those mechanisms improve one operational agent's reliability and continuity. The frozen runtime does not expose a first-party task-subagent/orchestrator subsystem. Test names referring to a subagent reflect test construction/history rather than a shipped separate agent role; the product README explicitly describes one tightly coupled agent loop.

## Operational model

The active model owns open-ended software-engineering choices: what to inspect, edit, run, verify and when to finish. Deterministic runtime code constrains those choices, preserves/reconstructs context and injects targeted corrective feedback when execution becomes unsafe, repetitive, syntactically broken or under-verified.

Plan mode and write_todos remain inside the same S1 decision process. Checkpoint restore, Ctrl+C cancellation and permission modes constrain or reverse the single agent's work. Ambient/session persistence can affect later turns, but no separate first-party future-intelligence owner develops adaptation options from changing external conditions.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify a software project through model-selected coding and tool actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, shell/test failures, malformed tool calls, context pressure, local-model failure modes, syntax regressions and verification gaps.
- Decisive decision or feedback right: choose substantive repository/tool actions, interpret returned evidence, revise the implementation and decide when the requested work is complete.
- Decision owner: the active model-backed chad Agent.
- Supporting / enforcement mechanisms: bash/read/write/edit/MCP tools, locally owned inference engine, context packing/compaction, ambient result annotations, guardrails, syntax gate, checkpoints, permission modes and session persistence.
- Closure path: user request → model selects coding/tool action → runtime executes and returns evidence → model revises work or verifies → model emits completion when satisfied.
- Boundary reachability: the shipped CLI/TUI directly instantiates the same Agent loop in ordinary local operation; optional backends change model execution, not organizational ownership.
- Why this is / is not agent-owned: deterministic code executes, validates and constrains actions, but the model owns the open-ended engineering decision and interpretation.
- Evidence: [README.md](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/README.md); [src/chad/agent.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/agent.py); [src/chad/tools.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/tools.py); [src/chad/prompt.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/prompt.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: normal/auto modes may retain human approval for some mutations; approval constrains the action and does not supply the substantive coding decision.

## S2 — Coordination

- State: —
- Function: no material inter-S1 coordination function is established.
- Disturbance / variety regulated: none at the declared recursion because the frozen standard runtime does not instantiate distinct concurrent operational agent units.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: tool-result sequencing, prompt queues, locks/caches inside inference/runtime and MCP connection concurrency coordinate components, not peer operational S1 units.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: there is no distinct-S1 interference relation under a first-party coordination loop.
- Evidence: [README.md](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/README.md); [docs/architecture.md](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/docs/architecture.md); [src/chad/agent.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/agent.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: parallel repo-map workers or MCP connections are implementation workers/services, not independently viable coding S1s.

### Absence scope

- Surfaces inspected: agent loop, tools, TUI, architecture/configuration docs, repository tree/search for task/subagent/worker/orchestrator paths, model engine and MCP paths.
- Plausible first-party paths checked: coding subagents, parallel write workers, peer scheduling, file ownership/worktrees, conflict arbitration and inter-agent messaging.
- Why no material first-party path remains: the shipped product exposes one coding-agent loop; located parallelism is infrastructural rather than separate operational agency.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established beyond the single S1 operation.
- Disturbance / variety regulated: no portfolio of current S1 commitments/resources exists under a distinct current-control owner.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: todo state, step/turn caps, productive-work extensions, Ctrl+C, plan mode, permission modes, checkpoint restore and context diagnostics regulate one operational conversation.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the model manages its own task/todos as S1. Deterministic stop/retry/nudge/undo controls are safeguards over that same operation, not whole-system current control.
- Evidence: [src/chad/agent.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/agent.py); [src/chad/guardrails.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/guardrails.py); [src/chad/tui.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/tui.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: plan/todo tracking is useful self-management, but Methodology 0.3.6 requires a whole-system current view and substantive current-control scope beyond ordinary S1 self-management.

### Absence scope

- Surfaces inspected: todos, plan mode, TUI status/cancel, checkpoint restore, guardrails, context diagnostics, resume and model/backend controls.
- Plausible first-party paths checked: current worker/commitment portfolio, resource allocation, selective live worker intervention, supervisor model and parent current-control dashboard.
- Why no material first-party path remains: all current-control-like mechanisms operate on the same single coding loop or provide generic stop/reversal.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no separate first-party actor independently checks an implementation claim through a distinct evidence path and returns a corrective judgment.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established.
- Supporting / enforcement mechanisms: verify-baseline annotations, syntax gate, deterministic finish re-grounding and the same model's test/shell actions improve self-verification.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: verification is either deterministic or performed by the same author agent; no fresh reviewer/verifier model or independent audit channel is instantiated.
- Evidence: [src/chad/ambient.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/ambient.py); [src/chad/syntaxgate.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/syntaxgate.py); [src/chad/agent.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/agent.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: tests are evidence consumed by S1; deterministic syntax/verification gates are not an independent complementary intelligence owner.

### Absence scope

- Surfaces inspected: finish/re-grounding logic, syntax gate, verify baselines, prove command, tests/bench paths and repository search for reviewer/verifier/subagent roles.
- Plausible first-party paths checked: fresh-context reviewer, second-model critique, independent repository audit worker, separate eval verdict and automatic corrective review loop.
- Why no material first-party path remains: no independent agent/evidence channel is wired into ordinary coding operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no changing outside/future condition is placed under an actor that develops adaptation options and returns them into present capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persisted sessions, ambient facts/baselines, project instructions, skills, model configuration and context compaction preserve/reuse information but do not by themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: session/ambient state can survive resume and shape a later turn, but persistence/reuse is not an external-and-prospective option-development loop.
- Evidence: [src/chad/ambient.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/ambient.py); [src/chad/session.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/session.py); [src/chad/compaction.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/compaction.py); [docs/configuration.md](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/docs/configuration.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: resumed sessions can retain prior operational distinctions, but the active Profile/Methodology does not equate memory persistence with S4.

### Absence scope

- Surfaces inspected: session persistence/resume, ambient baselines, project instructions, skills, MCP, model/backend config, compaction and diagnostics.
- Plausible first-party paths checked: environment scanning, learned durable strategy, autonomous capability/model/tool reconfiguration and future-oriented option generation returned to current control.
- Why no material first-party path remains: identified mechanisms preserve context or externally configured capabilities rather than close a prospective adaptation conversation.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy issue is routed to an authoritative S5 owner and returned as governing policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: system prompt, permission modes, sandbox, destructive-command guard, credential filtering, project instructions and configuration constrain ordinary execution.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent operates within developer/user-authored safety and configuration rules and cannot authoritatively redefine chad's identity or ultimate operating principles.
- Evidence: [src/chad/prompt.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/prompt.py); [src/chad/agent.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/agent.py); [src/chad/seatbelt.py](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/src/chad/seatbelt.py); [docs/configuration.md](https://github.com/nathansutton/chad/blob/a5f7a47166005ef9aa3a3ddc2c035479b75911cb/docs/configuration.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user modes/configuration are legitimate constraints on S1; they are not identity governance.

### Absence scope

- Surfaces inspected: system prompt, permission modes, sandbox/security guardrails, project instructions, skills/MCP, configuration and model/backend selection.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity policy, agent-authored permissions and authoritative identity/policy return loop.
- Why no material first-party path remains: observed policy surfaces are static or externally controlled operating constraints.

## Distributed OSS parent arrangement

The assessed organization is the running chad coding agent, not the GitHub maintainer project. Repository development, benchmarks and release governance are not imported as runtime parent functions.

## Self-hosted and non-human modes

chad primarily runs a local model on Apple Silicon and can use a compatible remote backend. The S1 claim is independent of whether inference is local or remote. Owning the inference process is an implementation/deployment fact, not a separate S2–S5 organizational function.

## Recursion

The declared viable-unit candidate contains one model-backed coding S1. Tools, model engine, ambient state, context management, checkpoints and guardrails are components/support mechanisms of that S1 rather than distinct viable operational units.

## Variety and escalation

The S1 loop absorbs coding and verification variety. Deterministic guardrails, syntax checks, checkpoints, sandboxing, context compaction and ambient annotations reduce failure modes or preserve evidence but do not establish additional VSM ownership functions.

## Evidence gaps

No ? state is required. The frozen repository exposes the complete first-party agent loop, tool/runtime, session/ambient and safety surfaces, while repository-wide searches show no shipped multi-agent/reviewer/control-plane path that would require an unresolved positive ownership judgment.
