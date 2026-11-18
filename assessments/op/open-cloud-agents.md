---
harness_id: open-cloud-agents
project_name: Open Cloud Agents
repository: https://github.com/open-cloud-agents/ocagents
review_ref: 116f89171931e16cd7194122354815937b6ebef3
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Open Cloud Agents

## Review boundary

- System in focus: First-party specialist findings and review-gate organization.
- Purpose and identity: Produce and resolve structured infrastructure changeset findings for engineering review.
- Relevant environment: Local repositories, diffs, operator-supplied provider access, and optional target repository review-status integration.
- Standard-distribution boundary: Repository-backed Python package and source assets at the pinned commit. The review host and model service are external.
- Credited operating / distribution surfaces: Exported specialist runner, local findings store and configured triage/report commands. See [package contract](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/pyproject.toml) and [shipped execution components](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/docs/implementation-backlog.md#L130-L153).
- Adjacent first-party surfaces excluded from ownership: Staged simulator, benchmark and project CI/release governance, IDE prompt export, and roadmap proposals.
- First-party operating / deployment modes considered: Python API with first-party role, schema and store assets. Configured operator review of that stored result through the CLI.
- Recursion level: One changeset review organization; individual specialists operate within it.
- Reviewed revision: `116f89171931e16cd7194122354815937b6ebef3`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [specialist runner](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py) starts risk-tiered specialists, projects a shared snapshot into their prompts and persists validated findings and telemetry in a [SQLite finding store](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/blackboard/store.py). The packaged provider adapters supply model inference to the first-party [bounded generation and retries](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/providers/retry.py#L89-L198). The report, triage and resolution commands can consume stored findings. The similarly named CLI `run` leads to the [scripted pipeline](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/scripts/agents/agent_pipeline.py#L210-L332), whose staged result payloads are predetermined even if a provider flag is supplied. The separately exported Python execution path supplies the credited model-backed operation.

## Operational model

Specialists produce scoped assessment results, such as cost or reliability findings, from the selected changeset. Risk rules, budgets, transaction semantics and status publication are supplied by the program. The target maintainer has bounded review disposition authority through the configured triage path. The review package neither operates the target cloud infrastructure nor owns the external model service.

## S1 — Operations

- State: A
- Function: Produce distinct specialist review findings from an infrastructure changeset.
- Disturbance / variety regulated: Different risk tiers, heterogeneous diffs, malformed findings, and bounded model-call resources.
- Decisive decision or feedback right: Within an activated specialist, decide which evidence supports a finding, what finding to return, or whether the result should be empty.
- Decision owner: The provider-backed specialist operating in the first-party runner. The operator configures the provider, and the runner applies its risk and execution rules.
- Supporting / enforcement mechanisms: Risk-tier activation, bounded diff projection, provider schema, retry budget, SQLite persistence and per-specialist telemetry.
- Closure path: Accepted output is persisted under its run along with a publish receipt. Invalid output returns to the specialist as validation feedback within the retry budget.
- Boundary reachability: The exported Python runner contains this path and composes the store and model adapter. See [package export](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/__init__.py) and [shipped execution components](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/docs/implementation-backlog.md#L130-L153).
- Why this is / is not agent-owned: Removing the specialist leaves risk classification and storage but removes discretionary review findings.
- Evidence: [specialist runner](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [bounded generation and retries](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/providers/retry.py#L89-L198), [SQLite finding store](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/blackboard/store.py), [runner tests](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/tests/test_blackboard_runner.py).
- Basis: explicit and structural
- Confidence: high for the repository-backed API mode
- Caveats: The scripted run command does not use this path. Finding generation is an operational review outcome; cloud remediation and deployment are outside it.

## S2 — Coordination

- State: —
- Function: Regulate interference between distinct review specialists working on the same changeset.
- Disturbance / variety regulated: Duplicate reports and potentially conflicting claims across specialist scopes.
- Decisive decision or feedback right: No qualifying inter-specialist decision is established.
- Decision owner: Store deduplication is deterministic; each activated specialist selects its findings.
- Supporting / enforcement mechanisms: Risk-based assignment, parallel executor, common initial findings projection and transactional deduplication.
- Closure path: The store combines duplicate outputs. The runner captures existing findings before dispatch and passes the same snapshot to parallel and serial workers.
- Why this is / is not agent-owned: Merge and provenance logic stabilizes the output record without binding the later actions of interfering operational units.
- Evidence: [specialist runner](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [SQLite finding store](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/blackboard/store.py), [concurrent duplicate tests](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/tests/test_blackboard_concurrency.py).
- Basis: structural
- Confidence: medium
- Caveats: A seeded run can show earlier findings as context. The examined path supplies no function-specific arbitration response that redirects both specialists' later work.

### Absence scope

- Surfaces inspected: Both execution branches, prompt projection, finding publication, deduplication and concurrent-store tests.
- Plausible first-party paths checked: Same-finding collision, serial versus parallel specialist feedback, and conflict resolution via stored findings.
- Why no material first-party path remains: Publication merges result records, while dispatch never reloads the peer result into the remaining work within the run. No distinct coordination decision partitions work or returns binding conflict resolution to the specialists.

## S3 — Inside-and-now control

- State: P
- Function: Control the current review commitment for a changeset when consequential specialist claims remain unresolved.
- Disturbance / variety regulated: High-severity unverified claims block ordinary progression of the assessed review.
- Whole-system current view: The gate evaluates the entire selected review finding set by severity and resolution status, and identifies blocking claims and responsible reviewers.
- Current-control decision scope: Keep the review on hold or resolve the relevant claim to release the commitment; other unresolved high-severity claims continue holding it.
- Decisive decision or feedback right: Accept or dismiss an escalated finding for this review and supply the resulting disposition.
- Decision owner: Authorized maintainer in the documented per-finding CODEOWNERS path.
- Supporting / enforcement mechanisms: Finding store, CODEOWNERS check, automated current status calculation and optional commit-status synchronization.
- Closure path: The return updates the persisted resolution and reevaluates the aggregate gate. The configured GitHub path writes the resulting status for the changeset.
- Boundary reachability: The shipped triage command accepts a stored run, routes the per-finding resolution and reevaluates the gate. See [command reference](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/docs/cli-reference.md) and [CLI](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/cli.py).
- Why this is / is not agent-owned: No autonomous specialist may make the maintainer's discretionary finding disposition. Risk-tier dispatch and token constraints follow predefined rules.
- Evidence: [CLI](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/cli.py), [triage gate](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/gate.py), [maintainer resolution](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/resolution.py), [resolution tests](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/tests/test_triage_resolution.py).
- Basis: explicit and structural
- Confidence: medium
- Caveats: Scope is the configured review gate for a supplied run. Whether a target repository requires the status for merging is a deployment policy.

## S3* — Complementary audit

- State: ?
- Function: Potential complementary check of specialist findings using evidence outside their ordinary reporting.
- Disturbance / variety regulated: A plausible finding can have a syntactically valid anchor and still be factually mistaken.
- Decisive decision or feedback right: Independent selection and adjudication of direct evidence against an operational claim.
- Decision owner: Unresolved for a first-party complementary audit mode.
- Supporting / enforcement mechanisms: The deterministic preflight, provenance validator, report, and maintainer triage support evidence handling.
- Closure path: Maintainer triage changes the gate (S3). An independently controlled path from direct inspection to that decision is not demonstrated.
- Why this is / is not agent-owned: Routine schema and anchor checks verify a finding's structure or location. The runner can use the same changeset and earlier findings for several specialist outputs.
- Evidence: [provenance validator](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/findings/provenance.py), [preflight implementation](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/scanner/preflight.py), [specialist runner](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [maintainer resolution](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/resolution.py).
- Basis: structural and unknown
- Confidence: medium that the audit judgment remains unresolved
- Caveats: There is a concrete raw-source/corroboration candidate next to the return path. The inspected evidence does not settle who independently initiates and decides such an audit in the credited mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: Use prospective environmental distinctions to revise how future reviews operate.
- Disturbance / variety regulated: External changes that might require a new specialist, scanner or review policy.
- Decisive decision or feedback right: No operating path selects and returns a future-oriented capability change.
- Decision owner: The operator supplies incident facts; the repository maintainers own source changes outside the assessed runtime.
- Supporting / enforcement mechanisms: The learn command records facts or extracts text from a supplied incident report. Benchmarking and release updates are separate operations.
- Closure path: The learn command writes AGENTS.md. The specialist runner loads its per-role prompt file and does not consume the learned-fact section as an adaptation decision.
- Why this is / is not agent-owned: The reviewed route stores retrospective information and does not compare future scenarios or choose capability changes.
- Evidence: [incident ingestion](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/cli.py#L661-L728), [specialist runner](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [benchmark runner](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/benchmark/runner.py).
- Basis: structural
- Confidence: medium
- Caveats: Learned facts may inform a surrounding IDE agent or later project development. Those modes have no evidenced return into the credited specialist runtime.

### Absence scope

- Surfaces inspected: Learning command, specialist prompt loading, benchmark runner and packaging/CLI update route.
- Plausible first-party paths checked: Incident ingestion into later review capability, benchmarking feedback into provider/roster selection, and release update as an adaptation return.
- Why no material first-party path remains: The shipped paths store incident material, evaluate outputs, or obtain releases independently; none derives a prospective option and returns an authorized choice into the current review capability.

## S5 — Policy and identity

- State: —
- Function: Set or change the ultimate purpose and policy of the assessed review organization.
- Disturbance / variety regulated: Unresolved tensions involving organizational purpose or ultimate acceptable risk.
- Decisive decision or feedback right: No runtime path for an ultimate-policy issue, decision and return was established.
- Decision owner: Operators select parameters and maintainers own project source policy outside this operating boundary.
- Supporting / enforcement mechanisms: Role instructions, scanner policies, risk classifier and maintainer triage authorization.
- Closure path: Triage returns the disposition of findings in the current review. Policy and prompts are inputs.
- Why this is / is not agent-owned: The authority to resolve a specific review finding does not revise the mandate or policy that governs future reviews.
- Evidence: [triage gate](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/gate.py), [maintainer resolution](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/resolution.py), [specialist runner](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [maintainer contribution rules](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/CONTRIBUTING.md).
- Basis: structural
- Confidence: medium
- Caveats: The project maintainer's release governance is a different recursion.

### Absence scope

- Surfaces inspected: Specialist metadata, gate policy, operator configuration, triage resolution, and project contribution rules.
- Plausible first-party paths checked: Escalation to CODEOWNERS, policy input selection, and editing or upgrading runtime instructions.
- Why no material first-party path remains: The only traced in-product escalation resolves current findings. No operating feedback path raises a purpose/ultimate-policy matter and applies the returned authoritative decision to later operation.

## Recursion

Review specialists are operational units within the review system. The source shows no complete lower-recursion viable systems inside them. A target repository maintainer acts as parent for the bounded current review gate.

## Variety and escalation

Risk tiers route input variety. Schema feedback and bounded retries handle malformed output. Unresolved high-severity finding sets can hold the review while an authorized maintainer evaluates the case.

## Evidence gaps

The live provider and target repository status were not exercised. The complementary evidence path for S3* remains unresolved at this pin. The assessment credits the source-backed review API and the configured operator gate; it does not infer provider-backed operation from the CLI simulator or future roadmap.
