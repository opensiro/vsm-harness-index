---
harness_id: konductor
project_name: Konductor
repository: https://github.com/aws-solutions/konductor
review_ref: 09c34858ca2e704fb8572c91389a87255b1e1075
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: —
---

# Konductor

## Review boundary

- System in focus: One installed Konductor role/skill/SOP distribution in a supported Kiro CLI or Claude Code host executing a project development task with one or more specialist coding agents. Neither the complete host system nor the upstream AWS or GitHub organization is included.
- Purpose and identity: Source-defined agent orchestration for software delivery with specialist delegation, safe parallel writing, review/evidence gates, controlled escalation and maintained task context.
- Relevant environment: User requests and decisions, repository source/worktrees, independent agent replies, design/spec/test results, real Git diffs, CI findings, tool/resource availability and human approvals.
- Standard-distribution boundary: Source-shipped Rust CLI installers/agent-SOP synthesizers and installed Konductor orchestrator prompts, named specialist agent specs, delegation protocol, full-SDLC and review SOPs, verification skills, gate evaluator and project memory/skills. External Kiro/Claude model/runtime, MCP/OS/Git tooling and AWS services remain dependencies, not automatically credited first-party organizational owners.
- Credited operating / distribution surfaces: [README.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/README.md), [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [agents/k-developer.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/k-developer.agent-spec.json), [agents/k-architect.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/k-architect.agent-spec.json), [skills/delegation-protocol/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/delegation-protocol/SKILL.md), [agent-sops/k-full-sdlc.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-full-sdlc.sop.md), [agent-sops/k-adversarial-pull-request-review.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-adversarial-pull-request-review.sop.md), [cli/konductor-rs/src/cli/install.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/install.rs), [cli/konductor-rs/src/cli/gate_eval.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/gate_eval.rs) plus the shipped code-review and memory/skill contracts in supported installed host modes.
- Adjacent first-party surfaces excluded from ownership: Project development-only `tests/`, benchmarks and sample scripts, `package.json` benchmark-only runner, repository maintainer CI/release work, generated artifacts not distributed into a running session and unrelated external cloud services. Tests and docs may corroborate reachability but do not themselves own VSM decisions.
- First-party operating / deployment modes considered: Installed Kiro or Claude orchestrator with named coding/review specialist roles; default sequential branch-mode features; opted-in parallel worktree mode; strict multi-phase SOP with recorded review/user gates; independent adversarial reviewer checker; memory and workspace-skill reflexes conditional on local validated files and user authorization.
- Recursion level: One project delivery cell with multiple distinct coding/review specialist S1 agents and one Konductor orchestrator over active project tasks. Project owner/maintainers and external agent hosts are adjacent legitimate authorities, not included by merely using this distribution.
- Reviewed revision: `09c34858ca2e704fb8572c91389a87255b1e1075` (frozen original `main`).
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Konductor ships machine-readable orchestrator/specialist definitions (`agents/*.agent-spec.json`), a Rust installer that synthesizes the agent/skill/SOP distribution into supported host locations, and explicit source-defined multi-phase skills/SOPs. An installed model-backed Konductor agent owns task classification, specialist choice, dispatch, review/fix routing, active task tracking and escalation; Kiro/Claude provide model turns and tool execution. `k-full-sdlc` keeps project-specific phase/session state and gates in `.konductor/`, separates per-feature branch/worktree outputs and invokes specialist review and testing with bounded fix cycles. The installed delegation protocol prevents parallel file ownership conflicts before spawning; the Rust `gate_eval` evaluates recorded SOP states and findings mechanically without claiming discretionary managerial judgment. Code-review SOP reads actual Git diffs and delegates to a separate adversarial multi-pass review with fresh validator persona. Persistent-memory/workspace-skills support post-task lessons, but their future organizational adaptation authority needs separate adjudication. Sources: [README.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/README.md), [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [skills/delegation-protocol/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/delegation-protocol/SKILL.md), [agent-sops/k-full-sdlc.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-full-sdlc.sop.md), [cli/konductor-rs/src/cli/gate_eval.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/gate_eval.rs), [agent-sops/k-code-review-workflow.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-code-review-workflow.sop.md), [agent-sops/k-adversarial-pull-request-review.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-adversarial-pull-request-review.sop.md).

## Operational model

The user provides a requested engineering outcome. A named orchestrator chooses specialist agents and SOPs, maintains a phase/TODO view, routes constrained task briefs, executes disjoint parallel tasks when host/tooling support it and joins/reviews the resulting work. The delegation protocol orders dependent work, reserves per-agent file sets and rejects unguarded shared-tree concurrent writing. Independent code/review specialists inspect the actual diff, report findings and, within bounded limits, drive corrective work or a human halt. User approvals are explicitly scoped to a named action; an individual review gate is not an S5 mission/identity change. Project memory/workspace-skills may carry reusable conventions into later sessions, but the inspected shipped path alone does not establish a complete first-party environment-facing strategic adaptation loop.


## S1 — Operations
- State: A
- Function: Execute specialized model-conditioned engineering tasks, such as requirements analysis, architecture, implementation, tests and PR preparation.
- Disturbance / variety regulated: Diverse user requirements, repository code differences, implementation failures, external tools and test/review feedback.
- Decisive decision or feedback right: The model-backed specialist chooses concrete code/analysis/tool actions and returns artifacts; the orchestrator chooses a suitable specialist for an operating task.
- Decision owner: Installed Konductor `k-developer`, `k-architect`, `k-researcher` and similar registered model-backed agent roles, not the Rust installer or deterministic gate evaluator.
- Supporting / enforcement mechanisms: Agent spec registry, explicit delegation briefs, host tools, Git worktrees, SOP state/progress files, build/test scripts and bounded fix-cycle requirements.
- Closure path: A specialist performs the assigned job, writes or returns deliverables, and its result enters the orchestrator's review/repair loop; an accepted artifact advances the subsequent phase or is escalated.
- Boundary reachability: Rust installation synthesizes source-shipped agent specs, SOPs and skills for supported Kiro/Claude host modes; Konductor's packaged system prompt invokes explicitly registered specialists and their SOP contracts.
- Why this is / is not agent-owned: LLM-backed coding/research decisions are owned by the named roles under installed first-party instructions; the executable host's generalized cognition and Git tools are external support.
- Evidence: [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [agents/k-developer.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/k-developer.agent-spec.json), [agents/k-architect.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/k-architect.agent-spec.json), [skills/delegation-protocol/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/delegation-protocol/SKILL.md), [cli/konductor-rs/src/cli/install.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/install.rs), [agent-sops/k-full-sdlc.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-full-sdlc.sop.md)
- Basis: first-party distributed agent role prompts plus installer and runnable SOP invocation contracts
- Confidence: medium-high for supported configured mode
- Caveats: Host/Kiro/Claude agents and network tools must actually be installed/configured; no live model run or PR generated by the target was observed in this assessment.


## S2 — Coordination
- State: A
- Function: Prevent two independently writing agent units from overwriting the same source files or creating incompatible feature branch/merge results.
- Disturbance / variety regulated: Separate agent writers can edit a shared router, schema, registry or working tree concurrently; parallel worktrees isolate files on disk but do not automatically avoid merged-path conflicts or lost work.
- Decisive decision or feedback right: Model-backed orchestrator must list per-agent write file sets before parallel dispatch and decide whether to give an overlapping file to one agent or serialize the affected parts; it chooses exact worktree targets and coordinates integration.
- Decision owner: Installed Konductor model-backed orchestrator exercising the shipped `delegation-protocol` before assigning multiple writer specialists, backed by deterministic branch/isolation constraints.
- Supporting / enforcement mechanisms: Explicit target worktree in the delegation brief, per-feature worktree/branch options, disjoint-file preflight, sequential dependency handoff, integration of separate commits and post-integration build/test verification.
- Closure path: Potential duplicate ownership is resolved before work starts through revised agent-file allocation or sequential execution; approved writers receive distinct targets; integration owner combines outputs and runs tests/review before further delivery.
- Boundary reachability: The packaged `delegation-protocol` expressly governs Konductor's parallel specialist spawns; the shipped Konductor system prompt requires an explicitly named agent and 8-field brief. Full-SDLC SOP exposes branch-vs-worktree mode and physical per-feature isolation.
- Why this is / is not agent-owned: The S2-specific action is discretionary conflict-aware task/file reassignment by the model-backed orchestrator, not generic job sequencing, a host mailbox or Git branch commands alone.
- Evidence: [skills/delegation-protocol/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/delegation-protocol/SKILL.md), [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [agent-sops/k-full-sdlc.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-full-sdlc.sop.md), [agent-sops/k-delegate.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-delegate.sop.md)
- Basis: explicit first-party collision-specific operating contract and return into writer dispatch
- Confidence: medium
- Caveats: The pre-dispatch file sets must be reasonably identified by the orchestrator; no actual concurrent-run conflict episode was executed. The standard single-branch mode is sequential, whereas parallel disjoint-writer mode is conditional.
- Distinct S1 units: At least two model-backed coding specialists on separate feature slices or worktrees operating on a common project.
- Inter-S1 disturbance: Two writers modifying the same registry/schema/router or both writing the same shared checkout could lose changes or generate a merged source conflict.
- Attenuating coordination relation: The orchestrator enumerates file ownership before parallel spawn, assigns unique target worktree and overlapping file ownership to one writer, or serializes the collision; dependent tasks wait on upstream handoff.
- Feedback into subsequent S1 behaviour: Each writer's dispatch brief names its actual worktree/file scope and revised timing; resulting artifacts are merged into integration work, tested and reviewed before downstream operations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The concrete shared-file and overlapping worktree interference is named and resolved through assigned ownership/serial fallback with observable changes to subsequent writers; multi-agent delegation without that remedy would not qualify.


## S3 — Inside-and-now control
- State: A
- Function: Steer currently active project delivery by assigning specialist commitments, tracking phase status, gating quality, managing bounded retries and escalating blocked work.
- Disturbance / variety regulated: Incomplete phases, specialist output defects, failed build/review, blocked dependencies, parallel task limit exhaustion and critical findings beyond repair budget.
- Decisive decision or feedback right: Model-backed Konductor routes current specialist work, owns the TODO/phase picture and chooses whether to repair, redelegate, wait for human authority, or stop under the 2-strike and review ceilings.
- Decision owner: Installed Konductor orchestration agent over the local project delivery cell; humans retain separately reserved approvals of individual steps.
- Supporting / enforcement mechanisms: SOP state map, deterministic Rust `gate_eval` and severity thresholds, phase recording, TODO, receipts, specialist reports and human checkpoint prompts.
- Closure path: After specialist results, Konductor checks source evidence, updates phase and issues corrective briefs/reassignments or blocks progress; accepted results unlock the next phase and exceptions reach an operator for decision.
- Boundary reachability: Source-shipped Konductor system prompt requires TODO and current review ownership, 2-strike routing and full-SDLC phase orchestration; installed SOPs and gate configuration are executable by the host agent.
- Why this is / is not agent-owned: Konductor makes the cross-specialist current-control decisions; the Rust gate check and human approval forms constrain actions but do not replace the model's orchestration judgment.
- Evidence: [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [agent-sops/k-full-sdlc.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-full-sdlc.sop.md), [agent-sops/k-delegate.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-delegate.sop.md), [cli/konductor-rs/src/cli/gate_eval.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/gate_eval.rs), [cli/gate-config/sop-orchestration.yml](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/gate-config/sop-orchestration.yml)
- Basis: first-party installed role decisions plus phase tracking and native gate-enforcement path
- Confidence: medium
- Caveats: The whole-system scope is one project/task delivery team, not global organization resource management; no separate whole-team parent S3 closure is claimed merely from human checkpoints.
- Whole-system current view: Konductor's required TODO status, per-phase SOP session/checklist, returned specialist results, review gates and current remaining fix cycles across the project/task.
- Current-control decision scope: Assignments, rework responsibility, sequence/parallelism, phase priority, reroutes, bounded recovery and escalation of current specialist commitments.


## S3* — Complementary audit
- State: A
- Function: Independently challenge coding/review assertions with real Git diffs and multiple separate evaluation perspectives before release/merge recommendation.
- Disturbance / variety regulated: Defective code masked by a coder's self-report or routine review, latent security/schema/data-integrity holes and inaccurate proposed fixes.
- Decisive decision or feedback right: Three isolated adversarial generator agents (security, integrity, schema), a separate reuse evaluator and a fresh `k-architect` validator make independently role-separated judgments against the actual source diff, producing a blocking/nonblocking verdict.
- Decision owner: Distinct model-backed adversarial reviewers and fresh checker role in packaged `k-adversarial-pull-request-review` SOP, not the orchestrator who coordinates handoffs nor a deterministic word severity table.
- Supporting / enforcement mechanisms: Git diff intake, checker literal-diff verification, independent context boundaries, typed findings/severity, review ceilings, SOP result recording and gated phase progression.
- Closure path: Independent findings are checked against real changed hunks, translated to critical/important report and returned to orchestrator/implementer for a bounded fix and new review; unresolved important defects block completion and are escalated.
- Boundary reachability: `k-code-review-workflow` directly requires an adversarial pass on its current diff, and `k-adversarial-pull-request-review` supplies concrete generator and checker role assignments; Konductor registers those SOPs in its distribution.
- Why this is / is not agent-owned: Substantive review judgment is made by fresh role-separated agents with source access; mechanical gate_eval and report aggregation enforce the verdict but do not independently author the audit.
- Evidence: [agent-sops/k-code-review-workflow.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-code-review-workflow.sop.md), [agent-sops/k-adversarial-pull-request-review.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-adversarial-pull-request-review.sop.md), [skills/adversarial-code-review/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/adversarial-code-review/SKILL.md), [cli/konductor-rs/src/cli/gate_eval.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/gate_eval.rs), [agents/k-architect.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/k-architect.agent-spec.json)
- Basis: explicit shipped multi-review SOP, code/diff exposure and return-to-fix contract
- Confidence: medium-high
- Caveats: Source proves designed role/context independence but not empirical correctness of actual provider calls; this assessment is not a separate independent human OpenSiro S3* audit.
- Claim being audited: The implementer's changed code and PR fulfill requirements without significant security, contract or integration defects.
- Ordinary reporting path: Implementer says build/tests passed; basic code-review specialist submits first review report.
- Complementary access path: Adversarial SOP reads actual full Git diff and source, parallel independent vulnerability lenses, and a fresh different-persona architect checker verifies findings against literal diff.
- Independence boundary: The checker never generates its own candidate findings and starts after generator passes; distinct sessions/personas and prohibition on passing one generator's findings to the others.
- Who acts on findings: Konductor orchestrator routes required fixes to the owning developer/specialist, orders fresh checks per review ceilings, and escalates unresolved critical/important findings to the user.


## S4 — Outside-and-then intelligence
- State: ?
- Function: Plausible durable lesson/skill adaptation exists but the first-party environmental foresight and adopted future-capability change loop is unresolved.
- Disturbance / variety regulated: Unexpected external tool/API behavior, repeated implementation failures, changed project conventions and new constraints that could require revised future practices.
- Decisive decision or feedback right: The Konductor prompt invokes memory/skill reflexes following error recovery and user correction; skill writes are constrained by user and provenance policies. It is unclear whether this amounts to organizational prospective adaptation beyond retaining case facts.
- Decision owner: Agent can propose/select capture candidates, while the user may approve workspace skill creation; full decisive ownership of a closed first-party S4 strategic option-to-capability loop is not demonstrated.
- Supporting / enforcement mechanisms: `persistent-memory` stores bounded project/user facts, validator checks safe writes, `workspace-skills` scans and requests confirmation for reusable procedures; subsequent sessions may reload user-authorized data.
- Closure path: Past error/user feedback can become a tagged project memory or approved skill and be re-read on a later run. Source does not demonstrate an independent external-and-prospective strategic option and how it materially changes the managed team's future capability at this organizational recursion.
- Why this is / is not agent-owned: A persistence/reflection mechanism may inform future work, but may be ordinary context retention; neither automatic S4=A nor parent S4=P is established from a single-correction memory write.
- Evidence: [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [skills/persistent-memory/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/persistent-memory/SKILL.md), [skills/workspace-skills/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/workspace-skills/SKILL.md), [README.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/README.md)
- Basis: first-party packaged memory/skill contracts and embedded reflex rule; insufficient function-specific prospective governance closure
- Confidence: medium for a plausible in-boundary pathway, not enough for positive state
- Caveats: Specific unresolved case is whether a real supported workflow converts new environment intelligence into a parent/agent-approved enduring capability change used by later operating agents, rather than simply replaying case context.


## S5 — Policy and identity
- State: —
- Function: No first-party ultimate organizational purpose, identity or constitutional policy authority with a returned decision is supplied in the installed project orchestration boundary.
- Disturbance / variety regulated: Decisions over the organization's identity, constitutive authority and ultimate governing purpose rather than one engineering task or reusable project convention.
- Decisive decision or feedback right: Users approve task-specific irreversible operations and deviations; SOPs enforce fixed gates. No first-party legitimate owner is shown changing organizational ultimate policy and returning that decision to all future operations.
- Decision owner: None established at the declared first-party Konductor deployment recursion; the project user's broader institution is external.
- Supporting / enforcement mechanisms: Strict phase approval gates, `USER DECISIONS IN FORCE` action-specific briefer, configured severity policy, local safety controls, optional user-approved memory/skills.
- Closure path: Task and phase approvals resume or block work, but no authored constitutional policy decision-and-return loop is present.
- Why this is / is not agent-owned: Tool permissions, design review, task override and versioned playbooks are not automatically first-party S5 authority.
- Evidence: [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [agent-sops/k-full-sdlc.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-full-sdlc.sop.md), [skills/delegation-protocol/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/delegation-protocol/SKILL.md), [cli/konductor-rs/src/cli/gate_eval.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/gate_eval.rs), [skills/workspace-skills/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/workspace-skills/SKILL.md)
- Basis: bounded review of shipped agent rules and runtime gate/parent paths
- Confidence: medium-high (scoped negative)
- Caveats: This does not imply the engineers or deploying enterprise lack real S5 governance outside Konductor.

### Absence scope

- Surfaces inspected: [agents/konductor.agent-spec.json](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agents/konductor.agent-spec.json), [agent-sops/k-full-sdlc.sop.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/agent-sops/k-full-sdlc.sop.md), [skills/delegation-protocol/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/delegation-protocol/SKILL.md), [cli/konductor-rs/src/cli/gate_eval.rs](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/cli/konductor-rs/src/cli/gate_eval.rs), [skills/persistent-memory/SKILL.md](https://github.com/aws-solutions/konductor/blob/09c34858ca2e704fb8572c91389a87255b1e1075/skills/persistent-memory/SKILL.md)
- Plausible first-party paths checked: User decisions, irreversible actions, local SOP exceptions, static code review ceilings, safety/gate policies, persistent work memory and configurable setup were tested as possible identity/ultimate-policy paths.
- Why no material first-party path remains: All evidenced decisions either authorize one action, steer the current delivery work, or retain local knowledge; no shipped first-party identity/ultimate-policy authority returns a constitutional change at the declared organization recursion.

## Recursion

The installed project cell has multiple specialist coding/research agents and an orchestration agent with explicit cross-agent assignment, file-scope interference attenuation and independent review paths. Higher-level business/project constitutional governance, Kiro/Claude host architecture and AWS service administration are outside the credited system. Specialist agents may be reused but this alone does not establish a higher viable recursion.

## Variety and escalation

The project applies first-party constraints to cross-writer conflicts (disjoint-file ownership and serial fallback), phase quality (diff-grounded review and adversarial checker), overloaded execution (maximum 4 parallel workers) and failures (bounded fix cycles, 2-strike root-cause analysis). The model-backed orchestrator chooses current interventions; deterministic gate evaluators merely block unsafe phase transitions. Human phase and irreversible-action decisions remain reserved and explicitly scoped, not S5 delegation.

## Evidence gaps

- No actual supported Kiro/Claude model execution, real issue-to-PR lifecycle run, independent human review or empirical reviewer accuracy trace was performed. This is a source/role-contract assessment of installed first-party operating modes.
- S2/A and S3/A rely on the configured Konductor model honoring its shipped delegation/management instructions, not a deterministic server arbiter guaranteeing organizational conflict resolution at scale. Disjoint-file assumptions can be wrong.
- The independent adversarial checker (S3*=A) is source-wired to the real diff and distinct role/session, not a second external OpenSiro reviewer.
- For S4, a specific distributed memory/skill reload route exists but its external-prospective option selection and future managed-team capability closure are unresolved. The current pinned scope does not justify converting this uncertainty to an automatic positive or an unsupported bounded negative.
- S5 absence is restricted to the distributed Konductor project orchestration, not the enterprise parent or users' separate policy institutions.
