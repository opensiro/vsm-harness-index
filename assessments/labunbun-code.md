---
harness_id: labunbun-code
project_name: LaBunbun Code
repository: https://github.com/zayokami/labunbun-code
review_ref: 1470556287af8325a2c7971f7858f42c0d8241a2
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# LaBunbun Code

## Review boundary

- System in focus: one first-party LaBunbun Code coding-agent composition at frozen revision `1470556287af8325a2c7971f7858f42c0d8241a2`, including the `AgentSession` model/tool loop, first-party coding tools, session persistence/context management, permission and plan-mode gates, task list, background shell manager, nested Task subagents, hooks, memory/rules loading, project-definition trust and standard interactive/headless entrypoints.
- Purpose and identity: perform repository-facing coding work from a terminal through a model-driven tool loop, with optional nested subagents, persistent sessions, planning, permissions and user-configurable extensions.
- Relevant environment: user prompts and approvals, repository/filesystem/process state, tool and shell results, model-provider responses, configured settings/rules/hooks/skills/agents, MCP servers and session/context state.
- Standard-distribution boundary: the shipped `@labunbun/agent`, `@labunbun/coding-agent` and `@labunbun/tools` runtime surfaces concretely reached by the documented CLI are inside. External model endpoints, MCP servers, command hooks and project/user-authored skills/agent definitions remain dependencies or configured content; they do not donate organizational ownership beyond the first-party wiring that invokes them.
- Credited operating / distribution surfaces: `README.md`; `packages/agent/src/session.ts`; `packages/agent/src/concurrency.ts`; `packages/agent/src/permissions.ts`; `packages/coding-agent/src/main.ts`; `packages/coding-agent/src/headless.ts`; `packages/coding-agent/src/subagents.ts`; `packages/coding-agent/src/plan-mode.ts`; `packages/coding-agent/src/hooks.ts`; `packages/coding-agent/src/memory.ts`; `packages/coding-agent/src/project-trust.ts`; `packages/tools/src/tasks.ts`; `packages/tools/src/background.ts`.
- Adjacent first-party surfaces excluded from ownership: tests/CI and documentation as authority by themselves, imported configurations from other coding agents, user/project-authored hook commands, skills and agent-definition bodies, external MCP/tool services and provider-side behavior.
- First-party operating / deployment modes considered: interactive REPL, headless `-p` execution, persisted/resumed sessions, plan mode, nested Task subagents, safe-tool parallelism, background shell processes, task-list planning, hooks, memory/rules, skills/agents and configured provider fallback.
- Recursion level: one LaBunbun coding task/session is the assessed organization. The parent `AgentSession` is the primary operational S1. A Task invocation can instantiate a complete nested `AgentSession` and therefore can create an additional operational S1, but a higher VSM function is credited only if the product closes the required inter-S1 or metasystem relation over those units.
- Reviewed revision: `1470556287af8325a2c7971f7858f42c0d8241a2`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`packages/agent/src/session.ts` owns the stateful model/tool execution loop. It prepares current context, calls the configured model, streams assistant output, starts concurrency-safe tool calls when possible, executes the remaining tool calls through the first-party pipeline, records their results and returns those results to the same conversation so later model turns can revise the task-specific course of action. Session persistence, compaction, retries, steering and follow-up queues keep that operating loop viable without replacing its substantive model judgment.

The Task tool in `packages/coding-agent/src/subagents.ts` can create a fresh nested `AgentSession` with its own context window, system prompt, model selection, tools, permission evaluation and compaction wiring. Its final assistant report is returned to the parent as the Task tool result and start/end information is persisted as a sidechain. Multiple Task calls are declared concurrency-safe. `packages/agent/src/concurrency.ts` caps concurrency-safe tool calls at ten and batches overflow, but this is a generic execution-capacity mechanism. The frozen implementation does not identify semantic or operational interference between sibling subagents, negotiate conflicts among them, or feed a conflict-specific attenuation decision back into their later behavior.

