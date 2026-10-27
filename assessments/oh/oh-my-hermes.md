---
harness_id: oh-my-hermes
project_name: Oh My Hermes
repository: https://github.com/witt3rd/oh-my-hermes
review_ref: 3b06e33ae67b202b342989b484f08143e65e250d
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Oh My Hermes

## Review boundary

- System in focus: one user-invoked Oh My Hermes (OMH) multi-agent project workflow operating inside a supported Hermes Agent installation, with the optional shipped OMH plugin and skills installed; not Hermes as a whole or the upstream contributor organization.
- Purpose and identity: compose planning, execution, project evidence and feedback into persistent, multi-invocation task workflows with specialized model roles.
- Relevant environment: a host software project and its changing source/tests, user specifications, Hermes delegation and tool permissions, provider availability, concurrent sessions, tool errors and repository-local state.
- Standard-distribution boundary: repository-distributed OMH skills, optional `plugins/omh/` with `omh_state`, `omh_gather_evidence`, role hooks, dispatch breadcrumbs and documented local `.omh/` artifacts. Hermes `delegate_task` and model execution are external runtime dependencies rather than first-party OMH implementation.
- Credited operating / distribution surfaces: `plugins/omh/skills/{omh-ralplan,omh-ralph,omh-autopilot,omh-deep-research,omh-deep-interview}/`, plugin manifest, `omh_state.py`, `omh_delegate.py`, `tools/state_tool.py`, `tools/evidence_tool.py`, hooks and role prompt assets as explicitly installed modes.
- Adjacent first-party surfaces excluded from ownership: `docs/research/`, upstream-Hermes proposals, OMC reference comparisons, roadmap, contributor/CI/test fixtures and uninstalled/plugin-free experimental integrations. Other users' independent Hermes sessions are not silently included in one workflow.
- First-party operating / deployment modes considered: installed standalone skills, installed optional plugin (including state and evidence tools), `omh-ralph` one-task-per-call, `omh-autopilot` phase-by-phase, parallel executor tasks with locks, and first-party research/plan modes. An external caller must reinvoke the skill between phases; no always-running daemon is claimed.
- Recursion level: one project-scoped OMH workflow with a coordinating Hermes parent and delegated task agents; neither child role nor concurrent independent workflow is presumed individually viable.
- Reviewed revision: `3b06e33ae67b202b342989b484f08143e65e250d`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

OMH installs declarative Hermes skills and, optionally, a Python plugin. The skills prescribe model-guided planning, delegated execution, acceptance-criteria verification, persistent progress and re-invocation. The plugin adds atomic project-state storage, per-instance advisory locks, role-prompt injection into Hermes child sessions, a guarded deterministic evidence-command tool and `omh_delegate` prepare/finalize breadcrumbs. The plugin does **not** itself implement Hermes's model loop or `delegate_task`. The main supported `ralph` mode selects plan tasks, delegates implementation, gathers fresh build/test/lint output, delegates acceptance review, records verdicts and learnings, and on failure retries or blocks. `autopilot` composes spec, plan, execution, QA, multi-reviewer validation and cleanup; each invocation advances only one step. A separate research skill gathers external sources into a user-facing research report, not a persistent controller for OMH's own future strategy.

Primary pinned evidence: [README](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/README.md), [concepts](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/docs/concepts.md), [plugin manifest](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/plugin.yaml), [Ralph workflow](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-ralph/SKILL.md), [Autopilot workflow](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-autopilot/SKILL.md), [Hermes dependency boundary](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/docs/hermes-constraints.md).

## Operational model

The active Hermes parent and task children make model-dependent choices about implementation, evidence gaps, plan revision and acceptance; OMH's distributed skill instructions define their roles and the feedback progression. Plugin code persists, guards and transports those choices. A plan/file-specific lock is a real cross-session contention mechanism, but its callback/retry and conflict response are assembled through the OMH skill plus plugin, so the S2 claim is limited to `C`. The Ralph coordinator sees current task dependencies, retries, blocks and completion and chooses/updates whole-plan commitments; this is stronger than merely issuing a child task. Verification and multi-reviewer phases are ordinary production acceptance, not an alternative sporadic audit of operational claims. An initial user spec or approval defines the task but is not ultimate project identity governance.

## S1 — Operations

