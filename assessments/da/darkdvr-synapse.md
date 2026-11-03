---
harness_id: darkdvr-synapse
project_name: Synapse
repository: https://github.com/DarkDvr/Synapse
review_ref: b91345750a7d8ec1fca1557cdf33613762794223
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: —
---

# Synapse (DarkDvr)

## Review boundary

- System in focus: The shipped Windows Synapse software-building application, including the role/session orchestration that Synapse owns above the included OpenCode model/tool engine; not the developer organization.
- Purpose and identity: Build a project from operator-approved requirements with an Architect, specialist workers, separate quality checks and recorded acceptance/repair decisions.
- Relevant environment: Operator, Windows project directory, model providers, installed or vendored OpenCode engine, user-requested functionality and actual code/rendered application outputs.
- Standard-distribution boundary: `Synapse.exe` shell, Node backend, OpenCode HTTP/SSE adapter, project plan/run ledger, `src/runs.js` delegation controller, per-role prompts and isolated role folders.
- Credited operating / distribution surfaces: [README](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/README.md), [runs.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/runs.js), [plans.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js), [OpenCode adapter](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/engines/opencode.js), [delegate MCP](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/mcp/delegate-server.js).
- Adjacent first-party surfaces excluded from ownership: Development tests, packaging scripts and the upstream maintainer roadmap do not own runtime regulation. OpenCode upstream's general-purpose governance and model providers are also outside the focused project boundary; Synapse's bundled engine is credited only where wired into shipped first-party roles.
- First-party modes considered: Single agent mode; Multi mode with configured Architect/Inventor/Designer/Coder/QC roles, operator approval of feature scope, optional `Keep building` between delegated tasks.
- Recursion level: One Synapse-managed software project, with individual role-specific implementation tasks as S1 units and the Architect's project-level control as metasystem.
- Reviewed revision: `b91345750a7d8ec1fca1557cdf33613762794223`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Synapse starts a real OpenCode engine in an isolated home, bridges sessions/models/tool events over HTTP/SSE, and installs a first-party `delegate` MCP request that the Architect may call. `src/runs.js` reads that tool call from the live transcript, creates a separate role-owned session, executes it on the configured model, records actual written files/result, and injects a synthetic report into the Architect session. The model-owned `plan.json` is joined with the host-owned `runs.jsonl`, deliberately preventing worker success claims from becoming completed commitments automatically. The source documents completed multi-role operation but this review did not re-run a Windows model-provider session. [README](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/README.md#the-project-plan-and-the-pipeline), [runs.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/runs.js#L546), [plans.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js).

## Operational model

An individual coder/designer/inventor/QC role is a task-level unit that uses the engine's model/tool loop to produce a file, test or finding. The Architect is a distinct model session that maintains the whole project plan and revises commitments after seeing grounded worker reports. User-scope feature selection, permission decisions and `Keep building` state constrain activity but are not treated as agent-owned organizational discretion.

## S1 — Operations

- State: A
- Function: Autonomous local production and checking of a specific delegated project deliverable.
- Disturbance / variety regulated: Ambiguous requirements, codebase/tool errors, rendered defects and incomplete subtasks encountered during task execution.
- Decisive decision or feedback right: Role model chooses its own next implementation/test tool after observing results.
- Decision owner: Role-specific model agent, reached through Synapse-created engine session; human owns separate scope/permission gates.
- Supporting / enforcement mechanisms: OpenCode adapter, per-role tool rules, session brief, tool transcript, provider retries, bounded worker runner and written-artifact ledger.
- Closure path: Model tool call→real engine execution→tool feedback→continuing role turn→worker report/files, then return to Architect.
- Boundary reachability: Shipped Multi mode makes genuine model-backed role sessions rather than invoking a development mock.
- Why this is / is not agent-owned: The role's model has task-sensitive tool/repair choice; Synapse supplies the enclosing execution and evidence channel.
- Evidence: [OpenCode adapter](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/engines/opencode.js), [runs.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/runs.js#L1000), [plans.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js#L650).
- Basis: structural
- Confidence: high on reachable code path; no independent Windows-provider execution.
- Caveats: Actual model quality, installed/packaged engine availability and end-to-end completion were not live-tested.

## S2 — Coordination

- State: —
- Function: Feedback-based regulation of interference or oscillation among operational S1 task agents.
- Disturbance / variety regulated: Concurrent edits, shared project plan corruption and worker cross-role overwrite risks.
- Decisive decision or feedback right: No specific agent-owned inter-worker collision detection→mediation→returned adjustment evidenced.
- Decision owner: Deterministic harness serialization and folder rules; Architect decides task sequence as S3 commitment, not evidenced as S2 conflict mediation.
- Supporting / enforcement mechanisms: One-active-worker `busy` guard per project, `roleWriteRules`, plan ownership, role folders and assignment ladder.
- Closure path: Serial admission and static write rules prevent some conflicts but do not inspect actual inter-unit interference and negotiate mutual change.
- Why this is / is not agent-owned: Transport, isolation and top-down task allocation alone are insufficient for S2 at this recursion.
- Evidence: [runs.js#L546](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/runs.js#L546), [plans.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js).
- Basis: structural
- Confidence: medium-high for the reviewed first-party orchestration paths.
- Caveats: A model could discuss competing tasks in an individual session, but no reusable S2-specific interference closure was established.

### Absence scope

- Surfaces inspected: Worker concurrency controls, role authorization, delegation queue/ledger, plan statuses, current automation modes and worker recovery.
- Plausible first-party paths checked: Per-project serialization, coders' failure ladder, plan ownership, worker handoff, shared files and error reports.
- Why no material first-party path remains: Those enforce prior task ownership or S3 sequential commitment; none converts a measured inter-S1 clash into a specific coordination adjustment fed back to the affected units.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: Architect reads the project-wide `plan.json` task statuses, blocked items, confirmed features and per-worker completion reports grounded in `runs.jsonl` and actual file/tool records.
- Current-control decision scope: Architect alone accepts/rejects task completion, alters the whole plan and selects corrective work and next role commitments within approved project scope; a runner's retry/backoff merely enforces constraints.
- Function: Current project-wide commitment, progress and corrective task regulation.
- Disturbance / variety regulated: Partial deliverables, faulty worker claims, blocked tasks, failed providers, scope drift and new defects threatening the approved project goal.
- Decisive decision or feedback right: Judge each reported worker outcome, update the plan, mark done/retry/blocked, reprioritize or delegate the next current task.
- Decision owner: Model-driven Architect in Multi mode, constrained by operator-approved features and optional automatic continuation.
- Supporting / enforcement mechanisms: `plan.json` as Architect-only authority, actual `runs.jsonl`, injected post-worker report, task-role assignment, retry fallback, progress/status rail.
- Closure path: Worker run evidence→synthetic report→Architect evaluation/update of plan→next delegate or required operator escalation; `Keep building` enables continuation, while off returns after each judged task.
- Boundary reachability: `delegate` MCP, run ledger, `handleTurn`, `report` and `wake` are connected in shipped Multi mode.
- Why this is / is not agent-owned: Removing the Architect leaves recorded runs and deterministic stops but not discretionary whole-project acceptance, replanning or corrective commitment.
- Evidence: [runs.js#L2741](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/runs.js#L2741), [plans.js#L1270](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js#L1270), [delegate MCP](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/mcp/delegate-server.js).
- Basis: structural
- Confidence: medium-high; project-control closure is code-visible, not a live success claim.
- Caveats: An operator can pause or steer a task, but the documented toggles do not independently establish a distinct parent-governed S3 decision mode.

## S3* — Complementary audit

- State: A
- Claim being audited: Implementing worker's claim that the shipped build is usable, faithful to approved design and free of target regressions.
- Ordinary reporting path: Coder sends its own transcript, modified-file list and completion statement to Architect through `runs.jsonl` and the synthetic result message.
- Complementary access path: Separate QC model role uses the delivered application, renders/screenshots UI, diffs approved mock, tests unusual inputs and writes reproducible findings with IDs independently of worker prose.
- Independence boundary: QC has its own configurable model/session and role folder; it cannot edit the build and coders cannot write the QC findings folder under Synapse's first-party role rules. This is role separation, not tamper-proof institutional independence.
- Who acts on findings: Architect reads QC output and delegates the numbered fix to a coder, then assigns verification of that exact repro to QC again, up to the three-round cap.
- Function: Independent role-level challenge to implementation claims using real build behavior and a returned quality verdict.
- Disturbance / variety regulated: Worker reports that conceal unusable UI, clipping, misleading states, poor validation or regressions.
- Decisive decision or feedback right: QC chooses and executes adversarial/use-oriented checks, records reproducible findings and re-verifies fixes separately from implementing coders.
- Decision owner: Dedicated configured `qc` model/session, distinct from coder role, with its own findings area and read-only stance toward the build.
- Supporting / enforcement mechanisms: QC mandate to render/use the built artifact, screenshot/mock diffs, finding IDs and repros, separate folder permissions, bounded three-round QC/fix/verification plan.
- Closure path: QC direct inspection→`qc_findings/qc-N.md` with evidence→Architect receives report and assigns specific fix task→QC re-runs repros and verifies correction.
- Boundary reachability: First-party QC role, delegated real engine session, report loop and role-write restrictions are shipped in Multi mode.
- Why this is / is not agent-owned: QC independently determines and reports actual product defects; the Architect, not QC, retains current-control commitment changes.
- Evidence: [plans.js#L700](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js#L700), [plans.js#L1342](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js#L1342), [runs.js#L1002](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/runs.js#L1002).
- Basis: structural
- Confidence: medium: independently tasked source-visible QC path, with no performed cross-provider execution or efficacy audit.
- Caveats: The product does not establish strong organizational or cryptographic isolation; different role/model configuration and artifact-based repro constitute the limited claimed independence. If QC is never delegated in a particular plan, the optional path is inactive.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Sensing external/future needs and developing options returned to current project capability.
- Disturbance / variety regulated: Unanticipated user needs and future features for the product under construction.
- Decisive decision or feedback right: An Inventor model proposes and ranks extra features; operator chooses scope and Architect links confirmed features to tasks. Whether this amounts to an external sensing→adaptation→S3 loop is unresolved.
- Decision owner: Inventor generates options and operator accepts features; no proved future-environment evidence trail connecting the two.
- Supporting / enforcement mechanisms: Inventor role mandate, optional local search tools, ideas file, confirmed/rejected `features.json` and Architect planning instructions.
- Closure path: Proposed feature→human selection→confirmed feature/task is explicit; source does not establish that the proposal derived from an observed external prospective distinction rather than imagined additions to a current wish.
- Why this is / is not agent-owned: Generating project feature ideas is not, alone, a demonstrated VSM S4 process; the active inventor path prevents a defensible categorical absence claim.
- Evidence: [plans.js#L660](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js#L660), [plans.js#L1287](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js#L1287), [README](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/README.md#the-project-plan-and-the-pipeline).
- Basis: structural
- Confidence: bounded uncertainty.
- Caveats: Direct evidence of actual external future-condition observation and its governing choice would resolve the state; neither was reproduced at this source pin.

## S5 — Policy and identity

- State: —
- Function: Legitimate ultimate-policy or system identity dispute resolution at project recursion.
- Disturbance / variety regulated: Conflicts over project identity, ultimate purpose and governing policy rather than current task scope.
- Decisive decision or feedback right: No first-party identity-level issue→authority decision→returned governing policy path shown.
- Decision owner: Human operator chooses product features, permission and continuity toggles; those remain operational/requirement decisions.
- Supporting / enforcement mechanisms: Feature selection forms, prompt constraints, role-specific permission rules and operator approval.
- Closure path: Scope selection reaches project plan, but no recognized ultimate-policy decision channel governs a dispute about the system's identity.
- Why this is / is not agent-owned: Choosing which mock to build or whether to continue is not an S5 legitimacy mechanism.
- Evidence: [plans.js#L1287](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/plans.js#L1287), [automation.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/automation.js), [permissions.js](https://github.com/DarkDvr/Synapse/blob/b91345750a7d8ec1fca1557cdf33613762794223/src/permissions.js).
- Basis: structural
- Confidence: medium-high.
- Caveats: External real-world product governance or developer organizational decisions are out of the assessed standard-distribution boundary.

### Absence scope

- Surfaces inspected: Architect planning rules, feature contract/forms, role permissions, automation, engine config and operator stop controls.
- Plausible first-party paths checked: Feature approval/rejection, user scope change, security permissions, human model selection and operator stop/continue.
- Why no material first-party path remains: All identified decisions concern current requirements or execution authority; none closes a distinct legitimate identity/ultimate-policy dispute into product operation.

## Recursion

Task agents are operational units within a project-level Architect-managed system; no complete higher-order portfolio VSM or self-governed project-of-projects is inferred from the sidebar.

## Variety and escalation

Stop and operator hold guard against runaway work; failed workers trigger bounded retry/model-ladder decisions and report actual files rather than trusting claimed completion. Blocked tasks and QC findings reach the Architect or operator, without granting every alert a separate VSM function.

## Evidence gaps

No Windows runtime/model execution, UI use, or independent outcome assessment was performed. In particular the structural existence of QC does not guarantee effective adversarial findings; S4 remains unresolved rather than guessed. All results concern the frozen AGPL-3.0-only repo snapshot.

## Verdict

**Include.** Synapse exposes first-party multi-role project execution, model-owned current project control and a separate artifact-based QC inspection/return path. S2 and S5 have bounded negative scope; S4 is deliberately unresolved because feature invention and operator selection alone do not prove environmental/prospective adaptation.
