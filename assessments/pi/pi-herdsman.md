---
harness_id: pi-herdsman
project_name: Pi Herdsman
repository: https://github.com/boadij/pi-herdsman
review_ref: 2b78e1b7b4a62240f7be881ab066be4cefbee612
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Pi Herdsman

## Review boundary

- System in focus: one installed Pi Herdsman orchestration environment with directly owned model-driven Agents, optional branch-assigned project Leads and their Manager, and optional higher Chief supervision.
- Purpose and identity: supply bounded asynchronous coding-agent delegation, durable exact-session/branch ownership, project coordination, and current supervision while the controlling Pi model session remains interactive.
- Relevant environment: user coding requests; Pi model/tool responses and sessions; independent local worktrees/branches; Herdr execution/process topology; result/evidence handoffs; incomplete or conflicting assignment and process state.
- Standard-distribution boundary: the npm Pi extension loaded through the package manifest, its installed model-facing role contracts and registered controller/staff/peer tools, local persistent assignments/mailboxes, and documented optional Manager/Chief modes. Pi itself and Herdr supply external model and process engines but are used through directly wired first-party integrations.
- Credited operating / distribution surfaces: `extension/index.ts`, `agent-controller.ts`, `managed-agent-runtime.ts`, `lead-runtime.ts`, `supervision.ts`, `herdr.ts`, `storage.ts`, `mailbox.ts`, `peer-correspondence.ts`, and the package's active default role definitions.
- Adjacent first-party surfaces excluded from ownership: repository ADR/history, developer instructions, tests and fixtures, package validation/release CI, container/development scripts, demo media, and project-maintainer governance; external Pi and Herdr private metasystems and arbitrary user-defined agents/extensions are not automatically attributed to Herdsman.
- First-party operating / deployment modes considered: an ordinary Pi Lead with directly delegated Agent tasks; explicitly delegation-enabled nested Agents; project Manager in the primary repository workspace with multiple assigned Leads on worktree branches; optional workspace-neutral Chief; supervised/paused/retired sessions, peer coordination and optional human-approved checkout removal.
- Recursion level: one local project orchestration system when a Manager is active, with Lead/Agent operational subunits; Chief is considered as an optional adjacent supervisory level, not silently merged with project ownership.
- Reviewed revision: `2b78e1b7b4a62240f7be881ab066be4cefbee612`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Pi Herdsman is an installable Pi extension, not an independently packaged LLM. The first-party extension registers agent-delegation and direct-owner controls, resolves agent definitions and permitted tools, launches/continues managed Pi sessions through Herdr, and delivers verified results and questions back along exact ownership edges. Managed Agent requests, session identities, mandatory evidence and result bindings are persisted for interrupted/recovered runs. A delegating Agent may own an explicitly allowed next tier; that is a bounded dependency structure, not automatic VSM recursion.

The optional project Manager is itself a model-operated Pi session with a role charter and project tools. It can create worktree/branch-bound managed Leads, inspect a fresh assigned-work ledger, message or steer exact Leads, stop/resume work, and integrate a specifically accepted commit by guarded local fast-forward. A separate Chief supervises direct-report Managers/ordinary Leads without inheriting a Manager's branch authority. Exact process, branch and assignment checks prevent one controller from silently appropriating another session. Per-role tool allowlists, leases, mailbox persistence, process locks and Git verification enforce those decisions; they do not themselves make autonomous decisions. Agent/Lead result handoffs are nonterminal and must not be confused with project acceptance or worktree retirement.

Primary sources: [package distribution](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/package.json), [extension wiring](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/index.ts), [agent controller](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/agent-controller.ts), [managed runtime](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/managed-agent-runtime.ts), [lead runtime](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/lead-runtime.ts), [coordination contract](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/concepts/coordination.md), [project guide](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/guides/project-orchestration.md).

## Operational model

