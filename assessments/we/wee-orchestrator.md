---
harness_id: wee-orchestrator
project_name: Wee-Orchestrator
repository: https://github.com/leprachuan/Wee-Orchestrator
review_ref: 4f34d5737910098c79f2ee42d0f3f383cfca830f
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Wee-Orchestrator

## Review boundary

- System in focus: one self-hosted Wee-Orchestrator deployment with configured agent workspaces, sessions and background commitments.
- Purpose and identity: provide persistent multi-channel agent work and observable, operator-controllable background execution.
- Relevant environment: user requests, workspace files, tools, model/runtime providers, delegated domain tasks, runtime failures and authenticated operators.
- Standard-distribution boundary: Python API/SessionManager, native Wee Copilot-SDK BYOK mode, first-party tools, supported external runtime adapters, background manager/scheduler and clients of the same API.
- Credited operating / distribution surfaces: agent_manager.py, wee_copilot_sdk.py, native tool/dispatch code, session isolation, background task state, authenticated task views/cancel/steer and documented deployment.
- Adjacent first-party surfaces excluded from ownership: repository development/self-improvement agent examples, contributor governance, tests/fixtures, CI/release and historical development reports. Provider SDK/CLI internals and separately operated services do not donate additional organizational rights.
- First-party operating / deployment modes considered: installed self-hosted native Wee provider session, configured CLI/SDK agents, quick delegation and background tasks, operator dashboard/API, optional router, scheduler, memory and updater. No live provider task executed.
- Recursion level: one deployment with bounded domain work cells; nested sessions/delegation do not themselves prove recursive viable organizations.
- Reviewed revision: 4f34d5737910098c79f2ee42d0f3f383cfca830f.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

A shared SessionManager serves authenticated API/client channels, loads configured agents and workspace context, persists sessions/history and dispatches selected runtimes. Native Wee resolves an Ollama/OpenRouter-compatible provider through the Copilot SDK, supplies search/delegation/browser/shell and provider-specific native tools, and processes returned events and session continuation. The SDK supplies model/tool-loop execution; first-party assembly makes those tools and persisted feedback reachable. The model chooses substantive work/tool calls; fixed prompt/tool/permission settings constrain it.

Background jobs receive distinct sessions, runtime/model/permission configuration, a queue, execution history, status and cancellation. A documented file-based steering channel returns operator instructions to active background work. Delegation has explicit caller/child session isolation to prevent an invoked agent from overwriting the caller's selected agent/session state. The optional LLM router chooses a runtime/model for a request, subject to availability, cooldown, allowlist and fallback; this does not itself own a deployment-wide resource bargain. Memory injection/promotion and software update machinery persist or transport change without automatically establishing prospective intelligence.

