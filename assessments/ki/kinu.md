---
harness_id: kinu
project_name: Kinu
repository: https://github.com/AshishKumar4/kinu
review_ref: 64e48f2bcb08d8a9a7a26b27552f79dcd361d16b
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Kinu

## Review boundary

- System in focus: One installed Kinu workspace agent application, including supported durable hires, swarm fan-in and session-advisor operation.
- Purpose and identity: Carry out owner work through model-directed tools, maintain workspace state and integrate delegated work.
- Relevant environment: Owner requests, workspace files/processes, connected tools/devices, model providers and sibling workspaces.
- Standard-distribution boundary: Public repository at the frozen ref, especially packages/core and its local/Cloudflare backend wiring.
- Credited operating / distribution surfaces: Core actor/session execution, native delegation tools, reported-artifact swarm merge-back, dynamic state, and separately instantiated advisor with read-only evidence access.
- Adjacent first-party surfaces excluded from ownership: Development/benchmark organization, sealed experimental verifiers, marketing claims and slate-building packages/agent-core vendored runtime. No metasystem is inherited from that runtime or from third-party agents/providers.
- First-party operating / deployment modes considered: Local CLI and hosted workspace, durable subagents and optional beta-enabled swarm. Backend capability wiring and account settings determine which native operations are actually offered.
- Recursion level: One workspace application containing separate task actors; a swarm node or hire is not thereby a complete viable organization.
- Reviewed revision: `64e48f2bcb08d8a9a7a26b27552f79dcd361d16b`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[docs/ARCHITECTURE.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/ARCHITECTURE.md); [docs/WORKSPACES.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/WORKSPACES.md) describe a platform-neutral core with separate local and hosted adapters. ChatSession owns durable admission, queues and settlement; ActorSession owns mutable per-actor execution, context, orchestration and cancellation. Its model/tool program closes the task loop. Hosted hires have distinct actor state while sharing workspace files; local shared directories are not isolated private branches.

Native agents operations support durable hires, assignments, reports, inspection and dismissal. Live dynamic context carries tasks, jobs and delegates. A separate swarm mode creates work candidates, measures/judges them and performs fan-in. In the reported-artifact fan-in path, incompatible edits to the same path cause a new model-driven merge node rather than an unconditional last writer overwrite.

SessionAdvisor is constructed in ActorSession and observes model steps through a separate conversation. It can read file/memory evidence through its own read-only tool instances and send a grounded concern to the actor or a blocker to its hirer. This differs from the producer's completion gate and from routine dream-edit QA. Evolution learns from tool struggles, rated turns and proposed text/scaffold changes; its real capability edits are not by themselves evidence of outside-and-then intelligence.

## Operational model

Model actors choose work actions and integration responses. Deterministic queues, admission, budgets, measurements, trust rows and artifact gates support/enforce those choices. The supervising workspace actor reads its current collective commitments and can change the composition or ongoing assignments of its hires. Human owner attention handles unresolved questions; generic ownership, approval and editable SOUL.md are not automatically S5.

## S1 — Operations

- State: A
- Function: Perform owner work through model-directed tools and persistent workspace effects.
- Disturbance / variety regulated: Changing task evidence, tool failure, asynchronous results and interruptions.
- Decisive decision or feedback right: Select the next substantive action, revise an approach or answer using observed results.
- Decision owner: The configured workspace/task actor.
- Supporting / enforcement mechanisms: ChatSession, ActorSession, native tools, background work, durable history, context preparation and model-provider adapters.
- Closure path: Actor execution runs model/tool rounds; tool results and admitted signals become subsequent context before further action or settlement.
- Boundary reachability: Both supported backends assemble the first-party core actor turn; model APIs supply inference rather than an imported agent loop.
- Why this is / is not agent-owned: Queuing/storage can run without a model actor, but do not choose an equivalent task-specific transformation.
- Evidence: [packages/core/src/orchestrator/actor-session.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/orchestrator/actor-session.ts); [packages/core/src/orchestrator/chat-session.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/orchestrator/chat-session.ts); [packages/core/src/orchestrator/main-turn-surface.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/orchestrator/main-turn-surface.ts); [docs/ARCHITECTURE.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/ARCHITECTURE.md).
- Basis: structural
- Confidence: high for shipped ownership.
- Caveats: No provider-backed task execution or empirical quality/security claim.

