---
harness_id: swarms-code
project_name: Swarms Code
repository: https://github.com/The-Swarm-Corporation/swarms-code
review_ref: eb00b2a5a84d0a07461e0d264d9727b6367555b0
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Swarms Code

## Review boundary

- System in focus: the first-party Rust terminal coding-agent executable at `eb00b2a5a84d0a07461e0d264d9727b6367555b0`, especially `Engine`, `Session`, its model wrapper, directly registered coding tools, permissions and CLI turn handling.
- Purpose and identity: interpret user software-engineering requests, inspect or modify files, run permitted shell actions and iterate model/tool feedback in a local project until the model finishes or a bounded stop intervenes.
- Relevant environment: the local working directory, repository/project instructions, file contents and modification times, user requests and consent, tool results and failures, and configured remote model services.
- Standard-distribution boundary: shipped `swarms-code` CLI, `src/agent.rs` execution loop, `src/tools/*`, `src/session.rs`, `src/main.rs`, first-party model/provider selection and prompt construction. The `swarms-rs` library executes provider-model calls and the registered tool contracts as a dependency; remote model inference is external. Its general-purpose swarm features are not assumed to be instantiated here.
- Credited operating / distribution surfaces: `src/main.rs`, `src/agent.rs`, `src/tools/mod.rs`, `src/tools/fs.rs`, `src/tools/search.rs`, `src/tools/bash.rs`, `src/tools/todo.rs`, `src/session.rs`, `src/models.rs`, `src/prompt.rs` and documented ordinary CLI use.
- Adjacent first-party surfaces excluded from ownership: crate unit tests, GitHub CI/release/build tooling, README development claims beyond the inspected implementation, contributor governance and any multi-agent constructs available only in the external `swarms-rs` library.
- First-party operating / deployment modes considered: interactive chat, one-shot `-p`, `--auto-approve`, approval-on-edit/command mode, model and effort switches, conversation `/clear` and user interruption.
- Recursion level: one Swarms Code session with one model-backed coding actor and one shared tool/session state. Multiple tool calls or external library classes are not additional S1 work cells at this assessed boundary.
- Reviewed revision: `eb00b2a5a84d0a07461e0d264d9727b6367555b0`.
- Observation date: 2026-10-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The Rust CLI constructs a `Session`, resolves a selected model/provider and instantiates an `Engine`. `Engine::run_turn` places the user instruction into conversation history and repeatedly asks the `SwarmsAgent` to chat; when the model calls a tool, the engine records assistant tool-call IDs and corresponding tool results in provider-compatible history, then makes another model call. A final response or bounded step limit ends the turn. This is a first-party executable composition even though `SwarmsAgent::chat` delegates model transport and individual tool-call dispatch to `swarms-rs`.

The registered tools are local file read/write/edit/list, glob/grep, Bash and a todo-list update. `Session` tracks previously read file modification times; writes/edits require a fresh read and, in interactive mode, an operator approval unless the operator enabled `--auto-approve`. The permission interface also supports allowing edit or command categories for the rest of a session; refusing an action halts the turn and prevents subsequent same-step tools from running. One-shot mode denies actions needing unavailable interactive consent unless auto-approval was explicitly selected.

Session conversation history lives in the `Engine` for that process; `Session` also maintains the file-read freshness map, permissions and todos. The user can change model or effort, clear conversational state, and interrupt a turn. Provider selection, effort fitting, model catalog refresh, retry policy and max steps are operational support. The code does not instantiate independent subordinate agent loops, a current-work portfolio manager, an independent auditor, a prospective capability-adaptation cell, or an ultimate-policy adjudicator. This last sentence is bounded to the reviewed standard executable, not a claim about what the `swarms-rs` library or custom future code can build.

Primary pinned sources:

