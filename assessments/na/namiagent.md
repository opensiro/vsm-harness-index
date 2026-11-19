---
harness_id: namiagent
project_name: NamiAgent
repository: https://github.com/aa1143/NamiAgent
review_ref: 13cdae0ac62571fc4e6e320d31651a01353de489
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# NamiAgent

## Review boundary

- System in focus: the shipped lesson-11 local assistant composition, including its CLI, Telegram/scheduled mode and default web adapter.
- Purpose and identity: complete user-selected local file, shell and information tasks with a model-driven tool loop.
- Relevant environment: a bounded workspace, user requests and permission answers, optional MCP servers/web information, model provider and Telegram.
- Standard-distribution boundary: executable lessons/lesson-11 modules and web/app.py importing that composition; historical lesson snapshots are explanatory predecessors.
- Credited operating / distribution surfaces: agent.py, tools.py, permissions.py, subagent.py, context.py, skills.py, memory.py, planning.py, scheduler.py, bot.py, mcp_client.py and the web adapter.
- Adjacent first-party surfaces excluded from ownership: tutorial comparisons of external products, scripted web demo, fake-model tests and GitHub CI; they do not donate external harness functions.
- First-party operating / deployment modes considered: interactive CLI, default lesson-11 web UI, Telegram messages and preauthorized scheduled/heartbeat runs; optional read-only parallel explorers and serial worker delegation.
- Recursion level: one assistant contribution cell with subordinate task workers; the OSS development project is outside the assessed system.
- Reviewed revision: `13cdae0ac62571fc4e6e320d31651a01353de489`.
- Observation date: 2026-11-19.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

This is a runnable educational Python assistant rather than only a prompt tutorial. Session holds messages, a permission manager and plan; run/_loop repeatedly calls a configured OpenAI-compatible model, dispatches selected tools and returns tool results to subsequent model calls. File/shell/web tools, optional MCP and skill loading provide actions. Context compaction and JSON sessions preserve working state. The web adapter imports the lesson code; Telegram supplies a whitelist, confirmations and scheduled sessions. Side-effect permission remains human or preauthorized, while the model chooses the operational solution.

delegate creates a separate nonpersistent Session with a depth limit and result truncation; delegate_parallel admits at most three read-only explorers. Permission/tool filtering constrains children, and MCP serializes a shared request stream. Memory entries are proposed by the model, individually confirmed and loaded at a later session start. Planning is an operational checklist and optional human-approved read-only phase. Maintainer tutorial/CI activity is not runtime governance.

Primary implementation and explanatory sources: [loop](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/agent.py), [subagents](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/subagent.py), [permissions](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/permissions.py), [memory](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/memory.py), [planning](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/planning.py), [scheduler](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/scheduler.py), [bot](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/bot.py), [context](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/context.py), [MCP](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/mcp_client.py), [coordination rationale](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/docs/09-subagents.md), [web mode](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/web/app.py).

## Operational model

The main assistant and delegated explorers/workers are operational units producing task answers or workspace effects. The model chooses tools and follow-up actions; permissions, hard limits, dispatch, storage and scheduling enforce or transport those choices. Parents approve risky actions, not an evidenced system-wide current-control, strategic-adaptation or identity-policy transaction. Scheduled jobs are another operational entry, not automatically another VSM recursion.

## S1 — Operations

- State: A
- Function: transform an assigned local task into an answer or permitted file/command outcome.
- Disturbance / variety regulated: unknown file contents, tool errors, task-specific choices and results requiring further action.
- Decisive decision or feedback right: choose the next tool/arguments or finish after observing returned results.
- Decision owner: the configured assistant model; delegated models own their bounded investigations.
- Supporting / enforcement mechanisms: tool registry, permissions, maximum steps, context cleanup, session persistence and provider calls.
- Closure path: _loop appends each tool result and queries the model again until an answer or bounded stop.
- Boundary reachability: CLI main, web adapter and Telegram bot call the shipped run function; no custom agent implementation is needed.
- Why this is / is not agent-owned: removing model selection leaves only dispatch and limits, not the task-dependent choice of actions. Per-action human permission narrows the available actions without choosing the full solution.
- Evidence: [run/_loop and Session](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/agent.py), [tools](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/tools.py), [web entry](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/web/app.py).
- Basis: structural.
- Confidence: high.
- Caveats: source inspection, not live model execution; side-effect permissions and scheduler preauthorization remain explicit constraints.

