---
harness_id: atlas-ade
project_name: Atlas ADE
repository: https://github.com/The-Anthropocene/ade
review_ref: b719450d92b86e546b0bd8b8ddc4d66d050e0064
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: C(P)
---

# Atlas ADE

## Review boundary

- System in focus: One installed Atlas ADE project and its card board, live lanes, review and governance surfaces.
- Purpose and identity: Translate scoped project cards into tested, integrated work using separately commissioned builder and review seats.
- Relevant environment: A host Git project, a project operator and an installed supported model CLI.
- Standard-distribution boundary: ADE's packaged commands, role dispatch, provider adapters, records, lane worktrees and hooks.
- Credited operating / distribution surfaces: Native card/board/conductor, supported provider role calls, direct review, landed changes and standing-ruling return.
- Adjacent first-party surfaces excluded from ownership: Provider internals, outside schedulers, the maintainers' personal coordination environment and ADE development-only experiments.
- First-party operating / deployment modes considered: One-card loop, parallel conductor, terminal/cockpit supervision and supported external model clients invoked through native adapters.
- Recursion level: One ADE project. Concurrent card lanes have independently scoped operations.
- Reviewed revision: b719450d92b86e546b0bd8b8ddc4d66d050e0064
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The supplied driver reads a card and walks lane, build, review, test and land. Supported provider CLIs execute first-party role prompts in the lane. The project record persists cards, questions and rulings. The conductor can keep independent card lanes active. It defers a lane whose source reach overlaps another active card and rechecks after sessions finish.

## Operational model

Each lane owns producing the card's scoped change. The builder selects actions and reports completion, and ADE validates and journals the resulting tree. A distinct reviewer judges the artifact before test/land. The project operator can suspend or remove current obligations and authorize a project-wide standing rule.

## S1 — Operations

