---
harness_id: comet
project_name: Comet
repository: https://github.com/rpamis/comet
review_ref: 78b1b11ae75648c6f387e01d889f2ef097d6e8df
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Comet

## Review boundary

- System in focus: The Comet CLI, Runtime SDK, Native and Classic workflow applications and their shipped host integration for one local change or Supervisor run.
- Purpose and identity: Maintain confirmed change scope, workflow progress, evidence, recovery and acceptance for work performed by an agent host.
- Relevant environment: Local project and Git worktrees, operator approvals, host sessions and tools, repository outcomes and configured evaluation environments.
- Standard-distribution boundary: First-party business workflow engine, state and Action protocol, dashboard, checked-in Skills, workflow generation and evaluation control surfaces. Adjacent agent platforms provide operational agent execution.
- Credited operating / distribution surfaces: Native and Classic state transitions, SDK executors and Action claims, Supervisor worktree/dependency paths, approval/recovery, memory and Eval entry paths.
- Adjacent first-party surfaces excluded from ownership: External coding agents and external evaluator hosts, experimental archives, test fixtures and upstream project governance.
- First-party operating / deployment modes considered: Native and Classic interactive host workflows, Native Supervisor with external peers, fixed SDK applications, Eval and supported memory paths.
- Recursion level: One Comet-managed project change and any child change state. The host agent’s internal operation is an adjacent system.
- Reviewed revision: 78b1b11ae75648c6f387e01d889f2ef097d6e8df.
- Observation date: 2026-11-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Comet provides a resumable operational protocol with version-pinned workflow definitions, durable Action claims, approval/evidence waits, business validators and resumable archive. Native differs from Classic in workflow design and external Skill dependencies. In both cases the agent platform supplies the semantic task execution and tool decisions. SDK handlers execute declared deterministic actions or hand work to an external executor. Supervisor integration supplies ordered state and worktree constraints. Eval and memory supply useful ancillary functions, with external agent adapters or deterministic rules in the paths assessed.

Evidence: [README.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/README.md), [runtime-sdk.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/docs/architecture/runtime-sdk.md), [SKILL.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet-native/SKILL.md), [platform-execution.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet/reference/platform-execution.md), [run-agent-runtime.sh](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/eval/scaffold/shell/run-agent-runtime.sh).

## Operational model

The Builder and Verifier select and perform work in their host sessions. Comet can refuse invalid receipts and advance the relevant change or integrate child results after supported completion conditions. With the external sessions removed, the CLI retains state transitions, approval waits, fixed commands, evidence validation and persistence. It lacks an internal actor that interprets the request and owns the semantic Builder tool/result loop. The proposed disposition is exclusion from the general agentic corpus at this ref.

## S1 — Operations

- State: —
- Function: Determine whether the packaged runtime owns an autonomous unit that performs the commissioned project change.
- Disturbance / variety regulated: A changing codebase, mixed implementation choices and real check failures require task-level judgment.
- Decisive decision or feedback right: Interpret scope, choose substantive implementation and check actions, and decide subsequent work from results.
- Decision owner: External host Builder or Verify session.
- Supporting / enforcement mechanisms: Comet Action contracts, run state, SDK handlers, artifact validation and deterministic Git/recovery operations.
- Closure path: External agent performs work and submits evidence. Comet validates it and returns the next permitted phase or task. The semantic work loop closes in the host.
- Why this is / is not agent-owned: Comet Native ships its workflow without external Skill dependencies, but explicitly uses agent-platform tools and session identity for the work itself.
- Evidence: [SKILL.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet-native/SKILL.md), [platform-execution.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet/reference/platform-execution.md), [runtime-sdk.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/docs/architecture/runtime-sdk.md), [run-agent-runtime.sh](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/eval/scaffold/shell/run-agent-runtime.sh).
- Basis: structural
- Confidence: high
- Caveats: External Skill dependencies and the ownership of the actual agent engine are distinct engineering questions.

### Absence scope

- Surfaces inspected: Native and Classic run/verification paths, SDK workflow executor, Supervisor host and Eval adapters.
- Plausible first-party paths checked: Built-in Native, SDK handler dispatch, Supervisor children, and evaluation subjects.
- Why no material first-party path remains: Runtime’s built-in execution owns workflow effects. Its workflow declaration contains no model client and the evaluated agents run in external executors.

## S2 — Coordination