## S2 — Coordination

- State: C
- Function: prevent shared-workspace write interference and overlapping confirmation/MCP exchanges between child work cells.
- Disturbance / variety regulated: concurrent children writing the same workspace or simultaneously interacting with the shared confirmation/request channel.
- Distinct S1 units: parent assistant and the distinct delegated child Sessions.
- Inter-S1 disturbance: docs/09-subagents.md explicitly motivates serial writes versus parallel reads; simultaneous confirmations and MCP request streams also compete for one channel.
- Attenuating coordination relation: delegate_parallel supplies read-only toolsets; write-capable delegate is synchronous; MCP client locks its request/reply stream.
- Feedback into subsequent S1 behaviour: disallowed tools yield an error instead of a write; child results join before the parent resumes and selects subsequent work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the read/write asymmetry and shared-channel locking address identified interference, independently of merely creating child contexts.
- Decisive decision or feedback right: select/revise the conflict-avoidance arrangement and permitted concurrency/tool classes.
- Decision owner: the developer-supplied fixed coordination policy; no installed autonomous coordination actor is established.
- Supporting / enforcement mechanisms: toolset filtering, MAX_PARALLEL, synchronous future collection and MCP stream lock.
- Closure path: filtered child tool access and serialized shared exchanges constrain subsequent child action; parent receives joined outcomes.
- Boundary reachability: the imported subagent module registers these specific tools in the ordinary lesson-11 loop.
- Why this is / is not agent-owned: the main model chooses operational delegation, but the conflict response itself is fixed by the constructor. Autonomous revision/coordination authority would require composition.
- Evidence: [coordination design rationale](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/docs/09-subagents.md), [toolsets and parallel runner](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/subagent.py), [MCP client](https://github.com/aa1143/NamiAgent/blob/13cdae0ac62571fc4e6e320d31651a01353de489/lessons/lesson-11/mcp_client.py).
- Basis: structural.
- Confidence: medium.
- Caveats: C is limited to the evidenced first-party interference-control path; it does not credit an autonomous negotiator, arbitrary worker cooperation or workspace isolation not supplied here.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-cell resource/commitment regulation path established.
- Disturbance / variety regulated: whole-cell operational contention would be relevant, but the shipped path exposes local task progress and fixed limits.
- Decisive decision or feedback right: no supplied whole-system discretionary resource/priority intervention owner.
- Decision owner: not established for S3; developer limits and human task approvals remain distinct.
- Supporting / enforcement mechanisms: step/context bounds, scheduler task cap, local plan and permission checks.
- Closure path: these constrain individual runs; no evidenced whole-cell bargaining/accountability loop returns a current-control decision.
- Why this is / is not agent-owned: task decomposition and plan edits do not themselves establish S3.
- Evidence: agent.py, planning.py, scheduler.py and bot.py linked above.
- Basis: structural.
- Confidence: medium-high.
- Caveats: users can manually choose tasks or extend the runtime; neither is credited as shipped S3.

### Absence scope

- Surfaces inspected: main loop, scheduler/bot job lifecycle, plan and permissions, subagent result path.
- Plausible first-party paths checked: scheduled-task list/cancel, parent delegation, plan submission and maximum steps/concurrency as possible current-control paths.
- Why no material first-party path remains: they expose per-task execution, deterministic caps or ordinary approvals without a whole-system current view coupled to discretionary shared-resource/commitment control; no qualifying parent S3 return is supplied.

## S3* — Complementary audit

- State: —
- Function: no packaged complementary audit of an operational claim.
- Disturbance / variety regulated: unreliable child answers could need audit, but the distribution provides general exploration.
- Decisive decision or feedback right: no audit-specific independent judgment and governed corrective return supplied.
- Decision owner: not established.
- Supporting / enforcement mechanisms: separate child contexts, logs, fake-model tests and stored transcripts.
- Closure path: child conclusions return to ordinary production; no distinct audit-to-control loop is installed.
- Why this is / is not agent-owned: a separate context and the ability to ask for review do not supply an S3*-specific actor/constructor.
- Evidence: subagent.py, context.py, tests/test_subagent.py and docs/09-subagents.md at the pinned revision.
- Basis: structural.
- Confidence: medium-high.
- Caveats: tutorial discussion of reviewing code is not borrowed as autonomous audit.

### Absence scope

- Surfaces inspected: child role prompt and spawning, result return, context/session storage, tutorial rationale and tests.
- Plausible first-party paths checked: clean-context child inspection, parallel investigation and routine validation as candidate audit paths.
- Why no material first-party path remains: no function-specific claim challenge, complementary evidence choice and corrective-control relation is packaged beyond generic delegated S1 investigation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material externally/prospectively oriented adaptation loop supplied.
- Disturbance / variety regulated: changing user preferences or future-useful facts can be retained, but are not tied to prospective capability options.
- Decisive decision or feedback right: no function-specific adaptation judgment/return established.
- Decision owner: model proposes generic memory; user confirms entries, neither thereby owns an established S4 loop.
- Supporting / enforcement mechanisms: fetch_url, skill loading, memory file, session search, scheduled prompts and context summaries.
- Closure path: confirmed memory reappears in later prompts; no supplied external distinction → prospective option → current-capability adaptation relation.
- Why this is / is not agent-owned: generic retention, fetching and task planning do not establish S4.
- Evidence: memory.py, skills.py, scheduler.py and context.py linked above.
- Basis: structural.
- Confidence: medium-high.
- Caveats: externally supplied skills/research jobs could add behavior outside this supplied organizational path.

### Absence scope

- Surfaces inspected: durable memory, skill discovery/loading, context compaction, scheduled/heartbeat inputs and planning.
- Plausible first-party paths checked: confirmed future-useful notes, recurring fetch jobs and skill loading as possible base or parent adaptation modes.
- Why no material first-party path remains: these are generic operational information mechanisms without a first-party prospective adaptation owner, options evaluation and function-specific return into capability; user confirmation alone is not parent S4.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy resolution path established.
- Disturbance / variety regulated: ordinary action risk and task-plan permission are regulated; unresolved identity or S3–S4 policy tension is not.
- Decisive decision or feedback right: no supplied identity-policy escalation and authoritative returned decision.
- Decision owner: user owns ordinary approvals; developer owns fixed permission rules, without an established S5 function.
- Supporting / enforcement mechanisms: BASE_SYSTEM, workspace bounds, deny patterns, AGENTS.md, tool confirmation and preauthorization.
- Closure path: approved tools/plans execute within existing boundaries; no identity/ultimate-policy transaction is returned to govern future operation.
- Why this is / is not agent-owned: static instructions and final say on an action are not sufficient S5 evidence.
- Evidence: permissions.py, planning.py, skills.py and scheduler.py linked above.
- Basis: structural.
- Confidence: high.
- Caveats: governance of the educational repository belongs to another system boundary.

### Absence scope

- Surfaces inspected: base/system instruction assembly, permission hard limits/confirmation, plan approval, memory confirmation, Telegram whitelist and scheduled preauthorization.
- Plausible first-party paths checked: human confirmation and persistent project/memory instructions as possible parent-policy channels.
- Why no material first-party path remains: no identity/ultimate-policy issue is routed to a legitimate authority and returned as a governing resolution; the paths close operational permission or fact retention only.

## Distributed OSS parent arrangement

Individual users may operate local copies. No shared project-recursion parent loop is evidenced; maintainer changes and CI do not become runtime S5.

## Self-hosted and non-human modes

CLI, web and Telegram are local operator modes. Human tool approval and unattended preauthorization are explicit, but do not supply function-specific S3/S4/S5 parent modes.

## Recursion

Subordinate sessions have bounded tasks and isolated messages, not evidenced viable metasystems. Nesting is capped at one child level.

## Variety and escalation

The model handles local tool/task variety. Risky tools ask the local user; denied actions become feedback, and step/context/tool output bounds attenuate information. Truncation can lose decisive details; errors and approvals are not automatically algedonic or S5.

## Evidence gaps

No live model, Telegram or browser session was executed. The assessment uses the complete pinned source tree and inspected runtime/tutorial/test paths; it does not establish performance, adversarial robustness or independent semantic agreement.