- State: A
- Function: implement and verify individual software-plan tasks using model-guided agents and actual project tools.
- Disturbance / variety regulated: uncertain implementation paths, changing repository files, build/test failures, unexpected tool results and acceptance feedback.
- Decisive decision or feedback right: choose what code/commands to use, revise an implementation after verifier feedback and produce task artifacts.
- Decision owner: Hermes parent/`executor` model agents invoked by first-party OMH `ralph`/`autopilot` skill modes; external Hermes supplies the model runtime, not the organizational task choice.
- Supporting / enforcement mechanisms: `delegate_task`, OMH role hooks, work-state persistence, planned acceptance criteria, evidence command execution and progress logs.
- Closure path: a plan task is delegated to an executor; source changes and tool feedback are returned; the separate verdict can cause targeted rework, task completion or a blocked state, changing subsequent operating action.
- Boundary reachability: README documents skill and optional plugin installation; `omh-ralph/SKILL.md` explicitly invokes a provider-backed delegated executor within that supported installed mode, while plugin `pre_llm_call` injects packaged executor role context.
- Why this is / is not agent-owned: the model selects implementation actions under task/role constraints; plugin code only stores and enforces the workflow.
- Evidence: [Ralph Steps 3–6](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-ralph/SKILL.md), [role injection hook](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/hooks/llm_hooks.py), [delegation boundary](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/docs/omh-delegate.md).
- Basis: explicit and structural.
- Confidence: high for supported skill mode, not actual task quality.
- Caveats: requires a separately installed Hermes runtime/model and user/caller re-invocation; no live provider-backed workflow was executed for this review.

## S2 — Coordination

- State: C
- Function: attenuate collisions among parallel task workers and between two live OMH sessions targeting the same plan.
- Disturbance / variety regulated: concurrent task agents writing overlapping files and separate workflow sessions racing on the same plan/state.
- Decisive decision or feedback right: determine which tasks can safely run in parallel and whether an invocation may proceed with a particular workflow instance.
- Decision owner: skill-following Hermes coordinator chooses independent task groups and responds to lock-denied feedback; deterministic OMH state tool implements the keyed lock and refuses conflicting holders. The full function requires explicit installed skill/plugin composition.
- Supporting / enforcement mechanisms: per-instance advisory locks in `omh_state`, key/holder records, Ralph and Autopilot acquisition/release discipline, dependency/file-footprint checks and cancellation.
- Closure path: before work, the skill asks the state tool to lock a project plan; a conflicting holder causes wait/cancel/other-plan feedback rather than two writers proceeding on the same plan. Within a run, the coordinator selects only independent tasks for parallel delegation and feeds results into later task choice.
- Boundary reachability: both installed `omh-ralph` and `omh-autopilot` explicitly call shipped `omh_state(action="lock")`, and the registered `state_tool.py` dispatches to lock acquire/release/check; no hypothetical third-party coordination plugin is necessary.
- Why this is / is not agent-owned: `C` records the explicitly composed agent decision plus state-based contention mechanism; fixed mutex implementation alone is not promoted to an autonomous S2 decision owner.
- Distinct S1 units: parallel executor child agents within Ralph; competing skill-driven workflow sessions for one plan form the second, narrower interference case.
- Inter-S1 disturbance: same-file overlap or simultaneous updates to the same `.omh` task/plan state.
- Attenuating coordination relation: dependence and file-footprint screening before parallel delegates, plus keyed plan/session lock and conflict response.
- Feedback into subsequent S1 behaviour: a denied lock pauses/reroutes a would-be session; only noninterfering workers receive parallel tasks, and their reports affect the coordinator's next eligible-task selection.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path addresses explicit competing writer/session interference, not mere message delivery or parent-to-child sequencing; the state lock is connected to the skill's alternate action on contention.
- Evidence: [Ralph lock and parallel selection](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-ralph/SKILL.md), [Autopilot contention response](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-autopilot/SKILL.md), [state tool](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/tools/state_tool.py), [state engine](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/omh_state.py).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: advisory rather than universally enforced across independent Hermes instances; plugin-free skills and arbitrary independent writers do not inherit this guarantee. Coordination within unrelated projects is not assessed.

## S3 — Inside-and-now control