- [`src/agent.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/agent.rs)
- [`src/tools/mod.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/tools/mod.rs)
- [`src/session.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/session.rs)
- [`src/main.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/main.rs)
- [`src/prompt.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/prompt.rs)
- [`README.md`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/README.md)

## Operational model

The model-backed coding actor owns the next repository-oriented action choice within its available tools; the first-party executable turns that choice into tool execution and returns the result for another discretionary choice. File-freshness checks, permission gates, transient-retry handling, step bounds and ordered tool execution are enforcing/support mechanisms around that one S1. In `--auto-approve` the shipped mode can close this loop without case-by-case human intervention. In interactive default mode the operator retains veto power over edits and non-read shell actions, but that veto is not a separate organizational S2/S3/S5 function.

## S1 — Operations

- State: A
- Function: carry out software-engineering work by selecting local repository/tool operations from task and workspace evidence, executing them and revising subsequent choices from returned effects.
- Disturbance / variety regulated: heterogeneous file/project state, user intent, coding alternatives, tool failures, stale file reads, provider replies and uncertainty about the next useful action.
- Decisive decision or feedback right: choose the task-specific next tool call and its arguments, or decide to answer without further tool calls, after receiving the preceding tool evidence.
- Decision owner: the model-backed coding actor wrapped by the `Engine` in its supported `--auto-approve` mode. The selected remote model is an inference dependency, while the first-party runtime assembles and closes the coding tool loop.
- Supporting / enforcement mechanisms: `swarms-rs` model/tool API, first-party `ObservedModel`, eight registered coding tools, `Session` approval/freshness gate, history encoding, provider routing, step limit, retries and CLI controls.
- Closure path: user task and carried conversation → model selects coding action → first-party registered tool executes → tool result is added to history under its call ID → next model call chooses a new action or finishes.
- Boundary reachability: `src/main.rs` constructs the shipped `Engine`; `build_agent` registers all tools; `Engine::run_turn` is called by both interactive chat and one-shot command handling. `--auto-approve` is a documented CLI option.
- Why this is / is not agent-owned: remove the model actor and the remaining tool adapter, permission checker and retry/budget machinery cannot choose meaningful task-specific edits, commands or follow-up actions. They support or enforce the model's discretionary operations.
- Evidence: [`src/agent.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/agent.rs); [`src/tools/mod.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/tools/mod.rs); [`src/main.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/main.rs); [`src/session.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/session.rs).
- Basis: explicit + structural.
- Confidence: high for source construction; no live provider-backed outcome was run.
- Caveats: chat completion/tool-call execution depends on the external `swarms-rs` library and a selected model service. This assessment credits only the instantiated first-party coding composition, not undocumented provider behaviour.

## S2 — Coordination

- State: —
- Function: no materially evidenced inter-S1 conflict/oscillation damping relationship in the shipped single-session coding organization.
- Disturbance / variety regulated: tool-call ordering and permission prompt overlap are within one S1's execution, not interference among distinct S1 units.
- Decisive decision or feedback right: no inter-S1 coordination decision established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ordered tool calls, a shared `Session`, read-freshness checks, todo state and user interruption.
- Closure path: no distinct S1s → inter-S1 disturbance → attenuation → altered subsequent separate-S1 behaviour path is instantiated.
- Why this is / is not agent-owned: sequencing a single actor's requested tools prevents UI/permission overlap but is not coordination among separate environment-facing operational units.
- Evidence: [`src/agent.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/agent.rs); [`src/tools/mod.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/tools/mod.rs); [`src/session.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/session.rs).
- Basis: structural absence review.
- Confidence: high within assessed first-party runtime.
- Caveats: the name and dependency `swarms-rs` do not demonstrate that this binary instantiates multiple agent work cells.

### Absence scope