Evidence: [README.md](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/README.md#L8-L22), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L10155-L10236), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L10460-L10520), [wee_copilot_sdk.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/wee_copilot_sdk.py#L407-L428), [wee_copilot_sdk.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/wee_copilot_sdk.py#L472-L532), [docs/background-tasks.md](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/docs/background-tasks.md#L1-L17).

## Operational model

Configured domain agents perform real workspace/user transformations; the first-party native route connects provider cognition to useful local/delegated tools. The runtime owns enforcement, storage and dispatch mechanics. Parent current-control decisions remain with the legitimate local deployment operator, who can see all background commitments, stop selected work, free capacity and redirect active work. S2=C is based specifically on evidenced caller/child state interference prevention, not on the existence of delegation or a queue.

## S1 — Operations

- State: A
- Function: perform user/domain work by selecting substantive actions, invoking tools, interpreting results and returning usable output.
- Disturbance / variety regulated: heterogeneous requests, uncertain workspace state, tool failures and changing information.
- Decisive decision or feedback right: choose how to accomplish the task, which tool/action to invoke and what result to return.
- Decision owner: model-backed configured agent, including the native Wee SDK session.
- Supporting / enforcement mechanisms: SessionManager context, agent workspace, provider resolution, SDK transport, first-party tool adapters, session/history persistence, timeout/permissions and event normalization.
- Closure path: first-party tools return results to the SDK/model session; outputs/events are persisted and resumed with the selected agent context. Quick delegation returns child results; background delegation returns task identity and observable completion state.
- Boundary reachability: normal run_wee_native builds the agent prompt, registers first-party tool handlers, calls execute_wee_copilot with working_directory/tools and saves the resulting session ID. The supported installation supplies this assembly without a custom external controller.
- Why this is / is not agent-owned: model discretion determines substantive actions/output; removing it leaves routing/enforcement rather than the same work judgment.
- Evidence: [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L10155-L10236), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L10460-L10520), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L11269-L11377), [wee_copilot_sdk.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/wee_copilot_sdk.py#L472-L528).
- Basis: structural and documented supported mode.
- Confidence: high for source path.
- Caveats: a configured/provider-authenticated SDK or external CLI is required; no live quality or reliability claim is made. SDK transport is support and does not inherit every first-party VSM function.

## S2 — Coordination

- State: C
- Function: attenuate interference between a caller work cell and independently invoked domain agents that share session-management infrastructure.
- Disturbance / variety regulated: delegated execution overwriting the caller's agent/session_map entry, causing later work to run under the wrong domain/session; multiple delegations can otherwise contaminate the same caller context.
- Decisive decision or feedback right: isolate child dispatch state and restore/preserve caller context while returning the child's output.
- Decision owner: deterministic first-party delegation/session-isolation path. No autonomous agent-owned arbitration policy is established.
- Supporting / enforcement mechanisms: is_delegation flag, unique delegation session key, copied channel/identity, separate agent field, session-map lock and cleanup.
- Closure path: child dispatch uses its isolated key and returns its result; ephemeral state is cleaned while the caller retains its original agent/session, governing subsequent dispatch. The interference is prevented rather than merely logged.
- Boundary reachability: /agent invoke and detected one-off delegation enter the supported _execute_with_context path; tests exercise those same production methods with mocked dispatch.
- Why this is / is not agent-owned: model choice to delegate does not own the isolation rule. A function-specific stabilization path is shipped, while autonomous coordination judgment would require composition.
- Distinct S1 units: caller agent and invoked domain agents executing their own bounded workspace tasks.
- Inter-S1 disturbance: shared caller session-map mutation can switch subsequent caller work into a delegate's domain/context.
- Attenuating coordination relation: isolate each child in a unique ephemeral context and preserve caller state.
- Feedback into subsequent S1 behaviour: returned child output is available to the caller without changing its active agent; later caller work therefore remains in its intended domain.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: production code explicitly identifies and prevents the concrete session overwrite defect; preserving caller context, not merely sending a child task, is the credited relation.
- Evidence: [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L7229-L7278), [tests/test_delegation_session_isolation.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/tests/test_delegation_session_isolation.py#L99-L159), [tests/test_delegation_session_isolation.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/tests/test_delegation_session_isolation.py#L276-L334).
- Basis: structural; concrete first-party interference regression witness.
- Confidence: medium-high.
- Caveats: this is context-isolation coordination, not shared-file conflict mediation, agent-negotiated resource allocation or an autonomous S2 regulator. Queue/concurrency limits alone are not the witness.

## S3 — Inside-and-now control

- State: P
- Function: regulate deployment-wide current background commitments and intervene in active work on behalf of the whole.
- Disturbance / variety regulated: stalled/unwanted tasks consume capacity, priorities change, or an active task needs direction under current constraints.
- Decisive decision or feedback right: inspect the current task portfolio, terminate a selected running/queued commitment, admit replacement work or supply binding current-task steering.
- Decision owner: legitimate authenticated operator of this self-hosted deployment, not the deterministic background manager or request-level model router.
- Supporting / enforcement mechanisms: global authenticated task list/details/transcripts, process-group cancellation, queue promotion, steering files, per-agent capacity/timeouts, scheduler and client UI.
- Closure path: operator reviews current tasks, kills a selected task and frees capacity for queued work; steering is timestamped and written to the task's channel, whose injected instructions require the agent to check and incorporate new guidance during subsequent work.
- Boundary reachability: normal API exposes whole-deployment background views, cancellation and steer; _run_background_task injects the consumption contract. This is a first-party operator mode, not repository developer governance.
- Why this is / is not agent-owned: neither fixed queue limits nor LLM selection of a provider for one prompt supplies an autonomous deployment-wide commitment decision. The operator selects the intervention and runtime machinery implements it.
- Whole-system current view: background task set with agent/runtime/model, prompt summary, status, creation/completion, failure/fallback and detailed transcripts/tool calls.
- Current-control decision scope: active/queued work commitments, capacity release, replacement scheduling and substantive steering across this deployment.
- Evidence: [docs/background-tasks.md](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/docs/background-tasks.md#L3-L9), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L16562-L16606), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L16705-L16749), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L16765-L16789), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L15746-L15754).
- Basis: explicit operator contract and structural return path.
- Confidence: high for cancellation/capacity closure; medium for instruction-following steering.
- Caveats: all authenticated users can inspect/cancel background tasks under this documented coarse local authority model; fine-grained tenant governance is not claimed. Steering consumption is an agent instruction, not a guaranteed hard interrupt. The positive parent witness includes portfolio visibility/intervention, not only an isolated stop button.

## S3* — Complementary audit

- State: —
- Function: sought complementary independently governed access that can challenge routine operational success claims.
- Disturbance / variety regulated: misleading task reports or incomplete tool execution.
- Decisive decision or feedback right: no first-party independent audit judgment-to-control loop is established.
- Decision owner: no audit owner credited; ordinary agents, runtime event parsers and operators provide normal reporting/review.
- Supporting / enforcement mechanisms: transcripts, logs, normalized tool events, process-liveness reconciliation, watchdog and anti-hallucination retry.
- Closure path: normal status/errors reach task views and retries; these do not add an independently governed complementary operational-reality channel.
- Why this is / is not agent-owned: the producing path and runtime monitor supply routine observations; a regression file called tool audit does not install an independent auditor in the deployment.
- Evidence: [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L10477-L10513), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L16574-L16606), [tests/test_issue111_wee_tool_audit.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/tests/test_issue111_wee_tool_audit.py#L1-L23).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: arbitrary delegated reviewers or external auditors can be composed but are not a first-party function-specific S3* path in this supported deployment.

### Absence scope

- Surfaces inspected: native execution/event handling, transcript/tool-call views, background watchdog/reconciliation, anti-hallucination retry, delegation and tool-audit tests.
- Plausible first-party paths checked: producer retries, process liveness, operator raw transcript viewing, separate delegated reviewer and audit-labelled regression checks.
- Why no material first-party path remains: inspected mechanisms validate/report the ordinary execution path; no shipped independent audit selection/access/judgment and returned corrective control relation is established. Tests/development review remain adjacent.

## S4 — Outside-and-then intelligence

- State: —
- Function: sought externally and prospectively informed capability adaptation coupled to current operation.
- Disturbance / variety regulated: future mismatch of runtimes, skills or operating strategy to environmental change.
- Decisive decision or feedback right: no first-party external/future options-to-adoption loop is established.
- Decision owner: router model chooses a current request's provider; humans configure/update software; neither alone establishes S4 ownership.
- Supporting / enforcement mechanisms: runtime/model discovery, request router, cooldown/fallback, per-agent memory injection/promotion, skill installation and software updater.
- Closure path: provider selection affects the current request, memory persists previous information and updater transports chosen releases. No distinct prospective adaptation-option evaluation/return path is specified.
- Why this is / is not agent-owned: current routing and generic memory are not externally prospective intelligence; repository self-improvement tasks cannot supply ownership to the installed service merely through co-location.
- Evidence: [llm_router.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/llm_router.py#L25-L43), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L11917-L11985), [memory/inject.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/memory/inject.py#L60-L116), [scripts/promote_all_agents_memory.sh](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/scripts/promote_all_agents_memory.sh#L1-L8), [update_launcher.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/update_launcher.py#L15-L44).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: user-authored research/self-change tasks could realize a different boundary; no claim that such a system is impossible.

### Absence scope

- Surfaces inspected: optional router/configuration and cooldown, model discovery, memory injection/daily/promotion, skill surfaces, update launcher, heartbeat and development-agent documentation.
- Plausible first-party paths checked: model-aware runtime selection, fallback after failure, memory promotion, release update and configured self-improvement agent.
- Why no material first-party path remains: present-request provider choice and generic persistence/update machinery supply no function-specific external/prospective adaptation contract. Development-agent examples and an empty/test heartbeat do not close the service's S4.

## S5 — Policy and identity

- State: —
- Function: sought runtime identity/ultimate-policy resolution at deployment recursion.
- Disturbance / variety regulated: unresolved conflict between the deployment's purpose, current commitments and future change.
- Decisive decision or feedback right: no identity-level matter-to-legitimate-authority-to-returned-policy loop is established.
- Decision owner: operator authors agent configuration, access and permissions; no S5 mode credited from those generic rights.
- Supporting / enforcement mechanisms: authentication, configured domain descriptions, permission modes, initial prompts, runtime allowlists and ordinary task steering.
- Closure path: configuration/steering changes operational settings and work, without an explicit identity/ultimate-policy adjudication path.
- Why this is / is not agent-owned: permission handling and user final say over a task do not establish ultimate policy. The model is not shown owning deployment identity.
- Evidence: [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L7379-L7408), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L16437-L16469), [agent_manager.py](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/agent_manager.py#L16765-L16789), [docs/background-tasks.md](https://github.com/leprachuan/Wee-Orchestrator/blob/4f34d5737910098c79f2ee42d0f3f383cfca830f/docs/background-tasks.md#L3-L9).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: local operator S3 and generic permission approval are kept separate from S5; contributor/release authority is outside this runtime boundary.

### Absence scope

- Surfaces inspected: agent/context/configuration loading, authentication, permission resolution, task steering/cancellation, operator docs, router policy and adjacent contributor governance.
- Plausible first-party paths checked: user role/mission text, elevated/restricted permissions, allowlists, agent configuration edits and background instructions.
- Why no material first-party path remains: these provide setup, access or present-task control, not an identity issue routed to legitimate ultimate authority and returned to govern the deployment under a specific first-party contract.

## Recursion

Configured domain workspaces can be separate operational cells; spawning a child/background session is not proof of recursive viability. Operator parent control is local to the self-hosted deployment, not a claim about the OSS organization. Model/provider and external service internals are outside this assessment.

## Variety and escalation

Native tools and specialist delegation amplify response capacity; context compaction and workspace scoping attenuate input volume. Ephemeral delegation state reduces domain contamination. Queue limits, cooldowns, timeout/fallback and visible errors regulate runtime load while operators intervene through current-control channels. A status/watchdog alert alone is not an algedonic channel or a new VSM function.

## Evidence gaps

Pinned source-first review without a live model/provider or agent E2E. Native deterministic tests passed: background-default isolation plus mocked SDK BYOK 25/25, delegation-session isolation 11/11, router/configuration/mock dispatch 50/50 (86 total). Initial missing pydantic in the isolated test environment was repaired and the full affected 50-test suite rerun successfully without upstream changes. Steering is instruction-based and depends on agent compliance. The root LICENSE is GPL-3.0 text although README displays an MIT badge; the frozen intake's GPL-3.0 observation is preserved and no license interpretation/change is made by this assessment.
