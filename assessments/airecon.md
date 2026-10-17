---
harness_id: airecon
project_name: AIRecon
repository: https://github.com/pikpikcu/airecon
review_ref: 6bd19df88506df754a3abc95f14de5488d02c4e4
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: C
autonomy_s5: —
---

# AIRecon

## Review boundary

- System in focus: Shipped first-party Python AIRecon autonomous security research/recon task runtime: FastAPI proxy, AgentLoop model/tool feedback, dynamic RECON→ANALYSIS→EXPLOIT→REPORT phase prompts, built-in Kali/Caido/MCP/browser/security tools, optional graph specialist mode, scope control, separate verification/report admission, memory and adaptive strategy/tool performance learning. One local AIRecon installation and recurring research tasks is the recursion; externally served OpenAI-compatible model and third-party service internals remain dependencies.
- Purpose and identity: Autonomously investigate authorized targets with real model-selected reconnaissance, code/web/proxy tools, maintain evidence and only present grounded vulnerability reports, with learned tool reliability across research tasks.
- Relevant environment: User-authorized attack surface, changing web services and app configurations, live HTTP/WAF/redirect/response evidence, source files and container tools, Caido/browser and external model endpoint, accumulated prior experiment effectiveness and human input.
- Standard-distribution boundary: Installable `airecon` CLI/TUI `airecon/proxy/server.py` FastAPI agent host plus first-party `airecon/proxy/agent` model/tool loop and its first-party independent verification/learning/phase components. Optional external `airecon-skills`, `airecon-dataset`, provider model, Caido and Kali OS internals are dependencies, not transferred agents.
- Credited operating / distribution surfaces: [README.md](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/README.md); [airecon/proxy/server.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/server.py); [airecon/proxy/llm.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/llm.py); [airecon/tui/app.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/tui/app.py); [airecon/proxy/agent/loop.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop.py); [airecon/proxy/agent/loop_process.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_process.py); [airecon/proxy/agent/loop_process_core.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_process_core.py); [airecon/proxy/agent/loop_cycle_llm.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_llm.py); [airecon/proxy/agent/loop_cycle_post.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_post.py); [airecon/proxy/agent/loop_exploration.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_exploration.py); [airecon/proxy/agent/loop_state.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_state.py); [airecon/proxy/agent/loop_message_entry.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_message_entry.py); [airecon/proxy/agent/agent_graph.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/agent_graph.py); [airecon/proxy/agent/subagent.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/subagent.py); [airecon/proxy/agent/pipeline.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/pipeline.py); [airecon/proxy/agent/verification.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/verification.py); [airecon/proxy/agent/executors_reporting.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/executors_reporting.py); [airecon/proxy/agent/adaptive_learning.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/adaptive_learning.py); [airecon/proxy/agent/loop_supervision.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_supervision.py); [airecon/proxy/agent/loop_phase_mentor.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_phase_mentor.py); [airecon/proxy/agent/loop_objectives.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_objectives.py); [airecon/proxy/agent/loop_inference.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_inference.py); [airecon/proxy/agent/loop_policy.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_policy.py); [airecon/proxy/agent/loop_cycle_prelude.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_prelude.py); [airecon/proxy/scope.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/scope.py); [airecon/proxy/reporting.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/reporting.py); [airecon/proxy/config.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/config.py).
- Adjacent first-party surfaces excluded from ownership: Tests as independent product reviewer, technical landing-page/README '1.09M dataset' benchmark counts, optional community skill add-on and external knowledge dataset, Caido sandbox internal logic, provider model policy and model-training, repo issue governance and developer release CI.
- First-party operating / deployment modes considered: Default live native tool-calling agent, OpenAI-compatible local or hosted backend, soft security phases, optional role AgentGraph, optional runtime vulnerability verification with replay/negative controls (can be off), verified-only cross-session memory, adaptive learning/recommendation by phase/target type and current-context tool ranking, human input and scope lock.
- Recursion level: One AIRecon research agent installation across independently requested security-task episodes and evidence/learning history; its primary model/tool operation is S1, with optional nested specialized roles. The app is not a lab-wide portfolio authority.
- Reviewed revision: `6bd19df88506df754a3abc95f14de5488d02c4e4` frozen from intake #186, batch #1648 row 10.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The installed FastAPI `server.chat`/`_stream_agent_events` initiates `AgentLoop.process_message`, not a mere pass-through to a third-party agent application. `AgentLoop` manages conversation, target/scope, model response, selected structured tool calls, local execution, result evidence, iteration counters and next inference. The TUI streams actual `tool_start/tool_output/tool_end`, subagent and user-input events; optional Caido/browser, execution and HTTP tools are first-party registered/mediated interfaces. The external LLM makes substantive next-action decisions but the executable tool/result loop belongs to AIRecon. [airecon/proxy/server.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/server.py); [airecon/proxy/agent/loop.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop.py); [airecon/proxy/agent/loop_process.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_process.py); [airecon/proxy/agent/loop_cycle_llm.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_llm.py); [airecon/tui/app.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/tui/app.py).

