---
harness_id: halo-harness
project_name: Halo Harness
repository: https://github.com/roloVibes/Halo-Harness
review_ref: 710dde651035be3f204598aee90a1e4b85e3d6e8
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Halo Harness

## Review boundary

- System in focus: Halo native model/tool sessions with supported Orchestra, supervised-goal, built-in review/fix and operator model-roster adaptation modes.
- Purpose and identity: Run and regulate local/fleet agent work on selectable models with explicit artifacts and controls.
- Relevant environment: users, workspaces, model services, tools and the operational disturbances described below.
- Standard-distribution boundary: Installed halo CLI/TUI/Studio and first-party Orchestra/Supervise/review/model-library paths at the frozen revision.
- Credited operating / distribution surfaces: Native Python loop/worker adapters; Orchestra claims/fresh conflict judge; supervised auto/review replan paths; built-in review --fix; operator adviser/download/verify/role-apply path.
- Adjacent first-party surfaces excluded from ownership: Repository research_notes, plans, reports of harness development, CI/tests and retrospective design reviews; external provider internals and remote peer implementations not supplied by this tree.
- First-party operating / deployment modes considered: Native sessions; Orchestra run; supervised replan:auto and replan:review/Attention owner decisions; halo review --fix; operator-controlled Local Models adviser/library. Optional modes are explicit, not claimed simultaneously active or universal defaults.
- Recursion level: one deployed harness/composition and its work sessions; repository maintainers and external hosts are outside this operational recursion.
- Reviewed revision: `710dde651035be3f204598aee90a1e4b85e3d6e8`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (active Index pair; current Skills main calibration also consulted).

## Repository architecture

Halo owns its Python model/tool loop and child workers, while reading Claude-compatible config as input. Orchestra turns a goal into claim-scoped lanes and worktrees, merges with a fresh conflict judge and returns failed pieces. Supervise detects current drift, can apply lead replans automatically or park durable operator decisions and then resume. Built-in review launches read-only dimension reviewers/judge and optionally fixes confirmed findings with re-verification. Model Library/adviser compares outside model options with local gaps and exposes operator-controlled installation/verification/role changes. Permissions, queue caps, test gates, role prices and telemetry enforce or inform these decisions; they do not become owners. Development and benchmark/research artifacts stay outside the operational boundary.

## Operational model

Native session and lane actors are S1. S2 is grounded in real cross-worker claim/merge disturbance. S3 has separately reconstructed autonomous and operator modes; S3* is grounded in the explicit review/fix/reverify chain. S4 is limited to the documented operator model-capability adaptation path, not internal task replanning or generic coaching. S5 remains a bounded negative. Evidence is structural at the exact revision; no live model/fleet/GPU performance is claimed.

## S1 — Operations

