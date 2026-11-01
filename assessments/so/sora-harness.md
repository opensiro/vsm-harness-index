---
harness_id: sora-harness
project_name: Sora Harness
repository: https://github.com/S0ra233/Sora-Harness
review_ref: cbfddafca44ff18f80181943ce17ba1d271ed7a6
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Sora Harness

## Review boundary

- System in focus: the Python desktop/CLI agent product, including the supported optional subagent and game-translation skill mode.
- Purpose and identity: carry model-directed local work and game-translation projects through tools, durable conversations and controlled output submission.
- Relevant environment: local project/game files, model endpoints, plugins/MCP resources, concurrent child work and user steering.
- Standard-distribution boundary: first-party AgentLoop, ConversationApplication, built-in tool/plugin/skill wiring and subprocess child runtime; no external host's private agents.
- Credited operating / distribution surfaces: desktop/runtime/agent, application/subagents, plugins/subagent tools, ToolRegistry/mutation_gate and the bundled game-translation collaboration flow.
- Adjacent first-party surfaces excluded from ownership: release/packaging helpers and examples; unrelated external Codex/Claude hosts named by cross-host skills; tests or documentation alone do not supply an actor.
- First-party operating / deployment modes considered: single-agent desktop/CLI, opt-in enabled/configured subagent profiles, and bundled translation skill invoked through first-party SkillService.
- Recursion level: one operational application with parent/child task actors; delegation does not establish recursive viability.
- Reviewed revision: cbfddafca44ff18f80181943ce17ba1d271ed7a6.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgentLoop requests a model response, checks complete tool-call identities, executes permitted tools and appends correlated results into the next request. Checkpoints and append-only conversations retain observed outcomes; compaction and steering occur at safe boundaries. SubagentManager persists child lifecycle and launches the same ConversationApplication in isolated child histories under a start barrier. The child inherits the parent's workspace and mutation-lock path but has its own conversation store. Built-in subagent tool descriptions instruct the model to assign distinct result files and avoid concurrent edits to one target. ToolRegistry serializes exclusive operations via a cross-process mutation gate. The translation plugin contributes the bundled skill root; its collaboration flow assigns disjoint target IDs/output paths and makes the main actor reconcile real files before serial apply/build. Users configure providers, profiles, prompts and enabled plugins; these settings do not create identity governance.

## Operational model

The main model actor owns task execution and, in the enabled multi-actor mode, chooses non-overlapping child scopes and output files, revises work through send_subagent, checks actual terminal/artifact state and serializes logical publication. File locks enforce physical write exclusion but cannot resolve semantic overlapping edits; that distinction makes the agent's scope/output choices the S2 decisive right. Task decomposition, result aggregation and ordinary translation review do not by themselves establish S3 or S3*.

## S1 — Operations

- State: A
- Function: produce local tool-mediated task results, translations and project artifacts.
- Disturbance / variety regulated: input formats, provider/tool errors, partial results, project state and user steering.
- Decisive decision or feedback right: choose operations/tools and revise task work after observed results.
- Decision owner: the model-backed main actor and supported child actors in their respective task scopes.
- Supporting / enforcement mechanisms: AgentLoop, provider backends, tool registry, workspace restrictions, step/call limits, checkpoints and subprocess execution.
- Closure path: tool results append to model history; errors or partial state lead to revised actions, while terminal results are persisted.
- Why this is / is not agent-owned: removing the model actors leaves wrappers/storage/guards without discretionary problem solving.
- Evidence: [desktop/runtime/agent/loop.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/runtime/agent/loop.py); [desktop/application/conversations.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/conversations.py); [desktop/runtime/subagents/runner.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/runtime/subagents/runner.py); [desktop/tools/registry.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/tools/registry.py)
- Basis: structural
- Confidence: high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.
- Boundary reachability: ConversationApplication invokes the first-party AgentLoop; the child runner constructs that same application and sends/resumes a message.

## S2 — Coordination

