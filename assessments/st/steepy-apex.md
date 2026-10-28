---
harness_id: steepy-apex
project_name: Steepy Apex
repository: https://github.com/steepy-it/steepy-apex
review_ref: 7283b7940e6ec97ec739a28b6de1525d2891bdb4
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Steepy Apex

## Review boundary

- System in focus: one user-owned repository/project operated through the first-party Steepy Apex installed skill/hook package, spanning its supported pre-hub inception and subsequent hub-governed coding work, rather than Steepy the vendor or its OSS maintainer organization.
- Purpose and identity: establish a bounded, verified application and persistent project conventions; translate accepted specs/goals into model-owned coding work, coordinate surfaces, inspect outcomes and preserve user-controlled project identity and release authority.
- Relevant environment: application requirements and users, actual repository changes, task interfaces and tests, changing external frameworks/model providers and supported versions, project architecture/permission choices, host coding-agent capabilities, CI/release targets and execution interruptions.
- Standard-distribution boundary: the published cross-host package, its user-invocable inception/discovery/plan/implement/review/loop-engineer skills, generated hub conventions and agent routing, host adapters and executable workflow/governance helpers. Normal interactive Gear 3 uses host model/subagent dispatch when available, with documented inline degradation; Gear 3 autopilot runs fresh Claude/Codex/OpenCode headless phase models; Gear 4 uses deterministic state/retry/verification with headless model coding/review. Inception is human-dialogue only, including on other supported hosts.
- Credited operating / distribution surfaces: `skills/{inception,discovery,brainstorm,plan,implement,review,loop-engineer}/SKILL.md`, `skills/implement/{implementer-prompt,task-reviewer-prompt,final-review-prompt,reviewer-recovery}.md`, `skills/loop-engineer/loop-final-review-prompt.md`, `scripts/{autopilot,loop-engineer,inception-state,inception-governance,reviewer-response,workflow-state,verify-model-mappings}.mjs`, `adapters/{headless,model-mappings}.mjs`, generated `.apex/` hub and user-owned work artifacts.
- Adjacent first-party surfaces excluded from ownership: Steepy Apex's own contributor/release/marketplace/CI process, `RELEASE.md`, `docs/publication-readiness.md`, `tests/` fake harness fixtures and canaries, decorative branding and standalone privacy/marketing claims; external Claude/Codex/OpenCode/Pi/DeepSeek implementations beyond first-party invocation contracts are not attributed to Steepy.
- First-party operating / deployment modes considered: existing-project manual Gear 1–3; Gear 3 pre-authorized `plan → implement → review` headless autopilot; Gear 4 human-ratified bounded loop with model worker and separate reviewer; first-project inception → certified init → per-decision discovery; explicit optional inline review/delegation downgrade on hosts without a task tool; no native headless runner on Pi or DeepSeek.
- Recursion level: one evolving target project under Steepy governance. Distinct S1 implementation tasks/surface specialists produce local changes; the model implement coordinator supervises whole accepted plan, a separate branch reviewer evaluates those interactions, and inception's parent user retains project-wide purpose and foundational adaptation decisions. Steepy's package-maintenance organization is another recursion.
- Reviewed revision: `7283b7940e6ec97ec739a28b6de1525d2891bdb4`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Steepy Apex ships model-consumed skills and generated project hub routing, not a self-contained new LLM provider. Its real host dispatch is the attached Claude/Codex/OpenCode/Pi/DeepSeek model agent; the package supplies specific prompts, role contracts, manifests, command-line helpers, persistent `.apex/work/` task evidence, and deterministic gates. Gear 3's `implement` orchestrator assigns each task to a model-owned specialist under TDD, starts fresh read-only model reviewers, validates their artifact-backed results and loops actionable findings to the relevant implementer. The final reviewer gets a separate criteria-only artifact and aggregate Git diff to discover *cross-task* integration problems. The next `review` skill re-runs explicit tests and hub validation before requesting human publication approval. Gear 3 autopilot's `scripts/autopilot.mjs` only starts one fresh model session per phase in fixed order; it does not steer or choose a changed policy, and it never pushes/PRs.

