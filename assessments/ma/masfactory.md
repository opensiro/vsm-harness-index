---
harness_id: masfactory
project_name: MASFactory
repository: https://github.com/BUPT-GAMMA/MASFactory
review_ref: 7e5beb2e5a2093963ee9a5babfffc2cc22784f45
reviewed_at: 2026-10-26
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

# MASFactory

## Review boundary

- System in focus: the first-party installable Python MASFactory agent/graph runtime, including explicitly built graph workflows, model-backed agent nodes, tools/context/memory adapters, VibeGraph AML construction, loop/switch primitives and supported human-in-the-loop nodes at the frozen revision.
- Purpose and identity: let an application build and run graph-shaped collaborations of LLM agents and tools, including model-generated workflow designs with optional user correction.
- Relevant environment: application task inputs, model-provider responses, user tools and external context systems, changing intermediate agent outputs, operator design/review decisions and the Python host of the graph invocation.
- Standard-distribution boundary: `masfactory/components/agents/`, `components/graphs/`, `components/composed_graph/`, `components/controls/`, `components/vibe/`, adapters, messages and graph engine. Configured model API, tool implementations supplied by an adopter and external participant organizations are dependencies, not automatically first-party owners.
- Credited operating / distribution surfaces: model-backed `Agent.step` with repeated tool call/feedback, shipped `SingleAgent` and graph nodes, `RootGraph.invoke` execution, loop feedback and `VibeGraph.build` with the first-party role-assigner/planner/diagnose/human AML compilation route.
- Adjacent first-party surfaces excluded from ownership: `applications/` benchmarks/reproductions and example-specific agents, development/dogfood workflows, visualizer-only presentation, docs site, npm build/test tooling, CI and OSS contributor governance. Illustrative graph patterns show API reachability without transferring their separate application-level organizational rights to the generic library.
- First-party operating / deployment modes considered: direct `SingleAgent` invocation; developer-defined `RootGraph` agent/tool graphs; loop and `AgentSwitch` routing; generator-verifier and brainstorming templates; model-generated `VibeGraph` with cached AML or interactive role/profile design; human chat/file-edit nodes and external model/tool adapters.
- Recursion level: one installed application invocation over a configured graph. Individual agent nodes can be S1 execution cells in a larger application, but graph nesting or multiple agent names alone does not prove recursive viable organizations.
- Reviewed revision: `7e5beb2e5a2093963ee9a5babfffc2cc22784f45`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/README.md) presents MASFactory as a graph-centric framework. The decisive executable evidence is the [first-party `Agent`](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/agents/agent.py): `observe` assembles instructions, context/memory/tools and messages; `think` invokes an injected model adapter; `act` executes selected registered tools; `step` loops model → tool results → model until content, error or a ten-tool-call guard. Its output and history influence subsequent decisions. [`SingleAgent`](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/agents/single_agent.py) exposes a direct invocation of this runtime.

The [root graph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/graphs/root_graph.py) invokes built node/edge objects; [graph scheduling](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/graphs/graph.py) executes ready nodes until exit/stall/max iterations. [`Loop`](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/graphs/loop.py) returns iterative messages to its controller; [`AgentSwitch`](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/controls/agent_switch.py) asks a model whether an output satisfies a developer-supplied route condition. These form flexible task control flow. They do not by themselves identify distinct S1 businesses, inter-unit interference, whole-current control, independent audit or ultimate authority.

First-party patterns such as [`GeneratorVerifierGraph`](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/composed_graph/generator_verifier_graph.py) implement ordinary candidate → verifier → retry/exit quality gates; [`BrainstormingGraph`](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/composed_graph/brainstorming_graph.py) serially broadcasts critic outputs to later nodes. Neither is by itself evidence of systemic inter-S1 conflict attenuation or complementary S3* access to reality.

The supported [`VibeGraph`](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_graph.py) invokes an in-package [role/plan/profile workflow](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/main.py), accepts [human review of roles](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/role_assigner.py) and [editable AML profiles](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/profile_designer/profile_designer_human_graph.py), diagnoses structural problems in generated AML and [compiles](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/compiler.py) it to a runnable graph. This is a substantial constructor for an application workflow. It is still a task-design/build operation until an actual multi-unit ongoing regulatory function and decision/return loop is evidenced.

## Operational model

