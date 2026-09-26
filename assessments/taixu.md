---
harness_id: taixu
project_name: TaiXu
repository: https://github.com/wkbin/taixu
review_ref: 037880a898ad503128dee7b2991dd6d351ad8cb3
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# TaiXu

## Review boundary

- System in focus: one first-party TaiXu Android agent-runtime deployment at pinned revision `037880a898ad503128dee7b2991dd6d351ad8cb3`, including its main `HarnessLoop`, model/tool rounds, persistent session tree, first-party subagent lanes/orchestrator, checkpoint/rewind surfaces, skill-evolution advisor and standard Chat UI closure paths.
- Purpose and identity: a local Android-native agent harness that executes user work through a persistent model/tool loop, workspace/Linux/browser/MCP tools, bounded subagents, resumable sessions and optional persistent workflows.
- Relevant environment: user requests, the linked workspace/device/runtime, external model providers and MCP/web resources, tool outcomes, and the human operator who may approve ordinary actions and accept or reject capability-evolution suggestions.
- Standard-distribution boundary: packaged Android runtime and UI at the frozen ref. Repository CI/tests and maintainer development activity are adjacent; they may corroborate behavior but do not own credited decisions.
- Credited operating / distribution surfaces: `HarnessLoop`, `HarnessToolRoundRunner`, provider/tool protocol, `SubagentOrchestrator`, `SubagentLaneRunner`, subagent write-lease/claim contracts, system/subagent prompts, persisted session/lane state, `SkillEvolutionAdvisor`, `ChatViewModel` skill-suggestion apply path, and ordinary shipped UI/runtime wiring.
- Adjacent first-party surfaces excluded from ownership: repository tests, GitHub Actions, build/release tooling, developer-only fixtures, documentation examples, and any future/default-branch behavior after the frozen review ref.
- First-party operating / deployment modes considered: ordinary model→tool session loop; automatic main-agent subagent delegation; multi-subagent batches with read-only/scoped/whole-workspace write leases; subagent resume by `task_id`; operator approval/rewind; post-run skill-evolution suggestions with explicit user apply/dismiss.
- Recursion level: one TaiXu deployment/session organization. Main session and durable subagent lanes are distinct operational units for S2/S3 analysis, but child lanes are not promoted to fully recursive viable systems solely because they run their own bounded model/tool loops.
- Reviewed revision: `037880a898ad503128dee7b2991dd6d351ad8cb3`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

TaiXu has a persistent main agent loop and separate headless subagent lanes. A lane repeatedly calls the configured model, parses model tool calls, validates and executes them, records tool results, and feeds those observations into later model rounds. Subagent lanes share the parent session tree/workspace while keeping separate lane identities and operation histories.

The first-party subagent protocol exposes `writePaths` to the main agent. `subagent_guidance.md` instructs the main model to place independent work in one `invoke_subagent` batch and to declare each task as read-only, scoped-write, or whole-workspace-exclusive. `SubagentOrchestrator` turns those declared leases into write-clean waves: non-conflicting tasks may run concurrently, conflicting tasks move to later waves. `SubagentLaneRunner` enforces the lease at tool execution time and returns violations as failed tool results to the child lane. The completed batch is summarized back to the main agent with success, termination, approval and blocked-write information.

TaiXu also separates a subagent's completion claim from host-observed operational evidence. `SubagentClaim.kt` treats model status as a claim, extracts successful command/file-write receipts from the host-persisted lane transcript, independently adjudicates each criterion, and may downgrade an unsupported `complete` claim to `partial`. That adjudication is included in the parent-facing result.

After a sufficiently tool-heavy successful run, `SkillEvolutionAdvisor` can use a separate model call to decide whether the observed user workflow reveals a reusable future capability gap or a defect in an existing skill. It emits a create/update suggestion. The standard Chat UI lets the human accept it, and `ChatViewModel.applySkillSuggestion()` writes the resulting custom skill into the active skill repository for subsequent operation.

Primary evidence:

