---
harness_id: harness-kit
project_name: Harness Kit
repository: https://github.com/deepklarity/harness-kit
review_ref: 87305cd35cba8e75194a50d6dd301c6dd52a69c9
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Harness Kit

## Review boundary

- System in focus: one Harness Kit software-engineering organization at pinned revision `87305cd35cba8e75194a50d6dd301c6dd52a69c9`, centered on the first-party `odin` planner/orchestrator and `taskit` durable board/control plane, including task DAGs, assignment/routing, worktree/sandbox lifecycle, liveness/retry, reflection/rework, merge/integration, proof/evidence and operator-question paths. The official Pattern Engineering adoption flow is considered as a second supported distribution mode where relevant.
- Purpose and identity: organize AI coding workers into auditable software-delivery work: decompose a current goal, allocate work, prevent or absorb cross-worker interference, execute in isolated environments, independently review claims, merge accepted work, recover failed runs and optionally adapt a target repository's engineering environment through the shipped adoption procedure.
- Relevant environment: operator specifications and replies, target source repositories, Git/worktrees, TaskIt state, configured Claude/Codex/Gemini/GLM/MiniMax-style worker harnesses, provider quota/cost/availability, execution infrastructure, screenshots/proof and the external target repository inspected by the Pattern Engineering adoption mode.
- Standard-distribution boundary: first-party `odin`, `taskit`, shipped runtime configuration, standard documentation and the documented Pattern Engineering Quickstart/adoption procedure. External coding-agent CLIs/models are operating actors reached by Harness Kit but their vendor-internal reasoning loops, memory, tool policy and provider-side control are not inherited as Harness Kit metasystem functions.
- Credited operating / distribution surfaces: root `README.md`; `odin/README.md`; `odin/docs/sample_flow.md`; `odin/docs/philosophy.md`; `odin/src/odin/agent_routing.py`; `odin/src/odin/orchestrator.py`; `odin/src/odin/reflection.py`; TaskIt dependency/DAG-executor/views/state machinery; `docs/breadcrumb_analysis/spec-task-lifecycle/03-reflection-loop/{FLOW,DETAILS}.md`; `docs/breadcrumb_analysis/task-liveness-retry/FLOW.md`; `docs/breadcrumb_analysis/quota-failover-reassignment/FLOW.md`; `docs/breadcrumb_analysis/git-worktree-isolation/`; `docs/Quickstart.md` and its shipped adoption checklist/procedure.
- Adjacent first-party surfaces excluded from ownership: `docs/fable_roadmap/` self-development plans/audits and repository-maintainer dogfood are corroborative only; CI/release/contributor activity, tests, replay scripts and historical bootstrap traces do not become runtime owners merely by co-location. Root maintainer instructions and repository-local development waves are not borrowed into a downstream installation unless separately exposed by the documented distribution mode.
- First-party operating / deployment modes considered: all-in-one `odin run`; staged `odin plan → review/override → exec`; TaskIt board-driven execution; dependency-wave execution with isolated worktrees/sandboxes; automatic reflection/rework/merge; liveness and retry/reassignment; blocking operator questions; and the documented read-only audit → human decision → adoption → re-score Pattern Engineering flow.
- Recursion level: one Harness Kit project/spec organization is the system-in-focus. Distinct task workers are S1 units when they own separate software-work outcomes. Odin/TaskIt planning, coordination, current control and review paths are evaluated as metasystem functions at that project/spec recursion.
- Reviewed revision: `87305cd35cba8e75194a50d6dd301c6dd52a69c9`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Harness Kit is a local, MIT-licensed software-engineering harness suite. `odin` turns a specification into a dependency graph, suggests worker assignments, executes ready tasks through pluggable coding-agent harnesses and records results. `taskit` supplies the durable board/API/state machine, status history, proof, comments, reflection reports and automated dispatch/recovery. Each task can run in an isolated worktree/sandbox and accepted task branches merge into a spec branch before downstream dependencies become runnable.

