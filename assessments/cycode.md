---
harness_id: cycode
project_name: CYCode
repository: https://github.com/ChaoYue0307/CYCode
review_ref: 8b09d0a8cbca739a8d5598127b00edd3e5955fb5
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
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CYCode

## Review boundary

- System in focus: the first-party CYCode TypeScript coding/research agent runtime at frozen revision `8b09d0a8cbca739a8d5598127b00edd3e5955fb5`, including its model/tool loop, built-in coding and research tools, permission/hook/sandbox machinery, session/checkpoint/context state, synchronous read-only explore subagents, and shared REPL/GUI/headless execution path.
- Purpose and identity: perform software-engineering and AI-research work in a selected project by turning user intent and project/research evidence into model-selected repository actions, experiments, literature queries, notebook/LaTeX operations and final responses.
- Relevant environment: the user task, selected project/workspace, source/build/test state, local experiments and logs, external literature/web services, model/provider responses, configured permissions/hooks/sandbox, durable session/context files and optional MCP servers.
- Standard-distribution boundary: CYCode's `Agent` loop, first-party core/research tools, explore subagent, permission gate, hooks, sandbox wrapper, context/config loading, sessions/checkpoints, skills and REPL/GUI/`exec` surfaces are inside. Model providers, arXiv/Semantic Scholar/web services, external MCP server implementations and supervising shell/CI loops remain dependencies or parent systems and cannot donate organizational functions.
- Credited operating / distribution surfaces: `README.md`; `src/agent/loop.ts`; `src/agent/subagent.ts`; `src/runtime.ts`; `src/exec.ts`; `src/permissions/permissions.ts`; `src/context/context.ts`; `src/config.ts`; `src/checkpoint/checkpoint.ts`; `src/tools/research/experiments.ts`; `docs/configuration.md`; `docs/loops.md`.
- Adjacent first-party surfaces excluded from ownership: `evals/`, `docs/evals.md`, repository tests and CI/release workflows are development/evaluation surfaces rather than actors wired into ordinary runtime control. External supervising loops shown in `docs/loops.md` are parent compositions around `cycode exec`, not internal CYCode organizational owners.
- First-party operating / deployment modes considered: interactive REPL, local GUI, headless `cycode exec`, default/acceptEdits/plan/bypass permissions, optional OS sandbox, durable session continuation, project/user context and skills, background experiment execution/status and synchronous `explore` delegation.
- Recursion level: one CYCode task/session around one selected project is the assessed organization. Tool calls, experiment processes and deterministic safety machinery are components. Read-only explore agents are subordinate investigation helpers that can run concurrently when the model emits a read-only batch, but the reviewed runtime does not establish a coordinated population of independently mutating operational S1 units.
- Reviewed revision: `8b09d0a8cbca739a8d5598127b00edd3e5955fb5`.
- Observation date: 2026-10-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

CYCode owns a provider-agnostic model/tool loop. Each user turn is appended to the conversation, the model chooses tools or text, every tool call passes hooks and the permission gate, execution returns a typed tool result, and the model receives that result for a subsequent step. Read-only tool batches may execute concurrently; mutating tool calls are serialized. The same agent core is used by terminal, local GUI and headless `exec`.

The runtime adds research-specific environment actions beside coding tools: literature search/read, experiments, notebooks and LaTeX. `exp_run` can launch a detached experiment and `exp_status` can inspect logs/metrics later. These processes remain tools of the same coding/research S1 rather than independent agent actors.

The `explore` tool creates a nested agent with a separate conversation and only read-only tools. Its task is self-contained, it returns one final report to the main loop, and multiple read-only calls can be executed concurrently. This is delegated investigation, not by itself a positive S2 relation: no concrete interference among distinct operational S1s and no attenuation loop are established.

Permissions separate operational judgment from enforcement. Project/user allow/deny rules, hooks and optional OS sandbox can constrain what the model may execute; deny rules win over bypass. Durable sessions, compaction and per-turn shadow-git checkpoints support recovery and context continuity.