An ordinary Lead receives a user task, makes task-level coding/analysis decisions in its Pi model loop, and can transfer bounded work to Agent sessions with explicit direct ownership. When project mode is selected, Manager decomposes a project objective across branches, delegates it to independently reasoning managed Leads, observes their progress/failures, sends corrective messages, and may integrate an accepted exact source revision after the Lead's own checks. Leads retain technical solution and validation rights; Manager owns project assignment and integration decisions. Multiple worktrees and agent trees allow concurrent, distinct environmental transformations, while exact assignment/worktree verification and model-directed messages regulate collision risk. A Chief can exercise a larger direct-report supervision scope but cannot bypass a Manager's assigned Leads. No distinct autonomous product audit institution, prospective external capability-adaptation program, or ultimate-policy dispute-return path is established merely by these roles.

## S1 — Operations

- State: A
- Function: model-owned completion of bounded coding/analysis work by directly delegated Agents and, in project mode, independently reasoning managed Leads.
- Disturbance / variety regulated: changing task requirements, file content, tool outcomes, partial work, failures and follow-up questions within one owned assignment.
- Decisive decision or feedback right: the current Lead/Agent model selects task decomposition, investigation, edits/tests, requests to its direct owner and final reported result; a project Lead retains implementation/validation judgment rather than having every step prescribed by Manager.
- Decision owner: supported Pi model actors in the exact owned Lead/Agent sessions, with a Manager model choosing project assignment objectives when that mode is active.
- Supporting / enforcement mechanisms: agent definitions, scoped tool allowlists, Herdr-launched Pi sessions, exact-session assignment records, required-evidence snapshots, durable request/result mailboxes, bounded context retirement and direct-owner result delivery.
- Closure path: user/Manager objective → model-decided Lead/Agent tools and delegation → local task actions/evidence → completed session result or blocking question → exact owner receives result/answers and changes subsequent work or acceptance.
- Boundary reachability: installed extension exports and registers `delegate_agent`/`continue_agent` and associated owner tools, starts managed Pi sessions, and injects active role policies. The advertised normal Lead and Manager modes reach the same real agent runtime; fixtures are not needed to supply the actor.
- Why this is / is not agent-owned: removing the model-owned Pi session leaves session/permission/transport machinery but not the task-specific choices or final substantive work. Provider mechanics are external; the first-party harness directly assembles and governs their installed task loops.
- Evidence: [delegation contract](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/concepts/delegation.md), [agent controller](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/agent-controller.ts), [managed session runtime](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/managed-agent-runtime.ts), [project Lead charter](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/guides/project-orchestration.md).
- Basis: explicit and structural.
- Confidence: high for shipped wiring and local decision-right separation; no live provider task was attempted.
- Caveats: tool execution and model inference depend on installed Pi/Herdr and selected provider; neither an external agent's unrelated internal metasystem nor user-defined agents are automatically credited.

## S2 — Coordination

