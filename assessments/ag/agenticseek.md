---
harness_id: agenticseek
project_name: AgenticSeek
repository: https://github.com/Fosowl/agenticSeek
review_ref: 4f5f924c1eb326b4163d3bf942954dcc7dd7875b
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgenticSeek

## Review boundary

- System in focus: The first-party self-hosted AgenticSeek Python agent runtime composed of the CLI/API entry paths, query router, code/file/browser operational agents and optional complex-task `PlannerAgent` with actual child-agent delegation and feedback.
- Purpose and identity: Let a user perform local coding, file retrieval, web research/navigation, and multi-step tasks using an operator-configured local or remote model while retaining control of the deployment.
- Relevant environment: User requests, local host files/workspace, execution interpreters, browser/web results, language/model limitations, failed commands and subordinate agent task outcomes.
- Standard-distribution boundary: Shipped `cli.py` or `api.py` → `Interaction` → `AgentRouter` and role agents under `sources/agents/` → their first-party execution/browsing tools and provider calls. Externally provided model inference, browser websites, Web search service, Ollama/llama.cpp runtime, downloaded routing/classifier weights and host system tools are support/dependencies, not separately credited as autonomous first-party organizational owners.
- Credited operating / distribution surfaces: [CLI agent instantiation](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/cli.py#L24-L75), [query/complexity routing](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/router.py#L369-L478), [agent tool feedback](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/agent.py#L163-L286), [coding loop](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/code_agent.py#L12-L88), [planner manager](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L14-L321), [user/agent activation](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/interaction.py#L270-L305).
- Adjacent first-party surfaces excluded from ownership: CI and unit tests, README marketing of universal/local autonomy, launch/install scripts, GitHub maintenance, speech/UI display, commentary on external model quality, third-party model provider/router internals, and commented-out `McpAgent` in the normal CLI. These may show configurability but do not create separate S-functions.
- First-party operating / deployment modes considered: CLI and API starting configured providers and browser drivers; normal low-complexity direct coder/browser/file/casual routing; `HIGH` complexity route to first-party Planner; browser and code execution under user-supplied configuration. The package requires runtime dependencies and router model weights for actual startup. No live provider/LLM/browser session was launched here.
- Recursion level: One current user-task delivery organization consisting of multiple domain-specialist operational S1 agents under an optional Planner metasystem. A single coder's internal retry loop alone is not reclassified as S3; S3 is evaluated on the Planner's cross-specialist current-work authority.
- Reviewed revision: `4f5f924c1eb326b4163d3bf942954dcc7dd7875b`, frozen under [intake #2000](https://github.com/opensiro/vsm-harness-index/issues/2000) and [batch #2001](https://github.com/opensiro/vsm-harness-index/issues/2001).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipped CLI and API construct distinct `CasualAgent`, `CoderAgent`, `FileAgent`, `BrowserAgent` and `PlannerAgent` instances, each with a model-provider interface, specialized prompt, memory and tools. `Interaction.think` calls the router on the current query and awaits the chosen agent's `process`. The router uses a fixed/few-shot task classifier plus BART voting for domain assignment, while `HIGH` complexity redirects the entire task to `PlannerAgent`. The classifier weights must be separately downloaded into `llm_router`; they are not granted an additional organizational decision function merely because routing can be model-assisted. [CLI](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/cli.py#L24-L75), [routing path](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/router.py#L370-L477), [interaction](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/interaction.py#L275-L305).

Each nontrivial S1 chooses output/tool blocks from model inference and executes local first-party tools. For example, CoderAgent may generate Python/Bash/C/Go/Java blocks, execute them, place interpreter feedback into memory and ask the model again after failure; the browser actor similarly iterates over page/action observations. The operator's configured provider supplies language-model inference, but the agent's loop/action/world coupling and tool feedback are present in this source. [Code agent](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/code_agent.py#L14-L85), [base execute modules](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/agent.py#L257-L287), [browser process](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/browser_agent.py#L347-L445).

In complex-task mode PlannerAgent constructs a JSON plan from the user's whole goal, dispatches each step to a named subordinate domain agent and supplies preceding task results required by later steps. After each subordinate result it receives ordinary task feedback and model-reasons whether subsequent tasks should change, retry or recover from failure. Its `update_plan` prompt expressly bars retroactive changes to earlier steps and revises future work; the top-level `process` loop acts on the revised plan. This is a first-party model-owned whole-current *task portfolio* management function, but there is no evidence of a persistent multi-user organizational supervisor or externally prospective capability redesign. [Planner plan/replan](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L150-L229), [dispatch and current-plan loop](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L232-L310).

## Operational model

In normal mode a request maps to a specialist, the specialist receives a model response, executes tools when relevant and uses the observed result to continue or finish. In complex mode a model-backed Planner decomposes the current goal, chooses subordinate S1 specialists and information dependencies, executes them sequentially, interprets reported successes/failures and remakes its plan for outstanding work. The router is intake triage, while the Planner's substantive current-commitment rights are S3. There is no demonstrated separate S2 stabilization relation between conflicting concurrently operating siblings, independent complementary S3* audit, outside-and-then adaptation into future harness capability, or ultimate identity decision system.

## S1 — Operations

- State: A
- Function: Autonomously fulfill bounded coding, file, web and ordinary conversation tasks by choosing and executing domain tools from task/environment feedback.
- Disturbance / variety regulated: Unanticipated code errors, unavailable local files, changing page contents, tool failures, incomplete web results and variable user requirements.
- Decisive decision or feedback right: Each model-backed specialist chooses its next tool/code/browser action or an answer in response to its prompt, memory and tool observations. CoderAgent decides whether to revise generated code after interpreter failure, within bounded attempts.
- Decision owner: First-party specialist agent loops plus a configured model-backed decision actor; external provider implementations are inference dependencies rather than owners of the agent's executable tool environment.
- Supporting / enforcement mechanisms: Persistent memory, provider interface, tool-block parser, interpreter feedback, browser driver, per-agent status and bounded attempts.
- Closure path: User or Planner subtask → specialized agent model response → first-party tool/browser action → actual result/rejection → feedback in agent memory → further model decision or terminal answer returned to the caller.
- Boundary reachability: Both CLI and API instantiate these concrete agent classes, and `Interaction.think` invokes their `process`; Planner also creates and invokes subordinate instances. This is not merely a test or example path.
- Why this is / is not agent-owned: A fixed router or interpreter does not decide the substantive sequence of code edits, web navigation or recovery; the model-backed specialists do so within their first-party loops.
- Evidence: [shipped CLI construction](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/cli.py#L30-L62); [coder decide/execute/retry](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/code_agent.py#L33-L86); [base feedback](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/agent.py#L173-L195); [tool execution and memory return](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/agent.py#L257-L287).
- Basis: Shipped source-level model/tool decision/action/observation recurrence, not a live effectiveness benchmark.
- Confidence: High for genuine first-party loop topology; runtime success depends on configured models, weights, browser and interpreters.
- Caveats: CasualAgent alone is single-response; S1 credit derives from the active coder, browser and file modes. Code/shell execution risks and model quality were not evaluated.

## S2 — Coordination

- State: —
- Function: No separate first-party function specifically damping interference among concurrently operating S1 specialists is established at the declared task-organization recursion.
- Disturbance / variety regulated: Specialist outputs can depend on one another and could conflict in shared host resources, but the normal Planner dispatches them sequentially rather than observing and attenuating inter-S1 contention.
- Decisive decision or feedback right: The router picks one initial specialist or Planner; Planner chooses handoffs and dependent-step order as its S3 whole-current plan, not a distinct S2 stability/oscillation decision.
- Decision owner: Deterministic router/classifier and model-owned Planner task management; no separate S2 owner or constructor is evidenced.
- Supporting / enforcement mechanisms: Task labels, `need` dependencies, sequential awaits, results dictionary, tool interpreters and language routing.
- Closure path: Planned specialist A finishes → its result is optionally passed to B → Planner may revise subsequent work; this is a hierarchical S3-to-S1 handoff rather than a documented interference attenuation among simultaneously operating sibling S1s.
- Why this is / is not agent-owned: Inter-agent communication and task scheduling are present, but no concrete S1/S1 oscillation, collision detection, quota arbitration or reciprocal stabilizing path is established.
- Evidence: [routing selection](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/router.py#L438-L478); [planner dependency passing](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L232-L260); [sequential loop](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L262-L309).
- Basis: Bounded negative function-specific first-party review.
- Confidence: Medium-high.
- Caveats: No claim that concurrent S1 interference is impossible in other configurations; simply no distinct closed S2 stabilization function is supported by the shipped selected paths.

### Absence scope

- Surfaces inspected: Router, Planner role/task/dependency parsing, subprocess runner, memory, CLI/API agent topology and interpreter/tool execution.
- Plausible first-party paths checked: Static domain routing, model-updated plan order, `need` dependencies, sequential execution, shared-filesystem file agent, thread executor and cross-agent response handoffs.
- Why no material first-party path remains: These either regulate a single agent's work or form the parent Planner's hierarchical current-task management; they do not establish a distinct accountable inter-S1 disturbance attenuation and feedback path.

## S3 — Inside-and-now control

- State: A
- Function: Govern the present commitments and next specialist work across the whole complex user-task portfolio under the supported Planner mode.
- Disturbance / variety regulated: Failed specialist tasks, missing dependency results, multi-step task uncertainty, wasted work, changed feasibility and the need to recover/reprioritize outstanding steps.
- Decisive decision or feedback right: PlannerAgent model chooses current task decomposition, specialist assignment, required predecessor information and revised outstanding steps after interpreting each subordinate's reported result and success/failure.
- Decision owner: A first-party PlannerAgent with its own model-backed memory and `llm_request`; source explicitly requests a new JSON plan after work failure and subsequently acts on the returned plan.
- Supporting / enforcement mechanisms: Task JSON parser, specialist registry, synchronous/awaited subtask calls, result map, ordinary interpreter success flag, bounded plan parse retries and a loop index protecting completed tasks.
- Closure path: Whole user goal → model-authored multi-specialist plan → chosen S1 executes step → result/status returns to Planner → Planner model decides `NO_UPDATE` or a revised subsequent plan → actual next specialist/task choice changes → current goal completes or fails.
- Whole-system current view: The Planner holds the active list of all planned specialist steps, their dependencies and completed work results for the entire *current complex task*. This is the chosen level of recursive whole-system control, not persistent oversight of every independent user session.
- Current-control decision scope: Change future step assignment/content and append recovery work after observing present subordinate outcomes; it does not autonomously set organization-wide budget or identity policy, and cannot rewrite past completed steps.
- Boundary reachability: CLI/API instantiate Planner in the normal agent set; `AgentRouter.select_agent` selects it for `HIGH` complexity, and `Interaction.think` awaits its substantive `process` rather than merely presenting a plan to a human.
- Why this is / is not agent-owned: The `update_plan` step invokes the Planner model for discretionary outcome interpretation and revised commitments; deterministic executor/sequencing only enforces the model-selected plan.
- Evidence: [CLI Planner construction](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/cli.py#L45-L60); [complexity switch](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/router.py#L411-L470); [model-authored plan and correction](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L150-L229); [actual dispatch and replan loop](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L232-L309).
- Basis: Source-backed whole-current delegated task decision/feedback loop, not just presence of a planner name.
- Confidence: High for the supported configured structural path, medium for runtime robustness due external provider/model dependencies and no live execution.
- Caveats: S3 is task-organization scoped; a single specialist's internal retry does not contribute S3 separately, nor does routing into Planner prove any broader fleet-level management.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary inspection that challenges ordinary S1-to-S3 work claims via a separate route is established.
- Disturbance / variety regulated: A specialist can report success despite poor code or untrue web results, but the inspected Planner consumes worker results and ordinary interpreter success rather than an independent audit's alternative reality sample.
- Decisive decision or feedback right: PlannerAgent may revise tasks after reported tool error; no separate auditor acquires complementary raw evidence, judges a disputed claim and returns a challenge into current governance.
- Decision owner: Planner's primary management feedback remains inside S3; tool executors own routine operational pass/fail reports, not independent S3* judgment.
- Supporting / enforcement mechanisms: Interpreter output/error detection, logger, browser result parsing, plan recovery and ordinary unit tests.
- Closure path: Tool outcome → worker response/status → Planner update is an ordinary production/management path; no complementary independent observation → corrective management return is shown.
- Why this is / is not agent-owned: Ordinary tool failure indicators and a second model thought by the same managing Planner do not create an independent audit relation with protected alternative access to reality.
- Evidence: [tool feedback](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/agent.py#L257-L287); [worker-reported plan outcomes](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L184-L247); [results returned](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/planner_agent.py#L263-L309).
- Basis: Negative independence/access review.
- Confidence: Medium-high.
- Caveats: User could separately audit generated code or web claims, but this is not an installed first-party complementary audit function.

### Absence scope

- Surfaces inspected: Planner result/update path, subordinate status, interpreters, browser observations, stored logs, role declarations and unit tests.
- Plausible first-party paths checked: Failed-tool feedback to Planner, code interpreter checks as auditor, use of second domain agent, browser source lookup, per-agent logging.
- Why no material first-party path remains: No separate audit-controlled source or independent adjudication of ordinary operational/management claims is returned to S3; existing paths are part of completing and repairing the same task.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party future-focused environmental intelligence and adopted adaptation of the harness's ongoing organizational capability is established.
- Disturbance / variety regulated: Model limitations, website changes, new tools and future task demands are relevant environmental variety, but the assessed router/Planner reacts to the *current* user task rather than strategically evolving the harness.
- Decisive decision or feedback right: No installed actor compares prospective capability alternatives and commits an updated model/tool/role policy back into subsequent operation.
- Decision owner: Operator/developer chooses provider, prompts, downloaded weights and tool installations; runtime classifiers route current requests with fixed startup examples.
- Supporting / enforcement mechanisms: Fixed task/complexity few-shot classifiers, configurable providers, prompt files, package updates and task-level memory.
- Closure path: Current query → classifier/router → operational specialist or Planner; neither path produces prospective organizational options adopted as changed future capability.
- Why this is / is not agent-owned: The class name `AdaptiveClassifier` and first-party model reasoning do not prove organizational adaptation. Startup examples update a route classifier, not an externally informed future-capability plan with return into S3.
- Evidence: [router fixed startup examples](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/router.py#L25-L69); [few-shot training and local classification](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/router.py#L79-L370); [current-task routing](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/router.py#L411-L478).
- Basis: Bounded negative prospective-adaptation review.
- Confidence: Medium-high.
- Caveats: A local model may generalize during one conversation, but within-session learning/task planning is not S4 at the chosen recursion.

### Absence scope

- Surfaces inspected: Router/classifier initialization, agent prompt files, planner revisions, memory, config/provider selection and installer/update paths.
- Plausible first-party paths checked: Few-shot `AdaptiveClassifier`, task complexity prediction, dynamic file/web findings, Planner replanning, memory, provider changes.
- Why no material first-party path remains: The first-party decisions remain current-task routing/management or human/developer maintenance, without future-oriented external sensing, comparative capability options and adopted return to current harness governance.

## S5 — Identity and ultimate policy

- State: —
- Function: No first-party ultimate identity/policy adjudication loop is established at the user-task agent organization level.
- Disturbance / variety regulated: Provider control, safety, task scope and interaction identity can constrain agent execution, but the shipping system does not settle durable identity or S3/S4 conflicts through a legitimate ultimate authority path.
- Decisive decision or feedback right: User prompts/config set task and role constraints; the system supplies cancellation and sandbox/tool safety support, not an identity-level issue/proposal → final policy decision → binding return.
- Decision owner: The user/operator outside the first-party metasystem chooses durable goals, prompts and permissions; no agent or formal parent-policy mode owns ultimate identity settlement.
- Supporting / enforcement mechanisms: Static prompts, provider config, tool safety scripts, interactive stop, setup/install flags and user task request boundary.
- Closure path: Operational requests remain subject to ordinary user intent, tool constraints and cancellation; no independent ultimate-policy issue reaches an adjudicator and rebinds S3/S4 and subsequent operations.
- Why this is / is not agent-owned: Calling the planner a manager or a prompt a personality does not transfer legitimate organizational identity authority to those components.
- Evidence: [normal user loop](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/cli.py#L45-L77); [interactive stop/request](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/interaction.py#L198-L305); [tool safety](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/tools/safety.py).
- Basis: Bounded negative source review at chosen recursion.
- Confidence: High that task permission/role prompting does not alone close S5; no assertion about external deployer policy.
- Caveats: A broader organization using AgenticSeek might provide human S5 externally; that is not the assessed first-party harness.

### Absence scope

- Surfaces inspected: CLI/API interaction, source safety/tool constraints, role prompts, routing, Planner and documented provider config.
- Plausible first-party paths checked: User as task owner, Planner as policy authority, prompt persona/identity, safe-mode/tool controls and provider settings.
- Why no material first-party path remains: The reviewed source lacks identity/ultimate-policy issue escalation, legitimate final settlement and a binding return to whole-current and prospective governance; ordinary external user approvals and fixed constraints do not qualify.

## Summary and evidence gaps

| Function | S1 | S2 | S3 | S3* | S4 | S5 |
| --- | --- | --- | --- | --- | --- | --- |
| State | A | — | A | — | — | — |

The distinguishing first-party topology is specialized **model/tool S1 loops plus a separate model-backed, optional complex-task whole-current Planner S3** that actually dispatches domain agents and revises outstanding work after reported results. This does not establish peer-interference S2, complementary independent S3*, prospective S4 or ultimate S5. The source test `tests/test_planner_agent_parsing.py` is deliberately mock-backed; executing it in the assessment environment stopped at an undeclared local dependency (`colorama` unavailable), so **no upstream test PASS is asserted**. This is a test-environment observation, not a source-function failure.

All ownership conclusions use frozen-source static inspection and deterministic Index checks only. No live LLM, provider, browser, coding agent, Docker sandbox or effectiveness evaluation was performed. This record is the canonical included assessment at the frozen review ref.
