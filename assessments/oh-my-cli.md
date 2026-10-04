---
harness_id: oh-my-cli
project_name: oh-my-cli
repository: https://github.com/qwen-code-dev-bot/oh-my-cli
review_ref: 8dce0123dabfdae34093088281aaeb890e62d4fd
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# oh-my-cli

## Review boundary

- System in focus: the first-party `qwen-code-dev-bot/oh-my-cli` distribution at frozen revision `8dce0123dabfdae34093088281aaeb890e62d4fd`, including its repository-owned coding loop, file/shell tools, approval/folder-trust/sandbox plane, durable sessions and recovery, headless/local-client surfaces, and the repository-owned parent product-development mode defined by `AUTONOMY.md` plus `.autonomy/**` where that parent mode has function-specific closure.
- Purpose and identity: provide a small self-hosted coding-agent CLI that can inspect and modify a workspace through a bounded model/tool loop while preserving explicit local safety and durable run evidence; at the parent product-development recursion, keep the product adapting through an evidence-bound autonomous queue under protected human governance.
- Relevant environment: user objectives, workspace files and Git state, shell/tool results, provider responses, approval and trust decisions, durable session/recovery evidence, user/community product evidence, dogfood findings, GitHub Issues/PRs/checks, and governance-maintainer decisions.
- Standard-distribution boundary: the shipped CLI agent loop, tools, safety plane, session/recovery/headless/Desktop/local-web surfaces, repository-owned autonomy contract/configuration, and repository-owned coordinator procedure are inside. The model provider, host scheduler that invokes the documented coordinator tick, GitHub service, host OS/sandbox backend, and independent governance maintainer are environment/parent dependencies; their decisions are credited only where a first-party return path is explicitly closed.
- Credited operating / distribution surfaces: `README.md`; `src/agent.ts`; tool/safety/session/recovery modules; `src/subagents.ts` and `src/workspace-guard.ts` as inspected but not assumed runtime-reachable; change-review/scorecard/evidence surfaces; `AUTONOMY.md`; `.autonomy/product.yml`; `.autonomy/issue-policy.yml`; `.autonomy/quality-gates.yml`; `.autonomy/prompts/coordinator.md`; `.github/workflows/governance.yml`; `.github/workflows/ci.yml`; and `.github/workflows/issue-triage.yml`.
- Adjacent first-party surfaces excluded from ownership: tests and evidence archives as such; scorecards or queues without returned decisions; dormant/unwired components; GitHub/host scheduling internals; maintainer activity unrelated to the explicit protected-governance path; and generic external review.
- First-party operating / deployment modes considered: interactive CLI; headless `-p`/JSON automation; durable/resumed sessions; approval/folder-trust/sandbox modes; recovery/checkpoint/evidence modes; Desktop/local web surfaces; and the documented parent product-development coordinator mode with user/community/self-discovery intake and protected governance.
- Recursion level: the base recursion is one oh-my-cli coding session, whose model-backed coding actor is the operational S1. S4 and S5 are published as explicit parent modes at the product-development recursion because their decisive rights live above the coding session and return through first-party product/governance paths. Dormant subagent machinery is not promoted into a lower-recursion multi-S1 organization.
- Reviewed revision: `8dce0123dabfdae34093088281aaeb890e62d4fd`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

oh-my-cli ships a concrete model/tool coding loop. `src/agent.ts` bounds a run to 30 model rounds, presents first-party tools, executes tool calls under command policy, approval, folder-trust and sandbox constraints, records results in the transcript and continues with the updated evidence. The loop also has provider retry handling, spend/turn/wall-time/tool-call caps, cancellation and context-pressure compaction.

Sessions are durable JSONL artifacts with resume, compaction, export, undo/redo and deterministic recovery support. Headless execution exposes a versioned event protocol plus summaries, scorecards and evidence archives. These surfaces materially improve observability and recoverability, but reporting/recovery artifacts are not treated as S3*, S4 or S5 merely because they preserve evidence.

The frozen repository also contains substantial subagent machinery. `SubagentManager` can bound concurrent delegated children and `workspace-guard.ts` explicitly models the concurrent-writer collision that worktree isolation should prevent. At this exact revision, however, repository code search finds `SubagentManager` only in its definition and tests, with no standard CLI production wiring that makes the manager a reachable model-owned organization. The implementation is therefore inspected as a plausible path but not published as positive S2.