- [`harness/src/main/java/top/wkbin/taixu/harness/HarnessLoop.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/HarnessLoop.kt) — persistent multi-session agent runtime, current session state, approval/recovery and checkpoint/rewind surfaces.
- [`harness/src/main/java/top/wkbin/taixu/harness/HarnessToolRoundRunner.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/HarnessToolRoundRunner.kt) — model-selected tool calls, validation/execution and tool-result feedback.
- [`harness/src/main/java/top/wkbin/taixu/harness/subagent/SubagentLaneRunner.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/subagent/SubagentLaneRunner.kt) — bounded autonomous child model/tool loop, result feedback, write-scope enforcement and structured termination.
- [`harness/src/main/java/top/wkbin/taixu/harness/SubagentOrchestrator.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/SubagentOrchestrator.kt) — first-party subagent batch scheduling, write-clean waves, lane resume and parent-facing batch summary.
- [`harness/src/main/assets/prompts/subagent_guidance.md`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/assets/prompts/subagent_guidance.md) — main-agent responsibility for decomposition, `writePaths`, post-batch repair and conflict integration.
- [`harness/src/main/java/top/wkbin/taixu/harness/SubagentArgsParser.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/SubagentArgsParser.kt) — model-supplied subagent task and lease parsing.
- [`harness/src/main/java/top/wkbin/taixu/harness/subagent/SubagentLaneContracts.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/subagent/SubagentLaneContracts.kt) — execution-time write isolation, incomplete-result and blocked-write feedback.
- [`harness/src/main/java/top/wkbin/taixu/harness/subagent/SubagentClaim.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/subagent/SubagentClaim.kt) — host receipt extraction and independent downgrade-only claim adjudication.
- [`harness/src/main/java/top/wkbin/taixu/harness/skill/SkillEvolutionAdvisor.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/harness/src/main/java/top/wkbin/taixu/harness/skill/SkillEvolutionAdvisor.kt) — post-run prospective skill adaptation option generation.
- [`feature/chat/src/main/java/top/wkbin/taixu/ui/chat/SkillSuggestionActions.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/feature/chat/src/main/java/top/wkbin/taixu/ui/chat/SkillSuggestionActions.kt) and [`ChatViewModel.kt`](https://github.com/wkbin/taixu/blob/037880a898ad503128dee7b2991dd6d351ad8cb3/feature/chat/src/main/java/top/wkbin/taixu/ui/chat/ChatViewModel.kt) — first-party human apply path that creates/updates a custom skill.

## S1 — Operations

- State: A
- Function: perform user-directed work through persistent model/tool execution, including workspace, shell, browser/MCP and other first-party tools, and return tool observations to the model until the work concludes.
- Disturbance / variety regulated: heterogeneous user requests, changing workspace state, tool outputs/failures, schema errors, loop conditions, external resources and task-specific follow-up needs.
- Decisive decision or feedback right: choose which available tool to call, with which task-specific arguments, and whether to continue using tools or conclude.
- Decision owner: the configured main-session model actor; bounded child lanes independently own the same kind of local operational discretion for their assigned task.
- Supporting / enforcement mechanisms: `HarnessLoop`, provider protocol, `HarnessToolRoundRunner`, `ToolExecutor`, schema/loop checks, persisted session/lane transcript, tool budgets and approval gates.
- Closure path: user request/history → model chooses tool call → host validates/executes → `ToolResult` is persisted into the conversation → later model round observes the result and chooses the next operational action or final answer.
- Boundary reachability: this is TaiXu's standard shipped chat/agent runtime; subagent lanes use the same first-party provider/tool protocol inside the packaged distribution.
- Why this is / is not agent-owned: removing the model removes the task-specific choice of tools, arguments and stopping point; deterministic machinery constrains and executes those choices but does not replace their ordinary operational discretion.
- Evidence: `HarnessToolRoundRunner.kt`, `SubagentLaneRunner.kt`, `HarnessLoop.kt`.
- Basis: explicit + structural
- Confidence: high
- Caveats: deterministic schema, safety, approval and loop guards are enforcement, not the S1 owner.

## S2 — Coordination

- State: A
- Function: prevent destructive interference among concurrently executing subagent S1 units that share a workspace, especially overlapping writes.
- Disturbance / variety regulated: two or more child lanes can otherwise concurrently modify the same file/directory or whole workspace, causing write collisions and invalidating each other's operational results.
- Decisive decision or feedback right: choose the task-specific write lease for each delegated S1 (`[]`, exact paths/directories, or `[*]`) and thereby determine which child operations may safely coexist.
- Decision owner: the main-session model actor issuing `invoke_subagent`; first-party prompt/schema makes `writePaths` part of the model's required task decomposition/coordination decision.
- Supporting / enforcement mechanisms: `buildWriteCleanWaves`, global parallelism gate, per-lane execution-time write-scope rejection, normalized path checks, blocked-write accounting and structured batch summaries.
- Closure path: main model defines multiple child tasks and write leases → orchestrator detects lease overlap and partitions work into non-conflicting waves → lane gate blocks any structured write outside the selected lease and returns the failure as a tool result → the child changes later behavior, while later conflicting waves wait → parent receives combined outcomes for further coordination.
- Boundary reachability: `invoke_subagent` is a first-party model-facing tool in the ordinary system prompt/runtime; the shipped guidance explicitly requires `writePaths`, and `SubagentOrchestrator`/`SubagentLaneRunner` enforce the same fields without downstream code.
- Why this is / is not agent-owned: the host decides deterministic overlap/scheduling from the chosen leases, but the task-specific coordination right — what each child may write and whether it is read-only/scoped/exclusive — belongs to the main agent. Without that model decision the host does not infer materially equivalent task-specific leases.
- Evidence: `subagent_guidance.md`, `SubagentArgsParser.kt`, `SubagentOrchestrator.kt`, `SubagentLaneContracts.kt`, `SubagentLaneRunner.kt`.
- Basis: explicit + structural
- Confidence: high
- Caveats: the lease gate does not cover arbitrary shell writes through `base`; the shipped prompt states this boundary and directs strict-isolation writes through structured write/edit tools.
- Distinct S1 units: separately named/resumable subagent lanes, each running its own bounded model/tool loop with its own operation/transcript while contributing to the parent job.
- Inter-S1 disturbance: concurrent lane writes to overlapping workspace paths can collide or invalidate peer work.
- Attenuating coordination relation: model-declared write leases plus deterministic conflict partitioning into write-clean waves and execution-time path enforcement.
- Feedback into subsequent S1 behaviour: out-of-lease writes are returned to the offending child as failed tool results; conflicting tasks are delayed to later waves; blocked/incomplete outcomes are returned to the parent for repair rather than silently treated as complete.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is explicitly designed around the concrete shared-workspace write-interference mode and changes when/how affected child operations may write.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current set of child operations as a whole, allocate their task/model/write commitments, and intervene when a child is incomplete, blocked, awaiting approval, timed out or in conflict with the larger delivery.
- Disturbance / variety regulated: partial/failed child work, blocked writes, pending approvals, timeout, model/role mismatch, conflicting returned conclusions, and changing current commitments across a multi-child batch.
- Decisive decision or feedback right: choose the child portfolio and per-child task/role/model/write commitments, then use the returned whole-batch outcome to resume a lane by `task_id`, re-dispatch with changed leases, perform an approval/write itself, resolve conflicts or proceed to final delivery.
- Decision owner: the main-session model actor.
- Supporting / enforcement mechanisms: batch outcome aggregation, structured termination/approval/blocked-write status, persisted lane transcripts and resumable lane ids, concurrency gate, timeout/recovery machinery, parent system prompt and main-session tool loop.
- Closure path: main model creates current child commitments → child lanes execute under S2 leases → orchestrator returns one ordered batch summary covering every child's result/status → the main model is explicitly instructed not to treat blocked/incomplete outcomes as complete and can revise current commitments through another tool round → subsequent child/main operation follows the revised decision.
- Boundary reachability: all elements are wired into the ordinary first-party `invoke_subagent` path and main chat loop; no development-only supervisor is borrowed.
- Why this is / is not agent-owned: deterministic concurrency/timeout machinery enforces limits, but the main model chooses the actual task portfolio, roles/models/write scopes and exception response. Removing it leaves no actor making the same task-specific whole-job interventions.
- Evidence: `subagent_guidance.md`, `SubagentOrchestrator.kt`, `SubagentLaneRunner.kt`, `HarnessLoop.kt`.
- Basis: explicit + structural
- Confidence: high
- Caveats: simple single-agent runs need not exercise S3; the state is established by the standard multi-subagent mode.
- Whole-system current view: the parent receives the ordered outcome set for the entire dispatched batch, including each task's success, termination, tool-call count, pending approvals, blocked writes, read-only/write-intent condition and resumable lane identity, alongside its own current session context.
- Current-control decision scope: create/withhold child commitments, choose role/model and write authority, resume a specific lane, redispatch failed/blocked work, personally complete approval/write obligations, reconcile returned conflicts and decide whether the current job is ready to close.

## S3* — Complementary audit

- State: C
- Function: challenge a child S1's self-reported completion using a host-side evidence path that sees independently persisted operational receipts rather than trusting the child summary alone.
- Disturbance / variety regulated: a child model can claim completion even though required verification commands never succeeded, claimed files were not actually written, or a criterion is manually unverifiable.
- Decisive decision or feedback right: determine whether each declared acceptance criterion is backed by host-observed successful command/file-write receipts and downgrade unsupported `complete` to `partial` before the claim reaches parent control.
- Decision owner: deterministic first-party host adjudication; no autonomous independent auditor owns the verdict at this ref, so the audit path is classified `C` rather than `A`.
- Supporting / enforcement mechanisms: persisted lane transcript, extraction of successful `ToolCall`/`ToolResult` command and write receipts, criterion parser, downgrade-only adjudicator and parent-facing adjudication rendering.
- Closure path: child emits optional completion claim → host independently reads persisted execution receipts → criteria are reconciled against those receipts → unsupported completion is downgraded → adjudicated result is included in the parent-facing subagent outcome → main S3 sees the corrected operational claim rather than the child's unsupported status.
- Boundary reachability: claim parsing/adjudication is first-party runtime code used by `SubagentOrchestrator` on ordinary child results; it does not depend on tests or an external evaluator.
- Why this is / is not agent-owned: the complementary evidence channel and corrective return are operationally present, but the decisive audit verdict is fixed host logic rather than an autonomous audit actor. The implementation therefore provides a function-specific constructor/audit path without autonomous S3* ownership.
- Evidence: `SubagentClaim.kt`, `SubagentOrchestrator.kt`, persisted lane transcript in `SubagentLaneRunner.kt`/session storage.
- Basis: explicit + structural
- Confidence: high
- Caveats: claims without a valid claim block fail open to legacy behavior; `C` reflects the available first-party audit path, not universal auditing of every child response.
- Claim being audited: the child model's assertion that a delegated subtask is complete and its acceptance criteria have actually been satisfied.
- Ordinary reporting path: the child lane's own textual conclusion/status returned through normal subagent summary.
- Complementary access path: host-persisted successful tool execution receipts for commands and structured file writes, which are not controlled by the child claim text.
- Independence boundary: the child produces the claim, while host runtime derives receipts from persisted execution events and applies downgrade-only rules; the host never upgrades an unsupported child claim.
- Who acts on findings: the host modifies the status before returning it, and the main S3 receives the adjudicated result for follow-up/re-dispatch or final-delivery control.

## S4 — Outside-and-then intelligence

- State: P
- Function: turn evidence from completed user-facing work into a prospective option to evolve TaiXu's reusable skill capability for future tasks.
- Disturbance / variety regulated: repeated/reusable user workflows not covered by current skills, or operational experience revealing defects in an existing reusable skill's instructions.
- Decisive decision or feedback right: accept or reject the proposed capability adaptation and, when accepted, create/update the persistent custom skill used by future operation.
- Decision owner: the human operator through the first-party skill-suggestion card/apply action; the model-backed advisor develops the adaptation option but does not autonomously install it.
- Supporting / enforcement mechanisms: post-run gating after successful tool-heavy work, conversation digest, current skill inventory, separate advisor model call, normalized create/update proposal, `SkillSuggestion` message/card, `SkillSuggestionActions`, and `AgentSkillRepository.addCustom`.
- Closure path: external user work exposes a reusable workflow or skill defect → after the successful run the advisor explicitly reasons about future reuse/current skill coverage → it emits a create/update adaptation option → human accepts through the standard Chat UI → the first-party repository persists the new/updated enabled custom skill → future agent operation can use the changed capability.
- Boundary reachability: `HarnessLoop` is wired with `SkillEvolutionAdvisor` in the packaged runtime and the standard Chat UI exposes apply/dismiss actions whose apply path persists the resulting skill; no repository-development workflow is required.
- Why this is / is not agent-owned: the advisor autonomously formulates an adaptation proposal, but the decisive right to alter persistent capability belongs to the human. Because that parent decision is first-party and returns into active skill capability, the published state is `P`, not `A`.
- Evidence: `SkillEvolutionAdvisor.kt`, `SkillSuggestionActions.kt`, `ChatViewModel.kt`, current skill repository wiring.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: generic memory/learning and current-task web research are not the S4 witness. The credited witness is specifically the post-run future-reuse/skill-gap analysis plus human-governed persistent capability update.
- External distinction: completed user-facing work reveals an externally sourced workflow demand or skill defect that the current reusable skill inventory does not adequately cover.
- Future / prospective distinction: the advisor explicitly asks whether the just-observed workflow should be reusable in future tasks or whether an existing skill should be evolved for future operation.
- Adaptation option generated: a normalized `create` or `update` skill proposal containing persistent future instructions, description and optional trigger.
- Path back into current capability / S3: the human applies the proposal through the standard Chat UI; `AgentSkillRepository.addCustom` persists the new/updated enabled skill so subsequent agent operation can select/use the changed capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established at the assessed deployment recursion.
- Disturbance / variety regulated: candidate surfaces inspected included tool approvals, safety/permission modes, system prompts, model/provider settings, workflow approvals and human UI controls.
- Decisive decision or feedback right: no path was found for an identity- or ultimate-policy-level issue to reach a legitimate authority and return as a durable highest-level policy/identity decision governing later S1–S4 operation.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: ordinary human approvals, permission modes, static system prompts/configuration, session/model settings and workflow gates.
- Closure path: not established.
- Why this is / is not agent-owned: ordinary approval of tools, rewinds, skill adaptation or workflows regulates action/capability but does not establish ultimate identity/policy closure.
- Evidence: `HarnessLoop.kt`, approval/runtime policy surfaces, standard prompt/settings paths.
- Basis: scoped absence
- Confidence: high
- Caveats: the positive human-governed S4 adaptation path does not imply S5.

### Absence scope

- Surfaces inspected: main harness/session runtime, approval and permission flow, system/subagent prompts, persistent workflows, checkpoint/rewind, skill evolution, Chat UI actions, model/provider/runtime settings and repository governance boundary.
- Plausible first-party paths checked: human tool approval as parent governance; system prompt/settings as constitution; persistent workflow approval; skill-evolution acceptance; model/provider selection; rewind/checkpoint authority.
- Why no material first-party path remains: these paths govern ordinary actions, current control, adaptation or configuration. None carries an identity/ultimate-policy issue to an ultimate authority and returns a durable identity/policy decision into operation.

## Recursion

Subagent lanes have separate identities, transcripts and bounded model/tool loops, so they are distinct operational S1 units for the parent session. They are intentionally prohibited from recursively spawning subagents and are bounded by parent-selected tasks, leases and budgets. The frozen evidence therefore does not establish each child as a fully viable recursive VSM system with its own complete metasystem.

## Variety and escalation

TaiXu attenuates operational variety through tool schemas, budgets, loop detection, approval gates and write leases while preserving feedback to the deciding model. S2 write-clean waves reduce destructive shared-workspace variety without requiring all child work to become serial. S3 receives structured child exceptions such as blocked writes, pending approval, timeout and downgraded claims. Checkpoint/rewind and recovery preserve operational reversibility but are not independently credited as S3/S5. The post-run S4 path moves a future capability proposal to a human authority rather than silently changing the harness.

## Evidence gaps

- The `base` shell tool can write outside the structured write-lease gate; the first-party prompt documents this limitation. S2 therefore has a real but not universal interference-control channel.
- S3* claim adjudication is optional/fail-open when a child does not emit a valid claim block; it is a material first-party complementary audit path, not universal mandatory audit coverage.
- S4 is credited only to the explicit skill-evolution suggestion/apply loop. Other learning, memory, MCP discovery and current-task research surfaces were not promoted to S4.
- External model providers supply inference only; they do not donate organizational ownership beyond the first-party protocols that assign decision rights at the assessed boundary.
