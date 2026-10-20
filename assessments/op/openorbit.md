---
harness_id: openorbit
project_name: OpenOrbit
repository: https://github.com/maneja81/OpenOrbit
review_ref: 2c30242310c3f2e8453b1116d657e65634e6973e
reviewed_at: 2026-10-20
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

# OpenOrbit

## Review boundary

- System in focus: Shipped Electron desktop OpenOrbit first-party multi-agent assistant. Main Orbit orchestrator and seeded Cipher/Atlas/Explorer/Chrono agents route and fulfill **one bounded personal assistant workstream**, with per-agent tools and connectors, interactive approval interruption/resumption and recurring headless prompts.
- Purpose and identity: Personal operator productivity assistant for files, knowledge, web research, settings, agent customization, optional Google and MCP connectors, reminders and scheduled tasks. It is not a first-party self-governing commercial institution simply because several specialist prompts coexist.
- Relevant environment: Running Electron app, configured OpenAI/OpenRouter/Anthropic/Ollama-compatible provider and credentials, SQLite knowledge/agent/task/history stores, human desktop operator, approved filesystem folders, Google/OAuth and MCP servers/HTTP tools when explicitly configured. External provider or remote tool rights are not imported as first-party VSM owners.
- Standard-distribution boundary: `electron/main/ai/{agents,provider,providers,runLoop,approvalPolicy}.ts`; interactive `ipc/agent.ts`; `tasks/scheduler.ts`; `ai/tools/*`, `ai/agentMutationGuard.ts`, `ai/replyGuard.ts`, DB task/history stores and `settingsSchema.ts`. The first-party application defines actual agent prompts/tool maps, orchestrator/specialist routing and approval continuation while the `@openai/agents` SDK handles generic model-agent execution.
- Credited operating / distribution surfaces: [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ai/provider.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/provider.ts); [`electron/main/ai/providers.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/providers.ts); [`electron/main/ipc/agent.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ipc/agent.ts); [`electron/main/ai/runLoop.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/runLoop.ts); [`electron/main/tasks/scheduler.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/tasks/scheduler.ts); [`electron/main/ai/tools/taskAgentTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/taskAgentTools.ts); [`electron/main/ai/tools/explorerAgentTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/explorerAgentTools.ts); [`electron/main/ai/tools/knowledgeAgentTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/knowledgeAgentTools.ts); [`electron/main/ai/agentMutationGuard.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agentMutationGuard.ts); [`electron/main/ai/approvalPolicy.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/approvalPolicy.ts); [`electron/main/ai/prompts/configAgent.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/prompts/configAgent.md); [`electron/main/ai/prompts/orchestrator.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/prompts/orchestrator.md).
- Adjacent first-party surfaces excluded from ownership: README screenshots/media assets and unexecuted demos, GUI rendering decorations, JS/TS unit test mocks, HTTP/MCP/Google services external to repository, human owner decisions, model-provider internal algorithms and user-specific agent prompts/content.
- First-party operating / deployment modes considered: Direct interactive Orbit chat, manually invoked named specialist, nested agent-as-tool workflows, configured provider options, guarded user settings/agent CRUD, user confirmation on sensitive agent mutations, per-tool HTTP mutation approvals, stored personal knowledge and tasks, headless recurring prompt scheduler that rejects approval-gated actions without present user. Provider credentials and Electron application process are prerequisites for actual autonomous operations.
- Recursion level: Single persistent **personal-assistant task service**, with specialist roles contributing to finite user tasks. Their naming/tool capabilities and ability to be edited don't themselves establish independently viable S1 businesses or a continuing corporate VSM metasystem.
- Reviewed revision: `maneja81/OpenOrbit@2c30242310c3f2e8453b1116d657e65634e6973e` on its actual default branch `develop`, immutable source Git tree `f1329d6a282e78af6d2f0eef226c16599dc82f09`, stable GitHub repo ID `1316640949`, created `2026-07-29T23:20:15Z`, public MIT nonfork/nonarchived.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`electron/main/ai/agents.ts` ships a first-party orchestrator and four concrete specialist roles. A configured OpenAI Agents SDK provider is selected using `provider.ts` and `providers.ts`, and the app registers actual web, document, settings, agents, tasks, optional MCP/HTTP tools and nested specialist wrappers. The interactive `ipc/agent.ts` calls the configured agent SDK `run`, streams intermediate events, keeps history and uses `resolveApprovalsAndRun` for model-selected tool interruptions and subsequent resume. That is a supported first-party **agent + tools + model feedback** path rather than a role roster design sketch. [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ai/provider.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/provider.ts); [`electron/main/ipc/agent.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ipc/agent.ts); [`electron/main/ai/runLoop.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/runLoop.ts).

`tasks/scheduler.ts` polls persisted tasks while Electron stays running. Ordinary reminders issue OS notifications; `prompt` tasks start an actual unattended `run` through central orchestrator or addressed specialist, with the **same** nested approval continuation semantics as interactive runs. In the unattended mode, tool calls requiring approval get a rejection/no-user answer; this does not transfer high-risk owner rights to the model. [`electron/main/tasks/scheduler.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/tasks/scheduler.ts); [`electron/main/db/tasksStore.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/db/tasksStore.ts); [`electron/main/ai/runLoop.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/runLoop.ts).

