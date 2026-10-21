---
harness_id: agentcharter
project_name: AgentCharter
repository: https://github.com/moerasermax/AgentCharter
review_ref: 7eeaf65367ff8ce945ab485fe9b1e41b17f7f607
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentCharter

**Proposed noncanonical disposition:** `excluded-no-agentic-vsm` under [Index #1827](https://github.com/opensiro/vsm-harness-index/issues/1827) row 6, original frozen #1281 position 9. This excludes the pinned default distribution from the agentic VSM corpus; it does not deny the practical value of role protocols, mutual auditing, reproducible prompts or executable Git guardrails.

## Review boundary

- System in focus: AgentCharter's shipped, cross-vendor role protocol and adoption package; not a custom AI runtime created by an individual adopting project.
- Purpose and identity: standardize human-authorized PM, Engineer, auditor and reviewer division of responsibility across providers, projects and sessions.
- Relevant environment: adopter Git repository, external Claude/Gemini/Codex/Cursor hosts, user-supplied agents and task prompts, role templates, local Git and shell tools, human authorizing roles.
- Standard-distribution boundary: pinned documentation, core/role definitions, templates/vendor-adapters, tools/*-spec.md and vendor-neutral Bash utilities. No separate model provider adapter, first-party agent runner, autonomous task loop or durable managed first-party model workcell is included.
- Credited operating / distribution surfaces: adopter-directed self-instantiation of vendor command templates, Git pre-commit checks H1–H7, checkpointer shell utility, hook installer, charter-spec-lint; documentation specs do not become first-party running functions solely by being model-readable.
- Adjacent first-party surfaces excluded from ownership: any adopting customer project and its external LLM execution, manually created vendor-specific slash commands, self-declared agent roles, example CryptoBot/IRON demonstrations and governance structures belonging to others.
- First-party operating / deployment modes considered: pure prompt/spec onboarding, optional profile and role workflows, installer/commit hook guards, checkpoint handler, optional pretooluse guard as a specification and project-authored implementation, cross-vendor handoff/second-context prompting.
- Recursion level: distributed reusable protocol for adopting projects, without a shipped continuing autonomous S1 unit to anchor VSM recursion.
- Reviewed revision: 7eeaf65367ff8ce945ab485fe9b1e41b17f7f607.
- Observation date: 2026-10-21.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The framework explicitly instructs adopting users to send an onboarding request to **their** existing AI; the AI reads `QUICKSTART.md` or `tools/init-spec.md` and creates its own vendor-specific command behavior. The spec says AgentCharter reverted to pure spec at v0.5.9; vendor-neutral shell scripts are declared exceptions only for git hooks, checkpoint operations and one-off installation. This is not a missing source directory due to oversight: the authoring model intentionally delegates model execution and actor lifecycle to adopting hosts. [BOOTSTRAP.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/BOOTSTRAP.md); [QUICKSTART.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/QUICKSTART.md); [tools/init-spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/init-spec.md); [tools/vendor/commons/README.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/README.md); [templates/vendor-adapters/README.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/templates/vendor-adapters/README.md).

The included executable Bash code is concrete, not cosmetic. `charter-commit-checks.sh` checks staged Git changes for role status, reflection bookkeeping, versioned mandatory profiles and handoff declarations; `install-git-hooks.sh` installs a local shim; `checkpoints_handler.sh` archives drafts and may invoke git commit. These operate on deterministic regular-expression/document/file criteria. They do not call models or own cognitive planning/execution/feedback. [tools/vendor/commons/charter-commit-checks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/charter-commit-checks.sh); [tools/vendor/commons/install-git-hooks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/install-git-hooks.sh); [tools/vendor/commons/checkpoints_handler.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/checkpoints_handler.sh); [tools/charter-spec-lint.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/charter-spec-lint.sh).

In a particular adopted environment the external AI may really perform productive engineering and the roles may complement one another. That outcome belongs to the adopter's configured AI harness and its own authority system; this general Index assessment may not transfer that external operational agency or human policy authority to the reusable spec distribution.

**Counterfactual owner test:** remove the external AI host, adopter project and user-driven prompts. The first-party repository still supplies complete documentation/templates and locally executable validation/checkpoint helpers, but cannot initiate and run a substantive model-decided task or a viable multi-agent organization. Conversely, having an external AI read role/permission instructions is not sufficient to establish a running first-party AgentCharter agent at the assessed repo boundary.

## Operational model

Human chooses project and AI provider → external AI is told to read published charter/init instructions → provider creates adopter-owned role scaffolding and follows prompts → deterministic hooks/checkpoint tools can validate, save or block specific Git/file actions → human and external AI decide subsequent adoption/approval. This is substantive distribution of a protocol and file-level controls, not a first-party autonomous operational S1/parent system.

## S1 — Operations

- State: —
- Function: Transform authorized project requirements into real user-facing deliverables by model-directed implementation with tool/result feedback.
- Disturbance / variety regulated: User requests, code edits and project requirements have semantic variety that a model actor would need to address.
- Decisive decision or feedback right: Select and revise task content/tool actions under project authority based on execution observations.
- Decision owner: The adopting project's external Claude/Gemini/Cursor/Codex instance, initialized by a user or adopter-created slash command, exercises any such model discretion; shipped first-party AgentCharter owns only rules/templates and deterministic shell support.
- Supporting / enforcement mechanisms: Role _spec and role-init mandates, onboarding prompts, vendor adapter templates, checkpoint shell and commit checks.
- Closure path: An adopter explicitly supplies a prompt to an external model, which may then implement its own tools/work; the pinned framework itself does not invoke a model, preserve an independent running agent work cell, execute a model-driven task and return its own work outcome.
- Boundary reachability: Adoption docs instruct an AI to read a spec and self-instantiate vendor-specific commands; the spec says the framework deliberately ships no Python/npm implementation runner. Bash tools perform fixed checks, handoff files and Git hooks, not semantic model-agent decisions.
- Why this is / is not agent-owned: The relevant step either follows fixed shell logic, is an instruction for an externally invoked adopter-hosted model or remains user-owned; none transfers the specific agent-operated VSM function into AgentCharter's own shipped runtime.
- Evidence: [README.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/README.md); [QUICKSTART.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/QUICKSTART.md); [ADOPTION.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/ADOPTION.md); [BOOTSTRAP.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/BOOTSTRAP.md); [tools/init-spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/init-spec.md); [tools/vendor/commons/README.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/README.md); [tools/vendor/commons/charter-commit-checks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/charter-commit-checks.sh); [tools/vendor/commons/checkpoints_handler.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/checkpoints_handler.sh); [roles/pm/_spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/roles/pm/_spec.md); [roles/engineer/_spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/roles/engineer/_spec.md)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Role content and user-triggered external AI use are genuine intended usage, but do not establish a first-party executed agent S1 at the default repo boundary.

### Absence scope

- Surfaces inspected: README.md; QUICKSTART.md; ADOPTION.md; BOOTSTRAP.md; tools/init-spec.md; tools/vendor/commons/README.md; tools/vendor/commons/charter-commit-checks.sh; tools/vendor/commons/checkpoints_handler.sh; roles/pm/_spec.md; roles/engineer/_spec.md.
- Plausible first-party paths checked: supplied Git hooks/checkpoint/lint helpers, adopter project bootstrap, vendor templates and multi-role/audit/escalation instructions for S1 — Operations.
- Why no material first-party path remains: No source-reachable first-party model execution plus function-specific decision and operational feedback loop for S1 — Operations survives removal of adopter-hosted agent execution.

## S2 — Coordination

- State: —
- Function: Attenuate reciprocal disturbances between independently continuing agent-run viable S1 units.
- Disturbance / variety regulated: Competing PM/Engineer changes and cross-session handoffs can conflict.
- Decisive decision or feedback right: Detect contention among two running agent S1 cells and return a corrective coordination decision that changes those cells' work.
- Decision owner: The role-separation and handoff protocols are written rules for adopting external agents, not a running first-party coordinator controlling and rebalancing independent S1 activities.
- Supporting / enforcement mechanisms: Role separation, mutual checking, refusal/escalation protocols, common memory root, handoff templates and Git hook H1–H7 checks.
- Closure path: Written handoff and checklist advice, and deterministic hook rejections, can constrain adoption but do not constitute a first-party inter-agent conflict detector with returned decisions in a managed multi-agent runtime.
- Boundary reachability: No default first-party model-backed agent execution owner is present, and role label separation is only provisioned when external AI adopts the instructions.
- Why this is / is not agent-owned: The relevant step either follows fixed shell logic, is an instruction for an externally invoked adopter-hosted model or remains user-owned; none transfers the specific agent-operated VSM function into AgentCharter's own shipped runtime.
- Evidence: [core/role-separation.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/role-separation.md); [core/audit-rights.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/audit-rights.md); [core/escalation-protocol.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/escalation-protocol.md); [core/individual-learning-loop.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/individual-learning-loop.md); [tools/vendor/commons/charter-commit-checks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/charter-commit-checks.sh); [QUICKSTART.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/QUICKSTART.md); [templates/vendor-adapters/README.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/templates/vendor-adapters/README.md)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Two agent role descriptions are not two demonstrated continuing agent S1 work cells.

### Absence scope

- Surfaces inspected: core/role-separation.md; core/audit-rights.md; core/escalation-protocol.md; core/individual-learning-loop.md; tools/vendor/commons/charter-commit-checks.sh; QUICKSTART.md; templates/vendor-adapters/README.md.
- Plausible first-party paths checked: supplied Git hooks/checkpoint/lint helpers, adopter project bootstrap, vendor templates and multi-role/audit/escalation instructions for S2 — Coordination.
- Why no material first-party path remains: No source-reachable first-party model execution plus function-specific decision and operational feedback loop for S2 — Coordination survives removal of adopter-hosted agent execution.

## S3 — Inside-and-now control

- State: —
- Function: Govern current whole-system work priorities, resources and operating exceptions across multiple viable S1 operations.
- Disturbance / variety regulated: Task overload, shifting project priorities and repeated role violations.
- Decisive decision or feedback right: Whole-organization current allocation and corrective authority returning to running independent S1 units.
- Decision owner: Human adopter approves identity changes and assignments; model-readable role mandates and shell gate checks restrict specific files/commits, not managerial whole-system deliberation.
- Supporting / enforcement mechanisms: User authorization for role activation, profile presets, work-budget, subagent/human gates, staged changes and pre-commit checks.
- Closure path: Git pre-commit can reject a documented violation and role protocol can escalate to user; no first-party allocation of ongoing organizational resources or return to constituent viable operation units is executed.
- Boundary reachability: Work-budget, routing and human gates are opt-in instructions or limited regex hooks; no organizational execution/control plane with independently maintained present-state report is shipped.
- Why this is / is not agent-owned: The relevant step either follows fixed shell logic, is an instruction for an externally invoked adopter-hosted model or remains user-owned; none transfers the specific agent-operated VSM function into AgentCharter's own shipped runtime.
- Evidence: [core/role-separation.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/role-separation.md); [tools/vendor/commons/charter-commit-checks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/charter-commit-checks.sh); [tools/vendor/commons/install-git-hooks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/install-git-hooks.sh); [QUICKSTART.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/QUICKSTART.md); [core/escalation-protocol.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/escalation-protocol.md); [GOVERNANCE.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/GOVERNANCE.md)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Do not convert explicit human role-authorization text, file checks or prompt discipline into S3 current management.

### Absence scope

- Surfaces inspected: core/role-separation.md; tools/vendor/commons/charter-commit-checks.sh; tools/vendor/commons/install-git-hooks.sh; QUICKSTART.md; core/escalation-protocol.md; GOVERNANCE.md.
- Plausible first-party paths checked: supplied Git hooks/checkpoint/lint helpers, adopter project bootstrap, vendor templates and multi-role/audit/escalation instructions for S3 — Inside-and-now control.
- Why no material first-party path remains: No source-reachable first-party model execution plus function-specific decision and operational feedback loop for S3 — Inside-and-now control survives removal of adopter-hosted agent execution.

## S3* — Complementary audit

- State: —
- Function: Independently audit the operational reality underlying a routine whole-current managerial report and feed discrepancies back into S3.
- Disturbance / variety regulated: Potential false completion claims, unverified hashes and AI role-boundary violations.
- Decisive decision or feedback right: A complementary auditor chooses an independent operational inspection and returns findings to actual S3 corrective authority.
- Decision owner: Auditor/validator prompts assign responsibility to external agents; deterministic doctor/lint/commit checks cover document, state and git-commit invariants.
- Supporting / enforcement mechanisms: Mutual PM/Engineer audits, Phase 5b second-context review mandate, checklists, charter-spec-lint.sh, Git hooks and documented anti-fabrication receipts.
- Closure path: When adopted, a second external model can review task artifacts and return a finding; this is task-level QA and depends on adopter invocation. The shipped shell checks do not provide an independent first-party S3 field-audit management loop.
- Boundary reachability: No first-party ongoing S3 report or independent assigned verifier process that independently inspects current operations was found.
- Why this is / is not agent-owned: The relevant step either follows fixed shell logic, is an instruction for an externally invoked adopter-hosted model or remains user-owned; none transfers the specific agent-operated VSM function into AgentCharter's own shipped runtime.
- Evidence: [core/audit-rights.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/audit-rights.md); [tools/init-spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/init-spec.md); [tools/vendor/commons/charter-commit-checks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/charter-commit-checks.sh); [tools/charter-spec-lint.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/charter-spec-lint.sh); [tools/pretooluse-guard-spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/pretooluse-guard-spec.md); [roles/pm/_spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/roles/pm/_spec.md); [roles/engineer/_spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/roles/engineer/_spec.md)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Significant verification policy and structural guardrails exist; that is not equivalent to a complementary S3* feedback function.

### Absence scope

- Surfaces inspected: core/audit-rights.md; tools/init-spec.md; tools/vendor/commons/charter-commit-checks.sh; tools/charter-spec-lint.sh; tools/pretooluse-guard-spec.md; roles/pm/_spec.md; roles/engineer/_spec.md.
- Plausible first-party paths checked: supplied Git hooks/checkpoint/lint helpers, adopter project bootstrap, vendor templates and multi-role/audit/escalation instructions for S3* — Complementary audit.
- Why no material first-party path remains: No source-reachable first-party model execution plus function-specific decision and operational feedback loop for S3* — Complementary audit survives removal of adopter-hosted agent execution.

## S4 — Outside-and-then intelligence

- State: —
- Function: Observe future/external environment, generate strategic capability options and return accepted adaptation into current organization.
- Disturbance / variety regulated: New vendors, changed model capabilities and repeated communication failures across adopting projects.
- Decisive decision or feedback right: Choose prospective changes to future operating capability based on environmental trends with a return to S3.
- Decision owner: Maintainers revise text/specs, release instructions and guardrails from dogfood incidents; the repo does not ship a model-run prospective sensing and strategy loop.
- Supporting / enforcement mechanisms: Failure-mode log, role/vendor lifecycle instructions, migration and dogfood hardening changelog, adopter prompts.
- Closure path: Maintainers may change future charter standards and shell checks; such author-managed project evolution is not a first-party agent-owned sensing/option/authority-return loop.
- Boundary reachability: No shipped recurring model agent watches outside environment, produces adopted strategic proposals and revises live S1 operating capability.
- Why this is / is not agent-owned: The relevant step either follows fixed shell logic, is an instruction for an externally invoked adopter-hosted model or remains user-owned; none transfers the specific agent-operated VSM function into AgentCharter's own shipped runtime.
- Evidence: [README.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/README.md); [core/individual-learning-loop.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/individual-learning-loop.md); [ADOPTION.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/ADOPTION.md); [GOVERNANCE.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/GOVERNANCE.md); [tools/vendor/commons/charter-commit-checks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/charter-commit-checks.sh)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Framework evolution and roadmap/history are maintained by humans; they are not automatically an implemented S4 agent.

### Absence scope

- Surfaces inspected: README.md; core/individual-learning-loop.md; ADOPTION.md; GOVERNANCE.md; tools/vendor/commons/charter-commit-checks.sh.
- Plausible first-party paths checked: supplied Git hooks/checkpoint/lint helpers, adopter project bootstrap, vendor templates and multi-role/audit/escalation instructions for S4 — Outside-and-then intelligence.
- Why no material first-party path remains: No source-reachable first-party model execution plus function-specific decision and operational feedback loop for S4 — Outside-and-then intelligence survives removal of adopter-hosted agent execution.

## S5 — Policy and identity

- State: —
- Function: Legitimately decide ultimate project identity/purpose and constitutional exceptions, returning accepted changes to a continuing agent organization.
- Disturbance / variety regulated: Conflicts over role legitimacy, exceptions and constitutional domain safety.
- Decisive decision or feedback right: Validly adopt or change ultimate organizational identity-policy and propagate the decision as operative authority.
- Decision owner: A human adopting the charter reserves role assignment, risk acceptance and domain axioms; no first-party constitutional S5 decision owner in a viable agent organization is constituted.
- Supporting / enforcement mechanisms: Domain safety axiom slot, governance process, role activation prose, Git hook text checks and opt-in human gates.
- Closure path: A user chooses project goals and whether to adopt a new rule; a hook may detect a phrase indicating approval, but this does not authenticate ultimate human authority or establish organization-wide policy identity feedback.
- Boundary reachability: No independently operating first-party agent organization with valid parent S5 and returned constitutional decisions exists within the shipped framework.
- Why this is / is not agent-owned: The relevant step either follows fixed shell logic, is an instruction for an externally invoked adopter-hosted model or remains user-owned; none transfers the specific agent-operated VSM function into AgentCharter's own shipped runtime.
- Evidence: [GOVERNANCE.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/GOVERNANCE.md); [core/role-separation.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/core/role-separation.md); [tools/vendor/commons/charter-commit-checks.sh](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/vendor/commons/charter-commit-checks.sh); [QUICKSTART.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/QUICKSTART.md); [tools/init-spec.md](https://github.com/moerasermax/AgentCharter/blob/7eeaf65367ff8ce945ab485fe9b1e41b17f7f607/tools/init-spec.md)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Legitimate human authority can exist in a particular adopter project, but must not be inherited by the distributed framework itself.

### Absence scope

- Surfaces inspected: GOVERNANCE.md; core/role-separation.md; tools/vendor/commons/charter-commit-checks.sh; QUICKSTART.md; tools/init-spec.md.
- Plausible first-party paths checked: supplied Git hooks/checkpoint/lint helpers, adopter project bootstrap, vendor templates and multi-role/audit/escalation instructions for S5 — Policy and identity.
- Why no material first-party path remains: No source-reachable first-party model execution plus function-specific decision and operational feedback loop for S5 — Policy and identity survives removal of adopter-hosted agent execution.

## Distributed OSS parent arrangement

The maintainer's repository governance controls changes to framework norms. The adopting project's legitimate human decision makers control role activation and final approval. Neither controls a default first-party AgentCharter-operated autonomous S1 workplace; these parent arrangements cannot be attached to a nonexistent autonomous organization.

## Self-hosted and non-human modes

The only executable default paths in this source tree are Bash hooks/checkpoint, schema lint and installer utilities. Any model-driven self-instantiation is requested in the external adopter environment, whose provider selection, running session, tool access, task results and deployment status are not delivered as one first-party AgentCharter-owned runtime. No first-party non-human ultimate policy holder is present.

## Recursion

A role chart (PM, Engineer, Auditor) and two-way audit instructions are organizational templates. They do not prove the actual existence, autonomy, recurrent boundaries or viable management of multiple running S1 operations in this distribution.

## Variety and escalation

The supplied hooks can reject/flag specific Git staging patterns, and role instructions may prompt a human escalation on repeated failures. These support adopter-level control, but a fail-fast regular expression is not a complete organization-level algedonic relationship with an agent-owned S3/S5.

## Evidence gaps

- No live external provider was run: the task is a frozen source-first assessment of first-party default distribution, not benchmarking an adopter-hosted AI.
- A future AgentCharter release that ships a real first-party cognitive runtime or a specific adopter integration could warrant distinct assessment with its own operating boundary; that possibility is not imported here.
- Shell hooks do real deterministic checks, but documented constraints admit `git commit --no-verify` and compliance depends on deployment. No security-proof claims are made.
- The absence verdict does not devalue contributor experience or the project's documented role-audit philosophy.
