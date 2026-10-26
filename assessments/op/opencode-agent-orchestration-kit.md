---
harness_id: opencode-agent-orchestration-kit
project_name: OpenCode Agent Orchestration Kit
repository: https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit
review_ref: a0b1b7869368576803c58b834707c907d62d273a
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OpenCode Agent Orchestration Kit

## Review boundary

- System in focus: One locally installed OpenCode Agent Orchestration Kit (OAK) configuration operating on a user's software-engineering project, especially its default `lead` agent, installed subordinate roles, `/feature` and explicitly selected `/autonomous` task flow. The GitHub project's contributor organization is not the system in focus.
- Purpose and identity: Turn a bounded software-change request into context discovery, specification, source changes, direct artifact review, correction and a reported outcome or open PR.
- Relevant environment: User objectives and approvals, changing repository code, tests, architecture constraints, tool permissions, OpenCode model execution, task uncertainty, incorrect implementation reports, reviewer findings, git/CI failure and external provider availability.
- Standard-distribution boundary: The kit's installable `opencode/` agent and command definitions, `opencode/opencode.json`, shipped task/loop state and reviewer-attestation scripts, and the OpenCode host's actual model-backed `task`/tools invocation when configured with this kit. The OpenCode provider/tool engine is a dependency, not an independently credited OAK metasystem.
- Credited operating / distribution surfaces: [installed configuration and default lead](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/opencode.json), [lead rights, delegation and correction return](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/lead.md), [feature flow](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/feature.md), [explicit autonomous task cycle](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/autonomous.md), [durable loop state and review attestation](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/scripts/loop-state.mjs), [reviewer source-access contract](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/reviewer.md).
- Adjacent first-party surfaces excluded from ownership: Maintainer CI, release/install transaction validation, compatibility canaries, historical AHE benchmark/replay fixtures and dogfood transcripts, the OAK repository's contributor governance, and developer-only harness self-evolution when `/evolve` requires `cwd` to be the kit repository. The generic OpenCode runtime and model/provider reasoning are not newly attributed OAK governance functions. Static scripts can support closure without becoming autonomous decision owners.
- First-party operating / deployment modes considered: Default installed `lead` routing; `/feature` research-to-review flow; explicit `/autonomous` bounded PR-delivery mode; human-gated `/loop`; optional `/review-orchestrated` preflight/specialist variants; and the separately scoped maintainer `/evolve` flow. A user may select smaller direct work or skip final review only under the kit's narrow small-gate.
- Recursion level: One current software-engineering work organization around a local project objective. Its operational researcher/specifier/developer units are not presumed independently viable organizations. The upstream OpenCode platform, human developer's company and OAK maintainers are outside this assessed recursion.
- Reviewed revision: `jcarlosrodicio/opencode-agent-orchestration-kit@a0b1b7869368576803c58b834707c907d62d273a` (`master`).
- Observation date: 2026-10-26; static first-party source and native deterministic tests only.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

OAK ships configurable OpenCode agent frontmatter, workflows and commands copied by its installation manager into an OpenCode configuration. `lead` is the model-backed primary default, with read-only inspection and a specifically allowlisted delegation surface; `developer` owns actual code changes, `researcher` evidence collection, `specifier` task shaping and `reviewer` original-diff adjudication. `/feature` makes research/design/specification/implementation/review dependencies explicit. The opt-in `/autonomous` flow stores a bounded iteration budget, branch/task run, durable JSON state, append-only history, session lease and review attestation; delivery stops at an open PR and never merges. `mission-runtime` records OpenCode session events into task logs on a best-effort basis; it does not itself decide a VSM function. The operator and OpenCode host retain permission, model and provider controls. A separate `/evolve` route operates on the harness source repository and is outside the normal target-project coding organization.

## Operational model

The operational work cells are model-backed roles handling project research, task specification and code implementation in the configured OpenCode host. The model-backed `lead` chooses current work routing, phase gates, bounded iteration/rework and stop decisions; scripts persist/enforce its already chosen parameters. `reviewer` is a separately instantiated read-only model role with direct diff/source/test access, rather than just the implementing developer's report. Its assessment returns to `lead` and then to `developer` for repair. The user's ordinary approval of a task, shell command, loop or final PR merge remains a distinct parent permission and is not evidence of ultimate S5 or an autonomous OAK decision.