- State: A
- Function: project-level attenuation of interfering concurrent Lead assignments on branches/worktrees, with model-controlled corrective routing and worker-directed return.
- Disturbance / variety regulated: multiple S1 writers to one checkout, duplicate branch ownership, stale assignment/checkout identity, incompatible integration bases and cross-Lead conflicting changes.
- Decisive decision or feedback right: the Manager model chooses branch-scoped delegated objectives and correction/integration order, can steer the exact responsible Lead to reconcile an outdated base, and may revise assignments in response to report/conflict evidence.
- Decision owner: Manager Pi model for substantive branch/assignment coordination; deterministic Herdsman/Git/Herdr checks enforce unique worktree occupancy and exact branch/session authority.
- Supporting / enforcement mechanisms: persistent branch-keyed `ProjectAssignment`, verified Herdr worktree group, assignment locks, peer eligibility and exact-session checks, nonterminal Lead results, `message_staff`, guarded local fast-forward and `needs_update` feedback.
- Closure path: Manager delegates separate branches → each Lead works in its verified checkout → real collision/merge/availability evidence returns in staff/result/tool outcomes → Manager redirects an affected Lead, chooses integration order or pauses/resumes → subsequent S1 work and write placement change.
- Boundary reachability: optional but shipped `/manager` mode registers `delegate_work`, `message_staff`, `resume_work`, `stop_lead` and `integrate_branch`; a new project can create its first linked worktree, so this is not merely a hypothetical configurable API.
- Why this is / is not agent-owned: branch placement, correction and conflict-handling judgment can be chosen by the Manager model; a lock or Git fast-forward alone has only deterministic authority and would not choose the task-level adjustment.
- Distinct S1 units: at least two independently assigned Pi Lead sessions, each operating one branch/worktree and its owned Agent tree in the same verified project.
- Inter-S1 disturbance: overlapping writers could clobber a shared worktree or a later feature branch could be stale after earlier integration; an occupied checkout/duplicate assignment is explicitly rejected and `needs_update` reports stale target state.
- Attenuating coordination relation: Manager-selected separate branch ownership plus first-party exact occupancy/assignment checks, result messaging and corrective Lead direction.
- Feedback into subsequent S1 behaviour: rejected ownership/new target SHA and Lead reports return to Manager, who uses `message_staff`/`resume_work` to assign the responsible Lead an updated base or correction before another accepted merge.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the branch/worktree anti-collision rules regulate a concrete interference among simultaneously active S1 writers, not merely pass messages or sequence arbitrary tasks.
- Evidence: [project orchestration](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/guides/project-orchestration.md), [coordination role/assignment contract](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/concepts/coordination.md), [registered staff tools](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/index.ts), [lead runtime](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/lead-runtime.ts).
- Basis: explicit and structural.
- Confidence: medium-high for supported Manager mode.
- Caveats: an ordinary single Lead has no inter-Lead S2 claim. Preventive worktree isolation is strong structural evidence but not proof of zero logical merge conflicts; the Manager model's decisions are distinct from validation enforcement.

## S3 — Inside-and-now control

- State: A
- Function: current project-wide regulation of assigned Leads' commitments, work lifecycle, intervention and integration by the model-operated Manager.
- Disturbance / variety regulated: stalled or failed branch work, competing current assignments, incomplete required evidence, branch readiness, unavailable workers, and the order in which accepted branch outcomes enter the main worktree.
- Decisive decision or feedback right: the Manager model assesses project status and Lead reports, delegates/redirects, chooses whether to pause/resume a branch, accepts a specific validated source SHA and invokes local integration or requests more work.
- Decision owner: active Manager Pi model for discretionary whole-project commitment/intervention choices; Chief is a separate optional higher-level model supervisor and cannot seize these branch rights.
- Supporting / enforcement mechanisms: `list_staff` direct-report and work ledger, `inspect_staff`/`read_staff_transcript`, event-driven completed-result/failure handoffs, persistent assignment records, `message_staff`, `stop_lead`, `resume_work`, Git fast-forward/cleanup checks, optional human removal approval.
- Closure path: current per-branch execution/status/evidence → Manager whole-project model judgment → instruction to exact Lead, stop/resume, revised delegation, or accepted-SHA integration → later Lead execution and verified project checkout/assignment state change.
- Boundary reachability: normal `/manager` activation from the primary worktree injects a Manager role charter and a live Pi model with registered staff/project tools; no development-only controller or hypothetical future dashboard is needed.
- Why this is / is not agent-owned: the Manager owns priority, commitment and acceptance choices based on whole-project status; deterministic locks/Git/Herdr execute only selected calls. Chief's distinct direct-report scope is not evidence of duplicate authority at this project recursion.
- Whole-system current view: `list_staff` projects exact current assigned/supervised Leads and branch work with `active`/`paused`/`conflict` status; inspect/transcript tools provide bounded additional evidence, while nonterminal reports/failures are automatically delivered to Manager.
- Current-control decision scope: `delegate_work`, corrective `message_staff`, `stop_lead`/`resume_work`, accepted-SHA `integrate_branch` and limited assignment required-evidence control; not merely a token budget, dashboard, process scheduler or close button.
- Evidence: [staff tool contract](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/reference/staff.md), [project guide](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/guides/project-orchestration.md), [Manager charter/registered tools](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/index.ts), [lead runtime](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/lead-runtime.ts).
- Basis: explicit and structural.
- Confidence: medium-high for supported Manager mode and documented returned intervention.
- Caveats: Manager integration is local Git only, never automatic hosted PR merge; its decision may be human-guided. Ordinary human permission to remove a checkout is a narrower destructive-action gate, not independently established project-wide parent S3 mode.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent, first-party complementary operational-claim audit with corrective verdict authority is established at the declared project recursion.
- Disturbance / variety regulated: a Lead or Agent may assert completion after an incomplete implementation, missed tests or unsound branch evidence.
- Decisive decision or feedback right: an individual Lead validates its own technical result; Manager may inspect reports or require evidence and choose acceptance, but a separate evidence-gathering auditor is not an installed mandatory or demonstrably independently owned control path.
- Decision owner: ordinary technical reviewer choices remain with Lead/Manager models and operator; no distinct first-party S3* owner is evidenced.
- Supporting / enforcement mechanisms: per-Agent reports, reusable result references, required evidence, bounded transcript inspection, test/check actions and accepted-source-SHA integration guard.
- Closure path: reports/evidence feed ordinary owner/Manager coordination, without a qualifying independent audit result and corrective-veto return before acceptance.
- Why this is / is not agent-owned: reviewer Agent definitions inside the same Lead herd are explicitly internal; manager inspection and an exact SHA check are not equivalent to independent complementary operational audit.
- Evidence: [coordination review boundary](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/concepts/coordination.md), [handoffs and accepted result contract](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/guides/project-orchestration.md), [staff inspection](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/reference/staff.md).
- Basis: bounded structural absence.
- Confidence: medium; a custom deployment could impose independent review, which is not credited at this standard boundary.
- Caveats: no live provider-run audit was attempted; the negative does not forbid external independent reviewers.