- State: —
- Function: Examine whether inter-unit work conflicts are resolved by autonomous units inside the Comet boundary.
- Disturbance / variety regulated: Dependent changes or overlapping edits can collide across child worktrees.
- Decisive decision or feedback right: Choose the actual scope split, delegated participants and deviation response.
- Decision owner: Supervisor coordinator and workers in host sessions.
- Supporting / enforcement mechanisms: Confirmed child DAG, readiness, separate worktrees, integration ordering and repair actions.
- Closure path: Comet blocks or returns repair steps and integrates accepted results in declared order. Host agents decide how to handle the substantive conflict.
- Why this is / is not agent-owned: The isolation and dependency protocol is first-party. The autonomous participants and discretionary coordinator reside outside the indexed Comet boundary.
- Evidence: [SKILL.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet-native/SKILL.md), [native-sdk-supervisor-plan.ts](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/domains/comet-native/native-sdk-supervisor-plan.ts), [native-sdk-supervisor-integrate.ts](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/domains/comet-native/native-sdk-supervisor-integrate.ts), [platform-execution.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet/reference/platform-execution.md).
- Basis: structural
- Confidence: high
- Caveats: The excluded disposition does not collapse Comet's coordination functionality into generic message transport.

### Absence scope

- Surfaces inspected: Native Supervisor plan, child worktree constraints, integration and platform execution contract.
- Plausible first-party paths checked: Semantic overlap/dependency decisions, host dispatch, ordered integration conflicts and repair.
- Why no material first-party path remains: First-party deterministic interference attenuation is real; no first-party autonomous S1 units supply an in-boundary organizational S2 loop for this general assessment.

## S3 — Inside-and-now control

- State: —
- Function: Check whether Comet owns a whole-current discretionary decision over the commissioned change.
- Disturbance / variety regulated: Host execution may be interrupted, failed, blocked or stale while other child work exists.
- Decisive decision or feedback right: Decide which implementation, current commitment and recovery route to pursue when several alternatives are possible.
- Decision owner: Host coordinator and authorized user at their respective decision surfaces.
- Supporting / enforcement mechanisms: Run view, typed actions, failure and approval waits, decision validation, integration and reconciliation.
- Closure path: Host and user choices return to the first-party run state, which enforces their transition limits.
- Why this is / is not agent-owned: The code exposes meaningful current-state control paths around external work. It does not supply the operating agentic cell on which to publish a general positive grade here.
- Evidence: [runtime-sdk.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/docs/architecture/runtime-sdk.md), [platform-execution.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet/reference/platform-execution.md), [native-sdk-verify-decision.ts](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/domains/comet-native/native-sdk-verify-decision.ts).
- Basis: structural
- Confidence: high
- Caveats: Formal continuation states do not establish packaged autonomous control ownership.

### Absence scope

- Surfaces inspected: Native SDK decisions, Supervisor, dashboard references, approval and interrupted execution contracts.
- Plausible first-party paths checked: Whole-run observability, recovery actions, confirmation/acceptance and blockers.
- Why no material first-party path remains: The runtime records and constrains executed decisions. Discretionary intervention is supplied by the adjacent coordinator or user, and the general first-party S1 boundary is unmet.

## S3* — Complementary audit

- State: —
- Function: Determine who independently checks Builder evidence and changes the disposition.
- Disturbance / variety regulated: An implementation report can omit requirements, reuse stale checks or describe an unbuilt result.
- Decisive decision or feedback right: Inspect original requirements and candidate evidence to accept or return a specific repair.
- Decision owner: Host Verifier when independent review is requested or required.
- Supporting / enforcement mechanisms: Separate Action identity, verification bindings, result/coverage checks and repair returns.
- Closure path: A failed verdict returns to Build or a repair condition. On success it can proceed to authorized acceptance.
- Why this is / is not agent-owned: Comet installs a verification protocol. Its supported independent mode requires a separately available host session to perform the substantive inquiry.
- Evidence: [host-check.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet/reference/host-check.md), [SKILL.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet-native/SKILL.md), [platform-execution.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet/reference/platform-execution.md), [native-sdk-verify-decision.ts](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/domains/comet-native/native-sdk-verify-decision.ts).
- Basis: structural
- Confidence: high
- Caveats: A host-composed deployment can run independent review, which remains meaningful outside this general Index boundary.

### Absence scope

- Surfaces inspected: Verify and independent session contracts, Native outcome decisions, SDK evidence and Eval paths.
- Plausible first-party paths checked: Separate Verifier, evidence validators and built-in evaluation scoring.
- Why no material first-party path remains: The independent evidence judgment is explicitly delegated to the host. Deterministic report acceptance and offline scoring do not supply an internal auditor over the absent first-party operating cell.

