---
harness_id: clouds-coder
project_name: Clouds Coder
repository: https://github.com/FonaTech/Clouds-Coder
review_ref: 83a0d25aa59ef1bc8e295ec45104a9c7f0819c83
reviewed_at: 2026-11-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# Clouds Coder

## Review boundary

- System in focus: the first-party Clouds Coder local-first coding-agent server and its supported in-session Sync multi-agent, governed LAN Collaboration and optional Liquid Kernel evolution modes, **at the frozen repository revision**. The system serves user coding tasks and, when enabled, coordinates project work by multiple private agent sessions.
- Purpose and identity: solve requested coding/IDE work through an observable model/tool execution loop, coordinate distinct agents sharing one project, and adapt versioned runtime policy for later sessions under operator-configured evolution rules.
- Relevant environment: user tasks, source and file changes, model/tool failures, concurrently edited project files, device/member permissions, long-running sessions, changing failure/retry rates and future coding workloads.
- Standard-distribution boundary: the runnable `Clouds_Coder.py` monolith and its in-tree `Code_Structure/` source extraction (64 substantive modules, not extra agents), CLI/server/IDE endpoints, project collaboration listener, active session state, and opt-in Liquid Kernel. The agent's model-provider inference remains an external computational dependency, not an independent donated VSM function.
- Credited modes: ordinary single-agent tool execution; Sync multi-agent model-driven Manager/Explorer/Developer/Reviewer with role-isolated contexts; separately governed LAN project Collaboration (enabled unless disabled at launch), with multiple members and private Agent sessions; opt-in `Tuning` and `Thinking`/`Aggressive` evolution. The Liquid Kernel default is `Off`; no evolution is claimed for an unconfigured default installation.
- Credited operating / distribution surfaces: runnable Python server `Clouds_Coder.py`, `Code_Structure/session/state.py`, `Code_Structure/agent/tools.py`, `Code_Structure/collaboration/core.py`, `Code_Structure/app/{main,context}.py`, `Code_Structure/liquid_kernel/control.py`, and the shipped Web/IDE/Collaboration session entry points.
- Adjacent surfaces excluded: contributor commits, tests, self-hosting/build/release workflows, benchmark results, documentation-only architecture, third-party model services, a human's external institutional governance, and independent projects merely using the exported APIs. The bundled regression tests corroborate reachability but are not live runtime S3* themselves.
- Adjacent first-party surfaces excluded from ownership: test fixtures and synthetic model callbacks, changelog prose, distributable packaging, developer-only benchmarks, installation scripts, public UI mockups, and repository contribution/release activity.
- Recursion level: the delivered local server/agent organization, including distinct operating coding sessions in project mode. Inside one complex Sync session the Manager and role-specific workers form a subordinate orchestration layer; no external multi-company organization is imputed.
- Reviewed source: `FonaTech/Clouds-Coder@83a0d25aa59ef1bc8e295ec45104a9c7f0819c83` (stable repository ID `1173658919`); Profile `0.2.4`, Methodology `0.3.7`; reviewed 2026-11-07.

## Repository architecture

The Web/IDE/CLI surfaces call the real session runtime: a configured model selects task-specific reads, code changes, shell actions and response steps while first-party code mediates tool effects, persists context and applies recovery/permission constraints. In Sync mode an LLM-backed Manager receives a live blackboard: objective, plan cursor, role outputs, failed attempts, progress, permissions and time/round constraints. Its `route_to_next_agent` decisions select Explorer, Developer or Reviewer and feed evidence and failed checks into subsequent assignment. The worker roles have separately maintained model contexts, tools and artifact feedback.

Project Collaboration is a different, independently reachable LAN service. Separate members' **private** agent sessions use a shared revisioned workspace and public task blackboard. A coordinator can produce shared plan slices and participant assignments; the service transforms concurrent text operations, rejects stale direct writes, freezes actual conflicts and requires explicit review/resolution by authorized people. Sharing a mailbox or an Agent label alone is not the S2 witness: the write collisions and their returned revision/freeze decisions are.

