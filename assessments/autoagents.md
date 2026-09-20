---
harness_id: autoagents
project_name: AutoAgents
repository: https://github.com/OWD-AI/AutoAgents
review_ref: 223ad991988d752c446d25a0381e647f6e71c92c
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-21
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AutoAgents

## Review boundary

- System in focus: the first-party AutoAgents executable runtime at pinned revision `223ad991988d752c446d25a0381e647f6e71c92c`, from user task intake through Manager-generated roles/plan, the generated `Group` operational runtime, model-selected actions/tools, shared environment memory and result production.
- Purpose and identity: automatically construct an expert-role organization for a supplied task and execute that task through LLM-driven expert actions with optional search/file operations.
- Relevant environment: user-supplied task goals, model responses, search/tool observations, prior expert outputs, generated role/plan descriptions, runtime budget and external LLM/search providers.
- Standard-distribution boundary: the shipped `main.py` / `startup.py` command-line and service execution path, `Explorer`, `Environment`, `Manager`, generated `Group`, `Role`/`CustomAction` loops, bundled role/action banks, memory and first-party tool wrappers are credited. External LLM/search providers and user/developer-authored extensions remain outside ownership.
- Credited operating / distribution surfaces: `main.py`, `startup.py`, `autoagents/explorer.py`, `autoagents/environment.py`, `autoagents/roles/manager.py`, `autoagents/roles/group.py`, `autoagents/roles/role.py`, `autoagents/actions/custom_action.py`, `CreateRoles`/`CheckRoles`/`CheckPlans`, first-party role/action banks, command-line and WebSocket service modes.
- Adjacent first-party surfaces excluded from ownership: dormant `ObserverAgents`, `ObserverPlans` and `ActionObserver` classes that are present in the repository but are not wired into the standard `startup.py` path at the reviewed revision; commented-out older per-role/ActionObserver wiring in `Environment.create_roles`; demo/frontend surfaces; repository development/tests/docs; external provider behavior.
- First-party operating / deployment modes considered: standard command-line mode, WebSocket service mode, Docker packaging of the same runtime, Manager setup followed by generated Group execution.
- Recursion level: one AutoAgents task organization. The shipped runtime constructs expert personas/actions inside a single generated `Group` role; those personas are not automatically credited as separate viable recursions merely because the framework calls them agents/roles.
- Reviewed revision: `223ad991988d752c446d25a0381e647f6e71c92c`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

The standard entry point calls `startup.startup`, constructs an `Explorer`, and hires only a `Manager`. The user task is published into the shared `Environment`. The Manager reacts to that requirement by running `CreateRoles` and its own `CheckRoles` / `CheckPlans` actions in a bounded feedback loop. The resulting Manager message contains the role definitions and execution plan; `Environment.publish_message` parses those artifacts and constructs a generated `Group`.

At this pinned revision, `Environment.create_roles` instantiates one `Group` whose action set is dynamically built from the generated role descriptions. Earlier code that instantiated each role separately and added an `ActionObserver` remains commented out. `Environment.run` first lets the original Manager react, then treats the newly created Group as the execution surface and repeatedly runs it until its fixed plan steps are exhausted. The Manager does not remain in a live whole-system supervisory loop over Group execution.

The Group deterministically advances through the Manager-produced plan. For each plan step it selects the generated role-action(s) named in that step. Each `CustomAction` invokes an LLM over prior results/current step/suggestions, chooses a concrete action such as search, file writing, print/final output, executes the first-party tool path where applicable, and may iterate several times until that substep produces a terminal response. This is a first-party autonomous operational decision/action loop even though the plan order itself is fixed.

The repository also contains `ObserverAgents`, `ObserverPlans`, and `ActionObserver` classes. The first two wrap role/plan checks over shared environment messages; `ActionObserver` can ask `NextAction` for necessary information, but its current code still assigns `next_step = self.steps[0]`. More importantly, standard `startup.py` does not hire any of these observer roles, and the corresponding wiring in `Environment.create_roles` is commented out. In the shipped path, role/plan review is therefore performed inside the Manager before operations begin rather than by an independent complementary audit path during operations.

Dynamic role generation and the role bank alter how the current task is staffed, but they do not establish an outside-and-then adaptation loop for AutoAgents itself. The current user task is the object of internal task planning; reviewed memory/role-bank surfaces do not sense prospective environmental change, generate future organizational adaptation options and promote a selected option into later harness capability. Runtime configuration, model/search keys and budget likewise constrain operation without closing identity/ultimate-policy S5.

Primary evidence:

- [`README.md`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/README.md) — shipped purpose, Planner/Observers/Agents/Plan/Actions concepts and supported command-line/service/Docker modes.
- [`startup.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/startup.py) — standard runtime hires only `Manager` before starting the project.
- [`autoagents/roles/manager.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/manager.py) — pre-operation role/plan generation and bounded `CheckRoles`/`CheckPlans` feedback.
- [`autoagents/environment.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/environment.py) — Manager output is parsed into a generated Group; dormant older per-role/ActionObserver wiring is commented out; Group then runs until plan exhaustion.
- [`autoagents/roles/group.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/group.py) — generated expert actions and fixed plan-step execution.
- [`autoagents/actions/custom_action.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/actions/custom_action.py) — LLM chooses current operational action/tool and receives resulting output within each step.
- [`autoagents/roles/role.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/role.py) — generic observe/think/act/publish loop and model-selected action state for multi-action roles.
- [`autoagents/roles/observer.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/observer.py) and [`autoagents/roles/action_observer.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/action_observer.py) — observer implementations inspected but not credited because the standard startup path does not wire them into operation.
- [`autoagents/actions/check_roles.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/actions/check_roles.py) and [`autoagents/actions/check_plans.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/actions/check_plans.py) — role/plan review operates on generated design artifacts rather than complementary operational reality.

## Operational model

A task enters the Environment and wakes the Manager. The Manager uses an LLM to generate expert role definitions and an execution plan, then repeatedly reviews those design artifacts with its own role/plan-check actions until they report no suggestions or the bounded review loop ends. The Environment parses that final design and creates a Group whose action objects embody the generated expert personas.

The Group then becomes the task-execution cell. It advances through the generated plan, invokes the relevant expert action(s), and each CustomAction decides how to complete the current step from accumulated results. Search results or file operations can feed the current action, and intermediate action outputs are accumulated into subsequent iterations/steps until the Group exhausts the plan and produces the final result.

This separation matters for the metasystem mapping. Manager planning is organizational construction before current operations, not a persistent current-control loop over live S1 state. The advertised Observer components are not reachable in the standard startup mode. Generated roles/actions are also implemented inside one Group execution cell at this revision, so generic multi-agent vocabulary is not sufficient to infer either multiple distinct S1 units or S2 coordination.

## S1 — Operations

