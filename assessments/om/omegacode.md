---
harness_id: omegacode
project_name: omegacode
repository: https://github.com/SawyerHood/omegacode
review_ref: 748d686a7950b3466e8d7fd014db32c4fb9fccf5
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# omegacode

## Review boundary

- System in focus: One omegacode JavaScript workflow run and its attached native workers, authoring interface and live run visibility.
- Purpose and identity: Compose durable parallel or staged model work and accept its structured or textual result.
- Environment: Local target repository, tool and agent outputs, configured provider availability, usage limits, partial results and interruption.
- Standard-distribution boundary: CLI, workflow DSL/runtime, journals, worktree allocator, viewer, built-in scripts and authoring skill. Native model clients and the target project are external.
- Credited operating / distribution surfaces: Agent activity and typed result processing, isolated parallel build mode, budget-aware workflow authoring and operator-controlled stop/resume.
- Adjacent first-party surfaces excluded from ownership: Development tests, demos, the maintainers' application code and usage of omegacode to review its own repository.
- First-party operating / deployment modes considered: Built-in or custom workflow, worktree-isolated parallel edits, budget-sensitive composition and CLI-managed continuation of an interrupted run.
- Recursion level: One workflow run is the unit for S3. Separately allocated workers are operational cells within it. The server's list of unrelated runs is not a shared portfolio authority.
- Reviewed revision: `748d686a7950b3466e8d7fd014db32c4fb9fccf5`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

