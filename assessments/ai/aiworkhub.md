---
harness_id: aiworkhub
project_name: AIWorkHub
repository: https://github.com/shrec/AIWorkHub
review_ref: 77bd873460b36df3312090948079d7158ad65081
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AIWorkHub

## Review boundary

- System in focus: one initialized repository-local AIWorkHub installation, including its shipped manager and worker role contracts and supported model adapters.
- Purpose and identity: deliver bounded software changes through repository-bound tasks, isolated agent work, evidence and verified manager acceptance.
- Relevant environment: the managed Git repository, requirements and owner constraints, authorized editor/CLI models, validation tools and concurrent work.
- Standard-distribution boundary: installed Python MCP runtime and VS Code extension, generated/on-attach role instructions, canonical task/context stores, worker/reviewer launch and acceptance machinery at the frozen revision.
- Credited operating / distribution surfaces: FastMCP manager contract and verified manager tools; first-party task-bounded worker prompt, workspace and observation/validation loop; conflict-specific plan/launch guards; separate anti-anchored read-only quality-review mode and returned acceptance/rework path.
- Adjacent first-party surfaces excluded from ownership: AIWorkHub's own development history, dogfood dashboards, performance claims, scripts/research/eval/release and CI workflows, tests as autonomous actors, and external repositories mentioned by CAAS. External CLI internal organization is not inherited.
- First-party operating / deployment modes considered: initialized VS Code manager chat, headless MCP manager deployment with writes/launch explicitly enabled, isolated CLI/editor workers, configured risk-based quality-review lenses, operator configuration and read-only defaults.
- Recursion level: the organization of one managed repository's current work; cards/workspaces are bounded operational cells, not independently established viable systems.
- Reviewed revision: `shrec/AIWorkHub@77bd873460b36df3312090948079d7158ad65081`; immutable intake #2446 / serial controller #2447; historical #201 pin preserved.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/README.md); [pyproject.toml](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/pyproject.toml); [docs/ARCHITECTURE.md](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/docs/ARCHITECTURE.md) describe a local stdio MCP control plane, with one repository's task/context/Source Graph truth under its own `.aiworkhub/`. MIT is the pinned project license. The VS Code extension packages the Python runtime and routes authorized model calls; headless clients can use the same MCP server. Writes and launches have separate opt-in gates, and workers do not inherit manager launch authority.

Crucially, [src/aiworkhub/server.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/server.py); [src/aiworkhub/core.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/core.py); [src/aiworkhub/agent_tool_instructions.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/agent_tool_instructions.py) deliver a manager responsibility/operating contract and a worker-specific runtime policy. The manager inspects the current Plan DAG, creates scoped tasks, chooses evidence-based work waves/routes, receives durable callbacks and accepts or rejects exact candidates. [src/aiworkhub/process_launcher.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/process_launcher.py); [src/aiworkhub/worker_workspace.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/worker_workspace.py); [src/aiworkhub/worker_ai_tools_mcp.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/worker_ai_tools_mcp.py) bind a worker to an exact card, isolated worktree, read scope, semantic edits and returned validation observations. CLI/editor inference is an adapter dependency; the first-party contract, tools and task loop are the credited organizational construction, rather than a borrowed external CLI metasystem.

[src/aiworkhub/task_plan.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/task_plan.py); [src/aiworkhub/core.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/core.py) expose concrete overlapping-write conflicts, active scope owners and dependency readiness. The runtime enforces admission; the manager chooses task scopes, dependencies and waves. [src/aiworkhub/quality_reviewer.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/quality_reviewer.py); [src/aiworkhub/quality_review.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/quality_review.py); [src/aiworkhub/process_launcher_accept_review.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/process_launcher_accept_review.py) separately bind a read-only reviewer to candidate source/diff/call-site evidence, exclude worker rationale and verify sealed findings before promotion or rework. Ordinary tests/logs alone are not credited as audit.

[src/aiworkhub/learning_commit.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/learning_commit.py); [src/aiworkhub/skill_miner.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/skill_miner.py); [src/aiworkhub/manager_skill_tools.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/manager_skill_tools.py); [src/aiworkhub/skill_registry_store.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/skill_registry_store.py) distill manager-adjudicated outcomes into proposed/evidence-gated skills and subsequent worker context. This is meaningful internal improvement, but the inspected path does not itself establish external-and-prospective S4. Roadmap and SDLC receipt state do not change that. [docs/CAAS_PROTOCOL.md](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/docs/CAAS_PROTOCOL.md); [src/aiworkhub/audit_system.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/audit_system.py) explicitly name a residual canonical NeedFix binding for the separate narrow-scope AuditSystem; that seam is not promoted to autonomous closure.