- State: A
- Function: regulate current whole-workflow task commitments, retries, completion and failure handling across delegated workers.
- Disturbance / variety regulated: stuck plan dependencies, incomplete acceptance criteria, repeated identical errors, unfinished tasks, conflicting runtime-phase progress and tool/test failures.
- Decisive decision or feedback right: choose eligible tasks, batch or defer work, initiate corrective retries, mark tasks passed or blocked, and determine current phase progression under shared constraints.
- Decision owner: skill-following Hermes coordinating agent inside the supported Ralph/Autopilot mode; first-party state machinery tracks and enforces its choices.
- Supporting / enforcement mechanisms: `omh_state` plan/task records, prerequisite gate, dependency graph, max-iterations and three-strike limits, `omh_gather_evidence`, verification verdicts and cancellation.
- Closure path: coordinator reads whole-plan/task status, assigns eligible work, receives executor and evidence-based verifier outcomes, writes changed pass/block/retry status, and the next invocation uses this state to alter commitments and later dispatches.
- Boundary reachability: `omh-ralph` is a shipped installable skill with explicit Steps 1–8 and whole-plan state transitions; `omh-autopilot` repeatedly checks Ralph state and advances/presents blocked current work. The actor is reachable via the installed Hermes tool boundary.
- Why this is / is not agent-owned: choosing what whole-plan work is committed, retried or stopped depends on the coordinator's context-sensitive judgment, not solely on deterministic state-file writes or raw task delegation.
- Whole-system current view: active phase, plan/task queue, dependency status, retries, evidence verdicts, error fingerprints, cancellation/lock state and current invocation.
- Current-control decision scope: work allocation and acceptance across all current tasks in a project workflow, not a child agent's local tool choice or future identity decision.
- Evidence: [Ralph orchestration and recovery](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-ralph/SKILL.md), [Autopilot phase controller](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-autopilot/SKILL.md), [state engine](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/omh_state.py).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: the user/caller still launches each separate invocation. The system does not autonomously continue if nobody re-invokes it; current decisions within a reached invocation are the claim.

## S3* — Complementary audit

- State: —
- Function: no sufficiently distinct nonroutine complementary audit of ordinary execution claims established in the supported OMH work boundary.
- Disturbance / variety regulated: an executor or coordinator can misreport success, and normal tests may miss defects.
- Decisive decision or feedback right: verifier and reviewer roles issue PASS/FAIL or REQUEST_CHANGES in mandatory delivery/QA phases, but no separately controlled sporadic audit decision is established beyond that ordinary path.
- Decision owner: routine Hermes verifier/reviewer and same-workflow coordinator own acceptance, not a separately evidenced S3* audit function.
- Supporting / enforcement mechanisms: read-only verifier prompt, fresh command output, QA and parallel validation reviewers, research citation checks and plan criticism.
- Closure path: failed verifier/reviewer judgments lead to executor retry or a blocked state within the normal production pipeline; a distinct complementary audit escalation/alternative observation path is not shown.
- Why this is / is not agent-owned: a different model role and real fresh test output strengthen routine quality control but do not by themselves provide independent sporadic access outside the standard success-report path.
- Evidence: [Ralph Step 5 verification](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-ralph/SKILL.md), [Autopilot QA/validation](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-autopilot/SKILL.md), [verifier role](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/references/role-verifier.md), [evidence tool](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/tools/evidence_tool.py).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: an external independent auditor could inspect project artifacts, but that would be adjacent to rather than demonstrated inside this product mode.

### Absence scope

- Surfaces inspected: ordinary acceptance/verifier, code/security/architect reviewer roles, evidence gathering, delegated research citation verification, production-step feedback, plugin hooks and test fixtures.
- Plausible first-party paths checked: fresh independent command outputs, read-only subagent reviews, final architect review, optional review phases and `omh-deep-research` citation checks.
- Why no material first-party path remains: each identified check is embedded in a planned production or research-delivery phase and returns to that same workflow. No separately triggered, sufficiently independent complementary inspection of ordinary operational reality with a distinct supervisory corrective loop was established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental scanning and strategic capability adaptation of OMH itself established in the assessed project workflow.
- Disturbance / variety regulated: changing external tool/model capabilities, project environment and future requirements might require adaptation beyond the currently requested work.
- Decisive decision or feedback right: the shipped research skill can synthesize outside facts for a user's research or planning task, but no agent-owned mechanism determines OMH's future capability policy and returns such options into its own present operational configuration.
- Decision owner: project users define research/feature goals; current-task planners execute them. OMH maintainers' future roadmap is adjacent development, not in-boundary S4.
- Supporting / enforcement mechanisms: `omh-deep-research`, `omh-ralplan`, persistent plans/specs, task learnings forwarded to later executors and roadmap documents.
- Closure path: a topic-specific report or implementation plan can inform the next user task, but there is no established outside-and-then system self-adaptation judgment with a durable capability change owned by the runtime.
- Why this is / is not agent-owned: external research as an S1 deliverable, feedback on the present coding task and stored learnings are not automatically a future-oriented S4 conversation with present capability.
- Evidence: [deep research scope](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-deep-research/SKILL.md), [Ralplan purpose](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-ralplan/SKILL.md), [Autopilot phases](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-autopilot/SKILL.md).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: specialized user-authored strategic workflows could be composed on top of OMH; generic possibility is not a shipped S4 ownership path.