## S1 — Operations

- State: A
- Function: Produce project research/specifications and source/test changes as bounded software-development outcomes.
- Disturbance / variety regulated: Unknown code architecture, conflicting implementation hypotheses, failures of tests, actual file differences and changing task acceptance criteria.
- Decisive decision or feedback right: Model-backed researcher/specifier/developer agents select investigation, implementation and correction actions within delegated scope; outputs and tool effects return to the current job.
- Decision owner: The selected first-party OAK-configured operational agent, executed by the OpenCode model/tool host, rather than the deterministic installation manager or a fixed static rule.
- Supporting / enforcement mechanisms: Agent permissions, task routing, OpenCode `task` transport, shell/edit permissions, local filesystem, tool/API runtime, task contracts and deterministic test runners.
- Closure path: User objective → configured `lead` → direct or phased delegate → model-selected read/write/check actions → project source/spec/test output and evidence → `lead`/user return.
- Boundary reachability: The kit's shipped `opencode.json` declares `lead` as default and the packaged `lead` permits task delegation to `developer`, `researcher` and `specifier`; these are installed roles, not illustrative agents from an example project.
- Why this is / is not agent-owned: Remove the operational model actor while keeping permissions and scripts: no task-specific source edit, specification or corrective implementation is selected. The external OpenCode runtime executes these decisions but its generic capabilities are not counted as a separate first-party OAK organization.
- Evidence: [default and model roles](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/opencode.json#L1-L36); [lead delegation contract](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/lead.md#L38-L70); [feature delegate ordering](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/feature.md#L23-L57); [developer task action](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/implement.md).
- Basis: Explicit installed agent roles and structural model/tool delegation path.
- Confidence: High for source reachability, not measured code-generation quality or prompt compliance.
- Caveats: OAK reuses the external OpenCode agent engine. Some commands are prompt contracts and not immutable runtime enforcement. A user can operate in a simple/manual mode that does not exercise every role.

## S2 — Coordination

- State: —
- Function: Would attenuate a specific interference or oscillation between distinct operational agent units and return a settlement into their subsequent work.
- Disturbance / variety regulated: Potential parallel edit collisions, contradictory investigations/specs and incompatible agent outputs; no shipped conflict-specific inter-S1 settlement was established.
- Decisive decision or feedback right: No S2-specific conflict/oscillation arbitration distinct from current mission assignment or final artifact quality judgment was evidenced.
- Decision owner: Not established for S2 at this recursion.
- Supporting / enforcement mechanisms: Sequential phase barriers, handoff packets, branch/lease/iteration locks, explicit nonparallel `/autonomous` mode, optional reviewer aggregation and generic role routing.
- Closure path: Work passes through `lead` and serial roles; no separately evidenced two-unit interference → S2 mediation → return to both units' subsequent interaction.
- Boundary reachability: Shipped routing and locks are reachable, but their source-witnessed role is task ordering, current-run integrity or reviewer feedback, not inter-S1 oscillation regulation.
- Why this is / is not agent-owned: An LLM scheduling researcher before developer or sending a review defect back for rework is not a demonstrated disturbance-specific coordination right. Deterministic journal leases also do not choose a reconciliation strategy.
- Evidence: [feature barriers](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/feature.md#L24-L58); [autonomous parallelism prohibited](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/autonomous.md#L7-L29); [journal/lease invariants](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/scripts/loop-state.mjs#L248-L310).
- Basis: Source-bounded negative, not a universal claim against custom integrations.
- Confidence: Medium-high.
- Caveats: Extra user-created conflict mediators or independently deployed agent swarms were not imputed to this packaged mode.

### Absence scope

- Surfaces inspected: Installed lead/task permissions, phase barriers, delegated agents, durable loop locks and handoffs, normal reviewer return and optional review coordinator.
- Plausible first-party paths checked: Concurrent source edits, competing implementation decisions, same-file collision, contradictory evidence from distinct operational units, role scheduling, shared-state/review disagreement and lease contention.
- Why no material first-party path remains: These source paths prevent overlap or route tasks vertically through a lead/reviewer. None shows a specific inter-S1 interference signal with a differentiated coordination settlement returned to the affected operational units; arbitrary custom OpenCode composition would be a different assessed boundary.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the current engineering mission's shared commitments, work-phase order, correction/retry budget and readiness for closure across its delegated operational roles.
- Disturbance / variety regulated: Under-specified objectives, changing complexity, incomplete current phase work, failure of tests, blocked review findings and exhaustion of task-local iteration budget.
- Decisive decision or feedback right: Model-backed `lead` chooses which role/phase receives a work commitment, whether a current plan/scope must change, when a review finding warrants developer rework and whether the bounded mission continues, blocks or closes. In `/autonomous`, it sets a task-specific 1–6 iteration plan before execution.
- Decision owner: The first-party configured `lead` agent for current mission choices; `reviewer` owns the content of a separate audit verdict; user owns actual external approval/merge rights.
- Supporting / enforcement mechanisms: Phase constraints, `loop-state` JSON and history, budget cap/lease, mechanical status transitions, reviewer attestation requirement, `oak deliver`, CI and OpenCode task dispatch.
- Closure path: Current mission/task reports, scope and reviewer findings → `lead` selects next current-role allocation/rework/stop → task instruction reaches `developer` or another operational role → updated work and review signal return. Durable state constrains the decision but does not choose it.
- Boundary reachability: `lead` is the installed default and the shipped `/feature` and opt-in `/autonomous` commands place it above the project roles with explicit review and retry feedback. This current-mission authority is available without developing a new coordinator plugin.
- Why this is / is not agent-owned: Removing `lead` leaves deterministic phase and budget checks but no discretionary allocation/rework choice for the current multi-role job. This is scoped to a current engineering mission, not the entire user's enterprise or upstream OpenCode project.
- Whole-system current view: Current task contract, role/phase completion, source/diff and validation return, review verdict, iteration status and blocking cause for the one mission.
- Current-control decision scope: Current job role allocation, phase barriers, bounded repair commitment and completion/block decision; not global organizational finances, release policy or future platform strategy.
- Evidence: [lead scope and phase decisions](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/lead.md#L187-L214); [rework return](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/lead.md#L262-L283); [explicit autonomous cycle and budget](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/autonomous.md#L42-L57); [iteration decisions/stop](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/autonomous.md#L120-L164); [state enforcement](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/scripts/loop-state.mjs#L900-L985).
- Basis: Explicit organizational role and first-party current-mission state/return wiring; no live model execution claimed.
- Confidence: Medium for current-mission scope, not enterprise-wide S3.
- Caveats: A phase graph or iteration validator alone would not qualify; the positive witness depends on model-owned current allocation and correction choices in the shipped orchestration mode. `/loop` may instead require human approval and is not claimed as a distinct parent-governed S3 mode.

## S3* — Complementary audit

- State: A
- Function: Independently challenge the implementing agent's correctness/safety claims using original source, diff and test artifacts before current work is accepted.
- Disturbance / variety regulated: Developer's incomplete or self-serving success report, undiscovered regression, unsafe change, spec violation or misleading green routine checks.
- Decisive decision or feedback right: A separate model-backed `reviewer` reads original artifacts, chooses causal findings and a final `pass`/`needs_changes`/`blocked` verdict; `lead` returns a blocking result to `developer` for corrected work. In autonomous mode completion additionally requires a reviewer child-session attestation.
- Decision owner: The configured reviewer agent for the audit judgment; state scripts only require and bind an attestation and do not judge semantic correctness themselves.
- Supporting / enforcement mechanisms: Read-only reviewer permissions, adversarial review skill, explicit raw diff/source/test access, review-result schema, bounded correction cycles and `oak state attest-review`.
- Closure path: Developer's output and routine status → separately invoked reviewer directly inspects source/diff/tests → evidence-based verdict → `lead` passes blocking findings to developer → revised artifact returns to another review/closure. A missing attestation prevents the opt-in autonomous loop from terminal completion.
- Boundary reachability: The installed `reviewer` is an OpenCode subagent and `/feature` calls it after implementation; `/autonomous` explicitly requires `task reviewer` rather than an ordinary top-level self-review and ties approval to a reviewer child session. The positive mode does not rely on CI alone or on optional unrelated benchmark workers.
- Why this is / is not agent-owned: Reviewer independently selects the substantive discrepancy judgment from original artifacts; replacing it with a deterministic attestation verifier leaves no semantic independent review. Source-read independence is a declared role/session boundary, not a guarantee that models are uncorrelated or that the host sandbox is tamperproof.
- Claim being audited: Developer/lead claims that changed code meets task spec, tests and security expectations.
- Ordinary reporting path: Developer supplies its implementation summary and validation envelope to lead.
- Complementary access path: Reviewer reads the real diff, source, relevant specs and repeatable tests, excluding developer summary as primary evidence; optional adversarial probing adds different inspection questions.
- Independence boundary: Distinct OpenCode reviewer subagent/context with denied edit permission and separate final-verdict authority; the same host and model family may be reused.
- Who acts on findings: `lead` dispatches corrective work to `developer`, then reopens review; the reviewer does not directly write fixes.
- Evidence: [reviewer source policy and independent artifact access](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/reviewer.md#L39-L87); [reviewer outputs](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/reviewer.md#L139-L160); [lead return path](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/lead.md#L262-L282); [required distinct child review in autonomous mode](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/autonomous.md#L125-L149); [review-attestation structural gate](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/scripts/loop-state.mjs#L791-L828).
- Basis: Source-declared and structurally connected complementary audit path.
- Confidence: Medium; no claim about actual defect-detection rate or independently proven runtime isolation.
- Caveats: Small low-risk direct work may use an explicit reviewer-skipping gate; optional `/review-orchestrated` preflight alone is **not** an independent audit verdict. This positive state is for the supported non-trivial `/feature`/`/autonomous` review path.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would sense changes in the external/future development environment, formulate prospective organizational capability adaptations and return their choices into subsequent current operating capability.
- Disturbance / variety regulated: Changing model/tool ecosystem, persistent user needs, future project risk and capability portfolio; this future-oriented organizational adaptation closure was not established in the assessed installed project mode.
- Decisive decision or feedback right: No first-party current-project S4 right evidenced. The optional `/evolve` generates proposals to alter the **OAK harness itself**, with source-repository cwd and human application approval, not the user's installed coding project's strategic adaptation.
- Decision owner: No S4-specific owner at the declared target-project recursion; project user/maintainers independently choose future scope and software evolution outside this task harness.
- Supporting / enforcement mechanisms: Research role/web tools, task memories, `/evolve` session evidence collection and preflight, evaluator/debugger/evolver proposals, manifests and deterministic tests.
- Closure path: Research and project planning can inform today's implementation; the separately scoped maintainer `/evolve` can feed kit development after approval, but it is not a first-party external-prospective decision path governing the assessed installed project operation.
- Boundary reachability: `/evolve` is shipped as an optional command but explicitly requires running in the kit's own git checkout and keeps evolution artifacts in its developer documentation; the target-project runtime does not thereby acquire a standing S4 regulatory loop.
- Why this is / is not agent-owned: Capturing previous sessions, recommending a test fix and patching a harness under a maintainer approval are not by themselves a credited future-facing S4 function at the target-project recursion.
- Evidence: [evolution scope and cwd precondition](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/evolve.md#L1-L32); [manifest/approval and re-evaluation path](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/evolve.md#L103-L131); [AHE separation from normal app features](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/docs/ai/harness/playbooks/lead-ahe-flow.md).
- Basis: Bounded negative at the declared recursion; separately acknowledges a developer-side adaptive mechanism.
- Confidence: Medium.
- Caveats: A separate assessment of the OAK maintainer's development organization, rather than one installed coding mission, could legitimately revisit this function at a different boundary.

### Absence scope

- Surfaces inspected: Standard default/feature/autonomous work, researcher/model configuration, persistent run/session evidence, optional `/evolve` and its AHE playbook, human apply gate.
- Plausible first-party paths checked: Prospective provider/tool choice adjustment, learned changes from past coding sessions, new capability/skill policy, changing user-environment modelling and evolution manifest returned to runtime.
- Why no material first-party path remains: Normal coding research and rework govern the present objective; the only explicit harness-adaptation flow is scoped to maintaining OAK's own source, not the installed project operating boundary. No source-backed external-prospective capability decision and subsequent operational return closes S4 at the chosen recursion.

## S5 — Policy and identity

- State: —
- Function: Would legitimately decide an identity/ultimate-policy-level conflict and return the decision as a binding constraint on future system operation.
- Disturbance / variety regulated: Conflicts about the harness's underlying mission, identity and ultimate trade-offs beyond ordinary task permission or review readiness.
- Decisive decision or feedback right: No autonomous or first-party parent-governed ultimate-policy judgment and return loop established for the installed project harness.
- Decision owner: Humans choose request, model/provider, permission and merge policy outside this first-party S5 path; OAK's configured `lead` resolves current work, not its own enduring identity.
- Supporting / enforcement mechanisms: System and agent prompts, permissions, explicit approval boundaries, `/autonomous` prohibitions on merging/deploying and immutable task contracts.
- Closure path: Ordinary user authorization changes the currently allowed task action; no source-reachable identity dispute → legitimate policy authority → binding decision → subsequent operation sequence at the declared recursion.
- Boundary reachability: Installed policy/permission constraints are active, but a distinct ultimate-policy deliberation and governance-return function is not part of the credited mode.
- Why this is / is not agent-owned: Static rules and normal human approvals constrain operations and must not be treated as a model or parent exercising S5 discretion.
- Evidence: [permissions and default agent](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/opencode.json#L1-L36); [lead limits](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/agents/lead.md#L5-L68); [ordinary autonomous safety boundaries](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit/blob/a0b1b7869368576803c58b834707c907d62d273a/opencode/commands/autonomous.md#L9-L31).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: The user's company, project maintainers and OpenCode provider may separately exercise policy/identity authority; that is not a first-party runtime S5 path here.

### Absence scope

- Surfaces inspected: Root configuration, agent system prompts, task permissions, user approval and PR delivery restrictions, task/loop contracts, maintainer/project documentation and harness evolution path.
- Plausible first-party paths checked: Identity-level disagreement, authority to revise project purpose, policy escalation, human acceptance/merge, model-provider selection and cross-task adaptation priorities.
- Why no material first-party path remains: The evidenced decisions admit, plan, perform, review, constrain or stop coding work. None processes and returns an ultimate identity/policy choice that binds subsequent operation at this recursion.

## Distributed OSS parent arrangement

OAK maintainers, independent OpenCode/plugin contributors and each local project operator are not one observable parent authority for a user's configured session. Project issues, CI and release administration govern source distribution, not automatically the assessed coding mission. No S3/S4/S5 `(P)` state is inferred from ordinary user approval or GitHub merge rights.

## Self-hosted and non-human modes

Users install and configure OAK locally. The declared normal mode connects OAK role definitions to a model-backed OpenCode host, with `lead` as default. `/autonomous` creates an optional bounded, model-owned current-control loop and separate reviewer-attested completion; `/loop` offers explicit approvals and stricter manual control. These are alternative task modes, not evidence of simultaneous human and agent ownership or a separate parent VSM function.

## Recursion

The evaluated work organization is one coding mission with subordinate research, specification and development roles. Reviewer complements their evidence, and `lead` regulates the current mission. A spawned researcher or reviewer is not automatically an independently viable nested organization, and a maintainer AHE flow over OAK's source belongs to an adjacent development recursion.

## Variety and escalation

Model-backed roles absorb changing source and user-task variety. `lead` chooses bounded current work/rework commitments while state scripts prevent duplicate leases, limit iterations and reject completion without the required reviewer attestation. Genuine blocked/ambiguous requirements, external permissions, missing verification, exhausted budgets and integration decisions return to the user rather than being silently promoted to S5. This is a source-wiring assessment, not measured agent reliability.

## Evidence gaps

- No live LLM-agent, model-provider, Browser, generated-code-quality, security-effectiveness or adversarial-review-quality trial was performed. All agent ownership claims are source-based and conditional on the supported installed mode executing as configured.
- On the pinned source, native deterministic `mission-runtime` and `task-run` test modules passed. The `loop-state` test module reported 19/20 passing subtests when invoked directly; its portable CLI subprocess case failed with `SyntaxError: Unexpected end of JSON input`. This local observation is **not** attributed to a VSM semantic failure and does not invalidate the source-level review-attestation code path; the cause was not established.
- Reviewer independence is a distinct context/role and direct-source-evidence rule, not independently attested secure isolation or guaranteed correctness. The optional small-gate weakens universal application of review but does not remove the evidenced non-trivial workflow.
- `/evolve` warrants a separate, differently scoped analysis if the future system-in-focus is OAK's own source-maintenance organization rather than an installed user's engineering mission.