Project/user `AGENTS.md` and project configuration are loaded as standing context/constraints. They can shape later operation, but the standard runtime does not expose an identity/ultimate-policy issue path to a legitimate parent authority and return the resulting decision as S5 closure. Static context/policy text and ordinary permission changes therefore remain mechanisms, not a positive S5 mapping.

Primary evidence:

- [README.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/README.md)
- [src/agent/loop.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/agent/loop.ts)
- [src/agent/subagent.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/agent/subagent.ts)
- [src/runtime.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/runtime.ts)
- [src/permissions/permissions.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/permissions/permissions.ts)
- [src/context/context.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/context/context.ts)
- [docs/loops.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/docs/loops.md)
- [docs/evals.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/docs/evals.md)

## Operational model

A native turn begins with user intent plus project/context/session evidence. The model selects one or more tools; first-party hooks and permission policy validate/limit the call; CYCode executes it; resulting repository, command, experiment or research evidence returns to the same model conversation. The model then selects another action or terminates. In explicit bypass mode the same task-specific decisions execute without per-action human approval, while hard deny rules and optional sandbox constraints remain enforcement around that S1.

## S1 — Operations

- State: A
- Function: perform environment-facing coding and AI-research work by selecting task-specific repository/research actions, executing them, observing results and iterating toward the requested outcome.
- Disturbance / variety regulated: heterogeneous source/build/test state, ambiguous implementation choices, literature/search evidence, experiment outcomes, notebook/LaTeX state, command failures, context-window pressure and provider/tool errors.
- Decisive decision or feedback right: choose the next task-specific tool/action and integrate returned evidence into later actions and the final answer.
- Decision owner: the model-backed CYCode agent; in supported bypass/headless configurations it can close the action sequence without per-action parent approval.
- Supporting / enforcement mechanisms: permission modes and allow/deny rules, pre/post hooks, optional OS sandbox, tool schemas/dispatch, retries, session persistence, compaction, checkpoints/undo, diagnostics and max-step bounds.
- Closure path: user task/current evidence → model selects coding/research action → hooks/permission enforcement → tool execution → tool result/environment evidence returns to model → subsequent action or final response.
- Boundary reachability: REPL, GUI and `cycode exec` instantiate the same first-party agent core; `exec --mode bypass` provides an explicitly supported unattended path without importing an external coding-agent runtime.
- Why this is / is not agent-owned: removing the model actor while retaining tools, permissions, sandbox and persistence leaves callable/enforcing machinery but removes the open-ended judgment that selects and sequences task-specific coding/research actions.
- Evidence: [src/agent/loop.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/agent/loop.ts); [src/runtime.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/runtime.ts); [src/exec.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/exec.ts); [README.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: human approvals and deterministic guardrails may constrain side effects, but they do not supply the agent's open-ended operational action selection.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established because the supported runtime does not show a concrete interference/conflict/oscillation among multiple operational S1 units that a CYCode-specific coordination relation attenuates.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: concurrent read-only tool batches, parallel explore helpers, serialization of mutating calls, shared project root and external loop examples.
- Closure path: not applicable; no distinct-S1 disturbance → coordination response → changed subsequent S1 behaviour loop was found.
- Why this is / is not agent-owned: explore agents perform delegated read-only investigations and return reports; serialization merely orders tool execution in one main agent turn. Neither supplies evidence of a specific inter-S1 disturbance plus an attenuation relation.
- Evidence: [src/agent/loop.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/agent/loop.ts); [src/agent/subagent.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/agent/subagent.ts); [docs/loops.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/docs/loops.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: externally supervising multiple `cycode exec` processes could create a larger multi-S1 system, but that parent composition is outside the reviewed CYCode boundary.

### Absence scope

- Surfaces inspected: model/tool loop; read-only batching; explore subagents; mutating-tool serialization; experiment processes; headless loop examples; session/checkpoint machinery.
- Plausible first-party paths checked: concurrent explore workers, concurrent writable workers, shared-workspace collision control, experiment jobs as S1 units, multi-process headless loops and parent/subagent mutual adjustment.
- Why no material first-party path remains: the only first-party concurrent agents are read-only investigation helpers, while writable actions remain one main S1 path. No concrete inter-S1 disturbance and feedback attenuation loop is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-current organizational control function distinct from one coding/research S1 and deterministic runtime constraints was established.
- Disturbance / variety regulated: not established at S3 level; located status, todo, experiment and permission mechanisms regulate work inside one S1 rather than resources/commitments across an operational population.
- Decisive decision or feedback right: not established. The main model may choose delegation, todos, experiment polling and task actions, but those are local task decisions rather than whole-system current management.
- Decision owner: not established.
- Supporting / enforcement mechanisms: todo state, experiment launch/status, step caps, permission modes, hooks, sandbox, diagnostics, session state and abort handling.
- Closure path: not applicable; no whole-system current view → substantive resource/commitment/prioritization decision → changed organization-wide operations loop was found.
- Why this is / is not agent-owned: delegation and experiment monitoring remain part of the primary task actor's local work. Static bounds and permission machinery enforce developer/operator choices and do not become an S3 manager.
- Evidence: [src/agent/loop.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/agent/loop.ts); [src/tools/research/experiments.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/tools/research/experiments.ts); [src/permissions/permissions.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/permissions/permissions.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a supervising external loop can decide retries/escalations across multiple runs, but `docs/loops.md` explicitly places that decision in the parent loop, outside CYCode.

### Absence scope

- Surfaces inspected: todos/events; experiment run/status; explore delegation; step/retry bounds; session continuation; permissions/hooks/sandbox; REPL/GUI/headless modes.
- Plausible first-party paths checked: main agent as manager, experiment portfolio control, todo commitment controller, subagent supervisor, resource/concurrency control and loop retry/escalation.
- Why no material first-party path remains: CYCode supplies one primary operational actor and local control aids. Whole-population current authority is either absent or explicitly delegated to an external supervising loop.

## S3* — Complementary audit

- State: —
- Function: no material complementary and sufficiently independent audit path with corrective return into ordinary CYCode operation was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. Post-edit diagnostics and model-requested tests are routine operational evidence; the separate eval harness scores isolated tasks for development but is not wired into normal session control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: configured diagnostics, test/build commands, hooks, checkpoints/diff/undo, eval task checks and CI.
- Closure path: not applicable; no sufficiently independent audit judgment is returned into ordinary current control as a corrective decision.
- Why this is / is not agent-owned: runtime verification evidence is consumed by the same coding actor, while `evals/` belongs to an adjacent benchmark/development system. Neither establishes complementary audit ownership at the assessed boundary.
- Evidence: [src/agent/loop.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/agent/loop.ts); [docs/evals.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/docs/evals.md); [evals/runner.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/evals/runner.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: objective eval checks provide meaningful independent development evidence, but boundary reachability and corrective runtime closure are absent.

### Absence scope

- Surfaces inspected: post-edit diagnostics; model-invoked verification; hooks; checkpoint diff/undo; eval runner/checks/tasks; CI eval workflow.
- Plausible first-party paths checked: separate reviewer/judge agent, protected evaluator during a live session, objective checks returned into runtime control, explore as reviewer and external CI as audit.
- Why no material first-party path remains: normal verification is in-band S1 evidence, and the independent eval harness runs as an adjacent development/benchmark surface rather than a complementary audit actor in ordinary operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective organizational adaptation loop was established in the supported CYCode runtime.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Literature/web tools investigate external information for the current research task, while model/provider/skill configuration remains operator-authored rather than an autonomous future-facing capability-change process.
- Decision owner: not established.
- Supporting / enforcement mechanisms: arXiv/Semantic Scholar/web tools, built-in/project/user skills, model switching, provider configuration, session compaction and experiment evidence.
- Closure path: not applicable; no external/future distinction → adaptation option → adopted change to CYCode's present organizational capability/control loop was found.
- Why this is / is not agent-owned: external research is part of S1's primary transformation. The agent can use information to finish the current task but does not own a persistent program that changes CYCode's future organizational capabilities.
- Evidence: [README.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/README.md); [src/tools/research/papers.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/tools/research/papers.ts); [src/skills/skills.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/skills/skills.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: being research-oriented and externally connected does not itself satisfy S4's outside-and-then adaptation requirement.

### Absence scope

- Surfaces inspected: paper/web search; research skills; experiment tools; model switching/providers; user/project skills; context/compaction; eval results.
- Plausible first-party paths checked: autonomous provider/model adaptation, external trend sensing, future capability planning, skill acquisition, learned configuration update, eval-driven self-improvement and persistent strategic memory.
- Why no material first-party path remains: located external sensing serves current operational work, and durable capability/configuration changes are supplied by user/developer action rather than a closed first-party prospective adaptation loop.

## S5 — Identity and ultimate policy

- State: —
- Function: no material identity/ultimate-policy decision function with legitimate authority and return-to-operation closure was established at the selected session recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. User/project `AGENTS.md`, permission rules, hooks, sandbox, model selection and project config define durable constraints/preferences but do not themselves resolve an identity/ultimate-policy issue through a legitimate authority path.
- Decision owner: not established.
- Supporting / enforcement mechanisms: global/project context files, project/user configuration, allow/deny rules, persisted always-allow entries, hooks, permission modes, sandbox and model/provider settings.
- Closure path: not applicable; no identity/policy issue or proposal → parent authority decision → returned governance of subsequent CYCode operation path was found in the supported runtime.
- Why this is / is not agent-owned: the model receives context/policy but cannot promote ordinary operational questions into an explicit ultimate-policy process. A human can edit configuration/context externally, yet static policy text and ordinary permission/configuration changes are insufficient under the Profile without identity-level issue and closure evidence.
- Evidence: [src/context/context.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/context/context.ts); [src/config.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/config.ts); [src/init.ts](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/src/init.ts); [docs/configuration.md](https://github.com/ChaoYue0307/CYCode/blob/8b09d0a8cbca739a8d5598127b00edd3e5955fb5/docs/configuration.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: `AGENTS.md` is deliberately durable standing context and may contain "what to never touch", but the Profile explicitly rejects policy text alone as S5; no runtime identity/ultimate-policy closure path was established.

### Absence scope

- Surfaces inspected: system/context prompt construction; global/project `AGENTS.md`/CLAUDE.md; project/user config merge; permissions; hooks; sandbox; model/provider selection; init scaffolding; skills and headless execution.
- Plausible first-party paths checked: parent-governed standing project policy, autonomous policy revision, identity/purpose escalation, project context as constitution, permission escalation, trusted extension policy and model choice as identity authority.
- Why no material first-party path remains: CYCode loads and enforces durable external choices, but no supported process turns an identity/ultimate-policy issue into a parent decision and returns that decision as organizational closure.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one CYCode task/session is the assessed organization. Explore subagents are bounded read-only investigation helpers; external shell/cron/CI loops can compose multiple `cycode exec` runs but belong to a parent system outside this boundary.
- Variety: project/source state, task ambiguity, literature/research evidence, experiments, notebooks/LaTeX, provider/tool failures, context growth, permissions and long-running process state are absorbed primarily by S1 plus deterministic supporting machinery.
- Escalation: interactive side effects may ask the user; denied tools return evidence to the agent; unattended loops may be retried/escalated by an external supervisor. These operational paths do not by themselves establish S3/S4/S5.
- Unresolved evidence: no material evidence gap remained that required `?`. Positive credit is limited to the first-party model/tool operational loop; coordination, control, audit, adaptation and policy mechanisms were not promoted without the Profile's required closure.

## Assessment vector

**`A · — · — · — · — · —`**