## S2 — Coordination

- State: A
- Function: Reconcile interfering outputs from distinct swarm work actors before integration.
- Disturbance / variety regulated: Two settled members change the same artifact path to different bytes from a common base.
- Decisive decision or feedback right: Choose a combined version retaining the independently earned contributions, then submit it as another candidate.
- Decision owner: A first-party model-driven merge node.
- Supporting / enforcement mechanisms: mergeBack conflict detector, provenance/base checks, dependency ordering, fan-in expansion, measurement and bounded node budget.
- Closure path: conflictWith detects incompatible writes; spawnMerge creates a brief naming both members and affected paths; fan-in expands that brief into a new actor candidate with the consumed results; its output re-enters ordinary candidate grading/integration.
- Boundary reachability: Native agents.swarm reaches the search engine; createLevelFanIn supplies the real spawnMergeNode callback to mergeBack. This is the supported reported-artifact aggregate mode, not merely an unbound callback.
- Why this is / is not agent-owned: Deterministic detection and grading cannot choose the substantive merged content. The spawned model actor supplies that resolution.
- Distinct S1 units: Separately executing swarm-node actors producing candidate work/artifacts.
- Inter-S1 disturbance: Conflicting changed bytes at the same target path, beyond generic concurrent execution.
- Attenuating coordination relation: Pause conflicting application and create an explicitly tasked reconciliation actor using both outputs.
- Feedback into subsequent S1 behaviour: The new candidate carries the reconciliation and is graded like other work; no conflict-resolution label grants automatic acceptance.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The path is triggered by concrete incompatible outputs and requests a corrective combined artifact. Ordinary hire/report plurality and lock ordering alone are not credited.
- Evidence: [packages/core/src/strategy/merge-back.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/strategy/merge-back.ts); [packages/core/src/strategy/fanin.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/strategy/fanin.ts); [packages/core/src/delegation/agents-tool.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/delegation/agents-tool.ts).
- Basis: structural
- Confidence: medium-high for the bounded fan-in mode.
- Caveats: Exhausted budget or missing parent can prevent creation, producing no credited resolution. Shared-plane writes are refused as unattributable/already landed; this is not a claim that all local/shared filesystem races are resolved. Scoring and judge-only synthesis alone are not S2.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the workspace's current collective commitments and continuing delegated work.
- Disturbance / variety regulated: Several ongoing workstreams become blocked, obsolete or misaligned while durable workers remain available.
- Decisive decision or feedback right: Inspect current work/status/reports, change an existing agent's workstream, hire a needed role or retire a worker.
- Decision owner: The supervising workspace/hirer model actor.
- Supporting / enforcement mechanisms: Native agents.list/assign/hire/message/dismiss, current delegate/task/job context, report-triggered wakes, roster store and backend lifecycle ports.
- Closure path: Current roster and child reports enter the supervisor's view; it chooses a changed commitment/composition; assignment messages reach the existing actor and later reports wake the supervisor with the resulting state.
- Boundary reachability: serveAgents exposes the wired native operations with their real handlers. DynamicContextLedger refreshes the live task/job/delegate view across steps; supported backend team wiring supplies the durable roster.
- Why this is / is not agent-owned: Lifecycle code applies the decision and bounds admission, but the supervising model chooses the workstream/composition response. This is more than initial task decomposition.
- Whole-system current view: The assessed workspace's live tasks, jobs and delegates, plus agents.list tree with current work/status and unread reports; detailed inspection provides additional evidence beyond capped context rows.
- Current-control decision scope: Current hires' work commitments, creation/retirement and integration at this workspace recursion. It does not claim account-wide authority over every sibling workspace.
- Evidence: [packages/core/src/delegation/agents-operations.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/delegation/agents-operations.ts); [packages/core/src/delegation/agents-tool.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/delegation/agents-tool.ts); [packages/core/src/subagents/inspection.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/subagents/inspection.ts); [packages/core/src/subagents/team-wiring.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/subagents/team-wiring.ts); [packages/core/src/prompting/volatile-context.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/prompting/volatile-context.ts); [docs/ARCHITECTURE.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/ARCHITECTURE.md).
- Basis: structural
- Confidence: medium-high, limited to the instantiated multi-actor workspace mode.
- Caveats: Mission budget ceilings are enforcement rather than the S3 owner. Reports are ordinary reporting, not independent audit. No parent modifier is inferred from generic owner approvals.

