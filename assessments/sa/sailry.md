---
harness_id: sailry
project_name: Sailry
repository: https://github.com/sailry/sailry-harness
review_ref: eaad1b7f18e448c8c4e9e9286e19560c8a351ae1
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Sailry

## Review boundary

- System in focus: the shipped Rust Sailry desktop/mobile-controlled Host agent runtime, with first-party model/tool turns and its optional Flagship model-led team of subagents.
- Purpose and identity: perform user-authorized coding, browsing, office and project actions on a local or remote Host, optionally dividing a coding task among concurrent child agents.
- Relevant environment: project files and worktrees, user requests, competing child edits, model/provider availability, run errors, host connectivity and permission boundaries.
- Standard-distribution boundary: Sailry Host's node runtime, agent loop, native desktop/mobile session control, tools, permissions, model-provider adapters and built-in Flagship mode; external LLM providers are dependencies rather than owner of Sailry orchestration.
- Credited operating / distribution surfaces: Host model/tool execution, documented Standard/Plan/Flagship modes, registered delegation tools, child admission/status/guidance and model-led task-wave integration.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests and release machinery, separate community plugin/theme repositories, third-party models, downloaded model-score data and generic developer administration.
- First-party operating / deployment modes considered: local and remote Host; desktop/mobile client; Standard direct agent, Plan read-only mode, optional Flagship team mode; bounded child-concurrency and permissions.
- Recursion level: an individual project session in one Host, whose Flagship parent coordinates multiple child operational sessions; multiple Hosts under one desktop do not by themselves form a higher VSM organization.
- Reviewed revision: `eaad1b7f18e448c8c4e9e9286e19560c8a351ae1`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The first-party Node runs a worker pool that claims conversations and invokes a model/tool execution engine. Models select actions through registered coding, terminal, browser and other tools, with session-scoped permissions and tool feedback. In Flagship mode, a parent model receives a first-party coordination prompt and registered `spawn_agent`, `guide_agent` and `wait_agent` tools. Each child receives a separately admitted session with its own scoped task, model/role, durable status and final response; the parent may inspect results, redirect a child and run consolidated verification. Worktrees can isolate writable surfaces, but they are not automatically created for every child. [runtime](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent.rs), [Flagship mode](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/prompt/modes.rs), [delegation tools](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/delegation/tools.rs).

## Operational model

Normal mode is one model-governed S1 agent. In the explicitly shipped Flagship mode, independent model-backed children execute different coding or investigative slices. The lead model is asked to allocate disjoint writable scopes, isolate concurrent worktrees if needed, assign read-only review roles, collect outcomes, integrate shared files and send failed consolidated checks back to the owning child. This is more than forwarding tool calls: the parent agent decides the contention-avoidance plan and revises actual child work after observing results. The same lead also has a narrow S3 current-control role over the **whole task wave**, not over every concurrent Sailry user, Host or account. There is no demonstrated independent S3* auditor, S4 future-environment option cycle, or S5 ultimate-identity decision return.

## S1 — Operations

- State: A
- Function: model-controlled user task execution over first-party project, terminal, browser and other tool surfaces.
- Disturbance / variety regulated: changing repository contents, tool failures, ambiguous requests, project-specific instructions and provider responses.
- Decisive decision or feedback right: model chooses next available tool and arguments from current conversation and returned observations, including when to finish or delegate in supported modes.
- Decision owner: model operating within Sailry's first-party Host agent session; platform sets tool and permission limits.
- Supporting / enforcement mechanisms: model integration, tool catalog, captured modes and permissions, persistent session state, execution workers, approval flow.
- Closure path: user/host session task → model reasoning → first-party tool execution → observed result/error → subsequent model choice or final response.
- Boundary reachability: documented `Create session` on local/remote Host starts the shipped Node runtime, rather than outsourcing the loop to an external coding harness.
- Why this is / is not agent-owned: model owns discretionary tool/action selection inside developer/user constraints.
- Evidence: [README Host loop and features](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/README.md), [Node execution](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent.rs), [session/project operation](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/docs/projects.md).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: source-backed capability, not a live provider/API end-to-end exercise.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrently working child S1 agents by assigning non-overlapping writable scopes and sequencing shared integration.
- Disturbance / variety regulated: competing child edits to the same files, shared module lists/manifests and test runs on inconsistent integrated output.
- Decisive decision or feedback right: Flagship parent model chooses a division into disjoint owned files or worktrees, retains shared registration files, delegates roles, and reassigns follow-up fixes based on observed conflicts and consolidated checks.
- Decision owner: the first-party Flagship parent model, instructed by a shipped coordination policy; bounded child admission is deterministic infrastructure.
- Supporting / enforcement mechanisms: `spawn_agent` task brief with owned paths, optional registered worktrees, `guide_agent`, child result collection, concurrency budget and integration prompt.
- Closure path: parent observes task and possible shared-file collision → model assigns disjoint edits/worktrees to children → independent children act → parent integrates outcomes and feeds corrective tasks to specific children.
- Boundary reachability: selecting shipped Flagship mode registers child tools inside an ordinary Sailry Host conversation; no custom downstream product is needed.
- Why this is / is not agent-owned: the coordination choice (who edits which conflicting slice and how to reconcile) is the lead model's, while the queue itself is a fixed controller, not the basis of `A`.
- Distinct S1 units: separately admitted model-backed child sessions with separate roles, tasks, status and results.
- Inter-S1 disturbance: concurrent writes to overlapping source files/worktrees and competing verification could invalidate the project build or another child's changes.
- Attenuating coordination relation: parent-created disjoint ownership/worktree assignment, parent retention of shared files, and one consolidated verification/integration wave.
- Feedback into subsequent S1 behaviour: child outputs and test failures are gathered by the parent, which can send `guide_agent` to the owning child or assign a next wave.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the shipped policy names a concrete inter-agent write collision and gives the parent a model-selected isolation and correction policy, beyond merely launching several generic workers.
- Evidence: [Flagship ownership and correction instructions](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/prompt/modes.rs), [spawn/guide operational contract](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/delegation/tools.rs), [child control](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/delegation/control.rs).
- Basis: explicit coordination policy with structural child execution and feedback.
- Confidence: medium.
- Caveats: disjoint-file discipline is model-instruction based and not a hard source-file lock; default Standard/Plan sessions do not instantiate several S1 units.

