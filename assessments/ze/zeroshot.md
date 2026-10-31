---
harness_id: zeroshot
project_name: zeroshot
repository: https://github.com/the-open-engine/zeroshot
review_ref: 4c2ed7d5cf3dce968ef7634a2bb49f4382226637
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# zeroshot

## Review boundary

- System in focus: one installed zeroshot native CLI/host/graph execution and its workspace-scoped multi-agent software-change or auto-research organization, including local Active Memory and postmortem agents; not the vendor-hosted Platform organization.
- Purpose and identity: execute user-defined coding/research goals with agent steps, independent review and repair, bounded run state and reusable evidence-backed learning.
- Relevant environment: project/repository tasks, tool/model responses, acceptance/code/security failures, CI/delivery conflicts, competing active memory writers, costly recurring mistakes, changing repository facts and user-defined policy.
- Standard-distribution boundary: first-party Rust native v2 templates, graph/runner/supervisor, exact reviewer and delivery contracts, local ledger and workspace, built-in auto-research agents, Active Memory postmortem specialists/storage/retrieval hooks; independently installed harness CLIs supply model/tool execution.
- Credited operating / distribution surfaces: shipped `software-change` and `auto-research` graph templates, graph dispatch/review branches, accepted/rejected repair round loop, run/lease/cancellation controls, Active Memory specialist reconciliation and scoped future-run injection.
- Adjacent first-party surfaces excluded from ownership: documentation examples and benchmarks, release/build tooling, hosted Platform billing/deployment administration, unrelated Opcore feedback repository, upstream contributor governance and user-supplied custom graph extensions. External Codex/Claude/Copilot/Pi/OpenCode/harness inner model loops are dependencies, not donated first-party autonomy organs.
- Modes considered: local binary, self-hosted Docker target, built-in software-change and auto-research templates, optional push/PR/ship delivery, enabled-by-default Active Memory and configurable review/repair; exact mode-specific rights are separated below.
- Recursion level: one graph-run organization of multiple task/scout/reviewer agents in one workspace, with persistent scoped memory feedback into subsequent runs. Provider and repository ecosystem remain environment/parent inputs.
- Reviewed revision: `the-open-engine/zeroshot@4c2ed7d5cf3dce968ef7634a2bb49f4382226637`, GitHub repository ID 1122859216, intake #2501 / controller #2502 row 5.
- Observation date: 2026-10-31; active Profile 0.2.4 and released Methodology 0.3.7. Structural source review, no live paid-provider run.

## Repository architecture

The pinned [README](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/README.md) describes enforced graph execution with separate worker, acceptance and code reviewers, deterministic revisit-to-worker repairs and bounded durable SQLite history. The [native software-change template](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates.rs) implements this route and the [continuity tests](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/tests/continuity.rs) prove repair returns to the original worker session rather than silently accepting failed reviews. The [auto-research template](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/auto_research.rs) coordinates three scouts, one researcher selecting experiments and a separate fresh reviewer with bounded rounds. [Active Memory guidance](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/docs/guides/active-memory.md) describes four separate post-run maintenance/discovery specialists for graph and repository lessons; the [postmortem implementation](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/postmortem.rs) validates versioned decisions, retries conflicting publication after refreshed evidence, and the [retrieval/hook code](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/hooks.rs) carries admitted lessons into later model/tool contexts. None of these facts proves the correctness of any arbitrary model output or live task success.

## Operational model

An operator supplies a task, model/harness bindings, a graph/profile and delivery policy. The native graph runtime invokes model-driven external harness workers as deliberately distinct decision cells, controls branches, fan-in, retries and immutable run state. Model reviewers own substantive acceptance/code verdicts; trusted graph machinery enforces them and returns feedback to the worker. In the auto-research mode, a model researcher chooses a current experiment from independent scouts and incorporates review feedback. After main graph completion, separate model specialists review evidence of costly work and adapt/retire/discover reusable scoped lessons, admitted by versioned host rules and injected into future runs. Fixed graph enforcement and SQLite authority are not themselves model agency.

## S1 — Operations