The application also provides concrete independent task-truth checks: `agentMutationGuard.ts` rejects false claims of creating/updating an agent unless that tool was used in the run; `replyGuard.ts` checks tool-related text; `approvalPolicy.ts` classifies HTTP write methods for interruption. They constrain output accuracy/tool authority but do not create a complementary organizational management S3* or a constitutional S5. Cipher may interview and create agent prompts/roles after user confirmation, which expands task-specific personalization but is not automatically autonomous long-horizon S4 strategy. [`electron/main/ai/agentMutationGuard.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agentMutationGuard.ts); [`electron/main/ai/replyGuard.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/replyGuard.ts); [`electron/main/ai/approvalPolicy.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/approvalPolicy.ts); [`electron/main/ai/prompts/configAgent.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/prompts/configAgent.md); [`electron/main/settingsSchema.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/settingsSchema.ts).

## Operational model

An input task reaches a model-controlled central orchestrator, named specialist or scheduled due prompt. The model chooses task tools and accepts observations in the SDK loop under the app's first-party built agent/tool definitions, with bounded turns and approval/answer/resume handling. The dedicated S1 work function is closed when a compatible provider and allowed tools are configured. No function-specific continuing multi-unit S2–S5 managerial/strategic/identity loop is evidenced at this local personal-assistant recursion.

## S1 — Operations

- State: A
- Function: Autonomous personal assistant work: route operator or scheduled tasks to suitable model specialists, select live web/knowledge/connector/tools, act on observations and return a bounded result.
- Disturbance / variety regulated: Novel user requests, variable web/knowledge/data inputs, missing permissions, failed tool invocations, unresolved user questions, stale application settings and scheduled work whose result cannot be precomputed.
- Decisive decision or feedback right: The configured model-driven orchestrator chooses specialist agent-as-tool calls; actual specialists choose registered first-party tools (Explorer web, Atlas knowledge, Cipher settings/agent creation, Chrono scheduled tasks). The Agents SDK performs model-directed turns, and the first-party runLoop resolves tool approval interruptions/resumes the same task with new observations, in both UI and unattended scheduler modes.
- Decision owner: First-party model-backed central Orbit orchestrator and specialist Agent instances, with selected configured provider. The user defines providers/credentials, permitted agent capabilities and protective approval policy; model owns case-specific tool selection and substantive response while Electron runtime enforces bounded turns/approvals.
- Supporting / enforcement mechanisms: buildOrchestrator, seeded model-bound Agent constructors and agentAsTool wrappers with approved nested run, run(ipc interactive), resolveApprovalsAndRun(MAX_TURNS_PER_RUN=40), protected per-tool access, SQLite task/history stores, background runPromptTask and provider adapters.
- Closure path: User message or due persistent prompt task → buildOrchestrator or named specialist → configured provider chooses agent/tool action → tool executes under policy or pauses for actual operator approval → result/rejection returned through runLoop/resume → next model choice and final answer/task/agent data artifact → history and task-run record. Scheduled headless flow auto-rejects approval-gated actions rather than silently granting them.
- Why this is / is not agent-owned: Desktop normal interactive `ipc/agent.ts` and `tasks/scheduler.ts` both instantiate shipped Agent and call `@openai/agents` SDK `run`, wiring first-party typed tools and nested specialist returns. The app supplies actual prompts/tool maps/settings; external provider performs inference but does not supply the domain/task agent implementation.
- Evidence: Agent chooses how to route, what permitted tools to invoke and what output means; deleting the configured generative inference leaves UI/stores and deterministic scheduling but not task-contingent action judgment.
- Basis: [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ai/provider.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/provider.ts); [`electron/main/ipc/agent.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ipc/agent.ts); [`electron/main/ai/runLoop.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/runLoop.ts); [`electron/main/tasks/scheduler.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/tasks/scheduler.ts); [`electron/main/ai/tools/taskAgentTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/taskAgentTools.ts); [`electron/main/ai/tools/explorerAgentTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/explorerAgentTools.ts); [`electron/main/ai/tools/knowledgeAgentTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/knowledgeAgentTools.ts); [`README.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/README.md).
- Confidence: Source-backed normal first-party app wiring. Live model inference and app build were not run in this assessment.
- Caveats: High for supported configured S1 at personal agent workstream recursion.
- undefined: Supported actual tool access varies per chosen specialist/connection; Google/MCP backends and their internal business policy are external. No model quality/security, desktop automation success or safe unattended destructive action is claimed.
- Boundary reachability: [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ipc/agent.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ipc/agent.ts); [`electron/main/tasks/scheduler.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/tasks/scheduler.ts): normal packaged interactive and scheduled routes both construct concrete configured Agent instances and dispatch actual model/tool feedback through first-party tools, subject to approved availability and MAX_TURNS_PER_RUN.


## S2 — Coordination

- State: —
- Function: No S2-specific autonomous mutual-regulation relation among multiple continuing, independently viable S1 operational departments.
- Disturbance / variety regulated: Specialists can receive overlapping user requests, tool calls may compete, persistent facts may diverge, or one named agent may lack access to a requested tool.
- Decisive decision or feedback right: Central orchestrator selects a specialist for the current request, and first-party serial queue/agentAsTool coordinate nested subtask execution. There is no actor judging reciprocal interdepartmental operational interference and returning negotiated changes to multiple continuing viable businesses.
- Decision owner: Single-request routing model and deterministic nested-tool queue, not an independent S2 owner maintaining mutual disturbances among distinct viable S1 units.
- Supporting / enforcement mechanisms: Agent roster with specialist descriptors, buildOrchestrator routing, serialQueue, agentAsTool and shared facts, per-agent tool grants and nested approval runLoop.
- Closure path: Incoming request → central model chooses Atlas/Explorer/Cipher/Chrono or custom agent → sub-agent responds → orchestrator composes answer. No separate S1 department conflict observation → balancing decision → returned bilateral commitments.
- Why this is / is not agent-owned: Names and independence of prompts/tools don't prove each agent is a viable ongoing business unit with separate enduring product mandate and organizational responsibilities. Context sharing is information access, not autonomous S2 disturbance control.
- Evidence: [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ai/runLoop.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/runLoop.ts); [`electron/main/ai/prompts/orchestrator.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/prompts/orchestrator.md); [`electron/main/ai/tools/history.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/history.ts); [`electron/main/ai/tools/agentDataTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/agentDataTools.ts).
- Basis: Bounded negative for observed single personal-assistant recursion.
- Confidence: High.
- Caveats: A downstream deployment with independent viable units could add institutional S2, but no such own-mode management is shipped.