The external worker CLIs remain separate operational engines. Harness Kit supplies the organization around them: task boundaries, assignment, dependency order, worktree and microVM lifecycle, execution fencing/liveness, provider failover, review, merge and evidence. This assessment therefore credits worker model actors as the operational S1 actors reached by the standard Harness Kit organization, but does not import their internal vendor capabilities as S2-S5.

The repository also ships a separate Pattern Engineering adoption path. A coding agent follows `docs/Quickstart.md`, performs a read-only evidence audit of a target repository, writes scored findings and explicit adaptation decisions, stops for the human to mark yes/no/later, then applies only approved changes and re-scores. That distribution path matters for S4 parent ownership but is not used to infer autonomous S4 from repository dogfood.

## Operational model

In quick mode, the base planning agent reads the current specification, decomposes it into tasks, declares dependencies and supplies per-task judgment that can override the history-driven router. Tasks then execute in dependency-respecting waves. Independent units may run concurrently; dependent units wait until upstream work has passed review and merged. Worktree isolation keeps concurrent work separate and the post-review merge gate makes accepted upstream content available to later workers.

In staged mode, the same plan is exposed to the operator before execution. The operator can inspect assignments, dependencies, costs/quota reasoning and current task state, reassign workers, add dependencies or otherwise adjust the current plan. During execution, deterministic TaskIt machinery enforces concurrency, dependency, memory, timeout and liveness policies; these mechanisms are treated as support/enforcement rather than autonomous organizational owners.

Successful worker execution enters REVIEW rather than immediately completing. A separate reflection invocation reads the task detail, comments, direct proof/screenshots and execution output in a read-only workspace and produces PASS / NEEDS_WORK / FAIL. PASS merges before the task advances; NEEDS_WORK/FAIL reopens the task and puts the review finding at the head of the next execution prompt. This supplies the complementary S3* loop.

## S1 — Operations