- State: A
- Function: Produce and integrate a scoped implementation from a card.
- Disturbance / variety regulated: The card's premise may be stale, implementation alternatives differ and tests reveal failures.
- Decisive decision or feedback right: Choose edits and evidence against the card's done condition, or attest that the baseline already meets it.
- Decision owner: The builder model commissioned by the shipped ADE provider adapter.
- Supporting / enforcement mechanisms: Worktree, card scope, generated prompt and required review, test and land stages.
- Closure path: The builder's workspace changes or attestation hit the build contract. The driver commits qualifying work and advances it through validation and ordinary landing.
- Boundary reachability: The installed loop calls a configured supported CLI in the builder seat with a shipped role protocol. Installing/authenticating an engine is setup rather than composing the operational actor.
- Why this is / is not agent-owned: The deterministic driver moves stages and records evidence. The builder chooses the actual work from the task state.
- Evidence: [README.md](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/README.md#L28-L53), [ade/verbs/loop.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/loop.py#L89-L126), [ade/stages/build.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/build.py#L105-L145), [ARCHITECTURE.md](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ARCHITECTURE.md#L255-L263)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Reserved paths and unresolved stage judgments can require user action.

## S2 — Coordination

- State: C
- Function: Attenuate code-footprint interference between concurrently active card lanes.
- Disturbance / variety regulated: Two work scopes can depend on or touch the same graph reach or trunk paths.
- Decisive decision or feedback right: Choose whether to defer, change scope or admit a potentially clashing commitment beyond the supplied exclusion heuristic.
- Decision owner: The conductor supplies a specialized graph-range coordination path with a fixed admission order. A discretionary coordinator is a composition point.
- Supporting / enforcement mechanisms: Graph reach, live process records, isolated worktrees and serial landing.
- Closure path: A clashing card is held from start. The conductor recomputes eligible work after a lane leaves the active set and starts newly free cards.
- Boundary reachability: The native parallel conductor invokes the overlap filter before launching detached card sessions.
- Why this is / is not agent-owned: The function-specific disturbance and feedback are supplied. The fixed rule and stage enforcement do not establish an agent choosing negotiated tradeoffs.
- Distinct S1 units: Independently scoped, worktree-isolated cards with their own builder calls.
- Inter-S1 disturbance: Potential inter-card conflict from shared files, dependencies or conservative folder-level reach.
- Attenuating coordination relation: Compare per-card graph footprint with active and selected lanes. Defer clashes and communicate the reason.
- Feedback into subsequent S1 behaviour: When a prior lane ends, live lane and graph state is recomputed and changes which pending card may start.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Admission depends on overlap with current operations and is revisited from their observed state. It goes beyond starting cards in sequence.
- Evidence: [ade/verbs/conduct.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/conduct.py#L128-L163), [ade/verbs/conduct.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/conduct.py#L192-L231), [ade/verbs/conduct.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/conduct.py#L232-L255), [ARCHITECTURE.md](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ARCHITECTURE.md#L298-L307)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Graph reach is a heuristic. Local worktree separation does not by itself discharge changed trunk conflicts.

## S3 — Inside-and-now control

- State: P
- Function: Regulate project-wide current card commitments through an operator-visible board.
- Disturbance / variety regulated: Previously selected work can become low priority, blocked or inappropriate to land.
- Decisive decision or feedback right: Choose which held work to retry, drop or rework, and which reserved-path change may enter trunk.
- Decision owner: Project operator in the terminal/cockpit mode.
- Supporting / enforcement mechanisms: Board, open-question desk, persisted answers, hold state, conductor and land gate.
- Closure path: A drop answer closes the obligation. A rework answer returns to the builder, and a permitted land answer releases the reserved hold.
- Boundary reachability: Board, decision desk and typed answers ship in the installed ADE CLI. The conductor reads the returned disposition.
- Why this is / is not agent-owned: The conductor applies a fixed route and the wake prompt scopes repairs to one stopped card. The established portfolio disposition is the operator's choice.
- Whole-system current view: The board, handover and decision desk expose open cards, flying lanes and questions across this project.
- Current-control decision scope: Park, release, drop, rework or allow reserved delivery for a selected project obligation in light of the current board.
- Evidence: [ade/verbs/handover.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/handover.py#L72-L99), [ade/verbs/card.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/card.py#L138-L147), [ade/verbs/conduct.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/conduct.py#L79-L93), [ade/verbs/conduct.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/conduct.py#L272-L313), [ade/verbs/decide.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/decide.py#L265-L282), [ade/stages/land.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/land.py#L126-L157), [ade/stages/build.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/build.py#L99-L112)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The agent may repair a lane or answer specific questions when configured. The supplied repair wake does not itself establish autonomous board-level resource or priority judgment.

## S3* — Complementary audit

- State: A
- Function: Independently audit the actual lane change against the card's claimed completion.
- Disturbance / variety regulated: A builder can produce an incorrect, insufficient or over-scoped patch.
- Decisive decision or feedback right: Review the lane diff and files, then choose approval, a corrective edit or a stopped finding.
- Decision owner: Separately invoked reviewer model using the first-party review role.
- Supporting / enforcement mechanisms: Pinned tree, direct Git diff, isolated lane, review runner, tree-keyed verdict, scope check and stage journal.
- Closure path: A qualifying verdict advances the reviewed tree. An authorized correction changes the tree before advancing, and a negative finding stops for judgment.
- Boundary reachability: The default non-prose, review-enabled card flow calls the native reviewer. Optional opposite or forked review selects a different seat/runtime context without adding custom control logic.
- Why this is / is not agent-owned: The builder's ordinary result cannot supply the review verdict. The separately commissioned reviewer reads the diff and owns its disposition.
- Claim being audited: The tree satisfies the card's done line and the change belongs to the card.
- Ordinary reporting path: Builder report, worktree commit and build stage status.
- Complementary access path: Review reads the actual lane tree delta and can inspect files through its configured engine.
- Independence boundary: The reviewer receives a separate role invocation and independent tree evidence. Same-provider operation is possible.
- Who acts on findings: The driver uses the review verdict and tree identity to advance or route a stopped finding. In-scope reviewer edits can be committed.
- Evidence: [ade/stages/review.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/review.py#L168-L196), [ade/stages/review.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/review.py#L231-L274), [ade/stages/review.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/review.py#L276-L305), [ade/stages/review.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/review.py#L331-L363), [ade/verbs/loop.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/loop.py#L105-L126)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Prose-only and review-off paths do not run this reviewer. The source does not prove reviewer quality.

## S4 — Outside-and-then intelligence

- State: —
- Function: A recurring outside-and-then capability decision was sought across installed project operation.
- Disturbance / variety regulated: New deployment constraints or changing future work could require a different operating capability.
- Decisive decision or feedback right: No supplied recurring path links environmental findings to a judged and returned future adaptation.
- Decision owner: Initial configuration uses a deterministic project survey. The operator and pilot can initiate future work.
- Supporting / enforcement mechanisms: Install survey, trunk drift notes, recurring cards, digest and external scheduler seams.
- Closure path: The survey seeds configuration at first install. Digest observations inform the user or a future card but do not supply the full prospective adaptation loop.
- Why this is / is not agent-owned: The installed signals address current trunk movement, repeated internal decisions or first-time setup. Supplied operation does not turn changes in the external environment into a settled future capability option.
- Evidence: [ade/survey.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/survey.py#L48-L82), [ade/install.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/install.py#L433-L437), [ade/verbs/digest.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/digest.py#L59-L74), [ade/verbs/card.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/card.py#L69-L96), [ARCHITECTURE.md](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ARCHITECTURE.md#L105-L120)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: An operator can act on digest suggestions or configure an external coordinator. The assessment covers the installed first-party paths.

### Absence scope

- Surfaces inspected: Install survey, card draft and recurrence, path drift, digest guidance and scheduler interfaces.
- Plausible first-party paths checked: Persistent external sensing, option formation from forecast conditions, and autonomous or parent-enacted return to changed operating capability.
- Why no material first-party path remains: The initial survey ends at configuration seeding. The operating digest summarizes internal events and offers scoped advice without a shipped environmental sensing and adaptation transaction.

## S5 — Policy and identity

- State: C(P)
- Function: Decide which standing rules about project intent, values and reserved authority govern all seats.
- Disturbance / variety regulated: An agent proposal or a new project constraint can conflict with existing standing direction.
- Decisive decision or feedback right: Approve or reject a proposed standing rule, and keep or retire adopted policy.
- Decision owner: Project operator in the default mode. An explicitly enabled agent-answer mode provides function-specific construction for a policy decision actor.
- Supporting / enforcement mechanisms: Proposal state, typed standing answers, attribution marker, rule book limits and role prompt injection.
- Closure path: A proposal governs nothing until stood. Standing rulings are returned into handover and every relevant role prompt, and retired rules stop appearing.
- Boundary reachability: The installed CLI has an explicit standing proposal/answer path and returns the resulting live rules into native role prompts. A supported option admits agent answers, while separately commissioning an agent to choose standing policy remains a construction step.
- Why this is / is not agent-owned: An installed pilot can propose a standing change. The default policy judgment is reserved to the project operator. Opt-in agent permission supplies policy-specific closure without a native autonomous portfolio-policy assignment.
- Identity / ultimate-policy issue: Which project-wide directions, values or reserve conditions should bind all cards and seats.
- Ultimate authority in each claimed mode: The root project operator by default. An agent may be explicitly authorized to act through the standing-ruling constructor.
- Return-to-operation path: The enacted record becomes a live ruling and appears in subsequent handover and role prompts. Proposal or retirement does not enter those prompts.
- Evidence: [ARCHITECTURE.md](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ARCHITECTURE.md#L267-L280), [ade/verbs/decide.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/decide.py#L285-L316), [ade/verbs/decide.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/decide.py#L434-L449), [ade/verbs/handover.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/handover.py#L72-L88), [ade/stages/build.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/build.py#L84-L96)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The actor label is based on environment markers, and the supported opt-in does not itself demonstrate an autonomous S5 policy judgment.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Externally commissioned policy actor | Standing policy proposal and configured agent answer right | A typed stand decision activates the rule and returns it to native prompts. Commissioning the deciding policy actor remains separate | [ade/verbs/decide.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/decide.py#L285-L305), [ade/stages/build.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/stages/build.py#L84-L96) |
| Parent (`P`) | Project operator | A proposed standing direction is before the operator | The operator stands or rejects it. A standing ruling enters the prompts used for later work | [ARCHITECTURE.md](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ARCHITECTURE.md#L269-L280), [ade/verbs/decide.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/decide.py#L285-L305), [ade/verbs/handover.py](https://github.com/The-Anthropocene/ade/blob/b719450d92b86e546b0bd8b8ddc4d66d050e0064/ade/verbs/handover.py#L72-L88) |

## Recursion

A card lane is a nested operating unit. Project-level coordination, current control and standing policy span cards, while complementary review reads each lane's actual artifact.

## Variety and escalation

Graph reach, isolated worktrees, route dispositions, typed operator questions and the shared landing runway regulate varied code work and interventions. Some questions explicitly hold a commitment or guard reserved paths. No separate claim of algedonic classification is made.

## Evidence gaps

Static pinned-source review across supported modes. Actual provider execution, operational conflict traces and authorization behavior of deployed actor markers were not run. The project's own VSM table is a source lead and the vectors above use the selected Index contract.