The task-list surface is likewise local to one coding objective. `TaskCreate`, `TaskList`, `TaskGet` and `TaskUpdate` expose an in-memory plan/status list to the same operating agent. The prompt asks it to keep only one task `in_progress`; the store does not independently allocate or reprioritize a population of autonomous S1 commitments. Background shell tracking records process state and exposes output/kill controls, but those child processes are coding-tool workloads rather than autonomous organizational S1s by themselves.

Several plausible higher-function surfaces were checked. Plan mode makes the agent research read-only and requires human approval before mutations resume. The permission engine applies operator/configuration rules and mode shortcuts. Project trust requires one-time user approval before repository-supplied agent/skill definitions load. Hooks are user-configured external commands: `PreToolUse` may block an action, while `PostToolUse` is explicitly advisory after the tool already ran. Memory loads static `MEMORY.md`/`LABUNBUN.md`/`AGENTS.md`/rules content; session resume and compaction preserve context. These are useful safety, extensibility and continuity mechanisms, but the frozen product does not close them into autonomous S3*, S4 or S5 functions.

Primary evidence:

- [`README.md`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/README.md)
- [`packages/agent/src/session.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/agent/src/session.ts)
- [`packages/agent/src/concurrency.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/agent/src/concurrency.ts)
- [`packages/agent/src/permissions.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/agent/src/permissions.ts)
- [`packages/coding-agent/src/headless.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/headless.ts)
- [`packages/coding-agent/src/subagents.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/subagents.ts)
- [`packages/coding-agent/src/plan-mode.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/plan-mode.ts)
- [`packages/coding-agent/src/hooks.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/hooks.ts)
- [`packages/coding-agent/src/memory.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/memory.ts)
- [`packages/coding-agent/src/project-trust.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/project-trust.ts)
- [`packages/tools/src/tasks.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/tools/src/tasks.ts)
- [`packages/tools/src/background.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/tools/src/background.ts)

## Operational model

A user supplies a coding objective and model/configuration. The first-party session loop gives the model repository-facing tools and returns tool results into subsequent turns until the model completes or a bound/abort/error terminates the run. The model may create/track subtasks, enter plan mode and spawn nested Task subagents. Each nested subagent runs its own complete model/tool loop and returns one final report to the parent. Deterministic concurrency, permission, persistence, compaction and trust mechanisms constrain or support this work; they do not by themselves own the open-ended coding decision.

## S1 — Operations

- State: A
- Function: transform a user coding objective into repository/process changes or a task result through model-selected tool actions with returned environment feedback.
- Disturbance / variety regulated: repository state, implementation alternatives, file/shell/tool results, model uncertainty, provider/context failures, permission outcomes and evolving task evidence.
- Decisive decision or feedback right: select the next task-specific tool call or substantive answer and revise later choices from returned tool/environment evidence.
- Decision owner: the configured model actor running inside the first-party parent or nested `AgentSession`.
- Supporting / enforcement mechanisms: `AgentSession`; first-party coding tools and pipeline; session store; compaction/recovery; permission engine; task list; skills/MCP; nested Task tool; background shell controls; provider adapters.
- Closure path: current prompt/history/environment evidence → model emits tool call or answer → first-party runtime permits/executes the action → tool/environment result is appended to the session → same model actor observes the result and chooses another action or final output.
- Boundary reachability: the documented `labunbun` interactive and `labunbun -p` headless entrypoints instantiate the shipped `AgentSession` directly. Task subagents instantiate the same first-party operational loop through the standard Task tool.
- Why this is / is not agent-owned: removing the model actor while retaining tools, permission rules, task storage, concurrency and session machinery removes the substantive task-specific judgment of what action to take next; those mechanisms support or constrain the decision rather than replacing it.
- Evidence: [`packages/agent/src/session.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/agent/src/session.ts); [`packages/coding-agent/src/main.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/main.ts); [`packages/coding-agent/src/headless.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/headless.ts); [`README.md`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference and external services remain dependencies; the positive finding is for first-party closure of their task-specific decisions through the repository/tool loop.

## S2 — Coordination

- State: —
- Function: no material S2-specific inter-S1 disturbance-attenuation loop is established at the assessed recursion.
- Disturbance / variety regulated: no concrete interaction-generated conflict, oscillation or coupled disturbance among sibling operational S1s is detected and attenuated by a dedicated first-party relation.
- Distinct S1 units: Task calls can instantiate distinct nested `AgentSession` operational units with separate contexts and tool loops.
- Inter-S1 disturbance: not established as a concrete product-observed relation. Sibling subagents can share a workspace/resource envelope, but the frozen runtime does not identify a specific sibling collision/contention condition as the input to a coordination decision.
- Attenuating coordination relation: not established. The generic tool semaphore/batching cap limits simultaneous concurrency-safe calls; it does not resolve semantic/file/commit conflicts or otherwise coordinate one sibling S1 in response to another sibling's state.
- Feedback into subsequent S1 behaviour: not established for an inter-S1 disturbance. Task results return to the parent after completion, while semaphore admission merely delays generic safe calls until capacity is available.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not. The inspected positive-looking surfaces are delegation, batching and generic execution-capacity control, so they are not promoted to S2 without a concrete disturbance-specific attenuation/feedback witness.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Task subagents, `partitionToolCalls`, per-turn `Semaphore`, task-list dependencies/status and parent collection of final subagent reports.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the parent model can choose to delegate and consume results as part of its own S1 task pursuit; no separate S2 function is shown regulating interaction among sibling S1s.
- Evidence: [`packages/coding-agent/src/subagents.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/subagents.ts); [`packages/agent/src/concurrency.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/agent/src/concurrency.ts); [`packages/tools/src/tasks.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/tools/src/tasks.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream composition could impose coordination among several LaBunbun sessions, but generic fan-out or a concurrency cap is not credited without the Methodology 0.3.6 disturbance-and-feedback witness.

### Absence scope

- Surfaces inspected: nested Task subagents, safe-tool parallelism and semaphore, task-list dependencies/status, background shell management, session sidechains and parent return of subagent results.
- Plausible first-party paths checked: concurrent Task calls as sibling S1s, semaphore capacity as S2 attenuation, task `blockedBy` as coordination, sidechain persistence as shared state and parent aggregation of final reports as coordination.
- Why no material first-party path remains: the product can create multiple operational subagents, but the inspected relations delegate, queue, record or aggregate work. No first-party path detects a concrete inter-S1 disturbance and feeds a disturbance-specific attenuation decision back into later sibling operation.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control loop is established above the current coding task/session.
- Disturbance / variety regulated: task-list progress, subagent completion, background-process status, permissions and session/context state are maintained locally, but not through a distinct higher-recursion current-control authority over a population of autonomous operational commitments.
- Decisive decision or feedback right: no distinct whole-system owner with authority to reprioritize, reallocate or intervene across current S1 commitments is established.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: parent `AgentSession`, task list, nested Task results, background shell manager, event stream, session persistence/resume, plan mode and concurrency controls.
- Closure path: not applicable for the negative finding.
- Whole-system current view: the task list exposes the decomposition/status of one coding objective and the parent eventually receives final Task reports; no boundary-reachable surface maintains a live whole-population view of all autonomous subagents plus commitments/resources for a separate control decision.
- Current-control decision scope: the operating model may choose its own next task/action/delegation as part of S1. Task status bookkeeping, generic concurrency admission and a human plan-approval gate do not establish a separate S3 resource/priority/commitment authority.
- Why this is / is not agent-owned: the same model pursuing the user task can read/update the task list and decide to spawn a subagent, but that is decomposition inside its operating objective rather than a distinct metasystem S3 function.
- Evidence: [`packages/tools/src/tasks.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/tools/src/tasks.ts); [`packages/coding-agent/src/subagents.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/subagents.ts); [`packages/tools/src/background.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/tools/src/background.ts); [`packages/coding-agent/src/plan-mode.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/plan-mode.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the parent is an orchestrating S1 and can make delegation choices; orchestration naming or task-board visibility alone is not sufficient for S3.

### Absence scope

- Surfaces inspected: task store/status/dependencies, Task subagent lifecycle and sidechains, parent session/event flow, concurrency batches, background shell lifecycle, plan-mode approval, resume/session state and tool permissions.
- Plausible first-party paths checked: parent model as S3 manager, task list as whole-system current view, background manager as current resource manager, semaphore as allocation control, plan mode as parent control and session resume as organizational continuity.
- Why no material first-party path remains: each inspected path either regulates the operating agent's own objective, provides generic execution/safety support or delegates a decision to the human. No separate controller closes whole-current observation over autonomous S1 commitments into substantive cross-S1 current intervention.

## S3* — Complementary audit

- State: —
- Function: no material complementary operational-audit loop with sufficiently independent access and returned corrective closure is established in the standard product runtime.
- Disturbance / variety regulated: configurable hooks, code-review skills, permission checks and plan approval can inspect or constrain actions, but no first-party complementary auditor independently observes actual S1 operation and returns a qualifying audit finding into subsequent organizational control.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `PreToolUse`/`PostToolUse`/`Stop` and other command hooks, permissions, plan approval, project trust, code-review skills and normal tool/test output.
- Closure path: not applicable; no standard path closes ordinary operational evidence → complementary independent access → audit finding → returned corrective organizational decision.
- Claim being audited: not established as a distinct operational claim under an independent complementary channel.
- Ordinary reporting path: assistant/tool results, task/session events, subagent final reports, background logs and persisted session data.
- Complementary access path: configurable command hooks are the strongest candidate. `PreToolUse` can block before an action, but that is an inline configured guard; `PostToolUse` is explicitly advisory after execution and receives tool name/input rather than an independent result/evidence channel. Review skills run through the ordinary model/tool composition rather than a distinct audit boundary.
- Independence boundary: external hook commands can be separate processes, but their content/criteria are user-configured and the standard distribution does not establish a complementary observer with independent evidence access and a required return path over actual operations.
- Who acts on findings: a `PreToolUse` hook may cause the ordinary tool call to be blocked; advisory post-use failures are reported. No qualifying independent audit finding is shown returning to a separate current-control owner for corrective action.
- Why this is / is not agent-owned: hooks and review prompts may provide downstream checks when configured, but the product supplies an extension point rather than owning a complete S3* function.
- Evidence: [`packages/coding-agent/src/hooks.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/hooks.ts); [`packages/coding-agent/src/headless.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/headless.ts); [`packages/coding-agent/src/plan-mode.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/plan-mode.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a particular user can configure an external verifier hook, but user-authored downstream composition is not credited as first-party S3* ownership without the required standard complementary closure.

### Absence scope

- Surfaces inspected: hook runtime and headless hook wiring, permission checks, plan approval, project trust, bundled review skills, normal test/tool results, session/event persistence and subagent reporting.
- Plausible first-party paths checked: PreToolUse as independent audit, PostToolUse as review, Stop hooks as corrective return, code-review skills as independent reviewer, plan approval as S3* and permission denials as audit findings.
- Why no material first-party path remains: the blocking paths are inline safety/approval gates or user-authored extensions; the post-use path is advisory and lacks an independent operational-evidence/return closure. No standard first-party complementary observer and corrective return loop remains.

## S4 — Outside-and-then adaptation

- State: —
- Function: no material autonomous prospective adaptation loop is established.
- Disturbance / variety regulated: memory/session state, context pressure, provider failures and imported/user-authored configuration are handled, but not through an actor that detects an external future-relevant change, generates an organizational adaptation and persists it back as a new current capability.
- Decisive decision or feedback right: not established for S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: memory/rules loading, session persistence/resume, context compaction, skills/agent definitions, model fallback, provider catalog probing, migration/import tooling and settings.
- Closure path: not applicable for the negative finding.
- External distinction: provider/tool/repository conditions can be observed during ordinary work, but no S4-specific environmental sensing surface classifies a future-relevant organizational change.
- Future distinction: not established beyond ordinary task planning or provider-recovery handling.
- Adaptation option: operator-authored settings/skills/agents/rules and imported configurations can change capability, but the frozen product does not autonomously generate and select such a durable option from external evidence.
- Path back to current capability: memory/settings/definitions are loaded on later runs when humans or external tooling write them; no first-party autonomous S4 loop is shown persisting its own selected adaptation and then operating under it.
- Why this is / is not agent-owned: the operating model may reason about future steps inside one coding task, while durable skills/rules/settings remain externally authored or imported. Context compaction and model fallback preserve service, not organizational adaptation.
- Evidence: [`packages/coding-agent/src/memory.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/memory.ts); [`packages/coding-agent/src/subagents.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/subagents.ts); [`README.md`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: persistence and extensibility are substantial, but Methodology 0.3.6 requires the future-facing adaptation decision and return-to-capability closure, not merely a place where a human can store instructions.

### Absence scope

- Surfaces inspected: `MEMORY.md`/`LABUNBUN.md`/`AGENTS.md`/rules loading, sessions/resume, context compaction, model fallback, startup provider probing, skills/agents, migration/import tooling, settings and task planning.
- Plausible first-party paths checked: persistent memory as learning, provider fallback/probing as environmental adaptation, compaction as self-adaptation, imported skills/settings as capability evolution and plan mode as future planning.
- Why no material first-party path remains: inspected mechanisms preserve context/service or apply externally authored capability/configuration. None closes external distinction → future distinction → generated/selected durable adaptation → later current operation under that adaptation.

## S5 — Identity / ultimate policy

- State: —
- Function: no material runtime identity or ultimate-policy authority loop is established.
- Disturbance / variety regulated: permission rules, project-definition trust, plan approval and configured system/memory instructions constrain what the coding agent may do, but ultimate policy remains authored or approved outside the autonomous runtime.
- Decisive decision or feedback right: not established for an autonomous identity/ultimate-policy owner.
- Decision owner: user/operator and externally supplied configuration for the strongest candidate policy/identity decisions.
- Supporting / enforcement mechanisms: permission modes/rules, user approval dialogs, plan mode, project-definition trust ledger, settings, system prompts, memory/rules, skills and agent definitions.
- Closure path: not applicable for an autonomous S5 finding; configured/human policy is loaded and enforced by code rather than reconsidered by a runtime ultimate-policy actor.
- Identity / ultimate-policy issue: whether repository-supplied definitions are trusted, which tools/actions are allowed and whether an implementation plan may leave read-only mode are policy questions, but their decisive authority is explicitly external.
- Ultimate authority: the user/operator and layered configuration/rule sources. The permission engine deterministically enforces those decisions; it does not decide the organization's own ultimate identity or policy premise.
- Return-to-operation path: user approvals or configured rules directly change what ordinary operation may do (for example, plan approval restores the prior permission mode), but this is an external governance gate rather than autonomous S5 closure.
- Why this is / is not agent-owned: removing the user/configured rule sources leaves the enforcement mechanism without the ultimate policy choices. The model cannot autonomously approve repository definitions, rewrite deny rules or self-authorize leaving plan mode under the standard path.
- Evidence: [`packages/agent/src/permissions.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/agent/src/permissions.ts); [`packages/coding-agent/src/plan-mode.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/plan-mode.ts); [`packages/coding-agent/src/project-trust.ts`](https://github.com/zayokami/labunbun-code/blob/1470556287af8325a2c7971f7858f42c0d8241a2/packages/coding-agent/src/project-trust.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: strong fail-closed permission/trust mechanics improve safety but enforcement of externally authored policy is not itself S5 decision ownership.

### Absence scope

- Surfaces inspected: permission rule engine/source precedence, permission modes, interactive approvals, plan-mode enter/exit approval, project-definition trust ledger, settings/system prompt/memory/rules and subagent permission inheritance.
- Plausible first-party paths checked: permission policy as S5, project trust as identity admission, plan approval as ultimate-policy return, system prompt as organizational identity and subagent fail-closed behavior as policy authority.
- Why no material first-party path remains: these surfaces enforce or request externally authored policy. No runtime actor frames an identity/ultimate-policy issue, exercises final autonomous authority over it and returns the revised premise into normal operation.

## Summary

- Vector: **A · — · — · — · — · —**.
- The positive finding is the first-party model/tool coding loop (S1=A). LaBunbun can instantiate nested operational subagents, but at this frozen revision the inspected concurrency/task/subagent relations do not close a disturbance-specific S2 loop or a distinct whole-system S3 loop. Hooks/review gates, memory/extensibility and permissions/trust likewise do not satisfy the stricter S3*, S4 or S5 closure tests.
