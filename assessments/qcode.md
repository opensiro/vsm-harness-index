---
harness_id: qcode
project_name: QCode
repository: https://github.com/fwtllh-png/QCode
review_ref: 0807662a3bd41efe4e7fdf74b3d260971d9e1cf0
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# QCode

## Review boundary

- System in focus: the first-party Go coding-agent `qcode` **Runtime/Agent Engine** operating on one configured local repository/workspace, together with its supported subordinate-agent organization in the same parent session. This is a coding-agent organization, not QCode the broader open-source maintainer team.
- Purpose and identity: carry out bounded user-directed code investigation, edit, command execution, verification and coordinated child work under explicit filesystem, sandbox, policy, permission, constitution, approval and journal gates.
- Relevant environment: selected local workspace, changing code/tests, model calls and tool results, child worktree edits and conflicts, user policy/approvals, model-provider/OS capabilities, Web supervisor.
- Standard-distribution boundary: executable Go `qcode` local Web/CLI runtime on supported **macOS** with explicit workspace/provider configuration and built-in guarded coding/subagent tools. The shipped `DelegationAdaptive` mode permits model-initiated delegation after independent-scoping justification, while the default `DelegationExplicit` mode requires legitimate user/developer/skill/system authorization. Claims are **mode-qualified**, not asserted for every first-run configuration.
- Credited operating / distribution surfaces: `internal/runtime/agent/engine`, first-party provider/tool adapters, guarded tool registry, `internal/orchestration/subagent` model-visible spawn/list/wait/followup/integrate controls, own workspace worktree isolation and merge manager, subagent admission budget governor, persistent session/agent graph, safety gates on mutating calls.
- Adjacent first-party surfaces excluded from ownership: `testdata/` benchmark/mock providers, `scripts/` and CI, `docs/` plans/roadmaps, Web React UI and desktop wrappers without an autonomous decision owner, contributor/project governance and optional MCP/Skill/third-party model subsystems. These may support but do not transfer external agent decision rights.
- First-party operating / deployment modes considered: single local interactive coding session with guarded model/tool loop; explicit user-authorized subagent work; supported adaptive delegation with model-chosen independent tasks, isolated worktrees and parent-directed integration; platform gates for macOS Seatbelt and fail-closed network/process controls. Multiple Workspaces configured through one Web supervisor are not presumed one shared VSM recursion.
- Recursion level: one parent coding session and its first-party subordinate S1 child threads in a selected workspace.
- Reviewed revision: `0807662a3bd41efe4e7fdf74b3d260971d9e1cf0` from frozen Index candidate intake #848.
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/README.md) identifies macOS local runtime/product interface and details explicit versus adaptive subagents, governed code tools and persistent sessions. [internal/runtime/agent/engine/engine.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/runtime/agent/engine/engine.go) constructs a first-party session/turn engine with stages for model call, tool preparation/run, approval, verification and results feedback; [internal/runtime/agent/engine/turn_handler.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/runtime/agent/engine/turn_handler.go) owns the running turn and invokes runtime tool/response operations. The current supported macOS distribution hosts the runtime behind `cmd/qcode`, local HTTP/Web and (optionally) a desktop shell. External inference/model backend computes output but does not itself own the surrounding QCode tool/gate/continuation loop.

[internal/adapter/tool/agent/agent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/adapter/tool/agent/agent.go) registers model-visible `spawn_agent`, `send_message`, `wait_agent`, `list_agents`, `followup_task`, `interrupt_agent`, `close_agent`, `integrate_agent`; [internal/orchestration/subagent/control_plane.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/control_plane.go) defines explicit/adaptive delegation modes and built-in child role contracts. [internal/orchestration/subagent/subagent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/subagent.go) manages child contexts, execution, worktree isolation, status, budgets, claims and subordinate agent graph. [internal/orchestration/admission/governor.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/admission/governor.go) accounts concurrent workers/child token and cost spend without counter overflow. [internal/orchestration/subagent/claims.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/claims.go) reports path-level conflicts between children that already wrote to *separate worktrees*; it does not outright prevent work. [internal/orchestration/subagent/integration.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/integration.go) records preview digests, conflicts, states and guarded transitions, while [internal/orchestration/chatmerge/service.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/chatmerge/service.go) requires matching current preview before guarded actual-branch merge, with journal rollback. The parent can inspect child status and conflict feedback before choosing integration or follow-up.