`PipelineEngine` encodes soft phase objectives and per-phase tool budget hints; the model can act with context of target and prior observations, and phase assessments yield bounded task feedback. `AgentGraph` is a separately available first-party sequential specialist planner: `recon_node`, `analyzer_node`, `exploiter_node` and `reporter_node` each create an AgentLoop with explicit role max iterations and shared session. Its `execution_order` is a dependency topological traversal and `execute` awaits one specialist before the next. This supports model-active S1 specialized task decomposition, but no independent agent owns whole-installation present work resource commitments or detects operational interference among sibling S1s. Role names do not alone make S2 or S3. [airecon/proxy/agent/agent_graph.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/agent_graph.py); [airecon/proxy/agent/pipeline.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/pipeline.py); [airecon/proxy/agent/loop_message_entry.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_message_entry.py).

An important separate evidence channel is the `report` executor. Before publishing, `_verify_before_report` performs consistency/claim checks. If `verification_enabled` is configured and a relevant HTTP finding/parameter is available, `_runtime_verify_report` instantiates a distinct `VerificationEngine`, sends separate replay/negative-control requests, inspects captured network response status and evidence, scores false-positive/WAF/dynamic differences, and under narrowly enumerated reliable GET/HEAD conditions **blocks an unsupported report** before file write. When evidence is inadequate for negative inference (POST/auth/unreachable/stateful), the path avoids falsely disproving and reports inconclusive. This is bounded first-party *constructor-owned* S3* complementary access to actual target responses rather than the model's own claimed PoC or ordinary prose. The live replay path can be disabled; `FalsePositiveDetector` and verification verdicts are not separate autonomous models. [airecon/proxy/agent/executors_reporting.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/executors_reporting.py); [airecon/proxy/agent/verification.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/verification.py); [airecon/proxy/reporting.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/reporting.py).

The installed `AdaptiveLearningEngine` maintains per-tool historical success/failure, contextual scores and strategies conditioned on target stack and pipeline phase; `loop_cycle_post` calls `_record_adaptive_learning` on real tool results and `loop_cycle_llm` requests `recommend_tools` and `recommend_strategy` and injects the alternatives into the model's next context. `loop_state` also promotes only verified or high-confidence vulnerability findings into cross-session target knowledge by default. These are real **externally coupled, later-run** strategic/tool-selection adaptation paths: observed changes in target/tool behavior are evaluated under accumulated reliability and then offered as alternative next techniques for the current or later model to choose. However, the heuristics do not themselves select a novel organizational capability or create new tools/weights; the decisive future option selection is a deterministic ranking and suggestion structure, while a task model exercises actual next tool use. We therefore bound S4 to **C** (constructor-supported prospective operating strategy calibration), not autonomous S4=A or proof of scientific self-improvement. [airecon/proxy/agent/adaptive_learning.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/adaptive_learning.py); [airecon/proxy/agent/loop_cycle_post.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_post.py); [airecon/proxy/agent/loop_cycle_llm.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_llm.py); [airecon/proxy/agent/loop_state.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_state.py).

The host provides scope/credential protections, a global agent busy lock, request throttling and model fallback to protect concurrent TUI/HTTP traffic. These concern one active agent task's process lifecycle rather than an evidenced mutual S2 adjustment among autonomous sibling science cells. User stop/permission/scope handling belongs to task safety, not first-party ultimate research ethics/policy S5. [airecon/proxy/server.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/server.py); [airecon/proxy/scope.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/scope.py); [airecon/proxy/agent/loop_policy.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_policy.py).

## S1 — Operations