Gear 4 is different: the human ratifies a machine-verifiable goal, mutation budget, branch-only blast radius and commit authorization. `scripts/loop-engineer.mjs` enforces attempts, verifier results, commit/keep/discard and recovery deterministically while a model worker can choose code mutations; a separately dispatched model reviewer checks immutable whole-branch evidence and can force a fix *within* the original budget. Inception is a first-party alternative initial operating mode, not an example/dogfood process: the model conducts product/architecture dialogue and official-source foundation research, records candidate alternatives and supported versions, but a real parent human decides foundational project choices, approves full project contracts and must re-approve material changes. The helper seals the decision, and certified init/discovery returns accepted project decisions into later hub standards. No installed version autonomously patches its own model mappings from provider drift.

Sources: [README/package entry](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/README.md), [Gear 3 workflow and model modes](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/docs/workflow.md), [Gear 3 orchestration skill](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/SKILL.md), [headless conductor](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/scripts/autopilot.mjs), [Gear 4 controller](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/scripts/loop-engineer.mjs), [inception lifecycle](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/docs/inception.md).

## Operational model

For an existing project, the model workflow classifies a request against the routed hub (COVERED/CONFLICT/GAP), obtains the applicable approved spec/plan and delegates independently accountable task outcomes to configured specialist models. The current implement coordinator reads plan-level task progress, reacts to blockers and reviewer findings, chooses model tiers/escalations or corrective dispatch and maintains the whole-branch result. Read-only critics access task or aggregate diffs independently of the implementer's brief report. In new-project inception, external support/version research and architecture/policy questions are brought back to the user; approved constraints are bound in a machine-checked project contract, executed in bootstrap, and optionally certified into durable project conventions. In Gear 4 the model does not own the deterministic verifier or budget; coding discretion remains in the child. No result silently authorizes a remote push.

## S1 — Operations

- State: A
- Function: directly implement and test bounded target-project changes, or a representative first application path, using code-aware model discretion under explicit task/goal context.
- Disturbance / variety regulated: unfamiliar repository APIs, failing tests, incomplete specs, integration edge cases, platform setup and differing source conventions.
- Decisive decision or feedback right: a model specialist selects the actual code/test edits, investigates source ambiguity, runs red→green→refactor, and may choose a changed fix from reviewer feedback; a Gear 4 model worker selects a mutation attempt inside controller-owned constraints.
- Decision owner: host-backed task-specific `<surface>-agent` in Gear 3; headless Claude/Codex/OpenCode coding agent in supported autopilot/Gear 4; research/bootstrap model coordinator or bounded children during inception. Not the JavaScript event controller.
- Supporting / enforcement mechanisms: routed standards, task briefs, host model-tier mapping, `adapters/headless.mjs`, diff snapshots, work manifests, deterministic verifier and path/commit guards, task reports.
- Closure path: accepted plan task and real source → model specialist implements with TDD/tests → writes report/diff → scoped reviewer returns a correction or approval → changed source verified; Gear 4 repeats a model mutation only when the mechanical goal check/review/budget permits.
- Boundary reachability: `README.md` installs these first-party skills into supported coding hosts; `skills/implement/SKILL.md` dispatches the prompt-bearing specialist; `scripts/autopilot.mjs` and `scripts/loop-engineer.mjs` invoke headless host models on their documented supported subset. The emitted code edits and repository tests occur in the actual user's project.
- Why this is / is not agent-owned: removing the model leaves explicit task headers, guards and test commands but no source-specific code design or repair decisions; deterministic keep/discard and audit receipt parsing are not credited as autonomous implementation.
- Evidence: [implementer model prompt](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/implementer-prompt.md), [implement task dispatch/recovery](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/SKILL.md), [headless runner](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/adapters/headless.mjs), [Gear 4 implementation loop](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/scripts/loop-engineer.mjs), [inception bootstrap](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/inception/SKILL.md).
- Basis: first-party role prompt plus installed host invocation and executable implementation/feedback routes.
- Confidence: high for shipped model ownership contract; medium for cross-host live execution without provider credentials.
- Caveats: simulated/fake-runner tests demonstrate state handling, not third-party provider correctness. On Pi/DeepSeek, Gear 3/4 headless runners are explicitly unavailable; host tool absence reduces a delegate to same-session model work.

## S2 — Coordination

