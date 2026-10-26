---
harness_id: setup-ai-core
project_name: setup-ai-core
repository: https://github.com/kartalbas/setup-ai-core
review_ref: 9c78c081d8d49745ef0566f850e6cc3f83677574
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

# setup-ai-core

## Review boundary

- System in focus: shipped `ai-core` multi-repository agent-harness installation, CLI, project rules/skills, and its **directly invoked model-backed `map` task** at the frozen revision. A team's entire external Claude/Codex/agy process fleet is not silently absorbed into this boundary.
- Purpose and identity: give multiple installed coding-agent hosts common repository knowledge, issue/worktree/release workflow, safeguarded Git operations, and reviewable project conventions.
- Relevant environment: project checkouts, manifests and code, GitHub/Forgejo/Plane trackers, release and test state, human owner, and separately installed coding-agent CLIs with credentials.
- Standard-distribution boundary: [`bin/ai-core`](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/ai-core), the [`map`](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/map.sh) model-backed operation, deterministic `bin/` and `lib/`, installed rules, and the `person-in-charge`/`helper` skills. External coding-agent runtimes/models are dependencies, not additional first-party agent owners.
- Credited operating / distribution surfaces: `ai-core map` calls a configured agent CLI with repository-reading tools, checks the answer, writes the map to the project harness, commits/pushes and reinjects it into the checkout. Source-defined prompt, selected model CLI and validation/return path constitute a narrow first-party S1 invocation.
- Adjacent first-party surfaces excluded from ownership: model-backed coordinator/worker/reviewer sessions *started by an external host agent following installed skill prose*, user team's repositories and workflows, development tests, CI, sample fixtures, maintainer organization and third-party tracker authority. Their full model reasoning or management closure is not imported.
- First-party modes considered: install/init; explicit `ai-core map [--all]` with Claude/Codex/agy; status/watch/phase-model/issue/landing CLI; installed coordinator and helper skills, including external-host phase sessions; GitHub and Forgejo tracker modes.
- Recursion level: one installed project-folder harness coordinating coding work in its checkouts; the map-generation job is a narrow operational cell. A composed host-coordinator-plus-workers organization would be a separately declared boundary.
- Reviewed revision: `9c78c081d8d49745ef0566f850e6cc3f83677574`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/README.md) describes a layer copied into each checkout: common rules, maps, tracker integration, status, team modes and release gates. Most Bash/Node commands do deterministic state reconciliation and API/Git operations. The [coordinator skill](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/SKILL.md) directs a **separately started host session** to package issues, allocate fresh plan/build/review sessions, arbitrate overlapping file/contracts, control land/release sequence and seek product-owner decisions. Its [review brief](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/briefs/review.md) tells an external reviewer model to inspect diffs and tests independently of the builder's conversation. Those are meaningful compositional instructions but not themselves a first-party launcher/owner of a durable multi-agent decision loop.

A narrower executable exception exists: [bin/map.sh](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/map.sh) constructs a repository-inspection task and **directly invokes** `claude -p` with `Read,Glob,Grep`, `codex exec -s read-only`, or `agy --print`. The configured coding agent decides which source evidence to read and how to synthesize the five-section map; `map.sh` enforces output shape and length, preserves the human-authored section, updates the project harness and reinjects the map into checkouts. [First-party planted tests](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/tests/sections/08-harness.sh) exercise that invocation with fake CLIs. This is an intentional supported model-operated task, unlike mere prompt deployment.

## Operational model and admission decision

Operator invokes `ai-core map` → first-party CLI selects an external agent executable and hands it bounded source-reading autonomy → model inspects repository evidence and decides map content → first-party validator accepts/rejects the result → accepted map is committed and delivered to installed agent contexts. Separately, when a human starts a project coordinator in their existing agent host, *that external host session* interprets the first-party skill and launches/oversees worker phases; deterministic `ai-core` commands support it. The two paths must not be conflated.

