---
harness_id: q-agent-harness
project_name: q-agent-harness
repository: https://github.com/kju4q/q-agent-harness
review_ref: 37903fc742420f56e9568c6b45c9b89035a49139
reviewed_at: 2026-10-27
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

# q-agent-harness

## Review boundary

- System in focus: The first-party content-loop procedure installed into its documented Claude Code/Cursor host, plus shipped memory-maintenance scripts; not the external hosts' whole governance.
- Purpose and identity: Produce draft content through file-based plan/generate/verify/fix iteration and support reliable agent work with reusable context/memory.
- Relevant environment: User topics, draft/plan files, a separately installed tool-capable agent host and local memory files.
- Standard-distribution boundary: content-agent-loop/README.md explicitly directs copying loop.md into a supported agent environment and supplying a topic. Credit that exact ready-to-run role/procedure; no custom coordinator or new runtime is invented.
- Credited operating / distribution surfaces: [content-agent-loop/README.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/README.md); [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md); [scripts/compact](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/compact); [scripts/hotmem](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/hotmem); [scripts/log-task](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/log-task)
- Adjacent first-party surfaces excluded from ownership: Root AGENTS.md guides contributors to this educational repository. WorkspaceHub examples/demo/tests and tutorial descriptions of Claude/Hermes/Grok/Harness² are adjacent teaching/comparison surfaces, not owners of the installed content-loop functions. Separately suggested reviewer models/cron remain optional future composition.
- First-party operating / deployment modes considered: Copy/paste the shipped content loop into a supported tool-capable agent and provide a topic; standalone compact/hotmem/log-task utilities; manual memory review and harness-edit comparison recipes examined separately.
- Recursion level: One installed content-production cell, with memory-maintenance support.
- Reviewed revision: `37903fc742420f56e9568c6b45c9b89035a49139`
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The reusable loop is Markdown rather than a bundled inference server: the supported external host supplies model/file tools and execution machinery. The first-party procedure directs plan.md creation, draft.md generation, file inspection, critique-driven edits, and bounded retries before replanning. The human reviews only the final draft. Memory utilities are Bash log-task/hotmem and Python compact. compact invokes claude -p to propose repeating-lesson promotions, parses structured results and asks the operator before each write. These internal-memory proposals are not a future-environment strategy loop. Generic code/examples and verification instructions do not automatically join the content role's runtime.

## Operational model

The documented assembled mode assigns the content agent a durable draft outcome and local choices about plan, text, defect correction and termination. Host model/file tools support those choices; they are explicitly required dependencies rather than borrowed governance. No developer must invent the iterative procedure after installation. compact is separately a proposal-generation helper with human-owned promotion, not an autonomous promotion authority.

## S1 — Operations