- State: A
- Function: implement user-requested code changes or run research experiments with model-directed tool/file actions and return artifacts.
- Disturbance / variety regulated: arbitrary codebase tasks, repository state, model/tool feedback, tests and experiment outcomes.
- Decisive decision or feedback right: instantiated worker/researcher agent selects substantive coding or experiment actions; zeroshot graph invokes and retains the role under a specific runtime binding.
- Decision owner: the first-party configured graph node's autonomous agent role through a supported harness adapter; external harness internals retain lower-level execution but are not separately scored.
- Supporting / enforcement mechanisms: model/harness binding, graph transitions, workspace/capsule, runner, provider session, SQLite ledger and bounded retries.
- Closure path: task input → worker/researcher model/tool action → workspace artifact/experiment evidence → result returned to graph and, after review, revised worker action or accepted output.
- Boundary reachability: `zeroshot run --template software-change` and `auto-research` are built-in supported native CLI/Docker graph modes with first-party runner and first-party role prompts.
- Why this is / is not agent-owned: graph plumbing cannot implement semantic code changes or choose experiments without a model-driven worker; the autonomous operational actor is necessary.
- Evidence: [README](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/README.md); [native_v2_templates.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates.rs); [auto_research.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/auto_research.rs).
- Basis: structural
- Confidence: medium
- Caveats: installed harness CLI and provider/model configuration are required; no live E2E/quality performance was observed.

## S2 — Coordination

- State: C
- Function: attenuate interference between independently active run/postmortem cells that share a scoped lesson store and might overwrite contradictory or stale guidance.
- Distinct S1 units: separately executing runs and their postmortem maintenance/discovery agents, each producing prospective repository/graph advice for the same shared memory scope.
- Inter-S1 disturbance: concurrent updates to a lesson from stale snapshots, resurrecting a retired lesson, incompatible parallel advice replacing a newer record and duplicated overlapping recommendations.
- Attenuating coordination relation: each specialist returns keep/adapt/retire/defer for frozen lesson IDs; host requires expected revisions and atomic publication, rejects conflicting writes, reloads the latest lesson snapshot, then re-invokes model reconciliation rather than accepting last-writer-wins. Same-scope overlap is consolidated; unrelated scopes cannot rewrite each other.
- Feedback into subsequent S1 behaviour: a publication conflict suspends the stale mutation and returns refreshed data to maintenance agents; only successfully reconciled newer cards become injectable guidance into subsequent model/tool sessions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the evidence identifies actual competing independent agent/run modifications of one shared knowledge resource and a conflict-specific reject/reconcile/return path, not merely a datastore or graph edge.
- Disturbance / variety regulated: cross-run retained-guidance collisions and stale-write interference.
- Decisive decision or feedback right: decide how to reconcile a stale/overlapping scoped lesson so concurrent-run advice can coexist or supersede safely.
- Decision owner: first-party optimistic-concurrency and scoped specialist reconciliation constructor; autonomous maintenance judgments are available but the general inter-run arbitration mode remains scoped/composed, not a universal S2 organization.
- Supporting / enforcement mechanisms: versioned SQLite transactions, tombstones, stable IDs, scoped snapshots, conflict detection, specialist result schema and refresh/retry budget.
- Closure path: concurrent postmortem decisions → CAS/version conflict → refreshed scope + specialist reconsideration → atomic accepted lesson revisions → future run retrieval or explicit failed reconciliation.
- Boundary reachability: this is the supported local/Docker Active Memory path described in [guide](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/docs/guides/active-memory.md), implemented in [postmortem.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/postmortem.rs) and [store.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/store.rs).
- Why this is / is not agent-owned: the first-party mechanism explicitly constructs a recoverable S2-specific path; it does not establish broadly agent-owned coordination of every simultaneous run, so the conservative publication is `C`.
- Evidence: [Active Memory](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/docs/guides/active-memory.md); [postmortem.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/postmortem.rs); [store.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/store.rs).
- Basis: structural
- Confidence: medium
- Caveats: conflict witness is shared retained lessons across runs, not all inter-agent workflow interference. Worker/reviewer fanout and graph scheduling alone are not used as S2 proof.

## S3 — Inside-and-now control

- State: A
- Function: manage the current auto-research program and its experiment/review/correction choices across distinct scouting and research S1 units; not all unrelated zeroshot installations.
- Whole-system current view: one auto-research run's three scout proposals, current experiment/report, reviewer verdict and feedback, retained candidate and bounded iteration state.
- Current-control decision scope: select which current approach/experiment to execute, revise work from review evidence, retain accepted result or stop a blocked/inconclusive round.
- Disturbance / variety regulated: competing scout directions, experimental failure, reviewer rejection and incomplete current research commitments.
- Decisive decision or feedback right: the model-driven researcher chooses experiment and revision priorities from scouts and review, while native graph enforces maximum iterations and terminal decisions.
- Decision owner: first-party instantiated researcher Agent in the built-in `auto-research` graph; graph scheduler supplies deterministic execution constraints, and fresh reviewer provides challenge.
- Supporting / enforcement mechanisms: `Par` scout fan-in, researcher continuation session, bounded inner review loop, current state/feedback fields, SQLite run ledger and optional push gate.
- Closure path: three model scout proposals → researcher decision/experiment → fresh reviewer evidence → same researcher revises or accepts → next round's current plan/retained result.
- Boundary reachability: [auto-research native template](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/auto_research.rs) with shipped [researcher instructions](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/auto_research/researcher.md) is built-in, not a user-authored hypothetical graph.
- Why this is / is not agent-owned: model researcher owns current experiment selection and corrective judgment; removing it leaves fixed fan-in/limits but not the substantive cross-scout control choice.
- Evidence: [README auto-research](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/README.md); [auto_research.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/auto_research.rs); [researcher.md](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/auto_research/researcher.md).
- Basis: structural
- Confidence: medium
- Caveats: S3=A is specific to the built-in multi-agent research-program mode. In `software-change`, fixed graph control and reviewer gates alone are not credited as an independent model-driven S3 controller.

