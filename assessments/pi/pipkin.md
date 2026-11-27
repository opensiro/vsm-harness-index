---
harness_id: pipkin
project_name: Pipkin
repository: https://github.com/garywu000/pipkin
review_ref: 46f759914189847d24cece8f1f42cb8de647a1ff
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Pipkin

## Review boundary

- System in focus: The installed Pipkin desktop workspace-agent application, including the unattended scheduled Work mode supplied by the same server.
- Purpose and identity: Carry out scoped work in selected folders and return reviewable workspace outputs or findings to the operator.
- Relevant environment: Local workspace files, operator requests, local Ollama inference, and optional public web or connected services within user grants.
- Standard-distribution boundary: The desktop launcher, first-party local server, Agent tools and task scheduler. Ollama supplies inference. Connected GitHub and Drive services own their external repositories and provider effects.
- Credited operating / distribution surfaces: Interactive Agent Work, confirmed scheduled Work, workspace tool dispatch, skill checks and results, and the scheduler control surface.
- Adjacent first-party surfaces excluded from ownership: Repository development instructions, release engineering, benchmarks and tests supply corroboration only. External maintainers and providers do not become Pipkin runtime actors.
- First-party operating / deployment modes considered: Interactive Ask first and Auto Work, read-only Work, optional explorer phase, unattended read/create schedules, and isolated connector turns.
- Recursion level: One installed application instance with independently requested workspace commitments. Scheduled work is a supported operating configuration with its own queue and current-control surface.
- Reviewed revision: [46f759914189847d24cece8f1f42cb8de647a1ff](https://github.com/garywu000/pipkin/tree/46f759914189847d24cece8f1f42cb8de647a1ff)
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The local server creates a Work agent over a workspace with mode-filtered tools, streamed outcomes and resumable state. The optional explorer has a restricted tool list for an early phase of that same Work run. Scheduled Work dispatches through the installed server's own endpoint. The scheduler records waiting, running and terminal outcomes. [Agent operating modes](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/README.md#L98-L116), [model and tools](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/agent.py#L3246-L3320), [unattended Work entry](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L1143-L1202), [busy handling and receipts](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/scheduler.py#L1182-L1255).

## Operational model

Each Work run pursues one user-authorized demand and consumes file/tool feedback. Separate foreground and scheduled Work have separately scoped requests and can contend for the same inference slot. The scheduled operator controls current commitments through the queue and inbox surface. The model makes task-local choices.

## S1 — Operations

- State: A
- Function: Produce or inspect workspace deliverables in response to a user task.
- Disturbance / variety regulated: Partial evidence, missing files, conflicting edits, tool failures and completion uncertainty inside a Work run.
- Decisive decision or feedback right: Choose a bounded next tool action, consume its outcome, repair an incomplete result or return output.
- Decision owner: The model-driven Work agent owns the ordinary action choice in supplied Auto Work. The operator owns workspace and permission grants.
- Supporting / enforcement mechanisms: Scoped workspace, filtered tool schemas, task checks and deterministic effect dispatch.
- Closure path: The server runs the supplied Agent loop, returns tool observations to the model, emits the result and preserves saved output and checkpoints.
- Boundary reachability: The desktop Work entry wires the model request and workspace tools in the shipped distribution. Scheduled Work calls the same endpoint with a narrower access mode.
- Why this is / is not agent-owned: Ask first approvals, connector confirmations and deterministic order do not remove the supplied Auto Work path for ordinary workspace actions.
- Evidence: [model and tools](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/agent.py#L3246-L3320), [completion and check feedback](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/agent.py#L3402-L3459), [unattended Work entry](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L1143-L1202), [tool outcomes](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/agent.py#L3540-L3607)
- Basis: Pinned first-party implementation and supported operating modes.
- Confidence: High.
- Caveats: No claim that arbitrary shell or external connector effects are autonomously authorized.

## S2 — Coordination

- State: C
- Function: Attenuate collision between independent workspace Work demands sharing one inference admission slot.
- Disturbance / variety regulated: Foreground or earlier Work can hold inference when a separately authorized scheduled job becomes due.
- Decisive decision or feedback right: Supply busy/defer/retry/skip precedence over prospective overlapping Work.
- Decision owner: The first-party constructor supplies fixed priority and retry rules. The executing model does not revise this relationship.
- Supporting / enforcement mechanisms: One generation gate, scheduler busy predicate and persisted waiting reasons.
- Closure path: A 409 or occupied slot returns to the scheduler as a waiting condition. It retries when available or records a skip and advances the schedule.
- Boundary reachability: Both work sources converge on the shipped gate and the scheduler consumes its feedback without an external orchestrator.
- Why this is / is not agent-owned: An explicit Work-to-Work interference relationship is supplied. Autonomous agreement or revision of the coordination policy is not established.
- Evidence: [shared inference admission](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L3486-L3494), [due planning and deferral](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/scheduler.py#L1115-L1172), [busy handling and receipts](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/scheduler.py#L1182-L1255), [scheduler wiring](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L1260-L1268), [scripted busy cases](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/tests/test_scheduler.py#L523-L555)
- Basis: Pinned competing-entry points, contention return and deterministic test assertions.
- Confidence: High.
- Caveats: The read-only explorer phase is part of one run and is not the second S1 witness.
- Distinct S1 units: Separately requested foreground Work and an already-authorized, independently dispatched scheduled Work occurrence.
- Inter-S1 disturbance: Both can demand the server's single active model generation slot, including while scheduled Work is already due.
- Attenuating coordination relation: Defer due Work while the shared slot is occupied and retry on a later tick; a timed-out wait receives a terminal skip.
- Feedback into subsequent S1 behaviour: A scheduled invocation starts when the slot is available or its next occurrence is advanced after recorded contention.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The same generator mediates two independent commitments and the busy outcome explicitly reschedules one of them.

## S3 — Inside-and-now control

- State: P
- Function: Oversee the current portfolio of scheduled Work commitments and intervene across scheduled units.
- Disturbance / variety regulated: Queued, late, blocked or currently running scheduled Work can conflict with the operator's current priorities.
- Decisive decision or feedback right: Decide whether to stop the running scheduled job, change which existing task runs now, or pause automatic starts across the schedule.
- Decision owner: The legitimate installed operator in the supported scheduled-Work supervision mode.
- Supporting / enforcement mechanisms: Schedule state/inbox endpoints, persistent pause and task settings, scheduler wake and current stop signal.
- Closure path: Current schedules, running status and queued overrides are displayed. Operator actions feed back into the scheduler and change dispatch or stop the current Work.
- Boundary reachability: The installed schedule API exposes the portfolio state and applies pause, run-now and stop on the same scheduler that dispatches Work.
- Why this is / is not agent-owned: The scheduler provides a global view of queued scheduled commitments. The operator selects interventions, while the scheduler follows fixed rules and the model sees only its current task.
- Evidence: [schedule state](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L1057-L1074), [operator actions](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L2743-L2778), [queue/stop state](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/scheduler.py#L1078-L1101), [due planning and deferral](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/scheduler.py#L1115-L1172), [unattended Work entry](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L1143-L1202)
- Basis: Current state, attributed intervention authority, and runtime return in the shipped schedule mode.
- Confidence: Moderate.
- Caveats: This positive path is bounded to the scheduled-Work portfolio. A model-owned cross-run controller covering interactive clients is not established.
- Whole-system current view: Within the scheduled operating configuration, current running task and progress, waiting/manual queue, task states, due times and terminal receipts.
- Current-control decision scope: Stop current scheduled Work, choose an existing commitment to dispatch now or pause automatic dispatch for the portfolio.

## S3* — Complementary audit

- State: —
- Function: No distinct owner of complementary audit of Pipkin Work is supplied in the examined modes.
- Disturbance / variety regulated: Ordinary Work output or connector effect claims may be wrong.
- Decisive decision or feedback right: No separate system-owned audit and return over Work findings established.
- Decision owner: No qualifying supplied audit actor.
- Supporting / enforcement mechanisms: Workspace checks and the PR review snapshot guard local completion and connector merge.
- Closure path: No distinct audit finding path into the scheduled portfolio or interactive current control was found.
- Why this is / is not agent-owned: Workspace skill checks run at the completing agent's own finalization. GitHub review is the connector's exact-head preparation for a requested merge.
- Evidence: [completion and check feedback](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/agent.py#L3402-L3459), [PR review inputs](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/github_workflows.py#L183-L223), [merge preflight](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/github_workflows.py#L708-L732), [schedule state](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L1057-L1074)
- Basis: Bounded source absence after examining likely verification surfaces.
- Confidence: Moderate.
- Caveats: A user may inspect a result independently, but the supplied modes do not designate a separate complementary audit decision.

### Absence scope

- Surfaces inspected: Agent finalization, skill checks, connector review and merge, schedule inbox and current state.
- Plausible first-party paths checked: Separate checks of file claims, primary PR patch/check retrieval, possible supervisory review of the scheduled portfolio.
- Why no material first-party path remains: Checks return to the same Work completion or connector merge action. The inbox reports the standard Work receipts and supplies no separate audit dispatch, judgment and return.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied prospective adaptation loop changes the workspace harness's future operating capability.
- Disturbance / variety regulated: Model availability, product releases, and external changes can affect future work.
- Decisive decision or feedback right: No assessment-to-option-to-adoption right over future harness capability established.
- Decision owner: No qualifying runtime S4 owner identified.
- Supporting / enforcement mechanisms: Local model selection, product updates and saved skills/schedules are adjacent candidate paths.
- Closure path: No first-party present-to-future inquiry and return to capability across the examined operating modes.
- Why this is / is not agent-owned: The updater verifies externally authored releases. Work can research a user task and persist instructions, but those paths do not jointly supply prospective system adaptation.
- Evidence: [Agent operating modes](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/README.md#L98-L116), [permissions and updates](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/README.md#L157-L164), [signed release staging](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/updater.py#L434-L502), [schedule approval](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/agent.py#L2524-L2553), [due planning and deferral](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/scheduler.py#L1115-L1172)
- Basis: Bounded source absence over runtime and update paths.
- Confidence: Moderate.
- Caveats: Manual configuration can change future tasks without an S4 organizational loop.

### Absence scope

- Surfaces inspected: Model settings and explorer configuration, saved skills, scheduler proposal and update staging.
- Plausible first-party paths checked: Prospective model/capability selection, user-approved scheduled changes, research-as-Work and signed update adoption.
- Why no material first-party path remains: The product consumes selected settings and maintainer releases. It does not develop and adjudicate future capability options from externally sensed changes in a path returning to present control.

## S5 — Policy and identity

- State: —
- Function: No runtime closure of ultimate purpose or identity policy is supplied at the assessed recursion.
- Disturbance / variety regulated: Possible tension over workspace authority, automation grants and provider access.
- Decisive decision or feedback right: No identity-level issue, owner decision and return to subsequent operation established.
- Decision owner: The operator supplies local grants and the maintainer owns distribution policy at adjacent recursion.
- Supporting / enforcement mechanisms: Workspace grants, approval cards, modes and connector controls.
- Closure path: These apply scoped authorization choices to operations without closing a runtime identity or ultimate-policy issue.
- Why this is / is not agent-owned: Choosing access for an individual Work or schedule is an operational boundary decision.
- Evidence: [permissions and updates](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/README.md#L157-L164), [schedule approval](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/agent.py#L2524-L2553), [operator actions](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L2743-L2778), [connector boundary](https://github.com/garywu000/pipkin/blob/46f759914189847d24cece8f1f42cb8de647a1ff/server.py#L3457-L3489)
- Basis: Bounded source absence across distribution and runtime authority paths.
- Confidence: Moderate.
- Caveats: This finding does not deny maintainer governance or user ownership of local resources.

### Absence scope

- Surfaces inspected: Workspace and shell permissions, schedule settings/actions, connector grants, release signature policy.
- Plausible first-party paths checked: App-parent policy workflow, task approval as policy closure, durable runtime identity decision.
- Why no material first-party path remains: All inspected choices concern grants, individual schedules, tool constraints or external distribution. No supplied path escalates an ultimate identity/policy issue and binds subsequent Work to its resolution.

## Recursion

Workspace sessions and scheduled commitments are operational units here. The optional read-only model phase is part of the same Work run. No independently viable nested workspace organization is established.

## Variety and escalation

Tool feedback, resource deferral, time/step bounds and user review absorb different disturbances. Current supervision uses schedule state and explicit operator actions. The checks and locks enforce scope and receipt semantics without becoming the decision owner.

## Evidence gaps

Pinned source and repository tests were inspected. No desktop app session, live model run or connected third-party operation was executed. Scheduled S3 evidence is limited to the supplied portfolio mode. The audit finding does not extend to user-assembled independent reviews.
