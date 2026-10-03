---
harness_id: axiom
project_name: Axiom
repository: https://github.com/amuluze/axiom-agent
review_ref: da7b98b739a824713d230b2635edb56868553696
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Axiom

## Review boundary

- System in focus: the first-party Axiom desktop engineering-agent distribution at frozen public revision `da7b98b739a824713d230b2635edb56868553696`, including its streaming model/tool loop, AgentSession/AgentHarness runtime, workspace tools and approvals, durable session/recovery machinery, default desktop SubAgent runtime, discoverable Explore/Inspect/Examine/Review child agents, project-context/skills loading, and directly owned design/browser/computer/SSH execution surfaces where they participate in the assessed organization.
- Purpose and identity: execute local-first engineering work across design, coding and deployment while keeping workspace authorization, session state, approvals, recovery and tool execution inside one desktop product boundary.
- Relevant environment: the authorized local workspace, user objective, local filesystem and Git state, configured model/provider, browser/desktop/SSH targets when explicitly used, project documentation/skills, approval decisions, durable session state and tool results.
- Standard-distribution boundary: the public desktop source/distribution and its first-party TypeScript/Tauri/Rust runtime are inside. External model providers, host OS processes, target repositories/servers and user-authored project policy are dependencies/environment. The private development upstream may not donate evidence absent from this frozen public distribution.
- Credited operating / distribution surfaces: `apps/desktop/src/agent/core/runAgentLoop.ts`; `runtime/AgentSession.ts`; `runtime/AgentHarness.ts`; product tool/runtime assembly; approval/workspace boundary; SubAgent runtime and built-in reviewer tools/prompts; desktop store wiring that enables the default capabilities; session/recovery and project-context surfaces.
- Adjacent first-party surfaces excluded from ownership: unit/E2E tests and runtime-fault automation; CI/release machinery; public-repository feedback/development governance; private upstream behavior not present in this frozen public ref. These surfaces may corroborate invariants but do not donate operating VSM ownership.
- First-party operating / deployment modes considered: normal Tauri desktop engineering sessions with the production runtime policy; discover-gated tool activation; workspace read/write/execute; default Explore and Review SubAgent capabilities; branch/retry/checkpoint recovery; design, browser/computer and SSH tools where enabled and approved.
- Recursion level: one Axiom engineering session around one user objective/workspace. The main model-backed session is the primary operating S1. Read-only reviewer children are complementary audit actors, not peer production S1 units merely because they run separate model loops.
- Reviewed revision: `da7b98b739a824713d230b2635edb56868553696`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Axiom ships its own streaming model/tool runtime rather than delegating organization to an external agent framework. `runAgentLoop` owns message/model turns, tool execution, returned observations, budgets, queued messages, mutation batches and turn save points. `AgentSession` adds durable queues, runtime-update journaling, recovery and the bridge from model-facing delegated tools to `SubAgentRuntime`. `AgentHarness` exposes the session through the product runtime and hooks while enforcing lifecycle invariants.

Desktop production policy grants workspace read/write/execute plus `subagent:explore` and `subagent:review` by default. The product creates a real `SubAgentRuntime` and injects it into each runtime session. Reviewer tools are present in the registered tool table when their default capabilities are available; they are discover-gated rather than initially active. `discover_agent_tools` is always active, so the main agent can autonomously discover and activate `inspect_subagent`, `examine_subagent` or `review_subagent` during a run.

Each delegated reviewer is a separate, non-persistent child model session with a role-specific system prompt, scoped read-only environment, its own child session identity and bounded model/tool budget. It cannot write files, execute commands, request approvals or re-delegate. For code review, the parent can provide the actual Git diff plus scope; the child then reads relevant current files and returns a structured pass/fail judgment and issue list. The parent-facing tool parses that verdict. A failed verdict injects an explicit instruction to return to the prior stage, fix the findings and re-run review before finishing; the canonical SDD prompt independently encodes the same implement → review → repair/re-review closure. The gate is intentionally soft rather than a deterministic hard block, leaving the autonomous parent model the corrective decision/action channel.