- State: A
- Function: detect and correct incompatibility across distinct S1 implementation tasks contributing to one branch.
- Disturbance / variety regulated: Task A changes an interface or owned shared surface and Task B depends on its old API, silently undoes the change, or violates a cross-cutting standard; separate task-local TDD may still pass.
- Decisive decision or feedback right: a fresh model whole-branch reviewer evaluates aggregate task integration and reports specific `ISSUES_FOUND`; the model implement coordinator chooses an owning task fix and re-dispatches a specialist, then orders a new cross-task review.
- Decision owner: separate model reviewer for cross-task mismatch judgment and model implement coordinator for corrective work selection; local status parsers and serial dispatch only enforce/report.
- Supporting / enforcement mechanisms: one-implementer-in-flight discipline, task-result index, success-criteria-only artifact, aggregate Git branch diff, cross-surface standards, `final-review-issues.md` and fix manifests.
- Closure path: completed independent task results → aggregate diff/criteria/standards reviewed for mutually contradictory interfaces → actionable finding artifact → affected specialist model fixes the shared boundary → new aggregate diff, fresh independent review and final verification.
- Boundary reachability: installed Gear 3 `implement` calls `final-review-prompt.md`, regenerates the branch diff and loops issues into a task-local fix; the documented autopilot phase uses validated task/final reviewer manifests and reviewer-result guards. This is not inferred from a generic task queue.
- Why this is / is not agent-owned: explicit source-specific cross-task contract judgment and corrective task selection are model decisions, although task order and manifest/receipt constraints are deterministic.
- Distinct S1 units: at least two separately bounded implementation tasks/possibly different `<surface>-agent` specialists in the same accepted plan, each owning an independent code/test deliverable (serial execution does not erase cumulative inter-task interference).
- Inter-S1 disturbance: a later specialist's change to a shared interface or standards contradicts an earlier specialist's output, or its locally passing tests leave an aggregate integration fault.
- Attenuating coordination relation: a model fresh-eyes *whole-branch* reviewer explicitly checks cross-task interface composition and contradictions against one aggregate diff, then supplies owning-task corrections.
- Feedback into subsequent S1 behaviour: `final-review-issues.md` becomes a bounded fix manifest for the selected task's specialist; task output is revised, re-diffed and reviewed again.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the dedicated cross-task reviewer has the instruction to detect actual overlapping/interface incompatibility, and its issue artifact actively changes a task's implementation; mere one-at-a-time queueing or a status ledger does not supply the autonomous S2 witness.
- Evidence: [distinct task implementer role](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/implementer-prompt.md), [whole-branch cross-task review](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/final-review-prompt.md), [implement whole-branch fix closure](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/SKILL.md), [reviewer response evidence guards](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/reviewer-recovery.md).
- Basis: explicit cross-task interference/repair path, supported by source-level role separation and deterministic evidence validation.
- Confidence: medium-high for live shipped model-mode relation.
- Caveats: Gear 2 bypasses these fresh reviewers; same-session fallback on hosts without subagents weakens separation, and Gear 4's deterministic verifier alone should not be separately scored as S2.

## S3 — Inside-and-now control

- State: A
- Function: discretionary whole-current plan supervision, task/model-resource assignment, exceptional blocker escalation and whole-deliverable acceptance before handoff.
- Disturbance / variety regulated: task complexity spread, unplanned discovery, one blocked specialist, incomplete planned work, review-fix churn, conflicting standards and over-spending strong model calls on mechanical changes.
- Decisive decision or feedback right: the main model implement coordinator reads the accepted plan, chooses task-specific specialist/model tier within routing limits, responds to `NEEDS_CONTEXT`/`BLOCKED` by targeted context, tier escalation or splitting, assigns final cross-task fixes and controls whether the whole planned branch is ready for the next review phase.
- Decision owner: the model executing installed Gear 3 `implement` skill; human has ratified spec/plan and owns protected scope/publication. Gear 3 JavaScript autopilot does not steer models; Gear 4's deterministic attempt budget, verifier and commit/stop do *not* themselves furnish autonomous S3 discretion.
- Supporting / enforcement mechanisms: accepted plan/task dependency order, task/result ledger, per-surface model-tier mapping, reporter and reviewer output contracts, `task-results.mjs`, `autopilot-context.mjs`, `reviewer-response.mjs`, host role dispatch.
- Closure path: all current plan tasks/reviewer statuses and resource needs → main model prioritizes local task/specialist and escalates review findings or blockers → bounded work/fix dispatch changes current commitments and subsequently updated ledger → whole-branch verified review and exact review-phase handoff.
- Boundary reachability: ordinary installed Gear 3 `implement` has explicit supervisory instructions and runs in a model session; headless Gear 3 autopilot starts the same model phase as a real child with its routed manifest. This is not an attempt to credit the deterministic Gear 4 controller as a model supervisor.
- Why this is / is not agent-owned: the model decides actual current corrective assignments and risk-appropriate tiers under the whole plan, rather than a fixed `plan→implement→review` scheduler selecting those choices. Its human-approved scope remains binding; neither mere delegate invocation nor fixed budget logic is the evidence.
- Whole-system current view: the coordinator sees the accepted multi-task plan, completed/pending ledger entries, task concerns, critical reviewer outcomes and whole-branch criteria/diff/approval status.
- Current-control decision scope: sequencing and reassigning corrective work among specialists, model tier/escalation, splitting genuinely blocked tasks, and withholding next-phase completion until all task/branch gates are accepted.
- Evidence: [Gear 3 implement manager and escalation](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/SKILL.md), [model-tier/project flow](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/docs/workflow.md), [autopilot phase boundary](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/scripts/autopilot.mjs), [Gear 4 deterministic-rights separation](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/loop-engineer/SKILL.md).
- Basis: explicit model-coordinator instructions with operational child/review return contracts, not the name `controller`.
- Confidence: medium-high; no authenticated multi-model run executed during this assessment.
- Caveats: this is Gear 3's model-owned current-control mode, not a claim that every host has full delegation; Gear 4 is deliberately a fixed deterministic loop after human goal/mutation authorization.

