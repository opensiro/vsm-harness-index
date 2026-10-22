---
harness_id: iteron
project_name: Iteron
repository: https://github.com/Plantcore-AI/Iteron
review_ref: c146d7128a827c517732381a2a9722196677b0bd
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Iteron

## Review boundary

- System in focus: the Iteron Rust terminal coding agent and first-party model-directed Workflow execution available in its current pinned source, not its aspirational modular microkernel, future autonomous harness optimizer or the separate human-maintained OSS development organization.
- Purpose and identity: provide provider-backed coding assistance, safe tool actions, bounded agent workflows and durable local evidence; the broader research ambition is model × task-specific harness checkpoints.
- Relevant environment: user repository and shell, provider API and model features, mutable git working tree, workflow children, operator authorization, runtime budgets, audit records and verification command.
- Standard-distribution boundary: actual `iteron` terminal/one-shot CLI in frozen source, `crates/cli`, `crates/workflow`, `crates/tools`, `crates/agents`, provider/tool/kernel policy implementations, agent catalog and writer-worktree integration. The release binary referenced in README is v0.0.20 while the pinned source workspace is v0.0.21; no unsupported future target is credited.
- Credited operating / distribution surfaces: main model tool loop, model-authored Workflow scripts, bounded read-only child investigators, isolated writer child transactions, parent-turn result delivery, host-held writer lock, patch verification and refusal, permissions/sandbox, session and resource controls.
- Adjacent first-party surfaces excluded from ownership: repo-only `iteron-harness` research executable absent from published installs, future checkpoint selector, prospective evolution plane and microkernel diagram, maintainers' development approvals/AGENTS.md, benchmark ambitions, external provider intelligence and operator-authored extensions.
- Operating modes considered: interactive/print/headless coding, `--ask-permissions`, `--confine` where available, direct model run, model-authored in-turn/background `Workflow`, read-only child and host-isolated writer mode with required operator verification command.
- Recursion level: installed coding-session organization with possibly several first-party model child work units; not the separate project-maintainer team or offline research governance.
- Reviewed revision: [`c146d7128a827c517732381a2a9722196677b0bd`](https://github.com/Plantcore-AI/Iteron/tree/c146d7128a827c517732381a2a9722196677b0bd), immutable intake #200.
- Observation date: 2026-10-22, pinned structural source review; no provider-backed runtime campaign.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Iteron implements a Rust coding-agent runtime with model-selected file, shell, search and verification actions. Accepted ADR-0002 gives the root model the choice of direct execution or a task-specific `Workflow` script. The workflow engine runs bounded `agent()` leaf calls, with read-only investigator contexts and admitted isolated writer subprocesses, returning their reports/failures into the root's in-turn result. A fixed host forbids models from expanding authority, allocating beyond caps or merging their own patches.

The writer controller holds a session-wide mutex for each entire writer transaction, provisions a private git worktree, seals the patch digest, demands an operator-specified verifier, rejects parent HEAD drift and applies only a successful `git apply --check` patch. This is strong *interference prevention* between potential writing S1 children. However the policy is fixed by the host; failed or conflicting patches return `null`/a human-resolution requirement, with no agent-owned conflict settlement and adjusted sibling operations. The model can decide subsequent coding tactics, but the inspected first-party flow does not grant an identifiable separate S2 owner a decisive coordination-feedback loop. This distinction is especially important here: verified serialization is real but must not be silently called autonomous S2.

The offline evolution/checkpoint architecture is explicitly a target. Pinned source documents no first-class task-profile selector, autonomous promotion or completed real optimizer campaign; the repository-only research bridge is not in public release archives. Human maintainer review and project ownership do not migrate into the coding CLI's S3–S5 governance.

Primary evidence: [accepted model-directed workflow ADR](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/project/decisions/0002-model-directed-workflow-topology.md), [working writer transaction](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/activity.rs#L38-L298), [serialized merge and human escalation](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/worktree.rs#L384-L421), [current implementation bounds](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/project/status.md).

## Operational model

One user-oriented coding model selects current actions, including optionally specifying a bounded child workflow. Leaf agents independently execute specific investigations or permitted isolated coding tasks. Host rules preserve permissions, resource ceilings and patch integrity; the root sees child summaries or refusals and continues the current coding goal. There is no demonstrated distinct autonomous metasystem for present whole, future environment or ultimate identity.

## S1

- State: A
- Function: Pursue user coding goals through model-selected tools and task-specific workflow/child actions, adapting later choices to observed results.
- Disturbance / variety regulated: Unknown source files, failing tests, user requirements, tool/provider errors, read-only investigative uncertainty and mutable local workspace state.
- Decisive decision or feedback right: Root model selects code/tool actions and dynamically authors whether/how to run a Workflow; participating leaf models select task-local tools within host-enforced rights.
- Decision owner: Iteron's first-party root model loop and scoped child agent runs, not an external scheduler deciding every tool step.
- Supporting / enforcement mechanisms: Tool/provider adapters, `Workflow` tool with QuickJS script, `agent()`/`parallel()`/`pipeline()` primitives, model-visible results, bounded spawn, sessions, verification and writer worktrees.
- Closure path: User request → root model chooses tool/direct or Workflow script → host admits/bounds execution → tool or child outputs return → root model corrects, delegates further or finishes.
- Why this is / is not agent-owned: The model decides specific actions and topology after feedback; fixed gates constrain effects but do not replace the model's coding decision rights.
- Boundary reachability: `iteron` CLI and source workspace wire the standard coding/tool route and model-visible Workflow surface; ADR-0002 removes mandatory fixed pre-model fan triggers, leaving positive delegation to the model.
- Evidence: [public terminal CLI operation](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/README.md#L38-L116), [model-authored Workflow decision](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/project/decisions/0002-model-directed-workflow-topology.md#L20-L50), [actual child runs and results](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/activity.rs#L38-L181).
- Basis: structural.
- Confidence: high for implemented model/tool and child plumbing; empirical provider/model performance not tested.
- Caveats: Pre-alpha releases and runtime modes have platform restrictions, and source-level support does not imply all version 0.0.21 changes ship in release 0.0.20.

## S2

- State: —
- Function: Regulate actual interference among independently working coding S1 cells and return compensating coordination decisions to them.
- Disturbance / variety regulated: Competing child writers, shared-branch file conflicts, dirty workspaces, competing patch bases and concurrent effecting tool writes.
- Decisive decision or feedback right: Host policy serializes writer transactions and rejects dirty/advanced/conflicting parents, but conflict disposition is fixed `Reject`; rejected patches require human resolution, without first-party agent-authored replan/settlement returned to multiple affected children.
- Decision owner: Deterministic host writer lock, patch validator and permission gates for prevention; human for unresolved conflict decisions, not a separate installed autonomous S2 decision owner.
- Supporting / enforcement mechanisms: Session-wide mutex, isolated git worktree, exact patch SHA receipt, operator verification oracle, `git apply --check`, parent HEAD/cleanliness checks, deferred tool write-set overlap rejection.
- Closure path: Writer child completes → host verifies/serializes one patch → clean patch enters parent or conflict is discarded/refused and surfaced as child failure. No separate conflict arbitration → affected S1 negotiation/adjustment loop is installed.
- Why this is / is not agent-owned: These are substantive interference controls, but their refusal/serialization policy is deterministic and the correction right explicitly escalates to human resolution. Model response to one failed tool is task-local S1 troubleshooting, not evidenced S2 governance.
- Evidence: [writer mutex and child lifecycle](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/activity.rs#L49-L85), [verify/merge/refusal](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/activity.rs#L193-L294), [merge conflict human resolution](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/worktree.rs#L61-L75), [writer policy](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/workflow/src/execution_policy.rs#L150-L203).
- Basis: structural.
- Confidence: medium-high on non-autonomous settlement; no conflicting sibling writers actually run for this assessment.
- Caveats: This is a stronger first-party conflict-prevention design than generic messaging. An assessed extension adding autonomous conflict diagnosis and return could change the S2 result, but no such closure is credited now.

### Absence scope

- Surfaces inspected: accepted workflow topology, spawner read-only/writer classes, isolated worktrees, session mutex, patch verification, merge conflict paths, tool write-set scheduling and root result collection.
- Plausible first-party paths checked: colliding child writes, sibling fan/serial behavior, human escalation, deterministic patch rejection, model retries, background script alternatives, external Git conflict resolution and fixed authority.
- Why no material first-party path remains: The supported host only serializes/accepts/refuses; conflict-specific decisions are fixed or external, and no first-party autonomous cross-S1 adjustment channel is evidenced despite actual child and collision-protection primitives.

## S3

- State: —
- Function: Make binding whole-current resource, priority and commitment decisions across independently viable S1 operations.
- Disturbance / variety regulated: Shared provider cost, concurrent child load, active tool effects and unavailable verification/permissions.
- Decisive decision or feedback right: Root model plans its assigned coding workflow, while host enforces preconfigured ceilings and serialized writer admission; there is no distinct cross-session/whole-organization resource bargaining or reallocation mandate.
- Decision owner: User/operator for budgets and verification; fixed host enforcers for caps; root model for current task decomposition, not established S3.
- Supporting / enforcement mechanisms: Spawn ledger, child budget ceiling, capacity gates, provider route policy, writer admission lane, progress journals and operator-controlled limits.
- Closure path: User task → model-selected workflow → bounded child execution/ledger → task answer or refusal; not whole-current portfolio policy/commitment rebalance.
- Why this is / is not agent-owned: Budget gates make task execution bounded but do not confer discretionary current management across operational cells.
- Evidence: [runtime child budget inheritance](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/subagent_control.rs#L110-L173), [writer/resource admission](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/activity.rs#L38-L83), [model-directed topology scope](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/project/decisions/0002-model-directed-workflow-topology.md#L20-L51).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Strong host authority/invariants are deliberately not learnable; a human managing the repository is outside the coding-runtime recursion level.

### Absence scope

- Surfaces inspected: child limits, writer lane, workflow policy, runtime task status, permissions, provider route and human development ownership.
- Plausible first-party paths checked: whole-current shared resource optimization, priorities among active work cells, model decomposition, conflict arbitration and operator budget choices.
- Why no material first-party path remains: Only task-scoped planning and fixed host caps are evidenced; no separately owned current organizational commitment control.

## S3*

- State: —
- Function: Independently check a current S3 managerial claim against alternate operating evidence and cause corrective management decisions.
- Disturbance / variety regulated: False code progress, bad patches, failed verification, audit-record tampering and inaccurate provider cost observations.
- Decisive decision or feedback right: Patch verifier and hash-chain are mechanical task/evidence checks; external human maintainers review source changes. Neither audits a defined whole-current S3 claim via a complementary independent decision route.
- Decision owner: Deterministic verification host for patch/tool integrity, optional human maintainer for OSS changes; no operative S3* agent.
- Supporting / enforcement mechanisms: Test verifier, hash-chained session/effect records, patch hash receipt, independent developer CI and human ownership boundary checks.
- Closure path: Candidate writer patch → host verification before merge → accept or refuse tool effect; not S3 self-report → outside operational audit → corrected S3 allocation.
- Why this is / is not agent-owned: Reproducible evidence supports audits but does not create a decisive independent management-auditing function at the selected runtime recursion.
- Evidence: [host verification and merge](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/crates/cli/src/runtime/workflow_spawner/worktree.rs#L128-L187), [OSS governance separate](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/AGENTS.md#L1-L30), [source status/evidence boundary](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/project/status.md#L1-L71).
- Basis: structural.
- Confidence: high for verification mechanics; medium-high for bounded S3* absence.
- Caveats: Independent benchmark evaluation in repository-only research tooling does not audit runtime S3 decisions and is not installed in release artifacts.

### Absence scope

- Surfaces inspected: verification oracle, patch hash, runtime journals, research evaluation harness, OSS reviewer/ownership rules and workflow child result path.
- Plausible first-party paths checked: evidence integrity, alternative operational reality, verifier disagreement, management claim review and corrective authority.
- Why no material first-party path remains: There is no prior S3 whole-current claim owner and no independent audit/management correction loop above local patch correctness checks.

## S4

- State: —
- Function: Sense prospective external environment, develop adaptation strategies and return accepted new capacity into present S3 operations.
- Disturbance / variety regulated: Future provider capabilities, changed model-task fit, new domain requirements and degradation across task distributions.
- Decisive decision or feedback right: The target checkpoint selector and evolution/promote loop are explicitly unfinished; offline fixture tooling has no autonomous live candidate promotion or new-runtime policy installation decision.
- Decision owner: Human for evaluating/promoting policy bundles; selected provider and configured harness for present work, no first-party S4 strategist.
- Supporting / enforcement mechanisms: Typed policy manifests, optimization census, offline research bridge and checkpoint design, explicit human promotion, runtime immutable policy pinning.
- Closure path: Research intent → prototype/fixture candidate with human review or future pipeline. No demonstrated externally grounded prospective option → strategic selection → S3 capability-installation loop.
- Why this is / is not agent-owned: Versioned policy identity and planned evolution interfaces are real, but live S4 authority and operational return are expressly unshipped.
- Evidence: [architectural implementation truth](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/architecture.md#L55-L90), [no autonomous policy promotion](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/project/status.md#L25-L63), [checkpoint profile/selector gaps](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/concepts/harness-checkpoints.md#L147-L188).
- Basis: structural.
- Confidence: high about current nonclaim; no live fitness evaluation executed.
- Caveats: Future policy-candidate research could become S4 at a different supported release/boundary.

### Absence scope

- Surfaces inspected: checkpoint concept, policy manifest, target evolution path, research-only executable, current implementation/status and published CLI modes.
- Plausible first-party paths checked: environment scanning, model-task profiling, adaptation option comparison, registry publication, autonomous promotion/rollback and present S3 installation.
- Why no material first-party path remains: Current workspace expressly lacks a serving selector and autonomous live promotion; research-only fixture tools cannot be imported into installed runtime S4 governance.

## S5

- State: —
- Function: Legitimately decide ultimate identity and final-purpose values for the running coding organization.
- Disturbance / variety regulated: Unsafe code execution, unauthorized tools, untrusted inputs, incompatible user values and incomplete sandbox coverage.
- Decisive decision or feedback right: Human operator chooses task, permissions and verification; developer-maintained host denies policy/authority escalation. No model makes legitimate ultimate purpose/policy judgments for the running organization.
- Decision owner: Human and fixed host policy. The public OSS project lead separately retains final development override, without becoming runtime agent S5.
- Supporting / enforcement mechanisms: Four permission modes, `--ask-permissions`, opt-in Seatbelt/bubblewrap, runtime capability budgets, unmodifiable host constraints and human project ownership contract.
- Closure path: Operator/human policy → bounded host capability gate → permitted/denied tool effect. No first-party agent-originated ultimate policy adjudication with a governing return into S3/S4.
- Why this is / is not agent-owned: Policy enforcement is meaningful, but the model is specifically prevented from granting capabilities or modifying fundamental authority.
- Evidence: [runtime warning and config](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/README.md#L29-L50), [workflow fixed authority limits](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/docs/project/decisions/0002-model-directed-workflow-topology.md#L33-L49), [human project governance](https://github.com/Plantcore-AI/Iteron/blob/c146d7128a827c517732381a2a9722196677b0bd/AGENTS.md#L5-L20).
- Basis: structural.
- Confidence: high that final authority is external.
- Caveats: Default execution is unconfined and bypasses permission prompts per source status; this security limitation is not evidence of agent-held S5.

### Absence scope

- Surfaces inspected: user permission modes, confinement options, workflow policy gate, model budget restrictions and human OSS policy/ownership.
- Plausible first-party paths checked: role/system prompt, legitimate final values, tool approval, project lead override and capability-gate effects.
- Why no material first-party path remains: The host enforces human-defined authority and the coding model cannot legitimately redefine the organization's ultimate identity or policy.

## Distributed OSS parent arrangement

`OWNERSHIP.md`, `GOVERNANCE.md` and `AGENTS.md` assign development boundaries and final override to humans. They govern contributors to the source project, not the S3–S5 rights of an installed coding session; repo-only research controls similarly remain adjacent.

## Self-hosted and non-human modes

Users can run the CLI locally with remotely hosted model providers and execute bounded headless workflows. Optional confinement changes host trust, and model-chosen child work is autonomous at task level. The standard workflow's human-required verifier and conflict resolution remain external interventions, not an autonomous metasystem.

## Recursion

Root coding model and individually bounded leaf model workers are S1 at the chosen session organization. Workflow scheduling and writer serialization protect their lower-level execution relation. The offline checkpoint/research plane and OSS human maintainers operate at distinct boundaries and do not automatically add S2–S5 autonomy.

## Variety and escalation

Provider/tool results and child reports return to the root model. Conflicting writer patches fail closed with a human-resolution message; budget overruns, missing verifiers and untrusted effects are denied at the host. Such protections are substantive but do not show autonomous cross-cell settlement, whole-current management, complementary S3 audit, strategic adaptation or ultimate governance.

## Evidence gaps

- Source only: no provider-backed root/child workflow, competing writer transactions or conflict recovery was executed.
- The repository distinguishes published v0.0.20 from pinned source v0.0.21; documented prospective architecture must not be presented as released functionality.
- Research candidate counts and design promises are not empirical task-outcome or autonomous S4 measurements.
