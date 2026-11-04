---
harness_id: ork
project_name: Ork
repository: https://github.com/mimshins/ork
review_ref: e97d75c554095ff41d79ef91fafbbdc8bcfc8b64
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Ork

## Review boundary

- System in focus: locally installed Ork workflow runner and its declared Claude-agent execution, coordination, review and run-control paths, rather than the Ork development organization.
- Purpose and identity: run user-authored YAML workflows of agent/tool nodes against local project environments, with delegated work, isolated branches, feedback and human decisions.
- Relevant environment: developer repositories, local git worktrees, Claude SDK/CLI and credentials supplied by the operator, optional external programs and human user.
- Standard-distribution boundary: public Ork monorepo at the frozen commit, including its CLI, core engine, Claude runtime, packaged example workflows and local control/UI. A user must select a workflow and supply provider access; no live provider invocation is asserted here.
- Credited operating / distribution surfaces: `packages/core/src/run/`, `packages/runtime-claude/src/tools/`, `packages/cli/src/`, `packages/nodes/src/`, and the executable `examples/software-factory.ork.yaml` and `examples/pr-review.ork.yaml` workflow modes.
- Adjacent first-party surfaces excluded from ownership: Ork's own `CONTRIBUTING.md`, release/CI tooling, source tests, design roadmap and development feedback/discussions. Tests corroborate paths but do not enact functions in a user's workflow. Third-party Claude internals are not treated as Ork-owned metasystem functions.
- First-party operating / deployment modes considered: installed local CLI workflow, agent leader/worker and message/claim tools, optional example factory/PR-review workflow, human gate/CLI/UI operator controls; not-yet-implemented feedback triage/apply and visual workflow designer are excluded.
- Recursion level: one Ork workflow run as the focal harness, with operational Claude nodes as S1; a leader-child subtree is a subordinate task arrangement, not automatically a separately viable recursion.
- Reviewed revision: `e97d75c554095ff41d79ef91fafbbdc8bcfc8b64`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Ork is a TypeScript/Node monorepo with a Zod/YAML workflow compiler, scheduler, Claude SDK and CLI runtime drivers, a local event store, run-scoped messages and advisory resource claims, per-writing-node git worktrees, CLI/UI controls and bounded loops. The core scheduler activates nodes, routes edges, joins results and records events; it also enforces predeclared budgets and concurrency. Agent nodes have real Claude sessions, tools and reports, while tool nodes and gates are deterministic or human-mediated. A `claude.leader` can delegate to declared child agents or spawn allowed worker copies, receive status/artifact/branch reports and respond to failed work. User-authored workflow files define identities, roles and limits. No credentials are stored by Ork.

The shipped `software-factory` example includes a spec worker, builder leader, separate readonly security/UX/code reviewers, a bounded correction loop, an agent approver and human publication gate. The `pr-review` example separately obtains a git diff, runs security and correctness reviewers in parallel and requests human consent before posting. These are supported first-party opt-in workflows, not automatically active in every Ork run. Ork's feedback capture, fingerprints and inspection are implemented, but the feedback-to-change triage/apply/lessons loop is explicitly future work in this revision.

Primary architecture: [README](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/README.md), [runtime specification](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/specs/scheduler.md), [design](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/docs/design.md).

## Operational model

Claude worker and leader sessions make local implementation, review and report decisions and act on a repository through permitted tools. A run's workflow graph and budgets belong to its author; the scheduler decides mechanically when steps start, finish or stop. In the example factory, the builder agent owns local coding and retry choices, reviewers separately inspect the branch, and the approver emits a reasoned verdict; human gate owns external publication consent. Claim refusals and release notices constrain parallel editing, but agents decide which resources to request and how to change work when contention is reported. No claim is made that a workflow developer's settings or the maintainer's project governance are autonomous Ork decisions.

## S1 — Operations