## S3* — Complementary audit

- State: A
- Function: an independent source/diff/test evidence path that can reject an implementer's apparent completion and force correction.
- Disturbance / variety regulated: optimistic implementer reports, hidden missing tests, divergence between task claims and actual changed code, aggregate integration regression and verifier gaming.
- Decisive decision or feedback right: fresh read-only task and final reviewers use exact diff, applicable standards and criteria to decide `APPROVED` versus `ISSUES_FOUND`; Gear 4's separately dispatched model branch reviewer may identify goal gaming that a deterministic verifier missed.
- Decision owner: fresh model reviewer distinct from code-writing implementer/loop worker on supported task-tool/headless modes; deterministic receipt digests and test commands bind evidence, but do not decide the semantic verdict.
- Supporting / enforcement mechanisms: captured Git diffs, independent code read access, criteria-only context, reviewer reports/issue artifacts, reviewer-response strict schema/baseline checks, original terminal verifier output, mandatory `validate-hub.mjs` in later review.
- Closure path: reported task completion → separate reviewer directly inspects code diff/source and checks plan requirements → approval or actionable issue file → main model controller re-dispatches fix and re-audits; final phase independently re-runs test/hub commands before PR offer.
- Boundary reachability: `skills/implement` dispatches `task-reviewer-prompt.md` and `final-review-prompt.md` to fresh task tools where supported, and the headless Gear 4 controller dispatches a separate injected reviewer. These are installed, active role paths, not test-only fixtures.
- Why this is / is not agent-owned: the reviewer model owns substantive cross-check findings from a separate direct evidence path; the same-session fallback and deterministic validators are weaker and are not counted as the independent model case.
- Claim being audited: one task/whole branch is correctly implemented, tested and compliant with approved criteria, or a Gear 4 apparent verifier success is genuine.
- Ordinary reporting path: implementer's `DONE`/TDD report and work ledger plus a mechanical verifier's pass/fail.
- Complementary access path: fresh reviewer reads task/aggregate Git diff and relevant repository source plus standards, with separate criteria-only manifest; Gear 4 supplies immutable branch snapshot and model review evidence not reducible to the verifier exit code.
- Independence boundary: reviewer prompt is read-only and separate from code writer with a new context; it has independently derived diff/criteria inputs, not unlimited authority, and may use the same vendor/model family. If host has no task-tool, the documented inline pass is weaker and does not prove this mode.
- Who acts on findings: implement model coordinator reads issue file, assigns task fixes and reruns review; deterministic Gear 4 controller can grant only budgeted follow-up mutation; later review skill withholds publication.
- Evidence: [task reviewer](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/task-reviewer-prompt.md), [whole-branch reviewer](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/implement/final-review-prompt.md), [Gear 4 independent reviewer](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/loop-engineer/loop-final-review-prompt.md), [controller snapshot/feedback](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/scripts/loop-engineer.mjs), [final evidence gate](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/review/SKILL.md).
- Basis: direct-evidence separately prompted review with corrections fed back to operating work.
- Confidence: high structural, medium live reviewer independence without authenticated host dispatch.
- Caveats: a routine deterministic `validate-hub` test alone is not S3*, and successful fake-runner/CLI tests are not evidence that every provider delivers a fresh independent model.