**Proposed canonical disposition: included**, vector **`A — — — — —`**. The affirmative S1 is scoped to model-backed repository-map production, not a claim that setup-ai-core owns the broader coding-agent fleet or that its rulebook becomes autonomous S2–S5. No model-quality or provider-execution measurement was performed.

## S1 — Operations

- State: A
- Function: produce a repository-specific, evidence-grounded operational map for coding agents, from actual code/manifests and user repository constraints.
- Disturbance / variety regulated: unfamiliar languages/build commands, changing source layout, divergent repositories and incomplete generic harness maps.
- Decisive decision or feedback right: choose which code/manifests to inspect and how to summarize the shape/build/extension points into an agent-readable map.
- Decision owner: configured model-backed `claude`/`codex`/`agy` task **invoked directly by first-party `map.sh`**; operator selects tool/model, not content. First-party parser owns deterministic acceptance rules.
- Supporting / enforcement mechanisms: fixed prompt/heading contract, read-only tools, 80-line limit, human-section preservation, malformed-output refusal, map provenance and project-harness commit/push/install.
- Closure path: source evidence → model's read-and-synthesize task → checked map → project harness and agent instructions → subsequent work consumes the map; malformed output is withheld for correction.
- Boundary reachability: `bin/ai-core` dispatches `map` to shipped `bin/map.sh`; its `run_tool` selects the actual installed Claude/Codex/agy CLI and captures the source-reading model output. Standard `init` then deploys the resulting map. No unpublished hook or development-only script is needed.
- Why this is / is not agent-owned: replacing the model task with only `map.sh` leaves no contentful source-specific synthesis. Conversely, an externally initiated coordinator/worker coding session is not needed to execute this shipped map operation.
- Evidence: [map.sh](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/map.sh), [map tests](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/tests/sections/08-harness.sh), [README §4.7](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/README.md).
- Basis: first-party executable model-calling path and bounded structural evidence.
- Confidence: medium-high for source-wired operation; model/provider runtime quality untested.
- Caveats: this is a narrow one-task S1, not an unattended long-running software-development agent; `map` requires a configured external agent executable, and the actual reasoning/tool internals are not first-party.

## S2 — Coordination

- State: —
- Function: no established first-party S2 ownership loop across multiple **first-party** autonomous S1 operating units.
- Disturbance / variety regulated: concurrent external workers may overwrite files or violate shared contracts; coordinator skill asks the host agent to serialize overlapping packages.
- Decisive decision or feedback right: inspect collisions, revise package/file ownership, and send a changed operating arrangement back to distinct S1s.
- Decision owner: external host coordinator interpreting skill prose; `ai-core` Git locks, worktrees, issue board and phase selectors enforce selected ordering.
- Supporting / enforcement mechanisms: [coordinator skill](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/SKILL.md), [`tool-order`](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/lib/tool-order.sh), tracker state and push/landing locks.
- Closure path: an external supervisor can route conflicting worker packages apart, but the assessed executable's S1 map job has no independent peer; that external coordination loop is not directly launched/owned by this first-party runtime.
- Why this is / is not agent-owned: the instruction to serialize overlapping work is specific, yet the agent making the organizational compromise is supplied and started by the outside host; deterministic locks do not confer that autonomy.
- Evidence: [person-in-charge](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/SKILL.md), [integration command](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/integrate-issue.sh).
- Basis: bounded boundary-relative negative.
- Confidence: medium-high.
- Caveats: the composed host-coordinator/worker organization likely has real inter-agent interference control; it needs an explicitly wider ownership boundary.

### Absence scope

