---
harness_id: paseka
project_name: Paseka
repository: https://github.com/russ-p/paseka
review_ref: 11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: P
autonomy_s4: —
autonomy_s5: —
---

# Paseka

## Review boundary

- System in focus: one configured Paseka colony, with its first-party Go `paseka` CLI, NATS/JetStream reactor, task ledger, prompt/bee adapter composition, trace-bound Git worktree control, Queen Console and human review/merge path, at frozen commit `11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac`.
- Purpose and identity: coordinate persistent event-triggered, externally model-backed worker bees against a Git project, construct isolated work proposals and return results to a human operator for review and integration.
- Relevant environment: local Git repository, operator, NATS service, provider coding CLIs (Cursor, Pi, Claude, OpenCode), optional script adapter, per-colony bee declarations and provider credentials, working diff and code/test feedback.
- Standard-distribution boundary: installed `paseka init` and `paseka run`, `bee run`, configured adapter/bee execution, NATS/JetStream ledger and operational Console. Built-in code does not implement provider model inference and never inherits the external coding CLI's own governance.
- Credited operating / distribution surfaces: `colonyinit.Init` provisions scout/builder/hivewright, first-party dispatcher/reactor, optional declarative subscriptions, `worktree.Ensure`, Console trace board/merge diff and human approve/reject/request changes, final gate/rework/publish reconciliation.
- Adjacent first-party surfaces excluded from ownership: repository's own `.paseka/bees/guard.yaml`, `main-guard.yaml`, `receiver.yaml` and prompts as contributor/dogfood colony configuration **not provisioned** by standard `paseka init`; design/spec documents, future MCP wrapping, unconfigured external witness/reviewer tools, upstream provider cognitive loops.
- First-party operating / deployment modes considered: standard initialized colony and optional per-bee `worktree:true`/worktree-isolated proposals, headless `paseka run`, interactive HITL and Console final review; configured NATS/worker provider required. Worktree path is opt-in per bee, not automatic for every agent. Optional local user-supplied guard bee composition was inspected but cannot establish product-default autonomous audit ownership.
- Recursion level: one first-party colony as organizer of parallel agent operations and control returned to its human operator. Separate agent CLI internals and upstream workflow systems are a different lower recursion.
- Reviewed revision: `11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac`.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Paseka owns the first-party event topology and launch of provider-backed bee sessions. `paseka init` creates a usable colony with scout, builder and hivewright roles; `paseka run` builds the real reactor, subscriber/dispatcher and durable KV ledger. Incoming domain events change task state; eligible events and tasks dispatch actual configured worker CLI processes, with prompt and result records kept under trace/agent-scoped run directories. The workers choose local coding or planning actions within the scoped role and return code/events; their model/tool engines remain external dependencies. This is a **composed autonomous operational S1**, not Go code implementing an independent LLM engine ([internal/colonyinit/init.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colonyinit/init.go), [cmd/paseka/run.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/cmd/paseka/run.go), [internal/runtime/reactor.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/reactor.go), [internal/runtime/dispatch_task.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/dispatch_task.go), [internal/runtime/dispatch_stages.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/dispatch_stages.go)).

Paseka also provides a specific **cross-operation interference attenuator** when separate worktrees are configured. The dispatcher resolves a per-trace isolated Git worktree under `.paseka/worktrees/<traceId>/`, segregating coding modifications from the root working tree and from separate trace workspaces; changes return toward root only through a review gate and explicit merge/publish decision. This does not protect independent bees sharing the *same trace worktree*, and NATS delivery/energy gating alone would not prove S2 ([internal/runtime/colony_dispatch.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/colony_dispatch.go), [internal/worktree/worktree.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/worktree/worktree.go), [internal/review/gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/gate.go), [internal/review/final_gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/final_gate.go)).

A human has meaningful first-party present-control rights: the Console assembles a colony-wide task/review view, permits starting/retrying or interrupting execution, inspects incoming work, and approves/denies consequential merges. Reactor scheduling and energy gates execute previously selected task rules; they do not decide colony strategy with context-dependent discretion. Whole-present control is therefore **parent-owned S3=P** ([cmd/paseka/status.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/cmd/paseka/status.go), [internal/console/tasks.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/tasks.go), [internal/console/review.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/review.go), [internal/console/runtime.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/runtime.go)).

