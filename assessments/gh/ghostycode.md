---
harness_id: ghostycode
project_name: GhostyCode
repository: https://github.com/blissito/ghostycode
review_ref: c025ba29f3a55734ac05ff16ba677765a2845cfb
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# GhostyCode

## Review boundary

- System in focus: public Ghosty Rust coding-agent runtime with real TUI/CLI model/tool loop, bounded independent subagents, JavaScript workflows, scope/write coordination, review/check tools and session controls.
- Purpose and identity: code modification and testing in user project repositories, with optional distributed multi-worker coding tasks.
- Relevant environment: user Git working files, shell/test results, separate child model/tool sessions, task budgets, permissions, providers and source modifications.
- Standard-distribution boundary: executable first-party Ghosty CLI/TUI/runtime, not external providers/MCP services, development CI, pure IR fixtures or surrounding Open Source maintainer organization.
- Credited operating / distribution surfaces: crates/cli, crates/tui owned model/tool/agent paths, subagent worktree and coordination ledger, first-party workflow executor, live tool gates and native config/memory.
- Adjacent first-party surfaces excluded from ownership: tests, sample Fleet scripts without runtime entry, pure unwired review-repair IR, developer release workflows, web landing demos, third-party agents and inference providers.
- First-party operating / deployment modes considered: user coding agent in terminal; native model-directed subagent and workflow tools; concurrent source-writing child tasks with default worktree protection; optional configured code reviewer/verifier/gates; session memory and operator approval modes.
- Recursion level: coding project under parent agent and real independently operating child model/tool work cells when workflow launches them, not arbitrary tool calls as peers.
- Reviewed revision: c025ba29f3a55734ac05ff16ba677765a2845cfb.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Ghosty packages a native Rust terminal coding agent: model-based file, search and shell tool choices execute against real project state, with tool outputs returned to later model actions. It also ships a first-party subagent manager and model-directed Workflow task/parallel facility whose children retain their own contexts and execution budgets.

Workflow parallel write-capable leaves default to separate Git worktrees, and the native coordination ledger records owner-scoped paths/files/contracts and rejects overlapping active writers in the same working tree. These mechanisms are reachable in the packaged Workflow and subagent execution path and specifically prevent source-edit interference, not merely add labels to a scheduler.

The same codebase contains diff review with a separate model prompt, independent command verifier ensembles and a configurable role-to-role gate/handoff system. Their isolated component capability is real, but a standard complete independently source-inspecting audit verdict that automatically causes another coding attempt was not sufficiently reconstructed, so S3* remains uncertain. Workflow status and budget controls also do not by themselves prove a distinct discretionary whole-current S3 regulator. Memory curates stable preferences, and constitutional/permission guards constrain execution without establishing strategic renewal or ultimate identity governance.

Primary evidence: [crates/tui/src/tools/workflow/mod.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/workflow/mod.rs); [crates/tui/src/tools/subagent/coord/ledger.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/subagent/coord/ledger.rs); [crates/tui/src/tools/subagent/worktree.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/subagent/worktree.rs); [crates/tui/src/tools/review.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/review.rs); [crates/workflow/src/gates.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/workflow/src/gates.rs).

## Operational model

A real model/tool loop delivers coding S1. Model-defined or operator-composed multi-worker tasks may be protected against actual conflicting source writes by first-party scope claims or worktrees, supporting a narrow C-level coordination function. The same compiler and runtime enforce child budgets and return receipts, which do not automatically upgrade S3/S3*, S4 or S5.

## S1 — Operations