### Absence scope

- Surfaces inspected: research/synthesis, plan consensus, project spec interview, task learnings, plugin config, state persistence, roadmap and contributor development surfaces.
- Plausible first-party paths checked: web research, project-future planning requests, durable task learnings and skills/plugin version upgrades.
- Why no material first-party path remains: the identified loops produce user-requested artifacts or ordinary developer changes rather than autonomous/parent-owned prospective adaptation of the assessed operating system with a function-specific return into capability.

## S5 — Policy and identity

- State: —
- Function: no supported identity- or ultimate-policy dispute/decision path established for a deployed OMH workflow as distinct from normal task authorization.
- Disturbance / variety regulated: potential conflicts about what the multi-agent workflow ultimately exists to do and who may redefine its identity.
- Decisive decision or feedback right: users confirm requirements or approve risky plans, but no shipped ultimate identity-policy judgment is routed to a legitimate S5 owner and returned as governing operating policy.
- Decision owner: normal local user for specifications/cancellation and upstream project maintainers for product evolution; neither has a documented in-boundary S5 loop.
- Supporting / enforcement mechanisms: interview confirmation, Ralplan consensus, triage sign-off, command allowlists, plugin configuration and cancellation.
- Closure path: these mechanisms can govern an ordinary task transition; no distinct charter/purpose dispute → legitimate policy authority → binding decision → subsequent identity-governed operation path was established.
- Why this is / is not agent-owned: static skill purpose, safety allowlist and user sign-off cannot by themselves be equated with ultimate-policy ownership.
- Evidence: [deep interview user-confirmed scope](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-deep-interview/SKILL.md), [triage sign-off](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/skills/omh-triage/SKILL.md), [config](https://github.com/witt3rd/oh-my-hermes/blob/3b06e33ae67b202b342989b484f08143e65e250d/plugins/omh/omh_config.py).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: higher-recursion human governance may exist outside this one local workflow; it is not borrowed into this assessment.

### Absence scope

- Surfaces inspected: user interviews, plans/consensus, executor/verifier role boundaries, plugin configuration and permissions, local cancellation, triage human sign-off and contributor roadmap.
- Plausible first-party paths checked: owner confirmation of requirements, operator approval of backlog changes, role/allowlist constraints and developer release policy.
- Why no material first-party path remains: these paths decide ordinary work or code security bounds; none receives an identity-level problem and returns an authoritative ultimate-policy decision to the runtime.

## Distributed OSS parent arrangement

The upstream repo is an OSS skill/plugin package, not a shared operating instance across contributors. Its maintainers manage releases and conventions, but this does not show a legitimate S3/S4/S5 parent over independent users' local Hermes workflows. Users author specs and call/resume their own project workflows; no organization-scale parent authority is inferred.

## Self-hosted and non-human modes

OMH can be installed into a locally controlled Hermes instance and run with model/provider tools. The plugin is optional and some skills can be installed alone; S2 is explicitly scoped to the composed lock-enabled mode. External Hermes default concurrency and leaf-tool limits are documented dependencies. Re-invocation is required between workflow steps; no continuous non-human daemon or live autonomous quality assurance is claimed.

## Recursion

Children have separate roles and tool scopes but no established durable independent purpose, full metasystem, or autonomous identity. They are S1 operations in the parent project-workflow recursion, not automatically recursive viable systems. Different OMH projects may operate in parallel but are not one joined supersystem by repository co-location.

## Variety and escalation

Task state and error fingerprints attenuate repeated failure variety; execution/verifier results change retries and next task selection. Plan locks and file-boundary checks attenuate known inter-writer collisions. The user/caller receives `blocked`, `cancelled` or lock-denied states for intervention, and re-invocation is necessary for progress. A block signal is not automatically an algedonic S5 channel. Ordinary evidence and validation do not establish S3* independence; user approval alone does not establish S5.

## Evidence gaps

- Static pinned-source assessment only; no live Hermes model/provider/tool-execution roundtrip or measured project-quality outcome. The bundled pytest suite was not run because `pytest` is unavailable in the inspection Python environment.
- S2 `C` depends on the optional plugin plus the first-party skill following its plan-keyed locking/parallel-task instructions; no cross-host hard concurrency enforcement is claimed.
- S3 current regulation is bounded to one reached invocation and its persisted task workflow; full unattended multi-invocation completion depends on an external caller.
- No positive S3* is inferred from routine read-only verifier roles; a distinct audit deployment would require separate evidence.
