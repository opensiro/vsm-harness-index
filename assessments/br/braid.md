---
harness_id: braid
project_name: Braid
repository: https://github.com/Epsirom/braid
review_ref: 993b3a61941401695698eff8ccc64d4da61c350a
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Braid

## Review boundary

- System in focus: Braid graph runtime, bundled OpenAI-compatible runner, and first-party Pi/DSH adapters and operator panels.
- Purpose and identity: execute isolated model work and reconcile selected code changes through explicit graph-controlled integration.
- Relevant environment: user checkout/dirty edits, model providers, concurrent node work, optional external host primary agent and human graph owner.
- Standard-distribution boundary: published core/adapters and first-party installed integrations; arbitrary user runners and the external host's general cognitive ownership are separated.
- Credited operating / distribution surfaces: src/runtime.ts, workspaces.ts, merge-tools.ts, replan-tools.ts, adapters/openai.ts and first-party Pi/DSH runner/jobs/panel/tool code.
- Adjacent first-party surfaces excluded from ownership: benchmarks, fake runner demonstrations, tests, release/dependency-security workflows and contributor governance. General Pi/DSH host intelligence is not silently treated as Braid's own autonomous supervisor.
- First-party operating / deployment modes considered: core with bundled OpenAI runner, installed Pi/DSH worker adapters, graph control API and human live panels, optional bounded review command.
- Recursion level: one Braid job with operational node instances and its graph owner.
- Reviewed revision: 993b3a61941401695698eff8ccc64d4da61c350a.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The runtime admits isolated executions from a mutable dependency/cycle graph and records immutable execution identities/checkpoints. Workers use isolated predecessor snapshots; merge nodes combine them in another worktree, while integrate explicitly changes the invoking checkout. The bundled OpenAI runner supplies decision tools and a genuine local Git/finish_merge loop for merges; ordinary OpenAI execute nodes are text-only, not a general shell agent. Pi/DSH runners implement richer tool loops with read/write/shell capabilities according to workspace mode. Replan requests hold descendants and notify the external graph owner; whole-job snapshots and revision-checked update/resume/limit APIs return control changes into scheduling. Human panels can pause/hold/resume/cancel work. The optional Pi review command is a bounded review/fix production graph, not independent runtime audit by name alone.

## Operational model

Merge/integrate and installed worker loops establish autonomous S1 and agent-owned reconciliation of sibling edits (S2). Graph-wide current-control primitives are specific and substantial, but the autonomous graph-owner actor is supplied by an embedding application or external host; core is therefore credited C for that base mode. Human panels separately close a parent current-control mode, giving S3=C(P). No external host authority is borrowed as A, and per-task graph ownership is not S5.

## S1 — Operations

