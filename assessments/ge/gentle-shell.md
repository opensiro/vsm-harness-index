---
harness_id: gentle-shell
project_name: gentle-shell
repository: https://github.com/Gentleman-Programming/gentle-shell
review_ref: 407404372516ac0e27fc63e22ed08344f3f64c90
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: P
---

# gentle-shell

## Review boundary

- System in focus: one installed `gentle-pi` package (product named `gentle-shell`) within a supported Pi coding-agent session, whose model parent commissions focused children and whose user owns repository development policy. The recursion is the local workspace/session, not the organization publishing `gentle-pi` or its separate Gentle AI runtime.
- Purpose and identity: perform coding and associated repository tasks under recoverable ODD, optionally explicit SDD, bounded subagent delegation and independently inspectable review evidence.
- Relevant environment: changing target repositories, concurrent subagent workloads, overlapping remediation in the same worktree, tool/test results, consent, user corrections, provider errors, verification findings and changes to durable skills or local project policy.
- Standard-distribution boundary: packaged `gentle-pi` Pi extension, bundled prompts/skills, `subagent_*` execution, local agent/task persistence, runtime guardrails, optional native review adapter and interactive TUI. Stock supported Pi runtime is a required external host for standard operation.
- Credited operating / distribution surfaces: `extensions/{gentle-agents,gentle-ai,gentle-shell,skill-registry,gentle-todo}.ts`, `lib/{agents-runner,agents-protocol,agents-view,review-session-standing-permission,background-subagents-policy}.ts`, `assets/orchestrator*.md`, shipped skills and runtime policy/approval routes.
- Adjacent first-party surfaces excluded from ownership: separate Go `gentle-ai` review authority and risk engine (called through a packaged adapter, not credited as the Pi extension's decision owner), optional separately installed `gentle-engram` persistent memory, optional `pi-intercom`, `bench`/tests/fixtures, historical graph replay, published development/release machinery and external GitHub organization governance. Explicit user-held decision rights in the local package still count as parent mode when closed.
- First-party operating / deployment modes considered: inline Pi coding work, model-parent subagent task/background execution, local session/TUI task inspection and intervention, opt-in ODD and user-requested SDD, externally delegated native review, stored project/global runtime guardrails, shipped skill-audit/apply mode and skill-registry reindexing. Optional external memory absent by default.
- Recursion level: individually executing Pi coding child/parent actions are S1 cells; task-manager queue and worktree constraints are bounded S2; model parent and attended user direct the current local-session task portfolio; the user retains enduring permission and workflow-policy authority.
- Reviewed revision: [`Gentleman-Programming/gentle-shell@407404372516ac0e27fc63e22ed08344f3f64c90`](https://github.com/Gentleman-Programming/gentle-shell/tree/407404372516ac0e27fc63e22ed08344f3f64c90), frozen by [batch #1884](https://github.com/opensiro/vsm-harness-index/issues/1884). The README's transition to the `gentle-pi` package name and release descriptions do not repin the assessment.
- Observation date: 2026-10-23; source/config/docs and deterministic test-code inspection only, no live Pi subagent, LLM provider or benchmark execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`gentle-pi` is a Pi extension package, not a standalone model runtime. It integrates the host's model-driven tool loop with packaged parent delegation instructions. `gentle-agents.ts` registers a first-party `subagent_*` tool family, launching isolated `pi --mode rpc` child processes and persisting task records/receipts. It exposes child `status`, `result`, `continue`, `send_message`, `cancel` and TUI controls. The parent is instructed to select scope and task topology; one focused writer owns changes on ordinary ODD tasks, while scout/context and verification agents provide bounded supporting work. The runner enforces a configured concurrency ceiling and specifically refuses launching a second pending/running native `sdd-remediate` child in the same worktree.

Separate review transport is deliberately thin. `gentle-ai.ts` forwards typed tokens and scoped frozen prompts to in-process reviewer completions, but the external packaged Go Gentle AI binary supplies ordinary review lifecycle, candidate freeze, risk choices, authority, repair and admission semantics. A Pi reviewer completion does not independently inspect live repository state or choose its own review authority. Review outcome is informational; ordinary user/repository policy decides delivery. The parent/delegated verifier checks ordinary coding outputs and claims, not the parent model's portfolio-management judgment.

Persistent first-party policies resolve project/global `runtime-guardrails.json` and `background-subagents.json`; malformed configurations fail safe, and an interactive owner can authorize or refuse sensitive/remediation actions. Separately, the shipped skill-improver can model-audit and propose durable changes to `SKILL.md`, but defaults to **audit-only** and can only edit after the user expressly asks for application. Skill-registry scans and indexes revised skills for later tasks. This is a bounded parent-directed prospective capability loop, not an always-on autonomous learning system. Engram persistence is a separate optional package and is excluded from first-party default S4 evidence.

Primary sources: [package/install identity](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/package.json), [subagent host](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/extensions/gentle-agents.ts), [child runner](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/lib/agents-runner.ts), [delegation contract](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/assets/orchestrator-delegation.md), [review ownership statement](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/docs/review-integration.md).

## Operational model

The core S1 act is a model-selected repo inspection/edit/test action in an installed Pi session or separately executing child. The Pi parent is instructed to hand off bounded sub-tasks, uses first-party task/status/cancel tools and receives child evidence; the user may inspect and change this current task set. The worktree duplicate-remediation guard is concrete cross-cell interference attenuation, although it is deterministic, not an autonomous inter-worker coordination planner. The external Go provider's authority semantics are not attributed to the Pi extension. Product claims, illustrations and unexecuted optional companions are not measured performance or operational ownership evidence.

## S1 — Operations

- State: A
- Function: execute scoped coding and repository tasks, choosing inspection, edit, verification and subsequent repair actions based on results.
- Disturbance / variety regulated: ambiguous change requests, unknown files, tool failures, failing tests, incomplete output and parent corrections.
- Decisive decision or feedback right: supported Pi model tool loop and first-party focused worker definitions choose what to read/write/run and how to revise the next step.
- Decision owner: parent or focused Pi worker model at the task level, subject to bounded edit and consent rules.
- Supporting / enforcement mechanisms: stock Pi agent host, configured packaged worker definitions, `pi --mode rpc` execution, first-party task/receipt store and result return.
- Closure path: user-scoped goal → model chooses tool/child actions → observes tool/check results → revises or returns evidence → parent accepts, redirects or reports partial work.
- Boundary reachability: default installed `gentle-pi` extends Pi's supported native model loop and registers actually executable subagents; no evaluator-only or mocked agent is needed for the published execution route.
- Why this is / is not agent-owned: the model's choice among investigation/edit/repair actions is discretionary; tool policy bounds effects but does not mechanically select code actions.
- Evidence: [packaged Pi extension](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/package.json), [actual child process launcher](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/lib/agents-runner.ts), [delegated writer contract](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/assets/orchestrator-delegation.md#L220-L250).
- Basis: first-party installable runtime and model-driven worker decision closure.
- Confidence: high for structural action ownership, untested performance.
- Caveats: Pi SDK and model provider are normal product dependencies; no live agent run was made in this review.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference between independently running S1 agents in a shared clone/worktree, particularly duplicate concurrent privileged remediation.
- Disturbance / variety regulated: a new remediation agent racing an existing queued or live remediation actor in the same worktree, and finite child process slots.
- Decisive decision or feedback right: the runner rejects a conflicting same-worktree `sdd-remediate` launch and defers concurrent work to a bounded queue. The model parent can respond to the refusal, but no autonomous S2 conflict-arbitration judgment is established.
- Decision owner: deterministic worktree-scoped admission rule and configured queue cap; parent model has a potential orchestration interface but the decisive collision check is fixed code.
- Supporting / enforcement mechanisms: `AgentRunner.run`, task store, worktree-root validation, same-`cwd` remediation check, queue `pump`, per-child cancellation/status receipts.
- Closure path: second S1 remediation launch asks for same worktree → first-party runner detects active conflicting remediation → rejects instead of starting → parent receives error and must preserve/cancel/wait for existing work → later launch may proceed once no actor holds that worktree lane.
- Boundary reachability: native remediation launch flows through `gentle-agents.ts` and `AgentRunner.run` with the same-worktree collision guard, not just a protocol schema or maintainer test.
- Why this is / is not agent-owned: prevention of inter-worker resource/correction collision is real, but fixed admission and limits rather than a situated agent decide the conflict; `C` is bounded to the existing S2 relation, not generic delegation.
- Distinct S1 units: independent `pi --mode rpc` child remediation agents on separately queued requests; each would otherwise be empowered to edit/test within the same target worktree.
- Inter-S1 disturbance: overlapping edits, correction/review artifacts and uncertain ownership when both remediation workers target the same repository state.
- Attenuating coordination relation: one privileged remediation lane per worktree plus queue/resource admission; a second worker is refused until ownership is resolved.
- Feedback into subsequent S1 behaviour: refused launch cannot start an interfering actor and returns a specific message to the parent; after cleanup the next child starts under the remaining scope.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: unlike task-list rendering, this check recognizes and blocks a *specific clash in authority over shared worktree changes* between separate workers. Other subagent status/ACK paths alone would not qualify.
- Evidence: [deduplicating admission guard](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/lib/agents-runner.ts#L385-L407), [remediation scope authorization](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/extensions/gentle-agents.ts), [subagent lifecycle](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/docs/gentle-shell.md#L139-L175).
- Basis: shipped narrow cross-S1 interference attenuator without autonomous arbitration owner.
- Confidence: moderate: clear conditional code path, limited to `sdd-remediate` requests and not all repository writers.
- Caveats: `max_concurrency` alone would only be generic resource limiting; the worktree-specific duplicate remediation refusal is the material positive witness. No conflict-free deployment was empirically tested.

## S3 — Inside-and-now control

- State: A(P)
- Function: hold current accountability over the bounded parent-session development campaign: select child responsibilities, inspect their progress, stop/redirect unfinished work and reconcile outcomes.
- Disturbance / variety regulated: divergent child results, changed user scope, stalled worker, ambiguous verification, time/cost pressure and multiple current commitments.
- Decisive decision or feedback right: model parent chooses when to delegate, who maps/writes/verifies and what to do with returned evidence. The attended human owner can separately inspect all child tasks of the session, stop an owned active child or steer new scope/next work.
- Decision owner: model parent in standard agentic orchestration mode (`A`); interactive user as legitimate local workflow parent (`P`) through supported TUI/turn controls.
- Supporting / enforcement mechanisms: delegated work-unit contracts, `subagent_run`/`status`/`result`/`cancel`/`send_message`, task widget/overlay, ownership checks, result events that initiate a parent turn.
- Closure path: parent sees task plan and child status → selects/scopes writer, verifier or changed action → registered task executes or stops → child outcome/event returns to parent task context and updates current plan/delivery.
- Boundary reachability: shipped `assets/orchestrator-delegation.md` injects parent-mode guidance and the installed `gentle-agents.ts` registers real actionable tools; TUI shows active same-session tasks and provides stop/scope navigation to the human.
- Why this is / is not agent-owned: the parent model judges *which work to hand off or repair* in relation to other commitments, not only mechanically queues known inputs; human task intervention is a separate explicitly supported mode.
- Whole-system current view: for the chosen recursion, `subagent_list_tasks`, `status`, `result` and the task overlay cover current own-session workers, queued/running state and retained outcomes; cross-session peers are presence-only and not claimed as a whole distributed enterprise view.
- Current-control decision scope: delegation topology, worker/verification assignment, stop, continue and reconciled delivery for the current session's campaign, as opposed to generic concurrency/timeouts.
- Evidence: [parent orchestration contract](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/assets/orchestrator-delegation.md), [runtime tools](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/extensions/gentle-agents.ts), [parent task control and UI](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/docs/gentle-shell.md#L139-L174).
- Basis: scoped current-portfolio agentic control and distinct attended human intervention, not broad cross-repository strategic planning.
- Confidence: moderate because the model is prompted to own reconciliation but live compliance is not evaluated.
- Caveats: the local-session view excludes other process's action authority; an ACK from a separate session is not completion or control.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Pi parent coding model | multi-file request, child report, failed verification or changed requirements | chooses scoped work/verification/stop; first-party child tools enact and return results | `assets/orchestrator-delegation.md`; `extensions/gentle-agents.ts`; `lib/agents-runner.ts` |
| Parent (`P`) | local interactive user | same-session active-task observation and revised requirements | stops owned child or steers new request via TUI/turn; current work changes | `docs/gentle-shell.md`; `extensions/gentle-agents.ts` |

## S3* — Complementary audit

- State: —
- Function: separately audit S3's live parent orchestration/portfolio-management assertions and return management correction through an independent evidence channel.
- Disturbance / variety regulated: errors in allocation, supervising, prioritizing or reconciling the parent-managed set; no S3-audit closure established.
- Decisive decision or feedback right: native review lenses, refuter and verification concern *the exact code-change candidate*, not independent judgments about the parent session's management choices; their lifecycle and risk classification additionally belong to the separate Go provider.
- Decision owner: no independent S3-audit decision owner in the assessed Pi-extension local-recursion mode.
- Supporting / enforcement mechanisms: optional candidate-frozen reviewer completions, delegated verifier and immutable review status/receipts from external provider.
- Closure path: not applicable as S3*; artifact findings return to delivery/repair, not a separate evaluation of S3's allocation or intervention claims.
- Why this is / is not agent-owned: genuinely separate review of a code diff is important S1 acceptance evidence, but neither its claim nor independent access is directed at the S3 owner's management reality.
- Evidence: [provider review ownership](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/docs/review-integration.md), [delegated verification boundary](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/docs/delegated-verification.md), [native authority map](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/docs/native-authority-architecture.md).
- Basis: bounded negative at local parent-session portfolio recursion.
- Confidence: high for inspected reviews, moderate for other unenumerated external companion integrations.
- Caveats: excludes external Go provider as an independent organizational function; even including its ordinary diff audit would not by itself constitute S3-management audit.

### Absence scope

- Surfaces inspected: `docs/{review-integration,delegated-verification,native-authority-architecture}.md`, Pi reviewer completion/adapter path, parent delegation, task-store and TUI status.
- Plausible first-party paths checked: independent reviewer/refuter/validator, parent spot-check, task history, risk assessment and user-visible agent activity panel.
- Why no material first-party path remains: all checked reviewers judge output correctness or task-level permissions, or display information to the very S3 controller whose actions require auditing. None independently forms a S3-control finding and returns it for management correction.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: assess skill deficiencies seen during work and prepare improvements to reusable future worker capability; in an explicit parent mode accept and write improvements for later projects/tasks.
- Disturbance / variety regulated: drifting task methodologies, outdated or conflicting skill activation instructions, cumbersome skill bodies and recurring retrieval/usage mistakes.
- Decisive decision or feedback right: model-led shipped `skill-improver` generates bounded audit findings/proposed rewrites (`C`), but it defaults to audit-only. A human asking to apply changes authorizes actual writing of improved `SKILL.md`, which the registry reindexes for later use (`P`). No automatic autonomous future-capability adoption or self-selected learning cadence was established.
- Decision owner: assistant model for candidate skill auditing; local human owns the distinct affirmative future-capability application decision.
- Supporting / enforcement mechanisms: packaged `skills/skill-improver/SKILL.md`, style gate, allowlisted edits, skill registry scanner/watch and project-vs-global precedence.
- Closure path: evidence from existing skill usage/audit → model identifies a reusable skill problem and a revised form → person explicitly requests apply → persisted `SKILL.md` changes → `skill-registry` notices/scans revision → later task loads matching updated instruction.
- Boundary reachability: the improver and registry are both shipped first-party skills/extensions; no Engram installation is required for filesystem skill reuse. The human apply mode is not the default; no autonomous S4 owner is implied.
- Why this is / is not agent-owned: the proposed content is model-authored but selecting whether durable methodology changes govern future tasks is a human decision, so the positive base is only constructor `C`, with closed explicit parent mode `P`.
- External distinction: observed deficiencies in actual on-disk skill instructions, task audit outcomes and user-supplied correction requirements—not the current worker merely retrying its patch.
- Future / prospective distinction: changing skill activation/format affects later independent tasks by changing their available procedure, not just resolving the current deliverable.
- Adaptation option generated: recommended corrections to skill metadata, trigger, structure, rules and decision table; safe apply may rewrite the skill and refresh the index.
- Path back into current capability / S3: updated skill file becomes the new source of truth, indexed at `.atl/skill-registry.md` and routed into subsequent delegated work.
- Evidence: [first-party skill improver](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/skills/skill-improver/SKILL.md), [registry operational skill](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/skills/skill-registry/SKILL.md), [actual file-scanning registry extension](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/extensions/skill-registry.ts), [companion-memory boundary](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/README.md).
- Basis: narrow first-party agent-proposal plus user-approved prospective procedural adaptation; no claim of autonomous ongoing learning.
- Confidence: moderate; a supported apply protocol and future registry ingestion, not observed actual post-edit gain.
- Caveats: skill-improver is invoked for requested skill improvement, not passively after every run; Engram and external adaptive memory products are excluded. This does not establish unsupervised S4=A.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | model skill audit/proposal plus dormant apply branch, with human approval missing for autonomous use | explicit skill-audit task | proposes first-party prospective improvements, no autonomous decision to install | `skills/skill-improver/SKILL.md` |
| Parent (`P`) | local human asking for application | audit and explicit request to apply safe corrections | edited skill persists; first-party registry indexes it for future tasks | `skills/skill-improver/SKILL.md`; `extensions/skill-registry.ts` |

## S5 — Policy and identity

- State: P
- Function: set persistent permitted scope for the local coding workflow and ultimate authority over consequential operations and how future subagents may operate.
- Disturbance / variety regulated: conflicts between repository/user restrictions and tool-generated actions, new sensitivity to destructive commands, background autonomy and attempted widening of approval scope.
- Decisive decision or feedback right: local human owns project/global durable `runtime-guardrails.json` allow/confirm/block settings and `background-subagents.json`; per-session review/remediation authorizations and ordinary delivery remain subject to a human-controlled repository policy.
- Decision owner: legitimate self-hosted project owner (`P`), not the code reviewer, delegated worker or remote OSS maintainer.
- Supporting / enforcement mechanisms: first-party runtime config decoder, project-over-global precedence, guarded tool intercepts and interactive consent, session/repository-bound approval identity and fail-closed refusals.
- Closure path: human establishes project/global normative guardrails and delegation mode → persisted config is read into the installed session → sensitive commands are allowed/confirmed/blocked accordingly → workers act only under the resulting policy; new consequential authority is escalated for approval.
- Boundary reachability: `extensions/gentle-ai.ts` loads project/global guardrail policy on the production Pi path, and `lib/background-subagents-policy.ts` is called by `gentle-agents.ts` to choose child scheduling mode. This is durable local normative control, not individual PR acceptance alone.
- Why this is / is not agent-owned: the enduring rule contents and ultimate delivery/authorization identity are supplied by the user; the model acts within—not as the author of—those constraints.
- Evidence: [guardrail policy resolution](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/extensions/gentle-ai.ts#L1490-L1575), [background delegation policy](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/lib/background-subagents-policy.ts), [session standing review permission](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/lib/review-session-standing-permission.ts), [delivery separation](https://github.com/Gentleman-Programming/gentle-shell/blob/407404372516ac0e27fc63e22ed08344f3f64c90/docs/review-integration.md#L38-L49).
- Identity / ultimate-policy issue: whose standing development and safety boundaries determine what the installed local coding assistant is allowed to do across later tasks.
- Ultimate authority in each claimed mode: human owner (`P`); neither the native reviewer nor child tool has authority to rewrite user-confirmed global/project policy.
- Return-to-operation path: project/global files set behavior for subsequent tool interception and background delegation; the session/review consent gate halts unauthorized actions.
- Basis: durable local operator-owned policy loop with runtime enforcement.
- Confidence: moderate-high for scoped standing safety/workflow policy, not external maintainer governance.
- Caveats: `GENTLE_PI_AUTONOMOUS_MODE=1` is an explicit operator-selected override; this is still parent-granted, not agent-owned ultimate policy. Some actual safe handling depends on the underlying Pi host and external review provider.

## Distributed OSS parent arrangement

The maintainer organization and user installations are different recursions. This artifact credits an installed human as parent for the user's own runtime/project policy, not all OSS contributors as one centralized governance entity. Separate Go review-provider authorship is not another local S3* body.

## Self-hosted and non-human modes

In attended mode the user can inspect/stop owned subagents, manage project/global rules and explicitly apply proposed skill changes. Background child work remains dependent on a live parent Pi session; headless print mode refuses background delegation. Optional external Engram is not bundled and cannot silently fill S4. The native review endpoint has its own provider-owned final authority and a typed fail-closed integration; Pi does not inherit that authority merely by transporting its prompts.

## Recursion

Each model-backed independent Pi child/inline worker is S1; concrete worktree contention checks are bounded S2; the model parent and attended local owner manage the current session's worker portfolio as S3; requested skill improvement is a limited prospective S4 constructor and parent mode; local human-authored enduring workflow/safety rules are S5. Code-review quality lenses do not separately audit S3. Other external sessions have presence/notification only, not a claimed shared higher recursion.

## Variety and escalation

A scoped worker encountering failed tests reports partial/blocked or repair evidence; the parent can schedule verification or stop the child. A conflicting native remediation launch in the same worktree fails admission. Missing native reviewer authority gives typed refusal or risk-high fallback as specified, not synthetic approval. A skill-rule conflict is reported for human review; sensitive or destructive operations require the user's currently chosen safety policy. This distinction prevents generic CI green or notification ACK from becoming autonomy evidence.

## Evidence gaps

- Manual frozen-source assessment only; Pi models, external Gentle AI provider, repository quality results and live LLM-agent effectiveness were **not** executed.
- S2 positive evidence is narrow to same-worktree native remediation and deterministic queue admission; independent autonomous arbitration of arbitrary two-writer collisions is not established.
- S3 model current control is prompt/tool supported and local-session scoped; no enterprise-wide cross-session decision authority is claimed.
- First-party S4 is supported by an explicit requested skill-improvement and apply workflow, not by always-on self-learning; no observed adaptive gains or automatically selected future skill policy are claimed.
- Distinct Go provider review authority and optional memory remain adjacent boundaries; they cannot upgrade local Pi-extension S3*, S4 or S5 without a further boundary-specific assessment.