## S3* — Complementary audit

- State: A
- Function: test the implementer's outcome through fresh independent acceptance/code reviewers, then force rework on rejection before delivery or successful closure.
- Claim being audited: worker's code meets requested acceptance criteria and code-quality/correctness expectations, not merely that the worker completed a turn.
- Ordinary reporting path: worker writes/edit files, returns output and claims completed implementation in its retained session.
- Complementary access path: separate acceptance and code reviewer nodes run in parallel against the shared workspace, each with its own fresh model session and rubric; their structured verdict/diagnostic inputs are not copied from the worker's self-report.
- Independence boundary: both reviewers start fresh on every pass while implementation/repair uses the same worker session; the native graph gives reviewer roles separate identities and returns both findings.
- Who acts on findings: enforced graph routes rejected reviewer evidence back to original worker; the next pass repeats both independent reviewers. Delivery/CI conflicts may also return through controlled repair and re-review. Acceptance cannot bypass guards with a prose-only assertion.
- Disturbance / variety regulated: incorrect self-reported success, acceptance gaps, code defects, regression and unreviewed delivery changes.
- Decisive decision or feedback right: separately model-driven reviewer decides accepted/rejected criteria and can prevent progression, triggering another worker repair round.
- Decision owner: first-party instantiated independent reviewer/verifier agents for the standard software-change mode; trusted native graph gates/runner enforce their verdicts.
- Supporting / enforcement mechanisms: typed graph signals, `Par` reviewer join, guard routing, bounded global loop budget, retained worker session, fresh reviewer sessions, run ledger and CI/delivery gates.
- Closure path: worker code → fresh acceptance+code review → accepted or rejection diagnostics → worker repair → new review pass → accepted artifact/delivery or bounded honest failure.
- Boundary reachability: the default [software-change template](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates.rs) and [review/repair continuity tests](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/tests/continuity.rs) demonstrate a standard operational path.
- Why this is / is not agent-owned: reviewers independently choose substantive feedback; graph machinery supplies independent session enforcement and corrective return, not semantic acceptance decisions itself.
- Evidence: [README](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/README.md); [native_v2_templates.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates.rs); [continuity.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_templates/tests/continuity.rs).
- Basis: structural
- Confidence: medium-high
- Caveats: independence is of decision sessions/evidence roles, not guaranteed model-provider diversity or exhaustive correctness. User-specified graph/model settings can alter actual review coverage.

## S4 — Outside-and-then intelligence

- State: A
- Function: discover and reconcile costly recurring errors and outdated procedural knowledge so later graph/repository agent work is better adapted to changed evidence.
- External distinction: real repository files and tool receipts, repeated costly failures/rejected review loops, current scope content and changed advice provenance, rather than the just-finished worker's optimistic summary.
- Future / prospective distinction: determine which recurring or newly learned guidance will remain useful across subsequent runs, adapt stale lessons to current source and retire obsoleted/conflicting advice.
- Adaptation option generated: graph and repository discovery specialists propose new procedural cards; separate maintenance specialists keep/adapt/retire/defer all supplied lessons, consolidate overlaps and identify stable recommendations.
- Path back into current capability / S3: versioned accepted cards are stored per graph/node/repository and injected through native pre-tool hooks or graph instructions in **future** sessions, changing model choices in later S1/S3 work without rewriting the authored graph or policy.
- Disturbance / variety regulated: repetition of expensive mistakes, stale memory, changed code/graph context and loss of useful experience between runs.
- Decisive decision or feedback right: maintenance/discovery model specialists judge evidence-backed guidance changes; host validates cost/provenance, revisions and scope before publication.
- Decision owner: standard-distribution postmortem model specialists in separate sessions, automatically enabled by default when Active Memory scopes and postmortem remain enabled; fixed validation/SQLite machinery enforces their decisions.
- Supporting / enforcement mechanisms: tool receipt capture, post-run outcome latch, per-scope indexes, strict cost threshold, version/CAS, bounded context, admission validation, tombstones, retrieval budgets and native hooks.
- Closure path: run evidence/tool receipts → postmortem specialist review/discovery → validated revised scoped lessons → durable store → future run retrieval/injection → later model work and next postmortem reassessment.
- Boundary reachability: the built-in [Active Memory guide](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/docs/guides/active-memory.md) explicitly documents default enabled local/Docker paths; [postmortem.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/postmortem.rs), [native supervisor](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/native_v2_supervisor/postmortem.rs), [retrieval](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/retrieval.rs) and [hooks](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/hooks.rs) are source-backed.
- Why this is / is not agent-owned: specialist agents exercise context-sensitive keep/adapt/retire/discover discretion from actual evidence; host-only ranking/CAS cannot independently decide what lesson remains useful for future work.
- Evidence: [Active Memory](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/docs/guides/active-memory.md); [postmortem.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/postmortem.rs); [reconciliation tests](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/postmortem/tests/reconciliation.rs); [hooks.rs](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/zeroshot/src/active_memory/hooks.rs).
- Basis: structural
- Confidence: medium
- Caveats: postmortem may abstain when evidence is inadequate, can fail independently of completed main graph, and requires working model/harness hooks. Evidence of a closed adaptive mechanism is not proof that a given lesson causally improves future task quality.

