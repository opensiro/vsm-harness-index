---
harness_id: minicode
project_name: Minicode
repository: https://github.com/startupmini/minicode
review_ref: aa76dfbea2c3d262b7ff4951e532277135793487
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Minicode

## Review boundary

- System in focus: Minicode's first-party coding-agent layer together with the exact vendored MiniCore kernel instantiated in the frozen repository tree at `aa76dfbea2c3d262b7ff4951e532277135793487`.
- Purpose and identity: execute software-engineering tasks through a transparent permission-first model/tool coding loop with first-party file, shell, Git, memory, planning, MCP/LSP, delegated-child, session, recovery and optional verification facilities.
- Relevant environment: user objective, workspace files and Git state, provider responses, tool results, local permission/sandbox decisions, durable session/checkpoint state, MCP/LSP responses and optional verification-command output.
- Standard-distribution boundary: Minicode's `src/` and `cli/` composition plus the pinned `vendor/minicore` tree are inside. Upstream MiniCore behavior not present in that vendored tree, sibling clones, external providers/MCP servers, host OS facilities and repository-development documents that are not runtime authority are outside.
- Credited operating/deployment surfaces: interactive CLI, one-shot/headless execution, the production-wired `delegate_task` path, optional `--verify`, permissions/sandboxing, sessions/recovery and the pinned vendored kernel.
- First-party modes considered: default/auto coding, ask/allowlist/readonly/plan/allow-all permission modes, headless/interactive execution, delegated explore/plan children and opt-in verification/self-heal.
- Recursion level: one Minicode coding session is the focal operation. Production-wired child sessions are subordinate operational delegates. They are considered for S2/S3 only where the required same-recursion disturbance/control closure is actually established.
- Frozen Minicode revision: `aa76dfbea2c3d262b7ff4951e532277135793487`.
- Vendored MiniCore provenance at that revision: `vendor/minicore/VENDOR.md` pins source commit `0d33571047c0ed3778986108fd42e4bde6828bb0`; only the shipped vendored tree is assessed.
- Observation date: 2026-10-04.
- Generated/current Profile version: `0.2.4`.
- Generated/current Methodology version: `0.3.6`.

## Repository architecture

Minicode composes a coding-specific application layer over a vendored MiniCore kernel. The pinned kernel's `loop.ts` explicitly implements one deterministic model → tool → observation loop: provider output yields tool calls, the executor returns tool results, those results are appended to the turn store and the next model step observes them. `src/app/session.ts` instantiates that exact kernel with Minicode's tools, system context, permissions, recovery and executor.

The application tool surface includes file editing, shell execution, Git inspection/commit, web access, memory, todo state, MCP/LSP, structured result submission and `delegate_task`. The composition root in `cli/index.ts` production-wires the delegated-child session factory before normal dispatch, so delegated children are reachable in ordinary REPL, one-shot and server paths rather than test-only machinery.

Delegation is bounded by a first-party pool and child restrictions. Children receive independent model/session histories and child journals, but the normal delegated plan mode runs against the parent's workspace `cwd`; Minicode does not create per-child Git worktrees in this path. The pool limits concurrency rather than resolving concrete cross-child operational conflicts.

Opt-in `--verify` executes a deterministic project verification command before/after the coding turn and, on failure, sends corrective evidence back through the same coding session's self-heal loop. It is useful operational feedback, but it is not a separate independent reviewer organization.

Project memory, repo maps, skills, steering and AGENTS/CLAUDE-style files are explicitly inserted by `buildSystemPrompt` as untrusted data that cannot override Minicode's own instructions. They therefore do not create a parent identity/ultimate-policy path.

Primary evidence:

- [README](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/README.md)
- [vendored MiniCore provenance](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/vendor/minicore/VENDOR.md)
- [vendored MiniCore loop](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/vendor/minicore/src/core/loop.ts)
- [vendored MiniCore session](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/vendor/minicore/src/core/session.ts)
- [Minicode session composition](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/src/app/session.ts)
- [delegation tool](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/src/tools/task.ts)
- [sub-agent pool](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/src/agents/pool.ts)
- [CLI composition root](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/cli/index.ts)
- [verify/self-heal driver](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/cli/setup.ts)
- [system/context construction](https://github.com/startupmini/minicode/blob/aa76dfbea2c3d262b7ff4951e532277135793487/src/policy/context.ts)

## S1 — Operations

- State: A
- Function: perform software-engineering work in the selected workspace through a model-owned sequence of inspection, editing, execution and evidence-driven revision.
- Disturbance / variety regulated: heterogeneous user objectives, repository structure, source-code defects, tool/shell outcomes, provider failures, context pressure, permission restrictions and test feedback.
- Decisive decision or feedback right: choose the next permitted coding/tool action from current task context and returned observations, revise the approach after errors/results and decide when to produce a terminal response.
- Decision owner: the model-backed Minicode coding actor running through the vendored MiniCore loop.
- Supporting/enforcement mechanisms: first-party tool registry, permission handler, sandbox policy, bounded executor, provider recovery, context compaction, sessions/checkpoints, todo/memory surfaces and optional verification.
- Closure path: user objective + current session/workspace evidence → model selects tool/action → Minicode permission/executor path runs it → tool result is committed to the turn context → next model step observes it → revised action or terminal answer.
- Boundary reachability: this is the ordinary Minicode interactive/headless execution path.
- Why agent-owned: removing the model actor leaves deterministic transport, policy and execution machinery, but removes the open-ended choice of coding actions and revisions.
- Evidence: pinned vendored `loop.ts`; `src/app/session.ts`; `src/tools/index.ts`; README.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external infrastructure; the credited organizational discretion is the first-party model/tool loop.

## S2 — Coordination

- State: —
- Function: no same-recursion inter-S1 coordination loop meeting the Profile threshold is established.
- Disturbance / variety regulated: delegated children can run concurrently, and concurrent mutating work in one parent workspace could in principle interfere; however the production delegation path does not expose a concrete first-party relation that detects/negotiates/attenuates such collisions and feeds the result into subsequent peer behavior.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting/enforcement mechanisms: `Pool` limits simultaneous delegated children; child scopes restrict tools/permissions; child journals isolate evidence; parent receives child summaries/events.
- Closure path: absent at S2 level. The pool supplies a capacity limit, not disturbance-specific coordination among operational children.
- Why not agent-owned: choosing to delegate and returning child summaries is task decomposition. Children do not negotiate shared-workspace conflict, reserve edit regions or receive a coordination decision that changes their later behavior.
- Evidence: `src/tools/task.ts`; `src/agents/pool.ts`; `cli/index.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: independent child sessions are real S1-like operational actors, but multiplicity alone is not S2.

### Absence scope

- Surfaces inspected: production delegation factory/wiring, child tool restrictions, pool scheduling, journals/event forwarding, permission modes and vendored executor.
- Plausible positive paths checked: concurrency pool as coordination; child isolation as collision control; parent delegation/result integration.
- Why no material path remains: children normally share the parent `cwd`; the pool regulates quantity, while delegation/result integration is explicitly parent-task decomposition rather than a concrete interference → attenuation → feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control owner is established.
- Disturbance / variety regulated: current session steps, child concurrency, budgets, permissions, todo state and background processes are bounded/observable, but no actor has a whole-current operational portfolio plus discretionary authority over shared commitments/resources on behalf of a multi-S1 whole.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting/enforcement mechanisms: max steps/timeouts, sub-agent pool limit, rate limiting, permissions, todo state, journals, session state and cancellation.
- Closure path: no whole-system current view → resource/priority/commitment intervention → changed multi-S1 operation loop was reconstructed.
- Why not agent-owned: the parent agent's choice to invoke a child and consume its result remains decomposition. Static/bounded runtime gates enforce constraints rather than choose whole-system current policy.
- Evidence: vendored kernel session/loop; `src/tools/task.ts`; `src/agents/pool.ts`; `cli/setup.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.

### Absence scope

- Surfaces inspected: child pool/current lifecycle, todo state, session state, budgets/rate limits, executor concurrency, cancellation and delegation result path.
- Plausible positive paths checked: parent as manager; concurrency limits as resource control; todo state as whole-current state.
- Why no material path remains: no distinct S3 whole-system regulation is established beyond the focal coding actor's own task execution and deterministic limits.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established.
- Disturbance / variety regulated: faulty code or incorrect completion claims can be caught by opt-in verification, tests, LSP diagnostics and other checks.
- Decisive decision or feedback right: no separate independent audit judgment owner is established.
- Decision owner: not established.
- Supporting/enforcement mechanisms: `--verify`, baseline verification, deterministic verification commands, completion-evidence reconciliation, test/LSP output and self-heal cycles.
- Closure path: verification evidence does return into further coding, but failed verification is fed back to the same Minicode coding session for self-heal. This is routine operational QA rather than a complementary independent audit channel.
- Why not agent-owned: there is no separate reviewer/model/evaluator with materially different access to operational reality and its own audit judgment.
- Evidence: `cli/setup.ts` `runPromptWithVerify` / `runPromptWithVerifyInner`.
- Basis: explicit + structural absence review.
- Confidence: high.

### Absence scope

- Surfaces inspected: `--verify`, baseline verification, self-heal driver, test evidence presentation, LSP diagnostics, benchmark/audit references and child delegation.
- Plausible positive paths checked: deterministic verifier as S3*; delegated child as reviewer.
- Why no material path remains: the standard verify path is deterministic same-production-path QA, and no standard independent reviewer child is wired as a mandatory/complementary audit path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptation loop that changes future Minicode capability is established.
- Disturbance / variety regulated: current-task web/MCP information, memory retrieval, verified-run snippets and provider/model changes can influence later work, but none of these surfaces establishes the required environmental sensing → adaptation-option development → returned capability-change loop.
- Decisive decision or feedback right: not established at S4 level.
- Decision owner: not established.
- Supporting/enforcement mechanisms: web tools, MCP, memory RAG, session persistence, verified-run snippet memory, model/provider selection and repo-map/context loading.
- Closure path: no first-party prospective adaptation option is shown changing Minicode's reusable capability/configuration through an S4 loop.
- Why not agent-owned: memory and current-task research preserve/use evidence but do not themselves make future-oriented capability adaptations.
- Evidence: README; `src/policy/context.ts`; memory/session surfaces; verify snippet behavior in `cli/setup.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.

### Absence scope

- Surfaces inspected: memory/RAG, verified-run snippets, web/MCP, skills/context, provider/model selection, session persistence and repository plans/docs.
- Plausible positive paths checked: learning from verification; persistent memory as adaptation; external research as S4.
- Why no material path remains: these paths inform present/future prompts but do not establish a closed prospective adaptation decision that modifies current system capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established at the assessed harness boundary.
- Disturbance / variety regulated: permissions, sandboxing and project context constrain coding behavior, but constraints are not by themselves S5.
- Decisive decision or feedback right: no first-party identity-level decision path with legitimate ultimate authority and returned governance was reconstructed.
- Decision owner: not established at S5 level.
- Supporting/enforcement mechanisms: system prompt, permission modes, sandbox policy, trusted/local configuration, operator approval and project context files.
- Closure path: ordinary approvals/configuration alter execution posture, but no identity/ultimate-policy issue is escalated through a qualifying first-party parent loop and returned to govern subsequent operation.
- Why not parent-owned: `buildSystemPrompt` explicitly marks MEMORY, repo map, skills, steering and agent files as untrusted data that “never override the instructions above”; AGENTS/CLAUDE/steering therefore do not act as authoritative parent constitutions.
- Evidence: `src/policy/context.ts`; `src/policy/permission.ts`; `src/app/session.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.

### Absence scope

- Surfaces inspected: system prompt/context construction, AGENTS/CLAUDE/steering loading, permission modes, sandbox policy, local configuration, human approval and repository governance documents.
- Plausible positive paths checked: operator approval as S5; project instructions as parent policy; static permission/safety policy as S5.
- Why no material path remains: approvals are task/action-level, project files are explicitly non-authoritative data, and static policy/configuration does not provide runtime identity-level decision closure.

## Recursion

The focal recursion is one Minicode coding session. Delegated children are real bounded subordinate sessions and can independently perform limited work, but the frozen standard distribution does not show them forming a separately viable same-recursion organization with its own S2–S5 metasystem.

The vendored MiniCore kernel is implementation substrate inside Minicode rather than a separate assessed organizational recursion. Its source provenance is pinned by `VENDOR.md`, and only behavior instantiated in that vendored tree is used here.

## Variety and escalation

Minicode attenuates coding-task variety through a broad tool surface, permission modes, sandboxing, provider recovery, context compaction, child delegation, session persistence, todo/memory state and optional self-healing verification. These mechanisms make S1 robust, but their presence is not promoted to higher VSM functions without the required distinct decision and closure paths.

## Evidence gaps

No `?` state is required. The exact pinned repository contains enough runtime and vendored-kernel evidence to establish S1 and to bound the strongest higher-function candidates. Upstream MiniCore features outside the pinned vendored tree were intentionally not imported.

## Assessment summary

Minicode closes autonomous S1 through its first-party coding layer over the pinned vendored MiniCore model/tool loop. Production-wired child sessions provide real delegation but no disturbance-specific S2 or whole-current S3. Opt-in verification runs deterministic checks and feeds failures back into the same coding session rather than an independent S3* auditor. Memory, external tools, project context, permissions and static safety machinery do not close prospective S4 or identity-level S5.

**Vector:** A · — · — · — · — · —