Separately, the repository ships a product-development control surface. `AUTONOMY.md` declares durable product direction and a permanently installed development-side coordinator. The coordinator contract accepts three evidence sources—promoted user reports, bounded community research and reproduced self-discovery/dogfood—normalizes them into trusted execution Issues, selects work by explicit priority, develops it through branch/PR/checks/merge, then requires post-merge dogfood. Protected governance paths cannot be changed by the development Bot: governance changes can only be proposed and must be approved/merged by the independent governance maintainer. Those two parent paths are the basis of the S4 and S5 publication states below.

Primary evidence:

- [`README.md`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md)
- [`src/agent.ts`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/src/agent.ts)
- [`src/subagents.ts`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/src/subagents.ts)
- [`src/workspace-guard.ts`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/src/workspace-guard.ts)
- [`AUTONOMY.md`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/AUTONOMY.md)
- [coordinator contract](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/prompts/coordinator.md)
- [`issue-policy.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/issue-policy.yml)
- [`quality-gates.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/quality-gates.yml)
- [`governance.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.github/workflows/governance.yml)

## Operational model

A normal coding session receives the user prompt, current transcript and workspace context. The model chooses an exposed tool or returns text. oh-my-cli applies policy/trust/approval checks, executes permitted actions, records the result and invokes the model again until the task ends or a bounded stop condition is reached. Durable session and recovery machinery allows later continuation without changing who owns the coding judgment.

At the product-development parent recursion, the repository documents a different loop. The coordinator first reconciles Git/GitHub/ledger state, then chooses exactly one bounded action. External user reports, registered community evidence and reproduced dogfood findings can become normalized Bot-authored execution Issues after trust, fit, deduplication and reproduction checks. Accepted work is implemented, reviewed against quality gates, merged and dogfooded; later product runs therefore inherit the changed capability.

Identity-level governance is intentionally separated from that adaptation loop. `AUTONOMY.md`, `.autonomy/**`, workflows and CODEOWNERS are protected. The development Bot may open a governance proposal but cannot apply those changes; `.github/workflows/governance.yml` rejects protected-path PRs authored by the Bot. Only the independent governance maintainer can make the ultimate policy decision, after which the changed protected contract governs future coordinator/product operation.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work through a bounded model/tool loop inside the selected workspace.
- Disturbance / variety regulated: heterogeneous user objectives, repository structure, file/Git state, shell/tool output, provider errors, context pressure, approval/trust boundaries and implementation failures.
- Decisive decision or feedback right: choose what evidence to inspect, which permitted file/shell/tool action to execute next, how to revise work from returned results and when to finish.
- Decision owner: the model-backed coding actor in the first-party `src/agent.ts` loop.
- Supporting / enforcement mechanisms: first-party coding tools; command policy; folder trust; approval modes; sandboxing; provider retry; run/spend/tool caps; durable sessions; compaction; recovery; headless event protocol.
- Closure path: user task + session/workspace context → model selects action/tool → oh-my-cli gates and executes it → result is appended to the active transcript → subsequent model round sees the result → next action or terminal response.
- Boundary reachability: the ordinary CLI and headless prompt modes directly execute this loop; no downstream orchestration layer is required.
- Why this is / is not agent-owned: deterministic safety/runtime machinery remains if the model is removed, but the open-ended coding decision that selects and sequences work disappears.
- Evidence: [`src/agent.ts`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/src/agent.ts); [`README.md`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference and OS/sandbox facilities are dependencies; the credited organization is oh-my-cli's first-party decision/tool/feedback path.

## S2 — Coordination

- State: —
- Function: no runtime-reachable same-recursion inter-S1 coordination function was established in the frozen standard distribution.
- Disturbance / variety regulated: `workspace-guard.ts` explicitly identifies concurrent mutating agents sharing a workspace as a destructive-write/corruption disturbance, and `SubagentManager` contains a relation capable of preventing that launch.
- Decisive decision or feedback right: not established in a standard production path at the frozen revision.
- Decision owner: not established.
- Supporting / enforcement mechanisms: bounded `SubagentManager`; queued/running/cancelled child states; shared cost/spawn caps; workspace identity; shared-workspace launch refusal; tests exercising sibling/parent lifecycle.
- Closure path: not applicable in the assessed standard runtime because the manager/guard path is not wired into the production CLI model/tool surface at the frozen ref.
- Why this is / is not agent-owned: the repository contains an S2-capable mechanism, but exact-ref code search found the manager referenced by its module/tests rather than a normal reachable coding-session composition. Constructor capability without standard boundary reachability is not published as positive S2.
- Evidence: [`src/subagents.ts`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/src/subagents.ts); [`src/workspace-guard.ts`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/src/workspace-guard.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: future or external composition that wires these components could support S2; this review is frozen at the specified revision.

### Absence scope

- Surfaces inspected: coding loop/tool wiring; subagent manager; workspace guard; task runtime; headless/TUI surfaces; integration/unit tests for subagents.
- Plausible first-party paths checked: parallel delegated children; shared-workspace collision guard; worktree leasing; task runtime; parent/sibling cancellation and shared child budgets.
- Why no material first-party path remains: the strongest S2-capable code exists as repository machinery but is not reachable from the standard production coding-session path at this frozen revision, so no closed inter-S1 feedback loop can be credited.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function was established at the coding-session recursion.
- Disturbance / variety regulated: spend, turns, elapsed time, tool-call count, background tasks, approvals, recovery and session state are bounded/tracked, but those mechanisms do not establish a whole-system operational portfolio with substantive current-control authority.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: run/spend/tool caps; task runtime; cancellation; recovery; active/waiting states; approval/folder-trust policy.
- Closure path: not applicable; no whole-current state → resource/commitment/priority intervention → changed multi-S1 operation loop was reconstructed.
- Why this is / is not agent-owned: hard caps and task states enforce predefined/operator-selected constraints; they do not create an autonomous S3 owner. The parent development coordinator is a different recursion and its adaptation/governance paths are classified by function below rather than relabeled S3.
- Evidence: [`src/agent.ts`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/src/agent.ts); [`README.md`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operational supervision is extensive; the negative result is specifically about Profile S3.

### Absence scope

- Surfaces inspected: run budgets/caps; task lifecycle; recovery; goal/workflow surfaces; TUI/headless status; autonomy coordinator states.
- Plausible first-party paths checked: runtime caps as resource control; background task state as whole-current view; coordinator lease/priority state as current control.
- Why no material first-party path remains: base runtime mechanisms enforce one session's limits, while the parent coordinator primarily owns product adaptation lifecycle. No distinct coding-organization S3 closure meeting whole-system current-control requirements was established.

## S3* — Complementary audit

- State: —
- Function: no standard runtime complementary autonomous audit path sufficiently independent from the producing coding S1 was established.
- Disturbance / variety regulated: scorecards, change review, evidence archives, verification modes and CI can reveal errors or regressions, but their existence does not by itself create S3*.
- Decisive decision or feedback right: not established inside the active coding-session organization.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic change review; task verification; run scorecards; evidence archives; CI handoff/delivery briefs; parent development self-review gate.
- Closure path: not applicable at the assessed coding-session recursion; the reviewed reporting/checking modes are separate inspection/reporting surfaces and no standard path was found that injects an independent semantic audit judgment back into the current producer loop.
- Why this is / is not agent-owned: evidence collection and deterministic verdicts are mechanisms. Parent development self-review belongs to a separate product-development organization and Methodology 0.3.x does not publish parent-mode notation for S3*.
- Evidence: [`README.md`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md); [`quality-gates.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/quality-gates.yml).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the development-side governance requires independent self-review before merge, but that does not donate S3* to an ordinary oh-my-cli coding session.

### Absence scope

- Surfaces inspected: change-review; task verification; run scorecards; evidence archive/export/verification; CI handoff/delivery brief; development quality gates; coding loop.
- Plausible first-party paths checked: deterministic review as audit; scorecard regression gate; evidence bundle verification; independent development self-review.
- Why no material first-party path remains: runtime inspection/reporting surfaces lack a returned independent semantic auditor in the ordinary coding loop, while the separate development organization is outside the selected S3* publication recursion.

## S4 — Outside-and-then intelligence

- State: P
- Function: turn external and future-relevant product evidence into selected, implemented and dogfooded adaptations that change the capability of later oh-my-cli operation.
- Disturbance / variety regulated: changing user needs, community/competitor developments, regressions and usability/reliability findings discovered through later operation can make the current product capability inadequate.
- Decisive decision or feedback right: at the parent product-development recursion, reconcile evidence, decide whether a finding becomes trusted executable work, select the next adaptation under the priority/lease policy, and carry an accepted option through implementation and merge.
- Decision owner: the first-party parent product-development coordinator organization. The base coding-session actor does not own this prospective product-adaptation function.
- Supporting / enforcement mechanisms: `AUTONOMY.md`; permanent coordinator contract; bounded community registry; user-promotion policy; reproduced self-discovery/dogfood intake; normalized Bot-authored execution Issues; single active lease; quality gates; PR/merge lifecycle; targeted post-merge dogfood.
- Closure path: external user report, registered community distinction or reproduced dogfood finding → coordinator triages/deduplicates and develops a normalized adaptation option → trusted Issue enters priority/lease selection → accepted option is implemented/tested/reviewed/merged → targeted dogfood confirms the changed user path → later product runs execute the changed capability.
- Boundary reachability: the repository explicitly ships the parent contract/configuration and publicly describes the product as developing itself through the autonomous evidence-bound queue; `AUTONOMY.md` requires the single coordinator loop to remain installed indefinitely. The host cadence/invocation is an execution dependency, while the adaptation decisions and closure contract are repository-owned.
- Why this is / is not agent-owned: relative to an ordinary coding session the adaptation authority is at the parent product-development recursion. No separate first-party base-session S4 mode is established, so Methodology 0.3.6 publishes the closed parent capability as standalone `P`.
- Evidence: [`AUTONOMY.md`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/AUTONOMY.md); [coordinator contract](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/prompts/coordinator.md); [`issue-policy.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/issue-policy.yml); [`quality-gates.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/quality-gates.yml).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the portable coordinator's host/scheduler is not implemented by the ordinary CLI entry point; the positive mapping relies on the explicitly shipped and publicly claimed first-party parent operating mode, not on scorecards, queues or memory alone.
- External distinction: promoted user reports, the bounded community-source registry and observed post-merge/global dogfood findings supply distinctions outside the current product implementation.
- Future / prospective distinction: the coordinator evaluates whether those distinctions justify reusable product changes for later users/runs, rather than merely reacting inside the current coding task.
- Adaptation option generated: a normalized, deduplicated Bot-authored execution Issue with problem, user value, scope, acceptance criteria, test/dogfood plan, risks and dependency position.
- Path back into current capability / S3: the parent coordinator acquires an accepted Issue, implements it on a product branch, passes required checks/self-review, merges it and completes targeted dogfood; the changed default-branch product becomes the capability used by subsequent operation.

## S5 — Policy and identity

- State: P
- Function: preserve the product's durable identity, autonomy boundaries and ultimate governance policy by reserving protected-governance changes to legitimate independent maintainer authority.
- Disturbance / variety regulated: the autonomous development Bot could otherwise weaken its own safety/governance constraints, accept untrusted instructions as authority, alter protected quality gates or redefine product direction while optimizing local development goals.
- Identity / ultimate-policy issue: whether and how the durable product contract, autonomous-development authority, protected paths, governance workflow and quality/safety policy may change.
- Ultimate authority in each claimed mode: Parent (`P`) — the independent governance maintainer is the legitimate ultimate authority. The development Bot may propose but is explicitly forbidden to apply or merge governance changes.
- Return-to-operation path: governance issue arises → development Bot may create a `governance-proposal` only → independent maintainer reviews/decides and, when accepted, merges the protected change → later coordinator ticks are required to reread `AUTONOMY.md` and every `.autonomy/*.yml` file and operate under the changed authoritative contract.
- Decisive decision or feedback right: approve/reject and merge identity/ultimate-policy changes to `AUTONOMY.md`, `.autonomy/**`, `.github/workflows/**` and `.github/CODEOWNERS`.
- Decision owner: independent governance maintainer at the parent recursion.
- Supporting / enforcement mechanisms: protected-path list in `AUTONOMY.md` and `quality-gates.yml`; Bot proposal-only rule; `.github/workflows/governance.yml` rejection of Bot-authored protected-path changes; CODEOWNERS/GitHub review/merge boundary; coordinator's mandatory contract reread.
- Closure path: identity/policy tension → proposal reaches independent governance maintainer → maintainer decides and merges/rejects → approved protected contract becomes repository authority → every subsequent coordinator tick rereads and follows that returned policy.
- Boundary reachability: protected governance files and the enforcing GitHub workflow are shipped first-party surfaces, and the coordinator explicitly recognizes only the independent maintainer as governance authority; no ordinary task approval is being promoted to S5.
- Why this is / is not agent-owned: the development Bot is structurally prevented from self-authorizing changes to the rules that define its identity and authority. Ultimate policy therefore remains with the legitimate parent maintainer and is published as `P`, not `A` or `C`.
- Evidence: [`AUTONOMY.md`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/AUTONOMY.md); [coordinator contract](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/prompts/coordinator.md); [`quality-gates.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.autonomy/quality-gates.yml); [`governance.yml`](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/.github/workflows/governance.yml).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this S5 state belongs to the product-development parent mode. Ordinary per-command approval, sandbox denials and static CLI policy are not the S5 witness.

## Distributed OSS parent arrangement

oh-my-cli explicitly separates the autonomous development Bot/coordinator from an independent governance maintainer. This is not inferred from generic OSS contribution activity: the split is encoded in the tracked autonomy contract and enforced by a protected-path workflow. The parent mode supplies S4 product adaptation and S5 ultimate governance to the standard distribution while leaving ordinary coding sessions at the lower recursion.

The host mechanism that periodically invokes the coordinator is not credited as an organizational owner. Its role is cadence/execution support; the repository-owned contracts determine intake, adaptation selection, execution lifecycle, governance boundaries and return paths.

## Self-hosted and non-human modes

The normal CLI can run interactively or headlessly with strong local safety and recovery. Those modes preserve autonomous S1 but do not by themselves create the parent functions. Separately, the documented autonomous development coordinator is a non-human parent operating mode for product adaptation, while identity/ultimate policy remains parent-human-governed through the protected governance path.

## Recursion

At the lower recursion, one coding session is the focal viable operational unit and closes S1. Dormant subagent components are not treated as a proven recursive multi-S1 organization because production reachability was not established at the frozen ref.

At the higher product-development recursion, the persistent coordinator/queue/PR/dogfood organization adapts the product over time. S4 is therefore published as a parent mode relative to the coding harness. S5 remains one level higher in decisive authority: governance-policy changes must reach the independent maintainer and return through the protected repository contract.

## Variety and escalation

The coding runtime attenuates local variety through folder trust, approvals, sandboxing, deterministic command policy, budgets, retries, session recovery and evidence preservation. The parent adaptation organization attenuates product-development variety through source normalization, deduplication, priority, a single lease, quality gates, failure quarantine and post-merge dogfood. Identity-level exceptions are escalated outside the development Bot to the independent governance maintainer.

## Evidence gaps

No `?` state is required. The exact frozen revision provides enough primary evidence to establish S1 and the explicit parent S4/S5 modes, while also bounding the strongest false-positive risks: dormant subagent machinery is not treated as runtime S2, run/task status is not promoted to S3, and scorecards/evidence/review artifacts are not treated as S3* without a returned independent audit loop.

The main caveat is operational hosting of the portable product-development coordinator: the repository defines and publicly claims the permanent parent mode, but the host scheduler/invocation mechanism is external to the ordinary CLI source. That dependency does not own the S4/S5 decisions credited here.

## Assessment summary

oh-my-cli closes autonomous S1 through its first-party bounded coding loop. The frozen standard coding-session runtime does not establish reachable same-recursion S2, whole-current S3 or complementary runtime S3*. The repository additionally exposes a distinct first-party product-development parent mode: an evidence-bound coordinator closes prospective S4 adaptation, while protected governance reserves S5 identity/ultimate-policy authority to the independent maintainer and returns approved policy to subsequent operation.

**Vector:** A · — · — · — · P · P