Axiom also has substantial persistence, recovery, project-doc and project-skill machinery. Project docs/skills are rescanned/reloaded into the current session context and runtime dependency manifest, and queued/runtime mutations are journaled for crash recovery. These paths preserve current capability/context and externally authored project guidance; they are not by themselves prospective self-adaptation or identity-policy governance.

Primary evidence:

- [README.md](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/README.md)
- [`runAgentLoop.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/core/runAgentLoop.ts)
- [`AgentSession.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/runtime/AgentSession.ts)
- [`runtimePolicy.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/config/runtimePolicy.ts)
- [`agentStore.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/stores/agentStore.ts)
- [`createToolRegistry.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/tools/createToolRegistry.ts)
- [`productToolRuntime.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/runtime/productToolRuntime.ts)
- [`SubAgentRuntime.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/SubAgentRuntime.ts)
- [`createReviewerSubAgentTool.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/reviewers/createReviewerSubAgentTool.ts)
- [`buildReviewPrompt.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/reviewers/buildReviewPrompt.ts)
- [`systemPromptSections.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/prompt/systemPromptSections.ts)

## Operational model

A normal desktop run begins with an authorized workspace, a user objective and a configured provider. The main Axiom model receives first-party tools and current project/session context, selects a tool or response, and receives concrete results/errors in later turns. Mutating/execute operations pass through Axiom's approval and workspace enforcement, while the open-ended choice of what engineering action to propose next remains with the model-backed actor.

For complex or high-risk work, the same main agent can discover a first-party reviewer tool and delegate an independent read-only child. The reviewer obtains separate context and direct workspace evidence, produces a pass/fail audit judgment, and returns it as a tool result. A failed result explicitly sends the parent back to corrective work and re-review before finish.

## S1 — Operations