An authored script reaches real provider workers using the workflow DSL. The runtime owns admission, worktree allocation, result journaling and event output. Built-in scripts compose the same calls. [Journal and run setup](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/run.ts#L71-L109) · [Worker execution](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L327-L391) · [Worktree and fan-out return](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L438-L514)

## Operational model

Workers make local task choices. The author sets coordination rules and where aggregate budget evidence may affect later commitments. A CLI operator can observe and stop the run, then decide to resume. [Built-in parallel editing](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/bake-off.workflow.js#L60-L83) · [Budget-aware workflow authoring](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/skill/SKILL.md#L149-L157) · [Run-wide interruption](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/run.ts#L122-L179)

## S1 — Operations

- State: A
- Function: Perform model-led coding, research and review work.
- Disturbance / variety regulated: Task prompts, source state, tool feedback and failed or invalid results.
- Decisive decision or feedback right: Choose and revise local work and tools within the requested scope.
- Decision owner: Native model-backed provider worker launched by the shipped workflow API.
- Supporting / enforcement mechanisms: Provider adapters, phase context, worker journal and syntactic result validation.
- Closure path: The worker returns results and usage. The workflow can feed the result into a subsequent worker or close with a delivered result.
- Why this is / is not agent-owned: The provider worker chooses actions. The DSL selects when it runs and how its output is consumed.
- Evidence: [Worker execution](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L327-L391) · [Built-in parallel editing](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/bake-off.workflow.js#L60-L83) · [Task-defined source research](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/deep-research.workflow.js#L112-L131)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: The provider's own model and tool engine are external dependencies.
- Boundary reachability: Standard CLI loads the workflow, whose bound agent primitive resolves and invokes real provider workers.

## S2 — Coordination

- State: C
- Function: Prevent destructive overlap among parallel branch-editing workers.
- Disturbance / variety regulated: Workers independently implement the same requested change and could write conflicting versions of the same files.
- Decisive decision or feedback right: Assign worker-specific worktree scopes and expose each isolated output for downstream consumption.
- Decision owner: Workflow constructor selects isolation and branch scope. The deterministic runtime allocates and preserves the worktree.
- Supporting / enforcement mechanisms: Unique worktree addresses, branch assignment, scoped worker cwd and teardown mutex.
- Closure path: Each worker acts in its own target tree. The result and journal expose its branch and the runtime preserves dirty or committed trees so subsequent work can use the intended output.
- Why this is / is not agent-owned: The DSL explicitly supplies interference prevention. Defining scope and later reconciliation remains a constructor decision.
- Evidence: [Separate worktree allocation](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/worktree.ts#L41-L70) · [Worktree and fan-out return](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L438-L514) · [Work preservation](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/worktree.ts#L102-L140) · [Built-in parallel editing](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/bake-off.workflow.js#L60-L83)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: This witness is bounded to opted-in isolated editing. It does not claim arbitrary shared-workspace conflict arbitration.
- Boundary reachability: The shipped bake-off workflow invokes worktree isolation in its parallel native-worker launches.
- Distinct S1 units: Independent worker agents making potentially overlapping edits for separately owned alternative deliverables.
- Inter-S1 disturbance: Concurrent implementations writing the same repo paths or colliding in shared worktree setup and teardown.
- Attenuating coordination relation: Allocate a distinct tree and branch per worker, run the worker from that tree and serialize shared Git metadata operations.
- Feedback into subsequent S1 behaviour: Each worker receives its actual isolated cwd and follows it. Its preserved branch is returned for follow-on work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Worktree assignment explicitly displaces competing edits from the shared namespace into distinct execution sites.

## S3 — Inside-and-now control

- State: C(P)
- Function: Regulate current workflow-wide output-token commitments and choose whether to interrupt or continue outstanding work.
- Disturbance / variety regulated: A costly or stalled run can require fewer worker launches or a stop-and-resume intervention.
- Decisive decision or feedback right: Use run-wide consumption and progress to decide the next commitment, or end an active attempt and resume available work with selected execution overrides.
- Decision owner: Workflow constructor defines the discretionary admission response. The CLI operator owns a distinct run-wide stop and resume decision.
- Supporting / enforcement mechanisms: Workflow budget queries, per-agent accounting, fan-out admission gate, live run timeline and journaled continuation.
- Closure path: User-authored workflow code uses aggregate usage and chooses whether to launch another stage. The operator can observe the whole run and interrupt it, after which a same-workflow resume reuses valid results and launches outstanding work under supplied settings.
- Why this is / is not agent-owned: No shipped default model owns a general run-wide budget allocator. Runtime budget gates enforce configuration and workflow code. Operator controls apply direct session-level judgment.
- Evidence: [Workflow-wide budget observables](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L163-L181) · [Budget-aware workflow authoring](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/skill/SKILL.md#L149-L157) · [Worker execution](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L327-L391) · [Observable whole-run state](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/server/serve.ts#L128-L159) · [Run-wide interruption](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/run.ts#L122-L179) · [Run and resume CLI](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/cli.ts#L399-L466) · [Exact-resume guard](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/journal.ts#L153-L179)
- Basis: Explicit and structural.
- Confidence: Medium-high.
- Caveats: CLI viewer is read-only. Stop is run-wide. Same-file and same-arguments resume restrictions apply, despite broader authoring examples. The output-token cap is checked at launch and is not a hard cancellation threshold for workers already running.
- Boundary reachability: Run-wide budget feedback is bound in the executable DSL, with an authoring example showing it drives whether workers start. Operator control reaches the same run through terminal interruption and the shipped journaled CLI resume.
- Whole-system current view: The workflow reads its aggregate spent and remaining token allowance. The supervising operator can observe the visible workflow phases and worker state, results and progress for the current run.
- Current-control decision scope: Scale or end further whole-run branch admissions from the shared output-token budget. The operator can halt shared current commitments and decide whether to resume the same workflow.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Workflow constructor | Current aggregate consumption and remaining allowance approach a chosen threshold | Composed control code starts another worker or ends the loop | [Workflow-wide budget observables](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L163-L181) · [Budget-aware workflow authoring](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/skill/SKILL.md#L149-L157) |
| Parent (`P`) | CLI operator | Whole-run progress or outstanding commitments warrant intervention | User interrupts the run and may resume valid work with allowed execution settings | [Observable whole-run state](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/server/serve.ts#L128-L159) · [Run-wide interruption](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/run.ts#L122-L179) · [Run and resume CLI](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/cli.ts#L399-L466) · [Exact-resume guard](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/journal.ts#L153-L179) |

## S3* — Complementary audit

- State: —
- Function: Independently audit operational claims and return findings to current control.
- Disturbance / variety regulated: Separate workers may reach contradictory findings or miss issues in the same artifact.
- Decisive decision or feedback right: No supplied complementary operational-audit feedback into a run supervisor was found.
- Decision owner: Independent provider reviewers and judge agents perform assigned artifact-review work.
- Supporting / enforcement mechanisms: Read-only full-diff review, structured findings, independent refutations and synthesis.
- Closure path: Reviewers give another reading of an artifact. The supplied reviews terminate at an adjudicated answer or report. They do not deliver a separate audit-triggered change to run governance.
- Why this is / is not agent-owned: The independent review operation is real and can challenge claims. Its supplied integration is within the requested production workflow.
- Evidence: [Independent artifact review and synthesis](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/multi-provider-review.workflow.js#L79-L142) · [Review output](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/code-review.workflow.js#L143-L173) · [Material-disagreement escalation](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/second-opinion.workflow.js#L91-L129) · [Observable whole-run state](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/server/serve.ts#L128-L159)
- Basis: Bounded structural absence.
- Confidence: Medium.
- Caveats: An operator can separately incorporate a review into a supervisory decision after receiving its report.

### Absence scope

- Surfaces inspected: Built-in review, per-finding verification, disagreement escalation, terminal reports and viewer output.
- Plausible first-party paths checked: Exception-triggered audit of a live worker's operational claim, independence from normal reporting and returned adjustment of commitments.
- Why no material first-party path remains: The built-in judgments regulate answer or artifact quality within the production flow. They do not supply a distinct complementary action path to the workflow-wide regulator.

## S4 — Outside-and-then intelligence

- State: —
- Function: Model prospective external change and feed options into the harness's own present capability.
- Disturbance / variety regulated: An external repository or research source may change. Future worker capabilities may require new configuration.
- Decisive decision or feedback right: No supplied workflow makes a prospective harness adaptation decision from external findings.
- Decision owner: Researchers and code workers own assigned task outputs. Workflow authors choose provider and execution setup.
- Supporting / enforcement mechanisms: External source research, pluggable worker factory and static workflow authoring.
- Closure path: Research is summarized for the assigned question. Provider and workflow changes are supplied separately at launch or through authoring.
- Why this is / is not agent-owned: The runtime can execute an environment research task without itself choosing subsequent capability adaptations.
- Evidence: [Task-defined source research](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/deep-research.workflow.js#L112-L131) · [Shipped authoring skill installation](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/cli.ts#L601-L631) · [Run and resume CLI](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/cli.ts#L399-L466) · [Exact-resume guard](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/journal.ts#L153-L179)
- Basis: Bounded structural absence.
- Confidence: Medium-high.
- Caveats: A specially composed workflow can perform foresight for another system.

### Absence scope

- Surfaces inspected: Research workflow, provider selection, authoring surfaces and resume configuration.
- Plausible first-party paths checked: External-trend research connected to a binding choice of future provider, workflow structure or adaptation policy.
- Why no material first-party path remains: The shipped examples return research results and launch configuration remains external to those results.

## S5 — Policy and identity

- State: —
- Function: Resolve identity or ultimate-policy questions and apply the ruling.
- Disturbance / variety regulated: A workflow purpose or execution authority may conflict with another governing commitment.
- Decisive decision or feedback right: No supplied adjudication of ultimate identity or policy is exposed.
- Decision owner: The author and operator provide workflow intent and execution parameters.
- Supporting / enforcement mechanisms: Metadata, provider/sandbox constraints, runtime budgets and configuration validation.
- Closure path: The runtime enforces the supplied run parameters and resume invariants. It does not return an adjudicated ultimate-policy decision.
- Why this is / is not agent-owned: The supplied enforcement and operator commands address execution choices rather than an identity-governance loop.
- Evidence: [Run and resume CLI](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/cli.ts#L399-L466) · [Journal and run setup](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/run.ts#L71-L109) · [Exact-resume guard](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/journal.ts#L153-L179)
- Basis: Bounded structural absence.
- Confidence: High.
- Caveats: Application embedding or custom scripts can supply their own higher authority boundary.

### Absence scope

- Surfaces inspected: Run launch, metadata, operator controls, workflow validation and resumption guards.
- Plausible first-party paths checked: Higher-level override of purpose or ultimate policy, trusted adjudication, and subsequent enforcement of a returned ruling.
- Why no material first-party path remains: The run instantiates an authored purpose and obeys its current settings. No identity-level escalation and return is supplied.

## Distributed OSS parent arrangement

The operator owns the selected local workflow. Repository development and release governance are outside the assessed run.

## Self-hosted and non-human modes

A worker run can execute from a preset budget without human interventions. The CLI operator can exercise the distinct parent-controlled pause-of-work and resume decision.

## Recursion

One authored run is the whole supported supervisory boundary. Workers inside it carry result and worktree commitments.

## Variety and escalation

Provider disagreement may trigger deeper second opinions. Branch isolation absorbs concurrent edit conflicts. Output-token limits and interruption bound current commitments. [Material-disagreement escalation](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/builtins/second-opinion.workflow.js#L91-L129) · [Worktree and fan-out return](https://github.com/SawyerHood/omegacode/blob/748d686a7950b3466e8d7fd014db32c4fb9fccf5/src/runtime/primitives.ts#L438-L514)

## Evidence gaps

Frozen source and built-in control paths were inspected. No local provider execution was performed. Resume is described from the runtime guards, including the requirement for the original file and arguments.