[internal/security/constitution/constitution.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/security/constitution/constitution.go) and `internal/security/policy`, `permissions`, `sandbox`, `controlplane` limit file/shell/editor operations and typed action authority, independent of whether the model thinks they are useful. [internal/persist/session/](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/persist/session/) and `state` maintain sessions, events, graph, receipts and recovery. Role labels (`review`, `verifier`) in the built-in catalog are not themselves a demonstration of a distinct independent corrective audit path; see S3* uncertainty.

## Operational model

One parent model-guided coding session observes working context and user instruction, selects first-party coding tools, receives gated tool/verification results and continues. In supported adaptive mode, the parent can choose scoped child objectives and parallelism, instantiate worker/explorer/reviewer/verifier tasks, read live child state/outputs and follow-up or integrate. Children perform independent first-party model/tool turns, normally in isolated worktrees. Conflicting actual write paths become explicit unresolved receipts rather than silent overwrite; integration requires a digest-bound preview followed by a guarded apply/verification path. The model-parent's semantic conflict-resolution and current task allocation choices are different from deterministic budget/permissions/worktree-journal enforcement. In explicit mode a user/developer/skill must authorize the delegation opportunity; that authority is not an autonomous root policy owner.

## S1 — Operations

- State: A
- Function: adaptively carry out one software-engineering task through model-guided repository tool execution and observation.
- Disturbance / variety regulated: unknown code structure, failing tests, code edits, model and tool outcomes, permission or sandbox denials, changing workspace state.
- Decisive decision or feedback right: choose the next repository search/edit/test/tool action and revise it from execution outcome.
- Decision owner: parent or child model actor in first-party `internal/runtime/agent/engine` executing a supported live coding turn; provider servers calculate inference but not the first-party agent execution organization.
- Supporting / enforcement mechanisms: model and tool adapters, permission/policy/constitution guard, workspace journal, sandbox, persistent conversation/evidence, user approval gates.
- Closure path: input/task → parent engine model call → selected guarded coding tool → filesystem/process feedback and journal/verify receipts → engine feeding results → subsequent model-driven action or completion.
- Boundary reachability: `qcode` shipped main runtime and guarded coding tools operate with the explicitly configured provider/workspace on macOS, without borrowing another coding-agent CLI.
- Why this is / is not agent-owned: model makes the substantive choice of tool and follow-up based on observed task; deterministic gates can veto or constrain but do not choose the semantic coding solution.
- Evidence: [README.md](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/README.md); [internal/runtime/agent/engine/engine.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/runtime/agent/engine/engine.go); [internal/runtime/agent/engine/turn_handler.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/runtime/agent/engine/turn_handler.go); [internal/adapter/tool/agent/agent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/adapter/tool/agent/agent.go).
- Basis: explicit first-party source.
- Confidence: high.
- Caveats: unsupported platforms, provider absence and deterministic operations alone are not independent S1=A evidence.

## S2 — Coordination