- State: A
- Function: perform bounded software-engineering tasks that directly produce implementation, analysis, testing, documentation or other project outcomes admitted by the current spec/task organization.
- Disturbance / variety regulated: heterogeneous software requirements, repository state, failing tests/tools, implementation choices and task-local environmental conditions.
- Decisive decision or feedback right: choose the substantive action sequence inside an assigned task — code/search/tool choices, implementation steps, debugging actions and the task result/proof to return.
- Decision owner: the configured autonomous coding-agent/model actor launched for the task through a Harness Kit harness adapter.
- Supporting / enforcement mechanisms: Odin task briefs and harness adapters, per-task worktrees/sandboxes, TaskIt task state, MCP status/proof submission, execution fencing, timeouts and result persistence.
- Closure path: current spec/plan admits a task → Harness Kit dispatches the configured worker into its task environment → worker autonomously performs the work and returns result/proof → TaskIt records the result and the task enters the review/merge path consumed by subsequent project operation.
- Boundary reachability: `odin run` / `odin exec` are standard documented modes that launch configured external coding-agent CLIs or APIs as task workers and return their outputs through first-party task state. No autonomous S1 is borrowed from a maintainer-only dogfood path.
- Why this is / is not agent-owned: Harness Kit's scheduler and sandbox enforce the task boundary, but the material operational action sequence is selected by the model actor executing the task.
- Evidence: [root README](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/README.md); [Odin README](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/README.md); [sample flow](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/docs/sample_flow.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the external worker implementation is not first-party Harness Kit code; this claim is limited to autonomous operational work made reachable and organizationally closed by Harness Kit's standard task-execution boundary.

## S2 — Coordination

- State: A
- Function: attenuate interference among distinct task-worker S1 units by deciding which work may proceed concurrently and which work must be dependency-ordered when their effects would conflict.
- Disturbance / variety regulated: sibling workers that would modify the same file or otherwise depend on one another can race, create incompatible concurrent edits or start from repository state that does not yet contain required upstream work.
- Decisive decision or feedback right: during autonomous planning, decide the task dependency graph and parallel/sequential assumptions for the current spec; in particular, shared-file work is represented as a dependency chain rather than a same-wave parallel set.
- Decision owner: the base planning model actor in the documented all-in-one planning mode.
- Supporting / enforcement mechanisms: explicit `depends_on` edges, DAG validation, deterministic wave scheduling, per-task worktree isolation, merge serialization and the rule that REVIEW does not unblock dependents; TESTING/DONE are the post-merge completion states.
- Closure path: planner distinguishes independent versus interfering/dependent tasks → writes dependency relations into the task plan → scheduler withholds blocked S1 units → upstream work passes review and merges → downstream worktree is created from the updated spec branch → subsequent S1 behavior runs against the coordinated state.
- Boundary reachability: quick mode (`odin run`) automatically performs decompose → assign → execute; the documented planner creates task dependencies and its assumptions about parallel safety are stored as plan reasoning. The dependency and post-merge gates are first-party runtime machinery in the standard full-kit path.
- Distinct S1 units: separate coding-agent task executions belonging to the same current Harness Kit spec/project organization.
- Inter-S1 disturbance: two task workers writing the same file are explicitly documented as a shared-file conflict; running a dependent worker before upstream merge would also make it act against missing upstream code.
- Attenuating coordination relation: planner-owned dependency/chaining decision, enforced by DAG wave gating and isolated worktrees rooted from the spec branch only after dependencies merge.
- Feedback into subsequent S1 behaviour: the coordinated dependency result changes when a downstream worker is allowed to start and changes the repository state/context it receives; it starts only after the predecessor's accepted content has merged.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive witness is not task plurality or a generic DAG edge. It is tied to a specific structurally documented interference class — concurrent shared-file / upstream-state conflict among sibling S1 work cells — and to a relation that deliberately converts that unsafe parallelism into ordered execution with changed downstream context.
- Why this is / is not agent-owned: deterministic DAG machinery enforces the selected relation, but the standard quick path gives the planning model the material discretion to decompose work and choose dependency/parallel assumptions. The docs explicitly describe these as LLM planner assumptions that a human may later correct in staged mode.
- Evidence: [sample flow — shared-file conflict and waves](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/docs/sample_flow.md); [Odin philosophy — LLM parallel/conflict assumptions](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/docs/philosophy.md); [git/worktree isolation flow](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/breadcrumb_analysis/git-worktree-isolation/FLOW.md); [reflection dependency gate](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/breadcrumb_analysis/spec-task-lifecycle/03-reflection-loop/FLOW.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: merge-conflict resolution and generic worktree isolation are not independently treated as S2. The classification rests on planner-owned coordination of the documented inter-S1 shared-file/upstream-state disturbance and its closed dependency feedback path.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current project commitments and shared execution resources by constructing the current whole-spec work plan, allocating task workers and allowing either autonomous planner control or explicit operator override before/while current work proceeds.
- Disturbance / variety regulated: a current spec contains multiple commitments competing for agent capability, provider quota/cost, dependency order and limited execution capacity; assignments can also become unsuitable as current worker availability changes.
- Decisive decision or feedback right: base mode — the planning model decides the current task decomposition/dependencies and can make per-task worker judgments that override the history-based router; parent mode — the operator inspects the whole plan/current board and reassigns or changes dependency/current execution choices.
- Decision owner: base mode — the planner model actor; parent mode — the project operator using the staged workflow/board.
- Supporting / enforcement mechanisms: board/spec state, routing history and quota/cost data, deterministic `agent_routing` fallbacks, concurrency and memory gates, liveness/retry/reassignment policy, task status machine and scheduler.
- Closure path: current spec + available organization → planner or operator selects task commitments/assignment/dependency control → choices persist in TaskIt/Odin task state → deterministic dispatcher enforces them → subsequent current task execution follows the selected assignment/order; staged operator changes replace the earlier suggestion before later operation.
- Boundary reachability: both `odin run` (autonomous planning path) and `odin plan`/`status`/`assign`/`exec` (parent-supervised path) are documented standard modes. `agent_routing.py` explicitly states that planner-suggested per-task judgment wins before the history-driven phase, while the staged workflow exposes the plan for operator intervention.
- Why this is / is not agent-owned: liveness, quota thresholds, concurrency caps and scheduler transitions are not counted as autonomous S3 owners. `A` is attributed to the planning model's whole-current-plan allocation judgment; the runtime only persists/enforces it. The separate staged mode returns that current-control right to the operator.
- Evidence: [sample flow](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/docs/sample_flow.md); [Odin philosophy](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/docs/philosophy.md); [history-driven routing](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/src/odin/agent_routing.py); [task liveness/retry](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/breadcrumb_analysis/task-liveness-retry/FLOW.md); [quota failover](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/breadcrumb_analysis/quota-failover-reassignment/FLOW.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic failover and retry are supporting current-control mechanisms, not the reason for `A`. The autonomous claim is the planner-owned current allocation/commitment judgment visible before enforcement.
- Whole-system current view: the planner constructs the current spec's task graph and assignment picture; the staged operator sees the task table/board with assignments, dependencies, statuses, quota/cost reasoning and blocks across the current project.
- Current-control decision scope: current task commitments, worker allocation, dependency constraints and intervention/reassignment for work that is about to run or is being reworked.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | planning model actor | a current spec enters `odin run` / planning and must be decomposed and allocated | planner emits task/dependency/worker judgments; TaskIt/Odin persists them and dispatcher executes later work under those choices | `odin/docs/sample_flow.md`; `odin/src/odin/agent_routing.py`; `odin/docs/philosophy.md` |
| Parent (`P`) | project operator | staged plan/current board is reviewed or current assignment/dependency needs intervention | operator changes assignment/dependency/current-control choice; persisted task state drives subsequent execution under the returned decision | `odin/docs/sample_flow.md`; `odin/docs/philosophy.md` |

## S3* — Complementary audit

- State: A
- Function: independently challenge a producing worker's implicit claim that its task result is acceptable enough to integrate, using direct evidence beyond the producer's ordinary result/status report.
- Disturbance / variety regulated: worker output may be incomplete, incorrect or insufficiently evidenced even when execution exits successfully and reports a result.
- Decisive decision or feedback right: inspect the current attempt through a separate read-only reviewer invocation and return PASS, NEEDS_WORK or FAIL; PASS permits merge/advance, while negative verdicts require another execution attempt or eventually fail the task.
- Decision owner: the autonomous reviewer model actor launched by the reflection path.
- Supporting / enforcement mechanisms: ReflectionReport state, dynamic reviewer selection, separate read-only workspace invocation, direct task-detail/proof/screenshots/execution-output assembly, verdict parser, merge gate, retry count and rework-prompt construction.
- Closure path: producer finishes and task enters REVIEW → separate reviewer directly reads task evidence/workspace context → reviewer returns verdict/finding → PASS merges before TESTING, or NEEDS_WORK/FAIL returns task to IN_PROGRESS → latest finding is put first in the next worker prompt → corrected work returns through REVIEW again.
- Boundary reachability: automatic reflection is wired into the standard TaskIt execution path when a reviewer is available and reflection is not explicitly skipped. The reviewer uses first-party reflection orchestration and the same standard harness registry, not a maintainer-only CI/release path.
- Why this is / is not agent-owned: deterministic backend transitions enforce the verdict, but the material audit judgment is produced by a separate model invocation with direct complementary evidence and a read-only role.
- Evidence: [reflection flow](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/breadcrumb_analysis/spec-task-lifecycle/03-reflection-loop/FLOW.md); [reflection detailed trace](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/breadcrumb_analysis/spec-task-lifecycle/03-reflection-loop/DETAILS.md); [root README](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: reviewer selection may use the same provider family as the producer; the independence claim is organizational/session-role and evidence-access independence, not vendor diversity. Modes with `skip_reflection` or no available reviewer do not supply this S3* path.
- Claim being audited: the producing worker's task-completion/result claim is sufficient and safe enough to merge into the current spec branch.
- Ordinary reporting path: worker execution returns result/output/proof and moves the task from EXECUTING to REVIEW through normal TaskIt/Odin status machinery.
- Complementary access path: the reflection actor fetches task detail/comments, direct proof/screenshots and raw execution output, stages evidence into a read-only review workspace and evaluates the current attempt rather than merely consuming the worker's completion label.
- Independence boundary: reflection is a separate reviewer invocation, with `read_only_workspace=True`, distinct report state and a review-specific prompt; it does not ask the producing execution to self-certify its own status.
- Who acts on findings: TaskIt applies the reviewer's verdict to merge/advance or re-open/fail the task; on rework, the next execution receives the reviewer finding as the leading corrective directive.

## S4 — Outside-and-then intelligence

- State: P
- Function: inspect an external target repository's engineering environment, develop prospective adaptation options and return a parent-selected subset into changed repository capability.
- Disturbance / variety regulated: the target repository may lack or weakly implement agent entrypoints, testing discipline, verification gates, reusable patterns, evidence practices and other harness-engineering capabilities relevant to future software work.
- Decisive decision or feedback right: decide which proposed practices/skills/configuration changes should actually be adopted into the target repository after the read-only audit.
- Decision owner: the human/operator who reviews `report.md` / `action-items.md` and marks each proposed adaptation yes/no/later.
- Supporting / enforcement mechanisms: the shipped eleven-area audit checklist, evidence folder/tracker, scored report, explicit decision list, portable skills/presets, Step 3 adoption procedure and Step 4 re-score/close loop.
- Closure path: coding agent reads the external target repo → builds evidence and scored findings → develops concrete adaptation options → stops and exposes them to the parent → human selects changes → agent edits only the approved surfaces → re-scores touched areas → subsequent agent work operates in the changed repository environment.
- Boundary reachability: root README explicitly presents the Pattern Engineering Quickstart as a usable part of Harness Kit without installing the full runtime; `docs/Quickstart.md` is the first-party executable procedure that a coding agent is instructed to follow in the target repository.
- Why this is / is not agent-owned: the agent autonomously senses the target and develops options, but the standard procedure explicitly forbids adoption before the human marks the decision list. The decisive adaptation judgment therefore remains parent-owned; no separate first-party autonomous or constructor ownership mode is needed to close this published S4 path.
- Evidence: [Pattern Engineering Quickstart](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/Quickstart.md); [root README](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/README.md); [hk-compound skill](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/.claude/skills/hk-compound/SKILL.md) as supporting future-reuse machinery only.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary reflection, routing history, flow traces and pattern accumulation are not independently counted as S4 merely because they influence future work. The positive mapping rests on the official outside-target audit/adaptation loop and its explicit parent decision boundary.
- External distinction: the adoption agent reads and scores the target repository as an environment separate from the Harness Kit source/distribution, gathering target-specific evidence rather than reusing only internal runtime history.
- Future / prospective distinction: the report identifies missing/weak engineering capabilities and proposes changes intended to improve future agent/software work, then Step 4 measures the post-adoption capability state.
- Adaptation option generated: per-item yes/no/later decisions over concrete changes such as agent entrypoints, portable skills, verify gates, testing process, pattern habits and presets, each with rationale and effort.
- Path back into current capability / S3: parent-approved decisions become actual edits to the target repository's agent/tool/process surfaces; the procedure then re-scores affected areas and closes the adoption loop before later operation.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity / ultimate-policy closure is established at the reviewed boundary.
- Disturbance / variety regulated: not established for S5. Specifications, task questions, worker/model selection, engineering tenets and Pattern Engineering adoption decisions regulate operational/current/adaptation variety rather than a dispute over the identity or ultimate policy of the Harness Kit organization.
- Decisive decision or feedback right: no supported runtime path was found in which an identity/ultimate-policy matter is surfaced to an internal agent or legitimate parent authority and returned as an authoritative identity-level decision governing subsequent operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: static project philosophy/configuration, operator task/spec input, board questions, assignment/dependency override and Pattern Engineering approval surfaces can constrain behavior but do not establish an S5 owner.
- Closure path: not established.
- Why this is / is not agent-owned: the reviewed positive human decision paths close S3 current-control or S4 adaptation choices. Treating an ordinary spec, provider selection, task approval or adoption checkbox as S5 would collapse operational governance into identity policy contrary to the Profile.
- Evidence: [Odin philosophy](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/docs/philosophy.md); [sample flow](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/odin/docs/sample_flow.md); [Pattern Engineering Quickstart](https://github.com/deepklarity/harness-kit/blob/87305cd35cba8e75194a50d6dd301c6dd52a69c9/docs/Quickstart.md); root configuration/operator-question surfaces.
- Basis: explicit absence review.
- Confidence: high.
- Caveats: this is a boundary-relative no-material-path conclusion, not a claim that operators or maintainers lack authority outside the assessed runtime/distribution.

### Absence scope

- Surfaces inspected: root README/Quickstarts; Odin philosophy, plan/execute documentation and routing/control code; TaskIt current-control/reflection/liveness paths; operator-question path; Pattern Engineering audit/adoption procedure; first-party configuration and repository self-development/governance-adjacent material.
- Plausible first-party paths checked: user-supplied spec/mission, planner assumptions and operator replies, provider/model roster/configuration, blocking MCP questions, staged plan approval/override, reflection accept/rework decisions, Pattern Engineering adoption approvals, static philosophy/tenets and repository roadmap/self-dogfood governance.
- Why no material first-party path remains: each plausible path is task-level, current-control, adaptation-level, static configuration or adjacent project-development governance. None supplies the required identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned decision governing subsequent operation at the declared Harness Kit project/spec recursion.

## Distributed OSS parent arrangement

Harness Kit is an OSS project, but this assessment does not infer S3/S4/S5 parent ownership from contributor plurality or maintainer activity. The credited parent modes are local supported operator modes: staged current-control for S3 and the explicit target-repository adoption decision for S4. Repository maintainers, roadmap authors and contributors are adjacent to a downstream Harness Kit run unless the shipped operating mode explicitly returns a decision through them.

## Self-hosted and non-human modes

The full kit is locally/self-hosted and can execute a current plan autonomously after planning. Its staged mode deliberately exposes current-control rights to the operator, producing S3 `A(P)`. The Pattern Engineering mode deliberately retains the decisive adaptation judgment with the operator, producing S4 `P`. No qualifying first-party non-human S5 closure was found.

## Recursion

The assessed recursion is the current Harness Kit project/spec organization. Worker task executions are S1 units when each owns a bounded software outcome. Odin/TaskIt sit above those cells for dependency coordination, current allocation/control and complementary review. The external coding-agent products are not separately assessed recursions here, and their own internal planners, tool loops or memory do not donate S2-S5 to Harness Kit.

## Variety and escalation

Harness Kit attenuates operational variety through task briefs, explicit dependencies, worker routing, isolation and proof. Shared-file/upstream-state interference is converted into ordered dependencies. Current resource and commitment variety is handled through planner judgments plus deterministic quota/history/concurrency/liveness support and optional operator override. Failed completion claims escalate through the reviewer/rework loop; ambiguous execution can ask the operator and block rather than guessing. Infrastructure failures may auto-requeue to a cap; quota exhaustion can trigger same-tier reassignment; unresolved cases are held for a human.

These escalation paths are classified by the organizational function they actually serve. Retry, timeout and quota machinery are not promoted to S3 ownership merely because they can stop/reassign work; operator questions are not promoted to S5 merely because the human has final say over a local event.

## Evidence gaps

- The S3* reviewer selection does not guarantee provider diversity from the producer. Independence here rests on separate review execution, read-only role and direct complementary evidence, not on a different vendor/model family.
- The S2 claim uses the documented standard planner/DAG path and the explicit shared-file/upstream-state conflict witness. It does not claim that every dependency edge is S2 or that the planner detects every possible interaction correctly.
- The S4 `P` classification depends on treating the official Pattern Engineering Quickstart as a supported Harness Kit distribution mode, which the root README explicitly does. Repository-maintainer self-dogfood and roadmap audits are not credited as the S4 owner.
- The frozen revision is assessed exactly as pinned by batch #187; later upstream evolution is outside this standalone artifact and would require a new-ref reassessment.