## S5 — Policy and identity

- State: —
- Function: no distinct legitimate ultimate-identity/policy conflict adjudicator and authoritative return loop exists within a graph-run organization.
- Disturbance / variety regulated: runtime scopes, model choices, graph contracts, delivery authorization and user approvals are fixed constraints rather than identity-level questions.
- Decisive decision or feedback right: no agent or parent actor is first-party delegated ultimate purpose/identity choice at this recursion.
- Decision owner: user/operator defines graph, tasks, credentials, publishing authority and scope; native runtime enforces these settings.
- Supporting / enforcement mechanisms: graph validation, authored runtime plan, capsules, limits, run ledger, Git/CI policy and memory namespace controls.
- Closure path: an operator can change configuration for later runs, but no outstanding identity-policy matter is routed to a legitimate S5 authority and returned through an explicit governance closure.
- Why this is / is not agent-owned: graph profile names, model persona, user delivery ratification, or managed platform policy do not by themselves constitute identity or ultimate-policy decisions.
- Evidence: [README](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/README.md); [graph reference](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/docs/reference/cluster/graph.md); [Active Memory](https://github.com/the-open-engine/zeroshot/blob/4c2ed7d5cf3dce968ef7634a2bb49f4382226637/docs/guides/active-memory.md).
- Basis: structural
- Confidence: medium-low
- Caveats: bounded absence for the one installed graph-run organization, not a universal claim about the vendor or project maintainers.

### Absence scope — S5

- Surfaces inspected: graph/runtime contracts, role prompts, delivery/approval policy, target namespace/credentials, postmortem scope and OSS/product governance references.
- Plausible first-party paths checked: user graph/profile authoring, high-risk delivery approval, model routing, Active Memory adaptation, project/legal policy and hosted Platform administration.
- Why no material first-party path remains: these set task instructions, approve operational delivery or adapt procedure within already chosen purpose; none is a first-party ultimate-identity conflict and legitimate authoritative return path.

## Distributed OSS parent arrangement

The Open Engine Company and external model providers do not automatically become runtime S5. A user chooses a graph and publication permissions, which are current mission constraints; the automatic postmortem adaptation is S4 within scoped procedural capability, not a change of ultimate organizational identity.

## Self-hosted and non-human modes

Local binary and Docker target expose first-party graph, reviewer and Active Memory components. Model decisions run through configured separately installed harness CLIs. The runtime's deterministic graph gates, scope checks and SQLite publication mechanisms carry model decisions without acquiring autonomous policy ownership.

## Recursion

Worker, reviewer, scouts and researcher are distinct S1 units within one graph-run. A later run using the scoped lesson store creates a cross-run S4 continuity path; the narrow S2 witness regulates their shared memory publication collision, not all possible project interference.

## Variety and escalation

Native graph rejection, retry ceilings, independent review, delivery conflicts, cancellation and unprovable postmortem effects all produce typed control outcomes. Inconclusive or failed postmortem is logged without retroactively claiming main run failure. Such exceptions are not automatically S5 identity disputes.

## Evidence gaps

No live model/provider tasks, Docker target or production CI/merge run were executed; first-party source and deterministic test definitions were inspected. S3 is grounded specifically in built-in auto-research rather than attributing S3 to every fixed software-change graph. S3* has independently instantiated fresh reviewer sessions but not guaranteed diversity of models. S4 is a documented default-enabled, scoped postmortem memory/adaptation loop whose empirical benefit remains unverified here.