## S4 — Outside-and-then intelligence

- State: P
- Function: in the first-party inception mode, research external technology/version support and compatibility options for a prospective target-project architecture, obtain legitimate parent selection, and return that choice as the current approved implementation baseline.
- Disturbance / variety regulated: changing runtime/framework/host support, unsupported/deprecated package versions, mismatched toolchains, future deploy constraints and incompatibility between a planned app and feasible external technology.
- Decisive decision or feedback right: user/project owner confirms externally researched architecture alternatives and version combination; the model researcher gathers official-source evidence and options but does not own the foundational adaptation choice.
- Decision owner: the legitimate human project parent in the dedicated inception research/architecture/approval mode. No agent-autonomous S4 alternative is established in this release.
- Supporting / enforcement mechanisms: `skills/inception/research-prompt.md` official-source checks, version/date/support comparison table, decision register `DR-n`, helper-frozen approval/verification contract, component/coverage records, later certified hub import; model-mapping verifier detects host drift but does not automatically change shipped mappings.
- Closure path: official ecosystem version/support/compatibility facts + future application/deploy requirements → model-supported option/research report → project human selects/approves foundation/version table → `inception-state.mjs` seals the approved project/contract → subsequent bootstrap uses selected versions and can be re-approved on substantial technology change.
- Boundary reachability: `inception` is an installed skill invoked explicitly before `init`, with research step, user version-table confirmation, an approval gate and a real bootstrap/verification return. It is not Steepy maintainer roadmap or an example.
- Why this is / is not agent-owned: research may be model-run, but the consequential capability/stack adaptation choice is explicitly reserved for a parent; the model cannot silently pick unsupported versions or change approved foundation.
- External distinction: current official releases, model/harness/framework support life cycles, compatibility constraints and upstream project/tool documentation are checked as external facts, not inferred from the local code tree.
- Future / prospective distinction: chosen stack longevity, forthcoming deploy requirements and support/EOL risk are assessed as compatibility for the application's prospective operation, rather than only a current failing task.
- Adaptation option generated: the researcher and model coordinator prepare version/framework alternatives with explicit support status, latest stable version, compatibility experiments and reasons for deviation; the parent selects a foundation.
- Path back into current capability / S3: the parent-confirmed versions and architectural selection become a sealed project/verification contract, govern real bootstrap commands and current implementation, and require reapproval when a foundational choice must change.
- Evidence: [inception research/options and approval](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/inception/SKILL.md), [model researcher from official external sources](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/inception/research-prompt.md), [whole lifecycle/parent version choice](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/docs/inception.md), [state/approval enforcement](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/scripts/inception-state.mjs), [mapping drift explicit patch policy](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/docs/workflow.md).
- Basis: parent-governed prospective capability-selection/return loop, bounded to inception and major-stack reapproval.
- Confidence: medium; this is targeted externally verified first-project capability formation, not an ongoing autonomous environmental intelligence agency.
- Caveats: ordinary Gear 3 code discovery/brainstorm and routine model mapping drift alerts are not autonomous S4; follow-on hub work does not automatically re-run inception or adapt Steepy itself.

## S5 — Policy and identity

