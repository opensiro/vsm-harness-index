---
harness_id: multi-agent-harness
project_name: Multi-Agent Harness²
repository: https://github.com/WeiminWu2000/Multi-Agent-Harness-2
review_ref: 1ac2ad1c2793805c72623a6086bb80c91063c532
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Multi-Agent Harness²

## Review boundary

- System in focus: the repository-owned seven-role AppWorld agent execution team plus its outer task-local harness-improvement controller; integrated custom-team constructor and local scientific adapter are considered without borrowing their external executors.
- Purpose and identity: perform a user-supplied task with analyzer/planner/coder/verifier/router/debugger/finalizer roles, diagnose information-transfer failures and improve the team's role procedures and handoffs across bounded repeated rounds.
- Relevant environment: public AppWorld API/task state or user-supplied public scientific data, model gateway, budget and tool execution, external AppWorld service/evaluator and installed upstream prompt components.
- Standard-distribution boundary: shipped `mah2` AppWorld CLI/team, public-evidence editors, selector, recursive optimizer and harness schema/validation. Optional AppWorld package/model provider are execution dependencies; a callback-based custom team supplies its own executor.
- Credited operating / distribution surfaces: `mah2/appworld_cli.py`, `appworld_adapter.py` (`Team`), `appworld_worker.py` (public API), `appworld_optimizer.py`, `dsstar/optimizer.py`, `dsstar/recursion.py`, `dsstar/harness.py`, `gateway.py`, and their public configuration.
- Adjacent first-party surfaces excluded from ownership: test fixtures/scripted demos, `examples/existing_team.py`, developer CI/CONTRIBUTING, official post-commit AppWorld evaluator and grader, fetched `vendor/` upstream prompt code, Qwen-code executable in scientific adapter, MASS upstream dependency and developer research notes. None supplies an additional independent active S3* auditor or identity governor.
- First-party operating / deployment modes considered: AppWorld `base` fixed team, `harness2` two-round role/coordination improvement and current-round selection, optional `mass` workflow search, local scientific-Python adapter, custom existing-team callback mode, dry-run and no-key scripted demonstrations. Positive claims rest on the first-party model-directed AppWorld `harness2` mode, not the scripted smoke or external Qwen-code agent.
- Recursion level: one task-oriented seven-role operational team plus the bounded optimizer that governs subsequent team configuration. Outer task-local rounds are capability revision, not a claim of an independent recursively viable enterprise.
- Reviewed revision: `1ac2ad1c2793805c72623a6086bb80c91063c532`.
- Observation date: 2026-11-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`Team.run` makes model gateway requests for seven separately prompted roles. Analyzer explores public API state, planner chooses steps, coder/debugger produce Python for a fresh `AppWorld` worker, verifier evaluates reported public execution progress, router decides continue/finalize and finalizer submits. State, handoff contracts and bounded public history feed later roles. Each outer round executes a reference team, calls independent scoped model editors for role and coordination changes, executes candidate teams in fresh environments, composes a successor, selects one current-round execution from public evidence, and carries the selected harness into the next round. Invalid edits/citations are rejected; exact reuse requires harness/program identity. The official AppWorld grader runs only *after* final selection and cannot be borrowed as runtime evaluator or S3*. The separate scientific adapter may invoke an external Qwen-code executable; it is not needed to support the positive claims from the first-party AppWorld team.

Primary evidence: [README](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/README.md), [architecture](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/docs/architecture.md), [team code](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_adapter.py), [AppWorld optimizer](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_optimizer.py), [canonical optimizer](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/dsstar/optimizer.py), [recursion controller](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/dsstar/recursion.py), [schema](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/dsstar/harness.py).

## Operational model

Seven distinct model-decision roles operate against a shared task, with the gateway and tools carrying their selections. The decisive model output is the choice of next environment action, team continuation, coordination edit or future-harness proposal; deterministic schema validation, stage budgets and isolated workers enforce constraints. A team role being named "verifier" does not alone demonstrate independently acquired complementary audit evidence. The benchmark's official evaluator is post-commit and external. A planned/full task success rate is not inferred from source or scripted tests.

## S1 — Operations