A distinct **parent-owned complementary audit** path uses actual worktree changes, not just a bee's self-report: Queen Console's merge-diff viewer invokes `GetMergeDiff`; a human independently inspects raw patches, adds line-anchored comments or rejects, and those findings feed first-party review/rework or leave work blocked until reviewed. Approval and reject endpoints reach the task ledger and, when appropriate, Git merge or PR publication. This is specifically S3*=P **for the human-reviewed proposal mode**, not S3*=A from repository-local guard-role files. The sample guard role does inspect diffs and emit verification events, and default reactor can route verification failures, but `paseka init` does *not* provision guard; the default parent path is sufficient here ([internal/console/merge_diff.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/merge_diff.go), [internal/console/review.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/review.go), [internal/review/comments.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/comments.go), [internal/review/rework.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/rework.go), [internal/review/gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/gate.go), [internal/colonyinit/init.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colonyinit/init.go)).

No first-party prospective external-environment adaptation of the colony's future capabilities or ultimate identity-policy decision loop was evidenced in the supported distribution. Scout feature intake and model-drafted task plans are directed to current task execution; stored insights and adapter profile/model aliases are not by themselves S4, while operator consent and static configuration do not establish S5 ([internal/colonyinit/init.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colonyinit/init.go), [internal/invites/auto_invite.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/invites/auto_invite.go), [internal/runtime/insights.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/insights.go), [internal/console/review.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/review.go)).

## Operational model

The operator initializes a colony, provisions provider CLIs/NATS and starts the reactor. A role-specific subscriber accepts an event or ready task; Paseka loads that role, constructs the prompt and isolated workspace when requested, launches the configured external model-backed bee and normalizes status, artifacts and explicit event outputs. The event-driven ledger and dispatcher route successor operations. On the review path, an isolated proposal remains outside the project's default branch until the human inspects the independent Git diff and approves, rejects or requests rework; the review result changes subsequent task/merge state. No provider-backed live run or multi-trace collision trial was performed for this assessment.

## S1 — Operations

- State: A
- Function: produce code/research/plan artifacts for scoped project tasks through installed/role-bound autonomous provider-backed bee sessions.
- Disturbance / variety regulated: task uncertainty, repository/test/tool state, requirements and local model corrections encountered by each bee.
- Decisive decision or feedback right: choose provider-backed substantive code or analysis actions within a declared bee role, process environmental responses and report artifacts/domain events.
- Decision owner: a model-backed bee launched and identified by Paseka's first-party adapter/prompt/runtime composition; vendor model inference is external.
- Supporting / enforcement mechanisms: initialized bee YAML, provider adapter, rendered role prompt, RunRequest, run directory, NATS event bus, trace/task ledger.
- Closure path: configured role and ready event → first-party dispatcher launches external model-backed bee in scoped cwd → bee makes contextual task decisions and acts on repository/tool feedback → output/typed events enter Paseka ledger and later team tasks.
- Boundary reachability: `paseka init` writes scout/builder roles, and `paseka run` wires dispatcher/reactor; `dispatchReady` invokes `DispatchColonyBee`. Working external provider is required but already part of supported deployment.
- Why this is / is not agent-owned: removing the launched model-backed bee leaves only deterministic event routing, not autonomous task completion; no borrowed vendor internal metasystem.
- Evidence: [internal/colonyinit/init.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colonyinit/init.go); [internal/runtime/reactor.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/reactor.go); [internal/runtime/dispatch_task.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/dispatch_task.go); [internal/runtime/dispatch_stages.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/dispatch_stages.go); [internal/adapters/adapter.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/adapters/adapter.go).
- Basis: first-party installed composition and actual dispatch code; no observed external inference.
- Confidence: medium-high for supported S1 composition.
- Caveats: `script`/static adapters may not supply model-owned S1; grade is for enabled model-backed mode.

## S2 — Coordination