## S3* — Complementary audit

- State: A
- Function: Challenge operational work/claims through a distinct evidence-reading advisor.
- Disturbance / variety regulated: The producer skips a check, treats failure as success, acts on a wrong assumption or misses a reachable capability without recognizing it.
- Decisive decision or feedback right: Decide whether evidence supports a concrete problem and choose an actionable advisory finding.
- Decision owner: SessionAdvisor's separate model conversation.
- Supporting / enforcement mechanisms: Per-step observation, routed advisor model, independent read-only file/memory tool instances and ledgers, grounded review rules, note deduplication/severity floor, signal delivery and parent blocker forwarding.
- Closure path: ActorSession begins/updates advisor review; advisor reads actual evidence as needed and calls advise; accepted notes are recorded/delivered into the actor's subsequent signal stream, and blockers can reach the hirer.
- Boundary reachability: ActorSession constructs SessionAdvisor and wires beginTurn/step; turn-assembly binds advisorReadTools or hosted remote reads. Review applies to eligible input-taking actors when its model lane/settings are available.
- Why this is / is not agent-owned: Deterministic guards filter delivery, while a distinct model conversation chooses evidence and judges the discrepancy. Ordinary producer completion checks are separate.
- Claim being audited: That the actor's apparent progress/actions satisfy the requested work and that its assumptions/checks support the claimed result.
- Ordinary reporting path: Producer model messages and tool call/result transcript.
- Complementary access path: Advisor's own read-only file and memory operations; rules require checking windowed-out evidence or remaining silent, rather than treating an incomplete transcript as proof.
- Independence boundary: Separate conversation, review mandate and read-tool instances/ledgers; it may share model family, workspace guidance and actor observations. No security isolation or independently collected external truth is claimed.
- Who acts on findings: Reviewed actor via delivered signals; hirer for forwarded blockers. The actor is told the advisor may be wrong and must weigh the finding.
- Evidence: [packages/core/src/advisor/session-advisor.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/advisor/session-advisor.ts); [packages/core/src/advisor/advisor-ports.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/advisor/advisor-ports.ts); [packages/core/src/advisor/review.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/advisor/review.ts); [packages/core/src/orchestrator/actor-session.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/orchestrator/actor-session.ts); [packages/core/src/orchestrator/turn-assembly.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/orchestrator/turn-assembly.ts).
- Basis: structural
- Confidence: medium-high for enabled session-advisor operation.
- Caveats: Advisory rather than an unconditional publication veto. Floor, gate-open suppression and deduplication can withhold a note. Swarm/evolution actors without input are not automatically reviewed; routine failing tests or dream-edit grading are not separately counted as audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: Outside-and-then intelligence at the declared installed-agent recursion.
- Disturbance / variety regulated: Plausible shipped regulatory paths were checked below.
- Decisive decision or feedback right: No material function-specific closure established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Mutable definitions, configuration and operator controls support operation without establishing this function.
- Closure path: No qualifying shipped closure for this function.
- Why this is / is not agent-owned: Mutable skills/scaffolds and learning cadence do not by themselves establish outside-and-then intelligence.
- Evidence: [docs/EVOLUTION.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/EVOLUTION.md); [packages/core/src/evolution/refinement-lane.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/evolution/refinement-lane.ts); [packages/core/src/orchestrator/agent-orchestrator.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/orchestrator/agent-orchestrator.ts)
- Basis: structural
- Confidence: medium-high, bounded to the inspected distribution.
- Caveats: Downstream deployments can add organizational behavior.