- State: A
- Function: produce task results and effect selected code integration through isolated model invocations.
- Disturbance / variety regulated: changing code inputs, Git errors, tool failures and contradictory source results.
- Decisive decision or feedback right: select task actions/decision choices and merge Git operations/source dispositions after observations.
- Decision owner: model-backed node agents; specifically the bundled merge/integrate agent and first-party installed worker loops.
- Supporting / enforcement mechanisms: graph admission, workspace capabilities, local Git command allowlist, checkpoints, schemas, time/token limits and finish validation.
- Closure path: merge runner executes model-selected Git calls, returns their output and errors into subsequent model turns, then records source dispositions and final output.
- Boundary reachability: createOpenAICompatibleRunner is a shipped adapter with its own merge tool loop; first-party Pi/DSH runners additionally wire richer node tools. No custom runner is needed to demonstrate this narrow S1.
- Why this is / is not agent-owned: core does not choose a merge strategy or source acceptance; the model does. Text-only OpenAI worker replies alone are not used as proof of a general action loop.
- Evidence: [bundled actor/tool setup](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/adapters/openai.ts#L109-L171); [call/tool/observation loop](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/adapters/openai.ts#L214-L252); [explicit source decisions](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/merge-tools.ts#L34-L56); [first-party worker factory](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/integrations/pi/runner.ts#L110-L170).
- Basis: structural.
- Confidence: high.
- Caveats: OpenAI execute nodes have no general filesystem/shell tools. Platform adapters differ in capabilities; no empirical task-quality claim is made.

## S2 — Coordination

- State: A
- Function: reconcile conflicting concurrent code contributions without overwriting sibling/caller state.
- Disturbance / variety regulated: parallel agents produce diverging edits and integration can collide with pre-existing or concurrent caller changes.
- Decisive decision or feedback right: inspect source checkpoints/dirty status, choose which changes to integrate/discard/archive and choose/repair the Git integration method.
- Decision owner: merge/integrate model agent.
- Supporting / enforcement mechanisms: fresh worktrees, immutable predecessor checkpoints, invocation-specific Git operations, source dirty preview, integration serialization and finish_merge conflict checks.
- Closure path: Git conflicts/errors return to the model; selected source dispositions and reconciled checkpoint become the inputs for subsequent workers or the user's source checkout.
- Boundary reachability: explicit merge/integrate node types invoke the bundled agent loop and core beginMerge/finish path. The path handles actual conflicting code states, not generic graph routing.
- Distinct S1 units: independent worker node agents and the model-backed reconciliation unit consuming their outputs.
- Inter-S1 disturbance: incompatible sibling edits or accidental replay/overwrite of the invoking user's existing edits.
- Attenuating coordination relation: isolate contributions, then perform agent-selected explicit reconciliation with one accounted disposition per source.
- Feedback into subsequent S1 behaviour: downstream work uses the reconciled checkpoint; failed/unresolved integration blocks a successful finish and preserves recovery evidence.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the agent explicitly handles code collision and source-selection variety across independently produced artifacts, beyond waiting for graph edges.
- Why this is / is not agent-owned: core validates/enforces boundaries; it explicitly does not apply or select changes on behalf of the model.
- Evidence: [coordination contract](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/README.md#L481-L533); [collision/source decision tools](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/merge-tools.ts#L34-L56); [feedback loop](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/adapters/openai.ts#L214-L252); [merge completion guards](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/workspaces.ts#L466-L529).
- Basis: structural.
- Confidence: high.
- Caveats: In-process integration serialization does not coordinate arbitrary external processes; source changes can leave partial edits/conflicts and a backup.

## S3 — Inside-and-now control

- State: C(P)
- Function: hold, revise and resume whole-job commitments in response to current work findings and constrained execution resources.
- Disturbance / variety regulated: a worker discovers redundant/incorrect planned work, live work must be stopped or redirected, or graph/time/token limits are reached.
- Decisive decision or feedback right: graph owner decides whether to alter nodes/edges/limits or continue/cancel affected executions.
- Decision owner: base mode exposes this right to a consumer-composed autonomous graph owner; parent mode supplies a human operator through the first-party panels.
- Supporting / enforcement mechanisms: whole-job snapshots, execution/revision identities, replan holding and reminders, update/resume/limit API, suspension checkpoints and panel controls.
- Closure path: a worker's replan request holds successors; owner inspection and revision-checked update/resume changes subsequent scheduling. Human pause/hold/resume/cancel similarly returns directly into the live job.
- Boundary reachability: specific requestReplan and control methods are intentionally exposed by core; installed adapters notify a host primary agent. The human live panels are first-party operational surfaces. The external primary agent's own autonomy is not credited as Braid-owned A.
- Whole-system current view: job snapshot includes all node/execution states, paused IDs, current graph revision, results and finite limits.
- Current-control decision scope: job-wide current commitments, redundant work, execution admission and resource/time allowance.
- Why this is / is not agent-owned: workers cannot rewrite the graph themselves. Braid provides the control-specific feedback/right but no autonomous whole-graph owner in its standalone bundled runner; the external application/host must compose that actor. Human panel intervention has its own complete parent return.
- Evidence: [finding-specific control primitive](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/replan-tools.ts#L31-L63); [hold/notification wiring](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/runtime.ts#L930-L952); [whole-job control contract](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/types.ts#L649-L697); [parent notification](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/integrations/pi/jobs.ts#L403-L424); [human current intervention](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/integrations/pi/command.ts#L488-L524); [human return](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/integrations/dsh/panel.ts#L99-L115).
- Basis: structural.
- Confidence: high.
- Caveats: C is for a function-specific control path, not arbitrary framework expressiveness. The P mode is local graph supervision, not ultimate policy or simultaneous agent/human ownership.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Consumer-composed autonomous graph owner | Worker replan or resource/commitment exception | Snapshot → owner update/resume/limit decision → changed scheduling | request_replan, runtime control and adapter notifications cited above |
| Parent (`P`) | Human graph operator | Live work/status requiring intervention | First-party panel pause/hold/resume/cancel → direct live runtime change | Pi command and DSH panel code above |

## S3* — Complementary audit

- State: —
- Function: no separate complementary audit of Braid operational reporting beyond its ordinary work/review paths established.
- Disturbance / variety regulated: false implementation or validation claims are relevant, but available review is task production/QA.
- Decisive decision or feedback right: no independently controlled complementary audit of the runtime's ordinary reports supplied.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: read-only reviewers with raw files/diffs, check decision node, checkpoints/activity logs and fake-provider/native tests.
- Closure path: the review command sends findings through its prescribed check→fix→re-review→apply production cycle.
- Why this is / is not agent-owned: distinct fresh reviewer contexts and raw evidence are useful, but mandatory QA in that production graph is not automatically S3*.
- Evidence: [reviewer purpose and evidence boundary](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/integrations/pi/review.ts#L7-L28); [ordinary review/fix decision cycle](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/integrations/pi/review.ts#L29-L91); [graph integration checks](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/workspaces.ts#L512-L529).
- Basis: structural.
- Confidence: medium.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: Pi bounded review graph, node runner contexts, execution logs/status, workspace/finish checks and development test/audit workflows.
- Plausible first-party paths checked: parallel independent-angle review, raw diff/checkpoint inspection, check synthesis and dependency audits.
- Why no material first-party path remains: the first-party reviewers are assigned production review/QA stages; core checks enforce integration invariants, and development security/benchmark audits are adjacent. No separate complementary control-audit channel is wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective capability-adaptation loop established.
- Disturbance / variety regulated: future provider/tool/environment changes would require adaptation outside the current job.
- Decisive decision or feedback right: no future-option/adoption process with a return to present capability supplied.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: live graph edits, request_replan, cyclic refinement, model overrides and prompt templates.
- Closure path: findings alter the present job's plan or rerun current work, rather than develop external/future adaptation options for the harness.
- Why this is / is not agent-owned: replanning the current task and model selection are not S4 by themselves.
- Evidence: [present-work replan semantics](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/replan-tools.ts#L31-L63); [current graph scheduling/cycles](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/docs/execution-control.md#L49-L100); [task/model parameters](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/integrations/pi/index.ts#L64-L100).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: replan primitives and host notifications, live graph updates, cycle/retry/review loops, prompt/model options and compatibility/release boundary.
- Plausible first-party paths checked: worker contradiction reports, agent-suggested graph additions, model changes and repeated refinement.
- Why no material first-party path remains: all operate on current assigned work. No supplied external environment model/future distinctions → adaptation options → current supervisory capability loop is established.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy issue and legitimate authoritative-return loop established.
- Disturbance / variety regulated: ultimate purpose/delegation conflicts are not a supplied job workflow.
- Decisive decision or feedback right: graph goals, workspace capabilities and user pauses are task/control decisions, not ultimate-policy settlement.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: trusted adapter, graph schema, read/write capability flags, command allowlist and user-versus-agent control attribution.
- Closure path: settings and graph actions constrain task execution; no identity-level proposal reaching ultimate authority and returning as policy is supplied.
- Why this is / is not agent-owned: calling the task submitter an owner or allowing it to pause nodes does not establish S5.
- Evidence: [adapter trust boundary](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/SECURITY.md#L44-L70); [scoped merge capabilities](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/merge-tools.ts#L1-L31); [ordinary owner control](https://github.com/Epsirom/braid/blob/993b3a61941401695698eff8ccc64d4da61c350a/src/types.ts#L677-L697).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: graph goal/options/schema, adapter trust and tool permissions, human panels and host-control rules, security/contributor boundary.
- Plausible first-party paths checked: owner graph edits, human pause precedence, capability changes and trusted runner configuration.
- Why no material first-party path remains: the supplied authority is over current tasks and execution capabilities; no separate ultimate identity/policy escalation, adjudication and return process is packaged.

## Distributed OSS parent arrangement

The P mode is the human owner of one live Braid job, supported by first-party panels and runtime control methods. Project contributor/release governance is adjacent. External host general intelligence is treated as composition for the S3 base mode, not borrowed autonomous ownership.

## Self-hosted and non-human modes

Core runner, Pi and DSH differ materially: only merge/integrate get the bundled OpenAI Git loop; installed worker adapters add richer tools. API/host integration exposes graph supervision; human panels independently close the P mode. Worktrees and tool restrictions are not an OS sandbox.

## Recursion

Node contexts/lineages and graph cycles establish execution structure, not recursive viable organizations. Workers cannot recursively call Braid or directly replace the whole graph.

## Variety and escalation

Checkpoint identity, explicit dirty-state previews, source dispositions and conflict errors preserve integration distinctions. Replan requests retain local work while holding successors for whole-job decision. Limits/suspension enforce owner choices and do not inherit decision ownership.

## Evidence gaps

No live model/provider/host-agent tests were run. Node/npm are unavailable on the inspection host, so upstream TypeScript/native tests were not executed or reported PASS. Current documentation includes execution-only graph changes beyond the package's recorded 0.5.2 label; classification follows the exact pinned code rather than assuming a later release. Index-selected Profile 0.2.4 / Methodology 0.3.7 is preserved.