The Liquid Kernel is a first-party optional future-capability plane: historical user-session task/error evidence, failure rates, incumbent kernel source and generated challenge cases inform a model-proposed policy/tool patch. An independent configured model judges candidate behaviour against incumbent and hard checks. `Tuning` can stage a qualifying candidate automatically in a 5%→25%→100% measured canary with regression rollback/promotion; `Thinking`/`Aggressive` stage a candidate for an administrator's explicit acceptance before the same live canary. This is **opt-in** and depends on configured generator and judge models, not a default always-running self-rewrite claim.

Frozen first-party sources:

- [Product boundary, explicit two collaboration layers and evolution modes](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/README.md)
- [Actual in-session Manager, worker roles, review, blackboard and Sync dispatch](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/session/state.py)
- [Revisioned project edits, conflicts, reviewer separation and returned resolutions](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/collaboration/core.py)
- [Liquid Kernel proposal, benchmark, human/automatic approval and canary](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/liquid_kernel/control.py)
- [Experience from actual session histories and first-party model callbacks](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/app/context.py)
- [Server startup wiring and LAN listener](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/app/main.py)
- [Liquid Kernel control-plane regressions](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/tests/test_liquid_kernel.py) and [concurrent collaboration regressions](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/tests/test_collaboration.py)

## Operational model

The operator supplies tasks, models, collaboration membership and evolution mode. The operating model(s) perform source investigation and code work. In complex Sync sessions the Manager model decides which specialized working role should presently carry the goal and can adjust on evidence, while hard application guards enforce limits. Across project member sessions, first-party revision and conflict machinery prevents destructive interleaving but does not itself autonomously decide the legitimacy of a disputed overwrite. The separate read-capable Reviewer model challenges the Developer's reported result against code and tests. Optional future-kernel proposals are judged and can be deployed by the enabled mode's owner; ordinary coding tasks do not automatically transfer policy authority.

## S1 — Operations

- State: A
- Function: enact user coding, file investigation and project implementation through model-selected local tools and iterative feedback.
- Disturbance / variety regulated: changing task requirements, unknown source, test/build errors, context limits, interrupted work and conflicting workspace state.
- Decisive decision or feedback right: operating Developer/single-agent model selects source reads, edits, commands and successive repairs; Explorer performs bounded research. The user fixes the task and permissions, not each substantive model action.
- Decision owner: task-operating LLM agent and its role-specific supported model contexts; deterministic code owns tool transport, resource fences and permissions.
- Supporting / enforcement mechanisms: session state, tool registry/dispatch, todo and blackboard evidence, worktree coordination, model context, file/shell execution and failure recovery.
- Closure path: user request → model-selected action → constrained first-party effect → observed source/command result → next operating decision or reported outcome.
- Boundary reachability: server and UI session entry points instantiate the live session runtime; role-specific tool calls are executed in the Sync worker loop, with the same goal's observations persisted between turns.
- Why this is / is not agent-owned: deleting model discretion leaves generic tool endpoints but no task-specific decision about which code to inspect/change or how to repair a failure.
- Evidence: [session runtime](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/session/state.py), [tool implementations](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/agent/tools.py), [runtime entry](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Clouds_Coder.py).
- Basis: explicit + structural.
- Confidence: high for ownership path; not an empirical completion-rate claim.
- Caveats: no externally hosted live provider/model coding benchmark was run for this review.

## S2 — Coordination