## Operational model

Operational outcomes are accepted repository changes, or truthful rejected/blocked work with exact residual evidence. An isolated worker owns code/evidence choices within its frozen task; a verified manager owns current work organization and acceptance. The manager is an agent role supplied by the supported host chat, not a deterministic scheduler. Plan guards, hashes, route checks, callbacks and databases enforce/transport those decisions. Human initialization/provider consent supplies the operating envelope; it is not assumed to close an S3/S4/S5 parent mode. Source-based positive states describe supported ownership paths, not measured effectiveness or guaranteed behavior in every run.

## S1 — Operations

- State: A
- Function: Produce a bounded software change and supporting evidence in a managed repository.
- Disturbance / variety regulated: Task ambiguity, code dependencies, implementation errors and validation observations within allowed writes.
- Decisive decision or feedback right: Choose bounded code/tool actions, revise against returned observations and submit a truthful candidate or blocker.
- Decision owner: The task-bound worker model actor under the shipped worker runtime contract.
- Supporting / enforcement mechanisms: Exact task/claim binding, isolated worktree, provider adapters, Source Graph/context tools, semantic edit and validation MCP surfaces, allowed-write/output enforcement.
- Closure path: Manager creates/launches an exact card → first-party worker prompt supplies scope and context → worker reads/edits/tests through bounded tools → observations inform its next actions → exit evidence reaches review_ready → verified acceptance promotes exact bytes or returns residual work.
- Boundary reachability: The installed launch MCP tool invokes ProcessManager.launch with the canonical card; build_worker_prompt installs WORKER_RUNTIME_POLICY on the shared launch path and supported CLI/editor adapters expose the worker tools. No AIWorkHub-development-only role is needed.
- Why this is / is not agent-owned: The worker chooses semantic implementation and repair; machinery neither chooses the patch nor makes its quality claim true. Removing the worker leaves enforced task state but no discretionary implementation. External model/CLI internals are not separately credited.
- Evidence: [README.md](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/README.md); [src/aiworkhub/agent_tool_instructions.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/agent_tool_instructions.py); [src/aiworkhub/process_launcher.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/process_launcher.py); [src/aiworkhub/worker_ai_tools_mcp.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/worker_ai_tools_mcp.py); [src/aiworkhub/worker_workspace.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/worker_workspace.py)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

## S2 — Coordination

