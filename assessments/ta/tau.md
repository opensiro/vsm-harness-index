---
harness_id: tau
project_name: Tau
repository: https://github.com/huggingface/tau
review_ref: 9fe6a719ac0bda3696e9fc8413643cfe9786c73c
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Tau

## Review boundary

- System in focus: Tau's first-party, installed terminal coding-agent application, with its reusable `tau_agent.AgentHarness`, `tau_coding.CodingSession`, model-stream adapter `tau_ai`, built-in coding tools, and first-party CLI/print/TUI/RPC frontends.
- Purpose and identity: respond to project coding requests by examining files, changing code, running shell commands, incorporating results, and retaining inspectable sessions.
- Relevant environment: a user-supplied local project, filesystem and subprocesses, model-provider services, project instructions and resources, credentials, human prompts, error/cancellation signals and configured extensions.
- Standard-distribution boundary: frozen source-built/PyPI `tau-ai` command (`tau_coding.cli:app`) plus the first-party `tau_agent` and `tau_ai` packages; default in-process `CodingSession` wires a single `AgentHarness` to the four bundled `read/write/edit/bash` tools. Optional installed extensions and injected providers are supported configuration surfaces, not unobserved first-party decision owners.
- Credited operating / distribution surfaces: `pyproject.toml`, `src/tau_coding/cli.py`, `src/tau_coding/session.py`, `src/tau_agent/harness.py`, `src/tau_agent/loop.py`, `src/tau_agent/session/storage.py`, `src/tau_coding/tools.py`, `src/tau_coding/extensions/runtime.py`, `src/tau_coding/project_trust.py`, and `src/tau_coding/context_window.py`.
- Adjacent first-party surfaces excluded from ownership: repository tests, release/update/CI, educational development notes and example extensions, website/roadmap, package-maintainer governance, and third-party model providers or user-installed extension implementations. In particular, the documented reusable constructor seam does not by itself instantiate a product-level federation of S1 agents.
- First-party operating / deployment modes considered: interactive terminal UI, one-shot print mode, RPC/embedded frontend driving the same session/harness, session resume and branch operations, trusted optional extensions and local provider integration.
- Recursion level: one Tau coding-task/session operating organization, not the Hugging Face maintainer organization or a hypothetical host composed of multiple `AgentHarness` instances.
- Reviewed revision: [`9fe6a719ac0bda3696e9fc8413643cfe9786c73c`](https://github.com/huggingface/tau/tree/9fe6a719ac0bda3696e9fc8413643cfe9786c73c) (immutable intake #200).
- Observation date: 2026-10-22; first-party source inspection, no live external-provider execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Tau is a Python package distributed as the `tau` CLI, separating provider-neutral model streaming (`tau_ai`), the reusable agent loop and message/session primitives (`tau_agent`), and the project-aware terminal application (`tau_coding`). The installed app constructs a `CodingSession`, selects a provider/model, composes `read`, `write`, `edit`, and `bash` with eligible extensions, and creates one stateful `AgentHarness`. The harness obtains an assistant response, executes requested tools, appends tool observations, and asks the model again. A user can steer or queue follow-up messages; persistent JSONL sessions support return and branch operations.

Provider retry/failover and automatic context compaction maintain one coding session. The app also supports user-approved project resources, extension registration and hooks, model choice, package update checks and local tool/session locks. These are real operating features; their names do not establish distinct metasystemic ownership without a functional witness. In particular the model-generated compaction summary is context reduction, not a prospective organizational adaptation decision. A provider-neutral extension API can be used by a separate host to build subagents or validators, but the inspected default application does not ship such an interacting population.

Primary evidence: [package/runtime entry](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/pyproject.toml), [system architecture](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/README.md), [session wiring](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/session.py#L689-L761), [harness and loop](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/loop.py#L93-L182), [extension runtime](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/extensions/runtime.py#L264-L315).

## Operational model

The default product has one model-guided coding S1 unit, acting within a project and an asynchronously event-rendered session. Its outcome is a code investigation/change/command result, not mere text routing. The user defines the task and may change provider or project trust, while the agent selects concrete tool calls and continuation from context. Runtime loops, JSONL locks, queued user messages, trust gating and extension hooks execute, constrain or carry those decisions; they are not independently proved whole-system coordination, current control, audit, prospective adaptation or ultimate policy.

## S1 — Operations

- State: A
- Function: task-local autonomous coding operations over the project.
- Disturbance / variety regulated: changing user requirements, unfamiliar source layout, file/tool output, command failures and results requiring another implementation decision.
- Decisive decision or feedback right: the model selects coding tool names/arguments and its subsequent response based on returned results until task completion, cancellation or runtime turn limit.
- Decision owner: the model-backed `AgentHarness` operating through `tau_agent.run_agent_loop` in a first-party `CodingSession`.
- Supporting / enforcement mechanisms: `tau_ai` provider stream, built-in file/shell tools, event hooks, cancellation/turn limits, provider retry, context compaction and JSONL session history.
- Closure path: user/project context → provider model response/tool call → Tau tool executor → structured result message appended to context → next model request/decision or final response.
- Boundary reachability: the published `tau` entry constructs `CodingSession`; its `load()` installs bundled coding tools and creates an `AgentHarness`, while `prompt()` invokes its loop and streams/persists actual tool and model events.
- Why this is / is not agent-owned: the model exercises discretionary task-specific choice of the action sequence; fixed tool implementations and provider adapters alone could not choose the same coding solution without that model decision. This is S1 work, not autonomous metasystem management.
- Evidence: [wiring to model/tools](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/session.py#L689-L761), [agent decision/tool/result continuation](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/loop.py#L93-L182), [tool execution/observation](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/loop.py#L283-L340), [four default tools](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/tools.py#L164-L185), [session prompt handoff](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/session.py#L3134-L3213).
- Basis: executable first-party structure and maintainer description.
- Confidence: high for distributed source wiring; no live provider outcome measurement.
- Caveats: provider access and model effectiveness are external; static code inspection supports the task decision loop but not coding-success rates or full production traces.

## S2 — Coordination

- State: —
- Function: no separate installed coordination of distinct interacting S1 coding units established at this single-session recursion.
- Disturbance / variety regulated: potential write collisions between independent sessions, not an established default multi-S1 organizational disturbance; a single harness's multiple tool calls are S1 sequence steps.
- Decisive decision or feedback right: no identified first-party relation selecting or returning a conflict-attenuating adjustment among multiple default S1 agents.
- Decision owner: none established for S2; tool and transcript-lock machinery is deterministic shared-resource integrity support.
- Supporting / enforcement mechanisms: sequential model/tool calls, message steering queues, `JsonlSessionStorage` per-session cross-process advisory lock and per-path write/edit locks within a process.
- Closure path: file/session writes are serialized and readable, but no shipped multi-agent conflict report/adjustment/return into distinct S1 operating policies is established.
- Why this is / is not agent-owned: `AgentHarness` enforces one active run; no default subagent spawn/parallel S1 constructor is installed. A re-usable `AgentHarness` class and storage locks can support third-party coordination without proving a VSM S2 function in the assessed distribution.
- Evidence: [single active harness and steering/follow-up](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/harness.py#L147-L232), [sequential tool-call iteration](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/loop.py#L153-L180), [cross-process session lock](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/session/storage.py#L38-L90), [local coding-tool locks](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/tools.py#L164-L185).
- Basis: structural.
- Confidence: medium-high, limited to the supported default Tau coding session.
- Caveats: an external embedding host can create several harness instances or supply an extension implementing inter-agent coordination; that separate architecture is not a shipped default S2 path.

### Absence scope

- Surfaces inspected: default CLI/session/harness creation, run-loop tool iteration, session persistence locks, file edit locks, extension composition and reusable library boundary.
- Plausible first-party paths checked: multiple tool calls, parallel-tool declaration, cross-process JSONL serialization, in-process file locks, user message queues, possible host-constructed subagents and RPC consumers.
- Why no material first-party path remains: these protect the consistency of one session or provide a composition interface, but do not install a first-party population of independently goal-directed S1 cells plus identified inter-cell interference attenuation and behavioral return.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current controller of operating-unit resources and commitments established in the default coding-session boundary.
- Disturbance / variety regulated: token window, provider failures, session processes and user message queues are locally handled coding-run constraints rather than cross-unit commitments.
- Decisive decision or feedback right: no separate actor/reconstructable whole-system intervention over S1 resource, priority or accountability trade-offs.
- Decision owner: model/operator chooses task actions and configured provider; first-party runtime enforces local session limits and retries, without an S3-specific right.
- Supporting / enforcement mechanisms: session manager, model selection, context estimates/compaction, retry/failover and cancellation; trust/extension hooks enforce local control choices.
- Closure path: error, context or provider signals return to the current coding loop, not to a separate whole-system control decision subsequently applied to a portfolio of operations.
- Why this is / is not agent-owned: provider configuration, tool limits and task continuation stay at S1/operator scope; a Python class named `SessionManager` is not evidence of whole-system VSM S3 management.
- Evidence: [one harness per session](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/session.py#L689-L761), [local retry/compaction](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/session.py#L3189-L3314), [current local run state/queues](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/harness.py#L65-L100).
- Basis: structural.
- Confidence: medium-high for shipped terminal operation.
- Caveats: a programmatically composed multi-session product could have independent S3 governance; it is not evidenced as the Tau CLI's standard parent.

### Absence scope

- Surfaces inspected: one coding-session construction, durable session manager, context/usage estimates, failover, provider/config controls, extension hooks and terminal UI run control.
- Plausible first-party paths checked: running state, max turns, persistent sessions, queueing, model fallback, token budgets, operator commands and project trust.
- Why no material first-party path remains: these bound or recover a task-local S1 run; no separate whole-current view, resource decision right and returned cross-cell intervention can be reconstructed in this product mode.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit challenging normal operational reports and informing whole-current corrective control in the default session.
- Disturbance / variety regulated: defective code/tool output can be rechecked by the same coding agent or user, but task-level quality assurance is not an independent manager-account audit.
- Decisive decision or feedback right: no installed complementary auditor with a distinct raw-artifact path and authoritative return into current management.
- Decision owner: agent uses `read/bash` verification if it chooses; user may inspect outputs. Extension hooks are user-supplied capability, not a first-party audit claimant.
- Supporting / enforcement mechanisms: observable tool events, JSONL transcript, tool-call/result extension hooks and repository tests.
- Closure path: tool observations feed S1, while event observers and tests lack an installed independent S3*-to-S3 corrective feedback loop.
- Why this is / is not agent-owned: ordinary S1 validation and diagnostics can improve task results without independently auditing another reporting channel; optional extension registries cannot supply a concrete default audit owner.
- Evidence: [tool event stream](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_agent/loop.py#L283-L340), [extension event/hook mechanisms](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/extensions/runtime.py#L994-L1042), [extension event dispatch](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/extensions/runtime.py#L1179-L1227).
- Basis: structural.
- Confidence: medium-high at the default app boundary.
- Caveats: a separately installed auditor extension could establish another assessment boundary if its actual evidence access, independence and control return were pinned and inspected.

### Absence scope

- Surfaces inspected: model tool feedback, persistence/event stream, extension runtime and registrations, built-in terminal tools, source tests and CLI reporting.
- Plausible first-party paths checked: model self-testing, `bash` checks, event listeners, after-tool-call hooks, transcript replay and contributed extension examples.
- Why no material first-party path remains: normal checks are within S1, while installed source hooks offer generic user-programmable interception; the frozen default product lacks an independently owned complementary raw-access audit with returned corrective S3 control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no demonstrated externally prospective option-generation, choice and adoption loop that changes present organizational capability.
- Disturbance / variety regulated: model endpoint failure, context exhaustion and changing user task information; these are immediate S1 execution disturbances.
- Decisive decision or feedback right: no first-party adaptive choice about future capability or viability brought from external distinctions into current organizational arrangements.
- Decision owner: model selects task-local tactics; provider selection, extension installation and version updates remain operator/developer-controlled or deterministic.
- Supporting / enforcement mechanisms: provider-model catalog and route failover, model-generated compaction summary, provider retry, session persistence, optional extension registration and update notice.
- Closure path: model/tool or context errors trigger a current-task retry/summary; no outside/future option is evaluated and adopted into a changed operating capability through an S4–S3 return.
- Why this is / is not agent-owned: generic research tool calls or creating a context summary are not durable strategic adaptation; route failover preserves current work instead of modeling prospective futures.
- Evidence: [compaction/retry and route failover](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/session.py#L3189-L3314), [context summary creation](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/context_window.py#L265-L340), [extension loader/registry](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/extensions/runtime.py#L264-L315).
- Basis: structural.
- Confidence: medium-high for the frozen CLI.
- Caveats: external hosts or independently developed extensions might implement prospective learning/adaptation, but none is credited from configurability alone.

### Absence scope

- Surfaces inspected: runtime recovery, model/provider selection, tool-driven research possibility, extension loading, model-generated context compaction and project release/update documentation.
- Plausible first-party paths checked: Hugging Face endpoint failover, provider catalogs, skill/plugin installation, retained transcripts, session summaries and version checks.
- Why no material first-party path remains: these change task context or operator-selected configuration but do not expose a concrete prospective external distinction → adaptation option → accepted capability change → later operational feedback loop.

## S5 — Policy and identity

- State: —
- Function: no operational ultimate purpose/identity or policy-constitutional decision with legitimate authority and returned governing result at this single coding-session recursion.
- Disturbance / variety regulated: running untrusted project resources and tool commands is a permission/trust risk, not by itself a question of organizational identity or ultimate policy.
- Decisive decision or feedback right: user or trusted extension may grant/deny resource admission, but no evidenced ultimate identity-policy issue is decided and returned to re-govern Tau's ongoing organizational purpose.
- Decision owner: human and saved trust preferences own local project admission choices; developers author system prompts and built-in tool policy. The coding model owns S1 choices within these bounds.
- Supporting / enforcement mechanisms: project trust detector/coordinator/store, saved parent-path trust, UI approve/decline, extension trust hook, model/provider configuration and project `AGENTS.md`.
- Closure path: a trust decision filters protected resources in the current session; it does not close a legitimate S5 identity/ultimate-policy deliberation and ongoing governing-policy return.
- Why this is / is not agent-owned: neither a prompt nor a trust gate is an agent-owned identity decision, and a human permission approval over executable inputs is not automatically the parent-governed `P` S5 mode.
- Evidence: [trust scope and allowed decisions](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/project_trust.py#L1-L125), [decision flow](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/project_trust.py#L484-L646), [trusted resource selection](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/session.py#L551-L605), [extension trust gate](https://github.com/huggingface/tau/blob/9fe6a719ac0bda3696e9fc8413643cfe9786c73c/src/tau_coding/extensions/runtime.py#L1150-L1169).
- Basis: structural.
- Confidence: medium-high within the declared product boundary.
- Caveats: broader institutional/vendor governance may exist beyond the local coding-session recursion; it is not silently borrowed.

### Absence scope

- Surfaces inspected: system/project instructions, project trust UI and store, trust extension hook, tool/provider settings, accepted session state and repo maintainer adjacency.
- Plausible first-party paths checked: user approval, persisted project trust, parent-directory trust, dynamic trust extensions, tool gating, system prompt, contributor/release policy.
- Why no material first-party path remains: these are settings and executable-input admission mechanisms; no shipped first-party path elevates an identity/ultimate-policy issue to legitimate authority and returns a new governing decision into subsequent organizational operation.

## Distributed OSS parent arrangement

Tau's OSS repository is maintained by humans, and separate contributors may run their own `tau` sessions, but there is no evidence that ordinary coding sessions are deployed as a single first-party shared organizational parent whose S3–S5 decisions are fed back into those running local cells. Contributor review, tests, roadmap and releases are adjacent project governance, not automatically `P` modes of the installed coding session.

## Self-hosted and non-human modes

The installed app supports local projects, providers, skills, user extensions and operator-facing trust choices. None forms a documented separate parent-governed whole-system S3/S4/S5 closure at the assessed recursion. Likewise, no autonomous non-human metasystem is reconstructed solely from the single operating model or plugin API.

## Recursion

The assessed Tau unit is one coding-task/session organization. `AgentHarness` is embeddable in a larger host, and its package supports arbitrary consumers, but the inspected product wiring contains one decisive coding S1, not a bundled hierarchy of independent viable cells. Multiple installations or session branches do not alone establish nested VSM recursion.

## Variety and escalation

File and shell observations amplify the model's ability to discriminate local task state. Tool errors and model/provider failures return to the current session, while cancellation, trust denial, context overflow and extension hooks attenuate or reject unsafe/unusable operations. Ordinary UI interaction and queued follow-up provide task feedback; neither is automatically an algedonic channel or whole-organization policy escalation.

## Evidence gaps

- Pinned source-inspection assessment only: no external model invocation or end-to-end working-project trace was performed, and actual coding success is unmeasured.
- A separately authored user extension or host could add subagents, reviewer independence, coordination, governance or adaptation using exposed interfaces; those mechanisms are not intrinsic, inspected shipped Tau paths and cannot be assigned from hypothetical programmability.
- The session lock and file-write lock demonstrate deterministic data integrity. The declared default CLI supplies no evidenced inter-S1 organizational feedback loop, so they are not promoted to S2 by names or concurrency alone.