- State: C
- Function: separate potentially competing operational changes from distinct concurrent trace-worker groups before root integration.
- Disturbance / variety regulated: multiple coding bees/traces might change overlapping Git project files, contaminate the default worktree or prematurely expose one operational unit's incomplete patch to another.
- Decisive decision or feedback right: route appropriately configured bee work into a trace-specific Git worktree, instead of shared root; withhold transfer to the primary branch until review/merge authorization.
- Decision owner: first-party deterministic workspace allocator/construction based on `worktree` bee/proposal mode and task trace; user/parent owns any final merge.
- Supporting / enforcement mechanisms: `workspaceForDispatch`, per-trace `worktree.Ensure`, distinct branch/path, independent run directories and protected merge-diff/review.
- Closure path: concurrent trace IDs + worktree-isolation choice → distinct physical Git workspaces → each bee modifies its own trace branch, not another trace's working area → later review/merge controls reconcile effects into shared repo.
- Boundary reachability: `builder` in the default initialized colony is configured for worktree use; `workspaceForDispatch` is executed inside real `DispatchColonyBee`, not merely a design.
- Why this is / is not agent-owned: executable deterministic attenuation of inter-bee write interference, not independent choice by a model.
- Distinct S1 units: separately launched coding-role bees operating on different trace workstreams of a colony, potentially concurrent.
- Inter-S1 disturbance: overlapping writes from separate traces into the same repository root/working files.
- Attenuating coordination relation: physical per-trace worktree and branch isolation until explicit acceptance/merge.
- Feedback into subsequent S1 behaviour: assigned bees operate in their per-trace cwd and produce isolated proposals; their output is held from the shared root until a reconciled review result.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: path selection changes the writable execution environment for distinct operational groups and materially contains their shared-root interference rather than only relaying events.
- Evidence: [internal/runtime/colony_dispatch.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/colony_dispatch.go); [internal/worktree/worktree.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/worktree/worktree.go); [internal/review/gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/gate.go); [internal/colonyinit/init.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colonyinit/init.go).
- Basis: source-wired opt-in constructor, no observed multi-bee conflict test.
- Confidence: medium-high for physical containment, not semantic merge safety.
- Caveats: bees within one trace share its worktree, and direct root-mode roles bypass separation; this is a narrow conditional S2 construction.

## S3 — Inside-and-now control

- State: P
- Function: parent operator supervises the colony's current task/trace commitments and execution resource constraints, intervening across running/blocked/completed work.
- Disturbance / variety regulated: blocked work, pending review, competing tasks, in-flight session status, resource/energy limits, need to start/retry or stop.
- Decisive decision or feedback right: use colony-wide status/Console task board to choose task starts/retries, runtime stop/start, review dispositions and consequential merge commitments.
- Decision owner: human operator acting through shipped CLI/Queen Console; reactor handles eligible dispatch and bounded gates deterministically.
- Supporting / enforcement mechanisms: `hiveview.BuildColonySnapshot`, task ledger, `StartTask`, review queue, runtime supervisor, trace kill, energy gate and event bus.
- Closure path: colony/task status and review queue → operator changes pending work or stops/starts a run → first-party task ledger/dispatcher/supervisor applies change → status and subsequent worker activities reflect intervention.
- Boundary reachability: shipping CLI status/kill/task commands and Console read/write operations, not external manual shell-only modification.
- Why this is / is not agent-owned: no installed current-control model has been shown choosing whole-colony resource commitments; Scout/auto-invite make local event/task decisions, not this whole-current control choice.
- Whole-system current view: active colony status across traces, sessions, tasks, energy and items needing review, scoped to one initialized colony.
- Current-control decision scope: current task starts/retries, selected running process lifecycle and human approval/rejection of multi-task work.
- Evidence: [cmd/paseka/status.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/cmd/paseka/status.go); [cmd/paseka/task.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/cmd/paseka/task.go); [cmd/paseka/kill.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/cmd/paseka/kill.go); [internal/console/review.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/review.go); [internal/console/tasks.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/tasks.go); [internal/console/runtime.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/runtime.go).
- Basis: source-backed parent current-control return.
- Confidence: medium-high on control surfaces, not a witnessed operator session.
- Caveats: model-issued ordinary task plans and budget gates do not justify S3=A.

