---
harness_id: tevarn
project_name: Tevarn
repository: https://github.com/wu1w/tevarn
review_ref: e5e8e204ca2baf8ff671104ab6bf5529d40213ef
reviewed_at: 2026-09-22
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Tevarn

## Review boundary

- System in focus: one Tevarn personal Agent OS organization at frozen revision `e5e8e204ca2baf8ff671104ab6bf5529d40213ef`, including the primary model/tool loop, the persistent Identity + workforce inbox/dispatcher path, CEO/steward operating contract, kernel process/permission/budget controls, goal state and first-party task-grounding/completion controls.
- Purpose and identity: act as a persistent personal agent organization that can directly complete simple work and, for larger work, organize durable AI employees, assign jobs, regulate budgets/capabilities and return consolidated results to its owner across local and remote tools/devices.
- Relevant environment: owner instructions and strategic clarifications, local files and repositories, shell/browser/web/data tools, paired devices, model providers, external services/integrations and task-specific evidence.
- Standard-distribution boundary: the shipped Tevarn backend/runtime, `NexusAgentLoop`, first-party built-in tools, kernel-backed process controls, Identity registry, workforce inbox/dispatcher and the CEO/steward contact mode. External model providers, paired remote-device daemons and third-party MCP/services remain dependencies or local environments rather than inherited VSM owners.
- Credited operating / distribution surfaces: `backend/agent/loop.py`; `backend/agent/workforce_dispatch.py`; `backend/agent/workforce_budget.py`; `backend/agent/goal_state.py`; `backend/tools/builtins/crew_steward_tools.py`; `backend/tools/builtins/agent_ops_tools.py`; first-party kernel/process capability, budget and run-gate integrations reached by the shipped loop.
- Adjacent first-party surfaces excluded from ownership: repository-development history and maintainer workflow; tests/fixtures; UI presentation code; documentation/examples not wired into the runtime; `cluster_executor.py` review machinery where it only reviews returned deliverables without complementary access to operational reality; deterministic auto-memory capture where it records history without establishing prospective adaptation ownership.
- First-party operating / deployment modes considered: ordinary interactive tool-using session; owner contacting a steward/CEO identity; durable workforce assignment through Identity + Inbox; worker execution under capability/token budgets; direct owner clarification for strategic ambiguity; optional cluster execution only where its behavior is materially relevant to a claimed function.
- Recursion level: one owner-governed Tevarn organization. Individual persistent employees can be distinct operational S1 units, but this assessment does not assume each employee independently closes a full recursive viable system.
- Reviewed revision: `e5e8e204ca2baf8ff671104ab6bf5529d40213ef`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Tevarn implements a persistent model/tool loop around `NexusAgentLoop`. The loop loads context and enabled tools, asks the model for tool calls, executes those calls, feeds observations back into the model and continues until the model produces a final response or runtime limits stop the run. The runtime adds context persistence, process/token budgets, permission/capability checks, run gating, task grounding and completion controls around the model-owned operational choices.

For multi-agent work, Tevarn distinguishes durable workforce identities from ephemeral subagents. The first-party `crew_steward` tool can list/hire employees, assign inbox jobs, inspect status/results, grant/revoke capabilities, inspect pending grants, set persistent employee budgets and top up running process budgets. `workforce_dispatch.py` explicitly frames the steward/CEO as the actor that analyzes larger work, delegates to employees, allocates budgets, approves employee capability escalation, follows up failures and consolidates results. Employee jobs then run through the same model/tool infrastructure under their own identity/capability and budget context.

The repository also contains a cluster executor, dependency ordering, concurrency semaphores, task-grounding checks, completion gates and model-based reviewer machinery. These are considered carefully below. Their existence is not by itself treated as proof of S2 or S3*: the assessment requires a function-specific inter-S1 disturbance or complementary independent access path rather than generic sequencing, gating or review naming.

Tevarn persists chat-derived memory automatically, but `auto_remember.py` is explicitly a no-LLM heuristic capture path based on regex/length signals. It stores selected decisions/history; it does not itself generate prospective adaptation options or own a future-facing decision right, so memory persistence is not promoted to S4.

## Operational model

The ordinary S1 decision owner is the running model actor: it interprets the task, chooses substantive tool calls, incorporates observations and decides what result to return. In a workforce organization, durable employee agents are additional outcome-bearing operational units executing assigned jobs.

The strongest metasystemic path is the first-party steward/CEO mode. Its operating contract assigns the steward responsibility for current organizational regulation: decide whether work is simple enough to perform directly, otherwise inspect the workforce, split work, choose employees, allocate job budgets/capabilities, process pending capability requests, recover from budget/failure states, collect results and report the state of the whole effort. Runtime queues, token ceilings, capability gates and kernel controls enforce those decisions but do not replace the model's current-control discretion.

