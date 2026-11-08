---
harness_id: markov-harness
project_name: markov-harness
repository: https://github.com/vokramd/markov-harness
review_ref: 6ffac34f74e6ee9c1e93cdff145c8d7656a0d769
reviewed_at: 2026-11-08
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# markov-harness

## Review boundary

- System in focus: the first-party declarative Markov workflow and Python scripts forming an interactive local coding agent, with its packaged launcher and optional separately invoked specialist subagent workflow.
- Purpose and identity: a small Claude Code-like coding/tool harness with model-selected commands/files, permission controls, isolated sessions, instructions and long-term project/user memory.
- Relevant environment: a user worktree mounted into rootless Podman, model relay, host's local approval decisions, developer-authored tool and hook settings, files, subprocesses and external Markov runtime.
- Standard-distribution boundary: `bin/harness` launches `markov run /harness` using a separately built Markov binary, Podman and a relay key; the repository supplies the **actual workflow behavior** but not the external Markov engine or LLM. A real configured distribution is credited despite those declared dependencies.
- Credited operating / distribution surfaces: `meta.yaml`, `vars.yaml`, `vars/prompts.yaml`, `vars/tools.yaml`, `workflows/main.yaml`, `turn.yaml`, `agent_step.yaml`, `subagent_step.yaml`, `agent/run.yaml`, `tools/*.yaml`, `extract/*.yaml`, first-party `scripts/*.py` and `bin/harness`.
- Adjacent first-party surfaces excluded from ownership: tests, rendered demo recording/GIF, example skill/agent instructions, documentation and Containerfile construction steps; externally built `markov` runner, Podman and `model-relay` are supporting dependencies, not first-party organizational functions.
- First-party operating / deployment modes considered: regular interactive agent run, `approve=auto` and rule/hook-governed approvals, optional sequential agent-tool or `/agent` child invocation, context compaction, per-project instruction/memory snapshot, optional separate memory extraction after a turn.
- Recursion level: a single coding harness operating in one user workdir/session; its subagent call is an S1 delegation, not an independently viable nested organizational unit. Saved sessions do not automatically form a portfolio metasystem.
- Reviewed revision: `vokramd/markov-harness@6ffac34f74e6ee9c1e93cdff145c8d7656a0d769`.
- Observation date: 2026-11-08. Generated/current Profile `0.2.4`, Methodology `0.3.7`.

## Repository architecture

The package is a genuine directory workflow, not just a README wrapper: `main` snapshots session instructions/memory/skills and loops `turn`; `turn` records a user prompt and repeats `agent_step`; `agent_step` sends a Messages API request containing the first-party tool schema and history, parses the model's selected tool calls, runs permission gates, executes real read/edit/bash or an `agent.run` child and feeds results into subsequent model requests. The launcher bind-mounts workflow files and `/work` into Podman and calls an external Markov runner. Permission scripts and memory/history serialization are first-party, while the Markov workflow executor and model relay are not ([launcher](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/bin/harness#L1-L130), [top-level workflow](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/main.yaml#L1-L100), [model/tool workflow](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/agent_step.yaml#L1-L205)).

## S1 — Operations