- State: A
- Function: perform environment-facing engineering work by interpreting the objective, inspecting artifacts, selecting coding/design/deployment tools, proposing or applying authorized changes, observing results and iterating toward completion.
- Disturbance / variety regulated: heterogeneous project structure and code, incomplete task information, tool/provider failures, approval outcomes, changing workspace state, tests/commands, design/browser/remote evidence, context pressure and restart/recovery conditions.
- Decisive decision or feedback right: choose the next task-specific engineering action/tool, which evidence to gather or state to change, and when the requested operation is complete.
- Decision owner: the main model-backed Axiom agent operating through the first-party model/tool runtime.
- Supporting / enforcement mechanisms: tool registry/discovery; workspace authorization and approval leases; sandbox and redaction; durable session/recovery journal; context compaction; queues; runtime budgets; provider transport; project docs/skills; checkpoints and branch/retry support.
- Closure path: user objective/current session context → model selects action/tool → Axiom enforcement and tool execution against the environment → result/error persisted and returned → next model turn revises action or completes.
- Boundary reachability: the normal production desktop runtime directly instantiates the first-party AgentSession/AgentHarness with the product tool runtime; no downstream application author must compose a separate agent loop.
- Why this is / is not agent-owned: if the main model actor is removed while deterministic tools, approvals, persistence and recovery remain, the open-ended engineering choice of what to inspect/change/do next disappears.
- Evidence: [README.md](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/README.md); [`runAgentLoop.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/core/runAgentLoop.ts); [`AgentSession.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/runtime/AgentSession.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: side-effecting tools can require user approval, but approval gates the main agent's proposed action rather than supplying the engineering judgment itself.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the assessed recursion.
- Disturbance / variety regulated: no concrete collision, interference or oscillation among distinct production S1 units is present in the standard organization. Reviewer/explore children are scoped read-only subordinate roles invoked synchronously for evidence/audit rather than peer workers mutating a shared operational domain.
- Decisive decision or feedback right: not established at S2 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: child scope isolation; read-only child tool set; parent/child budgets; sequential child tool execution; message queues; durable mutation/session journals; workspace authorization.
- Closure path: not applicable; no distinct production-S1 interference → attenuation → changed later S1 behavior relation was found.
- Why this is / is not agent-owned: SubAgent plurality does not itself establish S2. The frozen runtime supplies reviewer/explorer support units, but no shared-write peer population or concrete inter-operational conflict requiring coordination.
- Evidence: [`SubAgentRuntime.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/SubAgentRuntime.ts); [`contracts.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/contracts.ts); [`createToolRegistry.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/tools/createToolRegistry.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: separate child model sessions are real actors, but their read-only reviewer/explorer roles do not turn them into mutually interfering production S1s.

### Absence scope

- Surfaces inspected: complete frozen tree; main loop/session/harness; SubAgent runtime/contracts/budgets; built-in Explore/Inspect/Examine/Review tools; queues; workspace approval/recovery; desktop capability and tool activation policy.
- Plausible first-party paths checked: simultaneous children, shared-write child workers, peer task assignment, child-child messaging/arbitration, parent scheduling of competing production work, resource/contention handling and queue coordination.
- Why no material first-party path remains: child delegation is bounded, read-only and returned as a parent tool result; no first-party operational peer set with an evidenced interference mode and coordination feedback path is shipped at this revision.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control function over a population of operational commitments/resources is established at the assessed recursion.
- Disturbance / variety regulated: run budgets, queue state, approvals, runtime updates, recovery, child delegation limits and lifecycle hooks regulate one main engineering session and its support/audit calls rather than a whole organization of production S1 units.
- Decisive decision or feedback right: not established at S3 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: AgentSession/AgentHarness lifecycle; message queues; mutation journal; turn save points; runtime hooks; subagent parent-run ledger; abort/deadline controls; approval coordinator; recovery/checkpoints.
- Closure path: these paths constrain, recover or support the focal operating session. No actor with a whole-system view chooses or revises shared production commitments, priorities, resource allocations or cross-S1 interventions.
- Why this is / is not agent-owned: the main agent can choose to delegate a reviewer/explorer, but managing support calls inside its own task is ordinary S1 work, not evidence of S3 over distinct operational units.
- Evidence: [`AgentSession.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/runtime/AgentSession.ts); [`AgentHarness.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/runtime/AgentHarness.ts); [`contracts.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/contracts.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: extensive runtime control and recovery should not be promoted to S3 merely because they supervise execution.

### Absence scope

- Surfaces inspected: AgentSession/AgentHarness; run budgets; queues; runtime hooks/updates; subagent ledger and delegation bridge; observability; recovery/checkpoints; approvals; settings/policy surfaces.
- Plausible first-party paths checked: parent-agent child control, live task/resource allocation, concurrent operational workers, global queue arbitration, provider/resource management, operator control and recovery interventions.
- Why no material first-party path remains: identified control surfaces remain lifecycle/enforcement/support for one primary S1 plus subordinate read-only roles, not a closed current-control loop over multiple operational commitments.

## S3* — Complementary audit

- State: A
- Function: independently review specifications/plans/code changes through a separate read-only model session, judge them against direct project evidence and return pass/fail findings into the parent agent's corrective workflow.
- Disturbance / variety regulated: specification/plan defects, implementation bugs, security regressions, inadequate tests, contract violations and cases where the implementer's ordinary self-assessment would otherwise allow incorrect work to finish.
- Decisive decision or feedback right: the child reviewer independently decides a structured pass/fail audit verdict and prioritizes concrete `path:line` findings from its own scoped read evidence; the parent model receives that verdict as a tool result and owns the subsequent correction/re-review response.
- Decision owner: a separate model-backed Axiom reviewer child for the substantive audit judgment. Deterministic verdict parsing and notices only expose/enforce the child's conclusion.
- Supporting / enforcement mechanisms: default `subagent:review` capability; `discover_agent_tools`; review/inspect/examine tool contracts; separate SubAgent child session; scoped read-only environment; reviewer-specific prompt; optional actual diff supplied by the parent; child/parent budgets; verdict parser and fail notice.
- Closure path: main agent implements/specifies/plans → autonomously discovers and invokes reviewer → separate child reads scoped operational artifacts (and code diff when supplied) → child emits pass/fail + findings → first-party tool parses and returns verdict to parent → fail notice and canonical SDD rules direct parent back to repair → parent can change the work and re-run review before finish.
- Boundary reachability: production desktop policy grants `subagent:review` by default, product startup creates and injects the first-party `SubAgentRuntime`, the review tools are registered in the ordinary tool table, and always-active `discover_agent_tools` lets the main model activate them without developer composition or user approval.
- Claim being audited: that the current Task Spec/Plan/implementation is sufficiently correct, safe, tested and contract-compatible to advance or finish.
- Ordinary reporting path: the main engineering agent's own plan/implementation and ordinary tool/test results inside its working session.
- Complementary access path: a separately instantiated child model session with a reviewer-specific system prompt and scoped read-only access re-reads the current workspace independently; for code review it can additionally receive the parent-collected Git diff as authoritative change evidence.
- Independence boundary: the reviewer has separate child session identity/context, cannot mutate the workspace or inherit the parent's conversation as an ordinary continuation, and forms its own pass/fail judgment from direct read evidence. It shares the configured model/transport family unless the operator changes that configuration, but the organizational judgment path is a distinct model invocation/session rather than the implementer's in-band self-report.
- Who acts on findings: the main Axiom agent receives the reviewer result. On fail, the tool result explicitly instructs it to return to the previous stage, fix findings and re-delegate review; the standard SDD system prompt independently encodes fail → repair → re-review before finish. A user can explicitly accept risk and override the soft gate.
- Why this is / is not agent-owned: removing the reviewer model while retaining the deterministic verdict parser, budgets and fail-message machinery removes the substantive independent defect judgment. The parser cannot manufacture a pass/fail audit finding on its own.
- Evidence: [`runtimePolicy.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/config/runtimePolicy.ts); [`agentStore.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/stores/agentStore.ts); [`SubAgentRuntime.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/SubAgentRuntime.ts); [`createReviewerSubAgentTool.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/reviewers/createReviewerSubAgentTool.ts); [`buildReviewPrompt.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/subagent/reviewers/buildReviewPrompt.ts); [`systemPromptSections.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/prompt/systemPromptSections.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the corrective gate is model-visible and workflow-enforced rather than a deterministic hard block; users can explicitly accept risk. That does not remove the autonomous complementary audit judgment or its normal corrective return path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective organizational adaptation loop is established.
- Disturbance / variety regulated: project docs/skills, provider/runtime settings, context compaction, session recovery and tool discovery alter current execution context/capability exposure but do not sense future environmental change and autonomously choose a persistent capability/strategy adaptation.
- Decisive decision or feedback right: not established at S4 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: project document scanning/reload; project skill inventory/load; runtime dependency refresh; provider/model settings; context manager; durable session state and recovery.
- Closure path: changed project files/configuration can be rescanned into later current prompts, but no first-party prospective scan → adaptation option generation → selected persistent organizational capability change → operational return loop is present.
- Why this is / is not agent-owned: generic ability to write project files plus later reload does not establish a function-specific adaptation decision. The reload machinery consumes externally/currently changed artifacts rather than deciding a future capability change itself.
- Evidence: [`projectDocs.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/prompt/projectDocs.ts); [`loadProjectSkills.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/skills/loadProjectSkills.ts); [`projectDocsRefresh.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/stores/services/projectDocsRefresh.ts); [`AgentSession.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/runtime/AgentSession.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: durable reloadable project artifacts can influence later behavior, but persistence/reload alone is not S4 without a prospective adaptation function and decisive adaptation right.

### Absence scope

- Surfaces inspected: project docs/skills loaders and refresh scheduler; runtime dependency updates; provider/model/reasoning settings; context compaction; session recovery; design/deployment tools; SubAgent prompts and built-in workflow.
- Plausible first-party paths checked: self-authored reusable skills, automatic project-doc evolution, benchmark/evaluation-driven capability selection, dynamic model/tool adaptation, self-update and external trend/environment scanning.
- Why no material first-party path remains: no standard path was found where Axiom itself forms future-oriented adaptation options and enacts a persistent capability/strategy change from that prospective intelligence.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity or ultimate-policy closure is established at the assessed recursion.
- Disturbance / variety regulated: workspace authorization, approval modes, capability policy, prompts, project docs and user decisions constrain work, but they do not form a first-party identity/ultimate-policy adjudication loop.
- Decisive decision or feedback right: not established at S5 scope.
- Decision owner: not established within the Axiom runtime.
- Supporting / enforcement mechanisms: production runtime policy; workspace authorization; approval coordinator/leases; system prompt; user/project documentation; settings; sandbox/network/security enforcement.
- Closure path: policy/configuration is supplied or changed externally and enforced/loaded into operation. No identity/ultimate-policy issue is routed to a legitimate first-party S5 authority, resolved there and returned as an authoritative organization-wide policy change.
- Why this is / is not agent-owned: the main/reviewer agents operate under the supplied capability/security/project boundaries but do not possess authority to redefine Axiom's purpose, identity or ultimate policy.
- Evidence: [`runtimePolicy.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/config/runtimePolicy.ts); [`ApprovalCoordinator.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/approval/ApprovalCoordinator.ts); [`systemPromptSections.ts`](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/apps/desktop/src/agent/prompt/systemPromptSections.ts); [README.md](https://github.com/amuluze/axiom-agent/blob/da7b98b739a824713d230b2635edb56868553696/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: user approval can override a soft review gate and project owners can author durable guidance. Generic approval/configuration is not promoted to S5 without an identity/ultimate-policy function.

### Absence scope

- Surfaces inspected: runtime capability policy; system prompt; workspace authorization/approval; settings; project docs/skills; runtime updates; session/recovery; reviewer override semantics; public repository governance.
- Plausible first-party paths checked: agent-authored constitutional/mission policy, durable policy escalation to a parent authority, runtime governance decisions, approval flows as possible S5, project policy reload and maintainer/private-upstream authority.
- Why no material first-party path remains: decisive ultimate-purpose/policy authority remains external configuration/user/project ownership, and no runtime S5 adjudication-and-return loop is implemented in the public frozen distribution.

## Recursion

The primary engineering agent is one operational S1. Separate Explore and reviewer child model sessions are subordinate evidence/audit roles with scoped read-only tools and bounded lifetimes. They do not constitute peer production recursion or a higher-level viable operating organization at this boundary.

## Variety and escalation

Axiom amplifies operational variety through a broad first-party tool surface, discoverable capabilities, design/browser/computer/SSH paths, separate reviewer agents and durable session state. It attenuates risk and failure through workspace authorization, per-action approval, sandboxes, child budgets, run limits, persistent mutation journals, checkpoints, recovery and independent review.

Exceptional findings can return from the reviewer into the parent agent's correction loop; runtime failures can abort/recover through journal/checkpoint paths; human approval can deny side effects or explicitly accept review risk. These are meaningful assurance/escalation mechanisms but do not establish positive S2, S3, S4 or S5 at the assessed recursion.

## Evidence gaps

The assessment is frozen to the public distribution at `da7b98b739a824713d230b2635edb56868553696`. The private upstream was explicitly excluded from evidence. The complete frozen source tree and the plausible control/adaptation/governance paths above were inspected. No unresolved evidence gap requires `?`.

## Assessment summary

Axiom closes autonomous S1 through its first-party engineering model/tool loop and autonomous complementary S3* through standard, model-selectable read-only reviewer children whose independent pass/fail findings return into a repair/re-review workflow. Its remaining multi-agent/runtime machinery does not establish inter-production S2 or whole-system S3, project docs/skills/runtime refresh do not close prospective S4, and approval/policy/configuration surfaces do not establish S5.

Proposed vector: **`A · — · — · A · — · —`**