- State: A
- Function: attenuate actual inter-worker interference from concurrent editing of overlapping files before parent integration, and use conflict feedback for subsequent S1 work partition/revision.
- Disturbance / variety regulated: concurrent coding child S1s independently edit the same paths or supply incompatible changes, making merges/parent workspace inconsistent.
- Decisive decision or feedback right: parent model scopes eligible independent child tasks, examines real path-conflict reports and integration candidates, chooses follow-up, rerouting, redo/discard or candidate integration; mechanical worktree separation prevents premature shared mutation.
- Decision owner: model-driven parent in supported first-party **adaptive delegation** mode; role/policy constraints and host journal enforce, but do not make semantic conflict decisions for the parent.
- Supporting / enforcement mechanisms: isolated child worktrees, per-agent path claims, `Result.Unresolved` conflicts, preview digests and stale-plan rejection, guarded merge rollback, mailboxes/list/wait/followup/integrate tools.
- Closure path: parent model scopes/spawns distinct child agents → worktrees isolate concurrent writing → child terminal write claims report overlap/incompatibility → model-visible outcomes and preview influence parent integration/reassignment → guarded merge/followup changes subsequent coding work.
- Boundary reachability: subagent manager, adaptive delegation policy and all model-visible child/integration tools are shipped under QCode's own runtime, not an uninstantiated external framework.
- Why this is / is not agent-owned: worktree/claim/merge checks are deterministic; the model parent must resolve which conflicting candidate or path to adopt and what to re-run. Removing the model owner leaves diagnostics and a protection gate, not the task-specific conflict-resolution return.
- Distinct S1 units: separately running model-guided child coding agents with thread/context, tool authority and worktree isolation, under one parent session.
- Inter-S1 disturbance: two independently generated edits to the same path; changed-file conflicts and stale integration candidates after parallel work.
- Attenuating coordination relation: scoped delegation plus isolated execution, first-party cross-child write claim visibility and digest-bound preview/apply under the parent-directed integration right.
- Feedback into subsequent S1 behaviour: `Result.Unresolved`/worktree merge preview/child state evidence is reported to the parent and allows subsequent model-controlled followup and integration choices, with accepted merge changing shared workspace.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: an actual overlapping-write conflict is recorded at cross-agent ownership level and accounted for before code enters the shared parent workspace; adaptive remediation is exposed to the parent, rather than merely queuing unrelated tasks.
- Evidence: [internal/orchestration/subagent/claims.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/claims.go); [internal/orchestration/subagent/result.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/result.go); [internal/orchestration/subagent/integration.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/integration.go); [internal/orchestration/chatmerge/service.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/chatmerge/service.go); [internal/adapter/tool/agent/agent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/adapter/tool/agent/agent.go); [internal/orchestration/subagent/control_plane.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/control_plane.go).
- Basis: explicit source and mode-specific structural ownership.
- Confidence: medium.
- Caveats: unlike Foe's pre-admission directory exclusivity, QCode allows conflicting *isolated* work to finish and reports it before integration. Positive S2 relies on model-owned parent choice/feedback, not conflict reporting alone.

## S3 — Inside-and-now control

- State: A
- Function: supervise *current* parent-session team commitments and resource limits, choosing allocation/intervention among subordinate ongoing coding units.
- Disturbance / variety regulated: child/task overcommitment, budget/concurrency saturation, stalled or failing children, stale integrations and unfinished delegated work.
- Decisive decision or feedback right: parent model inspects current child roster/status/results, chooses eligible child spawning/followup/interruption/closure and integration priority in response to actual current obligations.
- Decision owner: model parent, with initial delegation permission bounded by user/developer/skill in explicit mode and a first-party adaptive-delegation mode when supported/configured; runtime governor accounts and enforces tokens/cost/depth/concurrency but does not choose semantic current task commitments.
- Supporting / enforcement mechanisms: `AgentControl`/manager's full child graph, `list_agents`/`wait_agent`, child status and receipts, admission governor `Snapshot`, persistent session, child worktree and process controls.
- Closure path: live team/session child statuses and results → parent model chooses followup/spawn/interrupt/close/integrate → runtime governed action updates child/team state and shared workspace → later parent model observations reflect changed current commitments.
- Boundary reachability: first-party child agent control and parent model-visible tools are packaged in shipped executable and can be used in supported adaptive mode with configured models and workspace.
- Why this is / is not agent-owned: governor constraints and manager state transitions follow fixed code, while model parent decides what part of ongoing team work to prioritize or adjust. A human clicking Web controls is not silently credited as autonomous S3.
- Whole-system current view: one current session's subagent graph, statuses, ownership, direct receipts and unresolved work visible via `list_agents`/control. The assessment makes no claim of one global QCode supervisor governing all user Workspaces as a model-owned organization.
- Current-control decision scope: task delegation and limits within available capabilities, child turn followups, shutdown/intervention, selection/discard/application of child work, next coding commitments.
- Evidence: [internal/adapter/tool/agent/agent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/adapter/tool/agent/agent.go); [internal/orchestration/subagent/subagent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/subagent.go); [internal/orchestration/admission/governor.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/admission/governor.go); [internal/orchestration/subagent/control_plane.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/control_plane.go); [README.md](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/README.md).
- Basis: source/structural owner return.
- Confidence: medium.
- Caveats: positive S3 is at *parent-session recursion* and does not imply global fleet-level policy, shared human governance or full automatic load optimization.

## S3* — Complementary audit

