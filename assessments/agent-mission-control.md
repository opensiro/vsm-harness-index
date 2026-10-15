---
harness_id: agent-mission-control
project_name: Agent Mission Control
repository: https://github.com/ipanalytics/Agent-Mission-Control
review_ref: 0fe9acd4807b149a5c9c07390d195b95ffa87780
reviewed_at: 2026-10-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-14
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Mission Control

**Canonical disposition:** `excluded-no-agentic-vsm`. This is the reviewed source-first disposition for [Index batch #1537](https://github.com/opensiro/vsm-harness-index/issues/1537), row 1, frozen from intake #1281.

## Review boundary

- System in focus: local-first first-party Python CLI and shipped modules at `0fe9acd4807b149a5c9c07390d195b95ffa87780`.
- Purpose and identity: provide contract-scoped phase instructions, policy/scope checks and an evidence/reporting layer around external coding agents.
- Relevant environment: Python 3.11, git checkout, YAML contract, user/operator, external Codex/Claude/Hermes host, CI and human review.
- Standard-distribution boundary: `src/agent_mission_control` CLI, contracts, planning, runs, risk/scope, evidence and reporting. External host model inference, coding/tool actions and human approval are **not** AMC-owned.
- Credited operating / distribution surfaces: `README.md`, `docs/architecture.md`, `docs/safety-model.md`, `src/agent_mission_control/*.py`, shipped CLI, policy/templates and documented adapters.
- Adjacent first-party surfaces excluded from ownership: eval fixtures, unit tests, CI/contributor flows, documentation-only Builder/Verifier roles, generated external-host instruction files when no corresponding executable AMC agent is shipped.
- First-party operating / deployment modes considered: local CLI and CI use; mission init, static plan/goal, check scope and command risk, ingest evidence, report, replay, host bootstrap.
- Recursion level: one local mission/control utility around one or more **externally operated** coding hosts, without an AMC-internal autonomous agent recursion.
- Reviewed revision: 0fe9acd4807b149a5c9c07390d195b95ffa87780.
- Observation date: 2026-10-14.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`cli.py` exposes individually invoked deterministic commands for validation, mission creation, static phase-plan generation, scope and risk checks, command-evidence storage, reports, replay and writing Codex/Claude/Hermes instructions. `planning.py` generates five fixed phase templates and a prompt sent to an **external** agent. `runs.py` and `events.py` store local state/logs. `scope.py` uses a file manifest or git status; `command_risk.py` classifies supplied strings. `evidence.py` records caller-supplied commands, exit codes and text, without executing the commands. `reports.py` computes fixed safety scores. `integrations.py` writes host runbooks, not a model loop.

The architecture calls some intended roles Builder and Verifier, but the public executable CLI does not dispatch an autonomous builder or independent model reviewer. The Hermes adapter explicitly makes Hermes the executor and human review the approver. See [CLI](https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/cli.py), [planner](https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/planning.py), [Hermes adapter](https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/adapters/hermes.md), and [architecture](https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/docs/architecture.md).

Counterfactual owner test: remove Codex, Claude Code, Hermes and human reviewer while leaving AMC installed. Contracts, reports, plans and checks still work; no open-ended coding task can be interpreted, acted on and adaptively completed by AMC. That decisive operational agent loop is external.

## Operational model

Operator authors contract → AMC creates run and phase plan → separately operating coding agent receives instructions and performs semantic work → AMC can check supplied or git-visible changes, append evidence and render reports → external actor decides correction/approval. Real deterministic controls do not supply AMC-owned autonomous S1. The publication vector below is a bounded first-party absence finding, not a claim that AMC lacks useful governance tooling.

## S1 — Operations

- State: —
- Function: Autonomous coding operations are executed by an external model-backed coding host, not by AMC.
- Disturbance / variety regulated: Open-ended coding choices and responses to tool results.
- Decisive decision or feedback right: Select implementation actions and revise them after execution feedback.
- Decision owner: External Codex/Claude Code/Hermes; AMC owns only deterministic local checks and templates.
- Supporting / enforcement mechanisms: Contracts, static phases, run/event ledgers and risk/scope checking.
- Closure path: AMC generates instructions; the separately invoked host runs the task and may feed records back. No AMC model/tool/action loop.
- Boundary reachability: no positive first-party state claimed.
- Why this is / is not agent-owned: Without the external host, the command dispatcher still validates/checks/reports but cannot make task-semantic decisions.
- Evidence: https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/README.md; https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/cli.py.
- Basis: source-level structural / explicit review.
- Confidence: high.
- Caveats: external execution and externally provided agent judgment are outside the credited AMC boundary.

### Absence scope

- Surfaces inspected: CLI commands, static phase generator, host bootstrap, adapters and tests.
- Plausible first-party paths checked: Generated goal, adapter instructions, status/phase files and evidence ingestion.
- Why no material first-party path remains: None dispatches or owns a model-controlled coding turn.

## S2 — Coordination

- State: —
- Function: No qualifying coordination across distinct first-party operational agent S1 units is supplied.
- Disturbance / variety regulated: Potential conflicts between external workers or files.
- Decisive decision or feedback right: Identify an inter-S1 disturbance, attenuate it and feed resolution back into later S1 behavior.
- Decision owner: None established for AMC.
- Supporting / enforcement mechanisms: Fixed phase sequence, path scope ledger and separate run directories.
- Closure path: No first-party worker-team conflict/coordination return path.
- Boundary reachability: no positive first-party state claimed.
- Why this is / is not agent-owned: Sequencing, shared artifacts and file checks are not a complete S2 relation.
- Evidence: https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/planning.py; https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/scope.py.
- Basis: source-level structural / explicit review.
- Confidence: high.
- Caveats: external execution and externally provided agent judgment are outside the credited AMC boundary.

### Absence scope

- Surfaces inspected: Phase plan, run state, scope checks and adapter documentation.
- Plausible first-party paths checked: Conflict between distinct workers, path restrictions, sequencing and mission phase dependencies.
- Why no material first-party path remains: No actual first-party distinct agent S1 units or inter-S1 feedback witness.

## S3 — Inside-and-now control

- State: —
- Function: Human-set task bounds and deterministic status checks exist but autonomous whole-system current control is not shipped.
- Disturbance / variety regulated: Present risk, scope breaches, missing evidence and task-progress statuses.
- Decisive decision or feedback right: Discretionary whole-system allocation, current commitments, priorities and intervention.
- Decision owner: Task sponsor/contract author; fixed AMC validators enforce supplied rules.
- Supporting / enforcement mechanisms: YAML contract, command risk thresholds, scope decisions and safety reports.
- Closure path: Caller provides policy and invokes checks; returned status goes to external executor or human.
- Boundary reachability: no positive first-party state claimed.
- Why this is / is not agent-owned: A fixed command-risk verdict is an enforcement mechanism, not ownership of whole-system current discretion.
- Evidence: https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/contracts.py; https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/command_risk.py.
- Basis: source-level structural / explicit review.
- Confidence: high.
- Caveats: external execution and externally provided agent judgment are outside the credited AMC boundary.

### Absence scope

- Surfaces inspected: Contracts, policy loader, CLI dispatch, reports, scopes.
- Plausible first-party paths checked: Mission state, risk threshold, path boundaries, corrective warnings and status check.
- Why no material first-party path remains: No AMC actor observes and redecides the shared operating commitments of first-party S1 units.

## S3* — Complementary audit

- State: —
- Function: Independent facts such as changed-file paths can be inspected, but no autonomous complementary audit judgment with corrective return is shipped.
- Disturbance / variety regulated: Difference between external agent claims and actual file/command evidence.
- Decisive decision or feedback right: Independently challenge claims and return a judgment changing subsequent management action.
- Decision owner: Deterministic AMC check/report functions plus external human reviewer.
- Supporting / enforcement mechanisms: Changed-file checker, command-evidence record, score and final report.
- Closure path: AMC outputs records and risk scores; separate human/agent must interpret findings and decide remediation.
- Boundary reachability: no positive first-party state claimed.
- Why this is / is not agent-owned: Architecture mentions a verifier, but shipped CLI lacks a separate autonomous auditor/reviewer actor.
- Evidence: https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/reports.py; https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/evidence.py.
- Basis: source-level structural / explicit review.
- Confidence: medium-high.
- Caveats: external execution and externally provided agent judgment are outside the credited AMC boundary.

### Absence scope

- Surfaces inspected: Architecture, CLI, evidence module, scope checker, reports and Hermes review adapter.
- Plausible first-party paths checked: Independent git status, checker failure, recorded exit results, verifier prose and reporting.
- Why no material first-party path remains: No shipped independently owned audit-judgment-to-current-control correction loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective external sensing or selected capability adaptation return loop.
- Disturbance / variety regulated: Future changes to providers, project workflows and task constraints.
- Decisive decision or feedback right: Select adaptation options from future/external distinctions and return them to present capability.
- Decision owner: Human operator, maintainer or an external host.
- Supporting / enforcement mechanisms: Editable policy templates, stored events, replay and host-neutral runbook.
- Closure path: Human revises inputs or hosts; AMC repeats deterministic operations.
- Boundary reachability: no positive first-party state claimed.
- Why this is / is not agent-owned: Recorded history and static plan regeneration are not autonomous adaptation.
- Evidence: https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/replay.py; https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/planning.py.
- Basis: source-level structural / explicit review.
- Confidence: high.
- Caveats: external execution and externally provided agent judgment are outside the credited AMC boundary.

### Absence scope

- Surfaces inspected: Replay, contracts, policies, protocol generator and integration files.
- Plausible first-party paths checked: Report interpretation, archived runs, changed templates and host settings.
- Why no material first-party path remains: No autonomous prospective adaptation judgment affects subsequent first-party capabilities.

## S5 — Policy and identity

- State: —
- Function: AMC accepts caller-defined goals/policies without a first-party ultimate-policy/identity authority loop.
- Disturbance / variety regulated: Legitimate goal, scope, risk and network rules.
- Decisive decision or feedback right: Resolve an ultimate identity/purpose issue with legitimate authority and return the decision to operation.
- Decision owner: External task sponsor/contract author.
- Supporting / enforcement mechanisms: Contract YAML, policy presets and host instruction files.
- Closure path: User authors limits; AMC validates them; external agent consumes the resulting instructions.
- Boundary reachability: no positive first-party state claimed.
- Why this is / is not agent-owned: Configured policy and human approval alone do not establish a completed first-party S5 parent loop.
- Evidence: https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/policy.py; https://github.com/ipanalytics/Agent-Mission-Control/blob/0fe9acd4807b149a5c9c07390d195b95ffa87780/src/agent_mission_control/integrations.py.
- Basis: source-level structural / explicit review.
- Confidence: high.
- Caveats: external execution and externally provided agent judgment are outside the credited AMC boundary.

### Absence scope

- Surfaces inspected: Contract parsing, static policy, adapters and CLI path.
- Plausible first-party paths checked: Goal edits, allowed commands, operator review and the host instruction path.
- Why no material first-party path remains: No first-party autonomous identity decision or legitimate parent decision/return loop at the declared recursion.

## Distributed OSS parent arrangement

The use of independent local external agents by separate contributors does not establish a shared first-party AMC parent recursion or any S3/S4/S5 parent-mode closure.

## Self-hosted and non-human modes

The local/CI CLI remains deterministic; external Codex/Claude/Hermes integrations are runbook-based and do not transfer model decision ownership to AMC.

## Recursion

The local mission is the examined boundary. Phase nesting and run directories are not autonomous organizational recursion.

## Variety and escalation

Human-set contract constraints reduce file and command variety. Check failures and report warnings return to an external executor/reviewer; they are not automatically algedonic escalation or S3/S4/S5 decisions.

## Evidence gaps

- Static source-first inspection of the exact frozen revision; no live integration run or model inference was performed.
- Architectural Builder/Verifier terms were cross-checked against shipped `cli.py` and related modules, rather than credited as autonomous decisions.
- Custom integration with an external agent could be reassessed as a different declared system boundary; it does not change this frozen first-party conclusion.

## Publication

This file is **canonical** after the separate admission PR merges; review was published in PR #1538. Its exclusion is recorded in the catalog/projections without creating any included-corpus signature or rank.