- Surfaces inspected: coordinator overlap/phase contract, map --all, worktrees, locks, tracker and tool-order.
- Plausible first-party paths checked: several map jobs as S1 divisions, phase workers as owned S1s, package conflict/lock arbitration as autonomous S2.
- Why no material first-party path remains: maps run as sequential jobs; the genuine multi-worker discretionary response runs in an external host, while first-party coordination tools encode or enforce prescribed choices.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous/constructor/parent current-control loop over a portfolio of credited S1 units.
- Disturbance / variety regulated: quota use, issue state, branch drift, blocked work, releases, failed checks and worker liveness.
- Decisive decision or feedback right: reprioritize, reallocate, intervene and revise current commitments using a whole-work view.
- Decision owner: externally started `person-in-charge` session and product owner; status/watch/phase-model/landing scripts supply constrained state and enforcement.
- Supporting / enforcement mechanisms: [`status`](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/status.sh), [`watch`](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/watch.sh), [`phase-model`](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/phase-model.sh), coordinator skill.
- Closure path: dashboard/health/tool selection information becomes operational intervention only after an external coordinator chooses and acts; the narrow first-party map task lacks whole-operational-unit regulation.
- Why this is / is not agent-owned: status displays, watchdog triggers, hard gates and predefined quota tables do not themselves own the whole-current discretion.
- Evidence: [coordinator skill](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/SKILL.md), [status.sh](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/status.sh).
- Basis: bounded first-party ownership negative.
- Confidence: medium.
- Caveats: `ai-core` provides rich *support* for human/agent project control; grading that composition would require its own declared S1 divisions and parent arrangement.

### Absence scope

- Surfaces inspected: status/watch, priority/phase-model, board, issue integration, landing and coordinator workflow.
- Plausible first-party paths checked: watchdog as S3 intervention, phase-model as resource allocation, coordinator instructions as shipped autonomous management, parent release decisions as S3(P).
- Why no material first-party path remains: the CLI routes/enforces predefined policy and displays facts; external coordinator selects the portfolio action, and owner approvals chiefly govern single projects/releases rather than a closed first-party multi-S1 current-control mode.

## S3* — Complementary audit

- State: —
- Function: no independently owned first-party complementary audit outside standard externally hosted review/QA.
- Disturbance / variety regulated: model builder could miss a faulty edge case, weaken tests or claim work is complete when code differs.
- Decisive decision or feedback right: independently question operational reality from raw sources and return a corrective finding to whole-system control.
- Decision owner: separately started external reviewer-model session, with source-defined [review brief](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/briefs/review.md); routine test/CI/landing checks are deterministic.
- Supporting / enforcement mechanisms: different-model selection, no builder conversation, raw diffs/tests/contracts, GO/NO/REPAIRED verdict and downstream integration gates.
- Closure path: an external coordinator can receive a different-model review and order rework; `ai-core` itself does not instantiate that independent reviewer as a first-party audit lane and the shipped review is the ordinary mandatory phase.
- Why this is / is not agent-owned: complementary evidence is plausible, but independent reviewer ownership belongs to the outside host; a normal review stage is not automatically a systemic S3* audit.
- Evidence: [review brief](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/briefs/review.md), [phase-model](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/phase-model.sh), [GitHub CI](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/.github/workflows/check.yml).
- Basis: bounded structural negative.
- Confidence: medium.
- Caveats: an actual wider host deployment could establish more independent audit reachability than the source-only standard installation proves.

### Absence scope

- Surfaces inspected: reviewer brief, model separation, test and CI paths, status review tally, live UI-test phase and landing gates.
- Plausible first-party paths checked: independent different-model review, planted-case raw diff challenge, production UI checks and push gate as an S3* channel.
- Why no material first-party path remains: an external host creates/runs reviewers; mandatory routine pipeline tests and different-model review do not form a separately first-party-owned, returned complementary audit system at this boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established prospective external scanning, option testing and adaptation return loop.
- Disturbance / variety regulated: evolving repositories, agents and tool capabilities may require maps, rules, model tables and operating practices to change.
- Decisive decision or feedback right: choose future organizational capability changes from sensed external distinctions.
- Decision owner: operator/project maintainers or external coding coordinator; no first-party prospective strategy agent.
- Supporting / enforcement mechanisms: generated code maps, issue keeper, roadmap, skill updates, model table and capability/doctor checks.
- Closure path: maps update current repository knowledge and keeper files current defects; neither evaluates future external options and feeds a strategic adaptation decision into present S3.
- Why this is / is not agent-owned: documentation refresh, dependency probing and backlog planning are current-work tasks, not future-facing S4 simply by changing over time.
- Evidence: [map.sh](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/bin/map.sh), [keeper brief](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/briefs/keeper.md), [README](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/README.md).
- Basis: bounded negative.
- Confidence: high.
- Caveats: a user organization may add a future-capability strategy process beyond these tools.