- Surfaces inspected: first-party `Engine` and `build_agent` model/tool construction; `tools::all`; `main` session/turn handling; shared permission and todo state; README-supported CLI modes.
- Plausible first-party paths checked: independently running child agents, multiple coding S1 workers, shared workspace collision regulation, model/provider switching as role coordination and sequential tool-call discipline.
- Why no material first-party path remains: the shipped executable creates one model-backed work loop and registers coding tools only; no inter-S1 disturbance or coordination feedback among independently operating S1 units is instantiated.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-organization current-control capability managing multiple operational commitments, priorities or shared resources was established.
- Disturbance / variety regulated: step limits, output-token ceilings, command consent and transient retries bound one coding session, not a portfolio of operational units.
- Decisive decision or feedback right: no substantive whole-system allocation, commitment management or current-work intervention right separate from one S1's task choices was evidenced.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: `Engine::max_steps`, model maximum tokens/effort settings, prompt controls, `Session::approve`, user interruption and retry bounds.
- Closure path: no separate whole-system current view → S3 resource/commitment judgment → returned change to cross-S1 operation is shipped.
- Why this is / is not agent-owned: choosing a coding tool or observing its result remains S1; enforcing operator-preselected limits does not confer an S3 management decision right on the runtime.
- Evidence: [`src/agent.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/agent.rs); [`src/session.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/session.rs); [`src/main.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/main.rs).
- Basis: structural absence review.
- Confidence: high within inspected runtime.
- Caveats: parent permissions regulate side effects of one S1 and do not by themselves establish whole-system S3=P.

### Absence scope

- Surfaces inspected: engine turn state/history; model/catalog/effort setup; session controls and permission gates; todo tool; CLI commands and stopping behaviour.
- Plausible first-party paths checked: manager/lead agent over child workers, current portfolio view, adaptive resource redistribution, whole-system priority trade-offs and parent intervention through operator approvals.
- Why no material first-party path remains: only a single coding S1 and static/operator-set bounds are instantiated; no first-party whole-system manager owns resource/commitment decisions with operational return at this recursion.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary inspection and corrective-audit path is established in the supported coding session.
- Disturbance / variety regulated: test/build command results and file-read evidence are ordinary feedback to the same coding actor, not a separate audit channel challenging its report.
- Decisive decision or feedback right: no complementary audit judgment identified.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Bash, file read/search tools and source-code unit tests/CI outside the assessed runtime.
- Closure path: no independent audit → challenge judgment → resulting corrective control is wired into normal operation.
- Why this is / is not agent-owned: the same coding actor may choose to inspect files or run tests, but that is routine verification in its own S1 pathway; repository CI is an adjacent development surface.
- Evidence: [`src/tools/mod.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/tools/mod.rs); [`src/agent.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/agent.rs); [`src/main.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/main.rs).
- Basis: structural absence review.
- Confidence: high for this shipped source boundary.
- Caveats: no claim is made about development-stage or externally installed independent evaluation systems.

### Absence scope