- State: A
- Function: Choose and execute contingent security reconnaissance/analysis actions with model-selected first-party tools, observe real outputs and continue until an objective, phase or explicit stop.
- Disturbance / variety regulated: Unknown target technologies, changing HTTP responses, access restrictions, WAFs, missing evidence, failed security techniques, rate limits and uncertain code/path context.
- Decisive decision or feedback right: OpenAI-compatible configured model chooses tool name/arguments and reasoning/action continuation based on returned first-party tool results, per-target evidence, memory and phase guidance.
- Decision owner: Model acting through AIRecon-native AgentLoop tool execution and result feedback. External API inference is computation rather than a borrowed agent harness.
- Supporting / enforcement mechanisms: FastAPI chat, AgentLoop state, first-party tool registry, proxy sandbox/browser/Caido, scope enforcement, phase prompts, tool message history, backoff/timeouts and status stream.
- Closure path: authorized target/prompt → agent reasoning/tool choice → built-in HTTP/terminal/browser/security tool execution → captured results/target responses → next model turn and updated task session → report/further probing.
- Boundary reachability: `server._stream_agent_events` invokes the installed `AgentLoop.process_message`, and `loop_process_core` drives tool decisions/results; `airecon` TUI/CLI reaches that live service. Alternate AgentGraph can execute specialized AgentLoops by role.
- Why this is / is not agent-owned: The agent decides concrete next tools and adaptation to responses rather than following only a fixed scan list.
- Evidence: [airecon/proxy/server.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/server.py); [airecon/proxy/agent/loop.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop.py); [airecon/proxy/agent/loop_process.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_process.py); [airecon/proxy/agent/loop_cycle_llm.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_llm.py); [airecon/proxy/agent/loop_cycle_post.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_post.py).
- Basis: Direct reachable first-party model/tool feedback implementation.
- Confidence: High on source reachability; no external backend or authorized pentest was run.
- Caveats: Native tool-capable model is required. Phase boundaries are guided rather than universally enforced; optional external security datasets are not scored as AIRecon operators.


## S2 — Coordination

- State: —
- Function: No material first-party interference/oscillation-regulation path between two independently viable simultaneous operational agents established at the assessed installation recursion.
- Disturbance / variety regulated: Concurrent HTTP/TUI requests would corrupt the single active AgentLoop state; the server prevents duplicates with a busy lock, but that is same-agent single-session admission, not sibling S1 negotiation.
- Decisive decision or feedback right: A global busy lock restricts one agent; AgentGraph performs ordered dependent specialist tasks; no cross-S1 collision-sensitive mutual adjustment owner is shown.
- Decision owner: Deterministic request admission and sequential pipeline executor, without distinct S2 activity.
- Supporting / enforcement mechanisms: asyncio Lock / busy flag, rate limits, AgentGraph dependency execution order and tool result status.
- Closure path: Second request waits/is rejected while the **same** agent is active; graph specialists execute serially. No two independently ongoing S1 units detect and correct a shared clash and feed an altered coordination plan back.
- Distinct S1 units: Separate specialist AgentLoops may exist when AgentGraph is invoked; their sequential delegation is not mutually regulated interference.
- Inter-S1 disturbance: A theoretical shared HTTP target or write conflict among different concurrent specialists isn't matched with a first-party specific live resolution path.
- Why this is / is not agent-owned: A server-level single-agent busy lock and soft pipeline ordering are generic current-task safety rather than Beer S2.
- Evidence: [airecon/proxy/server.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/server.py); [airecon/proxy/agent/agent_graph.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/agent_graph.py); [airecon/proxy/agent/loop_policy.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_policy.py).
- Basis: Bounded negative on concurrency and graph/task scheduling.
- Confidence: Medium-high.
- Caveats: A different deployment running several research sessions could add a higher-level coordination mechanism, not shown here.

### Absence scope

- Surfaces inspected: Global AgentLoop busy lock, AgentGraph sequential execution, specialist delegation, shared session, tool concurrency/rate limits and scope guard.
- Plausible first-party paths checked: Two overlapping server chat tasks, two target specialists sharing a workspace, phase resources and concurrent tool calls.
- Why no material first-party path remains: All observed guards are single-agent admission or dependency sequencing, without evidenced specific sibling operating interference and response feedback.


## S3 — Inside-and-now control

