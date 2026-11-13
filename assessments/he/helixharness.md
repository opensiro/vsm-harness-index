---
harness_id: helixharness
project_name: HelixHarness
repository: https://github.com/didi/helixharness
review_ref: 8b23069fb464104ce556798ec69737f7eba469b3
reviewed_at: 2026-11-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: P
---

# HelixHarness

## Review boundary

- System in focus: installable `helixharness/` Codex/Claude Code plugin, including explicit optional companion `helixharness-platform/` for first-party framework evolution; not all user projects or the external base coding-agent host.
- Purpose and identity: turn project constraints and requirements into completed verified software changes, coordinate Workspace service delivery, and optionally test evidence-backed improvements to the framework.
- Relevant environment: supported Codex/Claude Code plugin runtime and model, application Git repositories, Python scripts, optional companion Python web/evaluation Workers, credentials and human project/framework operators.
- Standard-distribution boundary: plugin public commands, host-mapped workflows, skills and Python control scripts; optional installed Platform evaluation/evolution code and documented user flows. Demo data are not real operational proof.
- Credited operating / distribution surfaces: Propose/Apply/Archive, Workspace RepoJob dispatch, independent code-review skill, versioned knowledge/Specs, and the optional framework evaluation/evolution pipeline.
- Adjacent first-party surfaces excluded from ownership: example application business code, synthetic Demo evidence, tests/CI, developer-only workflows and external Codex/Claude model/host internals; framework publication outside Platform.
- First-party operating / deployment modes considered: installed single-project plugin; multi-repo Workspace host-native subagents; explicit host incapable fallback; optional self-hosted Platform with configured evaluation Worker and enabled evolution. Telemetry disabled by default.
- Recursion level: one project or Workspace delivered by an agent host (project S1 cells); optional platform is a separate first-party framework-maintainer loop whose evidence informs prospective framework capability, not arbitrary customer code acceptance.
- Reviewed revision: 8b23069fb464104ce556798ec69737f7eba469b3.
- Observation date: 2026-11-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Public plugin commands invoke a deterministic workflow router, then a selected `workflows/single/` or `workflows/workspace/` contract inside Codex/Claude Code. Agents create Specs and Tasks, perform TDD implementation, use real host-native isolated reviewers and seal accepted archive evidence/knowledge. Workflow scripts manage staged state, scope hashes, receipts and resumable errors. The Workspace registry defines repo ownership/dependencies and emits RepoJobs; parent model coordinator spawns/waits and independently checks completion. Optional Platform has usage, Case/Run evaluation, evaluation Workers and evolution service with eligibility, hypotheses, candidates and human-directed experiment. Source: [docs/user-guide.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/docs/user-guide.md), [helixharness/scripts/workflow_router.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/scripts/workflow_router.py), [helixharness/reference/workspace-repo-dispatch.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/reference/workspace-repo-dispatch.md), [helixharness-platform/evolution/service.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness-platform/evolution/service.py).

## Operational model

The host coding agents own actual implementation, scoped cross-repo coordination and independent reviewer judgments under first-party plugin contracts. Deterministic script validation and scheduling do not themselves own decisions. Project operator retains present whole-project intervention and policy authority. Platform can construct prospective capability candidates; final adoption to the shipped plugin is a separate maintainer act, so no automatic S4=A or P claim is made.

## S1 — Operations

- State: A
- Function: Host-agent-directed specification, implementation, testing and archiving of a concrete software feature.
- Disturbance / variety regulated: Changing requirements, repository code/constraints, failing tests, changed review scope and incomplete task evidence.
- Decisive decision or feedback right: Host coding agent chooses feature decomposition, implementation edits, tests and review remediation within the loaded first-party workflow.
- Decision owner: Codex/Claude Code agent executing shipped HelixHarness command/workflow as a supported host plugin mode; human supplies objectives and special decisions.
- Supporting / enforcement mechanisms: Workflow router, Spec/Tasks state, lifecycle scripts, validation receipts, knowledge/context loading, TDD hooks and evidence ledger.
- Closure path: Propose produces Spec/Tasks → Apply model edits code and gets tests/reviewer feedback → repair or human decision → Archive seals verified task and relevant knowledge for later features.
- Boundary reachability: Public plugin commands bind to source-shipped single/workspace workflows and execute within supported Codex/Claude Code sessions; external model host supplies reasoning but first-party plugin instantiates task-specific role/procedure and closure.
- Why this is / is not agent-owned: Removing the coding model leaves deterministic stage/receipt validators, not an owner that can implement new functionality or choose issue-specific code changes.
- Evidence: [helixharness/commands/propose.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/commands/propose.md), [helixharness/commands/apply.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/commands/apply.md), [helixharness/workflows/single/apply.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/workflows/single/apply.md), [helixharness/scripts/workflow_router.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/scripts/workflow_router.py), [docs/user-guide.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/docs/user-guide.md)
- Basis: structural
- Confidence: high for supported composition
- Caveats: No live Codex/Claude feature implementation executed; requires installed supported host plugin and configured model.