- State: A
- Function: Claude sessions in a workflow transform requests into code, specifications, reviews and other local project outcomes.
- Disturbance / variety regulated: changing user requests, repository state, test failures, tool results and child reports within each session's bounded task.
- Decisive decision or feedback right: choose concrete implementation/review actions and revise work from the tool, branch and report feedback.
- Decision owner: model-driven Claude agent node in the first-party runtime; an operator supplies the initial task and permissions.
- Supporting / enforcement mechanisms: graph activation, SDK/CLI driver, tool allowlists, worktrees, event store, session budget and schema validation.
- Closure path: agent chooses tools and edits, receives tool/result feedback, changes work and returns a structured report to its graph/leader.
- Boundary reachability: `claude.worker`/`claude.leader` nodes and their tool/report bridge are supported installed node types, exercised structurally by shipped example workflows; no third-party agent's hidden control architecture is borrowed.
- Why this is / is not agent-owned: actions in a live session remain discretionary even though workflow graph edges, budgets and output transport are deterministic.
- Evidence: [scheduler built-ins and delegation](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/specs/scheduler.md), [delegation port](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/packages/core/src/run/delegation.ts), [factory example](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/examples/software-factory.ork.yaml).
- Basis: structural.
- Confidence: high.
- Caveats: provider execution was not performed in this review; operator credentials and the chosen workflow are prerequisites.

## S2 — Coordination

- State: A
- Function: regulate competing write access among parallel S1 sessions in the same run.
- Disturbance / variety regulated: two concurrent writing agents can attempt overlapping files/folders or shared named resources, introducing overwrites or merge conflicts.
- Decisive decision or feedback right: agents select resources to claim, release them and respond to a refused claim by choosing another task or negotiating with the holder; the registry deterministically detects overlap.
- Decision owner: agent session for claim selection and the corrective work choice; deterministic claim registry for overlap verdict, holder identity, event delivery and automatic release.
- Supporting / enforcement mechanisms: advisory claim registry keyed by normalized paths, refusal and release notices, worktree isolation and message channels.
- Closure path: a conflicting claim is refused with holder identity; the agent receives that response, can communicate/replan, and may retry after a release notification, changing the subsequent S1 work target.
- Boundary reachability: claim/release tools are supplied to writing Claude nodes when a run exposes parallel writers; the scheduler binds the run-scoped claim port. This is a shipped operating mode, not a hypothetical custom integration.
- Why this is / is not agent-owned: Ork does not choose the agent's alternative work in response to contention; its registry only determines the fixed overlap rule. Claim discipline is advisory, so not every actual edit is protected.
- Distinct S1 units: concurrently running writer leader/worker nodes or spawned worker copies with separate tasks and checkouts.
- Inter-S1 disturbance: overlapping resource/path edits and resultant destructive interference, specifically documented as the reason for claims.
- Attenuating coordination relation: explicit per-resource claim refusal, release, holder/contender notification and optional peer messaging.
- Feedback into subsequent S1 behaviour: the refused agent sees the holding node and can work elsewhere or ask it; release notice tells the agent to claim again before editing.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: resource overlap is checked in executable first-party code, with a conflict-specific refusal/release feedback loop; message passing is only a support channel.
- Evidence: [claim registry implementation](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/packages/core/src/run/claims.ts), [Claude claim tool](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/packages/runtime-claude/src/tools/claims.ts), [claims and message specification](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/specs/messaging.md).
- Basis: structural.
- Confidence: medium.
- Caveats: autonomous conflict handling is agent-instructed but not hard-enforced and was not exercised with a provider here; if the claimed function is defined solely as lock acquisition, that deterministic subdecision is not agent-owned.

## S3 — Inside-and-now control

