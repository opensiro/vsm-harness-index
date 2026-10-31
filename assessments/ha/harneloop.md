---
harness_id: harneloop
project_name: Harneloop
repository: https://github.com/OpenRootdev/Harneloop
review_ref: d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Harneloop

## Review boundary

- System in focus: The packaged Harneloop Python CLI/library and its first-party agent-facing procedural skill for artifact-aware evolution of harness units, not the separate operating agents or target harnesses that use it.
- Purpose and identity: Keep goals, environment maps, attempts, artifacts, observations, candidate improvements, evidence gates, promoted versions and rollback coherent for an external operating agent.
- Relevant environment: User/agent-controlled task environment, externally run AI agents, produced artifacts, manually or agent-authored evidence, local unit files and target deployment adapters.
- Standard-distribution boundary: Installed `harneloop` console command/`python -m harneloop`, documented Python subcommands and bundled `skills/harneloop/SKILL.md` instructions. Neither the CLI nor skill launches or owns an internal model-agent task loop.
- Credited operating / distribution surfaces: `src/harneloop/cli.py`, `attempts.py`, `runs.py`, `evidence.py`, `candidate.py`, `versioning.py`, `state.py`, `adapters.py`, intake/validation and packaged agent-facing onboarding instructions.
- Adjacent first-party surfaces excluded from ownership: Upstream contributor workflows, product demos/case studies, docs/plans, tests and externally selected Claude/Codex/OpenClaw/other operating agents are not internal model decision owners.
- First-party operating / deployment modes considered: Local Python CLI for humans, externally invoked CLI through a user's agent, agent-facing SKILL.md, explicit harness-unit state machine, portable exports and manual/custom environment integrations. No provider-backed autonomous dispatcher comes bundled.
- Recursion level: One Harneloop harness-unit management installation. An external agent doing a Blender/code/browser task is a distinct adjacent operating system even if it voluntarily follows the Harneloop skill.
- Reviewed revision: `d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI manages versioned on-disk harness units through explicit subcommands: target/environment setup, intake, attempt plan/conclusion, run and artifact recording, candidate creation/readiness/validation, evidence attachment, promotion, rollback, package/export, wait/stop and brief. Its integrity kernel checks protected paths, run terminality, evidence hashes/references, candidate base-version freshness and restorable snapshots. `SKILL.md` tells an already-running external agent how to inspect an environment, perform actual tasks, interpret outputs and propose improvements. Export adapters transform promoted material into agent-facing instructions; no first-party LLM/provider dispatch is wired by the package. See [CLI](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/cli.py), [agent skill](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/skills/harneloop/SKILL.md), [core lifecycle](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/docs/architecture/core-lifecycle.md), [runtime layers](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/docs/architecture/runtime-layers.md).

## Operational model

The operator or an external model agent supplies the target, performs the task, chooses observations/evaluation and authors candidate changes; Harneloop validates records and evidence and carries out allowed state transitions. The developer explicitly states that Harneloop itself does not discover tools/endpoints, run arbitrary target tasks or generate Blender scenes. Removing the external actor leaves a useful deterministic evidence/version-management CLI but no autonomous task choosing and feedback loop. The process is substantive and can support an agentic *composition*, yet the standard distribution does not itself supply/launch the autonomous S1 actor required for general Index inclusion. **Canonical disposition sought: `excluded-no-agentic-vsm`**, not a claim that Harneloop is useless or that composed external agents cannot be viable.

## S1 — Operations

- State: —
- Function: No first-party model-driven task agent autonomously acts on the target environment and iterates on tool results within the Harneloop runtime.
- Disturbance / variety regulated: External agents handle uncertain coding, browser, rendering or document tasks; the CLI handles predictable lifecycle and file/evidence integrity constraints.
- Decisive decision or feedback right: External agent or human selects experiment action, tool calls, interpretation and next improvement; Harneloop receives explicit commands and applies transition predicates.
- Decision owner: Externally supplied AI agent or user for substantive operational reasoning; fixed Python command handlers for recording and guarding transitions.
- Supporting / enforcement mechanisms: Harness unit templates, attempt/run records, evidence registry, target/environment maps, candidate overlays, promotion gates and CLI status/brief.
- Closure path: External actor performs task and interprets artifacts → invokes Harneloop to record run/evidence/decision → CLI writes state → external actor decides next task. Harneloop does not internally take the latter decision and pursue it.
- Why this is / is not agent-owned: The user can operate the CLI without any model; when an agent uses it, its independent host harness owns the model/tool observation-action loop.
- Evidence: [README agent quick start](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/README.md), [onboarding](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/docs/agent-onboarding.md), [CLI dispatch](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/cli.py), [agent skill](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/skills/harneloop/SKILL.md).
- Basis: explicit product contract and structural runtime boundary.
- Confidence: high.
- Caveats: Agent-authored SKILL instructions are deliberately supported but require a separately installed executing agent; this is a published-boundary exclusion, not a judgment about user-composed deployments.

### Absence scope

- Surfaces inspected: Python packaging/entrypoint, CLI subcommand dispatch, run/attempt/candidate modules, installed skill, agent onboarding, adapters, runtime architecture and tests.
- Plausible first-party paths checked: SKILL.md loading, agent-facing prompts, automation adapters, explicit attempt plans, environment connection and candidate promotion for native inference/model-loop/operating-action ownership.
- Why no material first-party path remains: All model-authored actions occur in the externally configured host agent; Harneloop records and constrains their supplied commands and outputs rather than running a first-party model session.

## S2 — Coordination

- State: —
- Function: No first-party disturbance-specific coordination loop between Harneloop-owned operational S1 units is established.
- Disturbance / variety regulated: Parallel candidates can conflict when based on the same promoted version; multiple independent actors may edit a unit.
- Decisive decision or feedback right: The kernel marks sibling candidates `needs_rebase` after one promotion and requires new evidence; it does not negotiate tasks between model-controlled agents.
- Decision owner: Fixed candidate/base-version state-machine predicates; external agents decide if and how to reconcile, test and continue.
- Supporting / enforcement mechanisms: Candidate impact planes, base hashes, locks, status flags and linear promotion history.
- Closure path: One promotion invalidates stale sibling baselines → CLI flags rebase → external owner may reconcile; no first-party S1 pair is modeled and mutually regulated.
- Why this is / is not agent-owned: Stale-version detection is an integrity rule over artifact branches, not autonomous S2 regulation of competing working agents.
- Evidence: [candidate lifecycle](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/candidate.py), [concurrency](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/docs/architecture/concurrency.md), [lifecycle](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/docs/architecture/core-lifecycle.md).
- Basis: structural.
- Confidence: high.
- Caveats: External model workers could use candidate state as a coordination medium, but such a worker arrangement is not shipped inside Harneloop.

### Absence scope

- Surfaces inspected: Candidate concurrency, worktrees/overlays, base versions, promotion locks, agent skill and CLI states.
- Plausible first-party paths checked: Multiple candidates, rebase flags, file locks and shared evidence for a concrete inter-S1 conflict attenuator with returned agent decisions.
- Why no material first-party path remains: Candidate collision safeguards govern artifacts and require external reconciliation; no distinct first-party S1 agents or coordination discretion are composed.

## S3 — Inside-and-now control

- State: —
- Function: No autonomous or operationally parent-governed whole-system S3 management of current agent priorities/commitments is delivered.
- Disturbance / variety regulated: Missing environment context, evidence gaps, uncompleted attempts, candidate freshness and stop/wait conditions.
- Decisive decision or feedback right: Agent/human chooses accept, create candidate, rerun, request input or stop; Harneloop validates the explicit selected choice.
- Decision owner: Separate operating agent or user; Python state machine enforces allowed transitions without choosing the current priority strategy.
- Supporting / enforcement mechanisms: Adaptive intake, `attempt conclude`, `state wait/stop`, status/brief and locks.
- Closure path: Command returns state and suggested next action to outside caller, which chooses the next step; no Harneloop-owned S1 enterprise is managed from a whole-current view.
- Why this is / is not agent-owned: A status board and state transition can support external S3 but are not themselves a discretionary regulatory actor at this boundary.
- Evidence: [attempts](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/attempts.py), [state](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/state.py), [CLI](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/cli.py).
- Basis: structural.
- Confidence: high.
- Caveats: External parent/operator can govern a larger agent project built using these records, but that owner and its closure are not composed here.

### Absence scope

- Surfaces inspected: Attempt conclusion, intake checkpoints, states and brief, run/candidate status and locked promotion.
- Plausible first-party paths checked: Current activity dashboard, stop/wait, external approval and promotion gate for whole-operational S3 discretion.
- Why no material first-party path remains: Commands expose state transitions and enforce rules, while the consequential judgments originate outside the runtime.

## S3* — Complementary audit

- State: —
- Function: No independent complementary organizational auditor of operating-agent claims with audit-owned corrective feedback is shipped.
- Disturbance / variety regulated: Missing artifacts, misleading completion claims, altered run history, stale or self-serving evidence.
- Decisive decision or feedback right: External agent/human decides whether a render/task result is good and which hypothesis to test; CLI validates artifact references, immutability and declared evidence tier.
- Decision owner: Evidence quality assessment remains with outside evaluator/agent; Python validators only reject structural inconsistency.
- Supporting / enforcement mechanisms: Immutable finished runs, artifact hashes, evidence manifest, candidate validation tiers and promotion preconditions.
- Closure path: CLI flags invalid or missing records; a separate caller interprets real task quality and chooses corrections. There is no independent in-boundary auditor with a complementary raw-output judgment returned to an S3 owner.
- Why this is / is not agent-owned: Evidence integrity and an instruction not to trust textual claims strengthen auditability but do not, alone, create first-party S3* independence and judgment.
- Evidence: [evidence](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/evidence.py), [validation](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/validation.py), [run lifecycle](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/runs.py), [agent skill](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/skills/harneloop/SKILL.md).
- Basis: structural.
- Confidence: medium.
- Caveats: An independently staffed evaluator *could* use these artifacts, but its authority and returned correction are not first-party reachable.

### Absence scope

- Surfaces inspected: Evidence attachments, manifest schemas, run-record integrity, promotion gates, observer/validator directories, agent guide.
- Plausible first-party paths checked: Artifact-first observation, evaluator separation, immutable evidence, independent verification and corrective return to whole-system current control.
- Why no material first-party path remains: Structural checks enforce provenance and declaration; substantive independent quality judgment is delegated to the outside agent/operator and no auditor is instantiated.

## S4 — Outside-and-then intelligence

- State: —
- Function: No Harneloop-owned autonomous prospective analysis and adopted capability-change decision loop is delivered.
- Disturbance / variety regulated: Persistent target-agent errors, missing tools, environmental changes and anticipated future task weaknesses.
- Decisive decision or feedback right: An external agent reads failed attempts and proposes candidate changes; Harneloop stores and gates user/agent-authored proposals but does not generate the adaptation option.
- Decision owner: External model/human for diagnosis, design and future capability strategy; fixed code for versioning, evidence and promotion constraints.
- Supporting / enforcement mechanisms: `operational-map.md`, regression cases, candidate impact/tiers, evidence states, snapshots, rollback and export adapters.
- Closure path: Outside agent interprets task artifacts → chooses future harness change → Harneloop holds candidate and gate → external agent reruns/assesses → eligible version is promoted; no first-party model owns the prospective option.
- Why this is / is not agent-owned: Harneloop is built expressly to *support* external agent learning, but the agent performing that learning is independently supplied and not shipped as an autonomous execution mode.
- Evidence: [agent skill](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/skills/harneloop/SKILL.md), [attempts](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/attempts.py), [candidate](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/candidate.py), [README](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/README.md).
- Basis: structural and explicit external-agent interface.
- Confidence: high.
- Caveats: An integrated user-composed agent/Harneloop process may realize S4; this publication state is only for Harneloop's first-party standalone distribution.

### Absence scope

- Surfaces inspected: Candidate creation, experiment history, environment maps, agent skill, package/export and promotion.
- Plausible first-party paths checked: Recurring error diagnosis, agent-authored change hypotheses, prospective tool development, external research and adopted future capability feedback.
- Why no material first-party path remains: Adaptation strategy is assigned to an unbundled outside actor, while the shipped implementation validates and records its outputs.

## S5 — Policy and identity

- State: —
- Function: No first-party legitimate ultimate-policy adjudicator governs the identity of an agent organization from issue to binding return.
- Disturbance / variety regulated: Unit target, success criteria, authorized environment, tool permissions and what protected/promotable harness material is acceptable.
- Decisive decision or feedback right: Human/external agent confirms/delegates intake, sets criteria and commands promotion; fixed kernel guards protected state and artifact integrity.
- Decision owner: External user/operator chooses purpose and permissions, not an internally legitimate S5 authority with an identity dispute process.
- Supporting / enforcement mechanisms: Adaptive intake acknowledgement, `unit.yaml`, protected files, version policies, evidence thresholds and state wait/stop.
- Closure path: Inputs are acknowledged and rules enforced in later commands, but no identity-level claim is referred to a recognized authority for judgment and governing return.
- Why this is / is not agent-owned: Requiring acknowledgement or blocking a bad promotion is operational authorization, not ultimate-policy adjudication.
- Evidence: [intake](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/intake.py), [unit](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/unit.py), [versioning](https://github.com/OpenRootdev/Harneloop/blob/d46e1d5d4aa0bbb77d1bcf355c9848cb89455c31/src/harneloop/versioning.py).
- Basis: structural.
- Confidence: high.
- Caveats: An external institution could define policy over its Harneloop projects; no universal first-party parent feedback arrangement is shown.

### Absence scope

- Surfaces inspected: Intake confirmation, targets, unit identity, protection policy, promotion and documentation of human control.
- Plausible first-party paths checked: User delegation, context acknowledgement, target redefinition, protected manifests, approvals and project governance for identity-level dispute/authoritative ruling/return.
- Why no material first-party path remains: They set task premises and enforce lifecycle integrity; no ultimate-policy decision process is composed within the runtime.

## Distributed OSS parent arrangement

External users can run Harneloop against independently operated agents and export resulting harness materials. There is no shared first-party control of those agents' live contexts or a legitimate distributed parent that decides and returns organization-level S3/S4/S5 matters. Contributor and case-study work do not supply the missing runtime S1 owner.

## Self-hosted and non-human modes

The self-hosted CLI can run without any model credential, proving that its commands are ordinary deterministic record/version management. It can be *invoked by* a non-human host agent which reasons about tasks and artifacts, but agent instructions and the CLI tool surface do not transfer that host's autonomy to Harneloop's own published boundary.

## Recursion

A harness unit is a portable repository of capabilities and evidence; multiple units can evolve independently. This is useful organization of artifacts, not a complete first-party model-agent recursive organization. Assessing a composed external host agent would require its own source/deployment boundary and live wiring.

## Variety and escalation

Artifact schemas, immutable runs, candidate evidence gates and stale-base rebase rules attenuate version/evidence integrity risk. An external agent may amplify variation by proposing future tools and tests; `request_input`, wait and stop make blockers explicit. The runtime never itself supplies the open-ended decision owner or a complementary independent auditor.

## Evidence gaps

Pinned static source inspection, no external Blender/ViperMesh experiment or model-provider E2E. Published case-study results are external evidence, not proof that this CLI launches an agent. The exclusion is bounded to the current standard distribution; a later bundled agent runtime or explicit first-party composed execution path would merit reassessment.