- State: A
- Function: prevent logical and physical write interference between concurrent parent/child operational tasks.
- Disturbance / variety regulated: workers sharing a project can overwrite the same target or publish partial/inconsistent translation packages.
- Decisive decision or feedback right: choose disjoint work/target-ID ranges and separate result paths, revise overlapping scopes and decide serialized final publication.
- Decision owner: the main model actor following the supplied subagent/tool and collaboration mode; locks only enforce exclusive writes.
- Supporting / enforcement mechanisms: scoped subagent tools, actual child status/results, send/continue messages, shared mutation-lock propagation and file-lock serialization.
- Closure path: the main actor reads actual results, checks missing/duplicate/out-of-range IDs and file contents, corrects directly or sends revised child instructions, then commits the reconciled package serially.
- Why this is / is not agent-owned: without the main actor a lock can serialize two incompatible edits but cannot choose semantically disjoint task boundaries or reconcile their outputs.
- Evidence: [desktop/plugins/subagent/tools.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/plugins/subagent/tools.py); [desktop/application/subagents.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/subagents.py); [desktop/runtime/subagents/runner.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/runtime/subagents/runner.py); [desktop/application/mutation_gate.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/mutation_gate.py); [desktop/tools/registry.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/tools/registry.py); [desktop/plugin_catalog.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/plugin_catalog.py); [desktop/application/skills.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/skills.py); [skills/game-translation/references/collaboration.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/references/collaboration.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Optional enabled multi-actor mode, not every single-agent chat. Configured child models/profiles are normal deployment inputs. The lock alone would not justify A.
- Distinct S1 units: main task actor and independent-history child translation, review or research task actors with separate outcomes.
- Inter-S1 disturbance: shared-workspace writes, conflicting edits to the same target and overlapping or incomplete target-ID coverage.
- Attenuating coordination relation: agent-selected non-overlapping ranges/result files, central serial apply/build and corrective scope messages, backed by cross-process write exclusion.
- Feedback into subsequent S1 behaviour: real child states and artifact coverage checks cause corrected delegation/continuation or revised publication decisions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: first-party tool instructions and collaboration rules explicitly identify shared-file/logical collisions and complete-ID publication, rather than merely exposing a generic mailbox.
- Boundary reachability: enabled subagent profiles bind real tool capabilities in SubagentManager; the built-in tool description supplies coordination rules to the model. The translation plugin's skill root and SkillService make the concrete disjoint-ID/serial-commit workflow available in the supported product mode.

## S3 — Inside-and-now control

- State: —
- Function: No supplied whole-application discretionary current-control function is established beyond bounded task coordination.
- Disturbance / variety regulated: child runtime limits, failed work and local task progression.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: subagent status/cancel/continue, per-role step/time/call limits, run records and main-agent task aggregation.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [desktop/application/subagent_profiles.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/subagent_profiles.py); [desktop/application/subagents.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/subagents.py); [desktop/plugins/subagent/tools.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/plugins/subagent/tools.py); [desktop/runtime/runs.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/runtime/runs.py); [skills/game-translation/references/collaboration.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/references/collaboration.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: child profiles/limits, status/continuation/cancellation tools, runtime records and translation coordinator instructions.
- Plausible first-party paths checked: whole-system resource bargaining, competing commitments/priorities and legitimate parent current-control return.
- Why no material first-party path remains: the shipped relation delegates/checks/merges one bounded user task and enforces configured limits; it does not expose a distinct whole-application discretionary control mandate.

## S3* — Complementary audit

- State: —
- Function: No material independent complementary audit path is supplied beyond ordinary operational review.
- Disturbance / variety regulated: incomplete child claims and translation/schema errors are checked in the production workflow.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: actual-file reads, acceptance reports, review subtasks, tool receipts and run/checkpoint logs.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [skills/game-translation/references/collaboration.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/references/collaboration.md); [skills/game-translation/references/candidate-review.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/references/candidate-review.md); [skills/game-translation/SKILL.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/SKILL.md); [desktop/plugins/subagent/tools.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/plugins/subagent/tools.py); [desktop/runtime/session.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/runtime/session.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Independent histories and raw-file availability alone do not turn every review into S3*. This is bounded to the supplied product/skill modes, not a prohibition on a custom audit design.

### Absence scope

- Surfaces inspected: main artifact reconciliation, optional reviewer subtasks, candidate-source selection, acceptance reports and run receipts.
- Plausible first-party paths checked: an independently controlled challenge to operational reporting with complementary access/judgment returned into control.
- Why no material first-party path remains: candidate review selects production input, main reconciliation is normal production responsibility, and configurable review subtasks remain ordinary QA with generic role composition; no separate function-specific complementary audit authority/feedback path is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environment-to-capability adaptation loop is supplied.
- Disturbance / variety regulated: unsupported game layouts, context limits and task-relevant reference information.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: plugin/skill loading, retrieval, compaction and project-local adapter authoring.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [skills/game-translation/references/custom-adapters.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/references/custom-adapters.md); [skills/game-translation/SKILL.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/SKILL.md); [desktop/application/skills.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/skills.py); [desktop/runtime/context/compaction.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/runtime/context/compaction.py); [desktop/plugin_catalog.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/plugin_catalog.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: project adapter workflow, skill/plugin roots, retrieval instructions and context management.
- Plausible first-party paths checked: future external distinctions generating reusable capability options and returned adoption, including parent adaptation.
- Why no material first-party path remains: the adapter workflow solves the current project's layout under explicit task scope and pins a single project file; generic extension support and later discussion of upstream reuse do not supply a prospective capability decision loop.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy adjudication-return path is supplied.
- Disturbance / variety regulated: ordinary user task scope, prompt presets, permissions and plugin enablement.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: prompt configuration, user questions/steering, per-profile instructions and tool allowlists.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [desktop/prompts/config.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/prompts/config.py); [desktop/prompts/assembly.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/prompts/assembly.py); [desktop/application/subagent_profiles.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/application/subagent_profiles.py); [desktop/tools/contracts.py](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/desktop/tools/contracts.py); [skills/game-translation/SKILL.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/skills/game-translation/SKILL.md); [README.en.md](https://github.com/S0ra233/Sora-Harness/blob/cbfddafca44ff18f80181943ce17ba1d271ed7a6/README.en.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: prompt layers/presets, role configuration, questions/steering, plugin/tool settings and task-scope rules.
- Plausible first-party paths checked: a genuine identity-level dispute reaching legitimate ultimate authority and returning binding policy into operation.
- Why no material first-party path remains: editing presets or clarifying a task is external configuration/ordinary user direction; no first-party identity-level issue, ultimate decision and authoritative return transaction is supplied.

## Recursion

Nested child processes, model profiles and shared workspace leases do not establish a viable recursive metasystem for each task.

## Variety and escalation

Task/child IDs, package versions, file receipts and tool errors preserve operational distinctions. Uncertain translations return to the main actor/user; unknown mutation outcomes stop further writes. Those channels do not independently prove S3, S5 or algedonic authority.

## Evidence gaps

No provider-backed or game E2E run. S2=A is source-supported in the explicitly enabled first-party collaborative mode; single-agent mode need not exercise it. Optional role configuration does not donate an independent audit or whole-system-control actor. Project-local adapters are not automatically S4.