- State: C
- Function: attenuate actual shared-file interference between distinct first-party operating agent sessions and return revision/conflict outcomes before subsequent writes.
- Disturbance / variety regulated: stale concurrent text changes, same-path non-OT overwrites, conflicting integration candidates, overlapping work intents and a contributor working on a now-frozen document.
- Distinct S1 units: separate members' own private Agent sessions in the LAN project workspace, each carrying its own task and file edits; the in-session Explorer/Developer/Reviewer role sequence is **not** used as the sole proof of distinct S1.
- Inter-S1 disturbance: two agents can edit a shared document from different revisions, overwrite the same binary/non-OT file, or issue competing candidate changes against a protected shared path.
- Attenuating coordination relation: `submit_operation` transforms revision-aware text edits against intervening operations; `write_file` enforces `expected_revision` and creates a frozen conflict on a stale divergent write; task intents/participant slices surface collisions.
- Feedback into subsequent S1 behaviour: applied revisions and operations are published to participating sessions; stale-writer conflict returns HTTP 409 and a frozen document, preventing the next competing edit until conflict review and a binding accepted/discarded candidate resolution update the shared file and invalidate old leases.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: interference is a concrete version/overwrite collision among independent operating sessions; OT transform, revision rejection, freeze and resolved revision directly change their next permitted file actions.
- Decisive decision or feedback right: first-party deterministic OT/revision guards decide transform/reject/freeze; **authorized humans**, not an autonomous Agent, decide substantive disputed merge/discard after separate primary and secondary human reviews and owner confirmations.
- Decision owner: first-party constructor-owned coordination enforcement with human-owned discretionary conflict settlement. The project coordinator Agent may choose plan slices but does not independently ratify a contested merge.
- Supporting / enforcement mechanisms: CollaborationStore SQLite transactions, document locks/version log, shared events, `CollaborationWriteCoordinator`, task/intent registrations, device identity and conflict status.
- Closure path: concurrent writes → deterministic transform or conflict/freeze → published revision or refusal → agents rebase/stop; disputed case → two human reviews and authorized resolution → unfreeze/new revision → resumed S1 work.
- Boundary reachability: shipped `app/main.py` starts the `P+7` collaboration service by default when permitted, and first-party project/Agent bridge routes real workspace writes into `collaboration/core.py`; tests exercise concurrent and conflict paths.
- Why this is / is not agent-owned: a model chooses its task and proposed edits, but would not autonomously decide a human-protected conflicting overwrite; the S2 anti-interference feedback exists in code without model discretion, so `C` rather than `A`.
- Evidence: [project collision/transform/merge implementation](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/collaboration/core.py), [wiring](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/app/main.py), [explicit two-layer boundary](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/README.md).
- Basis: explicit + structural.
- Confidence: high for C closure, not A.
- Caveats: the reviewer separation for project conflicts is human/member-based, distinct from the in-session model Reviewer and not an automatic S3* claim.

## S3 — Inside-and-now control

- State: A
- Function: govern current complex-session operating commitments, plan-step priorities and exception interventions across delegated worker roles, rather than merely forward a prompt.
- Disturbance / variety regulated: stalled or repeated delegations, competing phase priorities, failed prior repairs, current plan-step dependencies, misallocated read/write work, out-of-budget cycles and unverified completion.
- Whole-system current view: `_manager_system_prompt` assembles the active original objective, current canonical subtask and owner, plan-step cursor, progress, role evidence, failure ledger, last attempts, permissions and available resource/round budget from the shared blackboard; Manager re-reads it after worker feedback.
- Current-control decision scope: the Manager model chooses/changes work role, operative focus, mandatory timeslice and next plan-step commitment via `route_to_next_agent`; it can intervene on failed attempts by changing assignments, request verification, keep a plan step active or advance only after evidence gates. Static watchdog and phase limits are **enforcers**, not the Manager's source of autonomy.
- Decisive decision or feedback right: select among active Explorer/Developer/Reviewer operating commitments and alter the current execution order on evidence; the model normally owns that judgment in Sync mode.
- Decision owner: first-party Manager LLM context, separate from subordinate worker contexts; code owns actual call dispatch, plan-step evidence gates, watchdog recovery and permissions.
- Supporting / enforcement mechanisms: per-role context isolation, common blackboard, `route_to_next_agent` schema, current task profile, planning/todo gate, failure-aware ledger and Sync worker dispatch.
- Closure path: whole current board/error view → model Manager intervention/assignment → constrained worker execution → new feedback/result/plan state → next Manager control choice.
- Boundary reachability: the supported complex-task Sync worker enters `_manager_delegate_turn` and `_multi_agent_sync_blackboard_worker`; simple single-agent runs do not receive the positive S3 mapping by mere label.
- Why this is / is not agent-owned: the Manager is instructed and invoked to make evidence-sensitive resource/commitment decisions rather than merely compute a fixed `status → role` mapping; deterministic watchdog can override pathological paths but is not the ordinary decisive allocation owner.
- Evidence: [Manager view/dispatch/plan gates](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/session/state.py), [current-control design](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/README.md).
- Basis: explicit + structural.
- Confidence: medium; this is **session-local whole-current** control, not top-level cross-project institutional resource governance.
- Caveats: a task worker/role is not automatically a separate viable business unit; credit is limited to the supported specialized current operating commitments in Sync mode. If narrowly interpreting all role outputs as one indivisible S1, the S3 distinction becomes less certain.

