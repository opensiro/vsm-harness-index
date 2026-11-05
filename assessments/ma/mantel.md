---
harness_id: mantel
project_name: Mantel
repository: https://github.com/RealNarcissus/mantel
review_ref: 0b8d577e9401f3fcdf1349b7c72288de82eff792
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Mantel

## Review boundary

- System in focus: one installed Mantel GTK4 Linux agent desktop, its Pi or Gemini engine adapter, per-turn tool/approval loop, user task/schedule/plan stores, live work/diff/weekly review panels and human control path.
- Purpose and identity: provide a native user-controlled place for agentic work and personal day planning while keeping approvals, persisted context, actual file changes and scheduled activity inspectable.
- Relevant environment: the user's workspace and Git status, present tasks and calendar, local folders, live provider responses, filesystem/tool risks, app crashes and changing scheduled commitments.
- Standard-distribution boundary: Python GTK shell and controller, built-in Gemini REST model/tool executor, Pi RPC adapter and approval extension, session persistence, tasks/schedules/calendar/knowledge and native controls; external Pi runtime, model providers and user credentials are dependencies. No vendor-side agent organization is borrowed.
- Credited operating / distribution surfaces: [README implementation and limitations](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/README.md), [Gemini tool loop](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/engines/gemini_api.py), [Pi RPC adapter](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/engines/pi_rpc.py), [window and steering](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/window.py), [scheduler](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/scheduler.py), [raw Git changes](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/changes.py).
- Adjacent first-party surfaces excluded from ownership: developer-side UI snapshot/demo tooling, 17 offline test suites, icon/font reverse-engineering, future provider/feature roadmaps, other providers' independent planning/coding agents and offline benchmark probes.
- First-party operating / deployment modes considered: installed interactive Pi RPC with real pre-execution approval extension, Gemini API streaming with directly implemented tool loop, persistent conversations and steering, in-app one-at-a-time scheduled prompts, GTK task/plan/calendar views, optional knowledge, plugins and external Git diff view.
- Recursion level: personal desktop/work portfolio with a model-operating per-turn S1, human user as current manager; not a distributed coordinated multi-agent company.
- Reviewed revision: `0b8d577e9401f3fcdf1349b7c72288de82eff792`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The GTK shell starts an engine-backed conversation, streams model/tool events, displays approvals *before* write or shell execution, stores turn state and shows live work. With `GEMINI_API_KEY`, Mantel's own Python `GeminiAdapter` sends function specifications to the model, resolves workspace-scoped read/write/command requests, returns execution results to the model and repeats for at most eight steps. With Pi, the first-party adapter invokes external `pi --mode rpc` and a shipped approval extension. Independently, the scheduler runs one due prompt while the app is open and saves the run as a conversation; the dashboard shows tasks, calendar and weekly aggregates. The Git changes panel fetches the actual working tree separately from model tool claims. [Architecture](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/docs/ARCHITECTURE.md); [engine code](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/engines/gemini_api.py).

## Operational model

The Gemini engine's dispatched model chooses between reading files, proposing writes, requesting commands and interpreting returned output. Mantel itself implements the permission-gated tool feedback loop; this is stronger evidence than merely wrapping an external chat UI. Pi's model/tool loop remains external, but Mantel wires pre-execution approval and result observation around it. The released README explicitly says the product is very early and that no full provider-backed turn has been observed end to end in the repository; actual tests used a local fake API and Pi protocol probes. Older module docstrings and `docs/ARCHITECTURE.md` call Gemini 'chat only' despite the pinned **executable code** implementing `TOOLS` and `APPROVALS`; operational source and current README delimit the mapping, while live readiness remains unverified. [README](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/README.md); [implemented `_pump` loop](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/engines/gemini_api.py).

## S1 — Operations

