---
harness_id: coding
project_name: CODING
repository: https://github.com/Guo-Yixin/coding-agent
review_ref: 1af81bc01090ed7c9ff59c59974ae5537cb640fa
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# CODING

## Review boundary

- System in focus: CODING's first-party repository-aware coding product at frozen revision `1af81bc01090ed7c9ff59c59974ae5537cb640fa`, including its assembled DeepAgents/LangGraph execution graph, primary coding Agent, concrete specialist subagents, controlled local workspace/backend, permissions/middleware, repository retrieval, persistent state/recovery, structured review findings and shipped web/API execution surfaces.
- Purpose and identity: turn a repository task into a traceable coding workflow that can inspect a real repository, plan, modify and test code, review changes through a separated read-only reviewer, recover persistent state and deliver repository changes through supported GitHub/Gitee paths.
- Relevant environment: user objectives and approval decisions, GitHub/Gitee repository and PR state, local project files and commands, CI/status evidence, model-provider responses, repository memory, stored review findings and application/checkpoint state.
- Standard-distribution boundary: CODING's own composition and the concrete DeepAgents/LangGraph behavior instantiated by `agent/server.py`, runtime, prompts, tools, backend, store and UI/API are inside. Generic DeepAgents or LangGraph features that the pinned product does not configure or reach are not imported. External model providers, Git hosts and optional OpenSandbox services remain dependencies.
- Credited operating / distribution surfaces: `README.en.md`; `agent/server.py`; `agent/prompt.py`; first-party runtime/task-intent routing; `agent/backends/*`; reviewer tools/diff parser/store; code-review skill; application persistence/checkpoint paths; supported web/FastAPI execution surfaces.
- Adjacent first-party surfaces excluded from ownership: Agent Eval benchmark infrastructure and fixed-suite reports, contributor/CI/release workflows, architecture capacity estimates not implemented as current services, tests/scripts as authority by themselves and generic framework capabilities not concretely assembled into CODING.
- First-party operating / deployment modes considered: normal coding/planning/analysis/QA/review task kinds; local workspace backend; supported persistent SQLite/PostgreSQL state; concrete `general-purpose` and `code_reviewer` subagents; optional isolated Eval/OpenSandbox paths only where they corroborate product boundaries rather than donate product functions.
- Recursion level: the assessed organization is the primary CODING Agent plus concretely instantiated specialist subagents. The primary Agent is the operational coding S1. The `code_reviewer` is treated functionally as complementary audit rather than automatically as a second operational S1 merely because it is another model process.
- Reviewed revision: `1af81bc01090ed7c9ff59c59974ae5537cb640fa`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`agent/server.py` is CODING's product assembly point. For a real execution thread it creates/reuses the controlled repository backend, prepares repository memory, selects the main and subagent models, constructs the product tool set and system prompt for the classified task kind, installs first-party middleware/checkpoint/store surfaces, and calls `create_deep_agent` with CODING's concrete `general-purpose` and `code_reviewer` subagent definitions. This is a concrete product composition rather than a claim that every DeepAgents capability belongs to CODING.

The primary Agent owns repository-facing coding decisions. The product prompt requires task-specific todos, repository inspection, controlled file/command execution, testing, Git delivery and explicit intervention when a requested coding action crosses protected boundaries. Persistent LangGraph checkpoints and the CODING business store preserve thread/intervention/review state while the workspace backend owns actual repository/tool execution.

The reviewer path is materially separate from ordinary production checking. `_code_reviewer_subagent` creates a separately prompted specialist model that is explicitly forbidden from modifying business source code, committing, pushing or creating PRs. It receives direct read access to review rules, GitHub/Gitee PR context and local diff evidence and owns model-based judgment about real risks. Deterministic reviewer utilities parse the unified diff and validate finding file/line locations before structured findings are persisted in the business store.