- State: ?
- Function: possible task-independent read-only reviewer or specialized verifier inspection of coding claims against direct evidence, with findings returned into parent correction before integration; whether this is a **closed complementary independent organizational audit** rather than task-time QA is unresolved in the shipped modes.
- Disturbance / variety regulated: agent implementation claims differing from actual patches/tests, misleading self-reported child results, unsafe changes from a subordinate episode.
- Decisive decision or feedback right: an independently tasked reviewer/verifier would inspect artifact/diff/test evidence, issue an independent judgment and cause a binding parent/operation corrective response.
- Decision owner: `RoleReview` and `RoleVerifier` are separately instantiated, read-only/test-focused child agents when selected, but no mandatory distinct audit authority or returned corrective decision path is proven from role catalog alone.
- Supporting / enforcement mechanisms: built-in role contracts, child evidence/verification receipts, `review` and `verify` tools, worktree diff visibility and parent integration preflight.
- Closure path: read-only review child can send findings to parent in a supported composition; inspected source does not establish that the separate complementary judgment is *authoritatively consumed* to re-regulate parent S3 rather than optionally considered as normal task QA. Thus positive and bounded absence are both withheld.
- Why this is / is not agent-owned: child reviewer is an agent capable of separate analysis, but the required independent evidence boundary and corrective-return ownership have not been reconstructed for the shipped ordinary operational integration path.
- Evidence: [internal/orchestration/subagent/control_plane.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/control_plane.go); [internal/orchestration/subagent/result.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/result.go); [internal/orchestration/subagent/integration.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/integration.go); [internal/adapter/tool/agent/agent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/adapter/tool/agent/agent.go); [README.md](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/README.md).
- Basis: unknown following inspection of concrete first-party plausible path.
- Confidence: unresolved.
- Caveats: check whether a supported role/test/approval flow provides an independently attested verdict and obliges parent rework or blocks integration; naming a child `review` is insufficient.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced first-party sensing of future external ecosystem change that generates and applies strategic/capability adaptation for the *QCode organization*.
- Disturbance / variety regulated: new external threats/requirements, prospective future coding tools/behaviors, future needed organizational capabilities.
- Decisive decision or feedback right: assess future-environment distinctions, develop adaptation options, select one and close return into current QCode operation.
- Decision owner: human maintainers/operator choose feature/config/skill adjustments; QCode agent plans steps for current task but does not own a shipped strategy adaptation loop.
- Supporting / enforcement mechanisms: plan and context modes, sessions, skills, MCP extensions, repo indexing, environment metadata, telemetry and roadmap.
- Closure path: persisted context or a user-installed skill can alter future requests, but no shipped autonomous external sensing → option evaluation → capability/config change → subsequent operational feedback is established.
- Why this is / is not agent-owned: future-looking code edits when requested by a human are ordinary task S1; plugin/skill extensibility is not agent-owned prospective organizational intelligence.
- Evidence: [internal/runtime/agent/engine/engine.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/runtime/agent/engine/engine.go); [internal/runtime/agent/engine/turn_handler.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/runtime/agent/engine/turn_handler.go); [README.md](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/README.md); [docs/zh-CN/architecture.md](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/docs/zh-CN/architecture.md).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: user-authored skills or future release work may add adaptation but are not credited at the pinned standard distribution.

### Absence scope

- Surfaces inspected: supported code/plan/agent operation, session persistence, model connection and skills, dynamic telemetry and extension surfaces, developer roadmap.
- Plausible first-party paths checked: automatic learning from external threat/product information, retention of strategic memory across sessions, agent-owned mutation of runtime capability/config beyond one coding task, parent-authorized future adaptation loop.
- Why no material first-party path remains: present code exposes coding/task and extensibility mechanics but no bounded first-party prospective external sensing/option-generation/selection that closes into runtime capability under organizational authority.

## S5 — Policy and identity

