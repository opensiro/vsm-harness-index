---
harness_id: revfactory-harness
project_name: Revfactory Harness
repository: https://github.com/revfactory/harness
review_ref: 92d9f1b29e7af81acebf51a9fcd1832e739a1414
reviewed_at: 2026-10-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Revfactory Harness

## Review boundary

- System in focus: The **first-party Claude Code skill-based harness-construction/adaptation cell** distributed by `revfactory/harness` v2: `skills/harness/SKILL.md` for designing and publishing a domain-specific agent/team/skill orchestration and `skills/evolve/SKILL.md` for improving the resulting harness from actual use feedback. The system performs project-local construction/maintenance, not an always-running autonomous execution engine or an arbitrary generated target team's internal management.
- Purpose and identity: Given a concrete user's project/domain and constraints, create a working reusable agent/team/skill operating configuration and, when `evolve` is invoked later, use execution/user feedback to make supported next-run capability changes.
- Relevant environment: Existing project files and Git history, operator requirements, target operating shape and test traces, user feedback, produced `.claude/agents/`, `.claude/skills/`, `CLAUDE.md` with change history, and installed Claude Code model/tool substrate.
- Standard-distribution boundary: Bundled v2 `skills/harness/SKILL.md`, `skills/evolve/SKILL.md`, `skills/harness/references/*`, `.claude-plugin` marketplace and plugin metadata and documented installed Claude Code mode. **External Claude Code model, proprietary tool runtime, arbitrary plugin host and created downstream agent organizations** are not itself first-party; the shipped skills bind the model's decision procedure to concrete project-file operations in the documented supported mode.
- Credited operating / distribution surfaces: [README.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/README.md#L1), [docs/quickstart.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/docs/quickstart.md#L1), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L1), [skills/harness/references/execution-modes.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/references/execution-modes.md#L1), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L1), [.claude-plugin/plugin.json](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/.claude-plugin/plugin.json#L1).
- Adjacent first-party surfaces excluded from ownership: Repository maintainers and git contributor governance, author-run v1 evaluation reports, architecture examples for generated third-party teams, generated user project's own live S2/S3/S3*/S4/S5 not yet instantiated and observed, Claude Code's provider/resource/permission policy, and the product/repository's unrelated release workflow.
- First-party operating / deployment modes considered: Installed plugin `/plugin install harness@harness-marketplace` or globally copied first-party skills, invoked `harness` new-build/extension/audit/migration phases 0–7 (incl. supported workflow/persistent/subagent mode choices and permissions) and **separately invoked** `harness:evolve` feedback-based adjustment phases 1–5. The two skills may operate serially on the same target project; no claim that `evolve` runs automatically without invocation or that generated agents execute during a pure source review.
- Recursion level: One skill-guided project harness builder/maintainer operating unit, with an adaptation function over its created target project artifacts; distinguish that construction recursion from the later target team's operational recursion. Nested generated agents and possible Claude Code tools are externally hosted or future configurations, not automatically viable S1 departments within the builder system.
- Reviewed revision: `92d9f1b29e7af81acebf51a9fcd1832e739a1414`, public repo ID 1193082155, clean first-party Git tree `0798e41621db36cb3c9b123426b84c82728befcc`, frozen in [batch #1732](https://github.com/opensiro/vsm-harness-index/issues/1732).
- Observation date: 2026-10-19, active Profile 0.2.4 and Methodology 0.3.7 (immutable generation and current semantic pair).

## Repository architecture

The repository supplies prompt/skill-controlled functionality, not a standalone server. The marketplace exposes a Claude Code plugin whose `harness` skill instructs the model to first audit current `.claude/agents/`, `.claude/skills/` and `CLAUDE.md`, analyze task control-flow shape, choose among workflow, persistent-agent collaboration and one-shot delegation, design expert agents and per-agent skills, write the orchestrator and `CLAUDE.md` trigger, and verify the output. `docs/quickstart.md` gives a concrete `claude "build a harness for ..."` route that produces these on-disk files. The Claude Code host/model performs reasoning and file-tool calls; the **first-party skill** makes the goal-specific construction loop reachable in the documented installed operating mode. This is not a claim to ship the external Claude runtime itself. [README.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/README.md#L15), [docs/quickstart.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/docs/quickstart.md#L1), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L7), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L35).

`harness` is a constructor, not the target team's persistent executive. Its mode selector chooses **deterministic workflow** when the work graph can be explicitly encoded, **persistent named agents with `SendMessage` and shared tasks** when ongoing context/debate matters, and **one-shot subagents** for independent work. Quality patterns include adversarial review, judge panels and regression checks, but these are instructions/templates for generated target-system workflows and routine construction-phase QA. They do not alone establish first-party S2 disturbance-sensitive regulation or S3* independent audit in the builder's own current operation. [skills/harness/references/execution-modes.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/references/execution-modes.md#L1), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L53).

`evolve` is a distinct shipped skill with an **explicit future-capability feedback loop**: read the existing target harness files, Git history and actual workspace outputs, gather user feedback (or notice repeated fixes, agent failures and trigger misses), generalize adaptation options, modify an existing agent skill, role, orchestration or trigger one change at a time, run structure/trigger validation, and record rationale in the project's `CLAUDE.md` history. The return is not a mere report or memory entry: it **changes the same on-disk agent instructions and orchestrator that the next supported Claude Code invocation reads and executes**. Major rearchitecture is routed back to `harness`; contradicting prior edits invokes explicit user consent. This is opt-in user-triggered adaptation, **not** an always-on independently scheduled environmental scanner, nor identity/policy authority. [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L1), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L16), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L41), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L57), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L75).

## Operational model

Primary transformation: model follows shipped project-specific constructor skill → compares task/environment to current project artifacts → selects architecture/roles/skills and writes/validates concrete files → reusable configured harness, optionally run. Adaptation: later model follows `evolve` when invoked → analyzes external user/operation feedback against current configuration → chooses generalizable prospective changes and writes/validates the same files → future operating capability changes. **There is no first-party resident orchestration manager/agent fleet implied** merely because the constructed configuration can later launch teams through the external Claude host.


## S1 — Operations

- State: A
- Function: Perform goal-conditioned, first-party skill-directed construction and repair of a domain-specific agent harness's project files.
- Disturbance / variety regulated: Unknown project's domain/tasks, preexisting skill/agent inventory, changing work graph and coordination mode suitability, model/quality requirements, missing trigger/role artifacts and user-supplied constraints.
- Decisive decision or feedback right: The Claude Code agent executing the shipped `harness` skill decides among control-flow modes, project-specific expert roles, generated skills, schemas and orchestration layout in response to inspected inputs; it writes and checks those actual project files.
- Decision owner: Skill-guided model-based operating actor in supported Claude Code invocation; the external Claude runtime supplies cognition and tools but first-party skill links those discretionary choices to construction outputs.
- Supporting / enforcement mechanisms: Skill steps, templates, mode-selection reference, target `.claude` file paths, generated metadata/trigger, routine QA rules, user goal and installation mechanism.
- Closure path: User requests project harness → agent inspects existing project files and relevant constraints → autonomously chooses generated team/mode/skill implementation → writes the agent/skill/orchestrator files → validates files/triggers and reports construction to user; follow-up can revise them.
- Boundary reachability: `docs/quickstart.md` documents installation, `claude "build a harness ..."`, expected concrete project files and test route. The plugin's `harness` skill is the operative first-party source of those reachable decisions, not a standalone backend.
- Why this is / is not agent-owned: Remove the skill-guided model and no dynamic domain-to-team architecture/skill configuration can be selected or written by the static Markdown/templates alone. Human-supplied project request scopes the task rather than making each design decision.
- Evidence: [docs/quickstart.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/docs/quickstart.md#L1), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L8), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L42), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L66), [README.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/README.md#L33).
- Basis: Explicit first-party shipped skill work instructions with documented installed model/file-change entry and output files.
- Confidence: Medium-high structural capability; no model inference or downstream actual project build executed during assessment.
- Caveats: The model and file tools are from the user's installed Claude Code; the skill does not guarantee successful execution independent of that host or budget.


## S2 — Coordination

- State: —
- Function: No first-party **builder-level** interference-specific stabilization of two viable simultaneous operating S1 units with changed behavior feedback is established.
- Disturbance / variety regulated: Generated target teams may later experience shared-file overwrite and role conflict; generated workflow mode may propose frozen handoff artifacts, but these are future target configurations, not actual competing S1 departments of the first-party constructor.
- Decisive decision or feedback right: The builder model **chooses a future team architecture**; the selected future workflow/persistent agents and shared tasks are not live first-party S2 regulation of builder-owned operating units.
- Decision owner: Model for constructor task choice; deterministic/external Claude tools for future workflow execution.
- Supporting / enforcement mechanisms: `pipeline`, `parallel`, `SendMessage`, task lists, artifact-freeze instructions and adversarial review recipes provided as generated-configuration templates.
- Closure path: Project-analysis requirements → model specifies future coordination configuration → writes target orchestrator file. The documented construction process does not run distinct competing builder S1 units, sense their actual mutual interference, choose an adjustment and feed a stabilized outcome into those units.
- Why this is / is not agent-owned: Constructor discretion is S1 design work here, not already exercised S2 regulation; the phrase "agent team" and syntactic `SendMessage` template are insufficient evidence of an inter-S1 regulator.
- Evidence: [skills/harness/references/execution-modes.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/references/execution-modes.md#L16), [skills/harness/references/execution-modes.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/references/execution-modes.md#L48), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L50), [README.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/README.md#L35).
- Basis: Bounded negative at explicit constructor recursion after testing targeted generated-team paths.
- Confidence: Medium-high.
- Caveats: Independently deployed generated target teams may have S2; they require their own separate source/runtime boundary and assessment.

### Absence scope

- Surfaces inspected: Constructor skill phase 2 patterns, execution-modes workflow/persistent/subagent references, generated artifact handoff guidance, build/verify phases.
- Plausible first-party paths checked: Potential shared outputs across generated agents, collaborative message loops, workflow gates and target artifact freeze.
- Why no material first-party path remains: These are generated/downstream architecture templates rather than first-party feedback regulation of an evidenced conflict between currently viable S1 units at the builder recursion.


## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current manager holding discretionary live resource, priority and accountability decisions across multiple operating units of the constructor system.
- Disturbance / variety regulated: Constructor's task complexity, budget guidance, execution mode suitability and quality errors require local project build control; they are not ongoing contested commitments of a current organizational portfolio.
- Decisive decision or feedback right: Builder model chooses current design/work plan and verification; external user/operator grants use of costly `Workflow`; no distinct S3 holds present portfolio-level authority across multiple viable operating builder cells.
- Decision owner: Model for S1 project design, operator for permission/limits, host for deterministic tool constraints.
- Supporting / enforcement mechanisms: Phases 0–7, cost/model tier heuristics, predefined orchestration mode, QA checks, tool permission constraints.
- Closure path: Inadequate generated file or user restriction → model revises local build, permissions control chosen tool use, not whole-current executive negotiation and cross-unit operating-priority feedback.
- Why this is / is not agent-owned: Model controls current project artifacts as primary construction work, not a separate organizational inside-and-now executive function; a permission gate is enforcement.
- Evidence: [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L12), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L53), [skills/harness/references/execution-modes.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/references/execution-modes.md#L30), [docs/quickstart.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/docs/quickstart.md#L15).
- Basis: Bounded negative after role/mode/approval and build quality verification inspection.
- Confidence: Medium-high.
- Caveats: The surrounding human development team and a target generated team's eventual S3 are not within this tested first-party builder boundary.

### Absence scope

- Surfaces inspected: Constructor phases 0–7, mode selection, file verification, user tool consent, QA and budget guidance.
- Plausible first-party paths checked: Design-time resource/model tier assignment, task planning, project assessment and local correction.
- Why no material first-party path remains: There is no separately operating current portfolio of autonomous builder S1s and no shipped whole-current mandate/decisive resource return beyond a single S1 constructor task.


## S3* — Complementary audit

- State: —
- Function: No independently sourced complementary reality audit of an S3 current executive's reports with distinct corrective judgment/return is wired into the constructor's own operation.
- Disturbance / variety regulated: Generated-skill formatting, trigger mismatches, agent-role conflicts and QA omissions can be checked, but these are ordinary construction acceptance/repair duties rather than an independent assessment of an S3 claim.
- Decisive decision or feedback right: The builder model runs mandatory QA and may generate a future `critic` or adversarial `Workflow`, but no independently mandated S3* auditor is shown with alternative evidence and corrective control over the current constructor organization.
- Decision owner: Same builder/revision model and routine host validation, not a separate first-party audit authority.
- Supporting / enforcement mechanisms: QA reference, with/without-skill A/B test recommendations, producer-reviewer team patterns, completeness critics, skill frontmatter and trigger checks.
- Closure path: Generated output → routine skill/QA inspection → ordinary correction of builder output; optional generated target critic is a future separate deployment, not a current independent audit feedback path to S3.
- Why this is / is not agent-owned: More than one proposed critic agent is an architecture choice, not proof that a distinct first-party complementary audit witness is actually run with independent operational access.
- Evidence: [README.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/README.md#L37), [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L72), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L61), [skills/harness/references/execution-modes.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/references/execution-modes.md#L17).
- Basis: Bounded negative after inspecting QA, verification, potential external agents and feedback.
- Confidence: Medium-high.
- Caveats: User-run independent audits or deployed generated multi-agent QA are adjacent systems and could change the analysis at another recursion.

### Absence scope

- Surfaces inspected: Constructor QA/verification phases, quality patterns, documented optional adversarial/judge workflows, evolve regression/trigger tests.
- Plausible first-party paths checked: Proposed independent critics, routine code/output checks, A/B tests and history-based discrepancy reviews.
- Why no material first-party path remains: Source does not show an independently mandated corrective auditor of the current builder S3 reality with additional operational access and returned governance decision; the noted checks are local build tests or future generated templates.


## S4 — Outside-and-then intelligence

- State: A
- External distinction: A user reports unexpected quality/behavior, repeated correction requests, failed agent retries, missing skill triggers, or user overrides of the orchestrator; `evolve` also inspects Git and actual `_workspace/` execution artifacts to distinguish new operating reality from planned design. These are external user and operating-environment signals, not just internal chain-of-thought or stored prompts.
- Future / prospective distinction: The next invocation needs a revised instruction/agent role/trigger/workflow to prevent recurrence; the skill compares the original harness with its observed current version and identifies pattern-level improvement rather than reacting once to the same run.
- Adaptation option generated: The skill-guided model maps observations to candidate changes (skill quality rule, agent role, orchestrator sequence, trigger description, token-policy adjustment), generalizes the feedback, selects and edits one at a time with reason, or routes major redesign to `harness`; user confirms conflicting revisions.
- Path back into current capability / S3: It first inspects **current** `.claude` agents, skills, CLAUDE.md change history and execution traces; then persists validated changes into those **same current operational artifacts**. The next project run reads the edited skills/orchestrator, closing two-way feedback from present operating configuration → future distinction → changed present capability. This is a functional inside-and-now capability interface, **not** evidence of a separately autonomous S3 owner.
- Function: Reassess **future suitability** of existing user-project agent, skill and orchestration capabilities against changing user expectations and evidence of actual operating failures, choose generalizable improvements, and return them into subsequent harness execution.
- Disturbance / variety regulated: Changing task requirements, recurring user correction patterns, agent output quality defects, failed workflow/trigger activation, resource inefficiency and v1-to-v2 compatibility drift.
- Decisive decision or feedback right: Once `evolve` is invoked, the skill-guided model reads current harness Git/file state and external user feedback or observed execution traces, classifies the mismatch, develops a generalizable adaptation (skill rules, agent roles, orchestrator or trigger), chooses and **edits the target files** one change at a time; it validates and records the rationale for future use. This is beyond an internal task plan or a memory summary.
- Decision owner: Model-backed `harness:evolve` actor for ordinary prospective adjustment within bounded authorizations; the user provides the trigger/feedback and is asked to approve contradictory reversals; major structural redesign is routed to `harness`, not silently taken by `evolve`.
- Supporting / enforcement mechanisms: Git delta review, `_workspace` trace inspection, feedback prompts, classification table, `CLAUDE.md` persistent history, trigger/frontmatter checks and one-at-a-time regression guard.
- Closure path: Existing target operating configuration/history + actual user/execution feedback → source-guided option/generalization/choice → project-local agent/skill/orchestrator edit → validation and change history → next installed Claude Code invocation reads the **changed** files, altering its future working capacity. `harness` inventory/build and current project artifacts provide the current-capability side; `evolve` proposes and returns prospective modifications to that same operating configuration.
- Boundary reachability: Separate bundled `skills/evolve/SKILL.md` is installed with the main plugin and documented `"evolve the harness with this feedback"` / `"하네스 회고해줘"` invocation in README/quickstart; Phase 3 explicitly requires applying agent/skill/orchestrator changes and Phase 4 validation/history. The closure is supported by first-party shipped mode, not a repository developer's proposed future feature.
- Why this is / is not agent-owned: Without the model's interpretation/generalization, Git/log scanning and static Markdown cannot pick appropriate future changes nor write semantic refinements; operator feedback triggers and bounds but does not routinely decide each adaptation. Fixed validators enforce the chosen edit without owning future strategy.
- Evidence: [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L1), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L12), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L19), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L33), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L47), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L59), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L74), [docs/quickstart.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/docs/quickstart.md#L57), [README.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/README.md#L44).
- Basis: Explicit first-party mode with external/user-feedback sensing, future-capability option selection and artifact write/validation closure.
- Confidence: Medium-high for structural user-invoked agent-owned future adaptation; **no actual live evolve run** was executed in this review.
- Caveats: This is **on-demand** S4 (not continuous background environment scanning). Major redesign and contradictory revision require routing/parent consent, but they do not establish a separate first-party S4 parent-governed mode without a corresponding legitimate decision-and-return trace; published state is `A`, not `A(P)`. No claim that every change measurably improves external task performance without empirical evaluation.


## S5 — Policy and identity

- State: —
- Function: No first-party legitimate ultimate-purpose/organizational identity arbitration and binding policy return to the harness system is demonstrated.
- Disturbance / variety regulated: User sets domain/goal and whether to incur large multi-agent cost; conflicting requested changes can require consent. These are project configuration and revision safety questions, not constitutional mission/identity decisions.
- Decisive decision or feedback right: User/developer supplies the project's purpose and authorizes tool/Workflow use. Builder model structures the team and `evolve` proposes scoped improvements, but neither is granted power to determine enduring ultimate project policy or resolve genuine identity conflict through a legitimate parent governance channel.
- Decision owner: External user/host for mission, permissions and ultimate legitimacy; model for subordinate design/adaptation decisions.
- Supporting / enforcement mechanisms: Static phase/mode constraints, approval/consent on conflicting revisions, generated `CLAUDE.md` trigger/history, host permissions and budget directives.
- Closure path: User-specified task/permission → model design/edit under existing limits; no packaged identity-level matter intake → legitimate authority decision → changed enduring governing purpose through an S5 return.
- Why this is / is not agent-owned: Being allowed to rewrite a skill in a user project is not the mandate to decide the team's institutional ultimate purpose; ordinary permission for `Workflow` does not create S5.
- Evidence: [skills/harness/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/SKILL.md#L9), [skills/harness/references/execution-modes.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/harness/references/execution-modes.md#L36), [skills/evolve/SKILL.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/skills/evolve/SKILL.md#L54), [README.md](https://github.com/revfactory/harness/blob/92d9f1b29e7af81acebf51a9fcd1832e739a1414/README.md#L44).
- Basis: Source-bounded negative after inspecting approval and policy-adjacent paths.
- Confidence: Medium-high.
- Caveats: The host organization's real parent authority remains outside this first-party skill's own governance.

### Absence scope

- Surfaces inspected: Constructor skill approval/goal/mode/scale conditions, evolve contradictory-change confirmation, persisted project CLAUDE.md instructions/history.
- Plausible first-party paths checked: Human Workflow consent, goal/task selection, change-history reversion, agent role/model assignment and prompt-policy text.
- Why no material first-party path remains: No first-party identity- or ultimate-policy-level matter is presented to a legitimate constitutional owner and returned as binding durable governance of future operation; the documented gates concern ordinary task/tool/change permissions.


## Recursion

At this boundary the single **constructor/maintainer** is S1. Its `evolve` process provides positive source-grounded future adaptation S4 to the **same project's current operating artifacts**. These can coexist without proving an autonomous S3 or S5. The **generated** customer project may later contain separate viable agents, S2 coordination and S3/S3* management; its actual source and runtime would require a separate assessment, rather than importing those functions via documentation templates.

## Variety and escalation

The builder attenuates the project's design variety by mode selection, skills and quality patterns; `evolve` amplifies adaptability when new feedback arrives. Routine architecture/QA corrections remain in S1. Major proposed changes route to `harness` and conflict reversals require user confirmation; those are bounded approval/skill-routing, not a demonstrated S5 algedonic constitutional path.

## Evidence gaps

- The frozen upstream is **documentation/skill-source** packaging. No Claude Code API endpoint, third-party model invocation or generated project was executed here. Source assessment judges supported first-party operating paths, not observed agent success/reproducibility.
- The plugin relies on separately installed/proprietary Claude Code and its available built-in tools. That host is not first-party `revfactory/harness`; future changes to Claude tools may affect successful operation. Source-grounded claims remain limited to documented installed mode.
- S4 is credited only in the **opt-in `evolve` operating mode** with actual feedback, selected semantic edits and return into next-run project configuration; it is not claimed for constructor-only invocations and not a continuous autonomous service. The evidence distinguishes effect on subsequent capability from measured improvement to task quality.
- No first-party distributed current-control/legitimate parent or independently run corrective audit is demonstrated at this constructor recursion.
- Proposed file `status: proposed` is noncanonical until separate exact-head GitHub CI and later catalog/admission transaction.