- State: A
- Function: an engine-backed model uses chat/tool turns to manipulate the workspace, complete scoped tasks and respond to tool outcomes; scheduled prompts can start a fresh bounded conversational task.
- Disturbance / variety regulated: unknown local files, model questions, command failures, incomplete prior turn and changing user instructions within the workspace.
- Decisive decision or feedback right: model chooses `read_file`, `write_file`, `run_command` and subsequent actions from returned tool results; write/command requests must receive human authorization before execution.
- Decision owner: configured model acting through Mantel's Gemini function-call executor or user-selected Pi tool runtime; first-party Mantel defines the integrated Gemini loop and regulates execution.
- Supporting / enforcement mechanisms: function schemas, workspace boundary check, per-command prompt, `GeminiTurn` result return, max-eight tool-step bound, durable conversation and steer/abort path.
- Closure path: user/task prompt → model selects a file/command action → Mantel gates and runs permitted tool → sends concrete result as `functionResponse` → model decides next tool or answer → persisted conversation and actual workspace changes.
- Boundary reachability: `GeminiAdapter.capabilities` advertises `CHAT`, `TOOLS`, `APPROVALS`, `run()` wires `GeminiTurn` and `_pump`, and the shell invokes it through standard `Engine.run`; the documented Pi mode is another wired host adapter.
- Why this is / is not agent-owned: next tool, modification and response selection are model choices operating on a real environment. UI task entry alone would not suffice; the actual first-party Gemini tool loop and protocol seam supply the operational closure.
- Evidence: [Gemini function call and returned result](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/engines/gemini_api.py), [app turn integration](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/window.py), [Pi approval extension](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/pi-extensions/approvals.ts).
- Basis: pinned source-level live code wiring, offline fake API tests and protocol validation; no authenticated provider E2E in this review.
- Confidence: high that meaningful model actions are implemented, medium that the immature release operates reliably on real accounts.
- Caveats: live provider/host integration remains unproven and the Pi runtime's own architecture is not credited as Mantel's autonomous governance.

## S2 — Coordination

- State: —
- Function: no first-party cross-S1 anti-interference and feedback loop was established for two distinct simultaneously acting autonomous operational agents at this desktop recursion.
- Disturbance / variety regulated: hypothetical overlapping edits or scheduled tasks racing active chat could be inter-S1 disturbances, but no witnessed shared multi-agent coordination cycle controls them.
- Decisive decision or feedback right: the scheduler serializes its own due prompts, and the engine separates conversations; neither establishes inter-agent negotiation or collision-specific feedback to independent S1 workers.
- Decision owner: not established for an inter-S1 coordination function; schedule ordering is deterministic.
- Supporting / enforcement mechanisms: one-at-a-time scheduled runner, command approval, personal task store, engine session separation and workspace-scoped tool access.
- Closure path: due jobs are processed in sequence and a turn finishes; no explicit collision evaluation between two independent model S1 units and corrective instructions returning to both were found.
- Boundary reachability: the serial scheduler runs within the app, but multiple independently owned concurrent S1 tasks and a clash-specific coordination path do not follow from its availability.
- Why this is / is not agent-owned: task/calendar ordering and safe tool approval do not become VSM S2 without identifiable inter-S1 interference and feedback; this review does not infer a multi-agent organization from many UI threads.
- Evidence: [single-run scheduler](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/scheduler.py), [engine seam](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/docs/ARCHITECTURE.md), [session/workspace scope](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/session.py).
- Basis: bounded negative review of shipped live-session and scheduled-work paths.
- Confidence: medium-high for absence of multi-agent S2, not a claim that no timing races can occur.
- Caveats: internal schedule serialization is useful safety engineering but not evidence that independent agents mutually adjust to a concrete collision.

### Absence scope

- Surfaces inspected: scheduler, schedule/run store, interactive engine session and turn loop, workspace tool scope, tasks/calendar and command approvals.
- Plausible first-party paths checked: multiple due prompts, scheduled-versus-interactive tool overlap, task dependency/order, isolated Pi/Gemini sessions and per-turn locks.
- Why no material first-party path remains: the shipped scheduler launches one due job at a time and exposes no conflict-specific relation between two simultaneously acting S1 agents with feedback into changed work.

## S3 — Inside-and-now control

- State: P
- Function: the human desktop owner can see and revise the current combined commitments of tasks, conversations, reminders, focus, schedules and model-tool activity.
- Disturbance / variety regulated: overdue work, clashing day commitments, unexpected writes/commands, failed scheduled prompts, too many nudges and agent actions misaligned with the owner's current intent.
- Decisive decision or feedback right: inspect Today/Review and work panels; add/complete tasks, change schedules, choose mode/model/effort and approve/deny commands or steer/abort active work.
- Decision owner: human owner/operator for what work and tools are currently authorized; automatic scheduler runs configured prompts but has no independent right to reprioritize the portfolio.
- Supporting / enforcement mechanisms: Today list, schedule runner/results, task/calendar/weekly review stats, current work panel, approval cards with scopes, steering and command palette.
- Closure path: whole-work view shows due/current/results → human changes tasks/schedule or approval and sends steering → next scheduled prompt or engine step obeys the changed commitment/envelope.
- Boundary reachability: GTK `Window` creates Today/tasks/schedule/review pages, installs scheduler and connects approval/steer UI handlers to active engine/session and persistent task store.
- Why this is / is not agent-owned: the app calculates and displays state, but a human decides current priorities/permissions; no model-based portfolio governor is shown, so `P` rather than `A`.
- Whole-system current view: aggregated deadlines, task history, planned work, scheduled prompts, review counters, agent work and permission requests across the desktop.
- Current-control decision scope: current task/schedule changes, active tool permissions, conversation steering and pause/stop of a running task.
- Evidence: [Today agenda](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/pages/today.py), [window and approvals](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/window.py), [scheduled work](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/scheduler.py).
- Basis: explicit UI implementation and first-party action wiring; live provider success is not required to see that the human retains these rights.
- Confidence: medium-high for supported human control, bounded by early-release operational gaps.
- Caveats: many dashboard panels are usable in demo mode without working tools; only actual user actions tied to stores or permitted engine turns are credited.

