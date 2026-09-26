---
harness_id: worldgui
project_name: WorldGUI-Agent
repository: https://github.com/showlab/WorldGUI
review_ref: 2117f0a87bcd3b1f330d3727a7ec0643930e7d90
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# WorldGUI-Agent

## Review boundary

- System in focus: one first-party WorldGUI-Agent desktop-computer-use run at pinned revision `2117f0a87bcd3b1f330d3727a7ec0643930e7d90`, including the shipped AutoPC loop, State-Aware Planner/Planner-Critic path, GUI Parser, Step-Check, Actor, Actor-Critic and direct execution of generated PyAutoGUI code.
- Purpose and identity: turn a user desktop-GUI instruction into an executable sequence of GUI actions, observe the changing Windows application state, verify action completion and correct failures until the task is complete or runtime limits are reached.
- Relevant environment: user query, opened project/application, Windows desktop state, screenshots, optional instructional video, model-provider endpoints, OCR/parser dependencies and local machine execution.
- Standard-distribution boundary: documented `test_guithinker_custom.py` / `agent/autopc.py` operating path plus first-party planner, parser, step-check, actor and actor-critic modules directly invoked by that path. Benchmark datasets/results, paper assets, external model providers and OS/application software remain environment or adjacent evaluation/development surfaces.
- Credited operating / distribution surfaces: `README.md`; `test_guithinker_custom.py`; `agent/autopc.py`; `agent/planner_critic/critic_planner.py`; `agent/step_check/stepcheck.py`; `agent/actor/`; `agent/actor_critic/actorcritic.py`; GUI-parser and model-wrapper modules called by the runtime.
- Adjacent first-party surfaces excluded from ownership: WorldGUI benchmark data/scoring, publication/project-page assets, benchmark comparisons, repository development/governance and external OOTB/ShowUI projects.
- First-party operating / deployment modes considered: documented local Windows custom-query execution, including no-video planning; instructional-video mode where present in the same planner path; configured remote/local base-model choices only insofar as they supply model calls to the first-party runtime.
- Recursion level: one desktop task episode is the system-in-focus. Planner, Step-Check, Actor and critics are organizational functions/components inside that run, not separate viable systems merely because they are separate modules or model calls.
- Reviewed revision: `2117f0a87bcd3b1f330d3727a7ec0643930e7d90`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The documented custom runtime creates an `AutoPC`, captures the live application screenshot, parses GUI elements, and calls `run_planner`. The planner first constructs a task/subtask plan from the user query and current screenshot (and optionally instructional-video evidence), then a separate Planner-Critic call checks that plan for wrong, missing or redundant steps and can replace it with corrected steps.

During execution, `AutoPC.run_step` reparses the current GUI. Before ordinary Actor generation, Step-Check inspects the current screenshot and current/next tasks and may mark the current task finished, pass it, modify it, or request an additional region view. If execution is still required, Actor generates executable GUI-control code. The shipped entrypoint directly `exec`s that code against the desktop.

After every ordinary executed action, `test_guithinker_custom.py` changes runtime state from `<Continue>` to `<Critic>`. On the next loop iteration `AutoPC.run_step` therefore invokes Actor-Critic. Actor-Critic receives the current subtask/action plus parsed current GUI and, crucially, the screenshot from before the action together with the screenshot after it. A dedicated critic model call returns an explicit success judgement and reason. On failure, a correction call uses that finding to generate replacement executable code and returns `<Critic>`, causing another execute-and-audit cycle; on success it returns `<Next>` and advances the task plan. This complementary post-action evidence channel is mandatory in the shipped custom runtime, not an optional operator-triggered review.

The architecture still represents one computer-use operation rather than several independent S1 units. Planning, pre-execution checking and action correction regulate the current operational task, so they do not establish a separate superior S3 merely from their names. No persistent capability adaptation across independent future runs and no runtime identity/policy authority were found.

Primary evidence:

- [`README.md`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/README.md) — documented local WorldGUI-Agent runtime and Planner-Critic / Step-Check / Actor / Actor-Critic roles.
- [`test_guithinker_custom.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/test_guithinker_custom.py) — documented executable entrypoint; executes returned code and deterministically enters `<Critic>` after each ordinary action.
- [`agent/autopc.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/autopc.py) — stateful planner/parser/step-check/actor/actor-critic control loop and feedback routing.
- [`agent/actor_critic/actorcritic.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/actor_critic/actorcritic.py) — post-action audit over before/after screenshots, explicit success judgement and correction generation.
- [`agent/step_check/stepcheck.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/step_check/stepcheck.py) — current-state pre-execution validation/modification.
- [`agent/planner_critic/critic_planner.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/planner_critic/critic_planner.py) — plan construction plus separate plan-critique pass using current screenshot and optional instructional knowledge.

## Operational model

The S1 operational outcome is completion of one user-specified desktop task. The runtime repeatedly observes the live GUI, decides what concrete action is needed, generates and executes PyAutoGUI code, observes the changed environment and advances or repairs the current subtask. Planner/Step-Check/Actor together provide ordinary operational control.

Actor-Critic is credited separately as S3* because it audits a concrete operational claim — whether the just-executed action actually completed the current subtask — through a complementary visual path using before/after screenshots rather than relying only on the Actor's generated action or ordinary history. Its finding automatically changes subsequent operation: failure produces replacement code and re-enters the critic cycle; success authorizes advancement to the next planned subtask.

## S1 — Operations

- State: A
- Function: execute a user-requested desktop GUI task through model-selected plans/actions, direct GUI code execution and state-conditioned correction/continuation.
- Disturbance / variety regulated: changing GUI state, uncertain element locations, redundant/already-completed steps, failed or ineffective mouse/keyboard actions, pop-ups and differences between expected and observed application state.
- Decisive decision or feedback right: choose/refine the current plan and subtask, decide whether a current step requires action, generate executable GUI-control code, and continue or revise behavior from observed desktop feedback.
- Decision owner: first-party model-driven WorldGUI-Agent runtime across Planner/Step-Check/Actor paths, with deterministic Python transporting state and executing generated code.
- Supporting / enforcement mechanisms: screenshots, GUI parser/OCR, plan/task iterator, persistent history, Step-Check statuses, Actor code generation, PyAutoGUI execution, step/critic limits and Actor-Critic feedback.
- Closure path: user query + current screenshot -> planner/refined plan -> current subtask + parsed GUI -> Step-Check -> Actor-generated code -> local execution -> changed desktop state -> later runtime decision/audit -> continue, correct or advance until completion/limit.
- Boundary reachability: the documented local entrypoint `test_guithinker_custom.py` directly instantiates `AutoPC`, invokes the credited modules and executes returned code against the user's desktop; no benchmark/evaluation harness is needed to close the operating loop.
- Why this is / is not agent-owned: substantive planning, step selection, GUI action generation and corrections are model-selected from live state; deterministic code supplies transport, execution and bounded-loop mechanics.
- Evidence: [`test_guithinker_custom.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/test_guithinker_custom.py); [`agent/autopc.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/autopc.py); [`agent/step_check/stepcheck.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/step_check/stepcheck.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the user supplies task identity/application and the operator supplies runtime/model configuration; autonomy here concerns within-task operational closure.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 disturbance-attenuation function is established at the declared boundary.
- Disturbance / variety regulated: none qualifying; Planner, Step-Check, Actor and critics are functional stages supporting one desktop operation rather than distinct S1 units whose interaction creates an organizational coordination disturbance.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: module routing, sequential state transitions, shared history and frontend/backend separation are present but do not establish S2.
- Closure path: no material S2-specific closure path established.
- Why this is / is not agent-owned: there is no evidenced S2 function to classify for ownership.
- Evidence: [`agent/autopc.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/autopc.py); [`test_guithinker_custom.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/test_guithinker_custom.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: multiple named modules and model endpoints are not treated as multiple viable operations by default.

### Absence scope

- Surfaces inspected: planner/critic, Step-Check, Actor, Actor-Critic, GUI-parser, AutoPC state/history and documented custom execution loop.
- Plausible first-party paths checked: module orchestration, frontend/backend separation, task/subtask plan structure, shared history and model-role interactions.
- Why no material first-party path remains: no distinct S1 units with an evidenced mutual interference/oscillation/resource disturbance and no relation whose organizational purpose is attenuation of such inter-S1 disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no separate superior inside-and-now regulator is established above the single desktop-operation S1.
- Disturbance / variety regulated: plan quality, current-step necessity, action choice and action failure are regulated inside the current S1 operation.
- Decisive decision or feedback right: none established beyond the task-local planning/action rights already credited under S1.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: Planner-Critic, Step-Check, task iterator, maximum-step and critic-trial bounds are present but do not create a separate whole-system current-control layer.
- Closure path: no material S3-specific whole-system control path established at this recursion.
- Why this is / is not agent-owned: Planner has a whole-task plan, but the assessed system contains one operational desktop mission; planning and subtask advancement are the operation's own control rather than superior regulation over multiple independent S1 units/resources/commitments.
- Evidence: [`agent/planner_critic/critic_planner.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/planner_critic/critic_planner.py); [`agent/autopc.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/autopc.py); [`test_guithinker_custom.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/test_guithinker_custom.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: the component name `Planner-Critic` is not used as evidence of S3.

### Absence scope

- Surfaces inspected: initial/refined planning, plan critique, current/next task state, Step-Check, Actor-Critic, history and loop limits.
- Plausible first-party paths checked: planner whole-task view, plan revision, task advancement, Step-Check modification and critic-count/max-step enforcement.
- Why no material first-party path remains: no separate current-control actor exercises superior authority over multiple independent operational units, their resources, commitments or accountability at the declared recursion.

## S3* — Complementary audit

- State: A
- Function: independently verify whether a just-executed GUI action actually completed the current subtask and return findings that either authorize advancement or cause a corrective action cycle.
- Disturbance / variety regulated: silent GUI-action failure, incorrect clicks/typing, pop-ups, mismatches between intended action and resulting desktop state, and false assumptions that execution succeeded merely because code ran.
- Decisive decision or feedback right: issue the post-action success/failure judgement from observed visual evidence and, on failure, supply a concrete correction path before the operation can advance normally.
- Decision owner: dedicated first-party Actor-Critic model call/module within the autonomous shipped loop; no operator invocation is required after task start.
- Supporting / enforcement mechanisms: dedicated `ActorCritic`, critic-specific prompt/model parameter, parsed GUI state, before/after screenshot pair, explicit `<Success>`/`<Reason>` output, correction prompt/code generation, `<Critic>`/`<Next>` state transitions and bounded repeated critic trials.
- Closure path: Actor produces code -> documented entrypoint executes it -> entrypoint deterministically sets `<Critic>` -> next `AutoPC.run_step` calls Actor-Critic with before/after screenshots -> critic judges completion -> failure generates replacement code and remains in critic cycle; success returns `<Next>` and advances the plan.
- Boundary reachability: `test_guithinker_custom.py` makes the post-action critic transition part of every ordinary executed-action cycle, and `AutoPC.run_actorcritic` directly invokes the shipped Actor-Critic service/module; no adjacent benchmark or human trigger is needed.
- Why this is / is not agent-owned: audit activation, judgement and operational response are closed by the first-party runtime/model loop. The outer Python state machine enforces when audit occurs, while the substantive completion judgement/reason and corrective content are model-produced.
- Evidence: [`test_guithinker_custom.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/test_guithinker_custom.py); [`agent/autopc.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/autopc.py); [`agent/actor_critic/actorcritic.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/actor_critic/actorcritic.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the configured critic model may be the same underlying model family/provider as the Actor. The credited independence is functional/evidentiary: a distinct post-action critic invocation reads complementary before/after visual state instead of relying on ordinary Actor output. Planner-Critic and Step-Check provide additional checking but are not required for the S3* finding.
- Claim being audited: the current Actor-generated GUI action successfully completed the current planned subtask in the real desktop application.
- Ordinary reporting path: Actor selects executable code from the current task, parsed GUI/current screenshot and prior history; successful Python execution itself does not prove the GUI objective was achieved.
- Complementary access path: Actor-Critic is invoked only after execution and receives the previous screenshot plus newly captured post-action screenshot, current action and parsed current GUI, allowing direct comparison of intended versus resulting state.
- Independence boundary: a dedicated Actor-Critic module/model invocation with its own critic prompt and success schema performs the judgement after the Actor/action path has acted. It is separated by execution and fresh environment observation; it need not accept the Actor's implicit success assumption.
- Who acts on findings: `AutoPC` and the documented outer loop. Failure triggers critic-generated replacement code and another execute/audit iteration; success returns `<Next>` so the task iterator advances.

## S4 — Outside-and-then intelligence

- State: —
- Function: no qualifying prospective environmental-intelligence/adaptation function is established.
- Disturbance / variety regulated: screenshots, GUI parsing, instructional-video steps and critic feedback address the current desktop task rather than future organizational capability/posture.
- Decisive decision or feedback right: none established for persistent prospective adaptation.
- Decision owner: none established.
- Supporting / enforcement mechanisms: task history, software tips, instructional-video extraction and self-reflection loops are current-run support, not persistent adaptive redesign.
- Closure path: no material S4-specific prospective change path established.
- Why this is / is not agent-owned: the harness reacts richly to environmental change inside a task but does not select and persist a new capability set/strategy for future independent runs.
- Evidence: [`agent/planner_critic/critic_planner.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/planner_critic/critic_planner.py); [`agent/autopc.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/autopc.py); [`agent/actor_critic/actorcritic.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/actor_critic/actorcritic.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: README's `self-reflection` description is not treated as S4; self-correction of the current operation is not prospective organizational adaptation.

### Absence scope

- Surfaces inspected: planner/Planner-Critic, instructional-video processing, Step-Check, Actor-Critic, persisted per-task history/cache, model configuration and README roadmap/update claims.
- Plausible first-party paths checked: extracted video knowledge, software tips, runtime history persistence, critic corrections and model/component updates.
- Why no material first-party path remains: no shipped runtime loop turns external trend/environment sensing into a persistent model-owned capability or strategic-posture change for later independent tasks.

## S5 — Policy and identity

- State: —
- Function: no runtime authority over organizational identity, ultimate purpose or binding top-level policy is established.
- Disturbance / variety regulated: none qualifying; user query, target software/project, models, limits and static prompts/configuration are externally supplied.
- Decisive decision or feedback right: no runtime actor can redefine the system's ultimate mission or authoritatively resolve constitutional policy/identity conflicts.
- Decision owner: user/operator/repository configuration outside the autonomous runtime.
- Supporting / enforcement mechanisms: command-line task inputs, basic configuration, model selection, static prompts, maximum-step and critic-trial limits constrain operation but are not S5 ownership.
- Closure path: no material S5-specific closure path established.
- Why this is / is not agent-owned: WorldGUI-Agent decides how to execute the supplied desktop task, not what its ultimate identity/purpose or governing policy should be.
- Evidence: [`test_guithinker_custom.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/test_guithinker_custom.py); [`agent/autopc.py`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/agent/autopc.py); [`README.md`](https://github.com/showlab/WorldGUI/blob/2117f0a87bcd3b1f330d3727a7ec0643930e7d90/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: fixed safety/usage prompts and operator-set limits can constrain behavior without transferring S5 authority to the runtime.

### Absence scope

- Surfaces inspected: CLI task/software inputs, AutoPC state, module/model URLs/configuration, planner/critic prompts, completion/limit logic and README deployment modes.
- Plausible first-party paths checked: plan correction, Step-Check modification, Actor-Critic success authority, runtime limits and model selection.
- Why no material first-party path remains: all decisive top-level purpose/identity constraints originate outside the running agent; no first-party runtime function can authoritatively redefine them.

## Recursion, variety and escalation

WorldGUI-Agent increases the variety of one desktop-operation S1 with visual parsing, state-aware planning, pre-execution checking, executable actions and a mandatory complementary post-action visual audit. Planner-Critic and Step-Check are not promoted to higher VSM functions by name. S3* is credited specifically because the post-action audit has a distinct claim, complementary visual access path, functional independence and returned findings that change subsequent operation.

## Standalone conclusion

`A — — A — —`

WorldGUI-Agent autonomously closes both its desktop operation and a complementary post-action audit path. No material first-party S2, superior S3, prospective S4 or runtime S5 closure is established at the pinned boundary.