## S3* — Complementary audit

- State: A
- Function: challenge a producing coding worker's outcome and completion evidence through a role-separated reviewer with its own direct file/command access and corrective feedback.
- Disturbance / variety regulated: untested fixes, fabricated completion, misdiagnosed errors, stale file claims, test failures and premature advancement through a plan.
- Claim being audited: Developer/operating worker reports that code is fixed, deliverables exist, checks passed and the current step is ready to close.
- Ordinary reporting path: Developer's code artifacts, execution logs, todo updates and shared blackboard status are its own production report.
- Complementary access path: separate Reviewer role context is specifically directed to `read_file` the exact source line/traceback and use `bash` to independently check observable code/test evidence; it can refuse success, issue a structured `fix_request` and write `review_feedback` distinct from producer reporting.
- Independence boundary: role-isolated model context, read/verify-only tools by default, and direct reinspection of raw source/command results; **not** an external organization/model-provider guarantee. A transient debug mode may temporarily grant Reviewer writes and is **excluded** from this narrow independent-audit witness.
- Who acts on findings: Manager reads review feedback/failure evidence, can reassign a Developer with exact corrections, keep a step open or route another verification cycle; the worker then repairs and the Reviewer may re-check.
- Decisive decision or feedback right: Reviewer model can form a substantive pass/fix judgment from fresh observations and send it into subsequent control; first-party gate code can enforce step validation but does not substitute for this audit judgment.
- Decision owner: independent in-session Reviewer agent model in supported non-debug Sync mode; constructor sets role permissions and feedback channel.
- Supporting / enforcement mechanisms: read-only reviewer tools, isolated role contexts, `review_feedback` blackboard, `ask_colleague` fix request, evidence-aware step gates and Manager routing.
- Closure path: producer claims → reviewer raw-source/test reinspection → recorded pass/fix → manager/worker action or evidence-bound completion.
- Boundary reachability: `_agent_role_system_prompt('reviewer')` and Manager delegation wire the role to runnable read/verify tools; feedback is appended during worker steps and consumed by later Manager/plan decisions.
- Why this is / is not agent-owned: model judgment selects what files or failure evidence to inspect and what correction to demand; merely replaying a fixed test suite would not explain the model's source-specific diagnostic decisions.
- Evidence: [reviewer prompt, role permissions and feedback handling](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/session/state.py), [role separation](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/README.md).
- Basis: explicit + structural.
- Confidence: medium-high for a bounded independent source-checking path; no claim of mathematically verified code quality or independent external audit.
- Caveats: same underlying server/provider may serve roles; default review is not a separate organization and may be bypassed in simpler single-agent mode. Human conflict reviewers are not the basis of this state.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: assess changing patterns of actual user-task demands/failures and develop/test versioned tool and prompt-kernel adaptations for **future** agent sessions, then return accepted options into currently deployed capability.
- Disturbance / variety regulated: future user workloads with failure/retry patterns not fully covered by the present prompt policy, model/tool mismatch, and regressions introduced by experimental kernel changes.
- External distinction: historic real user requests/agent-session outcomes in `codes_root/.../sessions`, tool failures/retries, task constraints and runtime error rates, recorded per incumbent kernel version by `_liquid_kernel_experience`; these represent encountered operational environment, not just the current prompt's plan.
- Future / prospective distinction: candidate kernel patches and newly generated benchmark task/failure scenarios are evaluated against an incumbent **before** deploying revised future-session policy; scheduled and metrics-triggered runs address emerging workload/reliability patterns rather than finish the currently active coding task.
- Adaptation option generated: independent model generator can elect `no_change` or propose limited edits to versioned policy/tool kernel files and prospective challenge cases; hard determinism and a separately configured model judge compare candidate with incumbent, producing a measured change option.
- Path back into current capability / S3: qualifying changes enter signed registry and controlled canary cohort for later session starts, with 5/25/100% comparison and automatic rollback/promotion. New pinned sessions then use the promoted policy/tool hooks; current-session pins are preserved to avoid uncontrolled mid-task mutation.
- Decisive decision or feedback right: **autonomous Tuning mode** lets configured generator/judge and deterministic promotion criteria select and stage qualifying future-capability options, then canary observations decide rollout/reversal. **Parent-controlled Thinking/Aggressive modes** require a human administrator to `approve` or `reject` the candidate before the same canary changes capability.
- Decision owner: candidate option generated by LLM, separately model-judged; in Tuning, constructor's evaluation thresholds and canary decide release without per-candidate human approval (`A` supported). In Thinking/Aggressive, the named authorized administrator owns candidate deployment ratification and returns it via `approve`/`reject` (`P` separately evidenced). Model errors or missing configuration fail the run.
- Supporting / enforcement mechanisms: mode presets, configured model-resolution, session-history collector, immutable validator/evaluator, hard and soft benchmarks, SQLite version registry, signed policy bundles, canary observations and rollback.
- Closure path: real task/error history → model future-option proposals → benchmark/judge decision → autonomous Tuning canary **or** parent approval before canary → observed later sessions → promoted/rolled-back kernel capability.
- Boundary reachability: `app/context.py` injects real experience/model/judge callbacks into `LiquidKernelControlPlane`; `app/main.py` enables startup choice, schedules and session routing. Default mode is explicitly `Off`; `Tuning` is the standard supported autonomous opt-in mode, `Thinking`/`Aggressive` are standard parent-approval modes.
- Why this is / is not agent-owned: future candidate patch and benchmark options require a configured model's choice, not a hard-coded patch; the parent-mode decision is a real administrator candidate-ratification gate, not generic approval of a shell command. Canary thresholds alone do not create model-owned S4, but close the chosen model's adaptation path.
- Evidence: [real history/model callbacks](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/app/context.py), [evolution/canary/approval](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/liquid_kernel/control.py), [server configuration](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/app/main.py), [regressions](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/tests/test_liquid_kernel.py).
- Basis: explicit + structural.
- Confidence: medium; strongest evidence is the controlled *prospective* option/return pipeline, not a claim of live performance improvement.
- Caveats: enabled evolution needs external configured inference providers and sufficient session history; neither continuous execution nor promotion in an actual deployment was observed. Current user workload is a bounded environmental proxy, not independently forecast regulatory/market intelligence. `A(P)` denotes **separate supported decision modes**, not simultaneous parent and autonomous approval.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Configured evolution generator/judge models plus automatic Tuning selection and rollout gates | Tuning schedule or elevated recorded error/retry rates | Future kernel patch option → judged candidate → auto-staged 5/25/100 canary → promoted/rolled back deployment influencing later sessions | `Code_Structure/liquid_kernel/control.py`, `Code_Structure/app/context.py` |
| Parent (`P`) | Authorized human administrator over a generated candidate | Thinking/Aggressive candidate has passed evaluation and awaits human ratification | Explicit `approve`/`reject` → approved canary or rejected candidate → later sessions use promoted policy or retain incumbent | `Code_Structure/liquid_kernel/control.py`, `Code_Structure/app/main.py` |

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-mission deliberation, legitimate binding ratification and returned policy resolution at the declared server-recursion boundary was found.
- Disturbance / variety regulated: access-control, model permissions, collaborative conflicts and kernel-change approvals are operational S2/S3/S4 issues, not by themselves organizational identity crises.
- Decisive decision or feedback right: no authority or execution path can reopen the purpose/identity charter and resolve contested S3-vs-S4 ultimate policy for this agent organization.
- Decision owner: human project owner/admin chooses configuration, member admission, disputed edits and adaptation rollout, but no demonstrated S5-specific remit or identity decision path.
- Supporting / enforcement mechanisms: admin roles/device approvals, immutable kernel safety controls, model/tool permissions, project conflicts and operator config.
- Closure path: ordinary admin approves a member, resolves a file conflict or accepts a future patch; no identity-level question → legitimate charter decision → binding returned future operating policy was established.
- Why this is / is not agent-owned: an authentication/authorization role and the word `policy` in Liquid Kernel name are not evidence of the organizational legitimacy or ultimate-policy function.
- Evidence: [admin/controller wiring](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/app/context.py), [collaboration approval/merge](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/collaboration/core.py), [evolution approval](https://github.com/FonaTech/Clouds-Coder/blob/83a0d25aa59ef1bc8e295ec45104a9c7f0819c83/Code_Structure/liquid_kernel/control.py).
- Basis: structural absence review.
- Confidence: medium.
- Caveats: a real team can supply ultimate policy **outside** the product boundary; that external governance is not borrowed merely from a generic admin console.

### Absence scope

- Surfaces inspected: server startup/admin roles, project member admission and shared conflict settlement, Liquid Kernel modes/manual approval, role prompts, session blackboard and published distribution documentation.
- Plausible first-party paths checked: purpose/identity-level conflict escalation, legitimate charter or ultimate-policy ratification, durable returned control over both present operations and future capability strategy.
- Why no material first-party path remains: every verified authority path closes a scoped code/task/file/access/evolution decision under already-given product purpose, without a visible separate identity-policy contest/ratification loop.

## Recursion

The ordinary single session is one operating goal. In the supported complex Sync mode, Manager regulates distinct role-specific operational work commitments; its view and decisions are scoped to that live session, not an external portfolio of independently chartered companies. Separately, LAN Collaboration connects private coding-agent sessions as distinct peer S1 units; document collisions provide the concrete S2 disturbance. The read-only in-session Reviewer is a complementary audit role, not another top-level manager. Liquid Kernel evolution governs *future capability of the served sessions* and stages it through controlled runtime rollout. Different recursion levels and operating modes are named instead of silently accumulating unrelated product features into one higher VSM tier.

## Variety and escalation

Local model-selected tools absorb code variety. Plan/blackboard-based Manager intervention changes current worker allocations after concrete error or verification feedback. Versioned project operations dampen distinct agents' concurrent-write instability; irreconcilable conflict escalates to protected human settlement rather than being force-merged by an agent. Reviewer may directly challenge the producer's claims with raw source and command evidence. Optional Liquid Kernel studies actual past task outcomes to prepare safer/fitter future kernel versions, with benchmark and canary return; a human approval route exists in more exploratory modes. None of these ordinary scoped permissions establishes ultimate S5 governance.

## Evidence gaps

- Source identity and frozen SHA verified; first-party runtime wiring and substantive generated source modules examined, with actual monolith entry point cross-checked. The architecture/changelogs are corroboration, not independent live evidence.
- Frozen upstream deterministic tests: `python -m unittest discover -s tests -p 'test_liquid_kernel.py' -q` **21/21 PASS**; `python -m unittest discover -s tests -p 'test_collaboration.py' -q` **59/59 PASS**. No real paid model/API, LAN multi-member E2E demonstration or live evolution deployment was run. `pytest` itself was unavailable, so standard-library `unittest` was used on these same in-tree tests.
- S3 is bounded to current complex-session operational allocation; in-session role names alone are insufficient evidence, so the decision explicitly rests on the actual blackboard→Manager decision→dispatch/feedback path. S3* rests on distinct model-controlled raw-source investigation, not all routine tests. S4 future signal is observed prior user-task history, not broad external strategic forecasting.

## Assessment summary

Clouds Coder has agent-owned model/tool coding operations (**S1=A**), a real constructor-owned inter-session shared-file anti-interference channel with human-owned contested resolutions (**S2=C**), evidence-sensitive whole-current complex-session work allocation (**S3=A**), a separate direct-file Reviewer model with actionable corrective feedback (**S3*=A**), and a supported opt-in historical-workload-to-future-kernel adaptation cycle with autonomous Tuning and separate parent-approval modes (**S4=A(P)**). Neither permissions nor admin/approval labels establish a genuine identity/ultimate-policy decision path (**S5=—**). This is a source-pinned organizational mapping, not a quality score or assurance of live model success.

Proposed vector: **`A · C · A · A · A(P) · —`**.