- State: A
- Function: The agent autonomously edits and tests source using real file, shell and search actions.
- Disturbance / variety regulated: Changing project code, unexpected tool failures, user requirements and test observations.
- Decisive decision or feedback right: Model selects the next coding tool/action given actual tool results.
- Decision owner: First-party Ghosty session agent and bounded model-driven coding subagents.
- Supporting / enforcement mechanisms: Native Rust tool handlers, model adapters, persisted session, action policy and tool approval.
- Closure path: User code request → model-selected source tool → native workspace change/observation → tool result returned to model → subsequent action or finish.
- Boundary reachability: Shipped Rust CLI/TUI registers source/shell tools and executes model-driven coding turns using its own session state.
- Why this is / is not agent-owned: Model controls operational choices; Rust runtime executes and limits them.
- Evidence: [crates/tui/src/tools/registry.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/registry.rs); [crates/tui/src/tools/file.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/file.rs); [crates/tui/src/tools/shell.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/shell.rs); [crates/cli/src/main.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/cli/src/main.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: External inference endpoint supports but does not own the Ghosty coding runtime..


## S2 — Coordination

- State: C
- Function: Prevent concrete overlapping source-write interference among independently operating coding workers.
- Disturbance / variety regulated: Parallel source-writing subagents can overwrite or invalidate changes under shared file roots.
- Decisive decision or feedback right: Model/operator creates task/file scopes or workflow composition; native coordinator enforces non-overlap and separate worktree choices.
- Decision owner: User/model-authored task/workflow scope with deterministic first-party coordination ledger and worktree enforcement.
- Supporting / enforcement mechanisms: Write claims per owner/roots/files/contracts; typed conflict receipts; automatic worktree isolation for parallel write-capable leaves; child cwd switching.
- Closure path: Distinct worker write claims → overlap check blocks conflicting shared writers or assigns independent checkout → child operations occur in permitted workspace → conflict or child result returns to parent to narrow, serialize or integrate next operations.
- Boundary reachability: First-party workflow and subagent tools use the write-claim and isolated worktree paths in the packaged TUI executable.
- Why this is / is not agent-owned: This directly attenuates actual cross-worker file-write collision, not generic fanout. Setup/composition rather than a separately autonomous regulator supports C.
- Evidence: [crates/tui/src/tools/workflow/mod.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/workflow/mod.rs); [crates/tui/src/tools/subagent/coord/ledger.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/subagent/coord/ledger.rs); [crates/tui/src/tools/subagent/worktree.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/subagent/worktree.rs); [crates/workflow/src/lib.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/workflow/src/lib.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Explicit shared-worktree overrides exist. Worktree isolation does not resolve semantic merge conflicts..

- Distinct S1 units: Independent model/tool coding subagents launched into live parent Workflow tasks.
- Inter-S1 disturbance: Two concurrent workers writing overlapping files/contracts risk clobbering one another.
- Attenuating coordination relation: Scoped write-claim ledger blocks live overlapping nonisolated owners; parallel write leaves default to separately provisioned worktrees.
- Feedback into subsequent S1 behaviour: Rejected claims block an unsafe new writer and report the specific collision; isolated children instead execute in distinct working trees and return results to parent for deliberate integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The runtime has a concrete multi-writer code-collision detector and protective worktree execution rather than only message routing or fanout.


## S3 — Inside-and-now control

- State: ?
- Function: Multi-worker run statuses, budgets and actions are present but a distinct discretionary whole-current regulator remains unresolved.
- Disturbance / variety regulated: Task failures, spent budgets, stale workers and competing current commitments.
- Decisive decision or feedback right: Workflow bounds and cancellation enforce static ceilings; separately owned resource-priority reconsideration across live S1 units is not established.
- Decision owner: Potential parent model/operator, supported by deterministic workflow driver; S3 decision ownership indeterminate.
- Supporting / enforcement mechanisms: Child task records, semaphore concurrency, budget snapshots, cancellation and operator fleet dashboard.
- Closure path: Child completions and budget/status reports return to the workflow owner; static stop/retry does not prove adaptive current allocation of multiple S1 commitments.
- Why this is / is not agent-owned: A status panel, scheduler and budget cap are not themselves a whole-current decision owner.
- Evidence: [crates/tui/src/tools/workflow/mod.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/workflow/mod.rs); [crates/tui/src/tools/subagent/coord.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/subagent/coord.rs); [crates/lane/src/control.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/lane/src/control.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Requires a separate fully wired mode tracing whole-current discretionary intervention..


## S3* — Complementary audit

- State: ?
- Function: Structured source-diff review, verifier tools and optional role/gate paths could support complementary audit, but a complete independent correction loop is not proved for the ordinary runtime.
- Disturbance / variety regulated: Coding changes can be incomplete, defective or misreported as completed.
- Decisive decision or feedback right: Reviewer model can inspect a diff and return findings; deterministic gates can block or retry configured roles, but the distinct audit judgment plus corrective return is not compulsory or sufficiently traced.
- Decision owner: Candidate separate reviewer/verifier role, with human/operator-selected gates and deterministic execution.
- Supporting / enforcement mechanisms: Review JSON prompts, diff fingerprints, parallel test verifiers, review-repair IR, explicit role handoffs and gate verdicts.
- Closure path: Source diff/test evidence → reviewer/verifier finding or gate status → may block or retry configured workflow role; whether an independent auditor directs a real corrective coder is unresolved.
- Why this is / is not agent-owned: A reviewer label, secondary model call or pure review-repair IR is insufficient without an actual audit-to-operation return path.
- Evidence: [crates/tui/src/tools/review.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/review.rs); [crates/tui/src/tools/verifier.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/verifier.rs); [crates/workflow/src/gates.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/workflow/src/gates.rs); [crates/workflow/src/review_repair.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/workflow/src/review_repair.rs); [crates/tui/src/tools/workflow/mod.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/workflow/mod.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Role-based workflows may have stronger modes; further targeted review is needed to credit autonomy..


## S4 — Outside-and-then intelligence

- State: —
- Function: No complete model-owned prospective external sensing and capability adaptation loop established.
- Disturbance / variety regulated: Future environmental changes and capability demands would require anticipatory organizational adaptation.
- Decisive decision or feedback right: Remember tool updates prior user facts, and Fleet setup can propose routes but cannot save or launch without human act.
- Decision owner: No independent S4 decision owner; model note curator and human setup wizard provide context support.
- Supporting / enforcement mechanisms: Durable note store, recall, model catalog and setup-time Fleet suggestion schema.
- Closure path: Observed preferences persist into later prompts, or a suggested Fleet awaits manual save; no prospective environment analysis and binding capability-renewal return.
- Why this is / is not agent-owned: Persistent memory and provider-role suggestions do not alone constitute future strategic adaptation.
- Evidence: [crates/tui/src/tools/remember.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/remember.rs); [crates/tui/src/tools/native_memory.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/tui/src/tools/native_memory.rs); [crates/workflow/src/fleet_composition.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/workflow/src/fleet_composition.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Optional custom workflows cannot be inherited without their actual prospective adaptation authority..

### Absence scope

- Surfaces inspected: User-memory tool, native recall, model/config changes, setup Fleet proposal and runtime coding modes.
- Plausible first-party paths checked: Model-chosen memory note updates, manual Fleet suggestions, provider switches and persistent task context.
- Why no material first-party path remains: No first-party shipped outside-and-then environmental sensing/options/decision loop changes the coding organization capabilities autonomously.


## S5 — Policy and identity

- State: —
- Function: No ultimate identity/purpose-level policy adjudication with authoritative binding return.
- Disturbance / variety regulated: Tool safety approval, local constitutional rules, model permissions and budgets are action-level governance constraints.
- Decisive decision or feedback right: Human approves risky tool calls or ratifies workflow posture, but no ultimate-policy question is decided and returned to all operations.
- Decision owner: Human/operator configures individual restrictions; deterministic guards enforce them.
- Supporting / enforcement mechanisms: Modes and approval postures, constitution prompt/config, workflow elevation gate and tool safety rules.
- Closure path: Permission allows/refuses a tool action or setup decision; no ultimate purpose/identity adjudication governs subsequent organization-wide activity.
- Why this is / is not agent-owned: Constitutional branding, static rules and human approvals alone do not establish S5.
- Evidence: [crates/config/src/user_constitution.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/config/src/user_constitution.rs); [crates/execpolicy/src/approval_mode.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/execpolicy/src/approval_mode.rs); [crates/workflow/src/elevation.rs](https://github.com/blissito/ghostycode/blob/c025ba29f3a55734ac05ff16ba677765a2845cfb/crates/workflow/src/elevation.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Parent developer governance of the public repository is outside an installed coding session..

### Absence scope

- Surfaces inspected: Constitution config, permission postures, workflow elevation, tool guards and runtime settings.
- Plausible first-party paths checked: User plan approval, safe shell, model choice, route ratification and constitutional instructions.
- Why no material first-party path remains: No first-party legitimate identity/policy decision actor and binding governing return to all subsequent coding-operation rules is demonstrated.


## Distributed OSS parent arrangement

GitHub maintainer workflows, release CI, upstream examples and third-party provider or model services are separate systems and cannot donate VSM closure to the installed coding runtime. The user can ratify an elevated workflow but per-task approval is not an ultimate-policy parent mode.

## Self-hosted and non-human modes

Local/external models are interchangeable inference dependencies; native tool execution and Workflow child admission remain first-party. Configured scope claims and worktrees enforce task boundaries while the parent actor chooses and combines them.

## Recursion

Parent and independent child coders each have bounded decisions over their own code operation. Coordinating physical file claims and checkout separation is an actual inter-S1 relation. Model plurality, a status panel or optional reviewer labels do not alone establish all higher VSM functions.

## Variety and escalation

Tool/test results return to the model; conflicting write claims can block a child and force narrowed claims or worktree isolation. Workflow gates and ceilings can stop or require ratification; these constraints are reported as evidence, not automatically proof of an autonomous S3/S3* or S5 authority.

## Evidence gaps

- Positive S2 is limited to write-capable independent coding children under native conflict claims or isolated worktree modes; no semantic merge arbitration is claimed.
- Whole-current S3 is uncertain because scheduling and status do not prove an independent aggregate prioritization decision.
- Complementary S3* is uncertain because a separate review/check module and optional roles must be traced into an independently owned audit-and-corrective path before positive credit.
- S4 and S5 conclusions are standard-distribution and selected-recursion scoped; no empirical benchmark capability result is asserted.
