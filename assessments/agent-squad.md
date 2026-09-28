---
harness_id: agent-squad
project_name: Agent Squad
repository: https://github.com/2FastLabs/agent-squad
review_ref: 31eccfeb0d546262d1d0ec2e2e5239186f8d2954
reviewed_at: 2026-09-15
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
last_checked_ref: 3d67629ca564eaf35ec7779115c45a42ee23a2bd
last_checked_at: 2026-09-28
assessment_changed_at: 2026-09-28
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Squad

## Review boundary

- System in focus: Agent Squad's repository-shipped Python agent orchestration/runtime at pinned revision `31eccfeb0d546262d1d0ec2e2e5239186f8d2954`, including classifier routing, registered `Agent` implementations, chat storage, and the optional first-party `SupervisorAgent` team-composition mode.
- Purpose and identity: accept user requests, select or compose suitable autonomous agents, preserve conversation state, invoke their model/tool-backed operating loops, and return task outcomes.
- Relevant environment: users and sessions, external model/provider services, tool and retriever backends, application-supplied agent definitions, and downstream systems reached by those agents.
- Standard-distribution boundary: the published Agent Squad library/runtime and its shipped Python orchestration, agent, classifier, storage, and supervisor surfaces. External model endpoints, user applications, and application-authored business/tool logic remain environment or parent composition.
- Credited operating / distribution surfaces: `python/src/agent_squad/orchestrator.py`, `python/src/agent_squad/agents/agent.py`, concrete shipped agent implementations, classifier/runtime integration, storage, and `python/src/agent_squad/agents/supervisor_agent.py` when the documented supervisor mode is composed.
- Adjacent first-party surfaces excluded from ownership: repository tests/examples/docs, CI/release activity, contributor governance, and `agent_overlap_analyzer.py` as an unwired diagnostic utility. Its repository search surface exposes the analyzer and tests but no standard runtime consumer that feeds its overlap labels back into later agent operation.
- First-party operating / deployment modes considered: ordinary classifier-based routing to one registered agent and optional `SupervisorAgent` composition in which a lead LLM can contact several registered specialists and aggregate their responses.
- Recursion level: one Agent Squad application/team organization. Registered agents can be autonomous operational actors, but mere nesting under a supervisor does not establish each as a complete viable recursive system.
- Reviewed revision: `31eccfeb0d546262d1d0ec2e2e5239186f8d2954`.
- Observation date: 2026-09-28 same-ref correction. Upstream was inspected through `3d67629ca564eaf35ec7779115c45a42ee23a2bd`; no commit after the accepted review ref changes `python/src/agent_squad/agents/supervisor_agent.py`, so the accepted boundary is not silently repinned.
- Generated Profile version: not recorded in the legacy artifact.
- Generated Methodology version: not recorded in the legacy artifact.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

`AgentSquad` registers agent objects, gives their descriptions to a classifier, classifies each incoming request, dispatches it to the selected agent, and stores the resulting conversation state. The abstract `Agent` contract gives concrete model/tool-backed agents the `process_request` decision surface used to produce operational outcomes.

`SupervisorAgent` is a separate optional composition mode. A lead Bedrock/Anthropic LLM receives a team list and a `send_messages` tool. It can contact several specialists in parallel, pass context to them, retain per-agent history, receive their responses, and synthesize the final answer. Its prompt explicitly says specialists are unaware of one another and the supervisor is their sole intermediary.

The repository also ships `AgentOverlapAnalyzer`, which computes TF-IDF similarity between agent descriptions and labels pairs as low/medium/high potential conflict. At the accepted revision, code search finds `analyze_overlap()` only in the analyzer and its test; no standard Agent Squad/Supervisor runtime path consumes those labels to alter subsequent agent behaviour. It is therefore an adjacent diagnostic surface, not credited S2 closure.

## Operational model

The primary operational units are the registered specialized agents that receive a routed or supervisor-delegated request and autonomously interpret it through their concrete model/tool-backed `process_request` implementation. Deterministic classification, storage, message transport, and tool-call plumbing support those decisions but do not themselves own the operational judgment.

The earlier assessment promoted Supervisor mediation to `S2=C` because it provides first-party cross-agent information exchange. Under Profile 0.2.4, that is insufficient. A positive S2 mapping additionally requires a concrete inter-S1 interference/conflict/oscillation, a relation specifically capable of attenuating that disturbance, and a feedback path that changes later S1 behaviour. The accepted runtime establishes delegation and information mediation, but does not tie that mediation to a specific destructive inter-S1 disturbance. The overlap analyzer names potential conflicts but is not wired into the operating loop. `S2` is therefore corrected from `C` to `—` at the same accepted repository revision.