### Absence scope

- Surfaces inspected: Orchestrator to specialist agent-as-tool router, specialist roster, shared facts/knowledge memory, serialQueue and nested approval handler.
- Plausible first-party paths checked: Checked independent specialist ability to maintain viable external operations, collisions between independent role obligations and any returned mutual-regulation decision for separately viable S1 departments.
- Why no material first-party path remains: Shipped specialists are reusable bounded personal task helpers with agent prompts/tool grants and callbacks. Routing and shared memory do not establish a dedicated autonomous inter-viable-S1 conflict attenuation loop with reciprocal returned commitments.


## S3 — Inside-and-now control

- State: —
- Function: No separately delegated or autonomous inside-and-now management owner controlling priorities/resources/commitments of multiple independently viable S1 departments.
- Disturbance / variety regulated: Current assistant task errors, running scheduled jobs, unexpected browser/MCP requests, user permission changes and pause-worthy mutations.
- Decisive decision or feedback right: User can configure and delete specialist agents, approve one tool action, grant connectors or change settings. Cipher can propose/perform permitted agent configuration and schedules can repeat prompts. All such changes manage personal assistant task configuration, not an accountable whole-current executive allocating real multi-unit organizational commitments with decision return.
- Decision owner: User operating their desktop/preferences and one-task agent routing, with deterministic permission and scheduler enforcement; no independent enterprise S3 actor or closed parent-governed S3 authority at a multiple viable-S1 scope.
- Supporting / enforcement mechanisms: IPC agents/settings, Cipher protected settings and create/update tools, per-tool approval loop, task scheduler, global chat history and UI telemetry.
- Closure path: Operator authorizes individual mutation or supplies new configuration → local agent roster/settings/task changes → subsequent personal assistant runs use new config. No multi-viable-S1 current operating report → resource/priorities intervention/decision → returned departmental commitments.
- Why this is / is not agent-owned: A strong personal admin interface and approved CRUD on agent definitions are not S3 current-control for an organization with independently viable departments. A tool permission check is task-local, not a standing parent manager's action.
- Evidence: [`electron/main/ipc/agent.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ipc/agent.ts); [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ai/prompts/configAgent.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/prompts/configAgent.md); [`electron/main/tasks/scheduler.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/tasks/scheduler.ts); [`electron/main/settingsSchema.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/settingsSchema.ts).
- Basis: Bounded no-evidence after checking human-assisted approvals and model-mediated agent administration.
- Confidence: High.
- Caveats: An external enterprise supervisor could use this app as a tool, but the source doesn't supply a current corporate-management mandate or return relationship.

### Absence scope

- Surfaces inspected: Central orchestrator, Cipher CRUD of named specialists, user-scoped consent and protected settings, stored task scheduler, UI/admin screen and history/logging.
- Plausible first-party paths checked: Checked whether central orchestrator is a current organization executive, whether human can exercise a packaged parent-governed S3 over continuing viable S1 departments and whether scheduling/prioritization affects their binding resources/commitments.
- Why no material first-party path remains: No independently viable organizational departments are established, and operations are user/task-scoped. Individual agent configuration, approvals or scheduled prompt runs lack standing whole-organizational current executive judgment/return to viable units.


## S3* — Complementary audit

- State: —
- Function: No complementary independently chartered audit of an S3 manager's ordinary current report using a distinct direct reality access path with correction returned to that manager.
- Disturbance / variety regulated: Model may falsely claim agent/settings mutation; leaked tool/checklist content could mislead user, tool outcomes may not match assistant prose, and approvals may time out.
- Decisive decision or feedback right: AgentMutationGuard inspects actual run item tool-call history before allowing the model to assert an agent was created/updated, and ReplyGuard suppresses unsupported checklist claims. These are genuine independent work-product/event truth checks, not an auditor of S3 organizational reporting and field reality.
- Decision owner: Deterministic claim/tool record verification in same desktop application, user approval/UI event sinks; no distinct S3* reality auditor and corrective S3 recipient.
- Supporting / enforcement mechanisms: guardFalseAgentMutationClaim, replyGuard, run item metadata, approval settlement, per-tool logs and persisted task run results.
- Closure path: Model assertion about one agent mutation → check corresponding current run's mutation tool history → correct user-facing text if no tool occurred. No regular S3 management account → independent access to field operations → corrective decision returned to S3.
- Why this is / is not agent-owned: Separate code validation can be independent of a specific model statement and remain valuable; it is still within S1 output safety rather than complementary organizational audit of a real S3.
- Evidence: [`electron/main/ai/agentMutationGuard.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agentMutationGuard.ts); [`electron/main/ai/replyGuard.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/replyGuard.ts); [`electron/main/ai/runLoop.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/runLoop.ts); [`electron/main/ipc/agent.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ipc/agent.ts); [`electron/main/db/tasksStore.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/db/tasksStore.ts).
- Basis: Bounded absence after inspecting strongest audit-like first-party guard surfaces.
- Confidence: High.
- Caveats: Do not confuse inability to prove organizational audit with absence of all correctness checking.