### Absence scope

- Surfaces inspected: directly owned Agent reviews, managed Lead/Manager handoffs, `read_staff_transcript`, retained evidence, accepted-SHA merge and role definitions.
- Plausible first-party paths checked: separate critic/reviewer Agent roles, Manager's independent transcript/branch access, technical validation and local-merge guard.
- Why no material first-party path remains: the shipped review helpers are within implementation ownership or ordinary Manager acceptance; no required or explicit complementary auditor with independent direct-evidence path, separate claim challenge and returned veto/correction control is wired into the project lifecycle.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed external-and-prospective capability-adaptation loop is established.
- Disturbance / variety regulated: changing Pi/Herdr capabilities, project context, new code requirements and agent-definition preferences.
- Decisive decision or feedback right: current user/Manager/Lead can revise task plans or manually configure agent definitions; no system-owned outside/future adaptation authority is evidenced.
- Decision owner: current-task models and operator, not a separate prospective intelligence function.
- Supporting / enforcement mechanisms: agent-definition discovery/overrides, role profiles, context handoffs, future session restarts, peer discovery and project status.
- Closure path: configuration and internal task updates affect present execution, without an environmental forecast/options judgment returned into an S3 capability decision.
- Why this is / is not agent-owned: learning task context, retaining transcripts or revising an active assignment does not itself model relevant future environmental change and adapt system capability.
- Evidence: [agent definitions](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/agent-definitions.ts), [extension configuration](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/config.ts), [recovery guidance](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/guides/recovery.md), [coordination](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/concepts/coordination.md).
- Basis: bounded structural absence.
- Confidence: medium-high for standard distribution.
- Caveats: a user could compose an outside-oriented research Agent using generic task tools, but such external future adaptation is not a shipped system-level S4 path.

### Absence scope