## Primary evidence

- [`python/src/agent_squad/orchestrator.py`](https://github.com/2FastLabs/agent-squad/blob/31eccfeb0d546262d1d0ec2e2e5239186f8d2954/python/src/agent_squad/orchestrator.py) — agent registration, classifier selection, dispatch to one selected agent, chat history and response persistence.
- [`python/src/agent_squad/agents/agent.py`](https://github.com/2FastLabs/agent-squad/blob/31eccfeb0d546262d1d0ec2e2e5239186f8d2954/python/src/agent_squad/agents/agent.py) — first-party autonomous agent contract and `process_request` operating interface.
- [`python/src/agent_squad/agents/supervisor_agent.py`](https://github.com/2FastLabs/agent-squad/blob/31eccfeb0d546262d1d0ec2e2e5239186f8d2954/python/src/agent_squad/agents/supervisor_agent.py) — optional lead-agent team composition, parallel messages, per-agent history, sole-intermediary prompt and response aggregation.
- [`python/src/agent_squad/agent_overlap_analyzer.py`](https://github.com/2FastLabs/agent-squad/blob/31eccfeb0d546262d1d0ec2e2e5239186f8d2954/python/src/agent_squad/agent_overlap_analyzer.py) — descriptive TF-IDF role-overlap diagnostic; inspected as a plausible S2 path but not credited because no standard runtime feedback integration is established.
- [Upstream `SupervisorAgent` path history after the accepted ref](https://github.com/2FastLabs/agent-squad/commits/main/python/src/agent_squad/agents/supervisor_agent.py) — checked through upstream head `3d67629ca564eaf35ec7779115c45a42ee23a2bd`; no post-review commit changes this S2-relevant surface.

## S1 — Operations

- State: A
- Function: perform user-facing specialist work by interpreting a routed/delegated request and producing an outcome through the selected agent's model/tool-backed operating loop.
- Disturbance / variety regulated: heterogeneous user intents, task-specific context, conversation history, provider/tool responses, and task-domain uncertainty encountered by each registered specialist.
- Decisive decision or feedback right: decide how to process the assigned request and what response/tool-mediated result to produce within the concrete agent implementation.
- Decision owner: the selected model-driven `Agent` implementation; in supervisor mode each contacted specialist owns its delegated operational response.
- Supporting / enforcement mechanisms: classifier selection, `AgentSquad.dispatch_to_agent`, session/chat storage, provider adapters, tool configuration, streaming wrappers and metadata/logging.
- Closure path: user request → classifier or supervisor selects/delegates to an agent → agent `process_request` interprets and executes the task → result is returned and persisted into conversation state → later requests can use that state.
- Boundary reachability: the standard `AgentSquad` runtime directly invokes registered agents through `process_request`; `SupervisorAgent` likewise invokes team agents directly. No adjacent repository-development actor is required to expose this operating discretion.
- Why this is / is not agent-owned: the runtime transports and records the request/result, while the model-driven selected agent owns the substantive response/tool-use decision within its configured role.
- Evidence: `orchestrator.py`; `agents/agent.py`; concrete shipped agent implementations; `agents/supervisor_agent.py`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model providers execute model inference and application developers configure the available agents/tools; those dependencies do not remove the first-party runtime's shipped autonomous operating path.

## S2 — Coordination

- State: —
- Function: no material first-party operating path establishes disturbance-specific attenuation of interference, conflict or oscillation among distinct S1 units at this recursion.
- Disturbance / variety regulated: no qualifying inter-S1 disturbance is established. Supervisor specialists being mutually unaware is a communication topology, not evidence of destructive interference; lexical role overlap is only a diagnostic similarity signal.
- Decisive decision or feedback right: no S2-specific decision/feedback right is established.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: `SupervisorAgent.send_messages`, sole-intermediary context forwarding, parallel fan-out, per-agent histories, ordinary classifier routing, and the separate `AgentOverlapAnalyzer` diagnostic.
- Closure path: ordinary messages can influence later specialist responses, but the repository does not establish a disturbance-specific coordination result that is selected in response to concrete inter-S1 interference and then returned to change subsequent S1 behaviour.
- Why this is / is not agent-owned: the supervisor autonomously decides whom to contact for a user task, but delegation and information mediation do not become S2 without the required inter-S1 disturbance/attenuation relation. The overlap analyzer does not close the gap because its conflict labels are not wired into the operating runtime.
- Evidence: `agents/supervisor_agent.py`; `orchestrator.py`; `agent_overlap_analyzer.py`; repository search for `analyze_overlap()` consumers.
- Basis: current-contract same-ref correction.
- Confidence: high.
- Caveats: a downstream application could compose Supervisor messages or overlap diagnostics into a real conflict-resolution loop, but that would be a separate system-in-focus unless such closure becomes first-party and reachable in the reviewed distribution.
- Distinct S1 units: multiple registered specialist agents can be contacted in supervisor mode.
- Inter-S1 disturbance: not established as an actual or structurally evidenced operational interference/conflict/oscillation.
- Attenuating coordination relation: no relation is tied to a qualifying disturbance; sole-intermediary messaging is generic communication/delegation at this boundary.
- Feedback into subsequent S1 behaviour: agent history and forwarded context affect later replies, but not as demonstrated feedback from an S2-specific disturbance attenuation decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not; the accepted evidence supports generic routing, delegation and mediation only.

### Absence scope

- Surfaces inspected: ordinary classifier routing, registered-agent dispatch, SupervisorAgent team composition and message fan-out, per-agent storage/history, overlap analysis, and current upstream history of the SupervisorAgent implementation.
- Plausible first-party paths checked: supervisor as sole intermediary; parallel `send_messages`; conversation-memory forwarding; classifier selection; lexical overlap/potential-conflict analysis.
- Why no material first-party path remains: none reconstructs all four Profile 0.2.4 S2 requirements at the accepted boundary: concrete inter-S1 disturbance, attenuation relation specific to it, and feedback of that coordination result into later S1 behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no distinct first-party whole-system current-control function is established over a portfolio of S1 resources, commitments, priorities or constraints.
- Disturbance / variety regulated: not established as S3 at this recursion.
- Decisive decision or feedback right: not established for whole-system current regulation.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: classifier selection, supervisor choice of which specialists to contact, parallel fan-out, request aggregation, execution timing/logging and application configuration.
- Closure path: not applicable as S3.
- Why this is / is not agent-owned: the supervisor manages one user-request composition and the classifier chooses an agent, but neither inspected path establishes a whole-current-system view plus authority to bargain/reallocate resources, commitments, priorities or constraints across operations on behalf of the organization as a whole.
- Evidence: `orchestrator.py`; `agents/supervisor_agent.py`.
- Basis: structural absence review.
- Confidence: high.
- Caveats: supervisor naming and task delegation are not S3 shortcuts.

### Absence scope

- Surfaces inspected: classifier dispatch, supervisor planning/contact selection, parallel invocation, chat storage, execution-time metadata and application-level agent registration.
- Plausible first-party paths checked: supervisor as S3 manager; classifier as S3 allocator; execution timing/logging as current-control telemetry; team registry as whole-system state.
- Why no material first-party path remains: these surfaces route or compose task execution but do not establish discretionary whole-system current regulation of resources/commitments/priorities with a returned intervention path.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path is established that challenges ordinary operational claims and returns findings into corrective control.
- Disturbance / variety regulated: not established as S3*.
- Decisive decision or feedback right: not established for independent audit judgment.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: ordinary tests, tracing/logging, response aggregation and role-overlap diagnostics are available adjacent/supporting surfaces, not a complementary operational audit loop.
- Closure path: not applicable as S3*.
- Why this is / is not agent-owned: the inspected operating paths do not separate an auditor with materially different access from the ordinary production agents and return its findings into correction/re-verification.
- Evidence: shipped agent/runtime surfaces; `agent_overlap_analyzer.py`; tests/examples excluded from operating ownership.
- Basis: structural absence review.
- Confidence: high.
- Caveats: a downstream application can register a reviewer-like agent, but generic extensibility does not establish first-party S3* ownership.

### Absence scope

- Surfaces inspected: registered agents, supervisor composition, logging/callbacks, overlap diagnostics, tests and ordinary response aggregation.
- Plausible first-party paths checked: specialist synthesis as audit; supervisor review of specialist output; overlap analyzer as complementary audit; test suite as runtime audit.
- Why no material first-party path remains: no inspected first-party operating path supplies an independent claim challenge with complementary evidence and corrective return into later operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective intelligence loop develops adaptation options for the Agent Squad organization and returns them into present capability.
- Disturbance / variety regulated: not established as S4.
- Decisive decision or feedback right: not established for future-oriented organizational adaptation.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: conversation history, classifiers, retrievers, provider/tool calls and application configuration can introduce external information but remain task-operation mechanisms.
- Closure path: not applicable as S4.
- Why this is / is not agent-owned: retrieval and ongoing conversation can react to external content, but the repository does not establish a prospective environment model → adaptation option → present capability change loop for Agent Squad itself.
- Evidence: runtime/classifier/storage/agent surfaces at the accepted revision.
- Basis: structural absence review.
- Confidence: high.
- Caveats: downstream applications may implement research or self-improvement agents, but their organizational adaptation cannot be inherited by the generic framework.

### Absence scope

- Surfaces inspected: classifiers, retrievers/integrations, chat history, supervisor memory/context, agent/tool extension points and standard runtime state.
- Plausible first-party paths checked: retrieval as S4 sensing; conversation memory as learning; classifier updates; dynamic supervisor context; extension points as adaptation.
- Why no material first-party path remains: these mechanisms support current task execution or downstream composition, not a shipped external-and-future adaptation loop that changes the framework's current capability.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy closure is established at the Agent Squad organization recursion.
- Disturbance / variety regulated: not established as an S5 identity/policy issue.
- Decisive decision or feedback right: agent membership, role descriptions, system prompts, provider/tool configuration and supervisory rules are supplied by application/developer configuration rather than decided through a shipped S5 loop.
- Decision owner: application developer/operator outside the autonomous assessed runtime for these choices.
- Supporting / enforcement mechanisms: prompts, `AgentOptions`, team lists, classifier configuration and supervisor guidelines constrain operation.
- Closure path: configuration is loaded into subsequent operation, but no identity/ultimate-policy issue is raised, adjudicated by legitimate S5 authority inside the assessed system, and returned as a runtime policy decision.
- Why this is / is not agent-owned: the supervisor follows the configured role/team/prompt contract; it does not own ultimate authority to redefine Agent Squad's organizational identity or policy at this recursion.
- Evidence: `agents/agent.py`; `orchestrator.py`; `agents/supervisor_agent.py`.
- Basis: structural absence review.
- Confidence: high.
- Caveats: parent developers/operators plainly configure the library, but ordinary construction/configuration is not published as `P` without a complete identity/policy decision loop.

### Absence scope

- Surfaces inspected: agent/team construction, supervisor prompt/rules, classifier/runtime configuration, tool/provider settings and application-owned composition points.
- Plausible first-party paths checked: system prompt as S5; supervisor lead as executive policy owner; developer configuration as parent S5; tool/provider restrictions as policy closure.
- Why no material first-party path remains: the inspected paths are static or application-supplied constraints and do not establish an identity/ultimate-policy issue → legitimate authority → authoritative decision → returned subsequent-operation loop at the assessed recursion.

## Distributed OSS parent arrangement

Repository contributor/maintainer governance was not credited as part of the shipped Agent Squad runtime. No organization-level distributed parent S3/S4/S5 loop is inferred from open-source contribution activity.

## Self-hosted and non-human modes

The library can be embedded under operator/developer configuration, but no inspected first-party supervised mode completes an additional parent-owned S3/S4/S5 loop at the Agent Squad runtime boundary. Absence of parent-mode notation is therefore evidentiary, not a maturity judgment.

## Recursion

A supervisor can contain multiple specialist agents and an application can nest Agent Squad components. That is composition/task decomposition. The reviewed repository does not by itself establish that each child agent carries the complete metasystem required for a separate viable recursion, so no recursive VSM credit is inferred from nesting alone.

## Variety and escalation

Classifier routing attenuates incoming request variety by selecting a specialist. Supervisor mode can amplify regulatory response variety by querying several specialists and forwarding context between otherwise isolated agents. Missing information or confirmation can be forwarded back to the user. These are useful operational channels, but no inspected path turns them into positive S2/S3/S5 merely from routing, escalation or human contact.

The current-contract correction is specifically about S2 evidence quality: the repository demonstrates multi-agent communication, but not the required concrete disturbance → attenuation → feedback loop.

## Evidence gaps

- No first-party operational trace/test at the accepted revision was found showing a concrete inter-S1 conflict or oscillation being detected and attenuated by SupervisorAgent mediation.
- `AgentOverlapAnalyzer` labels potential role-description conflict but is not wired into standard runtime behaviour; a future upstream path that consumes its findings to alter specialist allocation/behaviour could warrant reassessment if it closes the full S2 loop.
- No whole-system S3 resource/commitment regulator, independent S3* corrective audit loop, external-and-prospective S4 adaptation loop, or S5 identity/ultimate-policy closure was established at this boundary.
- Upstream current head was inspected for S2-relevant delta before this correction; the accepted `SupervisorAgent` surface is unchanged, so the correction preserves the canonical review ref rather than treating unrelated later repository changes as new evidence.