- State: A
- Function: Transform a topic into a finished draft with autonomous file-backed iteration.
- Disturbance / variety regulated: Draft defects, weak direction, format and factual/clarity problems.
- Decisive decision or feedback right: Choose the plan and content, judge defects, edit the draft and replan after repeated failure.
- Decision owner: The agent enacting the shipped content-loop role in the explicitly supported host.
- Supporting / enforcement mechanisms: External host inference/file tools; separate plan.md/draft.md state and iteration instructions.
- Closure path: Agent creates plan and draft → inspects draft against criteria → edits/revises plan → repeats until done, replanning after five unsuccessful iterations.
- Why this is / is not agent-owned: The host supplies machinery while the installed agent selects content and corrective actions. Markdown implementation does not by itself preclude agent ownership. Only this concrete supported role is credited, not all generic toolkit aspirations.
- Evidence: [content-agent-loop/README.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/README.md); [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Host-dependent prompt-level execution; no bundled inference runtime or live compliance/quality demonstration is claimed.
- Boundary reachability: README supplies the installation trigger (copy loop.md into Claude Code/Cursor and give a topic); loop.md contains the complete role/action/feedback instructions, with no bespoke local workflow required.

## S2 — Coordination

- State: —
- Function: No material inter-S1 coordination path in the supported content cell.
- Disturbance / variety regulated: Content revisions are local to one acting agent.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Separate plan/draft files and phases are state separation, not distinct S1 units. A separate reviewer is an advanced customization, not an installed collision-regulation path.
- Evidence: [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md); [README.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/README.md); [VERIFICATION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/VERIFICATION.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md); [README.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/README.md); [VERIFICATION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/VERIFICATION.md)
- Plausible first-party paths checked: Content phases, advanced reviewer model/scheduler suggestions, external review instructions and memory utilities.
- Why no material first-party path remains: No concrete conflict between distinct operational units plus an attenuating first-party coordination loop is supplied at this boundary.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control function beyond local work and operator approvals.
- Disturbance / variety regulated: Repeated draft failure and memory size need management.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Five-iteration replanning and memory token bounds are local operational rules; operator approval of a memory promotion is not whole-current resource/commitment regulation.
- Evidence: [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [scripts/compact](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/compact); [scripts/hotmem](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/hotmem); [COMPACTION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/COMPACTION.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [scripts/compact](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/compact); [scripts/hotmem](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/hotmem); [COMPACTION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/COMPACTION.md)
- Plausible first-party paths checked: Retry/replanning rule, hot-memory budget, promotion preview/approval/write and monthly review.
- Why no material first-party path remains: No current whole-system view with a supervisory decision right over team commitments/resources is established. The operator's ordinary promotion choice does not supply S3=P.

## S3* — Complementary audit

- State: —
- Function: No complementary independent audit path in the installed role.
- Disturbance / variety regulated: Self-critique can reproduce the writer's blind spots.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: The content agent reviews its own draft; the guide's external-review prompt is ordinary end-of-project acceptance, with a separate model left as advanced composition.
- Evidence: [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md); [VERIFICATION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/VERIFICATION.md); [docs/harness-loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/docs/harness-loop.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md); [VERIFICATION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/VERIFICATION.md); [docs/harness-loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/docs/harness-loop.md)
- Plausible first-party paths checked: Self-critique, fresh-context external acceptance review, golden examples and manual baseline/variant comparison.
- Why no material first-party path remains: These are routine production/verification or a manually assembled comparison recipe. No complementary audit owner with alternative operational access and a corrective-control return is wired into this role.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation loop established.
- Disturbance / variety regulated: Repeating task lessons and stale memory affect later outputs.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: compact and monthly review improve internal procedures from past task logs. The Harness² recipe replays an already failed task; describing outside research does not itself close a prospective environmental adaptation function.
- Evidence: [scripts/compact](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/compact); [COMPACTION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/COMPACTION.md); [docs/harness-loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/docs/harness-loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [scripts/compact](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/compact); [COMPACTION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/COMPACTION.md); [docs/harness-loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/docs/harness-loop.md); [content-agent-loop/workflow.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/workflow.md)
- Plausible first-party paths checked: Model-generated rule promotions, manual approvals, recurring memory review, harness-edit compare/keep/log recipe and topic research.
- Why no material first-party path remains: No specific future-environment distinctions are turned into adaptation options with a coupled current-control return; generic learning and research for the current content task are insufficient.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy decision-and-return loop.
- Disturbance / variety regulated: Risky operations and persistent memory rules constrain agent behaviour.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: The example approval policy and per-proposal yes/no gate govern operational changes; generic hot-memory rules do not establish an identity-level issue and legitimate ultimate-authority return.
- Evidence: [scripts/compact](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/compact); [COMPACTION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/COMPACTION.md); [docs/approval-policy.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/docs/approval-policy.md); [AGENTS.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/AGENTS.md); [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [scripts/compact](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/scripts/compact); [COMPACTION.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/COMPACTION.md); [docs/approval-policy.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/docs/approval-policy.md); [AGENTS.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/AGENTS.md); [content-agent-loop/loop.md](https://github.com/kju4q/q-agent-harness/blob/37903fc742420f56e9568c6b45c9b89035a49139/content-agent-loop/loop.md)
- Plausible first-party paths checked: Human memory-promotion decisions, contributor escalation, example dangerous-action approvals and role identity text.
- Why no material first-party path remains: None supplies a function-specific identity-policy issue → authority judgment → returned binding identity decision. The adjacent contributor rules are not runtime governance of the content cell.

## Distributed OSS parent arrangement

Operator memory approval is local to a support utility. The public repository does not establish project-wide distributed parent S3/S4/S5 authority over installed independent host sessions.

## Self-hosted and non-human modes

Supported hosts supply execution machinery, while first-party Markdown supplies the credited content role. Custom reviewer, scheduler, tool permissions or research organizations must not be imported from the host or tutorial links.

## Recursion

Plan/generate/verify/fix are phases in one cell, not recursive viable systems. No worker metasystem or recursive viability is established.

## Variety and escalation

The role limits repeated revisions before replanning. Utility parsing, EOF-as-rejection and exact preview prevent unsupported memory writes; human review remains a visible decision. These are not automatically algedonic channels.

## Evidence gaps

No live host/model run or content-quality evaluation. Bash syntax checks, both Bash --help entry points, hotmem check of the shipped example and Python compact compilation passed. Initial attempts to interpret Bash utilities as Python were corrected to their declared shebang; this was an assessor command error, not an upstream defect. Educational Vitest snippets have no packaged native test runner; no Vitest PASS claimed. No root LICENSE observed; no license is inferred.
