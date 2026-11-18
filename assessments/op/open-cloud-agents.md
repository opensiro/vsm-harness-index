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
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: ?
autonomy_s5: P
---

# Open Cloud Agents

## Review boundary

- System in focus: One configured source-review cell combining the public Python BlackboardRunner specialist model library, first-party preflight/triage CLI, and CODEOWNER-authorized disposition.
- Purpose and identity: Evaluate changed cloud configuration using model-specialist findings, direct-source checks and controlled human risk acceptance.
- Relevant environment: Git diffs, security/cost risks, provider results, separately installed scanners, code owner decisions and incident lessons.
- Standard-distribution boundary: The public Python package, its ModelProvider/BlackboardRunner, shipped scanner/triage/report/learn CLI, SQLite store and repository policy manifests.
- Credited operating / distribution surfaces: Importable and tested BlackboardRunner.run(diff) using a real provider; CLI preflight and triage, persisted findings and CODEOWNER gate resolutions.
- Adjacent first-party surfaces excluded from ownership: The simulated six-stage agent_pipeline.py launched by CLI run, demo figures, CI, tests and sample orchestration output. External IDE coding-agent behavior and model/scanner vendors are not credited as first-party decision owners.
- First-party operating / deployment modes considered: Programmatic model-backed Python review, deterministic preflight/triage, authorized human risk resolution, user-supplied learn and prompt sync.
- Recursion level: One repository changeset/security-review cell, not a production cloud enterprise with seven running agent teams.
- Reviewed revision: open-cloud-agents/ocagents@116f89171931e16cd7194122354815937b6ebef3.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The first-party importable Python BlackboardRunner selects specialists based on diff risk, calls configured ModelProvider through schema-bounded retries, and persists provenance-marked findings in SQLite. Thread-pool specialists use a shared pre-run snapshot and can publish findings independently. Separately, CLI preflight runs source-scanning tools and refuses to silently pass missing required checks; triage categorizes model assertions and needs owner review before high-risk pending findings clear. Importantly, CLI run launches a script whose six stages are hardcoded synthetic outputs regardless of the provider flag, so it is excluded as an operational actor. The CLI learn updates AGENTS.md from a user-provided fact, without demonstrating that this file is consumed by subsequent first-party model prompts. Evidence: [src/ocagents/orchestration/blackboard_runner.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [src/ocagents/orchestration/__init__.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/__init__.py), [src/ocagents/providers/retry.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/providers/retry.py), [src/ocagents/cli.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/cli.py), [scripts/agents/agent_pipeline.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/scripts/agents/agent_pipeline.py), [src/ocagents/triage/gate.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/gate.py).

## Operational model

True agentic S1 is a provider-backed specialist generating evidence-bound security findings, not the deterministic preflight or demonstration stage. Parallelism, task routing, dedup and blackboard do not prove S2-specific inter-agent coordination. CODEOWNER dispositions give a supported parent current-control role for the whole PR; independently configured static scans can construct a complementary inspection path. Human policy for security rules, signed exceptions and owner authority is returned via future CLI admission gates. No confirmed durable future adaptation from learned AGENTS.md facts into this programmatic runner is established.

## S1 — Operations

- State: A
- Function: Produce changeset-specific model-selected specialist security/cloud findings.
- Disturbance / variety regulated: Changed source diff and previously unreported risk.
- Decisive decision or feedback right: Actual provider-backed specialist chooses findings, supporting location, severity and recommendations, then persists schema-validated results.
- Decision owner: Configured model specialist invoked via first-party BlackboardRunner Python API, not the deterministic CLI demonstration.
- Supporting / enforcement mechanisms: Triage classification, specialist persona, retry engine, provider adapters, schema validator and SQLite blackboard.
- Closure path: Real diff and existing findings to provider model, verified structured findings to SQLite, then report/triage to owner.
- Boundary reachability: Public Python BlackboardRunner is exported, configured with real ModelProvider, and tested. In contrast, CLI run delegates to synthetic hardcoded six-stage script, which is excluded as an autonomy witness.
- Why this is / is not agent-owned: Without the provider model the runner has no substantive agent-selected specialist findings.
- Evidence: [src/ocagents/orchestration/blackboard_runner.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [src/ocagents/providers/retry.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/providers/retry.py), [tests/test_blackboard_runner.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/tests/test_blackboard_runner.py), [scripts/agents/agent_pipeline.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/scripts/agents/agent_pipeline.py)
- Basis: structural
- Confidence: moderate
- Caveats: The finding is bounded to the pinned first-party mode; no independent external model execution was performed.


## S2 — Coordination

- State: —
- Function: Regulate reviewer-versus-reviewer interference within this change review.
- Disturbance / variety regulated: Parallel specialist disagreements or competing findings.
- Decisive decision or feedback right: No shipped S2-specific arbiter chooses an inter-reviewer remedy returning into later specialist behavior.
- Decision owner: No qualified inter-S1 coordination owner shown.
- Supporting / enforcement mechanisms: ThreadPoolExecutor, shared blackboard snapshot, TOON projections, dedup, per-agent budgets.
- Closure path: Concurrent specialists publish findings; shared records and dedup alone do not close feedback about reviewer interference.
- Boundary reachability: Supported first-party package path at pinned revision, with stated mode prerequisites.
- Why this is / is not agent-owned: Generic parallel task sequencing and shared context are not evidence of S2.
- Evidence: [src/ocagents/orchestration/blackboard_runner.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [src/ocagents/blackboard/dedup.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/blackboard/dedup.py)
- Basis: structural
- Confidence: moderate
- Caveats: The finding is bounded to the pinned first-party mode; no independent external model execution was performed.

### Absence scope
- Surfaces inspected: Python reviewer fan-out, blackboard, risk classifier, scanner and data flow.
- Plausible first-party paths checked: Distinct S1 reviewer conflict witness, decisive arbiter and subsequent changed specialist action.
- Why no material first-party path remains: The shipped fan-out reads a shared snapshot and stores findings; no concrete distinct inter-S1 conflict-control loop is established.


## S3 — Inside-and-now control

- State: P
- Function: Current whole-changeset security admission, risk disposition and required remediation.
- Disturbance / variety regulated: Unresolved P0/P1 claims, unverified model output and absent required scans.
- Decisive decision or feedback right: CODEOWNER may verify, accept or dismiss concrete blocking findings so an active PR gate can remain held or proceed.
- Decision owner: Authorized repository maintainer in supported human parent mode.
- Supporting / enforcement mechanisms: Triage gate aggregates unresolved findings; CODEOWNERS validation, persisted resolutions and GitHub status integration enforce decisions.
- Closure path: Findings trigger pending gate, owner reviews and resolves, updated status gates following PR admission.
- Boundary reachability: Repository CODEOWNER deployment with real GitHub status/check enabled is a first-party CLI/API-supported mode, not guaranteed in a bare local scan.
- Why this is / is not agent-owned: This is a whole-PR change-level owner decision, not the deterministic classifier choosing policy or a cloud-enterprise supervisor.
- Evidence: [src/ocagents/triage/gate.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/gate.py), [src/ocagents/triage/resolution.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/resolution.py), [src/ocagents/cli.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/cli.py)
- Basis: structural
- Confidence: moderate
- Caveats: The finding is bounded to the pinned first-party mode; no independent external model execution was performed.
- Whole-system current view: Aggregated active PR findings and their unverified, tool-verified and human-verified states.
- Current-control decision scope: Human CODEOWNER determines disposition of blocking findings and whether the current changed source remains held or becomes eligible for merge.


## S3* — Complementary audit

- State: C
- Function: Complementary direct-source audit of model-generated risk findings.
- Disturbance / variety regulated: Model hallucination or omissions vs actual source security policy.
- Decisive decision or feedback right: An independently sourced scanner finding and owner adjudication can corroborate/refute a model claim.
- Decision owner: Separate deterministic scanner executor and human reviewer when configured; not the original model.
- Supporting / enforcement mechanisms: Preflight adapters for Checkov, Trivy, CodeQL and OPA; separate model/tool provenance markers and human triage resolution.
- Closure path: Actual changed source to external scanner through first-party adapter, distinct tool finding to owner, owner updates corroboration and next gate outcome.
- Boundary reachability: CLI preflight and triage paths are public and independently configured; a continuously running independent reviewer is not included automatically.
- Why this is / is not agent-owned: Constructible path with independent source access; ordinary model self-report and same-loop scoring do not qualify.
- Evidence: [src/ocagents/scanner/preflight.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/scanner/preflight.py), [src/ocagents/triage/gate.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/gate.py), [src/ocagents/triage/resolution.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/resolution.py)
- Basis: structural
- Confidence: moderate
- Caveats: The finding is bounded to the pinned first-party mode; no independent external model execution was performed.
- Claim being audited: Model-produced risk statement about the change.
- Ordinary reporting path: Blackboard model_assertion records and synthesized reports.
- Complementary access path: Source-scanning adapters run on actual diff/files, returning tool-verified evidence.
- Independence boundary: Separate tool execution and authorized CODEOWNER adjudication, not model self-validation.
- Who acts on findings: Maintainer accepts/dismisses findings or holds PR via triage state.


## S4 — Outside-and-then intelligence

- State: ?
- Function: Adapt future review capability using external incidents, postmortems and learning.
- Disturbance / variety regulated: New operational risks or past missed failure modes.
- Decisive decision or feedback right: User decides which learned fact to append to AGENTS.md; first-party consumption of those facts by future Python agent prompts is unproven.
- Decision owner: Potential human repository owner; a full first-party prospective feedback closure is not proven.
- Supporting / enforcement mechanisms: CLI learn adds categorized deduplicated AGENTS.md facts; sync exports individual agent specs to IDEs.
- Closure path: Incident/fact to durable AGENTS.md succeeds, but BlackboardRunner builds prompts from individual agent specs, diff and blackboard, not this updated file.
- Boundary reachability: Command learn is released and reachable, but a material exact shipped path from AGENTS.md into later first-party model decisions is unresolved.
- Why this is / is not agent-owned: A persisted document is not by itself future agent adaptation; CLI run also uses synthetic outputs.
- Evidence: [src/ocagents/cli.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/cli.py), [src/ocagents/orchestration/blackboard_runner.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/orchestration/blackboard_runner.py), [docs/how-to-use-agents.md](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/docs/how-to-use-agents.md)
- Basis: structural
- Confidence: moderate
- Caveats: The finding is bounded to the pinned first-party mode; no independent external model execution was performed.


## S5 — Policy and identity

- State: P
- Function: Define ultimate security-review identity and legitimate exception/approval authority.
- Disturbance / variety regulated: Unapproved high-impact changes, expired exceptions and unauthorized bypass of guardrails.
- Decisive decision or feedback right: Maintainer sets repository rules, signed time-limited exceptions, agent-tool scope and CODEOWNER approval policy.
- Decision owner: Legitimate repository parent owner; models cannot ratify these ultimate rights.
- Supporting / enforcement mechanisms: Policy and Rego files, signed exception manifest, CODEOWNERS authorization and validated gate state.
- Closure path: Owner-approved policy file or exception persists; subsequent preflight/triage reads it and enforces later changes and authorization.
- Boundary reachability: Released CLI reads and applies policies and owner constraints; scoped to repository review, not broader cloud-service enterprise.
- Why this is / is not agent-owned: Risk classifier and scanner enforce decisions but do not own the policy mandate.
- Evidence: [rules/README.md](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/rules/README.md), [policies/rego/rule_01_destructive_actions.rego](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/policies/rego/rule_01_destructive_actions.rego), [src/ocagents/scanner/exceptions.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/scanner/exceptions.py), [src/ocagents/triage/resolution.py](https://github.com/open-cloud-agents/ocagents/blob/116f89171931e16cd7194122354815937b6ebef3/src/ocagents/triage/resolution.py)
- Basis: structural
- Confidence: moderate
- Caveats: The finding is bounded to the pinned first-party mode; no independent external model execution was performed.
- Identity / ultimate-policy issue: Which risks, exceptions, allowed tools and reviewer rights are valid for repository change admission.
- Ultimate authority in each claimed mode: Authorized human CODEOWNER/maintainer.
- Return-to-operation path: Updated repository policy is consumed by later preflight and gate/approval checks.


## Distributed OSS parent arrangement

Each self-hosted consumer operates a separate review cell; upstream project contributors do not provide a universal organization parent. The P modes describe only configured repository maintainer authorization, with source-backed return into that local change-admission process.

## Self-hosted and non-human modes

Programmatic BlackboardRunner runs real agent-specialist decisions when supplied a provider and diff (S1=A). The standard CLI run demonstration does not. S3/S5 retain a legitimate human CODEOWNER; a tool-scanning S3* is constructible but not universally active. The first-party learn path is document persistence, not evidenced autonomous future control.

## Recursion

One repository's review and admission process. Remote cloud tenants, downstream IDE agents and original provider runtime ownership remain outside this assessed boundary.

## Variety and escalation

Risk tiers control when specialists are invoked; schema retries limit model-output errors; fail-closed preflight blocks missing checks; unverified P0/P1 claims require authorization. These gates cannot substitute for an S2 conflict regulator, independent running S3* owner or closed S4 future-adaptation loop.

## Evidence gaps

No live provider inference or independent audit session was run. CLI run uses hardcoded simulation despite model provider flags. The scanner and owner gate modes require tools/authorization configuration. The shipped Python runner does not ingest new AGENTS.md lessons in its specialist prompt, leaving S4=? rather than a speculative positive or unsupported universal absence.