- State: —
- Function: No separately owned whole-installation current operations/resource commitment regulator was established beyond one agent's task planning and soft phase guidance.
- Disturbance / variety regulated: Missing progress, failed probes, oversized inference contexts and many substeps are handled in primary S1 task feedback and phase mentor heuristics.
- Decisive decision or feedback right: The agent model decides its own next research probe; `PipelineEngine` suggests phase transition and AgentGraph wires dependent role tasks, but no metasystem manages competing live independent S1 operational mandates.
- Decision owner: Current S1 task model and fixed phase/role code, not a separate current-operation manager.
- Supporting / enforcement mechanisms: Phase prompts, progress checkpoints at 5/10/15 iterations, target priority and soft mentor, AgentGraph DAG role order, model/tool budgets and service locks.
- Closure path: Current tool result and phase assessment → continuation of the same S1 investigation; no whole-installation current picture → accountable cross-operation resource/priority choice → returned allocation across sibling units.
- Why this is / is not agent-owned: A task phase self-monitor and sequential science role chain are not Beer S3 simply because called planner or orchestrator.
- Evidence: [airecon/proxy/agent/pipeline.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/pipeline.py); [airecon/proxy/agent/agent_graph.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/agent_graph.py); [airecon/proxy/agent/loop_phase_mentor.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_phase_mentor.py); [airecon/proxy/agent/loop_objectives.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_objectives.py).
- Basis: Bounded negative of candidate current-control decisions.
- Confidence: Medium-high at one-agent installation recursion.
- Caveats: Phase budgets guide one operation, not system-wide resource bargaining.

### Absence scope

- Surfaces inspected: AgentGraph, pipeline, objective/phase mentor, target prioritizer, service busy lock, tool rankings and TUI status.
- Plausible first-party paths checked: Multi-agent mode, shared target/workspace, default phase progression, prioritized endpoints, live exception intervention.
- Why no material first-party path remains: No active first-party whole of independent operational units with separate above-S1 discretion over current commitments was observed.


## S3* — Complementary audit

- State: C
- Function: Challenge the operating model's submitted vulnerability/report assertions through an independent raw target replay/negative-control and alternative evidence path and return blocking or lowered confidence before publication.
- Disturbance / variety regulated: Hallucinated vulnerabilities, unrepeatable injection claims, WAF/redirect artifacts, volatile page content, misleading HTTP responses and unsupported PoC text.
- Decisive decision or feedback right: Report executor first runs deterministic evidence checks; when live verification is enabled and vulnerability type/endpoint are eligible, independent `VerificationEngine` sends separate diagnostic requests with varied test inputs, compares baseline/negative responses and determines replay confidence/false-positive features.
- Decision owner: First-party deterministic verifier plus direct captured target evidence, with report guard applying its result; no separate critic model/human owns the judgment.
- Supporting / enforcement mechanisms: VerificationResult, FalsePositiveDetector, replay and negative-payload sets, HTTP status/body evidence bundle, request headers/auth context, false-positive/WAF/dynamic-content logic, tool report block.
- Closure path: LLM/agent-proposed finding report → independent target evidence and negative/replay probes → verifier result/false-positive decisions → reporting executor blocks a sufficiently contradicted claim or annotates inconclusive → agent receives tool failure/success for subsequent investigation.
- Claim being audited: Whether a proposed report's vulnerability, param/endpoint and exploitability/PoC assertions are supported enough to publish.
- Ordinary reporting path: Agent-generated finding and proposed report arguments, drawn from its earlier tool conversation.
- Complementary access path: First-party independent live HTTP replay/negative tests and actual status/response evidence produced outside model-written text, with explicit confidence and FP diagnostics.
- Independence boundary: Different tool-origin evidence and verifier rules within same process, not separate human reviewer, independently hosted model or complete formal proof; per-type coverage and config govern availability.
- Who acts on findings: `_execute_reporting` uses `_runtime_verify_report`, can return `blocked_by_verifier` to original model and refuse report write. Ineligible findings remain evidence-grounded or inconclusive, not falsely disproved.
- Boundary reachability: `AgentLoop` model-selected report tool enters `executors_reporting`, which invokes `_verify_before_report` and `_runtime_verify_report`; enabled mode uses actual VerificationEngine and sends the verdict back before persistent vulnerability output.
- Why this is / is not agent-owned: Verifier uses deterministic request/response scoring; LLM isn't independently selecting auditor judgment. The additional observational channel is complementary, so bounded S3*=C.
- Evidence: [airecon/proxy/agent/executors_reporting.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/executors_reporting.py); [airecon/proxy/agent/verification.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/verification.py); [airecon/proxy/reporting.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/reporting.py); [airecon/proxy/config.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/config.py).
- Basis: Implemented separate replay/negative-evidence challenge and live conditional report correction.
- Confidence: High for enabled source path and conservative fail-condition; effectiveness not empirically reproduced.
- Caveats: Runtime verification is optional and depends on target/param/type. Verification can return inconclusive; lack of blocking does not certify every vulnerability and no live target test was performed.