- State: A
- Function: agent roles perform public-environment task work and turn observations into actions and final deliverables.
- Disturbance / variety regulated: changing AppWorld task requirements, API responses, intermediate state changes, execution errors and incomplete task progress.
- Decisive decision or feedback right: analyzer chooses inspection code; planner decides next work; coder/debugger choose executable API actions; finalizer chooses submitted task response.
- Decision owner: model-driven role actors instantiated by `Team.ask`; `Team.run` delivers their choices to `World.execute` and subsequent role prompts.
- Supporting / enforcement mechanisms: bounded `Gateway.request`, AppWorld worker, `max_team_steps`, typed role JSON and persistent trace/event store.
- Closure path: task/public API evidence → role model decisions → Python API effects/results → shared `state`/public interaction history → subsequent model decision and finalizer.
- Boundary reachability: `mah2 appworld --method harness2 --execute` runs the packaged first-party role actor with configured provider; `base` runs the same team without improvement; neither depends on an unshipped custom executor.
- Why this is / is not agent-owned: model roles select substantive next operations; AppWorld and gateway execute/limit, rather than autonomously deciding task content.
- Evidence: [team](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_adapter.py), [AppWorld worker](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_worker.py), [README CLI](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no credentials were supplied for a live paid provider/AppWorld run; code wiring and supported launch mode, not achieved benchmark success, are assessed.

## S2 — Coordination

- State: A
- Distinct S1 units: analyzer, planner, coder, verifier, router, debugger and finalizer each make model-directed role choices over the same task within `Team.run`.
- Inter-S1 disturbance: coder may act on stale/incomplete planner context; verifier's corrective diagnosis can be lost or ignored by router/planner; mismatched producer/consumer handoffs can perpetuate failed work cycles.
- Attenuating coordination relation: `proposal_b` model editor targets one diagnosed handoff or feedback route and its producer/consumer contract, probes the change in a separate team run, and the composer/selector adopts a tested version.
- Feedback into subsequent S1 behaviour: selected `coordination` routes and contracts alter future `Team.ask` handoff fields and instructions; the next round runs the selected harness rather than a mere logged proposal.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the editor identifies an actual role-interference mechanism from event evidence and changes *both ends* of a concrete coordination contract; a generic mailbox or static ordered role call would not do so.
- Function: diagnostic handoff repair regulates erroneous or lost information between planning, coding, verification, routing and later corrective work.
- Disturbance / variety regulated: stale/omitted verifier diagnosis, mismatched producer-consumer requirements, coder missing task context and repeated failed plan/execution handoffs among distinct role S1 cells.
- Decisive decision or feedback right: propose or reject a one-route coordination change from actual public execution events and apply selected shared contracts/diagnostic routes to later role interactions.
- Decision owner: independent scoped model `proposal_b` chooses targeted coordination repairs, model composer elects between validated coordination options based on candidate traces; deterministic schema checker limits legal edits.
- Supporting / enforcement mechanisms: `coordination.version`, `contracts`, `planner_receives_diagnosis`, `router_receives_diagnosis`, `verifier_diagnosis`, paired sender/receiver instructions, schema-scoped edits and fresh candidate probes.
- Closure path: execution trace of analyzer/planner/coder/verifier/router interdependence → coordination editor diagnoses lost/ignored information → candidate probe/composer selection → chosen harness's revised contracts/diagnosis reach later `Team.ask` handoffs and change subsequent S1 behavior.
- Boundary reachability: AppWorld `harness2` directly executes the coordination editor and applies selected `harness['coordination']` in the bundled `Team.ask`, with carried-forward harness in the next round; this is not only the generic custom-team callback.
- Why this is / is not agent-owned: model editors choose whether/which interference to attenuate, while runtime validates schemas and transports the chosen handoff; generic role sequencing by itself would not establish this S2 claim.
- Evidence: [coordination editor](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_optimizer.py), [team handoff](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_adapter.py), [coordination schema](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/dsstar/harness.py), [architecture](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: fixed base mode may not enable diagnosis routes; the positive is from documented operational `harness2` adaptation and composition, not from a mailbox/edge alone. Actual realized coordination improvement is unproven without a provider run.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: the router receives the team's current plan and execution feedback, optional verifier diagnosis and bounded public interaction history across the seven-role task unit.
- Current-control decision scope: accept/finalize the team's current work or commit remaining execution steps to another planning/coding cycle; error events can route current resources to debugger recovery.
- Function: current task-team progress supervision decides whether to continue work or seek final completion, with bounded present-run intervention on errors.
- Disturbance / variety regulated: unfinished task state, coding errors, contradictory/incomplete verification and scarce team execution steps.
- Decisive decision or feedback right: select `continue` versus `finalize` based on team execution state and verifier diagnosis; select whether finalizer proceeds or planner/coder receives another work cycle.
- Decision owner: model-directed `router` role, supported by the `verifier` judgment and deterministic `Team.run` scheduling.
- Supporting / enforcement mechanisms: team state (`plans`, `execution`, `verification`, `routing`), step cap, JSON route parsing, worker lifecycle and latest public history.
- Closure path: team execution/verification observations → router model decision → `Team.run` branches to finalizer or next planner/coder cycle; failed code triggers debugger branch for team recovery.
- Boundary reachability: router, verifier and conditional finalizer/next-plan branches run as part of the packaged AppWorld task team with no separate unshipped manager plugin.
- Why this is / is not agent-owned: router owns a task-team-level current commitment and intervention decision; static loop limits enforce developer budgets but do not choose the team route.
- Evidence: [Team.run](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_adapter.py), [architecture](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/docs/architecture.md).
- Basis: structural.
- Confidence: medium.
- Caveats: supervisory scope is the *one-task team*, not cross-task organization/resource governance. This is more than speaker selection only insofar as the route controls the team's present execution commitment.

## S3* — Complementary audit

- State: —
- Function: sufficiently independent complementary observation and challenge of operational claims is not established inside the shipped runtime.
- Disturbance / variety regulated: incorrect execution assumptions and incomplete progress are discussed by verifier, while official task correctness is independently checked only after final commitment.
- Decisive decision or feedback right: inspect operational reality via a separate enough evidence route, challenge ordinary reports and return corrective findings into team control.
- Decision owner: `verifier` model critiques the **same public interaction history and handoff `state.execution`** it receives from coder/runtime; official AppWorld grader is a separate post-commit evaluation dependency, not in-run auditor.
- Supporting / enforcement mechanisms: verifier role prompt, diagnostics in shared state, trace and optional official grader after selection.
- Closure path: verifier can return a progress diagnosis into router/planner, but lacks a distinct complementary source-observing evidence acquisition path. Official grading occurs only after selection, never returns into live candidate choices.
- Why this is / is not agent-owned: a model called verifier is a routine in-band checker, and post-commit external benchmark evaluation cannot be treated as a first-party S3* owner.
- Evidence: [Team.ask/Team.run](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_adapter.py), [post-commit grader boundary](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/docs/architecture.md).
- Basis: structural.
- Confidence: medium.
- Caveats: verifier has distinct role prompt and reasoning, but no evidenced independent operational data path distinct from the normal team reports; an added self-check tool could change this result at another pinned revision.

### Absence scope

- Surfaces inspected: team role prompts/data fields, worker `execute` channel, public traces, optimizer's current-round selection, official evaluator boundary and custom-team callback contract.
- Plausible first-party paths checked: verifier as S3*, public trace editor/selector as auditor, grader as independent challenge, model-gateway stages as independent observer.
- Why no material first-party path remains: all in-run checks consume same team-produced public state/results or select candidates; the genuinely separate official evaluator is external and starts after final commitment, with no feedback to candidate execution.

## S4 — Outside-and-then intelligence

- State: A
- External distinction: observed AppWorld public API responses, task demands, failure traces and execution outcomes reveal environmental requirements rather than merely internal source-code intentions.
- Future / prospective distinction: diagnosis targets the *next* execution of the team, via alternate role/coordination instructions in new candidate worlds and the subsequent outer round, not only repairing the current API call.
- Adaptation option generated: model role and coordination editors propose bounded harness variants; composer selects/revises a successor based on independent candidate probes and observed public evidence.
- Path back into current capability / S3: current-round selector commits `selected_harness.json`; `run_recursive` uses that configuration as the next reference team, changing role and handoff capability while the router retains present execution control.
- Function: adapt future team operating capability to observed public task/environment failures and potential coordination changes rather than merely repairing the current line of code.
- Disturbance / variety regulated: mismatch between role procedures/handoffs and evolving public task requirements, recurring mistakes, and unsuitable coordination for subsequent rounds.
- Decisive decision or feedback right: choose evidence-linked role/procedure options, test alternatives, compose a successor harness and choose the next-round configuration.
- Decision owner: model-directed `proposal_a` and `proposal_b` editors, composer and selector, with the recursive controller transporting the selected harness into the next round.
- Supporting / enforcement mechanisms: trace event IDs/citation validation, candidate isolation, stage budgets, scope-limited schema validation, current-round selection, lesson library and program/harness identity checks.
- Closure path: reference task/environment trace → role and coordination model hypotheses → fresh candidate probes and composition → public-evidence selector commitment → `run_recursive` carries `selected_harness.json` forward as the next round's operative role/coordination capability.
- Boundary reachability: bundled AppWorld `harness2` mode has two configured rounds and invokes these first-party editors/selector/recursion paths; not only an unshipped development benchmark or an external research paper.
- Why this is / is not agent-owned: LLM stages choose change proposals and selections; budget checks, schema constraints and trace citations enforce without making those adaptation judgments.
- Evidence: [AppWorld optimizer](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_optimizer.py), [round execution](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/dsstar/optimizer.py), [recursive carry](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/dsstar/recursion.py), [architecture](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is prospective **task-local** next-round adaptation only; no claim of persistent fleet-wide intelligence or cross-task self-improvement, and no successful improvement is asserted.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/policy decision loop over team/optimizer is shipped.
- Disturbance / variety regulated: API budgets, editable roles/allowed coordination routes and official evaluation separation are bounded by static developer/operator policy.
- Decisive decision or feedback right: decide/revise team/system ultimate policy or identity and authoritatively return it to later operations.
- Decision owner: external developers/operator choose hard-coded schema, model/budget/environment and command flags; model editors may change role procedures and **existing** bounded routes but cannot change identities, roster, tool infrastructure, budget, evaluator or ultimate policy.
- Supporting / enforcement mechanisms: schema `validate`, restricted editor surfaces, stage budgets, protected grader separation and configuration file.
- Closure path: invalid schema/policy changes are rejected; task-local harness procedure updates are S2/S4-level capability changes, not ultimate-policy decisions.
- Why this is / is not agent-owned: a configured governance limit, role prompt or operator selecting `--grade` does not itself provide an identity-level issue→decision→returned authority path.
- Evidence: [schema constraints](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/dsstar/harness.py), [editor constraints](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/mah2/appworld_optimizer.py), [architecture](https://github.com/WeiminWu2000/Multi-Agent-Harness-2/blob/1ac2ad1c2793805c72623a6086bb80c91063c532/docs/architecture.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: model-proposed coordination rewrites do not promote routine task policy to S5, and external maintainer roadmap is outside this runtime.

### Absence scope

- Surfaces inspected: `harness.initial`/`validate`, editor scope rules, AppWorld team/worker, CLI, configuration, recursive controller, docs and custom-team integration contract.
- Plausible first-party paths checked: editable procedures as S5, coordination contract version as identity policy, hard budget/evaluator boundary as S5, parent operator CLI as legitimate S5 closure.
- Why no material first-party path remains: the team identity/ultimate rules and model/tool authority stay externally fixed; no first-party runtime identity-level matter, legitimate final authority or returned new policy is encoded.

## Distributed OSS parent arrangement

No open-source maintainer/contributor workflow is promoted to a parent S3/S4/S5 mode of the shipped task team. AppWorld operator/provider rights and command-line flags are operational configuration choices, not an independently demonstrated ultimate-policy decision/return path.

## Self-hosted and non-human modes

The first-party AppWorld runner can use a self-provided model API credential and local AppWorld installation; the seven model-role team can operate without a human approving each role action, under fixed budget/step limits. Custom-team callbacks may be integrated but supply the actual team execution and are not separately credited to the current fixed distribution. No additional provider independence or true non-human parent governance is inferred.

## Recursion, variety, escalation and evidence gaps

- Recursion: seven role actors are task-team S1 cells; outer harness adaptation returns new capabilities to this team and is not, by itself, a separate whole-enterprise recursion.
- Variety: public API task variety enters through analyzer/coder execution, current operational conflict through verification/routing and inter-role handoff repair, and future-capability variety through reference/candidate/probe selection.
- Escalation: task errors go to debugger/router; stage budget and invalid edits stop/fall back, while unresolved outcomes are preserved and may later be officially graded post-commit. No independent S3* or parent S5 closure is claimed.
- Evidence gaps: no paid-model/AppWorld live run; source unit test discovery was partially blocked by absent `requests` and AppWorld dependencies (14 tests discovered, 13 setup/import errors). This does not certify task success, real measured improvements, current provider availability, or independent external benchmark accuracy.

## Outcome

**Proposed admission.** The first-party AppWorld mode supplies model-directed S1 operations, specific cross-role coordination feedback/repair, task-team current control and task-local next-round adaptation. It does not supply independently sourced complementary S3* audit or ultimate-policy S5 closure in the assessed distribution.