## S4 — Outside-and-then intelligence

- State: —
- Function: Examine prospective adaptation through accepted applications, verified skills and project knowledge.
- Disturbance / variety regulated: Future work can benefit from changed requirements, outcomes and reusable project lessons.
- Decisive decision or feedback right: Select the future capability or meaningful policy change and authorize its adoption.
- Decision owner: Host author/operator for workflow creation and distribution. Memory providers and deterministic policy refresh supply context.
- Supporting / enforcement mechanisms: Workflow creation and Eval records, Experience Journal and context selection.
- Closure path: Approved application or eligible knowledge reaches later host runs. It changes available context or workflow choices.
- Why this is / is not agent-owned: These are genuine first-party adaptation surfaces serving adjacent agents. No packaged autonomous Builder or adaptation owner grounds a positive general-harness grade at this boundary.
- Evidence: [README.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/README.md), [PERSONAL-MEMORY.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/docs/operations/PERSONAL-MEMORY.md), [PROJECT-KNOWLEDGE.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/docs/operations/PROJECT-KNOWLEDGE.md), [semantic-review.ts](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/domains/comet-memory/semantic-review.ts), [runtime-sdk.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/docs/architecture/runtime-sdk.md).
- Basis: structural
- Confidence: high
- Caveats: The exclusion is scoped to general Index eligibility and leaves the future-capability product mechanisms described.

### Absence scope

- Surfaces inspected: Workflow distribution, Eval, knowledge lifecycle and memory reflection rules.
- Plausible first-party paths checked: Future workflow version, skill iteration, project-policy promotion and background semantic learning.
- Why no material first-party path remains: Function-specific adaptation exists as host/operator composition and deterministic knowledge lifecycle. The shipped sources do not establish an internal operational agent with corresponding prospective authority.

## S5 — Policy and identity

- State: —
- Function: Check for constitutive authority governing an in-boundary operational agent organization.
- Disturbance / variety regulated: Requested delivery actions may exceed confirmed scope or retained operator authority.
- Decisive decision or feedback right: Set or change enduring mandate, permission and policy for an in-boundary agentic unit.
- Decision owner: The operator gives actual project/workflow authority. The host retains its own agent permissions.
- Supporting / enforcement mechanisms: Config, declared workflow governance, explicit Shape and result approvals, pinned runtime rules and separate delivery actions.
- Closure path: Approved decisions update project change state and constrain further host work.
- Why this is / is not agent-owned: Configuration and approval enforce a contract around external work. They do not establish first-party agentic S1 plus a constitutive identity loop in the general assessment scope.
- Evidence: [SKILL.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet-native/SKILL.md), [runtime-sdk.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/docs/architecture/runtime-sdk.md), [host-check.md](https://github.com/rpamis/comet/blob/78b1b11ae75648c6f387e01d889f2ef097d6e8df/assets/skills/comet/reference/host-check.md).
- Basis: structural
- Confidence: high
- Caveats: One change's confirmation and repository maintainer governance are distinct from constitutive authority of a running agent organization.

### Absence scope

- Surfaces inspected: Workflow selection, approval waits, project configuration and distinct delivery rights.
- Plausible first-party paths checked: Shape approval, authority to choose delivery, external host policies and package identity.
- Why no material first-party path remains: The current S5 candidate paths concern user authority over hosted work or configuration. There is no qualifying packaged agent organization to which to assign an Index S5 state.

## Distributed OSS parent arrangement

The upstream project maintainers and the local project operator occupy different boundaries. No project-wide parent status is inferred from contributor governance.

## Self-hosted and non-human modes

The code supports reusable local runtime deployments, version-pinned applications and interactive operation through compatible hosts. Separate host-owned execution and verification remain explicitly required for the corresponding paths.

## Recursion

Parent and Child SDK Runs are execution-scope relations. In this assessment they structure workflow state around external agent sessions.

## Variety and escalation

The Runtime reduces execution/reporting variety using accepted scope, schemas, Action identity and deterministic transitions. Host blockers and user decisions drive subsequent continuations.

## Evidence gaps

No live host or Eval run was reproduced. The proposed exclusion is based on the pinned source-level agent ownership boundary, not absence of reliable workflow, coordination or verification mechanisms. An alternative system-in-focus that explicitly includes a particular host would require a separate pinned assessment.