### Absence scope

- Surfaces inspected: `map`, issue keeper, model selection, doctor/update, roadmap and coordinator phases.
- Plausible first-party paths checked: updated maps as learning, model selection as strategic option evaluation, issue keeper as prospective discovery.
- Why no material first-party path remains: these support current repository work or operator-maintained configuration without a closed outside-and-then S4–S3 dialogue.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy-level decision-and-return loop at the assessed recursion.
- Disturbance / variety regulated: project scope, risky publishing, interface naming, permissions and other decisions reserved for the product owner.
- Decisive decision or feedback right: legitimate identity and ultimate-policy adjudication, with a durable return that governs the harness organization.
- Decision owner: human product owner makes named scope/publishing choices, while coding agent and CLI carry out routine tasks under static rules.
- Supporting / enforcement mechanisms: [`70-working-with-the-product-owner`](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/rules/70-working-with-the-product-owner.md), permissions/auto-mode, pre-push, review and release gates.
- Closure path: the agent asks before a release/new interface/issue, then resumes the affected task; no separately established identity/ultimate-policy issue, legitimate S5 adjudication and returned durable organization-wide rule path is evidenced.
- Why this is / is not agent-owned: owner task approval and static policy do not establish VSM S5 simply because they constrain the agent.
- Evidence: [owner rule](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/rules/70-working-with-the-product-owner.md), [skill](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/skills/person-in-charge/SKILL.md), [auto-mode table](https://github.com/kartalbas/setup-ai-core/blob/9c78c081d8d49745ef0566f850e6cc3f83677574/auto-mode.tsv).
- Basis: bounded negative, including parent-mode review.
- Confidence: medium.
- Caveats: the owner may exercise authentic S5 over their own separate company/project; ordinary approvals are insufficient to credit that higher recursion to this installed harness.

### Absence scope

- Surfaces inspected: product-owner rules, permissions, start authorizations, scope/new-issue decisions, pre-push and release gates.
- Plausible first-party paths checked: owner approval as S5(P), changing auto-mode as identity policy, model coordinator as autonomous policy setter.
- Why no material first-party path remains: reachable owner choices concern tasks, project scope and ordinary publication; no specific ultimate identity tension and returned S5 governance loop is supplied.

## Distributed OSS parent arrangement

Different adopters install this harness into independent projects. Shared templates and a public upstream repository do not form a single distributed parent with control of every adopter's agent sessions or identities.

## Self-hosted and non-human modes

The first-party map command can run against configured non-human coding CLIs, while the standard coordinator skill explicitly requires an external host and an owner's kickoff. Running several installed agent processes does not transfer their entire organization into `ai-core` itself.

## Recursion

An independent phase worker can be an S1 in a larger adopting organization, provided it has a real outcome/environment/local discretion and parent coordination. That recursive cell is externally instantiated; a phase name or issue label alone is not a viable sub-organization of this shipped program.

## Variety and escalation

Maps transduce source complexity into compact agent context. Skills split and route coding variety, with deterministic CLI gates reducing drift and unsafe landing. Watch/status/quota errors reach an external supervisor; neither a red dashboard nor a reviewer GO/NO label automatically inherits S3, S3*, S4 or S5 authority.

## Evidence gaps

Pinned source and its planted tests establish the `map` agent invocation and deterministic acceptance path, not model correctness or measured coding-agent autonomy. No live Claude/Codex/agy/model-provider/Browser test was executed. The entire native no-network `bash tests/check.sh` suite was started; its result is reported separately in the batch receipt when it finishes. No source-backed direct first-party launcher/management feedback loop for the external project coordinator and all its worker phases was identified in the inspected shipped code; a broader composed deployment could warrant a different assessment.