- State: A
- Function: Regulate simultaneous write authority and dependency interaction among separate task workers.
- Disturbance / variety regulated: Two pending/processing/review cells can own overlapping file/glob scopes, causing destructive code interference or contaminated candidate evidence.
- Decisive decision or feedback right: Choose non-colliding scopes/dependencies and sequence or revise the next work wave from collision/readiness receipts.
- Decision owner: Verified manager agent, instructed to plan waves from repository evidence and never parallelize overlapping allowed_writes; deterministic arbitration remains support.
- Supporting / enforcement mechanisms: Plan-DAG active write-collision projection, path/glob overlap rules, deterministic priority/task-ID arbitration, launch collision guard, isolated workspaces and retained review scopes.
- Closure path: Manager reads task_plan_snapshot/collision state → chooses bounded scopes/dependencies and safe launches → launch guard refuses contenders behind active owners → completion/acceptance releases authority → refreshed plan changes which worker may run next.
- Boundary reachability: FastMCP installs MCP_MANAGER_CONTRACT_BANNER and manager_bootstrap delivers the operating contract; plan_snapshot, create/supersede/rework and exact launch tools are available in the initialized manager mode.
- Why this is / is not agent-owned: Agent ownership concerns work-wave/scope choices and adjustment, not the fixed tie-break or lock-like guard. With the manager removed the runtime can retain a reservation and enforce prior cards, but cannot exercise the same scope/wave discretion.
- Evidence: [src/aiworkhub/core.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/core.py); [src/aiworkhub/task_plan.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/task_plan.py); [src/aiworkhub/agent_tool_instructions.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/agent_tool_instructions.py); [src/aiworkhub/server.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/server.py); [tests/test_core_task_plan.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/tests/test_core_task_plan.py)
- Basis: structural
- Confidence: medium
- Caveats: The source-native overlap/release exercise corroborates support behavior. No multi-model concurrency run or observation of a manager revising an actual conflict is claimed; the ownership finding is structural in the delivered manager mode.
- Distinct S1 units: separate exact task-bound coding workers producing different changes in the same managed repository.
- Inter-S1 disturbance: concrete overlapping allowed_writes among active pending/processing/review cards; processing and review cells retain scopes.
- Attenuating coordination relation: manager chooses non-overlapping waves/scopes or serial dependencies; plan and exact-launch arbitration enforce exclusive admission against active contenders.
- Feedback into subsequent S1 behaviour: blocked contenders remain unlaunched; accepted/finished owners release scope and the refreshed snapshot makes later work eligible.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implementation detects exact inter-cell write collisions and governs subsequent write admission, rather than treating a generic DAG edge or mailbox as coordination.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the managed repository current work portfolio, shared execution capability and accountable acceptance.
- Disturbance / variety regulated: Conflicting present commitments, blocked dependencies, unavailable/costly model routes and unreliable worker completion claims.
- Decisive decision or feedback right: Select current task commitments/priorities/scopes and workforce routes; launch, supersede, reject, recover or accept work based on the current whole-repository evidence.
- Decision owner: The verified manager agent inside owner-supplied goals, policy and launch/write authority.
- Supporting / enforcement mechanisms: Canonical Plan DAG, health/preflight/workforce catalog/rank, completion inbox, exact identity gates, durable callbacks, cancellation, combined-tree validation and promotion receipts.
- Closure path: Manager reads whole-plan readiness/blockers plus live route/outcome evidence → creates prioritized cards and launches safe current waves → callbacks/inbox expose results and failures → manager accepts exact validated deltas or returns residual work/supersedes commitments → canonical state and next wave change.
- Boundary reachability: The installed manager bootstrap, Plan DAG, create/launch/supersede/reject/accept tools and callback route form the documented first-task and ongoing-work workflow, usable for any initialized repository.
- Why this is / is not agent-owned: This goes beyond decomposing one prompt: the contract requires repository-wide current-state reconciliation, work-wave planning and acceptance/intervention over durable ongoing cards. Deterministic ranking and accept gates enforce decisions without inheriting their ownership. Exact token caps remain owner/policy supplied, not autonomously invented by the manager.
- Evidence: [src/aiworkhub/core.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/core.py); [src/aiworkhub/server.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/server.py); [src/aiworkhub/completion_inbox.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/completion_inbox.py); [src/aiworkhub/workforce_catalog.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/workforce_catalog.py); [src/aiworkhub/process_launcher_accept_review.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/process_launcher_accept_review.py)
- Basis: structural
- Confidence: medium
- Caveats: No discretionary self-granted budget, universal provider availability or autonomous ultimate authority is asserted. Operator read-only dashboards, settings and generic owner prompts do not independently establish a distinct function-complete parent S3 mode.
- Whole-system current view: repository task DAG, active/review/blocked states, collisions/dependencies, completion evidence and live workforce availability/outcomes.
- Current-control decision scope: current commitments and priorities, safe work-wave/resource route selection, exception recovery, acceptance/rejection and replacement within the owner-defined repository envelope.

## S3* — Complementary audit