### Absence scope

- Surfaces inspected: [docs/EVOLUTION.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/EVOLUTION.md); [packages/core/src/evolution/refinement-lane.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/evolution/refinement-lane.ts); [packages/core/src/orchestrator/agent-orchestrator.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/orchestrator/agent-orchestrator.ts)
- Plausible first-party paths checked: Execution-recovery lessons, rated-turn learning, dreams/refinement, scaffold/prompt/skill edits, retirement and operator-requested refinement; external-tool/research workloads.
- Why no material first-party path remains: These paths adapt from internal task outcomes and user corrections. They supply real learning and capability edits but no demonstrated prospective external environment model generating organizational adaptation options and returning them into current capability regulation. External research can be a user task without owning this workspace's S4.

## S5 — Policy and identity

- State: —
- Function: Policy and identity at the declared installed-agent recursion.
- Disturbance / variety regulated: Plausible shipped regulatory paths were checked below.
- Decisive decision or feedback right: No material function-specific closure established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Mutable definitions, configuration and operator controls support operation without establishing this function.
- Closure path: No qualifying shipped closure for this function.
- Why this is / is not agent-owned: A legitimate owner and editable purpose do not alone establish a function-specific policy arbitration loop.
- Evidence: [docs/WORKSPACES.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/WORKSPACES.md); [packages/core/src/prompt.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/prompt.ts); [packages/core/src/plans/owner-questions.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/plans/owner-questions.ts); [packages/core/src/types/instruction-trust.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/types/instruction-trust.ts); [docs/EVOLUTION.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/EVOLUTION.md)
- Basis: structural
- Confidence: medium-high, bounded to the inspected distribution.
- Caveats: Downstream deployments can add organizational behavior.

### Absence scope

- Surfaces inspected: [docs/WORKSPACES.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/WORKSPACES.md); [packages/core/src/prompt.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/prompt.ts); [packages/core/src/plans/owner-questions.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/plans/owner-questions.ts); [packages/core/src/types/instruction-trust.ts](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/packages/core/src/types/instruction-trust.ts); [docs/EVOLUTION.md](https://github.com/AshishKumar4/kinu/blob/64e48f2bcb08d8a9a7a26b27552f79dcd361d16b/docs/EVOLUTION.md)
- Plausible first-party paths checked: SOUL.md purpose, workspace ownership root, trusted instructions, owner questions/answers and resume, plan/build permissions and owner reverts of learned changes.
- Why no material first-party path remains: The owner question path durably returns task answers and approvals; editable identity text and trust gates configure authority. No inspected shipped path identifies a distinct ultimate-policy/identity tension, arbitrates present versus future organizational demands under legitimate authority, and returns a governing policy decision. Generic ask_owner availability is not function-specific S5 closure.

## Recursion

Hires, temporary asks and swarm nodes are distinct operational actors. Nested hiring and shared infrastructure do not demonstrate complete recursive viability for every actor. The grades describe the bounded modes and ownership above.

## Variety and escalation

Dynamic state includes explicit totals when context rows are capped; native inspection can recover details. Durable reports and owner questions preserve unresolved matters across turns. Budget exhaustion, unmeasurable artifacts and missing merge parents refuse unsupported continuation. These mechanisms are not automatically algedonic/S5 loops.

## Evidence gaps

Source-first assessment at the immutable frozen ref. No live model/provider, external account, owner-device or deployment execution was performed. Mode reachability is structural, not proof of successful behavior on a benchmark. Optional swarm/advisor settings, provider availability and shared-plane limitations constrain coverage. No conclusion is borrowed from unpublished components or the maintainer's own organization.
