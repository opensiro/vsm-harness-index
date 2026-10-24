---
harness_id: henrik-agent-harness
project_name: Henrik Agent Harness
repository: https://github.com/henrik-me/agent-harness
review_ref: 9168fa451b69c5d53b961ab5c805b3067597ade4
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Henrik Agent Harness

## Review boundary

- System in focus: A **consumer-installed and model-operated software-delivery process cell** using the project's shipped CLI, managed/composed process instructions, clickstop planning, agent briefing, WORKBOARD, independent PR review and evidence gates. The relevant recursion is one adopter project with orchestrator/model-backed contributor work and supervised PR delivery, **not** the deterministic CLI considered in isolation and **not** the maintainers of the upstream template repository.
- Purpose and identity: Organize model-assisted coding and PR delivery by turning reviewed clickstop work into bounded parallel contributor tasks, owned file changes, independently reviewed PRs and recorded closure.
- Relevant environment: New user product requests, concurrent edit conflicts, overlapping CS claims, incomplete or misleading implementer reports, failing checks, new upstream harness template revisions and adopter-controlled policy.
- Standard-distribution boundary: Node CLI and first-party `template/` process files copied to consumer repositories through `harness init/sync`; model-assisted consumer execution using emitted subagent briefs and GitHub Copilot PR review when configured. Supported supervised operator mode supplies the actual model host, GitHub credentials, claimed work, approval and final merge. CLI-only `dispatch` is read-only and does not start an agent; its existence is not itself an autonomous S1 or S3 actor.
- Credited operating / distribution surfaces: [managed/composed/seeded sync architecture](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/ARCHITECTURE.md#L1-L65), [subagent model and file-boundary contract](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L936-L1013), [canonical briefing emitter](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/dispatch.mjs#L1-L105), [claim plan and live admission guard](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/claim.mjs#L435-L604), [review invoking Copilot and independent rubber-duck](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L90-L299), [Copilot engagement](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/copilot-engage.mjs#L215-L351), and [consumer review gates](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/.github/workflows/review-gates.yml#L1-L172).
- Adjacent first-party surfaces excluded from ownership: The upstream source repo's own CI/release and historical clickstop records; maintainer retrospective claims of success not independently replayed; arbitrary host-internal Claude/Codex subagent APIs; GitHub/Copilot as a separate product/organization; future custom consumer process extensions; all review workflows not installed or enabled in a consumer. Upstream docs describe operational roles, but those model agents execute in an external host, not inside the Node CLI.
- First-party operating / deployment modes considered: Fresh consumer init and sync with review gates; human- or parent-agent-supervised task dispatch with exact bounded agent prompts; WORKBOARD claim/takeover; review --no-poll/manual rubber-duck and Copilot-request/poll modes; opt-in managed review workflows and guided upgrade preview. An unconfigured CLI-only dry run cannot independently run coding or approve policy.
- Recursion level: One consumer project delivery cell containing separately scoped implementer S1s, a source-supported but externally enacted current management role, and complementary PR audit.
- Reviewed revision: 9168fa451b69c5d53b961ab5c805b3067597ade4; frozen [intake #1699](https://github.com/opensiro/vsm-harness-index/issues/1699) and serial [batch #1700](https://github.com/opensiro/vsm-harness-index/issues/1700).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

This Node 20+ process library is not a hosted agent execution engine. Its shipped config/schema/template and `init/sync` materialize managed policies, composed local controls, seeded project state and GitHub CI workflows into an adopter repository. A model-bearing external orchestrator follows these first-party instructions, chooses and briefs specialist subagents, and re-enters the process after task reports. `harness dispatch` mechanically extracts a source-verified mandatory briefing, appends identity, explicit owned/do-not-touch files, deliverables and decision authority, then prints a prompt for the external orchestrator to paste into a model-enabled agent host; it never itself launches that host. [architecture](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/ARCHITECTURE.md#L1-L81), [CLI dispatch documentation](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L936-L1013), [dispatch read-only behavior](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/dispatch.mjs#L1-L36), [briefing composition](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/dispatch.mjs#L273-L386).

The first-party `claim` tool plans transition of a clickstop from planned to active, checks WORKBOARD so one orchestrator identity cannot silently claim a second active CS, and rechecks this condition immediately before applying a state mutation. It renames the work file and updates the active workboard row. `closeout` validates closing evidence and moves completed work; neither owns a discretionary judgment over overall project priority. External model-backed orchestrator guidance requests bounded delegation, file disjointness, report checks and return from failures, but the deterministic CLI does not invoke it autonomously. [claim planning](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/claim.mjs#L435-L500), [claim recheck and apply](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/claim.mjs#L563-L608), [orchestrator availability and progress](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L1333-L1383), [closeout](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/closeout.mjs#L390-L573).

The distinctive source-wired independent review mode is `harness review`: it requires implementer-model identities, composes a reviewer prompt with the actual PR identity/diff context, enforces reviewer-model separation, optionally awaits supplied independent rubber-duck output, **requests GitHub Copilot as an actual PR reviewer**, polls the PR head and folds returned findings into a combined Go/Needs-Fix verdict. Evidence rows are written back to the PR and managed workflow checks can block merge on missing/stale review evidence. The GitHub reviewer is an externally operated model, but its source-wired invocation, review response and enforcement are first-party paths when configured. [runReview](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L90-L299), [review independence](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L368-L424), [verdict](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L482-L537), [Copilot REST request and polling](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/copilot-engage.mjs#L215-L478), [review gates](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/.github/workflows/review-gates.yml#L1-L171).

Other source components harvest stale learning candidates, preview consumer upgrade diffs against a user-selected newer upstream ref, enforce schema and release constraints, and provide workboard-only auto-approval. These are deterministic workflow/option presentation, not proof of model-generated future strategic capability redesign. The frozen project identifies itself as MIT, npm package v0.17.0 with Node dependencies. The checkout was pinned to `9168fa4` with Git tree `1e86d762a72a6db54507eb1e4b005547599671b2`; local Node test installation and run are separately recorded. [upgrade preview](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/upgrade.mjs#L92-L183), [learning harvest](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/harvest.mjs#L1-L177), [package](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/package.json#L1-L43).

## Operational model

In the supported adopter mode, external model-backed coding subagents with first-party scoped briefs produce source changes and reports; a first-party Copilot reviewer also makes independent model-generated PR review findings (S1=A). The process specifically addresses two distinct operational disturbances: parallel implementers overwriting the same files (disjoint ownership protocol) and parallel orchestrators claiming overlapping active work (state-based claim guard) (S2=C). The WORKBOARD, report shape, claim/closeout and approved stage gates form a management-specific constructor, but the discretionary owner that actually reprioritizes and redispatches work remains the external orchestration host/operator rather than an autonomously invoked first-party management loop (S3=C). In the opt-in review mode, independent reviewer model judgments inspect PR evidence not simply the implementer's narrative; their blocking findings return through review/CI gates to rework or withheld integration (S3*=A). Stale learnings and preview upgrades alone do not establish prospective externally oriented strategic option generation/adoption (S4=—); ordinary user approval of a commit or file policy does not constitute legitimate ultimate constitutional identity closure (S5=—).

## S1 — Operations

- State: A
- Function: Produce substantive bounded changes and reviews in consumer software work through distinct model-backed contributors, and source-connected Copilot PR analysis.
- Disturbance / variety regulated: Task-specific source/edit choices, unexpected actual code state, review findings and failure/repair feedback.
- Decisive decision or feedback right: In the supported model-operated consumer mode, each contributor model chooses content of its scoped implementation or critique; GitHub Copilot chooses PR review findings from the actual current PR head.
- Decision owner: Externally provided model agents acting under first-party scoped briefing and PR-review invocation; human/operator chooses the task and final merge, not the agent's substantive code/review response.
- Supporting / enforcement mechanisms: `harness dispatch` emitted canonical prompt and owned-file scope, `WORKBOARD.md`, clickstop plan, real GitHub PRs, reviewer model allowlists and managed review gate checks.
- Closure path: Consumer work/PR requirement → orchestrator supplies bounded first-party briefing or CLI requests Copilot reviewer → model performs implementation or PR review → changed files/review findings returned to the consumer PR/workboard → further correction and submission.
- Boundary reachability: `harness init/sync` installs the model-enabled process instructions; `harness review` explicitly performs the GitHub reviewer request/poll rather than only drawing an agent diagram. External agent host/Copilot authorization must be configured; CLI-only mode has no model executor.
- Why this is / is not agent-owned: Model-backed specialists and reviewer choose substantive decisions; deterministic Node tooling cannot derive their implementation or review findings without the model. This is an A mode **only in the declared connected model-operated consumer cell**, not for a standalone Node CLI.
- Evidence: [model roles and parallel work](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L936-L1013), [subagent briefing and output](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/dispatch.mjs#L273-L386), [review execution path](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L90-L299), [real Copilot review request/poll](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/copilot-engage.mjs#L215-L478).
- Basis: First-party consumer operating contract plus executable external model reviewer integration.
- Confidence: Medium source-structural; distinct implementer execution depends on external agent host not bundled.
- Caveats: GitHub reviewer credentials, model quality, independent coding success and a complete live adopter project were not demonstrated. No autonomous execution claimed for the CLI itself.

## S2 — Coordination

- State: C
- Function: Prevent destructive conflicts among parallel operational contributors and overlapping currently active work claims before they affect other S1 outcomes.
- Disturbance / variety regulated: Concurrent specialists silently overwriting one another's files and two orchestrator work claims racing for an already occupied coordination slot.
- Decisive decision or feedback right: Establish disjoint per-agent editable file scopes and disallow a second active work claim for one owner unless deliberately transferred/taken over.
- Decision owner: The parent orchestrator or operator decides actual task partition/scopes and takeovers; first-party deterministic CLI state and briefing constructors enforce/show preconditions, not autonomous mutual compromise.
- Supporting / enforcement mechanisms: Explicit owned/read-only/do-not-touch briefing fields, no-commit worker discipline, WORKBOARD ownership rows, apply-time re-read/refusal, scoped clickstop branches.
- Closure path: Parent receives parallel task candidates → declares separate file ownership in each emitted brief and claims a single active work slot → worker follows scoped briefing; conflicting claim is rejected, requiring reassignment before additional work proceeds → subsequent agent tasks operate on revised or nonoverlapping assignments.
- Boundary reachability: `harness dispatch` builds emitted own/do-not-touch sections on every configured dispatch; `claim` directly checks the current WORKBOARD at plan and mutation time and fails closed for active owner collisions. These are delivered consumer-facing CLI commands and managed policy, not an aspirational slide.
- Why this is / is not agent-owned: Concrete inter-worker lost-edit failure is documented in the source policy, and S2-specific interference is regulated through source-wired constructor/enforcement. The external orchestrator must pick the compromise, and the CLI does not independently detect all overlaps between distinct work files/agents.
- Distinct S1 units: Independently model-operated specialist implementers assigned different concurrently active clickstop work and file scopes.
- Inter-S1 disturbance: Two contributors can write one overlapping file and silently lose the earlier changes; the process source describes an observed `lib/templating.mjs` / `lib/lock.mjs` collision from parallel dispatch.
- Attenuating coordination relation: Allocate exclusive writable sets per specialist and a single active work claim per owner; reject owner collision at apply-time.
- Feedback into subsequent S1 behaviour: A conflicting owner work claim fails or a shared file becomes explicitly read-only for one worker; parent must rebrief/serialize/reclaim before launching the affected worker.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: These targeted mechanisms mitigate a stated *inter-contributor lost-edit race* and concurrent work-claim collision. Generic passing of a task ID or state alone is not counted.
- Evidence: [actual lost-edit incident and explicit file ownership](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L969-L1013), [briefing file scope](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/dispatch.mjs#L273-L335), [claim collision check](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/claim.mjs#L435-L500), [apply-time recheck](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/claim.mjs#L563-L606).
- Basis: Shipped S2-specific coordination constructor with source-documented disturbance.
- Confidence: Medium-high for the narrow fail-closed work-claim check and explicit overlapping-file procedure.
- Caveats: The emitted brief does **not** compare all concurrent file scope declarations mechanically; adherence depends on the actual external orchestrator/worker.

## S3 — Inside-and-now control

- State: C
- Function: Assemble a whole-current delivery view and a bounded work-commitment lifecycle, allowing an external management actor to choose and revise active staffing, priorities and release/rework intervention.
- Disturbance / variety regulated: Competing active clickstops, stale work, incomplete handoffs, unidentified worker ownership, current blocked dependencies and inconsistent PR closure.
- Decisive decision or feedback right: Choose which planned clickstop to activate, assign its owner/branch, accept a failed review and instruct rework, decide whether to close/release completed work.
- Decision owner: The source-prescribed external orchestrator or responsible human in the consumer project. The Node CLI gathers/checks workboard/current-state evidence and applies selected transitions; it does not autonomously choose among priority alternatives.
- Supporting / enforcement mechanisms: WORKBOARD, `harness status`, `harness claim`, `harness closeout`, progress reports, single-active-work gate, review verdicts and CI merge controls.
- Closure path: Whole current WORKBOARD and planned clickstop inventory → external manager identifies a current commitment, invokes claim/dispatch → workers return status/review evidence → manager decides correction/reallocation or closeout → first-party CLI updates active work and subsequent assignment context.
- Boundary reachability: Consumer installation materializes the workboard and process docs; shipped `claim/status/closeout` commands read/write actual files and refuse inconsistent transitions. The core Node tool is a constructor for current-control decisions; the source does not auto-launch the orchestrator model.
- Why this is / is not agent-owned: Model-coded management acts only when operated by an external agent host; removing that host leaves deterministic workboard plumbing but no discretionary portfolio negotiation. A positive `C` here identifies a *specific delivered S3 control constructor*, not automatic S3=A or generic workflow completeness.
- Whole-system current view: The active/planned clickstop table and owner/branch/blocked metadata in WORKBOARD plus PR/review state and reporting, at the one consumer delivery-cell recursion.
- Current-control decision scope: Active CS allocation/owner, constrained parallelism, failed review return and closeout of a project's current delivery commitments, not host-company staffing or long-term constitutional goals.
- Evidence: [claim current-cell view](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/claim.mjs#L267-L500), [claim mutation](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/claim.mjs#L563-L603), [closeout](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/closeout.mjs#L390-L573), [orchestrator management role](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L1333-L1383).
- Basis: Specific first-party current-control observation, transition and return machinery, with externally owned discretionary S3 right.
- Confidence: Medium source-structural.
- Caveats: Human/LLM consumer actor is required; no standing self-running S3 agent, whole-system budget negotiator or parent-governed S3 `(P)` path is established by this source. Workboard alone does not count; the positive constructor depends on its wired claim/rework/closeout loop.

## S3* — Complementary audit

- State: A
- Function: Independently inspect producer claims against the actual PR head and return findings that alter acceptance/rework decisions.
- Disturbance / variety regulated: Implementer overconfidence, stale review against an old commit, omitted blocking code defects or approval from a reviewer sharing the implementer's model context.
- Decisive decision or feedback right: Model-based reviewer chooses a fresh Go/Needs-Fix and issue findings from reviewed PR evidence, independently of the producing actor; first-party review framework rejects reviewer-model conflicts and refuses to treat blocking findings as approval.
- Decision owner: Independently invoked reviewer model (local rubber-duck when supplied, or GitHub Copilot PR reviewer) for factual/technical judgment, with first-party CI acting as enforcement. A model that also implemented the PR is barred by the configured separation rule.
- Supporting / enforcement mechanisms: `assertReviewerAllowed`, model audit fields, actual PR HEAD and diff evidence, reviewer prompt, Copilot REST reviewer invocation, per-HEAD review log and managed review-gates.yml required checks.
- Closure path: Implementer submits current source/PR → independent model reviews that head and identifies findings → `computeVerdict` returns No-Go/Needs-Fix on blocking output, logs exact reviewed SHA → review workflow blocks integration until a valid current-head review → orchestrator/worker reworks PR and requests a new round.
- Boundary reachability: `harness review` first-party command genuinely requests Copilot reviewer through GitHub when review config enables it; `review-gates.yml` is shipped to consumers via `init/sync` and includes independent/attached evidence checks; source documents the reviewer dispatch as the normal content-PR gate.
- Why this is / is not agent-owned: Reviewer model assesses producer output from separately obtained actual PR source, chooses critique and can force new work; deterministic log parsing and CI do not themselves own that independent judgment.
- Claim being audited: Current implementer/subagent work is correct and ready to merge under its original clickstop acceptance criteria.
- Ordinary reporting path: Worker completion report and PR author statements, branch status and routine task tests.
- Complementary access path: Separate model reviewer analyzes actual PR current head/diff and required reading, with Copilot's independently attached GitHub review as a distinct channel.
- Independence boundary: Different reviewer model from recorded implementers is enforced for local audit; Copilot is a separate GitHub review actor; primary evidence and head SHA are checked instead of recycling author summary alone.
- Who acts on findings: First-party verdict and required checks withhold Go/merge evidence; supervised orchestrator triggers repairs and a new review round.
- Evidence: [review PR and independent-model gate](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L90-L224), [Copilot review and combined verdict](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L230-L299), [verdict logic](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/review.mjs#L482-L537), [Copilot actual review](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/copilot-engage.mjs#L215-L478), [managed enforcement](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/.github/workflows/review-gates.yml#L1-L170).
- Basis: Explicit source-connected complementary reviewer judgment, distinct access and rework/block closure path.
- Confidence: Medium-high for configured reviewer-enabled consumer mode; actual real PR review not replayed in this isolated assessment.
- Caveats: Without GitHub authentication, enabled review checks and a responding reviewer, the model audit is not executable; source review is not a measured guarantee that Copilot detects all errors. Optional manual-only mode should not be conflated with autonomous reviewer operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: Scan external changes with a prospective model, develop options for changing future delivery-cell capability and return chosen adaptation to current control.
- Disturbance / variety regulated: Changes in future tooling, supported environments, dependencies or customer delivery needs requiring a changed organizational capability rather than one repaired work item.
- Decisive decision or feedback right: No shipped first-party externally prospective adaptation judgment and closed option-to-capability feedback right found.
- Decision owner: Not established: `harness upgrade` compares a **user-specified** target Git ref deterministically, while `harvest` lists stale existing learning entries for later operator disposition.
- Supporting / enforcement mechanisms: Upgrade dry-run diff, version pin and managed sync, LEARNINGS.md harvest, clickstop planning, changelog and maintenance rules.
- Closure path: No first-party model of external future conditions that selects among capability change options, returns the prospective decision to S3, and updates later operational capacity without an externally authored plan.
- Why this is / is not agent-owned: Upgrade preview and manual version application can change installed files, but the candidate ref and adoption judgment are supplied from outside, not selected through a shipped strategic prospective loop; stale-learning surfacing is retrospective operational improvement.
- Evidence: [upgrade takes specified ref and previews only](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/upgrade.mjs#L92-L183), [harvest stale items](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/lib/harvest.mjs#L1-L177), [model/role process configuration](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L936-L1013).
- Basis: Bounded negative at first-party installed/CLI paths, not universal impossibility for custom consumers.
- Confidence: Medium; human-managed downstream process evolution can be built from these primitives but is not itself source-closed S4.
- Caveats: Consumer humans may perform strategic adaptation; the source does not warrant crediting that unobserved higher-recursion function.

### Absence scope

- Surfaces inspected: `upgrade` preview and `sync` application, harvest/learning lifecycle, clickstop planning, source docs, model selection and release rules.
- Plausible first-party paths checked: External newer upstream ref diff and promotion, learnings-to-future-CS suggestions, context harvesting and operational review corrections.
- Why no material first-party path remains: Tools expose manually nominated code diffs, stale retrospective records and current project tasks, but not autonomous or constructor-complete future externally oriented option judgment returned to delivery S3.

## S5 — Policy and identity

- State: —
- Function: Resolve legitimate ultimate-policy/identity disputes over the consumer delivery cell's enduring mission and reconcile current versus future orientations.
- Disturbance / variety regulated: Conflicting enduring purposes, permissible changes of identity, constitutional operating constraints or ultimate authority.
- Decisive decision or feedback right: Not established by the first-party shipped process. User approval gates concern task-plan/implementation details or acceptance of a code/review change, not a reconstructable constitutional adjudication path.
- Decision owner: No source-connected S5 ultimate-policy actor is evidenced; the adopter or project owner remains external higher recursion.
- Supporting / enforcement mechanisms: INSTRUCTIONS, CODE_OF_CONDUCT, CONVENTIONS, review rulesets, workboard approval policy, optional owner override, credentials and repository settings.
- Closure path: No identity-level issue → legitimate constitutional authority → authoritative decision → re-governed ongoing operations path established in first-party artifact.
- Why this is / is not agent-owned: Managed policy files and approvals constrain delivery, but do not transform their configured owners into a standing S5 entity. Model roles cannot independently rewrite legitimate identity.
- Evidence: [operating approval context](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/OPERATIONS.md#L73-L116), [review policy](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/REVIEWS.md#L1-L115), [workboard gate](https://github.com/henrik-me/agent-harness/blob/9168fa451b69c5d53b961ab5c805b3067597ade4/.github/workflows/workboard-auto-approve.yml#L1-L135).
- Basis: Bounded negative following inspection of permission, process governance and approval mechanisms.
- Confidence: Medium-high in this assessed recursion.
- Caveats: A consumer can attach genuine external S5 institution; it is not first-party authority supplied by the library.

### Absence scope

- Surfaces inspected: User approval gates, operating instructions, policy docs, model choices, CODEOWNERS, review gates, workboard approval/override and CLI surface.
- Plausible first-party paths checked: Human task approval, reviewer model independence, changelog/version approval, workboard auto-merge, administrator ruleset changes.
- Why no material first-party path remains: All observed checks regulate individual work/reviews or configured branch rules; none contains an ultimate purpose/identity question routed to legitimate authority with binding return into operation.

## Recursion

- Parent organization: Consumer owner/maintainers select goal, credentials, external model host and ultimately accept shipped code. Separate model provider/GitHub/organizational governance cannot be borrowed for S3*/S5 beyond explicit reviewer invocation in the supported consumer mode.
- Operational child work cells: Distinct specialist agents with disjoint work scopes perform implementation and report. Reviewers are separate operational/audit actors with independent PR access. `WORKBOARD` and clickstop files bind coordination and management at the parent delivery-cell recursion.
- Handoffs: Orchestrator/owner makes subjective current assignment choices, first-party claim/status/dispatch/closeout renders and records them; independent reviewer raises counterevidence and sends failed work back into the same current control path.

## Variety and escalation

- S1 variety: Model agent work and model reviewer handle local source/coding/verification choices; scopes and user tasks constrain authority.
- S2 interference: Exclusive writable-file brief and checked active work slots reduce worker overwrite and duplicate owner collisions.
- S3 current control: External orchestrator processes full workboard, chooses commitments and executes first-party claim/closeout state updates, but its internal model execution is not bundled by the Node CLI.
- S3* audit: Independent live model PR review can prevent merge on changed HEAD/Blocking feedback; repeat review round is required after repair.
- Higher levels: Upgrade/learning review offers deterministic upkeep but not S4 organizational prospecting; ultimate authority resides outside the assessed source.

## Evidence gaps

- Reviewed immutable Git ref and MIT license; no live external Claude/Copilot/GitHub production coding run or whole adopter-project merge was performed.
- `harness dispatch` produces textual prompts; it is **not** an agent launcher. S1 autonomy is bounded to the supported external-model-backed consumer mode, with a directly source-invoked Copilot reviewer; never infer CLI-only runtime autonomy.
- S2 file-scope exclusivity relies on orchestrator/worker prompt compliance; the CLI does not mechanically detect all cross-prompt overlaps. The narrower WORKBOARD owner-claim collision is explicitly checked.
- S3 remains constructor `C` because real current selection and reprioritization are by the external orchestrator/owner, not independently by a resident first-party agent. Task state and deterministic gates alone do not warrant `A`.
- S3* requires actual model reviewers and installed merge gates; the source proves review invocation and return contract, not independent accuracy on a real PR.
- Full frozen-source Node suite was run with dependencies installed; any nonzero test failures should be disclosed in the separate publication/PR receipt rather than interpreted as VSM state evidence.
