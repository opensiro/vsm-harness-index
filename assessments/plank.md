---
harness_id: plank
project_name: Plank
repository: https://github.com/aovestdipaperino/plank
review_ref: 7b69b23341e3500959fd39f43a7d395b6cdd2255
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Plank

## Review boundary

- System in focus: packaged first-party Plank Rust coding agent runtime, with local and provider inference, real source tools, bounded delegated subagents, optional checkout isolation and first-party goal/memory features.
- Purpose and identity: modify code in a user project, execute shell/file tasks and delegate bounded research/coding work.
- Relevant environment: user Git checkout and file system, shell, tool outcomes, separate delegated sidechain results, selected model inference, user configuration.
- Standard-distribution boundary: native first-party Rust coding runtime and its model-facing tool/sidechain/worktree paths. The external ds4 C model-engine submodule, remote provider internals and externally authored agent role/hook scripts are dependencies, not first-party organizational owners.
- Credited operating / distribution surfaces: src/ui.rs, src/engine.rs, src/tools, src/agents.rs, src/worktree.rs, src/goal.rs, src/memextract.rs, src/settings.rs.
- Adjacent first-party surfaces excluded from ownership: upstream C reference as a separate system, benchmark/demo material, test-only reviewer fixtures, developer CI, optional user-defined external integrations.
- First-party operating / deployment modes considered: normal TUI/REPL/headless code tools; bounded native agent tool with separate sidechain; cross-engine agent definitions; configured worktree-isolated subagent mode; disabled-by-default serial fanout; read-only plan; same-model goal adjudication; lifecycle hooks; automatic memory extraction.
- Recursion level: parent coding session and distinct task-executing agent sidechains as operational cells within a selected project. Isolated delegated coding can be assessed for bounded inter-cell S2 regulation; generic model multiplicity does not create a whole metasystem.
- Reviewed revision: 7b69b23341e3500959fd39f43a7d395b6cdd2255.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

A source-owned Rust agent loop dispatches real file, shell, worktree and other tools after first-party model inference. The model-facing agent tool runs a bounded child task on a forked transcript, executes its own iterative tool work and returns only a final report to its parent. Cross-provider child models are supported. The native fanout feature is optional and explicitly serial, so it must not be misreported as simultaneous independent workers.

A named child can opt into worktree isolation through the agent-definition field isolation: worktree, or use the global isolateAgents setting. Before the child loop the runtime creates an independent Git checkout, points its tool cwd there and then restores the parent cwd. When changes remain, the child checkout is not discarded: its location is reported to the parent for inspection and deliberate integration. This is specific inter-S1 write-interference attenuation. The setting is configurational and its first-party enforcement is deterministic, so classification is C and restricted to the isolated-delegation mode.

The parent may assign tasks and absorb reports; however a distinct discretionary whole-current regulator was not proved. A named reviewer persona is authored by the user, the built-in goal verdict comes from the same acting model and Stop hooks are user-configured. They do not together establish a stock independent source-audit with corrective return. Post-turn memory extraction and retrospective /insights do not amount to future-facing organizational capability renewal.

Pinned first-party sources: [src/ui.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/ui.rs); [src/agents.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/agents.rs); [src/worktree.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/worktree.rs); [src/tools/worktree.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/tools/worktree.rs); [src/goal.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/goal.rs); [src/memextract.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/memextract.rs).

## Operational model

The parent model performs real coding tool work and may delegate smaller tasks to model-driven child rounds. In isolation mode physical separation prevents subagent modifications overwriting the parent working tree, with the saved worktree path returned for subsequent source integration choices. Security and stop conditions support the mechanism but are not separately owned metasystem functions.

## S1 — Operations