- Surfaces inspected: `build_agent` registered tool list; production turn and result history; local file/search/Bash tools; bundled tests and README runtime description.
- Plausible first-party paths checked: independent reviewer agent, external-ground-truth sampling, reconciler/adversarial checker, ordinary Bash tests as potential audit and developer CI.
- Why no material first-party path remains: no separate auditor's evidence-access and judgment path is instantiated or fed back to current control; ordinary tests remain part of S1 or adjacent repository development.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective capability adaptation loop established for the runtime organization.
- Disturbance / variety regulated: provider availability/catalog differences, token capacity and current project context are handled as model selection and task execution, not prospective organizational redesign.
- Decisive decision or feedback right: no first-party externally informed adaptation proposal and adoption judgment evidenced.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: `models::fetch_catalog`, `Engine::prepare`, model/effort switch, project instruction loading and conversational continuity.
- Closure path: the code lacks an environment/future distinction → option generation → adoption into subsequent organizational capability path; model catalogs only constrain current choices.
- Why this is / is not agent-owned: a user switches a configured model/effort and model metadata bounds output settings; the coding actor is not given a prospective organizational capability-adaptation decision right.
- Evidence: [`src/agent.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/agent.rs); [`src/models.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/models.rs); [`src/prompt.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/prompt.rs).
- Basis: structural absence review.
- Confidence: high within examined supported modes.
- Caveats: developers may extend providers or tools later, but hypothetical extensions do not establish currently shipped S4.

### Absence scope

- Surfaces inspected: model catalog/selection and effort handling; engine turn loop; environment prompt; tool registration; session feedback and user settings.
- Plausible first-party paths checked: future environmental sensing, prospective provider/tool scouting, automated adaptation option generation, automatic adoption or parent-authorized deployment of new capabilities.
- Why no material first-party path remains: present mechanisms select and fit existing configured providers and execute current tasks; they do not make future-facing changes to the system's capability repertoire through a closed first-party S4 loop.

## S5 — Policy and identity

- State: —
- Function: no first-party identity or ultimate-policy adjudication with a return-to-operation path is evidenced at this runtime boundary.
- Disturbance / variety regulated: static system/project instructions, safety notices and action-approval preferences constrain runtime tools but do not establish an organizational ultimate-policy dispute and closure.
- Decisive decision or feedback right: not established for S5-level policy/identity.
- Decision owner: not established; operator/developer supplies instructions and approval configuration outside a distinct S5 function.
- Supporting / enforcement mechanisms: compiled system prompt, project `SWARMS.md`/`AGENTS.md`/`CLAUDE.md` instructions, `Session::approve`, `--auto-approve`, no-interactive consent refusal.
- Closure path: no identity-level issue → legitimate ultimate authority → authoritative decision → returned policy governing later operation is provided.
- Why this is / is not agent-owned: prompt contents and tool consent boundaries are externally selected constraints; routine approval of an edit or command is not ultimate-policy governance.
- Evidence: [`src/prompt.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/prompt.rs); [`src/session.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/session.rs); [`src/system_prompt.rs`](https://github.com/The-Swarm-Corporation/swarms-code/blob/eb00b2a5a84d0a07461e0d264d9727b6367555b0/src/system_prompt.rs).
- Basis: structural absence review.
- Confidence: high within inspected runtime.
- Caveats: repository maintainer governance changes the software distribution at another organizational boundary; it is not silently credited as first-party runtime S5=P.

### Absence scope

- Surfaces inspected: compiled system instructions; dynamic project instruction loading; operator approval modes; CLI configuration/model preferences; engine and tool execution boundaries.
- Plausible first-party paths checked: runtime agent-owned identity revision, ultimate-policy issue escalation to operator/maintainers, authoritative policy change returned to later sessions and normal tool-approval escalation.
- Why no material first-party path remains: observed instructions and permissions are preselected inputs/enforcement for execution; no shipped process classifies identity-level disputes, assigns legitimate ultimate authority and closes a returned policy decision.

## Recursion

The assessed terminal session contains one model-backed operational S1. The individual tools, UI, `Session`, `Engine` and external dependency `swarms-rs` do not establish viable nested S1 organizations in the first-party executable. Additional possible actors in the general dependency ecosystem were not credited without shipped composition evidence.

## Variety and escalation

Freshness checks attenuate stale-file edits; permission modes transfer risky side-effect authorization to the operator unless auto-approval is explicitly chosen; step bounds, ordered tool dispatch, retry limits and model output limits restrict operational variety. Search/read/edit/Bash and conversational tool-result feedback amplify the actor's means of handling heterogeneous coding tasks. Operator refusal stops the ongoing S1 turn and can be addressed in the next user message; it is not evidenced as an S3/S5 organizational escalation channel.

## Evidence gaps

- Source-first classification is based on the reviewed Rust code and maintainer docs; no real model-provider request, coding-effectiveness benchmark or execution-quality test was run.
- The implementation depends on `swarms-rs` for transport and tool invocation. First-party evidence proves the concrete executable model/tool composition but does not verify every behavior internal to the dependency.
- The review found no shipped second operational unit or independently corrective auditor. This is a bounded finding, not a claim that the underlying library or future extension cannot build one.