## S3* — Complementary audit

- State: C
- Function: the user can independently inspect actual Git filesystem changes and measured weekly task evidence instead of relying on the agent's own tool/work report.
- Disturbance / variety regulated: an agent could state that a file was edited or test passed when the working tree says otherwise, or paint a misleading picture of weekly progress.
- Decisive decision or feedback right: open a file-level `git diff` from the independent Changes panel and compare to the conversation/work claim; use steering or a new corrective request to change work; user can additionally compare local completed/overdue/focus counts to narrative.
- Decision owner: first-party independent Git/statistics observation constructor provides alternative evidence; a human chooses whether to inspect and send a corrective instruction. No independent auditing model owns that judgment.
- Supporting / enforcement mechanisms: `changes.collect` calls `git status --porcelain` and `git diff --numstat` independently, `changes.diff` shows raw unified diff, Window opens a read-only dialog, weekly review derives counts from local store separately from model-written prose.
- Closure path: model claims and work panel → user opens actual Git diff/weekly data → notices mismatch or missing work → sends steering/new instruction or denies unsafe follow-up; next model turn receives the correction.
- Boundary reachability: `Window._update_changes` reads Git independently of tool events, `_show_diff` opens the actual diff, and `Window.steer` queues a human correction through the active engine when supported.
- Why this is / is not agent-owned: the shipped alternative reality-access path is a deterministic constructor (`C`); a human can examine it and steer, but Methodology parent-mode `P` does not apply to S3*. It is neither an autonomous reviewer nor merely another model-authored progress log.
- Claim being audited: the agent's reported changed files/progress reflect actual workspace state and task record.
- Ordinary reporting path: model prose and streamed tool events feeding `Session.work_items()`/work panel.
- Complementary access path: direct Git working-tree diff and locally calculated finished/overdue/focus counters, separate from the agent's natural-language claim.
- Independence boundary: raw Git subprocess and local store are independent of the agent's narrative but share the user's mutable workspace; a malicious agent could tamper with the repository itself, and no external forensic auditor is claimed.
- Who acts on findings: human user issues a new instruction or steers a supported active Pi turn; there is no automatic blocking review verdict.
- Evidence: [Git audit source](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/changes.py), [live diff/steer UI wiring](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/window.py), [weekly evidence separation](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/pages/review.py).
- Basis: implemented complementary observation and optional human correction route; Methodology 0.3.7's canonical `C` ownership class, not a logged independent review incident.
- Confidence: medium for S3* closure because follow-up is discretionary and operator-driven rather than an enforced review step.
- Caveats: the changes panel is best-effort, can omit external/untracked detail and cannot prove test success from Git alone; optional human review does not imply continuous monitoring or formal assurance.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective adaptation cycle turning future environment alternatives into a durable changed operating capability is demonstrated at this personal desktop recursion.
- Disturbance / variety regulated: upcoming calendar commitments, changes in external model offers, new user goals and future workload could alter the user's longer-term approach.
- Decisive decision or feedback right: Today can propose a near-term calendar-aware day plan, Review compares last week's data, and user can select a model; no longer-horizon external environment scenario/option choice and S4-to-S3 return were shown.
- Decision owner: the human determines personal strategies; model-generated weekly narrative and current day scheduling stay at current operations/near-term planning.
- Supporting / enforcement mechanisms: calendar `.ics` reader, time-block plan and `.ics` export, statistics, lexical knowledge retrieval, per-turn model choice and future feature vision.
- Closure path: calendar data influences present day-plan suggestions, while review facts inform a prompt; neither proves a separate prospective external adaptation option is promoted into enduring desktop organization policy.
- Why this is / is not agent-owned: near-term to-do ordering, model selection and historical progress summaries are not automatically a VSM S4 future-environment intelligence/strategic adaptation loop.
- Evidence: [Today planner](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/pages/today.py), [weekly review](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/review.py), [architecture and boundaries](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/docs/ARCHITECTURE.md).
- Basis: bounded negative examination of implemented planning, review and knowledge functions.
- Confidence: medium-high in this early version.
- Caveats: a future model-driven personal strategic planning feature could change this, but vision documents are not an active S4 return.

