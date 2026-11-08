---
harness_id: openprogram
project_name: OpenProgram
repository: https://github.com/FuzzyKuji/OpenProgram
review_ref: 447264865e871e30e7f638b42cccfe25d826f8d0
reviewed_at: 2026-11-08
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# OpenProgram

## Review boundary

- System in focus: the first-party OpenProgram Python agent harness and supported CLI/web/desktop-managed local worker, including registered tools, saved Agent configurations, model execution, conversation/job dispatch, worktree control, optional always-on team agents and separately governed self-update.
- Purpose and identity: a programmable, model-backed personal/team agent workspace in which agent calls can select tools, maintain a conversation DAG, delegate to child/peer agents, and persist reusable Agent definitions.
- Relevant environment: user-selected external models and credentials, user workspace/files, web sources, local processes, Git repositories, owner-operated UI/API, local memory and program directories.
- Standard distribution: `openprogram` CLI and `openprogram web` load first-party runtime; model providers and operating-system primitives are external dependencies. Installed built-in specialists are supported configurations, **not** automatically enabled background jobs.
- Credited operating / distribution surfaces: `openprogram/runtime/agent/`, `runtime/conversation/`, `runtime/jobs/`, `runtime/agent_registry/`, `runtime/commands/`, `programs/tools/`, `state/worktree/`, `operations/worker/`, user-facing CLI/web integration and the implemented always-on and self-update modules.
- Adjacent first-party surfaces excluded from ownership: documentation aspirational architecture, examples and test doubles, upstream LLM inference, Git merge engine, host OS, GitHub repository maintainer governance, third-party MCP servers, future user-authored Programs and any unconfigured multistage pipeline.
- Supported modes distinguished: ordinary interactive model/tool loop (default); optional named subagents and concurrent Jobs/worktrees; **configured** saved Coordinator/Chief of Staff and independent PR Verifier conversations; **operator-authorized** saved Agent identity changes; separately invoked first-party update verifier. No end-to-end provider/model success is assumed.
- Recursion level: the owner's OpenProgram workspace and managed Agent conversations/Jobs, not the OpenProgram OSS maintainer organization. A spawned child is an S1 execution unit; a saved AgentSpec is configuration, not an extra viable system by itself.
- Reviewed revision: `FuzzyKuji/OpenProgram@447264865e871e30e7f638b42cccfe25d826f8d0`; observation `2026-11-08`, Index-active Profile `0.2.4` / Methodology `0.3.7`.

## Repository architecture