- State: A
- Function: Challenge candidate correctness/security/quality against direct operational artifacts independently of the producing worker report.
- Disturbance / variety regulated: A review_ready worker may claim success while changed code, callers or combined-tree behavior contradict the claim.
- Decisive decision or feedback right: A separate reviewer model inspects the sealed candidate and emits falsifiable lens-specific findings that can prevent acceptance and induce rework.
- Decision owner: Separate read-only quality-review agent for the audit judgment; verified manager owns corrective disposition, while receipt parsing/gating is deterministic support.
- Supporting / enforcement mechanisms: Anti-anchored packet, exact task/request/claim/hash binding, changed source and diff/caller evidence, candidate-scoped Source Graph, read_only reviewer card with empty allowed_writes, authenticated findings and acceptance/refinement gate.
- Closure path: After ordinary worker validation, risk-based review launches a separate reviewer on the sealed candidate → reviewer inspects raw evidence without worker rationale → authenticated findings enter acceptance/refinement → blocking findings hold promotion or produce residual rework → corrected candidate must be revalidated/reviewed before exact canonical promotion.
- Boundary reachability: Shipped aiworkhub_quality_reviewer_launch and risk-based review orchestration construct/bind the separate read-only card and wire its sealed receipt into accept_review. This works in supported installed client modes, independently of development CI and the unclosed AuditSystem sink seam.
- Why this is / is not agent-owned: The credited audit is the distinct blind/raw-evidence reviewer path, not routine worker self-tests or a verifier name. Its semantic judgment is agent-owned; anti-anchoring, isolation and hash checks support independence. Same-provider/model fresh-context mode is explicitly recorded and does not become a cross-provider claim.
- Evidence: [src/aiworkhub/quality_reviewer.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/quality_reviewer.py); [src/aiworkhub/quality_review.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/quality_review.py); [src/aiworkhub/process_launcher.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/process_launcher.py); [src/aiworkhub/process_launcher_accept_review.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/process_launcher_accept_review.py); [src/aiworkhub/review_orchestrator.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/review_orchestrator.py); [docs/QUALITY_CONTROL.md](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/docs/QUALITY_CONTROL.md)
- Basis: structural
- Confidence: medium
- Caveats: Structural reachability and packet invariants are inspected; no live semantic reviewer performance or actual independent-provider run is measured. CAAS naming, deterministic scan findings and ordinary manager review alone are not the positive witness.
- Claim being audited: worker review_ready success and semantic correctness/security/maintainability of the exact candidate.
- Ordinary reporting path: worker terminal status, self-validation outputs and durable completion evidence.
- Complementary access path: independently assembled changed-source/diff/caller and scoped Source Graph evidence; the reviewer may inspect candidate evidence beyond the worker narrative.
- Independence boundary: separate sealed, read-only reviewer invocation with no worker rationale/self-verdict and no repository mutation; provider/model separation is an explicitly recorded ladder, not an assumed universal condition.
- Who acts on findings: verified manager and review-orchestrator acceptance/refinement path; deterministic gates refuse invalid, missing or blocking review evidence and preserve/rework the candidate.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied function-specific external-and-prospective adaptation loop established at this product boundary.
- Disturbance / variety regulated: Changing external model/tool opportunities or user/environment requirements considered as future capability alternatives, rather than current task defects alone.
- Decisive decision or feedback right: Develop and judge future adaptation options from external distinctions and return them into current capability.
- Decision owner: No S4-specific autonomous or parent actor/return loop established; managers select current work and internal lessons.
- Supporting / enforcement mechanisms: Live workforce readiness and measured-outcome routing; Learning Commit, AI Memory/KB, skill mining/evidence-gated activation/injection, NeedFix/Roadmap and SDLC receipt stages.
- Closure path: Lessons from adjudicated task outcomes can become skills and subsequent worker context; model readiness changes current routing. The inspected paths do not supply the external/prospective option-development and capability conversation required for S4.
- Why this is / is not agent-owned: Real internal improvement and reusable knowledge are not automatically S4. A generic research task, a roadmap or an agent capable of writing arbitrary future code does not supply that function-specific loop; no closed P alternative is established by owner feature requests.
- Evidence: [src/aiworkhub/learning_commit.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/learning_commit.py); [src/aiworkhub/skill_miner.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/skill_miner.py); [src/aiworkhub/manager_skill_tools.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/manager_skill_tools.py); [src/aiworkhub/skill_registry_store.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/skill_registry_store.py); [src/aiworkhub/workforce_router.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/workforce_router.py); [src/aiworkhub/roadmap_store.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/roadmap_store.py); [src/aiworkhub/sdlc_case_store.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/sdlc_case_store.py)
- Basis: structural
- Confidence: medium
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Manager contract, workforce availability/outcome routing, learning-commit and skill-mining/activation/injection paths, memory/context writes, NeedFix/Roadmap/SDLC registries and public product architecture.
- Plausible first-party paths checked: Prospective model capability choice versus current route eligibility; reusable correction principles versus externally driven future adaptation; research cards and Roadmap outcomes versus an actual first-party option-development/return loop; operator requests as a possible parent mode.
- Why no material first-party path remains: The shipped paths regulate current execution and internally observed failures or store caller-authored work/evidence. No dedicated externally/prospectively distinguished adaptation judgment and return path is supplied; adjacent product-development research/release work cannot close it for an arbitrary installed repository.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy adjudication and return loop established.
- Disturbance / variety regulated: Ultimate purpose or unresolved present/future policy tension, distinct from ordinary task acceptance, provider consent and access controls.
- Decisive decision or feedback right: Resolve an identity/ultimate-policy issue through legitimate ultimate authority and return its decision to govern operation.
- Decision owner: Owners/developers configure operating constraints; no function-complete agent or parent S5 path established.
- Supporting / enforcement mechanisms: Repository identity binding, static repo/provider/quality policies, owner model pins, exact supplied token caps, opt-in write/launch gates and risk/destructive-change confirmations.
- Closure path: These settings and confirmations constrain launching, editing and acceptance. The inspected system does not route an identity/ultimate-policy issue for authoritative resolution and apply the returned decision as such.
- Why this is / is not agent-owned: A manager operating with the owner and static authoritative configuration do not by themselves establish S5. CAAS terminology rules and OSS maintainer policy concern adjacent development/governance, not a supplied installed-product ultimate-policy loop.
- Evidence: [src/aiworkhub/repo_policy.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/repo_policy.py); [src/aiworkhub/model_settings.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/model_settings.py); [src/aiworkhub/core.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/core.py); [src/aiworkhub/agent_tool_instructions.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/agent_tool_instructions.py); [src/aiworkhub/server.py](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/src/aiworkhub/server.py); [docs/CAAS_PROTOCOL.md](https://github.com/shrec/AIWorkHub/blob/77bd873460b36df3312090948079d7158ad65081/docs/CAAS_PROTOCOL.md)
- Basis: structural
- Confidence: medium
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Initialization/identity, manager authority contract, repository/model policies, cap ownership, high-risk/destructive confirmation, context-write acceptance and CAAS governance split.
- Plausible first-party paths checked: Owner prompts/overrides, policy.json and settings changes, manager final acceptance, skill activation and protocol enforcement as possible autonomous/parent policy paths.
- Why no material first-party path remains: All established paths bind repository/permission or decide bounded work/capability usage. None supplies the required identity/ultimate-policy matter→legitimate authority→authoritative return closure at this installed-repository recursion.

## Distributed OSS parent arrangement

Each installed repository has local authority and state. AIWorkHub maintainers and contributors govern the product source separately; their distributed dogfood activity is not the parent of every user installation. Human initialization, consent and task constraints are acknowledged, but no organization-level or function-complete parent modifier is inferred.

## Self-hosted and non-human modes

Both initialized VS Code and headless MCP modes use shipped contracts/tools, with write/launch capabilities explicitly enabled. Read-only defaults do not execute an autonomous work organization. The manager role is supplied by the supported host model chat; runtime instructions and wired authority make it first-party reachability, while the host model/CLI internal metasystem remains outside the claim. A wholly non-human ultimate-governance mode is not established.

## Recursion

A repository-local manager/worker organization is established. Independent repository instances and nested task/reviewer cards do not prove recursive viability; complete per-card S2–S5 organizations are not claimed.

## Variety and escalation

Task identity, source/context scope and write guards attenuate operational variety. Collision feedback and current-plan receipts expose cross-cell disturbances. Blind candidate inspection challenges reporting compression; callbacks preserve wake-up and claim provenance. Workers return blockers to managers, and unavailable authority stays fail-closed. These channels are not inferred to be algedonic or identity-level governance merely from exceptional status.

## Evidence gaps

This is pinned-source structural assessment, not provider-backed execution or a causal quality/cost benchmark. Full upstream pytest was attempted but unavailable because pytest is absent. Direct native-module assertions passed for overlapping-scope admission and release feedback, reviewer-packet delivery/tamper rejection and the explicit same-model fresh-context independence rung; they do not establish actual agent judgment. An initial hand-built source-evidence fixture was correctly refused for a missing candidate hash, then the minimal sealed-packet exercise passed. Live manager behavior, cross-provider independence and production effectiveness remain unobserved. The separate AuditSystem canonical NeedFix sink residual is recorded rather than credited as closed. No specific unresolved shipped S4/S5 path remains after the bounded review; hypothetical extensions are not used to manufacture unknown states.