- State: A
- Function: interactive model-selected repository reading, editing, shell execution and bounded specialist delegation in response to user coding requests and tool feedback.
- Disturbance / variety regulated: unfamiliar workspace files, command failures, tool denials and evolving coding subtasks within a user session.
- Decisive decision or feedback right: the configured LLM chooses substantive tool invocations and next action after reading real results; a child model separately selects its own allowed tools for a bounded delegated task.
- Decision owner: main model/agent and, in the supported agent-tool mode, an explicitly invoked specialist model with its own session and tool permissions.
- Supporting / enforcement mechanisms: declarative `repeat` steps, first-party history assembly, read/edit/bash tools, `hooks.py` gate, optional human approval, rules, container boundary, context compaction and session/memory snapshot.
- Closure path: model tool-use blocks enter gate and first-party tool workflows; outputs are recorded as tool-result content in the session; next `agent_step` call receives updated history and may correct/retry or finish. Child `agent.run` returns a tool result to main agent.
- Boundary reachability: `bin/harness` invokes Markov with the shipped workflow; normal `main -> turn -> agent_step` and optional model-produced `tools.agent -> agent.run -> subagent_step` are implemented, not only illustrated in a test.
- Why this is / is not agent-owned: model-dependent choice of tool, arguments and continuation is decisive S1 cognition; predetermined Markov repeat/gates constrain it but do not select individual coding actions.
- Evidence: [normal turn loop](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/turn.yaml#L135-L200), [model/tool feedback](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/agent_step.yaml#L35-L200), [delegated model loop](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/subagent_step.yaml#L1-L155), [tool return](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/tools/agent.yaml#L1-L23).
- Basis: first-party workflow/source evidence and unit tests; no live model-relay E2E in this assessment.
- Confidence: high for the installed S1 model/tool return wiring; not an empirical model-success measurement.
- Caveats: a separately installed external Markov engine, Podman and relay credentials are required. The bundled demo and provider claims are not promoted into independent verified operating evidence.

## S2 — Coordination

- State: —
- Function: no credited inter-S1 disturbance-specific mutual adjustment with corrective feedback among independent specialists.
- Disturbance / variety regulated: possible tool/workspace clashes between separately invoked specialist agents, but no first-party coordination of those clashes is established.
- Decisive decision or feedback right: no distinct mediation function shown; the main agent selects delegation and the workflow runs child calls one at a time.
- Decision owner: main agent owns task assignment as part of its S1, and deterministic workflow settings own read-only parallelism/mutating serialization; no independent S2 decision owner is evidenced.
- Supporting / enforcement mechanisms: `run_readonly` concurrency 4, `run_mutating` concurrency 1 and sequential `run_agents`, per-tool permission checks and shared worktree.
- Closure path: each child completes and reports back to the main model as a tool result; no unresolved conflict representation, peer settlement, reallocation or collision-specific adjustment drives another independent S1 unit.
- Why this is / is not agent-owned: generic delegation, deterministic serial execution and permissions may avoid some collisions mechanically but do not establish VSM S2's interference/attenuation/feedback relation.
- Evidence: [serialized subagent calls](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/agent_step.yaml#L134-L196), [subagent result flow](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/agent/run.yaml#L1-L77), [README explicitly one-at-a-time](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/README.md#L261-L292).
- Basis: source-level workflow modes and supported subagent documentation.
- Confidence: high for lack of credited coordination within inspected shipped modes.
- Caveats: this does not deny that serial execution is a valuable safety measure; it is not evidence of an independently agent-owned S2 function.

### Absence scope

- Surfaces inspected: first-party main, turn, agent_step, subagent_step, tools.agent, agent.run, tools, agents.py and shipped child-agent descriptions.
- Plausible first-party paths checked: multiple read-only calls in one reply, sequential mutating calls, `agent` delegation, `/agent` direct dispatch, approval hooks and shared memory/worktree.
- Why no material first-party path remains: observed paths are one S1's internal tools or strictly serial child task decomposition; they lack an identified inter-agent conflict, dedicated attenuating feedback and subsequent peer adjustment.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-harness current control over multiple independently committed S1 cells is established beyond the main agent's task-level delegation.
- Disturbance / variety regulated: tool budget, blocked commands, long transcript, subagent termination and user approvals, all at session-operation level.
- Decisive decision or feedback right: main model may call a child tool, while human may approve an individual edit/command; no separate whole-system controller can evaluate current multi-S1 commitments and reallocate them.
- Decision owner: main task S1 and deterministic workflow limits, not a demonstrated whole-system S3 actor.
- Supporting / enforcement mechanisms: `max_tool_rounds`, `max_turns`, `approve` rules, session continuation and summary compaction.
- Closure path: child result folds back into main transcript, tool denial folds into the same agent, and compaction changes that agent's context; there is no cross-cell S3 resource/commitment closure.
- Why this is / is not agent-owned: main-agent operational planning is not automatically promotion to autonomous S3; approval per operation is not parent whole-system control.
- Evidence: [single-session orchestration](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/main.yaml#L1-L100), [subagent run-and-return](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/agent/run.yaml#L1-L77), [session settings](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/vars.yaml#L1-L140).
- Basis: first-party workflow and task/agent mode inspection.
- Confidence: medium-high within reviewed distribution.
- Caveats: an operator could externally run several instances or coordinate them; such an added organization is not contained in the pinned harness.

### Absence scope

- Surfaces inspected: top-level workflow, turns, child agents, permissions/approval path, config and session persistence.
- Plausible first-party paths checked: user command approval, `agent` tool, subagent ceilings, compaction triggers and file-backed session continuity.
- Why no material first-party path remains: these operate one task or return a child result to the caller; no first-party fleet/commitment overview with an authoritative cross-worker current decision is present.

## S3* — Complementary audit

- State: —
- Function: no separate independent completed-work reality audit whose finding closes into corrective operational control.
- Disturbance / variety regulated: hallucinated file updates or false task completion claims would require independent verification, but reviewed validation paths do not own such audit.
- Decisive decision or feedback right: permission gate checks whether a proposed command/edit may run, and PostToolUse hooks may return suggestions; no default reviewer independently measures final claimed deliverables.
- Decision owner: user approval and developer-authored hook rules for pre/post tool constraints; neither is an independent auditor of the task's outcome.
- Supporting / enforcement mechanisms: `hooks.py`, edit diff and validation, tool-result feedback, local script tests, optional model memory extraction.
- Closure path: gating sends allow/deny to normal tool execution; memory extraction summarizes conversation history to memory files, not verified real results with independent corrective verdicts.
- Why this is / is not agent-owned: pre-execution policy checking and transcript-derived memory are not a distinct reality-reading audit of the completed S1 operation.
- Evidence: [tool gate and hooks](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/agent_step.yaml#L120-L227), [edit planning](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/tools/edit_file.yaml#L1-L125), [memory extraction workflow](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/extract/step.yaml#L1-L120).
- Basis: code path and self-test review.
- Confidence: high for absence of a first-party standalone reviewer within inspected modes.
- Caveats: a user might install custom hooks performing validation; an external customized hook is not an established first-party independent audit owner.

### Absence scope

- Surfaces inspected: permission matching, hook pre/post/stop paths, tool-error feedback, `edit_file`, example demos, extraction model pass and tests.
- Plausible first-party paths checked: PostToolUse command hooks, pre-tool approval, edit string uniqueness/diff preview, extracted memories, unit and E2E development tests.
- Why no material first-party path remains: checked paths inspect proposed tool inputs, status or transcript history, or belong to developer-only tests; no separate agent/evaluator reads actual completed output and returns a corrective reality judgment to current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed first-party external-environment intelligence and prospective organizational adaptation strategy, beyond retrieval/persistence of task memories.
- Disturbance / variety regulated: future unfamiliar tasks/user preferences, which the memory files might help with but do not constitute an agent-selected organizational strategy loop.
- Decisive decision or feedback right: model may extract memorable preferences/facts from past conversation, but no explicit future environmental option is selected, governed and enacted as a strategic adaptation.
- Decision owner: ordinary main task model/optional extraction model for memory text; operator/developer authors permanent workflows, tools and settings.
- Supporting / enforcement mechanisms: `extract.memories`, `extract.step`, `memory.py` index and snapshot, user/working-directory instructions, skills lookup and context compaction.
- Closure path: extraction stores a fact file and future session prompt may incorporate its index; this is persistent S1 context, not a wider outside-and-then metasystem decision returned into changed organizational capability.
- Why this is / is not agent-owned: retained instructions/memories can influence later S1 but have no evidenced externally oriented prospective scanning, alternative selection or strategy implementation closure.
- Evidence: [memory extraction trigger](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/turn.yaml#L186-L199), [extract fork and model pass](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/workflows/extract/memories.yaml#L1-L38), [persistent memory context](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/scripts/memory.py#L1-L150).
- Basis: workflow and storage/permission paths.
- Confidence: medium-high, with the memory mechanism reviewed as plausible false positive.
- Caveats: capability to modify arbitrary project files does not by itself establish S4; no change to the first-party configured harness is automatically enacted by extracted facts.

### Absence scope

- Surfaces inspected: memory extraction/recall, skill and agent type lists, automatic compaction, system prompt and user instruction reload, tool/hook settings.
- Plausible first-party paths checked: extraction fork, session-future memory influence, skill registry, external model selection and configuration changes.
- Why no material first-party path remains: inspected paths are ordinary context persistence or user-authored customization without independent external-future option generation and an implementation feedback loop.

## S5 — Policy and identity

- State: —
- Function: no distinct legitimate ultimate policy/identity decision authority is closed inside the evaluated agent harness.
- Disturbance / variety regulated: conflicting system purposes or durable constitution revisions would require a policy-identity adjudicator; source instead installs a fixed identity and user-written instruction precedence.
- Decisive decision or feedback right: no model or parent governance agent can authoritatively choose a constitutional identity for the harness; the user edits prompt/config/CLAUDE.md settings outside the agent.
- Decision owner: installer/operator and original prompt author define static identity; normal agents select code actions within that envelope.
- Supporting / enforcement mechanisms: `vars/prompts.yaml` static `client_identity`/`system_prompt`, `instructions.py` snapshots and folder precedence, `settings.py` permission rules, user approvals.
- Closure path: owner-edited instruction/settings text may be loaded in a later session, but no operating first-party identity-level adjudication and authoritative change cycle is established.
- Why this is / is not agent-owned: routine permission rules and human approval of one command are operational constraints, not ultimate policy S5; static instructions are necessary identity input but not a decision owner on their own.
- Evidence: [static prompt variables](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/vars/prompts.yaml#L1-L115), [instruction snapshot](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/scripts/instructions.py#L1-L145), [permission policy](https://github.com/vokramd/markov-harness/blob/6ffac34f74e6ee9c1e93cdff145c8d7656a0d769/scripts/settings.py#L1-L146).
- Basis: source-level prompt/authority and instruction path review.
- Confidence: medium-high within first-party runner configuration.
- Caveats: parent-maintainer GitHub governance or a user's own policy choices are outside the installed execution boundary.

### Absence scope

- Surfaces inspected: fixed agent identity, config variables, first-party instruction loader, user/workdir files, permission editing and hook definitions.
- Plausible first-party paths checked: persistent `CLAUDE.md`, user setting rewrites, dynamic skill and agent type loading, approval `a` saved rule, Stop hooks.
- Why no material first-party path remains: none supplies an independent legitimate ultimate-policy decision process with authoritative closed return to harness identity; saved per-command permissions are not constitutional policy arbitration.

## Recursion

The normal main agent can create a separate single task child model session through the `agent` tool or `/agent` command; it returns the child answer as a tool result. Subagents are expressly serial, have bounded permission lists and cannot spawn further subagents. No child has its own separate S2–S5 metasystem or independent viable recursion evidenced.

## Variety and escalation

Read/edit/bash and special-purpose child agent types amplify S1 action variety; rootless container, deny/ask/allow permission rules, edit validation, explicit approval and per-turn limits attenuate execution risk. Pre/PostToolUse hooks return denials or additional context to the main model. Once a session grows, a separate compaction pass summarizes context. Missing Markov binary, relay key or container runtime blocks E2E; these external prerequisites do not create a first-party metasystem.

## Evidence gaps

- The external `markov` engine, `model-relay` and Podman integration were not executed: first-party `python3 tests/test_scripts.py` passed **20/20** local unit tests; credentialed E2E tests require the documented relay/key/runtime environment.
- The bundled cast/GIF is illustrative and not treated as this assessment's observed credentialed model run.
- First-party async concurrency is limited to tool calls; independently reasoned subagent calls are serial. No peer conflict-control path was found.
- User/project memory persistence is not automatically S4, and user-authored prompt/settings do not automatically supply S5.