## S3* — Complementary audit

- State: P
- Function: independently challenge operational completion/merge claims using **raw Git diff evidence** beyond the bee's own summary and return rejection or corrected acceptance to current operations.
- Disturbance / variety regulated: incorrect, unsafe, unrelated or incomplete code patches/claims, accidental inclusion of unreviewed changes.
- Decisive decision or feedback right: inspect actual proposed diff, reject/request specific rework or approve final integration based on that independent evidence.
- Decision owner: human operator in supported Queen Console review flow; optional model-backed `guard` in repository-local bee config is **not** automatically credited as default first-party autonomous reviewer.
- Supporting / enforcement mechanisms: `GetMergeDiff` over worktree/branch, review queue, annotation/comment packet with code paths and lines, `RejectTask`/rework events, `review.Approve`, final gate.
- Closure path: completed/proposed worker result → independent raw worktree diff is rendered for human → line-anchored comment/reject or approval → rework task/human feedback returns through ledger to further bee work, or reviewed content merges/publishes → subsequent operations change.
- Boundary reachability: shipping Console review queue, code diff API and viewer, `RejectTask` with `SubmitAnnotatedReview`, `ApproveTask` driving review domain and merge/PR path; final merge gate is activated by reactor on completed AFK tasks with changes. Requires use of review-gated proposal workflow.
- Why this is / is not agent-owned: human reviewer holds the independent evidentiary judgment; presence of named guard agents in *this repository's own development colony files* does not prove a standard installed autonomous S3*.
- Claim being audited: worker's reported task outcome / readiness for code integration.
- Ordinary reporting path: adapter exit/result metadata, task/trace summary, events and `summary.md`.
- Complementary access path: independently calculated Git branch merge diff, actual changes, file/line citations and separate operator judgment.
- Independence boundary: operator does not merely replay builder self-report; raw Git diff is derived by code path distinct from provider output and enables rejection even when the worker says completed.
- Who acts on findings: operator records approve/reject; implemented ledger/rework/merge flow enforces the disposition.
- Evidence: [internal/console/merge_diff.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/merge_diff.go); [internal/console/review.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/review.go); [internal/review/comments.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/comments.go); [internal/review/rework.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/rework.go); [internal/review/gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/gate.go); [internal/review/final_gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/final_gate.go); [internal/runtime/review_gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/review_gate.go).
- Basis: complete parent-governed independently sourced return path in shipped Console/merge mode.
- Confidence: medium-high in structural audit closure, not proof reviewers correctly identify every defect.
- Caveats: the parent review only applies where proposal/gate workflow is enabled; non-review tasks may complete without this S3* path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped first-party exterior/prospective capability governance and feedback into new organizational capacity established.
- Disturbance / variety regulated: future technology, agent-provider/market changes, longer-horizon risks and capability constraints.
- Decisive decision or feedback right: develop, decide and adopt future adaptation options from environmental intelligence; no qualifying closed S4 path identified.
- Decision owner: operator/developer may change roles/model aliases and Scout may interpret a feature request, but no distinct installed colony-level prospective capacity actor is demonstrated.
- Supporting / enforcement mechanisms: Scout/feature intake, auto-invites, insights, runtime model aliases, prompts, persistent trace state.
- Closure path: feature requests can trigger current task plans/dispatch; this is not future/environment assessment → new operational capability design and installed S3/S1 adaptation at the assessed recursion.
- Boundary reachability: wired feature intake and event choreography were considered, not upgraded by vocabulary such as `scout` or persistence.
- Why this is / is not agent-owned: choosing how to do the next requested task is local S1/current work, not a distinct future-intelligence regulator.
- Evidence: [internal/colonyinit/init.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colonyinit/init.go); [internal/invites/auto_invite.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/invites/auto_invite.go); [internal/runtime/insights.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/runtime/insights.go); [internal/colony/colony.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colony/invite_rules.go).
- Basis: bounded negative on examined wired source.
- Confidence: medium-high within reviewed standard distribution.
- Caveats: bespoke externally authored bee roles might implement future intelligence in a wider custom deployment; not credited here.

