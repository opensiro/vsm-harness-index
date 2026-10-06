---
harness_id: marvis
project_name: Marvis
repository: https://github.com/meloer101/Marvis-codingAgent
review_ref: 3363617c15bdd2f773ef169fc5a44dd321e631a5
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

# Marvis

## Review boundary

- System in focus: the first-party Marvis coding-agent runtime at frozen revision 3363617c15bdd2f773ef169fc5a44dd321e631a5, including its ReAct model/tool loop, coding tools, permissions/sandboxing, Plan mode, session persistence/compaction, cross-session memory, Skills, MCP integration, configured subagents, telemetry and CLI/TUI/web/server execution surfaces.
- Purpose and identity: perform software-engineering work in a user project through one primary model-backed coding loop that can read/edit/run, load skills, invoke external MCP tools, consult persistent memory and dispatch bounded fresh-context subagents.
- Relevant environment: user goals and approvals, repository/workspace files, shell/test/tool results, provider/model responses, persisted session and memory files, configured project/user agents and skills, MCP servers and operator cancellation.
- Standard-distribution boundary: shipped Marvis packages/core, CLI/TUI/web/server/protocol surfaces and bundled first-party agents/skills. External model endpoints, MCP servers, host shell/toolchain and user/project-authored agent/skill definitions are dependencies or configuration and cannot donate uninstantiated organizational functions.
- Credited operating / distribution surfaces: packages/core/src/agent, tools, permissions, context, memory, subagents, skills, MCP, provider and telemetry; packages/core/agents bundled definitions; CLI/TUI/web/server session drivers and Plan-mode control.
- Adjacent first-party surfaces excluded from ownership: eval/benchmark harnesses, cassettes, CI/release/update infrastructure, docs/plans and user/project extensions unless the corresponding behavior is instantiated by shipped runtime code.
- First-party operating / deployment modes considered: one-shot CLI, REPL/TUI, browser UI/server, Plan mode with human approval, built-in explore/plan subagents, configured user/project subagents, persistent memory, MCP/skills, supported local/hosted provider routing and permission modes.
- Recursion level: one Marvis coding session. The primary model-backed coding loop is the operative S1. Built-in explore/plan subagents are bounded read-only support agents; configured external/user-defined subagents are not allowed to donate higher VSM functions absent first-party instantiated decision rights.
- Reviewed revision: 3363617c15bdd2f773ef169fc5a44dd321e631a5.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Marvis ships a first-party ReAct AgentLoop that repeatedly calls the selected model, collects tool calls, permission-gates them, executes safe read-only calls in parallel and serializes state-changing work. AgentSession wraps that loop with provider routing, permission policy, compaction, session persistence, Skills, persistent memory, MCP and subagent discovery.

The task tool dispatches a named subagent in a fresh context and returns only its final report. Multiple task calls in one parent turn may run concurrently. The built-in explore/plan agents are read-only; project/user agent definitions can extend the roster, but those external definitions are configuration and cannot be credited as standard first-party S2/S3/S3* constructors.

Marvis also provides a persistent memory tool with read/write/forget/list actions. The primary agent may stage project/global notes that flush at session end and later appear through a manifest for on-demand recall. This is stronger than passive transcript persistence, but at the frozen boundary it still constitutes retained context/experience reuse: no distinct outside-and-prospective adaptation function develops organizational options and returns them into current S3.

## Operational model

The primary model owns open-ended implementation, investigation, verification and delegation choices. Permissions, tool serialization, compaction, budgets, retries and Plan-mode approval constrain execution. Subagents solve bounded prompts in isolation and return summaries; the parent cannot inspect or reallocate their live internal work through a whole-system control surface.