- State: A
- Function: autonomously execute the supplied task through first-party model-driven expert actions and tool/result feedback inside the generated Group.
- Disturbance / variety regulated: ambiguity in the current task step, accumulated prior outputs, search/tool observations, uncertainty over which available action/tool to use and whether more subwork is required.
- Decisive decision or feedback right: choose the substantive current action/tool and action input from the step context, then use returned results to continue or conclude the step.
- Decision owner: the LLM-driven generated `CustomAction` / Group operational loop.
- Supporting / enforcement mechanisms: fixed Manager-produced plan, Group step iterator, Environment shared memory/history, parser/schema repair, search wrapper, filesystem writes, budget check and external model/search APIs.
- Closure path: user task → Manager constructs Group/plan → Group reaches a step → generated model action chooses operational action/tool → first-party runtime executes or records result → result is accumulated into later model iterations/plan steps → final task output.
- Boundary reachability: `startup.py` creates the Manager and `Environment.publish_message` creates the Group in the ordinary command-line/service path; `Group._act` directly runs the generated `CustomAction` instances, so the credited operational loop is wired into the shipped standard distribution.
- Why this is / is not agent-owned: deterministic plan ordering and runtime wrappers constrain execution, but the model chooses substantive per-step actions/tool inputs from current context. Removing the model decision leaves the Group without materially the same operational choice.
- Evidence: [`startup.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/startup.py), [`autoagents/environment.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/environment.py), [`autoagents/roles/group.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/group.py), [`autoagents/actions/custom_action.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/actions/custom_action.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the generated expert personas are implemented as action objects within a single Group role at this revision; S1=A therefore credits the autonomous operational cell without treating every persona label as a separate viable S1 recursion.

## S2 — Coordination

- State: —
- Function: no qualifying S2-specific attenuation of a concrete interference/conflict/oscillation among distinct S1 operational units is established in the shipped runtime.
- Disturbance / variety regulated: no specific qualifying inter-S1 disturbance is established.
- Decisive decision or feedback right: none established for S2-specific coordination.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: Manager-generated role division, fixed multi-step plan, shared Environment memory, Group accumulation of prior outputs and sequential invocation of generated expert actions.
- Closure path: no evidenced inter-S1 disturbance → attenuation decision/relation → changed subsequent S1 behaviour loop is supplied.
- Why this is / is not agent-owned: the framework decomposes and sequences work, but the reviewed standard implementation collapses generated expert personas into action objects inside one Group role and does not identify a concrete cross-S1 conflict that its sequencing is specifically regulating.
- Evidence: [`autoagents/environment.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/environment.py), [`autoagents/roles/group.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/group.py), [`autoagents/roles/manager.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/manager.py).
- Basis: structural absence after function-first review.
- Confidence: high.
- Caveats: older/commented per-role wiring or a downstream composition could create distinct S1 units and an S2 problem, but that is not the credited standard-distribution path at the pinned revision.

### Absence scope

- Surfaces inspected: Manager role/plan generation, Environment role creation, Group execution, shared memory, generated role actions, dormant per-role/ActionObserver code and standard startup wiring.
- Plausible first-party paths checked: generated role division, shared memory, plan sequencing, repeated multi-role actions, Observer messaging and the commented separate-role implementation.
- Why no material first-party path remains: active runtime sequencing transports/decomposes work but neither establishes distinct operational units with a concrete interference mode nor a dedicated attenuation relation whose feedback changes their later behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control loop is established after the generated organization enters operation.
- Disturbance / variety regulated: Manager handles task design variety before Group execution, but no actor is shown regulating changing whole-organization current commitments/resources/priorities while operations proceed.
- Decisive decision or feedback right: none established over live whole-system operations.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: Manager role/plan construction, Explorer budget limit, Environment scheduler/run loop, Group fixed step ordering and bounded action iterations.
- Closure path: Manager design output creates the Group and plan, but once Group execution begins the Manager is excluded from the new-role execution loop; no live fleet/organization view → current-control decision → returned operational intervention path is supplied.
- Why this is / is not agent-owned: the Manager owns decomposition/design choices, not evidenced current S3 regulation; deterministic budget/run/step machinery enforces bounds without owning whole-system current discretion.
- Evidence: [`startup.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/startup.py), [`autoagents/roles/manager.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/manager.py), [`autoagents/environment.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/environment.py), [`autoagents/roles/group.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/group.py).
- Basis: structural absence after function-first review.
- Confidence: high.
- Caveats: the component is named Manager and creates the organization, but Profile 0.2.3 explicitly does not equate planning/task allocation with S3 without a whole-system current view and intervention right.

### Absence scope

- Surfaces inspected: Manager action loop, Explorer budget enforcement, Environment lifecycle/run scheduling, Group execution and dormant observer paths.
- Plausible first-party paths checked: Manager planning/review, runtime budget check, environment-wide memory, Group step selection and any return from operations to Manager for replanning/reallocation.
- Why no material first-party path remains: the Manager is part of the initial role set and does not participate in the subsequent loop that runs newly created Group operations; no current whole-system state/authority loop over active operations remains.

## S3* — Complementary audit

- State: —
- Function: no reachable standard-distribution complementary audit path with sufficiently independent access to operational reality and corrective return is established.
- Disturbance / variety regulated: role/plan design errors are reviewed before execution, but hidden divergence between ordinary operational claims and independent reality is not audited through a qualifying S3* path.
- Decisive decision or feedback right: none established for a complete complementary operational audit loop.
- Decision owner: none established for S3* publication.
- Supporting / enforcement mechanisms: Manager-owned `CheckRoles` / `CheckPlans`; repository `ObserverAgents`, `ObserverPlans`, and `ActionObserver` classes; Environment history/logging.
- Closure path: Manager-generated role/plan artifacts → Manager's own review actions → suggestions → regenerated/reviewed design. This is pre-operation self-review. The separate Observer classes are not hired by `startup.py`, and the older ActionObserver wiring is commented out, so no standard complementary operational evidence → findings → corrective S1 return closes.
- Why this is / is not agent-owned: model-based review exists, but the active checks operate inside the same Manager planning path over its own design artifacts. They neither provide complementary access to live operational reality nor constitute a wired independent audit actor in the assessed mode.
- Evidence: [`autoagents/roles/manager.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/manager.py), [`autoagents/actions/check_roles.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/actions/check_roles.py), [`autoagents/actions/check_plans.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/actions/check_plans.py), [`startup.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/startup.py), [`autoagents/environment.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/environment.py), [`autoagents/roles/observer.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/observer.py).
- Basis: structural absence after boundary/reachability review.
- Confidence: high.
- Caveats: repository-local Observer implementations show an intended audit-like design surface, but Methodology 0.3.5 forbids borrowing closure from adjacent/unwired first-party code.

### Absence scope

- Surfaces inspected: Manager review loop, role/plan check actions, observer role classes, ActionObserver, Environment standard role creation/run path, history/logging and README observer description.
- Plausible first-party paths checked: separate observer hiring, operational artifact inspection, Manager review feedback, ActionObserver runtime checking and findings returned to Group/S1.
- Why no material first-party path remains: standard startup hires only Manager; active role/plan checks are self-review before operations; dormant observers are not boundary-reachable; no complementary operational evidence path closes findings back into corrective execution.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective organizational adaptation loop for future AutoAgents capability is established.
- Disturbance / variety regulated: current task requirements and tool observations affect current execution, but prospective environmental change affecting future harness capability is not regulated through S4.
- Decisive decision or feedback right: none established for selecting and promoting a future capability adaptation.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: dynamic role/plan generation, role/action banks, search observations, memory/long-term-memory substrate and repeated Manager design review.
- Closure path: user task → roles/plan tailored to that same task → current Group execution. No prospective environmental distinction → adaptation options → selected option → changed later AutoAgents capability/S3 loop is established.
- Why this is / is not agent-owned: the Manager autonomously constructs a current-task organization, but Profile 0.2.3 distinguishes internal task planning from S4. RoleBank is a bundled/developer-authored capability surface rather than evidence of autonomous future adaptation.
- Evidence: [`autoagents/roles/manager.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/manager.py), [`autoagents/environment.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/environment.py), [`autoagents/roles/role_bank/`](https://github.com/OWD-AI/AutoAgents/tree/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/role_bank), [`autoagents/roles/role.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/role.py), [`README.md`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/README.md).
- Basis: explicit/structural absence after future-adaptation review.
- Confidence: high.
- Caveats: dynamic agent generation can be a mechanism used by an S4-capable downstream organization, but current-task staffing alone does not establish the S4 function.

### Absence scope

- Surfaces inspected: Manager dynamic role generation, plan generation/review, role bank, action bank, search/tool paths, RoleContext long-term memory and Environment persistence/history.
- Plausible first-party paths checked: reuse of learned roles, persistent adaptation across tasks, environmental trend/threat sensing, generation of future alternatives and promotion of those alternatives into later runtime capability.
- Why no material first-party path remains: reviewed paths customize current task execution or retain information/templates; none establishes external-and-prospective sensing plus future adaptation choice and return into present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision loop is established at the assessed AutoAgents organization boundary.
- Disturbance / variety regulated: ordinary task goals, provider/tool configuration and budget constrain work, but no identity-level S3–S4 tension or ultimate-policy issue is shown entering an authoritative closure loop.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5 publication.
- Supporting / enforcement mechanisms: user task, Manager prompt/goal, configured API/model/search choices, Explorer investment/budget and developer-authored role/action definitions.
- Closure path: no identity/ultimate-policy issue → legitimate authority → authoritative decision → returned governance of subsequent operation path is established.
- Why this is / is not agent-owned: the Manager and generated roles operate under authored goals/constraints, but prompts/configuration and ordinary task authority are not S5 by themselves.
- Evidence: [`startup.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/startup.py), [`autoagents/explorer.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/explorer.py), [`autoagents/roles/manager.py`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/autoagents/roles/manager.py), [`README.md`](https://github.com/OWD-AI/AutoAgents/blob/223ad991988d752c446d25a0381e647f6e71c92c/README.md).
- Basis: structural absence after identity/policy review.
- Confidence: high.
- Caveats: the operator remains able to choose tasks/configuration, but generic operator input does not establish a first-party parent S5 mode without an identity-level issue and closed return path.

### Absence scope

- Surfaces inspected: CLI/service inputs, Manager goals/prompts, Explorer budget, runtime configuration, role/action definitions and standard execution path.
- Plausible first-party paths checked: agent-owned constitution/policy revision, human/parent identity escalation, durable organization-level purpose change and returned authoritative policy affecting later operation.
- Why no material first-party path remains: inspected controls govern ordinary task execution and resource/configuration bounds; none closes identity or ultimate policy at the declared recursion.

## Recursion

The assessed system is one generated AutoAgents task organization. The Manager constructs an execution design and the runtime then realizes generated expert personas as action objects inside one Group role. Those personas can make local operational decisions, but the pinned standard implementation does not establish them as durable viable suborganizations with their own full metasystem and environment. Spawning/generating role descriptions therefore is not credited as VSM recursion by itself.

## Variety and escalation

AutoAgents amplifies operational variety by generating role prompts and a task-specific plan from the user goal, then lets generated model actions choose search/file/final-output behavior from accumulated context. Shared Environment memory and fixed plan steps attenuate information into the next operational stage. Parser/schema repair, bounded Manager review, bounded Group iterations and the Explorer budget provide deterministic limits.

Escalation is primarily internal to the current model/action loops: malformed outputs may be repaired/retried and Manager design suggestions feed another design iteration. No separate whole-system S3 exception path, independent S3* audit escalation, prospective S4 adaptation escalation or S5 identity escalation is established in the standard distribution.

## Evidence gaps

No material evidence gap requires `?` at the reviewed boundary. The main ambiguity suggested by README terminology is resolved by source reachability: separate Observer classes and older separate-role/ActionObserver wiring exist, but are not included in the standard `startup.py` execution path at the frozen revision. A materially different downstream composition that activates those paths would be a separate system-in-focus and would require its own assessment.