### Absence scope

- Surfaces inspected: read-only calendar, day-plan export, weekly comparison, facts/preferences memory, model picker, knowledge connectors and vision roadmap.
- Plausible first-party paths checked: long-term plan suggestion, outside model/dependency sensing, workload adaptation from review statistics and user-confirmed plan export.
- Why no material first-party path remains: found paths regulate today's commitments or recall past/internal facts, without a distinct externally prospective options loop that changes ongoing capabilities or strategy.

## S5 — Policy and identity

- State: —
- Function: no identity/ethos-level decision issue and legitimate binding policy return were shown inside the installed desktop agent's operating organization.
- Disturbance / variety regulated: future disputes about permissible autonomy, personal data and whether this assistant should prioritize speed or privacy may require ultimate human policy.
- Decisive decision or feedback right: the owner can set approval scope, deny a tool and remove personal memories; these are safety/privacy and local tool rights, not demonstrated adjudication of an identity-level charter.
- Decision owner: ultimate user values and project identity remain outside the first-party runtime governance loop.
- Supporting / enforcement mechanisms: approval cards, folder/session permission settings, local memory deletions, plugin sandbox declarations and security/trust documentation.
- Closure path: user grants or denies current operations and future calls obey the grant; no evidenced identity-level debate is decided and returned as binding ultimate policy across the personal agent's scope.
- Boundary reachability: first-party permission controls and memory deletion are real, yet no distinct ultimate identity/constitutional question is raised and closed by the shipped system.
- Why this is / is not agent-owned: user final veto is necessary safety governance but not evidence of S5(P); an identity-level closure needs more than persistent preferences or 'Always allow' tools.
- Evidence: [approval UI](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/approval.py), [local memory](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/app/memory.py), [security boundaries](https://github.com/RealNarcissus/mantel/blob/0b8d577e9401f3fcdf1349b7c72288de82eff792/SECURITY.md).
- Basis: bounded negative source review, distinguishing identity-level policy from current permission and privacy administration.
- Confidence: medium-high for missing organizational S5 at this recursion.
- Caveats: the human user may independently make life/ethical policy decisions, but they are not shown as a Mantel-wired S5 return path.

### Absence scope

- Surfaces inspected: approval ladder and Pi extension, Gemini tool gate, local memories and preference conflicts, plugin permission metadata, engine choice, personal settings and security guide.
- Plausible first-party paths checked: persistent 'allow in folder' policy, revocation/delete memory, user mode selection, model-provider switching and human approval on sensitive commands.
- Why no material first-party path remains: these are task/tool authorization and user preference controls; they do not decide a recognized ultimate-purpose conflict and return a new binding organizational charter.

## Distributed OSS parent arrangement

Maintainers' release/test roadmap and the external Pi/provider organizations are outside the installed desktop's own S5. The human is a real S3 parent controller for current personal work, while no project-identity adjudication workflow is credited merely from that ownership.

## Self-hosted and non-human modes

Mantel runs on Linux and can connect to Pi using the user's local model credentials or use a configured Gemini API key. Due schedule prompts are started automatically while GTK is running, one at a time; a closed app does not continue cron work. User approvals remain binding for higher-risk writes/commands, and fake API/demo runs do not establish live autonomous delivery quality.

## Recursion

The personal work portfolio has repeated independent conversations across time, but Mantel does not grant every conversation separate coordinated multi-agent work-cell identity. There is one model-operating tool loop and a user metasystem for current commitments; no independently justified autonomous S2/S4/S5 recursion is inferred.

## Variety and escalation

Model/tool choices, provider adapter swapping, scheduled prompts and local knowledge expand what work the desktop can attempt. Workspace path restrictions, pre-tool approvals, bounded tool steps, one-at-a-time due scheduler, visible actual diff and human steering attenuate mistakes. A denied tool returns an error into the turn; an interrupted conversation records the event for explicit human continuation.

## Evidence gaps

- The pinned 0.1.0 README explicitly says no full authenticated live-provider turn has been run end to end. Source and offline fake/protocol tests establish available construction, not production readiness.
- `GeminiAdapter` actually exposes `TOOLS` and `APPROVALS` despite outdated source/docstring statements that it is chat-only; this assessment follows callable runtime code while noting documentation drift.
- Multiple stored chats and serialized scheduled prompts do not demonstrate independently coordinated concurrent S1 agents; S2 stays absent.
- S3* depends on a person opening and acting on independent Git diff, and cannot guarantee all edits or correct code; this is human complementary audit, not a shipped independent adversarial reviewer.
- Future app vision and current planner/review/memory features do not provide a completed external-prospective S4 or organization-identity S5 loop.
