---
harness_id: harness-jordi-mar-al
project_name: Harness (Jordi Marçal)
repository: https://github.com/jordimarsal/harness
review_ref: 2aa8ffde95ebe78f4f99f991b262530d5acc02a3
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Harness (Jordi Marçal)

## Review boundary

- System in focus: The repository-installed Harness Standard workflow operating one software project on a supported Claude Code or OpenCode host.
- Purpose and identity: Deliver changes from specifications through separate implementation and review roles, with explicit human specification and completion gates.
- Relevant environment: Project requirements, repository worktree, tests, feature-state and progress files, configured host agents and maintainers.
- Standard-distribution boundary: The versioned installer, generated workflow instructions, role definitions, state schemas and supported verification tools. Host inference, tool execution and external SaaS remain dependencies.
- Credited operating / distribution surfaces: [README.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/README.md), [install.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/install.sh), [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh), [templates/.claude/agents](https://github.com/jordimarsal/harness/tree/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents), [templates/.opencode/agent](https://github.com/jordimarsal/harness/tree/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.opencode/agent), [templates/workflow](https://github.com/jordimarsal/harness/tree/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow), [templates/tools/commit.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/tools/commit.sh)
- Adjacent first-party surfaces excluded from ownership: Development tests, frozen installer evaluation fixtures, project documentation website and the underlying model-service organization.
- First-party operating / deployment modes considered: Project-installed full multi-agent workflows on supported hosts, single-session hybrid, optional parallel implementers and optional review gauntlet. Positive S2 and S3* witnesses concern the stated parallel/full modes.
- Recursion level: One installed project workflow with operating roles for specification, implementation and review under the leader agent.
- Reviewed revision: `2aa8ffde95ebe78f4f99f991b262530d5acc02a3`
- Observation date: 2026-11-18
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The installer copies first-party host-specific agent definitions in full mode and incorporates the corresponding workflow. A committed feature board, specification trio, task IDs and named on-disk reports form the operating state. The installer supports a single-session hybrid mode with stricter evidence logs and optional gauntlet steps.

## Operational model

The leader reads the feature board, sends a spec author, then waits for human specification approval. Once a feature is active, the leader selects implementation batches and checks files and gates between dispatches. A separate reviewer in full mode inspects primary artifacts and issues an approval or changes-requested verdict before the completion gate.

## S1 — Operations

- State: A
- Function: Operational task execution
- Disturbance / variety regulated: Approved specs, code state, test results and task failures
- Decisive decision or feedback right: Choose and carry out the implementation and test actions needed to complete a scoped task batch
- Decision owner: The configured host model running the shipped implementer role
- Supporting / enforcement mechanisms: Installed worker rules, task IDs, specification files and project verification tools
- Closure path: Files and tests are written and tasks and proof are reported to the leader for the next batch
- Boundary reachability: The full installer copies each host's implementer definition and workflow. The leader dispatches that installed role after specification approval; the hybrid instructions carry the same operational task responsibility in one session.
- Why this is / is not agent-owned: The worker selects and performs the particular code and test actions within the approved scope.
- Evidence: [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh), [templates/.claude/agents/implementer.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/implementer.md), [templates/.opencode/agent/implementer.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.opencode/agent/implementer.md), [templates/workflow/opencode/full.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow/opencode/full.md)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

## S2 — Coordination

- State: A
- Function: Attenuation of interference between distinct S1 units
- Disturbance / variety regulated: Parallel implementer cells can sweep each other's edits into a commit or start work before a required batch produces its files
- Decisive decision or feedback right: Decide which independent task batches may run concurrently, hold dependent work, and scope each cell's commit to its files
- Decision owner: The leader chooses the dispatch relation and each implementer supplies its own scoped paths
- Supporting / enforcement mechanisms: Feature and task state, model dispatch, predefined path-scoped Git wrapper and index-lock retry
- Closure path: The leader verifies named task/file evidence before releasing dependent dispatches. Subsequent commits contain only paths selected for that cell
- Boundary reachability: Full mode installs the leader, implementer and commit wrapper. Parallel mode is selectable in the feature configuration.
- Why this is / is not agent-owned: The leader determines the task batches and decides which are admissible in parallel. The wrapper enforces file scoping and does not select the task or owner.
- Evidence: [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh), [templates/.claude/agents/leader.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/leader.md), [templates/workflow/claude/full.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow/claude/full.md), [templates/workflow/opencode/full.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow/opencode/full.md), [templates/tools/commit.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/tools/commit.sh)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: The wrapper is not file locking and does not make two authorized edits to the same file independently safe.

- Distinct S1 units: Separate hosted implementer sessions dispatched for independent task blocks.
- Inter-S1 disturbance: The sessions share a Git worktree and index. Broad staging would capture another unit's in-flight work. Dependent implementation started too early could consume incomplete outputs.
- Attenuating coordination relation: Leader dispatch eligibility follows the task dependencies and observed completion. Each implementer commits its named paths through the installed wrapper.
- Feedback into subsequent S1 behaviour: Verified task status and actual produced files control which dispatch becomes eligible; an incomplete batch stays or is redispatched.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped protocol targets stated shared-index interference and dependency contention, with path-scoped commits and evidence-gated release.

## S3 — Inside-and-now control

- State: A
- Function: Whole-system current direction and resource or commitment intervention
- Disturbance / variety regulated: Stalled batches, missing evidence, context exhaustion and competing active workload across one project's feature workflow
- Decisive decision or feedback right: Select next work and batch size, control active feature admission, and reassign a stalled batch to a fresh worker
- Decision owner: The leader agent in the installed full workflow
- Supporting / enforcement mechanisms: Feature board, phase status, progress files, evidence check and lead-to-worker dispatch
- Closure path: The leader verifies the actual output, narrows, repeats or restarts a batch, and uses the updated state to govern later work
- Boundary reachability: The installer provides host-specific leader definitions and inserts the selected full workflow into the host's entry instructions.
- Why this is / is not agent-owned: The leader owns scoped deployment of workers and intervention after inadequate work evidence. Human specification and completion approvals remain binding gates.
- Evidence: [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh), [templates/.claude/agents/leader.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/leader.md), [templates/.opencode/agent/leader.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.opencode/agent/leader.md), [templates/workflow/opencode/full.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow/opencode/full.md)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: No separately selectable parent-owned project-supervision mode is asserted from the human checkpoints.

- Whole-system current view: The active specification, feature board and progress evidence cover the installed project workflow at this recursion.
- Current-control decision scope: Control the single active feature, scope current batches and recover stalled worker commitments subject to the two human gates.

## S3* — Complementary audit

- State: A
- Function: Complementary independent operational audit with corrective return
- Disturbance / variety regulated: The implementer reports completion but test coverage or delivered code does not match approved requirements
- Decisive decision or feedback right: Independently judge requirement-to-test coverage and actual delivered artifacts, returning defect findings or an approval
- Decision owner: The separately dispatched reviewer agent in full mode
- Supporting / enforcement mechanisms: Distinct read-oriented role, direct file access, test reruns, explicit report and verdict
- Closure path: The reviewer produces a verdict and writes actionable deficits. Completion requires both the reviewer verdict and human gate; a deficient implementation cannot simply mark itself complete
- Boundary reachability: The full installer supplies a distinct reviewer; the full workflow calls it after implementation. Optional gauntlet judgment passes can use separate fresh reviewer context.
- Why this is / is not agent-owned: The reviewer opens primary files and test bodies, reruns gates itself and decides whether observed evidence satisfies each requirement. The human completion decision remains separate.
- Evidence: [README.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/README.md), [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh), [templates/.claude/agents/reviewer.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/reviewer.md), [templates/.claude/agents/implementer.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/implementer.md), [templates/workflow/opencode/full.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow/opencode/full.md)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: The hybrid workflow's in-session review is not credited with the full-mode independence.

- Claim being audited: The implementation satisfies approved requirements, tasks and verification checkpoints.
- Ordinary reporting path: Implementer progress files, marked task list and self-verification summary.
- Complementary access path: Reviewer inspects actual changed files and tests and runs the gates independently.
- Independence boundary: Full workflow uses a separate reviewer role and reported artifacts do not substitute for direct evidence.
- Who acts on findings: The leader and implementer receive the verdict and findings. The human completion gate requires that review.

## S4 — Outside-and-then intelligence

- State: —
- Function: External, prospective intelligence and adopted capability adaptation
- Disturbance / variety regulated: Changed external requirements, technology or operating environment requiring changes to project workflow capability
- Decisive decision or feedback right: No supplied continuing external-and-prospective horizon loop adopts a change to organizational capability
- Decision owner: The human chooses approved scope and module or configuration changes. Agents can explore and record project designs
- Supporting / enforcement mechanisms: Spec author, optional architecture guidance and scanning, project history and retrospective counters
- Closure path: Approved spec moves a feature into implementation; the retro line records completed operations
- Why this is / is not agent-owned: Feature research changes the work specification. The review did not identify a recurring path that models outside future conditions, compares capability options and returns an adopted operational change.
- Evidence: [templates/.opencode/agent/spec-author.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.opencode/agent/spec-author.md), [templates/workflow/opencode/full.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow/opencode/full.md), [templates/modules/architecture-catalog/architecture-options.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/modules/architecture-catalog/architecture-options.md), [templates/modules/project-scanner/scan.py](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/modules/project-scanner/scan.py), [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [templates/.opencode/agent/spec-author.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.opencode/agent/spec-author.md), [templates/workflow/opencode/full.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/workflow/opencode/full.md), [templates/modules/architecture-catalog/architecture-options.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/modules/architecture-catalog/architecture-options.md), [templates/modules/project-scanner/scan.py](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/modules/project-scanner/scan.py), [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh)
- Plausible first-party paths checked: Trace architecture choices, startup scans, performance modules, configuration updates and completion retrospectives.
- Why no material first-party path remains: The shipped paths support present feature design, explicit user configuration or historical process observations. They do not close an external prospective adaptation decision.

## S5 — Policy and identity

- State: —
- Function: Resolution and return of ultimate identity or policy decisions
- Disturbance / variety regulated: Disagreement over the installed organization's binding purpose or ultimate workflow policy
- Decisive decision or feedback right: No installed authority process adjudicates and returns a change to constitutional rules
- Decision owner: Maintainers supply installed rules; the project human approves particular specs and completion
- Supporting / enforcement mechanisms: Host role definitions, feature-state requirements and installer options
- Closure path: The operator's two gates authorize a specific feature's implementation or closure
- Why this is / is not agent-owned: Human scope and completion approval regulate project work. The reviewed path does not decide and return a change to the system's ultimate mandate.
- Evidence: [templates/docs/specs.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/docs/specs.md), [templates/.claude/agents/leader.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/leader.md), [templates/.claude/agents/implementer.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/implementer.md), [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [templates/docs/specs.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/docs/specs.md), [templates/.claude/agents/leader.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/leader.md), [templates/.claude/agents/implementer.md](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/templates/.claude/agents/implementer.md), [init.sh](https://github.com/jordimarsal/harness/blob/2aa8ffde95ebe78f4f99f991b262530d5acc02a3/init.sh)
- Plausible first-party paths checked: Inspect human spec and completion gates, optional configuration and installer update behavior.
- Why no material first-party path remains: The workflow applies standing gates and processes a feature. A maintainer can edit installed policy outside that loop, but no first-party identity dispute and authoritative return path is supplied.

## Recursion

Leader and named agents have distinct task boundaries, evidence and host instruction scopes. Repeated deployment across projects does not by itself construct a complete recursive VSM.

## Variety and escalation

The leader scales batch size, redispatches stalled work and refreshes worker context. Direct evidence and a separate reviewer qualify the completion path. Human authorization is explicit before implementation and completion.

## Evidence gaps

Source-only. Host adherence, live multi-agent behavior and enforcement outside these first-party role and script paths were not tested. Optional external boards and scanners do not establish independent ownership.