- State: C
- Function: control a multi-child run's current commitments and exceptions at a configured leader/whole-run boundary.
- Disturbance / variety regulated: child failure, run budget/concurrency saturation, exhausted revision loops, and conflicting current delivery commitments.
- Decisive decision or feedback right: the leader can choose whether and where to delegate/retry in light of child reports; an owner can answer an exhausted-loop exception, while configuration author sets the initial hard limits.
- Decision owner: first-party leader/owner decision ports are available; workflow author must compose a genuinely whole-run supervisory objective and authority envelope. The deterministic runner owns enforcement, not the resource-policy judgment.
- Supporting / enforcement mechanisms: slot/budget accounting, maxWorkers cap, statuses, reports, loop counter, human fallback and halt semantics.
- Closure path: delegated children return outcomes and costs; the leader can select follow-on work, or answer an exhausted loop to stop/extend/go onward; the scheduler executes the selected transition.
- Boundary reachability: leader tools, child reports and owner-question/answer loop are shipped in the scheduler and Claude runtime; their S3-specific whole-run composition depends on the declared workflow.
- Why this is / is not agent-owned: these are real current-intervention primitives, but a generic leader's task division alone does not establish a default autonomous whole-run S3 owner for arbitrary user workflows. This supports the narrower constructor `C`, not universal `A`.
- Whole-system current view: available child reports, run status, costs and configured limits; whether they form an actionable whole-system view is workflow-dependent.
- Current-control decision scope: child commitments and retry/loop continuation under configured budgets; no assertion that the agent can revise operator-specified global policy.
- Evidence: [leader/child delegation](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/packages/core/src/run/delegation.ts), [loop owner decision](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/packages/core/src/run/escalation.ts), [scheduler budget](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/specs/scheduler.md).
- Basis: structural.
- Confidence: medium.
- Caveats: no parent-mode suffix from ordinary human gates, pause/stop or local approval; no runtime end-to-end current-control trace tested.

## S3* — Complementary audit