Cross-session memory lets the same operational agent retain facts, preferences and collaboration lessons. That continuity can improve later S1 behavior, but Methodology 0.3.6 explicitly does not promote persistence or memory reuse to S4 without the external/future distinction, adaptation-option generation and return-to-current-capability witness.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify software through model-selected repository, shell, browser/web, memory, skill and MCP tool actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, test/build/tool failures, provider/model differences, context pressure, permission constraints, user feedback and bounded delegated research/planning.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret evidence, decide whether to load skills/recall memory/delegate a subtask, revise the implementation and decide when the task is complete.
- Decision owner: the active model-backed Marvis coding agent.
- Supporting / enforcement mechanisms: AgentLoop, ToolRegistry, permission engine, provider router/retries, context compaction, session persistence, budgets, MCP/skills and subagent task execution.
- Closure path: user request → model chooses direct coding/tool work or bounded support delegation → first-party runtime executes and returns evidence → model revises/validates work → model ends the turn.
- Boundary reachability: one-shot, REPL/TUI and web/server paths instantiate the same first-party AgentSession/AgentLoop machinery.
- Why this is / is not agent-owned: deterministic runtime code transports, limits and records the work, but removing the model removes the open-ended engineering decisions.
- Evidence: [README.md](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/README.md); [packages/core/src/agent/loop.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/agent/loop.ts); [packages/core/src/agent/session-runner.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/agent/session-runner.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: user approval can constrain shell/write execution in ask/plan modes, but the user is not supplying the substantive coding decision.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established.
- Disturbance / variety regulated: no concrete interference among distinct standard-distribution operational S1 units is placed under a separate coordination feedback loop.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: read-only tool parallelism, write serialization, task-call concurrency limits, permission checks and isolated subagent context prevent or bound execution hazards but do not coordinate peer operational units.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: built-in explore/plan subagents do not own competing write commitments; user/project-defined subagent capabilities are configurable extensions and cannot establish first-party S2 by possibility alone.
- Evidence: [packages/core/src/agent/loop.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/agent/loop.ts); [packages/core/src/subagents/task-tool.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/subagents/task-tool.ts); [packages/core/agents/explore.md](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/agents/explore.md); [packages/core/agents/plan.md](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/agents/plan.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: several task calls may run concurrently, but concurrency and isolation are mechanisms; no distinct peer-S1 interference/attenuation/feedback witness is established.

### Absence scope

- Surfaces inspected: built-in subagent definitions, task-tool concurrency, subagent tool filtering, AgentLoop tool scheduling, permissions, session state and configured agent discovery.
- Plausible first-party paths checked: shared-write conflict arbitration, worktree/file leases, peer scheduling feedback, dependency management and autonomous conflict resolution.
- Why no material first-party path remains: standard built-in children are bounded read-only support agents and no first-party peer operational collision loop is instantiated.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established at the declared session recursion.
- Disturbance / variety regulated: no separate actor owns a live portfolio of S1 commitments with authority to reprioritize, reallocate or terminate individual operational units based on a whole-current view.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: task dispatch, AbortSignal propagation, budgets, Plan-mode approval, todo state, session notices and generic run cancellation constrain current execution but do not create whole-system current control.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the parent model may dispatch several subagents and later consume their final reports, but the task tool exposes no live child status/reallocation/kill surface; it waits for completion and returns only final output.
- Evidence: [packages/core/src/subagents/task-tool.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/subagents/task-tool.ts); [packages/core/src/subagents/run.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/subagents/run.ts); [packages/core/src/agent/control.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/agent/control.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: human approval to exit Plan mode and whole-run abort are legitimate safeguards, but approval/stop alone does not satisfy the Methodology 0.3.6 whole-current S3 constructor.

### Absence scope

- Surfaces inspected: task lifecycle, AgentSession notices, AbortSignal propagation, Plan-mode control, todo state, session runner, TUI/web driving surfaces and runtime budgets.
- Plausible first-party paths checked: worker dashboard, selective live child cancellation/retry, current resource reallocation, whole-run commitment reprioritization and model-owned supervisor loop.
- Why no material first-party path remains: available mechanisms are dispatch/wait/final-report or generic run control rather than substantive whole-current regulation.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no separate first-party reviewer is automatically instantiated with independent evidence access and a corrective return path.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: the bundled code-review Skill instructs the same active agent how to review; tests/tool evidence, Plan mode and generic subagents can support verification but are not an independent audit constructor.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: loading code-review changes the current agent's instructions; it does not create a separate authorship-independent model instance. A user/project could define a reviewer subagent, but that external configuration cannot donate first-party S3*.
- Evidence: [packages/core/skills/code-review/SKILL.md](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/skills/code-review/SKILL.md); [packages/core/src/skills/skill-tool.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/skills/skill-tool.ts); [packages/core/src/subagents/discover.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/subagents/discover.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: self-review and generic configurable delegation are not promoted to complementary audit without the independent claim/evidence/feedback witness.

### Absence scope

- Surfaces inspected: code-review Skill, built-in agent roster, generic agent discovery, task-tool execution, Plan mode and eval/verification-adjacent runtime surfaces.
- Plausible first-party paths checked: dedicated reviewer agent, fresh second-model review, independent repository evidence channel and automatic repair gate.
- Why no material first-party path remains: no shipped first-party path instantiates a separate complementary auditor around ordinary coding output.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-prospective adaptation function is established.
- Disturbance / variety regulated: persistent user/project lessons are retained, but no separate function is shown sensing an external/future distinction, generating adaptation options and returning those options into present organizational capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent global/project memory, memory manifest, memory read/write/forget/list tool, session compaction, project instructions, Skills and provider/model configuration.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: the primary agent may choose to record a fact, preference or collaboration lesson that matters later and recall it in a later session; this is agent-owned memory maintenance, but Methodology 0.3.6 does not equate retained context/reuse with an S4 prospective adaptation loop.
- Evidence: [packages/core/src/memory/memory-tool.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/memory/memory-tool.ts); [packages/core/src/memory/store.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/memory/store.ts); [packages/core/src/context/memory.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/context/memory.ts); [README.md](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the memory mechanism is durable and agent-writable; the negative state is specifically because no function-specific external/future option-development → current-control return loop is established.

### Absence scope

- Surfaces inspected: persistent memory read/write/forget/list, memory discovery/manifest injection, session persistence/compaction, Skills, provider routing, MCP resources and Plan mode.
- Plausible first-party paths checked: autonomous environment scanning, future-oriented option generation, learned capability/model/tool reconfiguration and retained adaptation feedback into whole-current control.
- Why no material first-party path remains: inspected mechanisms retain or retrieve context and configure current execution but do not close the required prospective intelligence loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy issue is routed to an authoritative S5 owner and returned as governing runtime policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes/rules, Plan approval, system/project instructions, Skills, memory and provider/MCP configuration constrain operation but are not identity governance.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent operates under developer/user-authored policy and cannot authoritatively redefine Marvis's identity or ultimate operating principles.
- Evidence: [packages/core/src/permissions/engine.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/permissions/engine.ts); [packages/core/src/agent/control.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/agent/control.ts); [packages/core/src/agent/prompt.ts](https://github.com/meloer101/Marvis-codingAgent/blob/3363617c15bdd2f773ef169fc5a44dd321e631a5/packages/core/src/agent/prompt.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user approval and local policy configuration are legitimate authority over actions, but no identity/ultimate-policy decision/return loop is established.

### Absence scope

- Surfaces inspected: permission modes and rules, Plan-mode approval, system/project prompts, memory, Skills, model/provider/MCP configuration and session controls.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity governance, runtime policy-authoring actor and authoritative policy feedback.
- Why no material first-party path remains: all identified policy surfaces are operating constraints or externally authored configuration.

## Distributed OSS parent arrangement

The assessed organization is the running Marvis coding session, not the GitHub maintainer project. Repository contribution/release/eval governance is not imported as runtime S3/S4/S5 ownership.

## Self-hosted and non-human modes

Marvis can run with local or hosted OpenAI-compatible models and can be driven through CLI/TUI/web/server surfaces. The positive S1 claim is provider-neutral. No higher function is inferred from external MCP/provider capability or generic human approvals.

## Recursion

One primary Marvis coding session is the viable-unit boundary. The primary model/tool loop is S1. Built-in read-only explore/plan subagents are bounded support units and do not establish peer coordination/current control by their existence. Memory, permissions, Skills, MCP and session components are supporting mechanisms unless a higher function-specific decision loop is proven.

## Variety and escalation

S1 absorbs ordinary engineering variety and may use memory, skills, MCP or bounded subagents as tools. Permissions, budgets, retries, compaction and Plan approval regulate execution mechanics. No first-party S2/S3/S3*/S4/S5 loop is established at the frozen boundary.

## Evidence gaps

No ? state is required. The frozen repository directly exposes the primary loop, built-in subagent definitions, task lifecycle, memory tool, review Skill, permission/control and session surfaces needed for the positive S1 and bounded negative conclusions.
