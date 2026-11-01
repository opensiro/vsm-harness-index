---
harness_id: opengeniemaster
project_name: OpenGenieMaster
repository: https://github.com/eust-w/opengeniemaster
review_ref: 8f6dab22a54a318bf8afa221269a6f9c00fa860c
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: C
autonomy_s5: —
---

# OpenGenieMaster

## Review boundary

- System in focus: the original OpenGenieMaster embodied-task harness, including its shipped EEP tool runtime, built-in optional Claude coding agent, multi-robot task continuity, execution/admission/feedback pipeline, recorded verification, and memory/practice interfaces; **not** the unrelated official AGIBOT GenieMaster system that this repository attempts to reproduce.
- Purpose and identity: let a coding agent perform persistent domain work with an embodied robot fleet, feedback-based recovery, continuity across interruptions, evidence-gated memory and prospective practice opportunities without changing robot policy weights.
- Relevant environment: simulation scenarios (store/office/home), optionally user-supplied HTTP robot services, inventory/objects/people, distinct robot execution and sensing services, human operator, optional Anthropic provider, and outside coding agents through MCP.
- Standard-distribution boundary: the documented first-party optional `ogm agent` CLI that wires `ClaudeAgent` to simulated `Harness` through `ToolRegistry`; the shipped `ogm mcp` server / EEP tool API and deterministic scripted orchestrator are inspected as additional supported modes/constructors. Anthropic inference is a configured external model service, not a separate organizational owner credited for non-shipped functions. The packaged default demo/bench is scripted and cannot be used to infer model-owned decisions.
- Credited operating / distribution surfaces: [Claude tool loop](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/llm_agent.py#L54-L139), [operator protocol](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/prompts.py#L1-L45), [tool registry](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/tools.py#L76-L240), [task/runtime entrypoints](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/cli.py#L43-L110), [continuity](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/continuity.py#L20-L180), [harness control and feedback](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L129-L355), [recheck and memory](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L409-L758), [capability gaps and practice](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/practice.py#L50-L125), [reflection pipeline](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/memory/reflection.py#L118-L350), [shared admission](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/admission.py#L97-L310).
- Adjacent first-party surfaces excluded from ownership: `docs/research/` public-paper reconstruction and comparisons to AGIBOT; synthetic `bench/` methods and scripted `ogm demo` demonstrations; contributor CI/release; `replay.py` offline regression; `flywheel.py` training-example export **without any policy training**; unverified external physical VLA/robot implementations. These constrain confidence but do not become runtime owners of adaptation, audit or policy.
- First-party operating / deployment modes considered: built-in Claude `ogm agent` on simulation (optional `anthropic` SDK and credentials), `ogm mcp` attached to external coding agents over stdio, deterministic `ScriptedOrchestrator` fallback/bench, `ogm mcp --fleet` with custom HTTP robots, human-operated robot backend example, manual `ogm reflect` and memory commands.
- Recursion level: one project-level embodied work system comprising multiple robot work cells as S1 operations and one coding-agent/harness metasystem. Each robot work cell has a separate local physical/task environment and its adapter/policy; the single central Claude tool loop is not falsely counted as several coding agents. Vendor/physical robot internals remain opaque below this level.
- Reviewed revision: 8f6dab22a54a318bf8afa221269a6f9c00fa860c; exact pinned checkout, 85 tracked source files.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python package defines EEP contracts (`eep/`), domain workflows, embodiment robot capability/calibration/adapter abstractions, a shared `Harness` owning persistent task state and memory, typed JSON-tool handlers for an MCP server and optional `ClaudeAgent`, a deterministic scripted `ScriptedOrchestrator`, a rule/optional LLM reflection pipeline, targeted practice constructor, simulated robot world, and offline tests. `ClaudeAgent.run` sends an operator system prompt, reads model tool calls, invokes first-party registry handlers and appends tool results until a terminal response or turn limit. `Harness.execute` enforces admission, calls a robot adapter, applies explicit completion criteria beyond policy self-report, records feedback and adjusts task continuity. `Harness.dispatch` assigns ready work items to capable/available robots while respecting busy assignments and group affinity. `Harness.recheck_step` may overturn earlier success/failure and reopen tasks. Execution records can be mined into machine-readable guidance/criteria/recovery/coordination patches, admitted with evidence checks, applied on future work and retired based on observed outcomes. See [architecture](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/docs/architecture.md#L1-L120), [runtime factory](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/runtime.py#L16-L104), [LLM agent](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/llm_agent.py#L54-L139), [Harness](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L59-L88), [CLI](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/cli.py#L43-L125).

The repository explicitly says its EEP wire format is a locally invented independent reimplementation, not an official compatible release; the PyPI package was not yet published at review. Real-robot testing is not claimed. A user-supplied backend and model credentials are prerequisites, not evidence of an independently governed organization. [Source README](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/README.en.md#L1-L185), [real-robot adapter](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/embodiment/adapters.py#L144-L218).

## Operational model

A user/system supplies a domain task goal. In the shipped autonomous simulation mode, the built-in Claude coding agent chooses the workflow/steps, calls `eep_dispatch`, inspects fresh observations and memory guidance, chooses multimodal execution requests and recovery/handoff actions based on returned failure evidence, verifies persistent effects and may propose memory. A robot/policy executes a local action; the harness enforces prerequisites and determines task outcomes. Two or more embodied robot work cells can run distinct work items, causing observable shared-capacity, affinity and handoff conflicts. In the scripted mode, the same EEP sequence is driven by deterministic rules; no autonomous organizational owner can be inferred from scripted benchmark success. The HTTP robot-service mode is supported but its physical autonomy, sensor independence and safety are not verified. [Operator prompt](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/prompts.py#L1-L42), [tool loop](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/llm_agent.py#L79-L139), [scripted loop](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/orchestrator.py#L24-L205), [real-fleet wiring](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/runtime.py#L55-L97).

## S1 — Operations

- State: A
- Function: primary embodied domain work (e.g. inspect/restock, retrieve, clean, handoff) by agent-guided robot work cells.
- Disturbance / variety regulated: user task variation, unavailable/unknown objects, visual occlusion, robot capability limits, unexpected failures, interruptions and contradictory task outcomes.
- Decisive decision or feedback right: the in-process Claude coding agent chooses task decomposition, relevant tools, guidance, execution/recovery/handoff and whether to retry, based on live task context and returned observations.
- Decision owner: `ClaudeAgent` in the optional first-party `ogm agent` mode; individual robot policy owns lower-level execution, not the higher-level coding-agent choice.
- Supporting / enforcement mechanisms: `ToolRegistry`, EEP schema, `Harness`, domain templates, adapters, admission interlocks, task store, completion criteria, typed failure/recovery hints, bounded turn count.
- Closure path: goal → model tool decision → `Harness.execute`/robot → observation, checked outcome and persisted continuity → next model turn or terminal response.
- Boundary reachability: documented `ogm agent` command constructs `ClaudeAgent` with first-party operator prompt and directly wired EEP tools; optional Anthropic SDK/API availability is an execution prerequisite. It is not necessary to invent an agent in application code. Offline fake-client tests demonstrate tool-loop wiring, not actual paid-model behaviour.
- Why this is / is not agent-owned: removing `ClaudeAgent` leaves `ScriptedOrchestrator`, which can follow fixed recovery rules but does not retain the agent's open-ended choice of guidance and recovery under novel user contexts. S1 `A` belongs narrowly to the shipped optional Claude mode; the deterministic demo does not itself establish `A`.
- Evidence: [Claude tool loop](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/llm_agent.py#L54-L139), [operator instructions](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/prompts.py#L1-L39), [EEP handlers](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/tools.py#L78-L177), [execution/feedback](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L409-L523), [CLI agent entrypoint](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/cli.py#L77-L110).
- Basis: first-party optional agent tool loop with consequential environment feedback.
- Confidence: high for code-level reachability, moderate for deployed agent outcomes (no provider E2E run).
- Caveats: robot simulator is semantic; physical policy autonomy and real-world safety are not verified; provider model behaviour was not exercised.

## S2 — Coordination

- State: A
- Function: dampen conflicts between distinct embodied S1 work cells over capacity, shared work-item affinity and interrupted handoffs.
- Distinct S1 units: two or more separately assigned robot/policy work cells with their own capability and physical state in a fleet; not two names for the same Claude agent.
- Inter-S1 disturbance: assigning one busy robot simultaneously, transferring an unfinished pick–carry–place group while the first robot still holds its object, running dependent steps before prerequisites, or handing off to an incapable robot.
- Attenuating coordination relation: `Harness.dispatch` excludes busy/stopped units, respects group affinity and dependencies; `update_task(assign/handoff)` mediates exceptional reassignment. The agent's operating prompt directs failure-driven handoff and deliberate retry/wait/stop decisions.
- Feedback into subsequent S1 behaviour: assignment and handoff update persistent `TaskStore`; the next `eep_task_get` / `eep_dispatch` / execution uses the new robot, group and dependency state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the code explicitly detects **the inter-robot work-item/capacity conflict** and blocks/moves conflicting assignments, including held-object restart semantics; a simple shared task list would not do so.
- Disturbance / variety regulated: concurrent incompatible robot assignments and unstable cross-robot handoff in shared work.
- Decisive decision or feedback right: the autonomous Claude agent can choose to wait, hand off/reassign, force-restart affected work items, or route around failures based on robot feedback; deterministic `dispatch` enforces ordinary constraints but does not itself own discretionary S2 judgment.
- Decision owner: `ClaudeAgent` for exception coordination in the supported multi-robot mode; deterministic `Harness` for bound-preserving enforcement. Routine default dispatch alone would support only constructor/enforcement, not `A`.
- Supporting / enforcement mechanisms: busy-robot set, capability filtering, group binding, held-object tracking, dependency graph, continuity persistence, readiness checks.
- Closure path: two robot work cells create assignment/holding conflict → feedback/continuity visible through EEP → agent chooses handoff/retry/alternate robot → guard updates whole work item → subsequent dispatch/execution observes new ownership.
- Boundary reachability: multi-robot scenarios and `eep_task_update` handoff are first-party tools available directly to `ClaudeAgent`; no custom coordinator is required in that mode. S2 `A` does **not** claim the scripted dispatcher has autonomous organizational discretion.
- Why this is / is not agent-owned: the full exception-response choice can be made by the tool-using model; deterministic locks/guards are supporting regulators. Removing the model would retain fixed handoff mechanics but not its context-sensitive coordination discretion.
- Evidence: [operating prompt](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/prompts.py#L8-L38), [dispatch and busy rules](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L305-L365), [handoff safeguards](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L267-L303), [continuity group assignment](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/continuity.py#L100-L168), [handoff regression](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/tests/test_regressions.py#L78-L115).
- Basis: identifiable multi-S1 interference, conflict-specific guard, model-accessible discretionary recovery and returned assignment state.
- Confidence: moderate: source and synthetic test wiring are clear; real multi-robot model behavior is untested.
- Caveats: if physical robots are only passive actuators under one central actor, the organizational S2 interpretation narrows; standard simulated policy work cells still retain local execution environments and separate assignments.

## S3 — Inside-and-now control

- State: C
- Function: provide a current whole-fleet task/priority/resource regulation path, beyond local per-step delegation.
- Disturbance / variety regulated: simultaneous active tasks competing for finite robot availability, differing priorities, stopped robots and unmet commitments.
- Whole-system current view: `eep_task_list` lists all tasks, `eep_capabilities` lists fleet skills/status, `Harness._busy_robots` spans active, paused and interrupted tasks, and `ScriptedOrchestrator.run_ready` enumerates all active tasks.
- Current-control decision scope: assign resources across all ready tasks, use task priority when selecting the next work item, stop/pause or restart commitments and intervene on assignment. Task priority is chosen at creation, not autonomously renegotiated by a dedicated whole-system governor.
- Decisive decision or feedback right: a developer/composed operator or future first-party agent policy must decide whole-system priorities, commitments and exceptions; the shipped scheduler executes preselected priorities and capacity rules.
- Decision owner: no autonomous agent demonstrably assigned sustained whole-system S3 discretion in the standard operating instructions. The caller chooses priorities and when the scheduler runs; scripts enforce them.
- Supporting / enforcement mechanisms: priority-sorted task store, cross-task dispatch, `run_ready` highest-priority selection, stop/resume and event log.
- Closure path: all-task view + priorities → scheduled fleet assignment/intervention → persistent task/robot state → next scheduling pass. The first-party constructor is real; an autonomous whole-system deciding/feedback actor must still be composed.
- Boundary reachability: `eep_task_list`, priority at `eep_task_create`, cross-task `eep_dispatch` and `ScriptedOrchestrator.run_ready` are shipped callable modes. No private benchmark oracle is needed. This is a function-specific S3 path, not mere generic tools.
- Why this is / is not agent-owned: scripted `run_ready` orders work by caller-supplied priority; Claude's documented `ogm agent` goal prompt serves one task and does not establish an autonomous sustained fleet-wide current-control review. Enforcement is not ownership. Human `eep_task_update` calls are local operations, not a distinct operationally closed **parent S3** mode.
- Evidence: [all-task and fleet view](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L113-L174), [task priorities and dispatch](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L129-L153), [cross-task busy guard](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L305-L353), [scheduler `run_ready`](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/orchestrator.py#L134-L183), [tool registry](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/tools.py#L85-L155).
- Basis: shipped S3-specific whole-current-task capacity/priority constructor with missing autonomous decisive S3 policy.
- Confidence: moderate-high.
- Caveats: no operator-governed (P) whole-system governance closure, budget bargaining, or accountable strategic priorities is demonstrated.

## S3* — Complementary audit

- State: C
- Function: challenge the robot policy's own success report and the ordinary step-completion record through a separately callable, more direct evidence check.
- Claim being audited: the physical action succeeded and its effect persists (e.g. an item really remains in the intended slot, not just policy-reported success).
- Ordinary reporting path: robot adapter `execute` returns a policy success/outcome and observation; harness evaluates immediate criteria, records execution and updates task status.
- Complementary access path: `eep_verify` / `recheck_step` later calls criterion checks, optionally at close range, through the adapter's separate `check` operation; contradictory results mark prior execution records, convert succeeded steps to failed, and reopen completed tasks.
- Independence boundary: the **verification request and criterion signal** are separate from the policy's initial self-reported success, and can overturn it in the shipped simulator. However physical `HttpAdapter.check` calls the *same configured robot service* (`/check`), with no guaranteed independent detector/operator/credential ownership; the model can also invoke the check itself. This is an explicit complementary **constructor**, not a demonstrated organizationally independent S3* auditor.
- Who acts on findings: the harness reconciles continuity deterministically, and the coding agent can read discrepancies, recover or create new memory; a distinct audit owner/trigger/sampling authority is not supplied.
- Disturbance / variety regulated: false-positive policy completion, persistent-effect regressions and false negatives hidden in routine execution summaries.
- Decisive decision or feedback right: an independent auditor's selection of when/how to check and corrective judgment is not operationally assigned; the first-party alternative-evidence and contradiction-to-rework feedback path is implemented.
- Decision owner: needs first-party-mode integration/developer composition for independent S3* authority; `Harness.recheck_step` owns deterministic reconciliation, not independent audit judgment.
- Supporting / enforcement mechanisms: criteria API, alternate camera/close-range flag, contradiction records, task reopening and offline regression tests.
- Closure path: policy claim → later direct criterion check → contradiction/reopening and marked evidence → S1 rework and future reflection. Distinct auditor authority is the missing component for `A`.
- Boundary reachability: `eep_verify` is exposed to the built-in Claude and MCP agents and `Harness.recheck_step` is shipped in the runtime; this is more than a test-only audit, though real detector independence is not established.
- Why this is / is not agent-owned: a same-loop verifier can provide valuable extra evidence but does not prove a separately controlled independent audit; C recognizes the material constructor without fabricating A.
- Evidence: [recheck and task reopening](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L615-L658), [robot adapter direct check](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/embodiment/adapters.py#L144-L201), [tool `eep_verify`](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/tools.py#L128-L140), [regression showing overturned completion](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/tests/test_regressions.py#L71-L91), [criteria](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/criteria.py#L1-L62).
- Basis: separate criterion and corrective-return path, conditional independence at the evidence level, missing independent audit ownership for A.
- Confidence: moderate; stronger simulation path than unverified real backend.
- Caveats: same backend may correlate failures; normal immediate completion-criterion checks alone would not suffice for S3*.

## S4 — Outside-and-then intelligence

- State: C
- Function: expose a capability-adaptation path using observed environmental difficulty and prospective targeted rehearsal, then return learned alternative guidance/coordination into subsequent work.
- External distinction: repeated physical-world failures in particular robot/model/skill/object contexts, e.g. occluded targets, look-alike stock, changed item placements and slow handling, compared across execution records and domain catalog.
- Future / prospective distinction: capability-gap severity and planned idle-time practice for troublesome contexts before the next customer/work task; this is an opportunity to develop/rehearse future response capacity, not just retry the current failed step.
- Adaptation option generated: `capability_gaps` groups recent failures, relative attempts and slowness; `plan_practice` generates low-priority repeated pick/return tasks; `RuleReflector` or optional `LLMReflector` mines successful recoveries and contradictions into contextual `patch` instructions.
- Path back into current capability / S3: practice runs produce execution records → evidence-checked `SharedAdmission` admits or rejects guidance/recovery/criteria/coordination patches → `GuidanceBuilder` and `_choose_robot` apply relevant memory on later dispatch/execution; weak non-safety memory can be retired based on outcome.
- Disturbance / variety regulated: foreseeable performance deterioration or new capability demands in observed external object/robot contexts.
- Decisive decision or feedback right: **whether and when** to run future-oriented practice, what capacity to spend, which gap to prioritize, and whether to make this a standing adaptation program. `eep_capability_gaps(schedule_practice=true)` is callable, but no automatic idle/foresight owner and no sustained whole-system adaptation conversation with S3 are assigned in the standard runtime.
- Decision owner: caller/developer must compose the autonomous S4 agenda and authority; deterministic gap ranking/practice creation and evidence-gated memory support do not by themselves own prospective choice. An optional Claude agent *could* call the constructor, but the shipped operator prompt lacks a recurring future-environment scan/idle planning loop.
- Supporting / enforcement mechanisms: execution record history, contextual failure aggregation, low-priority practice workflow, rule/LLM reflection, schema/evidence/safety admission, versioned long-term memory and replay tests.
- Closure path: environmental difficulty → exposed gap and practice option → caller-scheduled rehearsal → feedback/reflection/admitted patch → changed future guidance/robot preference. The function-specific construction path exists, but autonomous S4 initiative remains to be composed.
- Boundary reachability: `eep_capability_gaps` with `schedule_practice` and memory tools are actually in the shipped tool registry, not just a README roadmap; rule reflection and admitted patches run in standard simulation and the MCP mode. Physical extrapolation not claimed.
- Why this is / is not agent-owned: a reflective memory loop alone is not S4. The distinct prospective practice option and future capability return make this more than generic memory, while lack of a scheduled autonomous environmental/adaptation governor keeps it at C.
- Evidence: [capability-gap/practice construction](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/practice.py#L1-L125), [tool exposure](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/tools.py#L175-L211), [reflection](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/memory/reflection.py#L118-L155), [admission safety/evidence](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/admission.py#L190-L306), [memory application](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L334-L351), [architecture memory path](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/docs/architecture.md#L120-L192).
- Basis: first-party prospective gap/practice-to-later-capability constructor; no complete autonomous S4 decision loop or parent mode.
- Confidence: moderate.
- Caveats: gaps are mined from internal execution records of externally situated work, not broad market/strategy sensing. There is no robot-weight self-training; `flywheel.py` stops at dataset export.

## S5 — Policy and identity

- State: —
- Function: would decide or revise ultimate identity/mission and balance current robot operations against the future adaptation program.
- Disturbance / variety regulated: unresolved mission/safety/strategic-policy tensions beyond routine robot-task control.
- Decisive decision or feedback right: no first-party runtime path accepts a genuinely ultimate-policy question, routes it to legitimate authority, records an authoritative identity decision and returns it to govern subsequent operation.
- Decision owner: none evidenced for an active S5 loop; hard-coded safety constraints and user task goals do not constitute an identity governor.
- Supporting / enforcement mechanisms: domain safety rules, `SharedAdmission` rejection of unsafe guidance/memory, robot stop/resume, current-model prompt, human teleoperation example, repo contributor governance.
- Closure path: not established at ultimate-policy level; operational stop/resume and evidence-based memory patches affect tasks or safety settings rather than deciding identity or arbitrating S3–S4.
- Why this is / is not agent-owned: agent cannot revise ultimate mission under a dedicated first-party process, and no first-party parent institution/human S5 escalation-return path is supplied. Accepting task goals and protecting immutable safety flags are ordinary operating constraints.
- Evidence: [operator prompt/safety](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/agents/prompts.py#L1-L42), [admission rules](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/admission.py#L95-L155), [memory admission cannot weaken safety](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/admission.py#L190-L298), [robot stop/resume](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/opengeniemaster/harness/harness.py#L661-L681), [human backend](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/examples/human_backend.py#L1-L90), [research vs repo identity note](https://github.com/eust-w/opengeniemaster/blob/8f6dab22a54a318bf8afa221269a6f9c00fa860c/README.en.md#L1-L43).
- Basis: bounded negative conclusion for reviewed runtime rather than universal impossibility.
- Confidence: moderate-high within shipped modes.
- Caveats: a real deployment may have human/organizational identity governance outside this repository, but that external authority cannot be inferred here.

### Absence scope

- Surfaces inspected: `ClaudeAgent` and system prompt, EEP tool registry, runtime task/robot controls, `SharedAdmission`/memory governance, simulator/HTTP/manual robot modes, CLI and examples, contributor/CI/research adjacent material.
- Plausible first-party paths checked: agent instruction and task acceptance; human backend and robot emergency stop; admission's safety-policy locks; memory revision/retirement; external policy training data export; repository owner/contributor change process.
- Why no material first-party path remains: each shipped path either performs a task, protects a preselected constraint, modifies contextual operational guidance, or lies outside the runtime. None has the identity-level matter → legitimate ultimate authority → binding decision → return-to-operation chain required for S5.

## Distributed OSS parent arrangement

This is a community-maintained independent reproduction of publicly described AGIBOT concepts, not the official upstream product. Repo maintainers and independent users may configure their own fleet/credentials or submit code, but the reviewed first-party standard distribution has no common shared organization-level human parent governing an operating fleet. Repo CI/issues/releases and example human-backed robot execution do not establish S3/S4/S5 parent-mode ownership for a deployed local work system. No `(P)` is credited.

## Self-hosted and non-human modes

The self-hosted MCP/HTTP fleet route is supported but requires external robot services, independent safety equipment and a separately supplied coding agent. `examples/human_backend.py` makes one robot act through a human and is **not** a parent-governed whole-system mode. The built-in Claude loop provides narrow S1/S2 model-decision ownership on simulation; script-only and physical modes must not inherit that by label. No separate non-human swarm with autonomous S3/S4/S5 decisiveness is shown.

## Recursion

At the assessed project recursion, robot work cells execute domain work while a central coding agent and harness provide task context, resource distribution, controls, verification and adaptation constructors. An individual robot's low-level policy may itself have internal control loops, but its VSM viability and ultimate authority are not established by these adapters and no extra nested S3/S5 claim is made. A single `ClaudeAgent` orchestrating many robots is not itself evidence of many coding-agent S1 units.

## Variety and escalation

EEP attenuates task variety through domain workflows, capability filters, graph dependencies, group affinity, admission and deterministic recovery options. The agent amplifies local response variety through guided observations, alternate cameras, reference images, retries and handoffs; feedback is returned as evidence fields and continuity. Safety stops/people intrusions produce fail-closed pauses and require explicit resume. Shared memory proposals are constrained by unique execution-record evidence, conflict/safety guards and later use/retirement feedback. No separate exceptional algedonic bypass to a higher identity authority is supplied; a robot stop is an operational safety path, not an S5 signal by itself.

## Evidence gaps

- External Anthropic model calls and physical-robot E2E were intentionally not run (no paid provider E2E); the first-party tool-loop path is source-visible, and 100 frozen-source offline tests passed.
- The simulator's policy/check realism and detector independence are not evidence of a deployed independent S3* auditor; external HTTP `/check` can be implemented using correlated sensors or logic.
- There is no demonstrated continuous autonomous S3 fleet-governance policy or S4 prospective monitor/idle-practice scheduler in the shipped Claude prompt; both are classified as concrete constructors, not full ownership.
- The long-term memory adaptation changes guidance/recovery/criteria/coordination rules, not policy weights, and the `flywheel` exports offline samples without training.
- AGIBOT's official GenieMaster implementation, protocols and operating model are **not** inherited; this is a distinct OSS repository at a frozen commit. All source confidence is local to 8f6dab22a54a318bf8afa221269a6f9c00fa860c.