## S4 — Outside-and-then intelligence

- State: C
- Function: Condition later scientific/security task strategies and tool choices on observed external target/probe effectiveness, developing reusable prospective options and returning them to the model before later action.
- Disturbance / variety regulated: Tool effectiveness changes across target technologies/phases and WAF conditions, repeated failed strategies, unreliable reported findings and differing real-world app stacks.
- Decisive decision or feedback right: First-party AdaptiveLearningEngine records observed tool use and success, updates per-stack/phase reliability and strategy patterns, then `recommend_tools` and `recommend_strategy` select ranked prospective action alternatives for subsequent turns or sessions. LLM then chooses actual action from those options.
- Decision owner: Rule-based first-party adaptive learning and condition matching own recommendation ranking; autonomous task model acts on hints but no separate agent owns organization-wide adaptation-option judgement. Therefore S4=C, not A.
- Supporting / enforcement mechanisms: Persistent global_learning state, tool performance rolling success scores, context and target-type scores, minimum observations, strategy success/failure, verified-only finding memory, per-iteration prompt re-injection.
- Closure path: Observed tool/probe results from real target environment → persisted tool/strategy effectiveness and cross-session verified knowledge → phase/tech-specific recommendations in `loop_cycle_llm` prompt → actual agent tool strategy choice in later iteration/session → new result updates learned performance.
- External distinction: Target technology/WAF stack, network responses and effectiveness of the agent's independently executed HTTP/command tools are external-environment distinctions, learned by the agent from observed success/failure and per-target technology evidence rather than fixed in task prompt or mere generic model memory.
- Future / prospective distinction: The AdaptiveLearningEngine stores per-tool historical effectiveness and condition-specific strategy outcomes across calls/sessions, so the feedback changes which prospective tool/strategy choices are recommended in subsequent phases and later differently configured target sessions, not only the immediately preceding current action.
- Adaptation option generated: The first-party option set is an explicit new ranking of candidate tool choices (recommend_tools) and remembered target/phase strategy sequences (recommend_strategy); min-observation, recency/failure-streak and target technology matching select or suppress options before exposing them to the task model. No claim of newly authored code or model weights.
- Path back into current capability / S3: loop_cycle_post calls _record_adaptive_learning on observed tool outcomes, which updates persistent strategy/tool reliability; loop_cycle_llm then injects the resulting ranked alternatives as active model-control context for later decisions in the real AgentLoop. The first-party host thus returns revised operating strategy choice into present S1 action/control, with the selected tool's result fed back; no distinct higher-S3 organizational bargaining was found, so C only.
- Boundary reachability: `loop_cycle_post` invokes `_record_adaptive_learning` after completed tools; `loop_cycle_llm` calls `recommend_tools` and `recommend_strategy` using current target technologies/phase and injects to model continuation. `AdaptiveLearningEngine` persists relevant observations for future runs.
- Why this is / is not agent-owned: No model owns the higher-level strategic-option creation/adoption loop; effectiveness-based ranking is deterministic, with model using the result for S1. First-party reusable prospective option return supports S4=C, not model-governed S4=A.
- Evidence: [airecon/proxy/agent/adaptive_learning.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/adaptive_learning.py); [airecon/proxy/agent/loop_cycle_post.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_post.py); [airecon/proxy/agent/loop_cycle_llm.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_cycle_llm.py); [airecon/proxy/agent/loop_state.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_state.py); [airecon/proxy/agent/loop_exploration.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_exploration.py).
- Basis: First-party source evidence for cross-session environment performance learning and actual option re-injection.
- Confidence: Medium: bounded to strategy/tool repertoire calibration, not development of new tool categories or model weights.
- Caveats: These suggestions remain model-discretion hints, not automatic proof of enhanced penetration-testing quality; no independent performance benchmark conducted. No separate S3 whole-now negotiation demonstrated.