This is executable first-party agent infrastructure rather than a prompt-only wrapper. `Agent.__call__` and the installed model/tool loop invoke provider-backed decisions, registered tools return observations, and the context/session runtime persists and resumes work. `agent(...)` starts a separate branch and Job; background results return to the caller. The shared job governor independently enforces dispatch capacity. A local Git-worktree manager creates isolated branches and returns named conflicts on merge. Built-in `Coordinator`, `Chief of Staff`, producer and verifier are installed as editable saved Agent configurations; the always-on scheduler is opt-in. The extensive design docs are used only where corresponding source/operating tests exist ([Agent class](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent/agent_class.py#L18-L125), [agent Job dispatch](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/conversation/sub_agent_run.py#L295-L430), [resource dispatch](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/jobs/resource_governance/dispatch.py#L20-L143), [built-in Agent installation](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/builtin_agents.py#L344-L377)).

## S1 — Operations

- State: A
- Function: model-directed coding, web/file/shell operations, multi-turn reasoning, and delegated specialist execution with concrete tool-result feedback.
- Disturbance / variety regulated: changing user tasks, unknown files and webpages, failed tool actions, incomplete implementation results, and context-dependent follow-up instructions.
- Decisive decision or feedback right: an invoked model chooses actual model response/tool calls and how to continue after receiving results; a child/peer model chooses its own assigned work actions inside its own branch.
- Decision owner: active configured Agent model for each conversation; user-selected provider is an external implementation dependency.
- Supporting / enforcement mechanisms: `Agent` Python call API, model loop/tool dispatch, tool registry, permission gate, conversation DAG, context assembly, Job/run state, file/edit/shell/web tools and optional worktree context.
- Closure path: user or another authorized Agent supplies a task; runtime assembles current context, model requests tool calls, first-party tool dispatch obtains observations/errors, and the next model turn may repair, retry, delegate or conclude. Background child completion returns to the invoking conversation.
- Boundary reachability: public `openprogram` CLI/web entrypoints reach first-party Agent runtime and registered tools; `agent` tool reaches `run_agent_turn`/`run_agent_turn_async`; child work is admitted as canonical Job rather than only documented in a scenario.
- Why this is / is not agent-owned: tool selection and next-step adaptation are model decisions; deterministic permissions and execution adapters support them without becoming the S1 decision maker.
- Evidence: [Agent call](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent/agent_class.py#L95-L126), [tool dispatch](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent/loop/tool_dispatch.py), [child execution](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/conversation/sub_agent_run.py#L295-L430), [registered tools](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/programs/tools/).
- Basis: shipped executable source, component/unit tests and documented standard invocation; no credentialed live-model E2E.
- Confidence: high for first-party tool/model return wiring; provider success rates and operational safety are not measured.
- Caveats: account setup, configured model and requested tool permissions are required. Python `Agent` instance methods are not automatically model tools unless explicitly registered; claims of universally automatic self-programming must not be generalized to every mode.

## S2 — Coordination

- State: C
- Function: attenuate capacity interference among separate active Agent conversations/Jobs and give a worktree-using coordinator an explicit integration/conflict feedback surface.
- Disturbance / variety regulated: independent child/peer Jobs contending for global/session execution slots, simultaneous claims of the same queued work, and incompatible edits from multiple worktrees when integrating source changes.
- Decisive decision or feedback right: first-party capacity governor selects eligible queued Job claims and defers saturated sessions; an appropriately equipped coordinator model can then respond to a typed `merge_conflict`/`not_fast_forward` result by revising or deferring an integration.
- Decision owner: deterministic Job governor for scheduling/capacity settlement; configured coordinating Agent for the optional subsequent worktree-repair decision, not an automatically present global LLM mediator.
- Supporting / enforcement mechanisms: durable Job admissions, `claim_next` oldest-eligible selection, per-session/global capacity, lease/worker lock, worktree lifecycle states, conflict-returning `merge_worktree`, and `job_output`/worktree tools.
- Closure path: conflicting Job demand is admitted/queued; saturated sessions are skipped until slots release, and an eligible peer eventually starts with fresh execution context. In the optional worktree mode, conflicting source branches remain active on typed failed merge; the caller receives the error and can ask its agent to change/retarget work before reattempt.
- Boundary reachability: both concurrent Jobs and worktree operations are registered, exercised first-party execution paths; component tests cover skipping an older saturated session, dual claim prevention and failed merge preserving active worktree. This is a **composable** coordination relation, not evidence of an automatic model conflict-resolution team on all fresh installs.
- Why this is / is not agent-owned: the affected units are individually model-backed S1 branches, while the attenuation is primarily an implemented deterministic subsystem. C credits this cross-S1 facility and optional model composition; it does **not** claim S2=A autonomously negotiates conflicting task intentions.
- Distinct S1 units: independent model-backed subagent or saved Agent conversations whose Jobs can be live concurrently.
- Inter-S1 disturbance: actual global/session execution saturation and competing edits from distinct worktrees, not abstract task ordering.
- Attenuating coordination relation: capacity reservations/eligibility prevent exceeding limits, skip one saturated session to make another eligible, and worktree isolation plus typed merge failure prevents blind overwrite during integration.
- Feedback into subsequent S1 behaviour: released capacity starts the next Job; failed worktree merge preserves the branch and exposes its error to the agent/tool caller so subsequent S1 work can repair before merging.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the governor's admission decisions explicitly depend on *cross-Job capacity interference* and the worktree merge path explicitly represents *cross-edit collision*; mere `send_message`, a shared DAG or parallel queries are not credited.
- Evidence: [cross-session claim loop and limits](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/jobs/resource_governance/dispatch.py#L69-L142), [conflict feedback/active branch retention](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/state/worktree/manager.py#L354-L475), [dispatch tests](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/tests/component/runtime/test_resource_governance/test_dispatch.py#L62-L123), [worktree failure tests](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/tests/component/core/test_worktree_manager.py#L156-L185).
- Basis: first-party dispatcher, worktree manager and executable component tests.
- Confidence: medium-high for bounded mechanical conflict attenuation; low for an unconfigured agent-driven negotiation loop.
- Caveats: path warnings outside worktree are not a hard sandbox, and Git itself performs the merge. Capacity scheduling does not semantically detect two tasks editing the same path. The optional model retry is a possible feedback response, not an observed autonomous repair success.

## S3 — Inside-and-now control

- State: C
- Function: in a configured coordinator mode, maintain an owner-workspace view of current work, agent status and Jobs, select next responsibility and reassign/delegate based on returned work status.
- Disturbance / variety regulated: overdue/in-flight work, idle specialist conversations, blocked tasks, active/queued Jobs, failed handoffs and changing immediate user priority.
- Decisive decision or feedback right: the Coordinator/Chief of Staff model may read open work and current agent/job state, decide assignment or next task and send a bounded handoff; recipient execution and reply flow back into later coordinator turns.
- Decision owner: owner-selected coordinating Agent model; human enables always-on and chooses its permissions/mission; Job governor enforces but does not choose project priorities.
- Supporting / enforcement mechanisms: saved `Coordinator` and `Chief of Staff` system/tool configurations, `list_agents`, `open_work`, `list_jobs`/`job_output`, `handoff`/`send_message`, always-on wake/check-in and return notices, persisted Goal/Job status.
- Closure path: a live status or scheduled wake enters the coordinator conversation; it reads available work and cross-agent status, selects next owner/step and sends an authorized handoff; target executes in its independent Agent context and sends a completion reply, which alters the next current-control view.
- Boundary reachability: the shipped `create_builtin_agents` installs roles with planning/status/delegation tools; owner can enable a saved Agent's always-on mode; handoff and Job return are implemented with recovery and loop limits. Neither an installed template nor a default disabled ticker automatically proves every instance runs that coordinator.
- Why this is / is not agent-owned: current cross-work allocation is decided by a configured model rather than by a fixed queue; C reflects opt-in composition and limited scope rather than a universally active autonomous S3 manager.
- Whole-system current view: for the owner-selected Agent portfolio, open work, addressable conversations, in-flight Job state and returned status; not an external organization's finances or all agents on other users' instances.
- Current-control decision scope: prioritization and delegation among current user-visible jobs, targeted recovery/escalation and reporting, bounded by saved Agent permissions and owner instructions.
- Evidence: [Coordinator and Chief of Staff built-ins](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/builtin_agents.py#L54-L104), [built-in installation](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/builtin_agents.py#L344-L377), [durable handoff and reply](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/conversation/always_on/handoff.py), [always-on wake loop](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/conversation/always_on/ticker.py#L91-L170).
- Basis: first-party configurable role registry and execution feedback; component tests of handoffs and wake turns.
- Confidence: medium for the constructed S3 control loop; default-runtime universal coverage is explicitly not claimed.
- Caveats: resource-capacity governor alone is not model-owned S3, and current delegated task summaries are not independent audit. All built-in always-on roles begin disabled; owner must configure and activate the relevant mode.

## S3* — Complementary audit

- State: C
- Function: optionally attach a separate read/test-only PR Verifier Agent to inspect a producer's actual work and return a corrective verdict to the coordinating/producing conversation.
- Disturbance / variety regulated: a producer's untested, incorrect or misleading completion claim may otherwise be accepted from its own status summary.
- Decisive decision or feedback right: the separate PR Verifier model reads the specification, code/diff and real test outputs, then returns `ship`, `fix first` or `reject` and numbered findings; parent/producer may decide corrective work.
- Decision owner: separately configured verifier conversation for the judgment; parent agent/operator for what action to take on findings, not a hard automated PR merge veto.
- Supporting / enforcement mechanisms: distinct `pr-producer`/`pr-verifier` built-in AgentSpecs, verifier allowlist without write/edit tools, `handoff`/return-reply, named conversation/branch, worktree list and read/terminal access.
- Closure path: producer records work and requests a separate verifier handoff; verifier reads **actual shared project files** and runs checks independently of the producer's narrative; its reply arrives back at the sender for rework or operator delivery.
- Boundary reachability: the installed verifier has explicit read/test permissions and no write/edit tools, and real first-party handoff transport returns a separate Agent's result. This is composable when invoked; there is **no default mandatory reviewer before a Git merge or update**.
- Why this is / is not agent-owned: independent evaluation belongs to a different model-backed conversation with separate tool rights. A model merely summarizing its own tests or the deterministic update installer verifier alone would not establish this claim.
- Claim being audited: the producer's assertion that a change implements the handed specification and passes its tests.
- Ordinary reporting path: producer's task completion, change summary and claimed test results, as received by its parent.
- Complementary access path: verifier can inspect files/diff through read and code-navigation tools and invoke read-only test commands via shell, without relying only on producer's summary.
- Independence boundary: separate AgentSpec, conversation/turn and read-only allowlist; not a different GitHub organization, independent account, trusted third-party audit, or a proven mutually untrusted sandbox.
- Who acts on findings: configured coordinating agent, producer on a subsequent task, or local human owner receives the returned verdict and may request correction or block delivery.
- Evidence: [producer vs verifier roles and allowlists](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/builtin_agents.py#L143-L186), [returning handoffs](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/conversation/always_on/handoff.py), [handoff end-to-end test](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/tests/component/runtime/test_always_on_end_to_end.py#L217-L262), [independent self-update controller boundary as separate *non-agent* safety evidence](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/operations/self_update/verification/verification.py#L48-L145).
- Basis: constructed separate reviewer path plus source-level code/tests; no observed live LLM reviewer run or enforced reviewer acceptance gate.
- Confidence: medium for configurable complementary access; low for automatic per-change independent assurance.
- Caveats: role prompt forbids editing but a permitted `bash` may alter files; independent read/test intent is not a sandboxed read-only process guarantee. The distinct self-update verifier is deterministic controller-side verification, not automatically an S3* model auditor for every user task.

## S4 — Outside-and-then intelligence

- State: —
- Function: no verified closed agent-owned chain that senses external future change, selects a strategic capability/market option and returns that choice as an enduring adaptation of the managed agent organization.
- Disturbance / variety regulated: future tools, models, changing external knowledge and workflow requirements could require adaptation, but inspected functionality does not establish the full strategic closure.
- Decisive decision or feedback right: no single first-party, reachable, closed prospective option-selection right identified. The `Research Desk` may search current sources and report; arbitrary agent code edits may create new tools, but they are not automatically coupled into a future-intelligence decision loop.
- Decision owner: owner/configured agents decide what to research or edit, with ultimate option integration normally requiring task instructions or user permission.
- Supporting / enforcement mechanisms: optionally always-on Research Desk, `web_search`/`web_fetch`, persistent Memory, first-party program hot-loader/self-programming methods, manually editable AgentSpecs.
- Closure path: external updates can reach research briefs and user/agent actions; however the shipped role and tool wiring does not guarantee a future-oriented choice that changes strategy/capability and then verifies the enduring return to execution.
- Why this is / is not agent-owned: external browsing is sensing, reusable self-programmed methods are extensibility and current S1 programming; their existence in the same repository is not proof of a separate S4 cycle.
- Evidence: [Research Desk prompt/tool role](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/builtin_agents.py#L188-L208), [opt-in always-on scheduler](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/conversation/always_on/ticker.py), [Agent method registration](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent/agent_method.py#L107-L166), [ordinary agent class](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent/agent_class.py#L18-L68).
- Basis: supported role/module source plus explicit absence of a coupled strategic decision/return path.
- Confidence: medium within default and declared always-on modes; does not rule out a user-composed S4 program.
- Caveats: the README's self-evolution and proactive-agent promises are not treated as proof of completed outside/then organizational learning.

### Absence scope

- Surfaces inspected: research-desk built-in, always-on ticker/wake/report, Memory and Goal features, registered Agent methods, program tools and hot-load documentation, current coordinator roles and self-update subsystem.
- Plausible first-party paths checked: scheduled web research, reusable self-generated tools, external model/provider selection, package updater and per-task re-planning.
- Why no material first-party path remains: none ties independent forward-looking external option generation to a strategic choice, authorized adoption and persisted organization-level capability/strategy return; actual future composition would need new explicit evidence.

## S5 — Policy and identity

- State: P
- Function: owner-controlled, durable change of the saved Agent's constitutive instructions, identity, permissions and standing goal, with the updated configuration read into subsequent execution.
- Disturbance / variety regulated: conflict between an Agent's persistent purpose/permission boundary and the owner's desired identity or authorization regime, not a one-off shell approval.
- Decisive decision or feedback right: local human owner may edit/revoke Agent configurations and decide whether a specialist can act, research or send externally; Agent cannot legitimately grant itself unrestricted policy rights.
- Decision owner: parent local user/administrator of the OpenProgram workspace; the Model and settings UI can suggest/configure but are not a new autonomous S5 authority.
- Supporting / enforcement mechanisms: versioned saved `AgentSpec` configuration, `agent_registry.manager.update`, selected tool allowlists, `always_on` enabled/autonomy/goal fields and permission-mode enforcement, tool resolution into runtime request.
- Closure path: authorized owner changes saved Agent policy/identity; registry stores the edited spec; later selected Agent calls resolve the updated tool/system instructions and execute under the new policy. A deleted built-in is not silently recreated on restart.
- Boundary reachability: the normal installed UI/API exposes saving/updating AgentSpecs; the same registry is used to construct future Agent runtime and tool policy. This is a human **P** mode, not S5=A agent self-constitutional authority.
- Why this is / is not agent-owned: ultimate legitimate acceptance is a human choice; autonomous delegated task reassignment or self-programming cannot, by itself, rewrite the top-level owner's authority.
- Identity / ultimate-policy issue: persistent AgentSpec instructions/allowlist and `always_on.autonomy` define what a named Agent is allowed and tasked to do across turns, distinct from a single conversation response.
- Ultimate authority in each claimed mode: local human owner is the only credited ultimate actor; the configured agent remains subordinate even if able to propose changes.
- Return-to-operation path: `manager.update` persists the edited AgentSpec, and `Agent._call_options`/runtime tool resolution uses the spec when the Agent runs again.
- Evidence: [saved configuration schema](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/manager.py#L290-L370), [config update](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/manager.py#L759-L835), [built-in deletion and edit persistence](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent_registry/builtin_agents.py#L344-L377), [AgentSpec policy resolution into calls](https://github.com/FuzzyKuji/OpenProgram/blob/447264865e871e30e7f638b42cccfe25d826f8d0/openprogram/runtime/agent/agent_class.py#L75-L115).
- Basis: first-party persisted config source and operating endpoint architecture.
- Confidence: medium-high for genuine human-controlled persistent Agent identity; no model-origin constitutional proposal/independent appeal workflow is claimed.
- Caveats: updating a child Agent task prompt is usually ordinary S3 delegation, not S5. Credit applies narrowly to authorized durable changes of the governing Agent's own identity/rules, not to OpenProgram maintainers editing GitHub source.

## Modes and ownership

| Mode / owner | S1 | S2 | S3 | S3* | S4 | S5 |
| --- | --- | --- | --- | --- | --- | --- |
| Standard chat/model tool loop | A | — | — | — | — | — |
| Concurrent Jobs + worktrees | A | C (capacity/conflict) | — | — | — | — |
| Opt-in Coordinator / Chief of Staff with handoff | A | C | C | — | — | — |
| Opt-in distinct PR Verifier | A | C | C | C | — | — |
| Owner edits durable Agent identity | A | — | — | — | — | P |

Aggregate vector denotes evidenced **supported modes**, not an assertion that all functions are enabled by default or independently autonomous simultaneously.

## Recursion

The hosted workspace can hold many independently model-backed Agents and named conversation branches, but only owner-selected coordinator and verifier modes are credited as potential metasystem roles. Child DAG branches, local subagent teams, installable Programs and background Jobs do not automatically become separate viable organizations or prove self-governing S4/S5 at nested levels.

## Variety and escalation

Provider/tool extensibility, Agent methods, file/browser/shell tools and specialist branching amplify response variety. Permissions, bounded/queued Jobs, task/job cancellation, worktree merge status and owner-set operating modes attenuate execution variety. Explicit worktree conflicts can return to a coordinator; Job capacity release allows deferred work to start; optional independent reviewer findings can return through handoff for correction. Neither generic context DAG nor mere resource metrics is promoted to independent strategic/policy intelligence.

## Evidence gaps

- Assessment is source- and first-party-test-backed; `pytest` is not installed in this assessment environment, so OpenProgram's upstream tests were **not** executed here. No credentialed live-provider E2E or external integration success is claimed.
- The shipped role registry supplies a Coordinator, Chief of Staff and PR Verifier, but their always-on modes are initially disabled and their cooperation is not a universal default workflow; S3/S3* are **composable C**, not automatic A.
- The Job governor and Git worktree manager have typed capacity/conflict feedback, but do not implement semantic collision detection or autonomous resolution of all simultaneous filesystem changes.
- The separate native self-update verifier is a valuable actual acceptance/rollback boundary; it is not credited as a universally independent model audit of arbitrary agent work.
- Self-programming and proactive Research Desk are real capabilities, but an autonomous external-future strategic-adaptation cycle has not been demonstrated; S4 remains unclaimed.