- Surfaces inspected: agent definitions, overrides, role configuration, task context and durable handoffs, peer transport, runtime failure/recovery and project supervision.
- Plausible first-party paths checked: modifying execution profiles, using task Agents for research, restarting model sessions under new definitions and learning from previous failures.
- Why no material first-party path remains: none turns external/future distinctions into adaptation options evaluated against current project capability with returned S3/operational change; the paths regulate immediate work or manually selected configuration.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level dispute/decision loop closed by an in-boundary agent or parent arrangement was established.
- Disturbance / variety regulated: exact-session authority, developer-set agent allowlists, project trust, sensitive checkout removal and branch permissions.
- Decisive decision or feedback right: normal user grants/denies specific destructive action or changes configuration; runtime authenticates roles and applies exact-session ownership, not ultimate identity/ethos deliberation.
- Decision owner: operator for ordinary permission/configuration; implemented session/role contract for enforcement; no first-party ultimate-policy decision maker demonstrated.
- Supporting / enforcement mechanisms: Manager/Chief/Lead role charters, scoped tool allowlists, session identity/lease validation, removal-preapproval UI, project trust and immutable assignment ownership.
- Closure path: permission or configuration inputs gate individual operations and subsequent tool access, without an identity-policy issue referred to legitimate ultimate authority and returned to govern an agent organization.
- Why this is / is not agent-owned: role names and a human approval over worktree deletion are not S5; technical authentication/authorization preserves safety but does not resolve system purpose or ultimate policy.
- Evidence: [role contracts and tool boundaries](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/extension/index.ts), [project removal authority](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/guides/project-orchestration.md), [coordination identity](https://github.com/boadij/pi-herdsman/blob/2b78e1b7b4a62240f7be881ab066be4cefbee612/docs/concepts/coordination.md).
- Basis: bounded structural absence.
- Confidence: medium-high for standard distribution.
- Caveats: a real user or institution may govern the project externally; its ultimate-policy arrangement is not silently inherited by this local Pi extension.

### Absence scope

- Surfaces inspected: role/configuration/permission paths, Manager/Chief startup, exact-session leases and ownership, removal approval, project trust and persistent assignment identity.
- Plausible first-party paths checked: human preapproval for checkout removal, policy overlays/allowlists, supervisor escalation, model-selected project decisions and developer-maintainer governance.
- Why no material first-party path remains: approvals concern particular operational actions and role boundaries; no first-party identity/ultimate-policy matter, legitimate authoritative adjudication and returned policy closure is operationally wired.

## Distributed OSS parent arrangement

Herdsman operates local Pi/Herdr sessions whose private transcripts and process identities are not shared by arbitrary repository contributors. Its exact local Manager/Chief authority is operational and technical; maintainer release/contribution governance is outside the standard product boundary. Do not infer organization-wide parent S3/S4/S5 from multiple contributors or a user controlling locally installed agents.

## Self-hosted and non-human modes

Local self-hosted project Manager mode establishes model-owned current control when a Pi provider and valid Herdr runtime are available; Chief is an optional broader model supervisor. Operator toggles and approvals restrict operations but do not independently establish a closed alternate parent-owned S3/S4/S5 mode. A no-Chief/single-Lead installation still has its task S1 without cross-Lead S2 or project S3.

## Recursion

The Manager → assigned Lead → Agent and optional Chief hierarchy contains nested decision actors, but nesting alone does not certify each as a viable system. The assessment's positive S2/S3 claims are limited to the concrete Manager/project recursion with independently owned Lead objectives and a shared worktree/integration environment. An individual Lead/Agent owns bounded task decisions; no complete lower-level metasystem is inferred from process spawn.

## Variety and escalation

Task requests, model/tool outcomes and required evidence move between exact owners without routine polling. Branch-keyed assignments and peer eligibility attenuate overlapping-writer variety; Manager receives failed or completed Lead reports, can request correction, and may escalate above through verified direct-supervisor messages. Cancellation, failed model runs and worktree retirement remain distinct nonterminal facts, rather than falsely proving acceptance. Chief and Manager supervisory routing is an ordinary ownership channel, not by itself an algedonic signal or separate S-function.

## Evidence gaps

Assessment is based on pinned primary source, installed runtime contracts and declared supported modes. Native focused tests were attempted separately; provider-backed Pi/Herdr execution, real multi-host federation, OS-level worktree races and live user supervision were not exercised, so actual effectiveness and autonomy frequency are not measured. Custom agent definitions or external independent audit deployments can change the assembled system boundary and are not credited. All six states describe ownership capability at the reviewed source cut, not an organizational autonomy grade.
