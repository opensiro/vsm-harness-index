---
harness_id: sentra
project_name: Sentra
repository: https://github.com/dewhush/sentra
review_ref: d3736e0eb87aa7747ae18201f41c9abc6c584526
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

# Sentra

## Review boundary

- System in focus: Sentra's first-party Linux daemon, CLI, and browser/Tauri viewer, not the independent AI CLIs it starts.
- Purpose and identity: Multiplex externally supplied agent or shell processes in PTYs and allow a human or script to send, wait, read, and hand off their output.
- Relevant environment: Local operator, Linux PTY/process API, configurable executable presets, terminal UI and optional network viewer.
- Standard-distribution boundary: Rust `sentra-daemon` spawning PTYs; `sentra-cli` and GUI send explicit verbs through the daemon; no bundled first-party model reasoning engine.
- Credited operating / distribution surfaces: [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md), [registry.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/registry.rs), [server.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/server.rs), [presets.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/presets.rs).
- Adjacent first-party surfaces excluded from ownership: External `claude`, `codex`, `hermes`, `omp` executables, user shell scripts, roadmap-only MCP/DAG/sandbox designs and test harnesses.
- First-party operating / deployment modes considered: Local Unix socket daemon with headless CLI, browser UI and optional Tauri frontend; optional TCP viewer.
- Recursion level: One first-party Sentra multiplexer. Independent child agents are external processes, not Sentra-owned VSM function holders.
- Reviewed revision: `d3736e0eb87aa7747ae18201f41c9abc6c584526`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The registry spawns a configured executable into a PTY, records PID/state and broadcasts terminal bytes; server commands accept spawn/send/wait/read/kill requests. The README deliberately describes the UI as a viewer and the CLI as an orchestration API. A sample handoff runs `sentra read` and `sentra send` from an explicit user-authored shell command. Agent presets name external programs. Scheduled autonomous cross-agent DAG execution and MCP hub are future-roadmap items, not shipped runtime controls. [registry.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/registry.rs), [server.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/server.rs), [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md#usage).

## Operational model

Sentra receives operator/API instructions to start external processes, send literal input, and expose terminal output. The external CLI may reason and use tools, but the first-party Sentra daemon does not select its own task-sensitive tool actions from model feedback. A transport capable of joining several agents is not itself an autonomous agent-loop owner.

## S1 — Operations

- State: —
- Function: First-party autonomous task execution, rather than PTY transport for externally hosted agents.
- Disturbance / variety regulated: Task-specific uncertainties and tool observations in agents run inside external executables.
- Decisive decision or feedback right: No first-party model→action→observation→next-action choice found.
- Decision owner: Human/CLI caller chooses which executable and input; the external executable owns any AI choices.
- Supporting / enforcement mechanisms: PTY spawn, terminal send/read, ring buffers, process lifecycle and presets.
- Closure path: Terminal bytes return to caller/viewer, but no first-party reasoning loop consumes them to choose subsequent task actions.
- Why this is / is not agent-owned: Process hosting alone does not transfer an external AI agent's decision rights to the multiplexer.
- Evidence: [registry.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/registry.rs), [server.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/server.rs#L550), [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md#features).
- Basis: structural
- Confidence: high for code-visible PTY ownership; not a runtime exercise of each external agent.
- Caveats: A custom user-supplied shell/agent can orchestrate through Sentra's CLI, but that does not establish first-party bundled agency.

### Absence scope

- Surfaces inspected: CLI usage, daemon registry, request handlers, preset config, lesson injection and shipped architecture.
- Plausible first-party paths checked: Multi-spawn @mentions, send→wait→read handoff, lessons and auto-respawn prompts.
- Why no material first-party path remains: Each sends caller-authored data or transports an external program's output; even lessons and respawn require explicit operator action.

## S2 — Coordination

- State: —
- Function: Autonomous regulation of mutual interference between first-party S1 units.
- Disturbance / variety regulated: Concurrent child processes, output buffering and terminal contention.
- Decisive decision or feedback right: No first-party cross-agent conflict detection and corrective mediation discretion.
- Decision owner: Operator or external programs command handoffs; daemon enforces PTY bookkeeping.
- Supporting / enforcement mechanisms: Per-process buffers, global event fan-out, spawn/list/wait/kill APIs.
- Closure path: A wait/read response is available to a caller, without a first-party regulator changing agent behavior in response to interference.
- Why this is / is not agent-owned: Concurrent PTYs and direct-message transport are substrate, not evidence of an S2 decision owner.
- Evidence: [registry.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/registry.rs), [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: User-authored scripts can implement coordination outside this boundary.

### Absence scope

- Surfaces inspected: PTY registry, server commands, handoff UI, roadmap and presets.
- Plausible first-party paths checked: Concurrent spawn, idle waiting, inter-agent send, process exit and multi-pane view.
- Why no material first-party path remains: No path converts inter-unit interference evidence into an owned adaptive coordination choice and returned adjustment.

## S3 — Inside-and-now control

- State: —
- Function: Current whole-system priority, allocation and corrective commitment regulation.
- Disturbance / variety regulated: Resource use, dead PTYs, failed children and simultaneous work.
- Decisive decision or feedback right: No whole-harness adaptive prioritization/reallocation found.
- Decision owner: Operator sends kill/forget/spawn; daemon maintains requested sessions and counters.
- Supporting / enforcement mechanisms: PID registry, memory/uptime reporting, terminal event broadcasts, explicit kill/forget and manual respawn.
- Closure path: Runtime status is shown to user; no first-party state→managerial decision→resource correction loop.
- Why this is / is not agent-owned: Telemetry and process-lifecycle mechanics do not make an autonomous operational manager.
- Evidence: [server.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/server.rs#L468), [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md#features).
- Basis: structural
- Confidence: medium-high.
- Caveats: The roadmap proposes future orchestrated workflows only.

### Absence scope

- Surfaces inspected: Status/health reporting, lifecycle actions, idle waits and shipped roadmap phases.
- Plausible first-party paths checked: Dead-agent notices, RSS monitoring, auto-respawn proposal, timeouts and manual kills.
- Why no material first-party path remains: All decisions beyond deterministic lifecycle enforcement depend on external instructions or explicit human clicks.

## S3* — Complementary audit

- State: —
- Function: Independent challenge/verification and return of a corrective control verdict.
- Disturbance / variety regulated: Misleading outputs from independently running CLI agents.
- Decisive decision or feedback right: No independent first-party verifier with correction authority found.
- Decision owner: Human can read output; external agent may be asked to review another externally.
- Supporting / enforcement mechanisms: Terminal transcript read, logs and operator handoff.
- Closure path: Observations are available but there is no separate audit verdict→current-control correction return.
- Why this is / is not agent-owned: Displaying an external model's terminal text is routine visibility, not independent audit.
- Evidence: [registry.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/registry.rs), [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md#why-it-looks-like-this).
- Basis: structural
- Confidence: medium-high.
- Caveats: A separately configured external reviewer is possible but not a Sentra-owned shipped S3* mandate.

### Absence scope

- Surfaces inspected: Event stream, logs, UI, daemon commands and examples of one agent reviewing another.
- Plausible first-party paths checked: Output visibility, external security review prompts, lesson extraction and smoke tests.
- Why no material first-party path remains: No protected alternate-evidence path produces an independent runtime verdict bound to corrective authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: First-party future/environment sensing with adaptive capability change.
- Disturbance / variety regulated: Evolving external agent tools and future orchestration features.
- Decisive decision or feedback right: No prospective decision/installation loop reaches runtime.
- Decision owner: User edits presets; maintainers own the roadmap.
- Supporting / enforcement mechanisms: Configurable preset commands, research CLI invocation, planned MCP bridge/DAGs.
- Closure path: Config and roadmap remain externally updated, not changed by an autonomous harness intelligence loop.
- Why this is / is not agent-owned: A research command or planned features do not demonstrate closed future-oriented self-adaptation.
- Evidence: [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md#architectural-roadmap), [presets.rs](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/crates/sentra-daemon/src/presets.rs).
- Basis: structural
- Confidence: medium-high.
- Caveats: Future releases may add autonomous functions outside this pin.

### Absence scope

- Surfaces inspected: Roadmap stages, preset loading, research endpoint and server actions.
- Plausible first-party paths checked: Searching outside, learning from lessons, changing tools and proposed autonomous DAGs.
- Why no material first-party path remains: None yields first-party future-oriented option selection and an applied capability update.

## S5 — Policy and identity

- State: —
- Function: Legitimate first-party identity and ultimate-policy issue resolution.
- Disturbance / variety regulated: Security exposure, authority limits and conflicting user goals.
- Decisive decision or feedback right: No identity-level issue→governing decision→policy return path present.
- Decision owner: Maintainers and operator choose network exposure, presets and per-command authority.
- Supporting / enforcement mechanisms: Same-user Unix socket, manually enabled TCP listener, documented security warning.
- Closure path: Static configuration protects some entry points but cannot settle/return a higher-order policy dispute.
- Why this is / is not agent-owned: Security defaults and local operator choices do not constitute first-party S5 closure.
- Evidence: [SECURITY.md](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/SECURITY.md), [README](https://github.com/dewhush/sentra/blob/d3736e0eb87aa7747ae18201f41c9abc6c584526/README.md#security-notes).
- Basis: structural
- Confidence: medium-high.
- Caveats: Conventional human project governance is not evaluated as an in-product S5.

### Absence scope

- Surfaces inspected: Socket and TCP modes, security documentation, operator commands and user presets.
- Plausible first-party paths checked: Authority via Unix mode, unrestricted TCP opt-in, local process control and agent role preambles.
- Why no material first-party path remains: No legitimate in-system identity decision mandate and operational feedback channel is implemented.

## Recursion

External programs may be autonomous systems with their own functions; Sentra hosts their terminals without establishing ownership of those functions at the Sentra boundary.

## Variety and escalation

PTY lifecycle, event fan-out and operator-facing errors attenuate operational hazards. Kill/forget/wait and manual handoff are command-level control, not independent S2/S3/S5 escalation authority.

## Evidence gaps

Source review only, without a Linux runtime smoke test or live execution of external agents. Not a judgment about the autonomy of Codex, Claude or Hermes outside the Sentra boundary.

## Verdict

**Exclude — no first-party agentic VSM.** Sentra is useful as a multi-agent terminal/workspace, but its reviewed shipped architecture delegates AI discretion to separately installed executables, while Sentra only transports input/output and explicitly requested control operations.