## S2 — Coordination

- State: A
- Function: Coordinate distinct repository S1 workers in a multi-repository Workspace according to dependency and exclusive ownership constraints.
- Disturbance / variety regulated: Parallel repo changes can overlap ownership, consume outputs in incorrect order or race parent edits.
- Distinct S1 units: Independent per-repository RepoJobs with agent-owned Propose/Apply/Archive work.
- Inter-S1 disturbance: A downstream service depends on a not-yet-ready upstream service; two workers writing the same repository would collide.
- Attenuating coordination relation: Workspace Coordinator constructs a dependency-aware wave, launches isolated RepoJobs with single owner per repo, waits for native terminal results and recomputes plan on validated completion or blocker.
- Feedback into subsequent S1 behaviour: Failure/needs_input blocks dependent successors; successful independent completion checks enable eligible following RepoJobs and update the root feature state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The documented single-owner, dependency/forbidden-scope and validated-return rules regulate real interference between concurrent S1 code units; source scripts reject dependency cycles.
- Decisive decision or feedback right: Model-operated Workspace parent selects valid dispatches and revises work frontier from source-verified job outcomes.
- Decision owner: First-party Workspace Coordinator role instantiated in supported coding-agent host; deterministic DAG/validation enforces bounds.
- Supporting / enforcement mechanisms: Workspace registry, RepoJob contract, dependency DAG, host-native spawn/wait mapping, read/write scopes and independent completion_check.
- Closure path: Root Spec+repo graph → Coordinator waves → repo-level agent work → native terminal and source check → reconstructed plan changes later S1 dispatch.
- Boundary reachability: Shipped workspace workflow and scripts create jobs and host-contract mapping, requiring a supported host-native subagent facility or documented serial unavailable fallback.
- Why this is / is not agent-owned: Static DAG sorting alone is not S2 autonomy; the bounded coordinating host agent handles actual job assignment, agent callbacks and failed dependencies.
- Evidence: [helixharness/reference/workspace-repo-dispatch.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/reference/workspace-repo-dispatch.md), [helixharness/scripts/workspace.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/scripts/workspace.py), [helixharness/reference/subagent-runtime-protocol.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/reference/subagent-runtime-protocol.md), [docs/user-guide.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/docs/user-guide.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Single-repo deployments lack this inter-repo S2 witness; Workspace mode is explicitly supported but host capabilities/actual concurrency vary.

## S3 — Inside-and-now control

- State: P
- Function: Parent oversight of current project/Workspace commitments and framework evaluation resources.
- Disturbance / variety regulated: Blocked features, incomplete review evidence, mismatched dependency progress, evaluation capacity and budget contention.
- Whole-system current view: Status lists active feature progress, blockers, dependencies and next steps across Workspace; optional platform shows evaluation runs, worker slots and budgets.
- Current-control decision scope: Human selects which feature to continue/repair, grants scope/baseline waivers or changes the evaluation Worker pool and resource budgets.
- Decisive decision or feedback right: Change present project commitments/resource constraints after examining aggregated state, rather than merely approve one code change.
- Decision owner: Human developer/team or framework-maintainer parent using supported status/platform controls.
- Supporting / enforcement mechanisms: Status script, Workspace plan, stage receipts, review gates, platform run/resource configuration.
- Closure path: Parent views Workspace/project or platform current progress → chooses change in active work or capacity → plugin workflow or platform settings execute → next jobs/runs use changed commitment.
- Boundary reachability: The plugin's status and task-update commands are shipped; optional self-hosted platform has documented UI/config and Workers. Human intervention is explicit rather than a claimed autonomous S3 manager.
- Why this is / is not agent-owned: No supported agent autonomously owns allocation of the entire team's resource commitments; scripts/queues enforce the human's choices.
- Evidence: [helixharness/commands/status.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/commands/status.md), [helixharness/scripts/project_status.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/scripts/project_status.py), [helixharness/scripts/workspace.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/scripts/workspace.py), [docs/user-guide.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/docs/user-guide.md)
- Basis: structural
- Confidence: medium
- Caveats: Single-feature approvals alone would not suffice; credited P concerns whole-Workspace/project status and current intervention. The optional platform has a distinct maintainer operating focus.

## S3* — Complementary audit

- State: A
- Function: Independent first-party code review of S1 implementation claims against direct diff, project Standards and requested Spec.
- Disturbance / variety regulated: Implementer may assert tests passed while code violates standards or misses requirements.
- Claim being audited: That the Apply implementation satisfies the feature Spec and repository engineering constraints.
- Ordinary reporting path: Implementer completion, tests, Tasks state and verification artifacts.
- Complementary access path: Frozen Review Bundle of actual git diff/working-tree scope, Spec, source Standards and independent test result; two read-only reviewer agents independently inspect the code.
- Independence boundary: Standards and Spec agents are separately spawned in isolated contexts, read-only, never the Implementer context; unavailable host isolation yields BLOCKED, not self-review.
- Who acts on findings: Implementer repairs MUST_FIX and runs new complete review; DECISION_NEEDED returns to human; only separate APPROVE axes enable Evidence and Archive.
- Decisive decision or feedback right: Each independent reviewer agent issues reasoned evidence-backed verdict on its own axis; parent workflow accepts/rejects changes and repeats based on returned findings.
- Decision owner: Two dedicated host-native subagent review instances instantiated by the first-party code-review skill; neither implementer nor deterministic checker supplies their discretionary verdict.
- Supporting / enforcement mechanisms: Review fixed point, frozen git snapshot, source-scope hash, reviewer role contract, separate verdict logs and evidence receipts.
- Closure path: Implementation → frozen actual-code evidence → independent Standards/Spec judgments → targeted repair or allowed continuation → rerun tests and review → accepted/blocked archive path.
- Boundary reachability: Apply requires the shipped code-review skill and true native parallel isolated reviewers in a supported host; missing capability blocks instead of faking independence.
- Why this is / is not agent-owned: Deterministic scope and tests are support; two distinct review agents judge actual implementation vs independent evidence and return corrective findings.
- Evidence: [helixharness/skills/code-review/SKILL.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/skills/code-review/SKILL.md), [helixharness/workflows/single/apply.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/workflows/single/apply.md), [helixharness/reference/subagent-runtime-protocol.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/reference/subagent-runtime-protocol.md), [helixharness/scripts/workflow.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/scripts/workflow.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-first review does not itself attest a live independent review run, so host-native reviewer availability remains an execution precondition.

## S4 — Outside-and-then intelligence

- State: C
- Function: Construct a prospective framework-improvement cycle from external usage and benchmark evidence, not just current user coding work.
- Disturbance / variety regulated: Changing usage pain points, rework, capability regressions and new framework requirements outside an individual feature task.
- External distinction: Usage ledger and linked telemetry from application repositories plus controlled version/Case evaluation results.
- Future / prospective distinction: Improvement hypotheses and candidate commits are about what future HelixHarness framework capability should change, rather than finishing the current feature.
- Adaptation option generated: Platform evolution analyzer proposes an evidence-linked hypothesis, candidate builder constructs an isolated change, and evaluation compares frozen Base/Candidate Cases.
- Path back into current capability / S3: A candidate/version and its verdict are presented to a maintainer for a separate decision to publish/adopt into live plugin; the first-party platform stops short of autonomous or parent-complete production integration.
- Decisive decision or feedback right: Prospective option formation/evaluation is first-party and model-supported, but enduring framework adoption remains a separately composed maintainer/git workflow.
- Decision owner: First-party evolution analyzer and candidate builder provide an S4-specific constructor; final source publication owner must be supplied outside this pipeline.
- Supporting / enforcement mechanisms: Telemetry consent, evidence eligibility, capability catalog, frozen Case/Run, separate Workers, scheduler and evaluated candidate ref.
- Closure path: Usage/evaluation evidence → hypothesis → candidate commit → matched independent evaluation/verdict → proposed capability decision handoff; external maintainer must complete integration.
- Boundary reachability: Optional installed platform exposes EvolutionService, scheduler and worker pool with documented configurations; not an imagined future extension, though disabled by default.
- Why this is / is not agent-owned: Option generation can be agent-driven but effective published-capability adaptation is not autonomously closed by the platform; C preserves this missing final composition.
- Evidence: [helixharness-platform/evolution/service.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness-platform/evolution/service.py), [helixharness-platform/evolution/candidate.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness-platform/evolution/candidate.py), [helixharness-platform/evolution/scheduler.py](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness-platform/evolution/scheduler.py), [docs/user-guide.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/docs/user-guide.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Default scheduler off; matching calibrated Cases and configured model/Workers are required. Clicking Adopt enters an experiment, not automatic publication to live plugin. No provider-backed evolution run verified.

## S5 — Policy and identity

- State: P
- Function: Parent-governed team engineering mission/constraints and legitimate boundaries of what the coding harness may do.
- Disturbance / variety regulated: Conflicting requests against team rules, changes to accepted knowledge, unauthorized work scopes and decisions to waive project constraints.
- Identity / ultimate-policy issue: Which engineering principles, accepted specification, workflow rights and durable project knowledge govern the agent across tasks.
- Ultimate authority in each claimed mode: Human project owner sets binding Harness/project constraints, chooses feature scope and can confirm or refuse adding knowledge; agent cannot unilaterally redefine the enduring charter.
- Return-to-operation path: Owner-approved Constraints/Spec/Knowledge documents and explicit decision receipts are persisted into application repository; later Propose/Apply reads applicable indexes and constraints.
- Decisive decision or feedback right: Human maintains the standing project identity/charter and decides material changes to it rather than ordinary model-level implementation choices.
- Decision owner: Project owner/team parent in the supported supervised plugin mode.
- Supporting / enforcement mechanisms: Document loading protocol, Spec/Tasks receipts, archive acceptance, stage/decision gates, host permissions and versioned knowledge indexes.
- Closure path: Policy-level project issue → owner decision on binding requirement or durable Knowledge → accepted repository artifact → later agent workflow loads it as normative constraint and alters decisions.
- Boundary reachability: The plugin's Init/Propose/Archive workflows read and write these installed project constraints; explicit owner approval gates remain part of normal supported mode.
- Why this is / is not agent-owned: The agent implements within frozen constraints; it does not hold legitimate ultimate authority to waive or rewrite the team's standing engineering charter.
- Evidence: [helixharness/reference/loading-protocol.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/reference/loading-protocol.md), [helixharness/workflows/single/archive.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/workflows/single/archive.md), [helixharness/workflows/single/propose.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/helixharness/workflows/single/propose.md), [docs/user-guide.md](https://github.com/didi/helixharness/blob/8b23069fb464104ce556798ec69737f7eba469b3/docs/user-guide.md)
- Basis: structural
- Confidence: medium
- Caveats: Parent charter closure is scoped to one project/team; generic permissions or an unconfirmed knowledge suggestion alone are not credited as S5.

## Distributed OSS parent arrangement

This assessment credits a supported one-project/team supervisory parent and locally configured Platform maintainer. Independent OSS contributors do not automatically constitute a shared organization-wide S5 decision-maker. The Platform's candidate experiment owner is not the authority to publish the public HelixHarness plugin.

## Recursion

Single-project feature work is S1. In multi-repository Workspace mode, per-repo S1 cells are coordinated through parent RepoJobs and independent checks. Optional Platform supports the framework-improvement recursion, whose public software artifact can be adopted by a distinct maintainer process.

## Variety and escalation

Spec and Harness constraints bound what coding agents may do. Workspace dependencies and ownership attenuate clashes between service-level tasks. Independent reviewers inspect actual diff against two separate standards, then return MUST_FIX or DECISION_NEEDED rather than permitting a self-approved closure. Project status and platform dashboards inform parent choices. Evolution evidence may generate future framework candidates, but adopting an evaluated candidate for a trial is not silently equated with publishing a new framework version.

## Evidence gaps

- No provider-backed Codex/Claude host run, multi-repo native subagent wave, or real Platform evaluation/evolution was executed here; source paths and documented supported modes establish constructor/reachability.
- Independent reviewers are first-party role/wiring, but a deployment lacking isolated parallel host-native subagents must fail closed.
- S3 P is scoped to parent whole-project/Workspace status decisions, not merely one user approval.
- S4 C specifically records a prospective candidate/evaluation constructor without claiming completed automatic live-code adoption.