## S3 — Inside-and-now control

- State: A
- Function: maintain current task-wave coherence across the Flagship team's child commitments and integrated test outcome.
- Disturbance / variety regulated: child work unfinished or failed, mismatched implementation slices, repeated expensive verification and combined build failures.
- Decisive decision or feedback right: lead model observes child completion/result, directs failed work to its owning child, keeps shared/integration edits itself and decides whether the combined task is acceptable.
- Decision owner: Flagship lead model in the same first-party parent session, at the task-team recursion level; Node's child state serves as feedback, not the decision owner.
- Supporting / enforcement mechanisms: returned durable child statuses/responses, `wait_agent`/`guide_agent`, explicit wave-level integration instructions and consolidated builds/tests.
- Closure path: admitted child status and final result → parent views work across the current team → model redirects/reconciles assignments → agent child work or shared-file edits → consolidated verification and final decision.
- Boundary reachability: Flagship and delegation control are compiled into supported Host agent operation; child roles and budget are captured in the parent context.
- Why this is / is not agent-owned: the lead model exercises team-wide present-task control and error correction; routine scheduling/queue accounting alone is not credited as S3.
- Whole-system current view: the parent receives the roster, concurrency budget, individual child status/results and consolidated project checks across the **bounded Flagship task team**.
- Current-control decision scope: the parent can retain or change shared integration steps, guide/reassign follow-up work to child sessions, and accept/reject the assembled result.
- Evidence: [Flagship parent oversight instructions](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/prompt/modes.rs), [delegation context and guide/wait](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/delegation/tools.rs), [child result/status feedback](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/delegation/control.rs).
- Basis: explicit task-team control policy and runtime status feedback.
- Confidence: medium.
- Caveats: scoped to one Flagship team's current workload, not product-wide host governance or autonomous organizational resource allocation; source review does not prove the model always follows the prompt.

## S3* — Complementary audit

- State: —
- Function: no demonstrated separate complementary audit right with independent evidence access and corrective return to S3.
- Disturbance / variety regulated: incorrect code or unsupported child claims may be found in optional review/testing, but these are not an independently constituted operational audit channel.
- Decisive decision or feedback right: Flagship parent can request a read-only reviewer or run tests; no separate obligatory auditor has independent access and corrective authority.
- Decision owner: same parent model arranges and accepts review results; developer tests and CI are adjacent validation.
- Supporting / enforcement mechanisms: role-matched read-only children, shared test suite, test/build output, approval UI.
- Closure path: task review or consolidated test output → parent may correct/redelegate; this remains inside ordinary task supervision.
- Why this is / is not agent-owned: a read-only delegated child does not alone prove an S3*-specific independent witness and feedback path.
- Evidence: [review delegation and verification instructions](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/prompt/modes.rs), [tool roles/permissions](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/delegation/tools.rs).
- Basis: bounded negative.
- Confidence: medium.
- Caveats: independently staffed review may be configured in a particular installation but was not verified as shipped complementary-audit authority.

### Absence scope