An application developer constructs a graph or uses `VibeGraph` to generate one; optional human review changes the proposed plan and role descriptions. During invocation, first-party model-backed nodes select content/tools/actions and consume results inside a configured graph. The graph runtime transports and schedules messages, with optional loops, switches and validation. The developer/operator owns the higher-level business goal, tool permissions, policy and whether to deploy the graph. The framework supplies autonomous S1 execution, but it does not impose an S2–S5 constitution on every application that composes its primitives.

**Proposed disposition: included**, vector `A — — — — —`. Positive S1 uses the shipped real model/tool loop, not benchmarks or mere Vibe Graph documentation. The remaining findings are bounded to this first-party standard framework and do not say downstream developers cannot implement higher functions.

## S1 — Operations

- State: A
- Function: perform application-specified agent tasks, including iterative tool use and model-led production of graph node outputs; optionally construct a runnable graph design from the user's requirements.
- Disturbance / variety regulated: task-specific prompts, unknown tool observations, intermediate graph messages, retrieved context, complex role/edge constraints and output-format requirements.
- Decisive decision or feedback right: a configured model chooses tool calls and final outputs from instructions and successive tool results; in VibeGraph construction, model agents choose role and workflow design content before compiler/operator constraints.
- Decision owner: first-party `Agent.step` running an injected inference model in the explicitly supported standard mode; the developer selects the model and allowed tools, while deterministic graph/gate machinery executes chosen edges and outputs.
- Supporting / enforcement mechanisms: adapters, tool schemas, context/history assembly, output formatter, retries/ten-call guard, node/edge gate scheduling, AML parser/compiler and optional user correction.
- Closure path: task input → model call → model-selected tool → tool result appended to conversation → next model decision → validated agent output → graph edge/downstream node or direct caller. In VibeGraph mode, approved/generated AML is compiled into executing nodes.
- Boundary reachability: `SingleAgent.invoke` directly calls the in-package `Agent.step`; graph `RootGraph.invoke` executes `Agent` nodes through `Node` and graph scheduling. `VibeGraph.build` directly materializes shipped model-backed design workflow and compiles its output; no separately initiated outside coding-agent host is required.
- Why this is / is not agent-owned: removing the model leaves no discretionary tool/answer selection or semantic workflow design. Schedulers, parsers, templates and user-provided model credentials support rather than replace that owner.
- Evidence: [Agent](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/agents/agent.py), [SingleAgent](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/agents/single_agent.py), [RootGraph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/graphs/root_graph.py), [VibeGraph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_graph.py).
- Basis: first-party executable model/tool loop and graph constructor structure.
- Confidence: high for structural reachability; no live model/provider quality measurement.
- Caveats: the organization produced by a particular adopter's graph is not automatically part of the generic framework's assessed boundary. Tools, inference and high-level domain policy depend on configuration.

## S2 — Coordination

- State: —
- Function: no established S2-specific autonomous/constructor path that attenuates a concrete inter-S1 collision or oscillation and returns a coordinating change across distinct ongoing S1 units.
- Disturbance / variety regulated: independent agents in a built graph can produce inconsistent drafts, duplicate outputs or contending messages, but potential disagreement alone is not S2.
- Decisive decision or feedback right: identify actual inter-unit interference, choose a coordination response and change subsequent peer operations.
- Decision owner: graph edges, switch conditions and broadcasts follow developer-authored topology; generic composing application could add an S2 owner, but the default framework has none evidenced.
- Supporting / enforcement mechanisms: node input/output keys, graph edges/gates, loops, `AgentSwitch`, brainstorming broadcasts, role assignment and dependency ordering.
- Closure path: messages are sequenced or routed to another node, but no first-party conflict/oscillation detection, independent coordination choice and returned operating arrangement is supplied.
- Why this is / is not agent-owned: a model YES/NO route condition or critics→solver pipeline handles task flow/quality. This does not establish a regulating relation between two autonomous S1 units with a specified interference channel.
- Evidence: [Graph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/graphs/graph.py), [AgentSwitch](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/controls/agent_switch.py), [BrainstormingGraph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/composed_graph/brainstorming_graph.py).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: custom application graphs could supply concrete S2, but generic graph routing is an infrastructure constructor, not function-specific S2=C.

### Absence scope