- State: P
- Function: ratify and preserve the target project's ultimate purpose, architectural boundaries, security/identity/access design and acceptable change policy, with parent arbitration and return into subsequent work.
- Disturbance / variety regulated: changed project scope or purpose, newly proposed auth/data/deployment boundary, conflict with existing hub standards, an unapproved fundamental technology/commit-policy change or a reduced verification requirement.
- Decisive decision or feedback right: the legitimate user approves complete project documents and contract, must re-approve substantial design/scope/identity/commit-policy shifts, and approves each promoted inception decision or later explicit doc-wins override; the model cannot self-approve.
- Decision owner: project owner/operator as parent authority, not the worker, JavaScript status checker or autonomous implementation coordinator.
- Supporting / enforcement mechanisms: frozen full-document approvals, stable `DR-n` decision register, `inception-state.mjs` strict guards, verification-contract checks, certified `init` governance, `discovery` per-item accepted write-back, persistent `.apex/standards`/`conventions.md` plus CONFLICT stop rule.
- Closure path: identity-level architecture/purpose/permission change is surfaced in the inception decision register or as a hub conflict → legitimate parent selects/approves exact documents (or corrected hub preview) → helper freezes identity and gates bootstrap/change → approved decisions are certified/promoted to durable hub standards and subsequent model code work must obey them.
- Boundary reachability: shipped `inception` user dialogue and `inception-state approve` are invoked on a real target project; `init` and `discovery` explicitly verify-and-promote the same approved decisions into the ordinary installed workflow's constraints. Parent S5 exists even when later Gear 4 coding is headless.
- Why this is / is not agent-owned: model is the proposer/coordinator and may recommend options, but ultimate project identity and altered governing rules require explicit human affirmation; this is an identity-level documentary/operational return, unlike a one-off PR permission prompt.
- Identity / ultimate-policy issue: system purpose and shape, identity/access and security policy, deploy/design boundaries, and changed foundational commitments require a different authorized project charter; this is not mere task approval.
- Ultimate authority in each claimed mode: parent-governed inception is the only claimed positive S5 mode; the actual target-project human owner authoritatively approves complete architecture/policy documents and subsequent foundational revisions, and approves their hub promotion.
- Return-to-operation path: helper-frozen project and verification contract constrain all bootstrap and future material changes; certified `init` and `discovery` promote approved decisions to `.apex/` standards that govern later coverage/CONFLICT classification and code implementation.
- Evidence: [inception human approval/reapproval](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/docs/inception.md), [inception approval commands and scope](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/inception/SKILL.md), [certified policy return](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/scripts/inception-governance.mjs), [verified governance promotion](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/skills/discovery/SKILL.md), [doc-wins policy in normal workflow](https://github.com/steepy-it/steepy-apex/blob/7283b7940e6ec97ec739a28b6de1525d2891bdb4/docs/workflow.md).
- Basis: explicit, parent-governed identity-level choice plus recorded cross-mode return to future agent work.
- Confidence: medium-high for shipped protocol; provenance of a human statement remains an operational trust assumption, as the helper explicitly notes.
- Caveats: commit authorization, ordinary spec acceptance, PR offer, verifier pass/fail, and branch-only blast radius alone would *not* qualify as S5. The credited S5 path is deeper inception identity/reapproval → certified governed hub; it is not Steepy's OSS license/maintainer policy.

## Recursion

One user project's workflow is the parent system considered here. Specialist coding tasks and their reviewed changes are S1 operations. Gear 3 model coordinator and separate model reviewers provide live project-wide regulation and complementary audit; Gear 4 selectively replaces discretionary current-run control with a deterministic budget/verifier but does not erase Gear 3's supported model-owning mode. Inception's human authority is at a parent recursion for project technology adaptation and identity, and may persist after the first app through a certified hub governance path. Steepy product releases/marketplace governance are adjacent and not credited as extra recursive systems.

## Variety and escalation

A task specialist absorbs local file/test variety. The whole-branch reviewer notices interference across earlier/later tasks and returns a specific issue artifact to a specialist; the model implement manager controls current plan resources and corrective dispatch. Separately, externally verified foundations and ultimate project architecture can be changed only by explicit parent dialogue/approval and then returned to the current app/hub. Gear 4's loop records immutable attempts, deterministic verifier/keep-discard and reviewer outcomes; neither an anomalous status line nor a budget monitor becomes autonomous S3/S4/S5. Uncertain effects and unapproved scope stop rather than silently expand authority.

## Evidence gaps

- No authenticated live Claude/Codex/OpenCode/Pi/DeepSeek task or paid model invocation occurred. Source and fake-runner tests support first-party reachability but not production provider success, and headless Gear 3/4 explicitly exclude Pi/DeepSeek.
- Task and final review are separate model contexts on hosts with task dispatch; manual fallback may run a dedicated same-session pass, which is not equivalent to independent S3*.
- S2 relies on at least two differently scoped S1 changes in one branch; a single-task Gear 2 shortcut and a mechanically passing Gear 4 verifier alone do not show inter-S1 regulation.
- S3=A credits the Gear 3 model plan-wide supervisor and its actual corrective/tier/resource decisions, *not* the Gear 3 JavaScript phase sequence or Gear 4's deterministic terminal controller.
- S4=P is narrowly the supported inception external-tech research → parent version/architecture choice → sealed bootstrap, not persistent self-updating market intelligence. S5=P is the substantial foundational identity change → parent approval → certified governance return, not routine task/PR permission.