- State: A
- Function: inspect implementation claims through separately tasked agents that can directly read the produced branch rather than rely only on the builder's report.
- Disturbance / variety regulated: defects in the builder's asserted completion, including security, correctness, UX and code-quality issues overlooked by ordinary production.
- Decisive decision or feedback right: independent readonly reviewer sessions judge the produced work and return pass/changes_requested; the builder then receives review status and revises in a bounded loop.
- Decision owner: separate reviewer Claude agents in the first-party `software-factory` opt-in mode; graph routing enforces returned verdicts, but is not the audit judge.
- Supporting / enforcement mechanisms: readonly checkout, fresh reviewer sessions, join statuses, bounded edge `maxRounds`, agent approver and optional human publication gate.
- Closure path: builder branch is inspected by separately running security/UX/code reviewers; a changes_requested result routes back to builder and triggers repair; passing reviews route to the approver.
- Boundary reachability: `examples/software-factory.ork.yaml` is a distributed executable Ork workflow invoking the installed reviewer node types with readonly project access. The path is an opt-in mode, not assumed present in every workflow.
- Why this is / is not agent-owned: the reviewer models decide the audit verdict based on direct artifact access; deterministic joins merely transport outcomes. Their separation is context/process isolation, not institutional independence from the operator or model supplier.
- Claim being audited: builder's assertion that a branch implements the spec correctly and safely.
- Ordinary reporting path: builder's status, summary and artifact/branch report to the workflow.
- Complementary access path: security/UX/code agents in readonly workspaces inspect the actual branch and surrounding code, not just the builder's summary.
- Independence boundary: different agent sessions, reviewer roles and readonly source access; all are authored within one user-defined workflow, so a malicious author can weaken the separation.
- Who acts on findings: builder corrects the branch when any review requests changes; approver examines the passing result before the user-controlled publication step.
- Evidence: [factory workflow](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/examples/software-factory.ork.yaml), [PR-review workflow](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/examples/pr-review.ork.yaml), [worktree/delegation behavior](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/docs/guides/leaders-and-delegation.md).
- Basis: structural.
- Confidence: medium.
- Caveats: source-grounded installed example path, not independently executed S3* evaluation or a universal independent-audit service; routine sequential QA in an arbitrary workflow would not automatically qualify.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally oriented prospective adaptation loop is established at the assessed run boundary.
- Disturbance / variety regulated: changing external demands or future capabilities could require adaptation, but no shipped owner closes that function.
- Decisive decision or feedback right: not established for an Ork-run S4.
- Decision owner: none demonstrated; workflow authors or maintainers may revise YAML and Ork code outside the run.
- Supporting / enforcement mechanisms: captured feedback, event store, local feedback list/note/dismiss, context compiler and user-authored scripts.
- Closure path: no shipped feedback-to-accepted-change/lesson path into future current run capability at this revision.
- Why this is / is not agent-owned: collection and grouping of past errors are not themselves a future-oriented model/options/return loop.
- Evidence: [feedback spec with explicit partial implementation](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/specs/feedback.md), [feedback guide](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/docs/guides/feedback.md), [roadmap](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/docs/interaction-map/roadmap.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a user may build a separate adaptation workflow; that is not shipped S4 closure in the declared default system.

### Absence scope

- Surfaces inspected: README, design and feedback guide/spec, implemented feedback source locations, core run and agent tools, documented modes and example graphs.
- Plausible first-party paths checked: feedback capture/triage/apply/lessons, agent `feedback` tool, repeated loop/review repair, context compiler, roadmap and operator workflow edits.
- Why no material first-party path remains: triage/apply/lesson propagation is explicitly future work; ordinary within-task revision and manual YAML edits lack a built-in external/future option-to-capability feedback closure.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy adjudication path for a workflow organization is established.
- Disturbance / variety regulated: identity or policy tensions can arise, but Ork's gates and constraints concern routine task/runtime permissions and delivery.
- Decisive decision or feedback right: no shipped S5-specific issue, legitimate authority judgment and return-to-operation path.
- Decision owner: workflow author/operator defines configuration and controls ordinary approval; those actions are not an evidenced identity-policy process.
- Supporting / enforcement mechanisms: YAML settings, tool allowlists, budget caps, `ask_user`, human gates, CLI run controls and local auth.
- Closure path: ordinary approvals/stop and permission decisions affect run progression, not an established ultimate-policy matter.
- Why this is / is not agent-owned: a user or agent can edit instruction text or choose publication, but no system-specific S5 right is constructed or closed.
- Evidence: [workflow format](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/specs/workflow-format.md), [message and decision controls](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/specs/messaging.md), [factory human gate](https://github.com/mimshins/ork/blob/e97d75c554095ff41d79ef91fafbbdc8bcfc8b64/examples/software-factory.ork.yaml).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the external human/project may have its own legitimate S5; Ork's default standard distribution does not supply that governance loop.

### Absence scope

- Surfaces inspected: README, YAML schema/workflow descriptions, examples, Claude agent tools, run-control and decision queue, design/feedback documents.
- Plausible first-party paths checked: user approval/permission gates, workflow policy instructions, human stop/pause/answer modes, maintainer governance, feedback suggestions and operator editing.
- Why no material first-party path remains: these paths implement routine work control or external project governance, without a distinct identity-level matter, parent authority judgment and returned S5 closure for Ork's run.

## Distributed OSS parent arrangement

Contributors and maintainers govern the upstream Ork project, while local installed runs belong to their individual operators. No public maintainer issue/PR process is credited as a parent S3/S4/S5 mode of an installed workflow; no `(P)` notation is asserted merely from the repository's development organization.

## Self-hosted and non-human modes

The runner is self-hosted. A human can answer gates, interrupt or communicate with agents, but those controls alone do not evidence distinct parent-governed S3, S4 or S5 closure. The factory example remains an opt-in agentic workflow; no non-human ultimate-policy organization is claimed.

## Recursion

Ownership hierarchy and nested `claude.leader`/`claude.worker` sessions expose task subtrees. Child workers can decide local tasks, but no independently closed full VSM metasystem with its own persistent purpose/environment is established for arbitrary nested units; technical nesting is not scored as recursion.

## Variety and escalation

Ork attenuates run-level variety through brief-only child context, bounded loops, concurrency/budget limits, worktree isolation and claim notices. It amplifies handling capacity through concurrent workers and agent-owned retries. Failed delegation, merge conflicts, exhausted loops and explicit gates become reports/owner questions or human decisions, but these routine events are not automatically algedonic signals or S5 authority transfers.

## Evidence gaps

- This is a frozen source/architecture review; no paid Claude provider execution or external behavioral trace was run. Structural claims should not be read as measured reliability or audit quality.
- S2 claim discipline is advisory, and S3 is classified as a function-specific constructor rather than universal agent whole-run control; a specific deployed workflow may differ.
- `software-factory` demonstrates a separately tasked direct-artifact reviewer loop; this does not prove institutional audit independence, guaranteed reviewer efficacy, or that arbitrary workflows enable it.