- Surfaces inspected: graph gates/edges, composed horizontal/brainstorm/mesh and vertical templates, switches, role assignment, loop feedback.
- Plausible first-party paths checked: parallel/serial message ordering as S2; critic disagreement as inter-unit conflict; VibeGraph role distribution as collision control.
- Why no material first-party path remains: none of these inspected standard paths establishes the required distinct S1 interference plus a coordination feedback that revises their subsequent relation.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control authority over a portfolio of operational S1 units in the assessed generic run.
- Disturbance / variety regulated: node stalls, loop counts, route conditions, task progress, invalid graph designs and model/tool budgets.
- Decisive decision or feedback right: observe current whole-system commitments/resources and authoritatively revise priorities, constraints or interventions for S1 units.
- Decision owner: graph developer and operator choose topology, resource bounds and interventions; schedulers and loop controllers enforce those configured limits.
- Supporting / enforcement mechanisms: `Graph._forward` readiness loop and max iterations, `Loop` controller, hooks, visualizer runtime traces, VibeGraph diagnosis/compiled topology.
- Closure path: routine model task output or configured termination feeds a node transition; no supervisory whole-current assessment/decision is returned across autonomous divisions.
- Why this is / is not agent-owned: a class named `Controller`, graph-level invocation or whole-DAG visibility is not whole-organizational resource/commitment authority. Human editing a construction graph is not automatically an operational S3 parent mode.
- Evidence: [Graph scheduling](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/graphs/graph.py), [Loop](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/graphs/loop.py), [VibeGraph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_graph.py).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: actual adopter applications could appoint an autonomous/parent manager with a current portfolio view; its decisions must be assessed in that composed boundary.

### Absence scope

- Surfaces inspected: root/loop graph, scheduling/gates, model switches, visualizer hooks, VibeGraph user feedback and developer configuration.
- Plausible first-party paths checked: loop `Controller` as S3; runtime trace as current view; generated team design/human edits as S3(P).
- Why no material first-party path remains: these move a workflow or enforce specified transition rules without a first-party whole-current discretionary commitment/resource decision and returned multi-unit control.

## S3* — Complementary audit

- State: —
- Function: no established independent complementary audit path at the declared graph-runtime recursion.
- Disturbance / variety regulated: model hallucination, invalid outputs, graph misconstruction and falsely accepted work.
- Decisive decision or feedback right: use materially separate access to operational reality to challenge ordinary self-reporting and feed a corrective conclusion into current control.
- Decision owner: developer-supplied verifier/template and routine AML `DiagnoseNode`; the first-party library supplies gates but not a separately controlled, independent system audit.
- Supporting / enforcement mechanisms: `GeneratorVerifierGraph`, vertical critics, AML parser/diagnosis and execution hooks/traces.
- Closure path: verifier results can cause a generator to retry; this is an ordinary task production/QA loop, not a complementary inspection of operational reality outside that path.
- Why this is / is not agent-owned: an injected model verifier may independently judge a candidate answer, yet it consumes the same work artifact as a normal mandatory stage; independence of model name alone does not create S3*.
- Evidence: [GeneratorVerifierGraph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/composed_graph/generator_verifier_graph.py), [VerticalDecisionGraph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/composed_graph/vertical_decision_graph.py), [AML diagnose](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/planner/diagnose_node.py).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: an adopter could configure a separately independent raw-evidence audit node, but no such positive runtime loop is established by the generic template alone.

### Absence scope

- Surfaces inspected: generator-verifier, critic/solver graphs, AML structural diagnosis, run hooks, visualizer traces, benchmarks/tests.
- Plausible first-party paths checked: verifier as complementary reviewer, model critics as independent source inspection, runtime tracing as S3* alternative access.
- Why no material first-party path remains: the built-in paths are routine output checks within the same task flow or observation tools; no separately controlled operational-reality audit with systemic return is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no continuous or event-triggered external-and-prospective option loop that revises the ongoing organization from sensed future-relevant changes.
- Disturbance / variety regulated: new user requests and future task designs can require different roles, graph topologies and tools.
- Decisive decision or feedback right: observe outside/future distinctions, evaluate adaptation options and return a selected capability change to present operations.
- Decision owner: model-backed VibeGraph construction chooses a workflow for a stated current design request; adopting developer/human chooses its deployment. No separately established S4 owner.
- Supporting / enforcement mechanisms: role assigner, planner/diagnose, human profile edits, AML cache/compiler and model adapters.
- Closure path: design request → generated/corrected AML → runnable graph, but that is the S1 product-construction path, not a standing external prospecting/S3–S4 regulatory dialogue for the framework's current operation.
- Why this is / is not agent-owned: producing a new task workflow is operational creativity, not automatically S4 adaptation of a viable organization to a changing future environment.
- Evidence: [VibeGraph](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_graph.py), [workflow planner](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/planner/planner_agent.py), [human profile loop](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/profile_designer/profile_designer_human_graph.py).
- Basis: bounded negative.
- Confidence: medium.
- Caveats: the same workflow constructor could become S4 machinery inside a separately evidenced, continuously governed adopter organization.