Ultimate direction remains with the owner. The steward contract explicitly reserves direction and project-level decisions to the owner and instructs the steward to use `clarify` for strategic ambiguity. `clarify` is a first-party blocking owner-return channel, so identity/ultimate-policy questions can reach the legitimate parent and the returned answer can govern subsequent operation. Ordinary tool confirmations and permission grants are not used as S5 evidence.

## Primary evidence

- [`backend/agent/loop.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/agent/loop.py) — autonomous User → LLM → tool execution → observation → LLM loop; process/run-gate integration and runtime enforcement boundary.
- [`backend/agent/workforce_dispatch.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/agent/workforce_dispatch.py) — durable employee assignment plus explicit steward/CEO organizational contract and owner/steward/employee role split.
- [`backend/tools/builtins/crew_steward_tools.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/tools/builtins/crew_steward_tools.py) — first-party workforce list/hire/assign/status/results, capability regulation, budget inspection, persistent budget changes and live top-ups.
- [`backend/agent/workforce_budget.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/agent/workforce_budget.py) — per-job budget semantics and deterministic enforcement/support for steward-selected current resource decisions.
- [`backend/tools/builtins/agent_ops_tools.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/tools/builtins/agent_ops_tools.py) — durable delegation preference and blocking `clarify` owner-return channel.
- [`backend/agent/task_grounding.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/agent/task_grounding.py) — task-family evidence requirements and post-check support, considered but not promoted to S3*.
- [`backend/agent/cluster_executor.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/agent/cluster_executor.py) — optional parallel execution, dependency ordering and deliverable review path, inspected for S2/S3* claims.
- [`backend/agent/auto_remember.py`](https://github.com/wu1w/tevarn/blob/e5e8e204ca2baf8ff671104ab6bf5529d40213ef/backend/agent/auto_remember.py) — deterministic end-of-turn memory capture, inspected for S4 and intentionally not credited.

## S1 — Operations

- State: A
- Function: autonomously execute owner-directed work through model-selected tool use and, when delegated, through persistent employee agent jobs.
- Disturbance / variety regulated: heterogeneous user tasks, repository/file state, shell/browser/web/data observations, tool errors, capability limits, model/context uncertainty and job-specific evidence requirements.
- Decisive decision or feedback right: select substantive next actions/tools, interpret returned observations and decide what operational result is sufficient to return for the assigned work.
- Decision owner: the running Tevarn model actor for the active session or persistent employee job.
- Supporting / enforcement mechanisms: `NexusAgentLoop`, tool registry/executors, kernel process/token enforcement, permission/capability gates, context persistence, task grounding, completion gates and workforce inbox dispatch.
- Closure path: owner/steward instruction → model decision → first-party tool execution → observation/evidence → subsequent model decision → final result persisted/returned; durable employee results return through workforce status/results to the steward organization.
- Boundary reachability: the shipped `NexusAgentLoop` directly implements the model/tool feedback loop, and workforce jobs are dispatched into the same first-party runtime through the standard Identity + Inbox path.
- Why this is / is not agent-owned: deterministic runtime machinery constrains and executes actions, but the model chooses the substantive course of work and synthesizes the outcome rather than following a fixed workflow result.
- Evidence: `backend/agent/loop.py`, `backend/agent/workforce_dispatch.py`, `backend/tools/builtins/agent_ops_tools.py`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model providers host inference but do not inherit Tevarn organizational ownership; tool/runtime gates can terminate or constrain a run without becoming the S1 decision owner.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific coordination path is established at the reviewed organization boundary.
- Disturbance / variety regulated: the review looked for concrete oscillation, collision or interference among distinct Tevarn employee S1 units rather than treating delegation, inbox queues, dependency ordering or global concurrency limiting as coordination by name.
- Decisive decision or feedback right: no material first-party autonomous or constructor decision path was established that specifically selects/revises a coordination response to an evidenced inter-S1 disturbance.
- Decision owner: none established for qualifying S2.
- Supporting / enforcement mechanisms: workforce inbox queues, cluster dependency ordering/semaphores and kernel run gating can order or limit execution, but the reviewed evidence does not tie them to a reconstructable S2-specific mutual-adjustment decision path among operational units.
- Closure path: no qualifying inter-S1 disturbance → coordination judgment/response → changed later S1 behavior loop was established beyond generic queueing/scheduling/enforcement.
- Why this is / is not agent-owned: the steward decomposes and assigns work, but task allocation alone is not S2; the runtime can serialize or cap execution, but deterministic enforcement alone does not establish the required coordination discretion.
- Evidence: `backend/agent/workforce_dispatch.py`, `backend/agent/cluster_executor.py`, `backend/agent/loop.py` run-gate path.
- Basis: structural.
- Confidence: medium-high.
- Caveats: Tevarn clearly supports multiple operational employees; this negative result is about the stricter S2 witness, not absence of multi-agent execution.

### Absence scope

- Surfaces inspected: workforce dispatch/steward contract, cluster executor/dependency model, global run-gate/concurrency handling in the main loop, workforce inbox semantics and crew management tools.
- Plausible first-party paths checked: durable employee mailbox/assignment, cluster dependency ordering, semaphore-limited parallelism, global run-gate queueing and steward task decomposition.
- Why no material first-party path remains: the reviewed mechanisms either assign/order work or deterministically enforce preselected concurrency/resource bounds; primary evidence did not establish a specific inter-S1 collision/oscillation together with a first-party coordination decision path that owns its attenuation at this recursion.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current Tevarn organization by allocating work, budgets and capabilities, monitoring workforce state, intervening on failures/escalations and consolidating the current effort for the owner.
- Disturbance / variety regulated: oversized/complex work, employee capability gaps, pending grants, budget exhaustion, failed/dead jobs, uneven work allocation, incomplete results and current organizational commitments that require intervention.
- Decisive decision or feedback right: decide whether to execute directly or use the workforce; split complex work; select employees; assign/reassign jobs; set or top up budgets; approve task-relevant capability escalation; react to failed/budget-exhausted work; gather results and determine the next current-control intervention.
- Decision owner: the model-driven CEO/steward actor in the first-party steward contact mode.
- Supporting / enforcement mechanisms: `crew_steward` list/hire/assign/status/results/pending_grants/grant_caps/set_budget/budgets/top_up operations, workforce inbox persistence/dispatcher, kernel capability tokens, deterministic token accounting and budget hard stops.
- Closure path: current workforce/job/budget/grant state → steward model judgment → assignment/resource/capability/recovery action → persisted inbox/identity/kernel state changes → employees run under the changed state → status/results return for the next steward judgment.
- Boundary reachability: `workforce_dispatch.py` injects the steward organizational contract into supported steward contacts, and `crew_steward` exposes the corresponding first-party current-control actions directly in the shipped runtime.
- Why this is / is not agent-owned: the steward contract assigns current organizational choices to the model actor; budget/capability/run machinery enforces the selected constraints but does not decide which worker, budget change, grant or recovery action should be used.
- Evidence: `backend/agent/workforce_dispatch.py`, `backend/tools/builtins/crew_steward_tools.py`, `backend/agent/workforce_budget.py`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: simple task delegation alone is not used for this mapping; the positive state depends on the broader whole-workforce status/resource/escalation loop and enforceable intervention rights.
- Whole-system current view: the steward can inspect the active workforce, per-employee identity/capabilities, queued/running job status/results, pending grants and budget/usage state across the organization it is managing.
- Current-control decision scope: current work allocation, employee participation, per-job/persistent token budgets, capability escalation, requeue/recovery decisions and consolidation of current organizational outcomes.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established for the assessed Tevarn organization.
- Disturbance / variety regulated: incorrect or weak operational claims were inspected through grounding and cluster-review mechanisms, but the available paths do not establish complementary access to operational reality independent enough to qualify as S3*.
- Decisive decision or feedback right: no qualifying independent audit owner/path was established that can inspect materially different evidence from the ordinary production/reporting path and feed findings back into control.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: `task_grounding.py` requires evidence/tool usage for hallucination-prone task classes; cluster review can parse returned deliverables and ask a reviewer model for verdicts; completion gates can require further work. These are useful verification controls but do not by themselves supply independent operational access.
- Closure path: grounding/review can nudge, revise or reject a response, but the reviewed evidence did not establish an independent audit channel with materially different access to the underlying operational reality.
- Why this is / is not agent-owned: model-based reviewer judgment may be agentic, but reviewer naming or a second model is insufficient when its access remains the produced deliverable/ordinary evidence path rather than an independent complementary audit surface.
- Evidence: `backend/agent/task_grounding.py`, `backend/agent/cluster_executor.py`, completion-gate surfaces in `backend/agent/`.
- Basis: structural.
- Confidence: medium-high.
- Caveats: a future mode that gives a distinct reviewer direct raw-artifact/replay/probe access could change this classification without changing S1/S3.

### Absence scope

- Surfaces inspected: task-grounding classifier/post-checks, completion gates, cluster reviewer loop, deliverable contracts and ordinary workforce result/status reporting.
- Plausible first-party paths checked: evidence-count/deep-read requirements, independent reviewer model invocation, revise/reject feedback and post-completion validation.
- Why no material first-party path remains: reviewed checks remain in or over the ordinary production/deliverable path and do not establish sufficiently independent complementary access to operational reality beyond the claims being produced.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then adaptation loop is established at the reviewed boundary.
- Disturbance / variety regulated: changing external conditions, future opportunities/threats and learned owner preferences were inspected, but no shipped path closes sensing → prospective option generation → adaptation of present organizational capability.
- Decisive decision or feedback right: no autonomous or constructor owner/path was established that turns external/future distinctions into adaptation options and returns a chosen option into current S3/capability.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: web/browser tools can sense the environment; memory services can persist information; `auto_remember.py` heuristically stores selected chat decisions/history; skills/MCP/configuration can change capability when explicitly operated.
- Closure path: no qualifying environmental/future distinction → generated adaptation option → returned capability/current-control change loop is supplied by the standard distribution.
- Why this is / is not agent-owned: `auto_remember.py` explicitly performs no LLM call and uses regex/length rules to store notes; memory persistence or available web search therefore does not establish prospective agent-owned adaptation.
- Evidence: `backend/agent/auto_remember.py`, reviewed memory/tool/skill surfaces and steward tooling.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an ordinary task may research future facts, but task-local research is not credited as organization-level S4 unless it develops and closes a prospective adaptation option into present capability.

### Absence scope

- Surfaces inspected: automatic memory capture, memory/tool availability, web/browser/research tools, skills/MCP management surfaces, goal/current-control paths and runtime configuration.
- Plausible first-party paths checked: chat-to-memory learning, external research, skill/tool changes and persistent organizational configuration.
- Why no material first-party path remains: sensing/storage/change primitives exist, but the standard runtime does not supply a first-party prospective adaptation loop that develops options from external/future distinctions and returns one into current organizational capability/S3.

## S5 — Policy and identity

- State: P
- Function: preserve ultimate purpose/direction by reserving strategic ambiguity and project-level direction decisions to the legitimate owner above the steward organization.
- Disturbance / variety regulated: ambiguity over strategic direction, owner intent, project-level commitments or decisions whose consequences should not be settled by the steward as routine current control.
- Decisive decision or feedback right: answer strategy-level clarification and set/approve the direction or project decision that the steward must then operationalize.
- Decision owner: the human owner as legitimate parent authority for the assessed personal-agent organization.
- Supporting / enforcement mechanisms: the steward role contract explicitly separates owner vs CEO responsibilities; first-party `clarify` can block and return an owner answer; ordinary session state then carries the returned instruction into subsequent model/tool/workforce decisions.
- Closure path: strategic/identity-level ambiguity encountered by steward → `clarify`/owner conversation reaches the owner → owner decides direction/project point → answer returns into the active session → steward decomposes/assigns/acts under that returned direction.
- Boundary reachability: owner contact is part of the ordinary supported personal-Agent-OS boundary, the steward contract explicitly names the owner as direction/project decision authority, and the shipped `clarify` tool provides the runtime return channel.
- Why this is / is not agent-owned: no first-party internal ultimate-authority mode was established; the CEO/steward is explicitly subordinate on direction/strategic clarification while retaining current S3 authority, so the qualifying S5 closure is parent-governed rather than autonomous.
- Evidence: `backend/agent/workforce_dispatch.py`, `backend/tools/builtins/agent_ops_tools.py` (`clarify`).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary permission confirmation, task approval or capability escalation is not counted as S5; the positive mapping is limited to the explicit owner-reserved direction/strategy path.
- Identity / ultimate-policy issue: the organization's owner-directed purpose/strategic direction and project-level choices that define what the steward organization should pursue rather than how to execute current work.
- Ultimate authority in each claimed mode: parent mode only — the human owner; no first-party autonomous or constructor S5 mode is established at this boundary.
- Return-to-operation path: the owner answer returns through the active owner/steward session, after which the steward's model/tool/workforce decisions are made under the clarified direction.

## Recursion

Tevarn can maintain multiple persistent employee identities and can organize them into project work, but employee durability and nested agent execution are not enough to prove each worker is independently viable. The assessment therefore fixes one owner-governed Tevarn organization as the system in focus and treats employee agents as S1 units inside it.

## Variety and escalation

Variety is attenuated through task classification, durable assignment, capability-scoped identities, per-job budgets, kernel token/process controls, run gating and task-grounding requirements. The steward amplifies current regulatory variety by being able to inspect state, change budgets/capabilities, requeue work and select different employees. Routine employee capability/budget exceptions are explicitly meant to escalate to the steward rather than the owner; strategic ambiguity can escalate further to the owner through `clarify`.

## Evidence gaps

The main classification risk is S2: Tevarn contains real global concurrency gating and cluster dependency/semaphore machinery, but the reviewed evidence does not clearly reconstruct the stricter Methodology S2 witness tying those mechanisms to a specific inter-S1 disturbance plus a first-party coordination decision right. S3* is similarly conservative: the cluster reviewer is real, but its reviewed access appears deliverable-centric rather than a complementary raw-operational audit lane. These are candidates for reassessment if upstream documentation/tests expose stronger function-specific closure evidence.