- State: —
- Function: permission/policy/constitution/approval enforce developer/operator-selected safety boundaries, not a first-party ultimate organizational values/identity resolution loop.
- Disturbance / variety regulated: tool execution risk, unsafe write changes, sensitive credentials, approval requests and child delegation overreach.
- Decisive decision or feedback right: legitimately resolve a disputed ultimate organizational policy/identity matter and return the authoritative determination to following operations.
- Decision owner: human operator configures policy and approves ordinary risky actions, while runtime protects invariant restrictions; child agent has bounded delegated authority. The model does not own ultimate goals.
- Supporting / enforcement mechanisms: constitution deny-write and tool scope, OS sandbox, postures `never/suggest/auto`, policy/permissions, append-only journals, user prompt and tool gate.
- Closure path: configured constraint → guarded operation allow/deny/ask → code runs or blocks. Ordinary approval updates a tool decision, not system ultimate-purpose governance.
- Why this is / is not agent-owned: hard safety enforcement and even mandatory approval cannot by itself decide identity-level tradeoffs; standalone `P` is not awarded from a human clicking an approval popup.
- Evidence: [README.md](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/README.md); [internal/security/constitution/constitution.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/security/constitution/constitution.go); [internal/orchestration/subagent/control_plane.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/orchestration/subagent/control_plane.go); [internal/adapter/tool/agent/agent.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/adapter/tool/agent/agent.go); [internal/security/policy/policy.go](https://github.com/fwtllh-png/QCode/blob/0807662a3bd41efe4e7fdf74b3d260971d9e1cf0/internal/security/policy/policy.go).
- Basis: bounded source negative.
- Confidence: medium-high.
- Caveats: an organization deploying QCode might build parent policy governance externally; this is not credited to the first-party runtime.

### Absence scope

- Surfaces inspected: explicit/adaptive delegation authority, constitution and guarded execution, user approval/postures, persistent policy/sessions, agent role and Web host operations.
- Plausible first-party paths checked: escalated constitutional conflict, parent human approval for ordinary actions, release/contributor governance, agent-authorized policy rewriting, legitimate ultimate-identity decision and returned operation.
- Why no material first-party path remains: user-configured policy is enforced; no first-party shipped issue → legitimate ultimate parent decision → changed binding policy → subsequent operation loop is evidenced beyond local authorizations.

## Distributed OSS parent arrangement

Upstream maintainers and independent local operators do not share one first-party organization-wide runtime, logs or legitimate governance controller. The user picks supported models, workspaces and authority; source contributors govern releases outside the assessed runtime. No qualifying S3/S4/S5 `(P)` closure is inferred from those disjoint authorities. Positive current-control is parent-session agent-owned and mode-qualified.

## Self-hosted and non-human modes

The macOS local supervisor can be human-administered; default subagent delegation is explicit, while adaptive delegation is an intentionally exposed supported mode. Agent parents use first-party orchestration tools when authorized; this is not proof of autonomous *ultimate* policy. Parent approval for a risky edit is not a distinct operational whole-team S3 or S5 return loop. Multi-session/web infrastructure and child-mode role catalog must not be silently promoted to additional recursive metasystems.

## Recursion

One model parent coding session is the selected recursion; subordinate independently running model/tool child agents form S1 units, with session-local graph and integration. Session nesting and agent role labels are mechanisms that may implement organizational functions when actual conflict/current-control witness and returned feedback exists; recursion is not inferred from generic hierarchy alone.

## Variety and escalation

Model actions and changing code create operational variety. OS sandbox, posture/constitution checks, isolated worktrees and conflict/merge guards attenuate unsafe actions and divergent child edits. Separate role child suggestions, approval prompts and verification receipts may surface exceptional findings to the parent/user; absent independent audit authority, these are not separately graded S3* or S5. Token/concurrency guards bound aggregate spend without deciding the team strategy.

## Evidence gaps

- A concrete shipped read-only `review`/test-focused `verifier` path exists; the decisive **complementary independence, audit judgment and corrective return** into whole-current parent S3 is not resolved by these sources. This is a *specific in-boundary* reason for S3*=`?`, not a generic absence of evidence.
- S2=A/S3=A are specific to adaptive model-guided delegation and the parent session's model-visible agent-control tools, not the unconfigured first-run Web UI or `DelegationExplicit` invocation with no authority to spawn.
- Tool and worktree evidence came from pinned primary implementation. No macOS native Seatbelt deployment or external model-backed task benchmark was executed; source structure validates availability and causal paths, not success or safety rates.
- Initial optional/host-controlled session details and future integrations cannot be claimed as organization-wide governance without independent supported source witnesses.

## Assessment summary

**Proposed disposition: `included`.** VSM vector `S1=A / S2=A / S3=A / S3*=? / S4=— / S5=—` at supported, shipped adaptive parent-session orchestration mode; S1 also exists in ordinary single-session coding. S3* intentionally remains unresolved because review/verifier role availability alone does not demonstrate a separately closed complementary audit return. No reviewer/test independence is claimed for this assessment itself.