- State: A
- Function: Autonomous coding operations using first-party file, shell and source-edit tools.
- Disturbance / variety regulated: Unknown project files, code changes and observed failing commands/tests.
- Decisive decision or feedback right: Select next tool action after seeing returned tool and code effects.
- Decision owner: Plank native coding model and tool loop, including scoped child agent rounds.
- Supporting / enforcement mechanisms: Rust ToolContext, model inference, DSML dispatch, source tools, session persistence and safety gates.
- Closure path: Task request -> model calls first-party tools -> code/files/tests change -> tool output returned -> next model operational choice or completion.
- Boundary reachability: Shipped REPL/TUI/headless mode and model-facing agent tool invoke actual owned coding and file/command handlers.
- Why this is / is not agent-owned: Native model chooses task actions and owned tools execute with observational feedback.
- Evidence: [src/ui.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/ui.rs); [src/engine.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/engine.rs); [src/tools/mod.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/tools/mod.rs); [src/tools/edit.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/tools/edit.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: External C inference and provider endpoints are supporting dependencies, not counted as first-party organizational governance..

## S2 — Coordination

- State: C
- Function: Narrow suppression of write conflicts between parent coding operation and a separately acting delegated coding subagent.
- Disturbance / variety regulated: Child agent and parent can both modify the same Git files, leading to overwrite/dirty tree interference and lost parent work.
- Decisive decision or feedback right: Agent definition or global configuration selects isolated workspace; runtime enforces it and reports changed child worktree to parent.
- Decision owner: Human/configuration constructs isolation mode, deterministic first-party worktree controller enforces, parent agent decides whether to merge.
- Supporting / enforcement mechanisms: Unique per-child worktree creation, cwd transfer/restore, retained changed checkout, per-task report, fail-closed worktree disposal.
- Closure path: Parent delegates -> runtime creates isolated checkout and moves child tool cwd -> child edits separately -> runtime restores parent cwd and reports worktree path -> parent can inspect and deliberately integrate subsequent work.
- Boundary reachability: Built-in model-facing agent tool plus named agent isolation: worktree or worktree.isolateAgents activates this boundary in a real task.
- Why this is / is not agent-owned: Configured partition solves a specific inter-operating-cell write hazard; do not donate autonomous coordination authority to a static worktree gate.
- Evidence: [src/agents.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/agents.rs); [src/ui.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/ui.rs); [src/worktree.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/worktree.rs); [src/tools/worktree.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/tools/worktree.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Not applicable to default unisolated sidechains; serial fanout is not parallel orchestration; no guarantee of semantic merge quality..

- Distinct S1 units: The main task-operating coding loop and the child delegated model-driven task loop with independent source-edit decisions.
- Inter-S1 disturbance: Child editing shared checkout files can overwrite live parent changes, with unreadable and surprising inter-unit side effects.
- Attenuating coordination relation: Enabled per-agent worktree isolation creates a separate Git checkout, shifts the child ToolContext.cwd and restores the parent checkout after the child finishes.
- Feedback into subsequent S1 behaviour: The first-party runner retains any changed child worktree and returns its full location and subagent report; the parent may then inspect, cherry-pick or merge, instead of implicitly inheriting edits.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It directly attenuates a specific cross-S1 write conflict; mere child spawning, sequential fanout and generic report routing are not counted.

## S3 — Inside-and-now control

- State: ?
- Function: Candidate parent-agent orchestration of delegated current work, but no distinct whole-current control closure demonstrated.
- Disturbance / variety regulated: Pending delegated tasks and changed isolated outputs might need multi-unit priority/resource intervention.
- Decisive decision or feedback right: Parent can choose subagent tasks and next steps from returned reports; not proved to reassign ongoing independent work based on whole-current state.
- Decision owner: Potential parent coding model; separately governed S3 role remains unresolved.
- Supporting / enforcement mechanisms: Subagent task/report, opt-in serial fanout, task roster and session goal.
- Closure path: Child outcome and isolated changes are returned to the parent. This does not establish current aggregate resource reallocation of multiple active operating units.
- Why this is / is not agent-owned: A complete separately owned function-specific decision and feedback loop is not demonstrated.
- Evidence: [src/ui.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/ui.rs); [src/agents.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/agents.rs); [src/tasks.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/tasks.rs); [src/goal.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/goal.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Do not infer S3 from a sequential queue or manager-like model prompt..

## S3* — Complementary audit

- State: ?
- Function: Potential separate review sidechain or user Stop hook, but no built-in independent audit-to-corrective-work closure established.
- Disturbance / variety regulated: Coding model can deliver incorrect edits or make an incorrect success claim.
- Decisive decision or feedback right: Configured reviewer child may judge and return text; configured Stop hook may block, but neither is a standard independent source-native audit authority.
- Decision owner: Custom reviewer model/hook if explicitly authored by user; independent first-party S3* owner unresolved.
- Supporting / enforcement mechanisms: Agent definitions, report forwarding, hooks and same-agent GOAL_VERDICT prompt.
- Closure path: Generic child report or hook message may reach coder, but no standard independently constructed source review with a required failure-to-repair return exists.
- Why this is / is not agent-owned: A complete separately owned function-specific decision and feedback loop is not demonstrated.
- Evidence: [src/agents.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/agents.rs); [src/ui.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/ui.rs); [src/goal.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/goal.rs); [src/hooks.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/hooks.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Test-only reviewer fixtures and same-model goal self-verdict are not credited as independent audit judgment..

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environment intelligence and capability adaptation decision closure.
- Disturbance / variety regulated: Future environment requirements and opportunities would need strategic organizational renewal.
- Decisive decision or feedback right: No prospective capability-change decision right established.
- Decision owner: No first-party S4 owner.
- Supporting / enforcement mechanisms: Post-turn memory-extraction sidechain, saved skills, retrospective insights and engine update notices.
- Closure path: Past session memory may enter later prompts and user sees retrospective usage reports; neither implements autonomous future-facing sensing and adaptation.
- Why this is / is not agent-owned: A complete separately owned function-specific decision and feedback loop is not demonstrated.
- Evidence: [src/memextract.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/memextract.rs); [src/memory.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/memory.rs); [src/insights.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/insights.rs); [src/skills.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/skills.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Externally authored skill updates or developer release process are not automatically first-party S4..

### Absence scope

- Surfaces inspected: Automatic memory extraction, skills, personal usage insights, model catalog/version updates and agent settings.
- Plausible first-party paths checked: Past-data reflection, selected provider changes, skill files and developer engine upgrades.
- Why no material first-party path remains: No source-native prospective environmental inquiry, independent options choice and capability-changing decision returned to operations.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate-purpose policy/identity governance authority and binding return.
- Disturbance / variety regulated: Risky shell commands, local file access and cleanup are operational permission issues.
- Decisive decision or feedback right: No ultimate-policy/identity judgment; users configure operation-level tool safety rules.
- Decision owner: No S5 decision owner at this installed project task recursion.
- Supporting / enforcement mechanisms: Plan mode, guard/sandbox, hooks, worktree deletion safety, runtime settings.
- Closure path: Approvals and denials change immediate actions; no foundational policy dispute is adjudicated and returned as binding organizational policy.
- Why this is / is not agent-owned: A complete separately owned function-specific decision and feedback loop is not demonstrated.
- Evidence: [src/guard.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/guard.rs); [src/sandbox.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/sandbox.rs); [src/hooks.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/hooks.rs); [src/tools/worktree.rs](https://github.com/aovestdipaperino/plank/blob/7b69b23341e3500959fd39f43a7d395b6cdd2255/src/tools/worktree.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Human governance outside installed coding harness is excluded..

### Absence scope

- Surfaces inspected: Tool permission, safety, plan mode, hook configuration, worktree disposal and user settings.
- Plausible first-party paths checked: Operation approvals, custom hooks, model/provider switches, user-assigned goals and workspace policy.
- Why no material first-party path remains: No native legitimate authority settles foundational identity/purpose and sends an organization-wide binding policy decision back to later operation.

## Distributed OSS parent arrangement

The public maintainers and upstream ds4 C reference do not become first-party owners of VSM functions in a user's installed Plank coding-session system. Optional user-defined reviewers/hooks can add custom controls, but are not silently adopted into stock positive-function grades.

## Self-hosted and non-human modes

The Rust coding harness can run with its macOS Metal-backed ds4 engine or provider-backed inference. An echo-only build without native inference is not a real autonomous operating mode. The subagent worktree S2 mode is explicitly configured and should not be projected onto non-isolated child tasks.

## Recursion

The parent coding task and a bounded delegated coding subagent each have real iterative model/tool execution. Worktree isolation supplies an inter-unit boundary that attenuates parent-child write variety. Serial fanout, model counts, UI indicators and remembered data do not by themselves prove S3-S5 recursion.

## Variety and escalation

Unsuccessful tool calls and child error/report information return into parent context. Isolated child writes persist as an explicit worktree path for later decision rather than contaminating parent source; failures creating isolation stop the child before it runs. Optional goals are judged by the same model and Stop hooks are user-supplied, not established independent audits.

## Evidence gaps

- S2 C only in configured worktree-isolated child mode; no claim for unisolated sidechains or automatic merge-conflict resolution.
- Whole-current S3 management unresolved despite delegated work reports.
- Independent S3* audit-and-correction not proved by optional reviewer persona or self-adjudicated goal loop.
- No empirical benchmark correctness/latency claims derived from README.