### Absence scope

- Surfaces inspected: VibeGraph builder/AML compile, role/plan/profile workflow, context/memory adapters, examples and model-enabled dynamic agent.
- Plausible first-party paths checked: building a new graph as prospective strategic adaptation; stored history as learning; user role/profile feedback as S4(P).
- Why no material first-party path remains: these paths produce or revise a present requested deliverable rather than sensing future environment, comparing adaptation options and returning a legitimate strategy decision to present S3.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/policy issue decision-and-return loop governing the assessed framework as an organization.
- Disturbance / variety regulated: tool-risk permission, accepted agent roles, framework constraints, developer/enterprise purpose and human design approval.
- Decisive decision or feedback right: settle an identity/ultimate-policy matter through a legitimate authority and return that ruling into subsequent operation.
- Decision owner: application developer and operator set objectives/model/tool rights; role/profile UI solicits human corrections about workflow design, not organization-level identity governance.
- Supporting / enforcement mechanisms: agent instructions, model settings, graph conditions, AML validation, user agreement/edit loops and contributor policy.
- Closure path: human advice can modify generated AML and shape the current graph; no runtime identity-policy issue → legitimate parent adjudication → durable policy return is supplied.
- Why this is / is not agent-owned: prompts and human approval for a graph draft do not establish legitimate ultimate-policy closure; model-generated team roles are task design, not the framework's constitutional authority.
- Evidence: [role approval](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/role_assigner.py), [human AML edit](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/vibe/vibe_workflow/profile_designer/profile_designer_human_graph.py), [agent](https://github.com/BUPT-GAMMA/MASFactory/blob/7e5beb2e5a2093963ee9a5babfffc2cc22784f45/masfactory/components/agents/agent.py).
- Basis: bounded negative including parent-mode consideration.
- Confidence: medium-high.
- Caveats: downstream enterprises can and should own policy for tool/agent deployments; their S5 belongs to their declared recursion, not this generic framework by co-location.

### Absence scope

- Surfaces inspected: human role/profile review, root graph invocation, default agent instruction/tool interfaces, AML validation and OSS project policies.
- Plausible first-party paths checked: human edit/AGREE as S5(P), role architect agent as S5(A), static templates/permissions as ultimate policy.
- Why no material first-party path remains: these govern task design/configuration and execution constraints; no legitimate runtime identity/policy dispute with an authoritative returning decision is supplied.

## Distributed OSS parent arrangement

MASFactory's independent adopters run private graphs and may use unrelated models/tools. They do not become one public multi-installation organization through the upstream repository; contributor maintenance and the docs/project website are outside runtime S5/S3 authority.

## Self-hosted and non-human modes

The installed framework supports a fully model-driven agent/tool loop and optional visual/operator interventions during workflow design. Neither a non-human graph with many nodes nor a user-edited AML specification automatically supplies metasystem functions; function-specific ownership and closure would need an assessment of the constructed application.

## Recursion

Graph/node nesting and reusable subgraphs express composition. A node with local model/tool discretion can act as an S1 cell inside an application's broader VSM, but persistent local identity, metasystem, relevant environment and parent channels are not proved by nesting alone.

## Variety and escalation

AML graph design and edge schemas attenuate large natural-language task variety into executable structures. Model tools amplify action repertoire; formatters, node gates, loop iteration bounds, human edits and diagnosis restrict outputs. Warnings/stall traces and review prompts surface exceptions to an invoking operator, without themselves establishing an algedonic channel to a demonstrated S3/S4/S5 authority.

## Evidence gaps

This was a pinned first-party source inspection, not a live model or agent-quality benchmark. Native `import masfactory` could not run in this environment because `tiktoken` was not installed; Python AST/compile checks can only assess syntax. The generic library supports broad downstream customization, but no composed adopter organization with real inter-S1 disturbances, independent operational-reality audit or closed parent strategic/policy loops was available as the fixed system-in-focus. Negative states are bounded to the shipped standard library modes rather than claims of universal impossibility.