- State: A
- Function: Execute model-directed workspace tasks and operational worker lanes.
- Disturbance / variety regulated: Uncertain code/research work, tool failures, provider/context limits and incomplete artifacts.
- Decisive decision or feedback right: Choose next tool, code/research action or response from feedback.
- Decision owner: The first-party session/worker model actors.
- Supporting / enforcement mechanisms: Python model/tool loop, provider transports, permission engine, local tools/MCP, sessions, role lineups and worktrees.
- Closure path: Model request → selected tools → observations/session state → subsequent model step or worker result.
- Why this is / is not agent-owned: Halo owns its loop rather than merely configuring Claude Code. Claude-compatible settings and external model endpoints do not donate control functions.
- Evidence: [halo_harness/agent/loop.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/agent/loop.py); [halo_harness/agent/subagent.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/agent/subagent.py); [halo_harness/orchestra/workers.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/orchestra/workers.py); [README.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.
- Boundary reachability: Normal halo CLI/TUI and Orchestra adapters instantiate the native session/worker loop; installed role/model configuration does not require a third-party agent runtime.

## S2 — Coordination

- State: A
- Function: Regulate overlapping file-unit writes and merge conflicts across distinct Orchestra worker lanes.
- Disturbance / variety regulated: Agents may claim overlapping functions/file regions or produce mutually conflicting changes.
- Decisive decision or feedback right: Workers choose a different claim, wait or escalate on refusal; a fresh judge selects a conflict resolution when branches collide.
- Decision owner: Worker/lead model actors and the fresh conflict-judge model own the discretionary choices; code owns atomic admission and merge/test enforcement.
- Supporting / enforcement mechanisms: AST/heading/file-unit claim keys, exclusive claim log, guarded writes, per-lane worktrees, serialized merges, test checks and bounded send-back.
- Closure path: Claim refusal returns holder/expiry to worker → changed claim/wait/escalation; conflicting branches → fresh judge sees goal/hunks → proposed text applied/tested → failed resolution undone and piece returned to the worker for revision.
- Why this is / is not agent-owned: A is grounded in model-owned response to a concrete cross-S1 disturbance, particularly the fresh conflict resolution and worker correction, not in deterministic locks or sequence alone.
- Evidence: [docs/ORCHESTRA.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/ORCHESTRA.md); [halo_harness/orchestra/claims.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/orchestra/claims.py); [halo_harness/tools/orchestra_claims.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/tools/orchestra_claims.py); [halo_harness/orchestra/merge.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/orchestra/merge.py); [halo_harness/orchestra/adapters.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/orchestra/adapters.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.
- Boundary reachability: Orchestra run creates real native worker sessions and exposes claim tools/guard in their run environment; merge uses the shipped fresh-judge adapter.

- Distinct S1 units: independently executing worker lanes, each with its own task, model session, claimed code unit and branch.
- Inter-S1 disturbance: overlapping live claims and incompatible edits to the same code regions at integration.
- Attenuating coordination relation: claimed unit boundaries and isolated worktrees plus fresh-agent conflict judgment and corrective return.
- Feedback into subsequent S1 behaviour: refusal/holder context changes the next worker choice; failed merge tests undo the resolution and send the piece back under the return cap.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it explicitly detects and settles shared-artifact collision between otherwise independent work actors.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate whole-run current resources and commitments after forecast/return/block/stall drift.
- Disturbance / variety regulated: Projected overspend, repeated returns, blocked dependencies/claims and stalled lanes threaten the current goal organization.
- Decisive decision or feedback right: Choose revised model/bio, split remaining work, add a read-only specialist, retry with corrective context or stop; in review mode the owner decides whether to apply the proposed revision.
- Decision owner: Auto mode: the lead model owns the checked replan. Review/parked budget mode: the legitimate local operator owns the returned acceptance/cap decision.
- Supporting / enforcement mechanisms: Drift thresholds, current lane/spend/forecast snapshots, plan validation, immutable merged-lane protection, pause/checkpoint, durable decision rows and deterministic apply/resume.
- Closure path: Drift → lanes pause → lead receives whole remaining plan/current evidence → auto applies a valid agent plan, or review parks its diff → operator approves/rejects/adjusts cap → split/claims/workflow/forecast updated and remaining operation resumes.
- Why this is / is not agent-owned: The lead makes the substantive current-control revision in auto mode; validation and budgets enforce it. Review mode separately returns an operator decision into operation. Neither hard stops nor initial task splitting alone supplies the positive witness.
- Evidence: [docs/SUPERVISE.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/SUPERVISE.md); [halo_harness/supervise/drift.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/supervise/drift.py); [halo_harness/supervise/replan_ask.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/supervise/replan_ask.py); [halo_harness/supervise/replan_apply.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/supervise/replan_apply.py); [halo_harness/supervise/decisions.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/supervise/decisions.py); [halo_harness/supervise/apply.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/supervise/apply.py).
- Basis: structural.
- Confidence: high.
- Caveats: Optional supervised modes; replan limits/cooldown apply, completed lanes are pinned, workflow-pinned stage sets disable free replanning, and budget ceilings remain separately operator-owned..
- Boundary reachability: halo supervise/goal options expose replan:auto and replan:review; ordinary runtime adapters call the lead and apply checked plans. Attention answers are polled and applied to the same queued goal.

- Whole-system current view: every unmerged lane with state/model/returns/claim refusals, pinned merged lanes, spend/forecast and concrete drift reasons; queue/goal caps remain visible constraints.
- Current-control decision scope: current worker/model commitments, lane structure and retries within the bounded goal; parent mode also decides budget/return-cap exceptions and stop/resume.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Lead model | Eligible forecast/return/blocked/stalled drift in `replan:auto` | Checked agent revision updates lanes/claims/forecast, then resumes checkpoint | `supervise/replan_ask.py`, `replan_apply.py`; SUPERVISE.md Replanning |
| Parent (`P`) | Local operator | `replan:review`, plan review or parked budget/gate exception | Durable answer applies/rejects plan or changes cap and requeues the goal | `supervise/decisions.py`, `apply.py`; SUPERVISE.md The review |

## S3* — Complementary audit

- State: A
- Function: Complement production claims with raw-code multi-dimension review, independent finding adjudication and correction/re-verification.
- Disturbance / variety regulated: Author summaries or reviewer allegations may be wrong; a claimed fix may leave the defect intact.
- Decisive decision or feedback right: Reviewer finds code defects; independent judge confirms/dismisses against source; confirmed findings are corrected by a separate fixer and judged again against the new code.
- Decision owner: Fresh read-only reviewer/judge model actors own audit judgments; a coder actor owns scoped correction.
- Supporting / enforcement mechanisms: Built-in dimension prompts, fixed target/diff resolution, read-only agent specs omitting CLAUDE.md, structured verdicts, serial fixes, file hashes and current-source re-verification.
- Closure path: halo review target --fix → raw artifact review → judge traces claim → CONFIRMED finding goes to fixer → changed file hash/current diff → judge rechecks → fixed only when the defect is dismissed; failed/unparseable checks remain PLAUSIBLE/skipped.
- Why this is / is not agent-owned: The separate code-inspecting actors add complementary reality access and a shipped corrective return. Deterministic Orchestra gates and model tuning statistics are not promoted to audit ownership.
- Evidence: [docs/REVIEW.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/REVIEW.md); [halo_harness/review/run.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/review/run.py); [halo_harness/review/agents.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/review/agents.py); [halo_harness/review/verify.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/review/verify.py); [halo_harness/review/fix.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/review/fix.py); [halo_harness/review/prompts/judge.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/review/prompts/judge.md).
- Basis: structural.
- Confidence: high.
- Caveats: Report-only mode alone is not claimed to complete correction. The positive witness includes --fix with verification; review exit code 0 is not evidence of zero findings or approval..
- Boundary reachability: halo review and /review call the common built-in run_review; --fix is a shipped option, not an unwired developer callback, and it requires verification.

- Claim being audited: correctness/security/performance/test/docs claims about the actual target artifact and the claim that a confirmed defect was fixed.
- Ordinary reporting path: original work result, author narrative and routine production checks.
- Complementary access path: separate read-only dimension reviewers and judge inspect raw diff, surrounding code and concrete failure scenario; after-fix judgment reads current file/diff.
- Independence boundary: fresh named reviewer/judge sessions with read-only tools and omitted CLAUDE.md; fixer cannot delegate and runs separately. Same underlying model/provider can still share blind spots.
- Who acts on findings: optional built-in --fix routes only confirmed findings to the coder, detects unchanged files, and re-verifies before retaining a fixed outcome; no automatic commit/merge gate is claimed.

## S4 — Outside-and-then intelligence

- State: P
- Function: Develop prospective model-roster capability adaptations from external ecosystem options and local operating constraints, with operator selection returned into the roster/roles.
- Disturbance / variety regulated: Missing embedding/vision/role capabilities, model-family blind-spot overlap and newly available model families can leave future tasks unsupported or costly.
- Decisive decision or feedback right: Choose whether to add/verify a new external model, retire an overlap or repoint a role after inspecting capability/cost/fit options.
- Decision owner: The legitimate self-hosting operator; deterministic adviser/battery/UI supply options and enforcement, not an autonomous S4 actor.
- Supporting / enforcement mechanisms: External Ollama/Hugging Face library/catalog metadata and dated snapshot, local host memory/capability profiles, gap/freshness/mismatch rules, ranked options with download/VRAM/role impact, download-and-verify job and explicit role acceptance.
- Closure path: External/local roster distinctions → bounded ranked adaptation options → operator selects Download and verify/retire/point → model pulled, battery profile written and role offered → accepted assignment updates the active lineup/role for subsequent work.
- Why this is / is not agent-owned: P is supported by a function-specific compare/select/apply path. Neither deterministic recommendation nor ordinary current model routing is called autonomous S4; the operator owns the prospective capability choice.
- Evidence: [docs/MODELS-adviser.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/MODELS-adviser.md); [docs/MODELS-ollama.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/MODELS-ollama.md); [halo_harness/models_library/advise.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/models_library/advise.py); [halo_harness/models_library/advise_rules.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/models_library/advise_rules.py); [halo_harness/models_library/browse.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/models_library/browse.py); [halo_harness/studio/local_search_api.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/studio/local_search_api.py); [halo_harness/studio/local_verify_job.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/studio/local_verify_job.py); [halo_harness/studio/roles_point_api.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/studio/roles_point_api.py).
- Basis: structural.
- Confidence: medium.
- Caveats: The adviser is deterministic and the packaged ecosystem snapshot can be stale; freshness is not measured superiority. No live download, benchmark or successful capability gain is claimed by this source assessment..
- Boundary reachability: Official halo local advise/Studio Local Models/Library exposes suggestions and the same supported verify/assign/role-point routes; this is installed product behavior, not a research plan.

- External distinction: externally available model families, capability/library facts and freshness are compared with the local installed roster and hardware/role gaps.
- Future / prospective distinction: options describe capabilities currently unavailable (for example image/embedding work), newer model lines and future role coverage/cost before adopting them.
- Adaptation option generated: add a fitting capability model, choose a different-family verifier, retire overlap or repoint a future-use role, with stated unlocks/cost.
- Path back into current capability / S3: operator-triggered pull and battery writes a real profile; explicit accepted role assignment changes the lineup used by subsequent sessions and workers.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy arbitration function is supplied at the assessed recursion.
- Disturbance / variety regulated: Goal stop criteria, permissions, fleet control grants, role bios and deployment policy.
- Decisive decision or feedback right: No function-specific identity/ultimate-policy decisive return path established.
- Decision owner: Operator/configuration owns constraints; no qualifying S5 owner/path established.
- Supporting / enforcement mechanisms: WHAT/DONE/STOP goal fields, role/lineup configuration, approval and fleet control levels, supervised plan/budget decisions and local settings.
- Closure path: Ordinary goal/resource/permission decisions return into work, but no distinct identity-level arbitration/return is established.
- Why this is / is not agent-owned: These paths close S1/S3 decisions or security constraints. Renaming them policy or giving a user final operational say does not establish S5.
- Evidence: [docs/ORCHESTRA.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/ORCHESTRA.md); [docs/SUPERVISE.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/SUPERVISE.md); [docs/FLEET.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/FLEET.md); [docs/TEAM.md](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/docs/TEAM.md); [halo_harness/permissions.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/permissions.py); [halo_harness/supervise/decisions.py](https://github.com/roloVibes/Halo-Harness/blob/710dde651035be3f204598aee90a1e4b85e3d6e8/halo_harness/supervise/decisions.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: docs/ORCHESTRA.md, docs/SUPERVISE.md, docs/FLEET.md, docs/TEAM.md, halo_harness/permissions.py, halo_harness/supervise/decisions.py and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Goal boundaries, plan/budget/stop decisions, bios/role grants, fleet pairing/control levels and permission approvals; parent-governed S3/S4 alternatives considered separately.
- Why no material first-party path remains: No shipped path identifies an ultimate-purpose/policy dispute, sends it to a legitimate final identity authority and returns an authoritative policy settlement. Maintainer release/governance and static config are outside or insufficient for this operational function.

## Distributed OSS parent arrangement

Public maintainers own development and release governance. Their repository process is adjacent to the installed harness; contributor plurality does not establish operational parent S3/S4/S5 at this recursion. S3 separately exposes an operator review/budget mode. S4 roster adaptation is operator-owned. Neither is treated as ultimate identity S5.

## Self-hosted and non-human modes

Native sessions; Orchestra run; supervised replan:auto and replan:review/Attention owner decisions; halo review --fix; operator-controlled Local Models adviser/library. Optional modes are explicit, not claimed simultaneously active or universal defaults. Model choice, permission settings and deployment administration alone do not establish ultimate-policy governance. Unimplemented extensions do not receive constructor credit.

## Recursion

Subagents are task decomposition; no recursively viable suborganization is established.

## Variety and escalation

Tool/model failures, permission limits and context exhaustion return as observations, refusals, pauses or terminal results. These channels support local recovery; they are not additional VSM functions or automatic algedonic evidence.

## Evidence gaps

No live provider or product E2E run was performed. Conclusions concern reachable source-level ownership at the exact frozen revision, not performance, deployment reliability or benchmark quality. Bounded absence claims cover the stated supported distribution, not arbitrary future extensions.