### Absence scope

- Surfaces inspected: agentMutationGuard, replyGuard, run item tool history, approval timeout/rejection, task-run result history and trace metadata.
- Plausible first-party paths checked: Checked whether independent tool-truth checks challenge a normal S3 management status report based on direct field access and return a corrective managerial mandate.
- Why no material first-party path remains: Guards check assistant responses against same task's tool evidence, not an organizational S3 manager account of multiple viable S1 operations. No complementary S3 reality-auditor mandate or S3 correction path remains.


## S4 — Outside-and-then intelligence

- State: —
- Function: No standing outside-and-then environmental intelligence that selects, accepts and returns prospective strategic organizational capability adaptations.
- Disturbance / variety regulated: Users may need new specialist knowledge, changed integrations, recurring future reminders or different assistant skills as tasks evolve.
- Decisive decision or feedback right: Cipher can interview a user to construct or revise a custom agent system prompt, consult references, and commit after required user confirmation. Chrono records recurring tasks and Explorer accesses fresh web pages. They do not independently initiate long-horizon organizational scanning, weigh capability portfolio options, secure strategic acceptance and feed a future-oriented change back to accountable current business management.
- Decision owner: Human user's articulated immediate need plus task-level model answers; deterministic scheduler and approval rules. No separately chartered S4 intelligence decision owner.
- Supporting / enforcement mechanisms: Cipher interactive agent creation/update interview, user-protected settings, specialist roster, Explorer web search, recurring prompt scheduler and knowledge store.
- Closure path: User requests a new agent or schedule → model may draft/configure a specialist after confirmation → later tasks use it. This is task/onboarding customization rather than independently initiated future-environment research with adopted organization-wide capability strategy.
- Why this is / is not agent-owned: Creation of new agents is a capability to implement a user's current request, not proof of an autonomous prospective strategic function; time-delayed prompts alone are scheduling.
- Evidence: [`electron/main/ai/prompts/configAgent.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/prompts/configAgent.md); [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ai/tools/explorerAgentTools.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/tools/explorerAgentTools.ts); [`electron/main/tasks/scheduler.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/tasks/scheduler.ts); [`electron/main/settingsSchema.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/settingsSchema.ts).
- Basis: Bounded negative after checking strongest first-party agent-created capability path.
- Confidence: Medium-high.
- Caveats: User can explicitly schedule periodic strategic research, but the source supplies no standing autonomous strategic acceptance right or multi-unit strategic management return.

### Absence scope

- Surfaces inspected: Cipher assisted custom agent construction, external web browsing, task scheduling, user memory and persisted custom prompts/agents.
- Plausible first-party paths checked: Checked new-agent creation as future capability, reminders as long-term intent, live web access as environmental intelligence and model interviews as autonomous option selection/acceptance.
- Why no material first-party path remains: All capability changes are reactive to a user's current task and require local user confirmation or configured schedules. No independently initiated prospective organizational environment → accepted strategic option → return into continuing company capability is shown.


## S5 — Policy and identity

- State: —
- Function: No first-party ultimate constitutional identity/purpose authority of a viable organization, internally owned or via a closed legitimate parent mandate.
- Disturbance / variety regulated: Potential unauthorized credential changes, unsafe connector permissions, destructive HTTP methods, changes to provider URLs, approval policy or location privacy.
- Decisive decision or feedback right: SettingsSchema and protected-setting refusal block AI-mediated changes to sensitive app controls; global approvalPolicy classifies HTTP methods and pauses potentially destructive writes for a human. This enforces already configured task security and user privacy rather than adjudicating the organization’s purpose/identity or changing a founding charter.
- Decision owner: Desktop user/developer establishes local capability/permission rules and model chooses bounded task tools. No internally authorized S5 decision maker or identified legitimate organizational parent mandate/return.
- Supporting / enforcement mechanisms: ALLOWED_SETTING_KEYS/PROTECTED_SETTING_KEYS, updateSettingTool, agent mutation confirmation, HTTP method requiresApproval, credential slots/provider choice, Electron IPC/OS permissions.
- Closure path: User-defined static privacy/tool policy → allowed/denied local change or approval → subsequent tool handler proceeds/refuses; no constitutional issue → ultimate legitimate policy judgment → formal enduring organization-purpose change returned to S1–S4.
- Why this is / is not agent-owned: Protected settings and human approval are real guardrails, not decisive identity/policy ownership at the organizational VSM recursion.
- Evidence: [`electron/main/ai/agents.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/agents.ts); [`electron/main/ai/approvalPolicy.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ai/approvalPolicy.ts); [`electron/main/settingsSchema.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/settingsSchema.ts); [`electron/main/ipc/agent.ts`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/electron/main/ipc/agent.ts); [`README.md`](https://github.com/maneja81/OpenOrbit/blob/2c30242310c3f2e8453b1116d657e65634e6973e/README.md).
- Basis: Bounded negative after checking owner/admin settings and agent-mutated policies.
- Confidence: High.
- Caveats: External user has legitimate control of the desktop, but mere possession of settings is not a source-backed corporate S5 mode.

### Absence scope

- Surfaces inspected: Protected settings from Cipher, HTTP approval-method policy, sensitive updateAgent confirmation, provider credentials and locations, IPC access and per-agent connector permissions.
- Plausible first-party paths checked: Checked owner consent on agent configuration and protected privacy settings as possible parent S5(P), or model-created organizational charter as autonomous S5.
- Why no material first-party path remains: Those controls enforce user/developer permissions for personal tools and profiles. No distinct first-party organizational purpose/constitutional decision owner, legitimate ultimate mission decision or formal returned S5 charter governs a viable organization.



## Recursion

The app supports long-lived *personal service continuity* and multiple reusable tool-bearing agents, but its work units remain delegated bounded requests under one user's personal assistant. A reusable named specialist and shared memory are not sufficient to infer a viable business department, and human confirmation on agent edits is a task safety decision, not an institutional S3/S5 parent contract. Future deployment inside a team or institution would require separate proven source evidence for that VSM recursion.

## Variety and escalation

Novel user requests, changing connected data, ambiguous documents and failed tool calls cause operational variety. Agent model chooses revised tools/action plan within configured policy; approval-gated mutations stop and ask the operator, and scheduled headless runs explicitly reject those operations. Missing request answers and false mutation claims are represented as task feedback/errors, not independent organizational algedonic escalation or complementary S3 reality inspection.

## Evidence gaps

- Assessment grounded in pinned first-party TypeScript/Electron implementation and real normal supported `@openai/agents` runtime setup. Configured provider and actually permitted external services are required for S1. No live paid provider, Electron desktop action, Google OAuth or MCP server execution was performed.
- JS/TS full project tests/build were not run without preinstalled npm dependencies. This is a source-code assessment and not empirical autonomous task-performance measurement; Index structural and unit tests are independent.
- No actual first-party standing enterprise VSM institution, separate viable business units or constitutional return was found. That source boundary does not deny a user's ability to deploy future external S2–S5 organizational systems.