- Surfaces inspected: Flagship review prompt, child roles and permissions, result collection, approval UI, repository tests and ordinary tool checks.
- Plausible first-party paths checked: read-only child review, unit/build checks, optional human approval and logged tool observations.
- Why no material first-party path remains: review is parent-delegated and parent-adjudicated, while tests and approvals protect normal tool execution; no independent S3* audit constructor and return to current-control decision was found.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future-environment intelligence loop that evaluates adaptive operating options and feeds a capability choice back into S3.
- Disturbance / variety regulated: dynamic provider metadata and model scores help users select existing models, while browsing and research tools serve current tasks.
- Decisive decision or feedback right: user configures providers; task model can browse or search for immediate task purposes; no strategic adaptation authority is evidenced.
- Decision owner: user for model settings and task agent for in-task research, neither a shown S4 prospective owner.
- Supporting / enforcement mechanisms: models.dev/ModelDial catalog download, web tools, provider settings.
- Closure path: catalog data can inform model selection and tool research can solve the current request; no prospect → option → changed whole-system capability feedback path is shown.
- Why this is / is not agent-owned: external information alone is not an S4 future-facing organizational intelligence function.
- Evidence: [README model metadata and capabilities](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/README.md), [model settings](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/docs/models.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: prospective work can be manually requested of an agent but does not establish a persistent first-party organizational S4 owner.

### Absence scope

- Surfaces inspected: model/provider selection, project and Host docs, agent modes, web/research tools, model-ranking data and agent team controls.
- Plausible first-party paths checked: external model benchmark score updates, task research, scheduled goals and changing configured model providers.
- Why no material first-party path remains: no source establishes future-environment distinction and adaptation-option evaluation returning changed current-system capacity or policy.

## S5 — Policy and identity

- State: —
- Function: no evidenced ultimate-purpose/identity conflict adjudication and authoritative policy-return cycle.
- Disturbance / variety regulated: user/project trust, tool permissions, role selection and approval constraints restrict actions in a task.
- Decisive decision or feedback right: user grants/denies permissions and can revoke project trust; developer fixes tool and mode limits, but neither is a dedicated system-identity decision pathway.
- Decision owner: user/developer for ordinary configuration and consent; no separate ultimate policy owner operationally identified.
- Supporting / enforcement mechanisms: captured permission scopes, trust gate, role constraints, explicit stop/cancellation and project instructions.
- Closure path: permission denied/approved or trust revoked → current task action allowed/stopped; no identity-level conflict → authority → policy decision → returned organizational rule.
- Why this is / is not agent-owned: strong authorization gates are not an S5 policy-identity deliberation mechanism.
- Evidence: [project trust lifecycle](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/docs/projects.md), [mode authority separation](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/crates/node-runtime/src/agent/prompt/modes.rs), [README approvals](https://github.com/sailry/sailry-harness/blob/eaad1b7f18e448c8c4e9e9286e19560c8a351ae1/README.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: human controls legitimate use, but the first-party product supplies no evidenced identity-governance loop.

### Absence scope

- Surfaces inspected: session modes, tool permissions, project trust, parent-team configuration, desktop/mobile user approvals and Host control.
- Plausible first-party paths checked: revocation of project trust, parent/child tool restrictions, role and model choices, developer-supplied team instructions.
- Why no material first-party path remains: these are task-level scope/consent constraints, not an adjudication of ultimate system purpose or identity with a returned governing rule.

## Distributed OSS parent arrangement

Sailry can pair multiple independently executing Hosts and clients, but one user's client choosing among Hosts does not establish model-owned global S3–S5 across all Hosts. Repository maintainer community and upstream plugin distribution remain outside the operating boundary.

## Self-hosted and non-human modes

Every Host runs the first-party loop near local data. Standard direct use remains S1=A; Flagship supplies the additional A-rated task-team S2/S3 coordination/current-control witnesses. Approval and trust changes still belong to the human in ordinary supervised modes; no agent-owned S5 is inferred from them.

## Recursion

Children are operational S1 cells coordinated at a task-team recursion level by the Flagship lead. They need not each own full S2–S5 capabilities; Host topology and teams are separate dimensions.

## Variety and escalation

Agent tools observe errors, child sessions have durable queued/running/final status, and `guide_agent` can return failed integration work to its prior owner. Node concurrency limits attenuate scheduling load; they do not by themselves confer model-owned coordination. Rejected permissions go back to user intervention, not S5 conflict arbitration.

## Evidence gaps

No provider-connected end-to-end run or experimentally induced concurrent file collision was performed. The S2 and S3 states rely on explicit shipped Flagship agent instruction plus real child tool/state/feedback plumbing, with model compliance and broad whole-Host reach left unproven. No independent S3* actor or S4/S5 closure was established.