### Absence scope

- Surfaces inspected: installed bee/template scaffold, `scout` feature requests, auto-invite rules, current ledger dispatch, insight collection, configuration/model aliases and operations.
- Plausible first-party paths checked: new-feature assessment, next-epic planning, stored cross-run insights, new worker provisioning and model/profile configuration.
- Why no material first-party path remains: found routes transform current demand into tasks, preserve context or change static user setup; none independently makes an externally and prospectively grounded organizational capability decision and returns a revised mode of operation.

## S5 — Identity and ultimate policy

- State: —
- Function: no ultimate organizational identity/ethos/policy decision path with return into whole-colony operation was evidenced.
- Disturbance / variety regulated: fundamental colony mandate, identity commitments, unresolved present-versus-future organizational direction.
- Decisive decision or feedback right: legitimate ultimate mission/values choice and returned governance policy; not established.
- Decision owner: operator declares colony config and approval limits; runtime validates events/permissions and enforces constraints, but no S5-level question/decision path is installed.
- Supporting / enforcement mechanisms: colony slug/manifest, credentials, event schema, energy budgets, human review approval and adapter trust flags.
- Closure path: project setup and per-task human approval affect execution and merges; neither is an ultimate identity/policy choice resolving S3–S4 tension then governing future colony behavior.
- Boundary reachability: shipped `init`/configuration, Console review and authority controls inspected; unrelated human project governance outside runtime excluded.
- Why this is / is not agent-owned: human approval of code is not automatically human-owned ultimate S5, and authentication/configuration does not grant a model authority to revise colony identity.
- Evidence: [internal/colonyinit/init.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colonyinit/init.go); [internal/colony/manifest.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/colony/routing.go); [internal/review/gate.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/review/gate.go); [internal/console/review.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/console/review.go); [internal/protocol/event.go](https://github.com/russ-p/paseka/blob/11bc0b91e1442e74ccadd9bbe591ebaa8afcc8ac/internal/protocol/protocol.go).
- Basis: bounded source-first negative.
- Confidence: medium-high for pinned shipped modes.
- Caveats: real humans/institutions may govern the project outside Paseka; those are not a first-party S5 loop.

### Absence scope

- Surfaces inspected: `init` colony purpose/config and slug, task/bee roles, event permissions, operator approval/energy policy, Console/current-control routes.
- Plausible first-party paths checked: human mandatory merge decision, changing project goals in feature requests, trusted credentials and role configuration.
- Why no material first-party path remains: found choices are ordinary project setup, current task acceptance, access constraints and runtime reliability, not a separate identity or ultimate-policy decision-and-return organ.

## Evidence gaps

- This was a **pinned first-party source assessment**, not a live NATS/provider-backed end-to-end or empirically witnessed human code review; existence of wired source paths does not certify effectiveness.
- The repo-local guard/main-guard/receiver configuration is explicitly **not** standard `paseka init` output. It shows a possible user-composed independent model review loop but must not inflate standard product S3* ownership.
- The S2 construction separates **different trace workspaces**, not simultaneously active bees within one trace or unsafe Git merges; per-bee `worktree` is configured, not universal.
- S3 and S3* parent functions may be exercised by the same operator but are functionally distinct: current task/capacity control vs complementary direct-Git-evidence challenge of completion claims.
- Model/provider internal reasoning, unpublished deployments, repository maintenance CI and design proposals are excluded from attributed ownership.

## Conclusion

**Proposed**, not canonical: `S1=A / S2=C / S3=P / S3*=P / S4=— / S5=—` for a standard initialized, model-backed and optionally worktree-isolated Paseka colony with shipped Queen Console review. The reactor and adapters instantiate substantive agent operations; worktree trace isolation constructs limited S2; human operator performs whole-current control (S3=P) and raw-diff-backed independent review with binding rework/merge disposition (S3*=P). Neither generic NATS transport nor repo-local optional Guard Bee is promoted to a product-owned higher agent function; no prospective S4 or identity S5 regulatory loop is demonstrated.