## S5 — Policy and identity

- State: —
- Function: No installed first-party ultimate ethics/purpose/identity policy settlement loop beyond authorization and scope enforcement.
- Disturbance / variety regulated: Out-of-scope targets, credential misuse, destructive actions, unsafe payloads and human-sensitive decisions trigger task-level checks.
- Decisive decision or feedback right: The user/operator supplies allowed scope, model and authorization; first-party enforcement can block tools, prompt for input or terminate. No distinct internal organization actor resolves ultimate legitimate scientific/pentest aims and returns revised policy.
- Decision owner: External legitimate target owner/operator defines engagement scope, code enforces permitted boundaries.
- Supporting / enforcement mechanisms: ScopeGuard, target allowlists, per-command audit, user input modal, tool risk constraints, Docker isolation, access controls and task stop.
- Closure path: Operator-supplied authorized scope → tool request permitted/blocked and agent continues under fixed rule; no ultimate purpose controversy → legitimate policy settlement → binding operational return.
- Why this is / is not agent-owned: Scope enforcement/human approvals aren't Beer S5 identity/governance; the security institution providing legitimate rules remains outside this deployed harness.
- Evidence: [airecon/proxy/scope.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/scope.py); [airecon/proxy/server.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/server.py); [airecon/proxy/agent/loop_policy.py](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/airecon/proxy/agent/loop_policy.py); [README.md](https://github.com/pikpikcu/airecon/blob/6bd19df88506df754a3abc95f14de5488d02c4e4/README.md).
- Basis: Bounded negative review of policy and authorization paths.
- Confidence: Medium-high.
- Caveats: Actual pentest engagement governance is an external parent system and is not credited as first-party without an explicit organizational return path.

### Absence scope

- Surfaces inspected: Scope guard, API management, tool action validator and auth, user input event, sandbox and configuration policy.
- Plausible first-party paths checked: Target ownership enforcement, human consent and authorization, attack phases, role restrictions and persistence.
- Why no material first-party path remains: No source-backed independent highest-level organization purpose conflict resolution or recurring ethos/identity governance for the installed AIRecon runtime.


## Distributed OSS parent arrangement

An operator/authorized client supplies targets and scope; first-party model-guided agent runs in local service and invokes real tools. Third-party model inference, Caido sandbox services and external community datasets do not become separate in-scope VSM decision owners. Optional AgentGraph role nodes are task specialists within current study; their pipeline status cannot independently supply S3/S5.

## Self-hosted and non-human modes

OpenAI-compatible inference can be local behind vLLM/LiteLLM/Ollama gateway or hosted. The native runtime supplies the same action feedback. Live replay verification can be configured on/off and conservative negative blocking is intentionally restricted. Adaptive strategies are local persisted metadata and prompt hints, not remote fine-tuning or changing model weights. User clarification/cancel remains task-level.

## Recursion

At a local AIRecon installation, the first-party AgentLoop is operational S1. Optional role-specialist loops and phase decomposition do not establish current whole-system metasystem. A distinct verification tool path can challenge the operating reporter using raw target evidence as S3*=C; external target/tool histories accumulate and become future strategy options as S4=C. No demonstrated inter-S1 S2 mutual adjustment or ultimate governing S5.

## Variety and escalation

Autonomous tools amplify handling of changing unknown targets. Scope checks, replay verifier/negative controls, constrained report publication and verified-only memory attenuate unsupported outcomes. New learned strategies can be re-presented under new target conditions, but suggestions don't imply verified success or permission to attack outside approved scope.

## Evidence gaps

- Exact frozen source review only; no authorized target attacks, external model inference, security benchmark replication or execution of verification probes against public targets.
- S3*=C is conditional/limited to report tool and supported replay types; does not guarantee every report passed independent verification or every model hallucination blocked.
- S4=C is bounded strategy/tool-ranking future option construction with actual feedback-return, not model-owned full capability expansion/new training. If future Methodology requires an additional independent S3–S4 transaction at this recursion, the classification should be reconsidered.
- Soft phase prompts and sequential specialist AgentGraph are not evidence of S2 or S3 management; the service busy lock protects the same agent loop rather than sibling agents.
- S5=— is limited to installed software, not an assertion about external pentest authorization owners.