CODING also supplies a concrete return path from those independent findings into later corrective control. The base system prompt requires review tasks to delegate to `code_reviewer`; when a user asks for a repair plan based on a review report/findings, the primary Agent must read the report and call `list_review_findings`, then generate the repair plan from that evidence. After user confirmation, the main coding path performs the repairs and validation. The user may gate the subsequent mutation, but the complementary audit judgment itself belongs to the reviewer Agent and its findings are first-party returned into the main corrective path. Methodology 0.3.x has no separate parent modifier for S3*.

Repository memory and task-intent routing improve continuity and select the appropriate current task path. They do not establish a future-facing organizational adaptation function: stable repository facts are persisted/reused, but no distinct actor senses external/future change, develops adaptation options and changes CODING's current organizational capability.

Primary evidence:

- [`README.en.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/README.en.md)
- [`agent/server.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/server.py)
- [`agent/prompt.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/prompt.py)
- [`agent/tools/reviewer_tools.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/tools/reviewer_tools.py)
- [`agent/reviewer_diff.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/reviewer_diff.py)
- [`agent/skills/code-review/SKILL.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/skills/code-review/SKILL.md)
- [`docs/CODING_CODE_REVIEWER_SUBAGENT.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/docs/CODING_CODE_REVIEWER_SUBAGENT.md)

## Operational model

A normal coding task runs through one primary model-backed CODING Agent that reads repository evidence, chooses tools, modifies files, runs validation and performs Git/PR delivery within the configured permission boundary. Task-intent routing changes the prompt/tool expectations for coding, planning, QA, analysis, sync, inspect or review; it does not create a separate organizational function by itself.

For review, the primary Agent delegates the audit to the concrete `code_reviewer` specialist. The reviewer obtains complementary read-only access to the artifact under review, applies review rules, analyzes diff/PR context, validates concrete locations and persists structured findings. Those findings remain queryable by the main Agent and are explicitly required input to later repair planning. This reviewer-to-findings-to-main-repair path is the positive S3* witness.

## S1 — Operations

- State: A
- Function: perform repository-facing software-engineering work by interpreting an objective, selecting repository/tool actions, executing them and revising subsequent action from returned evidence.
- Disturbance / variety regulated: repository structure and state, implementation alternatives, command/test failures, provider uncertainty, tool failures, repository/PR context and changing user requirements.
- Decisive decision or feedback right: choose the next task-specific coding/repository action and revise that choice from file, command, retrieval, test and provider feedback.
- Decision owner: the model-backed primary CODING Agent.
- Supporting / enforcement mechanisms: concrete DeepAgents graph assembly; controlled `LocalShellBackend`; path/input sanitization; tool-error normalization; permissions/interventions; repository retrieval; todos; checkpointer/store; context injection; model-call/graph limits.
- Closure path: user/repository context → main model selects action/tool → first-party backend/tool executes or returns a controlled error/intervention → result/checkpoint is returned to the main Agent → later action/repair/final response changes accordingly.
- Boundary reachability: `agent/server.py` assembles this Agent on real execution threads for the normal application path, and the documented FastAPI/web workspace invokes that runtime directly.
- Why this is / is not agent-owned: removing the main model actor while retaining backends, prompts, stores, deterministic validators and permission machinery removes the open-ended task-specific coding judgment; the remaining machinery constrains/transports rather than selects the implementation action.
- Evidence: [`agent/server.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/server.py); [`agent/prompt.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/prompt.py); [`README.en.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/README.en.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: protected or scope-expanding mutations can require human intervention; that constraint does not remove the Agent's ordinary coding decision right within the approved task boundary.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 interference-attenuation loop was established at the assessed product recursion.
- Disturbance / variety regulated: not established as an S2-specific relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: subagent delegation; main/reviewer role separation; read-only reviewer permissions; task-intent routing; checkpoints; repository/workspace scoping; middleware and tool constraints.
- Closure path: absent at S2 level. Specialist delegation returns an analysis/review result to the parent, but no concrete simultaneous S1 conflict/oscillation → coordination response → changed subsequent S1 interaction was found.
- Why this is / is not agent-owned: role separation and read-only reviewer constraints support safety/audit independence, but they do not establish a coordination function among distinct simultaneously operating S1 units. The reviewer is credited as S3*, not promoted into a second operational unit solely to manufacture S2.
- Evidence: [`agent/server.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/server.py); [`docs/CODING_CODE_REVIEWER_SUBAGENT.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/docs/CODING_CODE_REVIEWER_SUBAGENT.md); [`README.en.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/README.en.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the repository describes deployment capacity with multiple workers/nodes, but explicitly labels parts of that diagram as design/target components and provides no current load-test proof; process-level service scaling is not imported as S1 plurality.

### Absence scope

- Surfaces inspected: main Agent/subagent assembly; general-purpose and reviewer subagents; task-intent routing; local backend/permissions; checkpoint/store state; documented application architecture and multi-agent workflow; review-to-fix path.
- Plausible first-party paths checked: concurrent subagents; shared repository collision control; multi-worker arbitration; role negotiation; shared-task interference; reviewer/implementer conflict attenuation; queues/locks as possible inter-S1 coordination.
- Why no material first-party path remains: the concrete product evidence establishes bounded delegation and role separation, not a simultaneous operational-unit disturbance with a feedback relation that changes later S1 behavior. No qualifying S2 witness was found inside the supported assessed distribution.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function over a population of operational commitments/resources was established at the assessed recursion.
- Disturbance / variety regulated: not established at S3 level.
- Whole-system current view: not established for multiple current operational S1 commitments. Thread/checkpoint/task status and todos describe one workflow but do not create a whole-system operational population by themselves.
- Current-control decision scope: not established. The main Agent decomposes its task and delegates specialist analysis/review, but no first-party current resource/priority/commitment authority over an independently evolving operational population was found.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: todo planning; task-intent router; model-call/recursion limits; checkpoints; persistent application task state; human interventions; backend lifecycle and task-status UI.
- Closure path: absent at S3 level. These mechanisms track or constrain one coding workflow and specialist calls but do not show whole-current operational regulation with authority over shared commitments/resources.
- Why this is / is not agent-owned: the primary Agent is an operational owner and workflow orchestrator, but task decomposition/delegation and status tracking alone are explicitly insufficient for S3 under the Profile.
- Evidence: [`agent/server.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/server.py); [`agent/prompt.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/prompt.py); [`README.en.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/README.en.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deployment diagrams discuss multiple Agent workers as capacity/scaling targets, but worker multiplicity is not equivalent to S3 and target Redis/repository-lock components are explicitly not current application services.

### Absence scope

- Surfaces inspected: product graph assembly; runtime/task-intent routing; task/todo/checkpoint persistence; subagent definitions; application API/workspace status; backend/intervention paths; deployment architecture notes.
- Plausible first-party paths checked: manager/supervisor actor; multi-worker current dashboard; resource/priority allocation; commitment creation/cancellation; repository locks/queue as current-control mechanisms; review orchestration as possible S3.
- Why no material first-party path remains: no supported path supplied both a whole-current view of multiple operational units and substantive current authority over their commitments/resources. Review orchestration is credited separately as complementary audit rather than S3.

## S3* — Complementary audit

- State: A
- Function: independently challenge ordinary implementation claims by giving a dedicated read-only reviewer direct access to PR/diff/review-rule evidence, producing structured risk judgments and returning those findings into the primary Agent's subsequent repair-control path.
- Claim being audited: whether the main coding path's proposed/current changes are safe, correct and acceptable with respect to the actual diff, repository review rules, PR context and concrete changed lines.
- Ordinary reporting path: the primary coding Agent reports its own implementation/testing/delivery result and has broad write/Git/PR responsibility.
- Complementary access path: a separately prompted `code_reviewer` model receives narrowed read-only access to review rules, GitHub/Gitee PR context, local diff summaries and deterministic finding-location validation; it cannot modify business source, commit, push or create a PR.
- Audit judgment / decisive feedback right: decide which observed issues constitute real risk, assign severity/title/description and record structured review findings rather than accepting the implementation actor's own account.
- Decision owner: the model-backed `code_reviewer` subagent.
- Supporting / enforcement mechanisms: reviewer-specific tool list; code-review skill; read-only backend/permission boundary; deterministic unified-diff parsing and location validation; business-store `review_findings`; report persistence; task-intent routing.
- How findings enter subsequent control: reviewer → `add_review_finding`/review report → persistent findings associated with the thread → primary Agent repair-planning prompt is required to read the report and call `list_review_findings` → repair plan is built from those findings → after user confirmation, the normal coding path changes code/tests and records which findings were fixed.
- Closure path: implementation artifact/PR → independent reviewer direct evidence access → reviewer risk judgment/findings → persisted structured audit evidence → main Agent reads the findings for repair planning → subsequent coding operation is explicitly constrained to repairing those findings. Human confirmation may gate the mutating repair, but the audit judgment and complementary evidence path remain reviewer-owned; Methodology 0.3.x does not publish an S3* parent modifier.
- Boundary reachability: `_code_reviewer_subagent` is registered in the normal `create_deep_agent` product assembly, review task prompts require its use, reviewer findings tools/store are first-party, and the standard main prompt explicitly defines the repair-return path.
- Why this is / is not agent-owned: deterministic diff parsing validates evidence locations but does not decide which issue is materially risky. Removing the reviewer model leaves rules/tools/store but removes the independent risk judgment; removing the main implementation model does not remove the reviewer audit role itself.
- Evidence: [`agent/server.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/server.py); [`agent/prompt.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/prompt.py); [`agent/tools/reviewer_tools.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/tools/reviewer_tools.py); [`agent/reviewer_diff.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/reviewer_diff.py); [`docs/CODING_CODE_REVIEWER_SUBAGENT.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/docs/CODING_CODE_REVIEWER_SUBAGENT.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: version 1 intentionally does not auto-fix or auto-publish review comments. This limits automation of the corrective leg but does not remove the first-party return of independent findings into subsequent main-Agent repair control. User confirmation owns whether mutating repair proceeds, not the reviewer's audit judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop over CODING's own organizational capability was established.
- Disturbance / variety regulated: repository memory, web/fetch tools, task-intent classification, skills, persistent checkpoints and Eval evidence can improve or assess current work but do not close future-oriented capability adaptation.
- Decisive decision or feedback right: not established for an S4 actor.
- Decision owner: not established.
- Supporting / enforcement mechanisms: repository memory initialization/update; context injection; web search/fetch; skill methods; task-intent router; persistent store/checkpoints; Agent Eval reports and traces.
- Closure path: no external/future distinction → adaptation-option generation/evaluation → adopted change to present CODING capability/current control was found in the supported product. Memory writes stable repository facts after work and reuses them on later tasks; that is continuity, not prospective organizational adaptation.
- Why this is / is not agent-owned: the model can research external material when a task requires it, but that research serves the current task. The running product does not own a separate process that monitors changing external conditions, develops future capability/strategy options and adopts them into CODING's current organization.
- Evidence: [`agent/prompt.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/prompt.py); repository memory modules/middleware in the pinned tree; [`README.en.md`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/README.en.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: benchmark/Eval infrastructure can inform developers about future product changes, but it is adjacent evaluation/development machinery and is not wired as the product's own adaptation authority.

### Absence scope

- Surfaces inspected: repository memory/context middleware; task-intent routing; web/fetch tools; skills; persistent store/checkpoints; application/Eval documentation; reviewer/repair loop; provider/model configuration.
- Plausible first-party paths checked: external trend monitoring, future-scenario modeling, automatic capability/tool/provider scouting, Eval-driven product adaptation, memory-driven strategy change and returned prospective options into present control.
- Why no material first-party path remains: inspected mechanisms either support the current task, preserve past repository facts or belong to adjacent evaluation/development activity. No boundary-reachable S4 actor closes a future-facing adaptation cycle in the product.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: workspace/path restrictions, task-kind prompts, permissions, human-intervention gates, tool-input sanitization, model/run limits and deployment configuration constrain operation but do not constitute legitimate ultimate-policy/identity authority.
- Decisive decision or feedback right: not established for identity or ultimate policy.
- Decision owner: developer/operator/user configuration remains outside a qualifying runtime S5 actor.
- Supporting / enforcement mechanisms: system/task prompts; backend permission rules; `request_human_intervention`; path/tool sanitization; model-call/recursion limits; environment configuration; workspace isolation and authentication/secrets handling.
- Closure path: absent at S5 level. Externally authored operating policy → runtime enforcement/approval is present; identity/ultimate-policy issue → legitimate product authority → authoritative policy revision → returned organization-wide policy is not.
- Why this is / is not agent-owned: the Agent acts within CODING's configured rules and may ask a human before scope-expanding or dangerous action, but neither the Agent nor that ordinary approval interaction owns CODING's identity or ultimate constitutional policy.
- Evidence: [`agent/prompt.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/prompt.py); [`agent/server.py`](https://github.com/Guo-Yixin/coding-agent/blob/1af81bc01090ed7c9ff59c59974ae5537cb640fa/agent/server.py); backend permission/middleware code in the pinned tree.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: generic user approval of implementation scope is current operational governance, not S5 merely because the human can veto a tool/action.

### Absence scope

- Surfaces inspected: base/task prompts; permission/backend/middleware restrictions; human-intervention tool; workspace/config/auth boundaries; application persistence; review flow; repository/project governance adjacency.
- Plausible first-party paths checked: runtime constitutional revision, identity-level escalation, ultimate-policy adjudication, durable authoritative changes to organization-wide rules, and parent-governed identity decisions returned into subsequent product operation.
- Why no material first-party path remains: first-party runtime mechanisms enforce policy authored outside the Agent organization. No runtime actor or first-party parent loop was found that owns legitimate identity/ultimate-policy closure at this boundary.

## Recursion

The primary CODING Agent is a durable operational S1. Specialist subagents provide bounded analysis/audit roles within the same product composition, but their existence does not by itself establish full VSM recursion. The positive S3* finding treats `code_reviewer` as a complementary audit function, not as proof that it is an independently viable recursive subsystem.

## Variety and escalation

CODING attenuates operational variety through controlled workspace paths, task-intent-specific prompts, reviewer read-only separation, tool-input sanitization, model/run limits, checkpoint recovery and explicit human intervention for protected actions. It amplifies capability through repository retrieval, skills, web context, persistent memory and specialist subagents.

The strongest metasystemic feedback path is audit escalation: primary implementation evidence can be challenged by an independent reviewer with direct PR/diff access; findings are structured and persisted; the main Agent must consume them when producing the repair plan; later coding operations are explicitly tied back to the audited findings. This is complementary audit without inventing S3 from ordinary task orchestration.

## Evidence gaps

- No material simultaneous operational-unit interference path was found for S2; subagent/reviewer plurality alone was deliberately not promoted.
- No whole-current operational population/resource-control path was found for S3; task/todo/checkpoint state alone is insufficient.
- S3* corrective mutation is intentionally human-confirmed, but the independent audit judgment and findings-to-main-control return are first-party and boundary-reachable.
- Persistent memory and Agent Eval do not establish product S4 at the assessed boundary.
- Generic DeepAgents/LangGraph behavior not concretely assembled in the pinned product was deliberately excluded.
