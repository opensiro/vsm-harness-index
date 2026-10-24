---
harness_id: lyrie
project_name: Lyrie
repository: https://github.com/OTT-Cybersecurity-LLC/lyrie-ai
review_ref: 96048f6727c01760850e5ef5e1526c8cb9061db8
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Lyrie

## Review boundary

- System in focus: Shipped first-party Lyrie agent and security assessment runtime, including executable TypeScript LyrieEngine model/tool feedback, built-in optional spawn_subagent task delegation, the callable 7-stage `lyrie hack` static/security pipeline, its separate stages A–G finding validator, CLI security/red-team and ATP trust/receipt facilities, along with optional Dream Cycle skill export. Recursion is a deployed Lyrie agent/security assessment installation and its bounded security tasks, not company governance or offensive research publications.
- Purpose and identity: Execute user-authorized security and general tool tasks using a model agent and produce constrained vulnerability findings and remediation suggestions, with evidence filtering and optional defensive monitoring.
- Relevant environment: Target source repos/web assets, local shell, model inference APIs, tool results, trust boundaries/taint graphs, scanner output, security intelligence feeds, user approvals, ATP identity claims and optional subagent tasks.
- Standard-distribution boundary: Installed packages/core agent runtime and src/hack orchestration through documented `lyrie hack` CLI, optional `lyrie redteam`, separately invoked evolve scripts and proof-bearing trust modules. Other installed tools/Shield Rust and provider inference are dependencies. `packages/omega-suite` Claude Code agent role prompts/commands are adjacent *opt-in external host composition*, not injected as ordinary first-party LyrieEngine review/whole-current management.
- Credited operating / distribution surfaces: [packages/core/src/engine/lyrie-engine.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/lyrie-engine.ts); [packages/core/src/engine/model-router.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/model-router.ts); [packages/core/src/tools/tool-executor.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/tools/tool-executor.ts); [packages/core/src/tools/spawn-subagent.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/tools/spawn-subagent.ts); [packages/core/src/agents/subagent-runner.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/subagent-runner.ts); [packages/core/src/agents/sub-agent.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/sub-agent.ts); [packages/core/src/agents/message-bus.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/message-bus.ts); [packages/core/src/agents/coordinator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/coordinator.ts); [packages/core/src/hack/orchestrator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/hack/orchestrator.ts); [packages/core/src/pentest/stages-validator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/pentest/stages-validator.ts); [packages/core/src/pentest/attack-surface.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/pentest/attack-surface.ts); [packages/core/src/remediation-pr/revalidate.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/remediation-pr/revalidate.ts); [packages/core/src/aav/adversarial-loop.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/aav/adversarial-loop.ts); [packages/core/src/agents/verifier.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/verifier.ts); [packages/core/src/evolve/dream-cycle.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/evolve/dream-cycle.ts); [packages/core/src/evolve/skill-extractor.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/evolve/skill-extractor.ts); [packages/core/src/skills/skill-manager.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/skills/skill-manager.ts); [scripts/evolve.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/scripts/evolve.ts); [scripts/hack.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/scripts/hack.ts); [README.md](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/README.md).
- Adjacent first-party surfaces excluded from ownership: Standalone CVE proof/exploit labs under research/, README promises and numbers, external Claude Code omega-suite role prompts as installed LyrieEngine agents, static unused coordinator-mode constants, stand-alone test assertions, third-party model/provider internals, future model training outside the runtime and project-maintainer governance.
- First-party operating / deployment modes considered: Standard LyrieEngine tool conversation, optional user/model-spawned single child and isolated parallel workers, CLI `lyrie hack` quick/standard/deep/paranoid pipeline, dedicated adversarial `runAdversarialLoop`, optional remediation PR revalidation, manual scheduled `lyrie evolve dream`, and daemon tick. Not all distinct modes execute in the same session.
- Recursion level: One deployed Lyrie security-agent organization with one native LLM S1 operation, optionally delegated bounded child research/tool tasks and a distinct static security scanner/validator. Generic dispatch and scripted phases are not promoted to autonomous managerial VSM decisions.
- Reviewed revision: `96048f6727c01760850e5ef5e1526c8cb9061db8` frozen #186 and batch #1648 row 9.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipped `LyrieEngine.process` performs first-party `ShieldManager.scanInput`, memory recall and `ModelRouter.route`, then directly invokes a configured model and parses its structured tool-call choices. `ToolExecutor.execute` enforces the Shield boundary and runs built-in local file/web/shell/browser and user-selected tools; the *actual result* returns as a tool message to the next model turn, bounded by maximum turns/tool calls. `spawn_subagent` is registered as a model-callable built-in and creates a fresh model/tool engine and returns result/error to the parent. This is a reachable autonomous S1 agent/task feedback loop. [packages/core/src/engine/lyrie-engine.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/lyrie-engine.ts); [packages/core/src/tools/tool-executor.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/tools/tool-executor.ts); [packages/core/src/tools/spawn-subagent.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/tools/spawn-subagent.ts); [packages/core/src/agents/subagent-runner.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/subagent-runner.ts).

The documented seven-stage `lyrie hack` is a separate first-party **deterministic** assessment pipeline: `HackOrchestrator.run` performs recon/attack-surface and dependency identification, scanning plus secret checks, stage-wise finding validation, remediation **suggestion** generation, formatting and conditional Shield self-scan. The `--aav` ATTACK phase explicitly records a deferred launch event (the actual redteam script is separate); it does not execute an autonomous security attack inside that orchestrator. The supplied concurrency option for this path is advisory, with inline scanners. Reporting seven stages as seven independent S1 agents would misidentify ownership and parallelism. [packages/core/src/hack/orchestrator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/hack/orchestrator.ts); [scripts/hack.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/scripts/hack.ts).

`validateBatch` runs deterministic Stage A pattern checks, Stage B reachability against a separately built `AttackSurface`, Stage C code-path/test context, Stage D go/no-go, Stage E optional PoC construction and Stage F suggested remediation; Stage G deduplicates findings. It can downgrade confidence/severity, mark raw scanner claims `confirmed=false`, and suppress unsupported findings before remediations and reports. The alternative trust-boundary/flow evidence and filtering create a **bounded constructor-owned complementary challenge path** for scanner finding claims (S3*=C), not independent human or separate autonomous model criticism. Stage E PoC is a generated snippet/precondition, not proof of executed exploit; a `LyrieVerifier` model-critic *prompt/parser class* elsewhere is not invoked by ordinary `LyrieEngine.process` or `HackOrchestrator.run`. [packages/core/src/pentest/stages-validator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/pentest/stages-validator.ts); [packages/core/src/hack/orchestrator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/hack/orchestrator.ts); [packages/core/src/agents/verifier.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/verifier.ts).

The `SubAgentManager` tracks bounded separate model/tool workers and emits results, but its concurrency limit and `AgentMessageBus` simply constrain capacity and transport Shield-filtered messages. No source-backed different-S1 collision and responsive coordination of sibling task behavior was found. A `LyrieCoordinator` mode class exports tool whitelist and prompts, but source search located no actual first-party `LyrieEngine` instantiation or call that activates it in normal runtime; the built-in spawn tool waits for the child and returns its result to the same current parent task. No installed whole-current multi-operation resource bargain/exception-intervention S3 is evidenced by those names alone. [packages/core/src/agents/sub-agent.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/sub-agent.ts); [packages/core/src/agents/coordinator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/coordinator.ts); [packages/core/src/engine/system-prompt.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/system-prompt.ts).

The optional `lyrie evolve dream` batch selects scored outcomes and writes proposed markdown `SKILL.md` descriptions under `~/.lyrie/evolve/skills`; its default `HeuristicExtractorLLM` groups by domain and copies previous summaries without autonomous future capability-option judgment. `LyrieEngine` calls `SkillManager.checkForImprovement` with an **empty step list**, which immediately returns null, and `SkillManager` loads `~/.lyrie/skills/*.json`, **not** the Dream Cycle's output markdown directory. Thus no default first-party loop from changing external environment → prospective skill option/model decision → selected, admitted installed capability → later S1/S3 is established. This is stronger negative evidence than treating the words `evolve` and `self-heal` as proof of S4. [packages/core/src/engine/lyrie-engine.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/lyrie-engine.ts); [packages/core/src/skills/skill-manager.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/skills/skill-manager.ts); [packages/core/src/evolve/dream-cycle.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/evolve/dream-cycle.ts); [scripts/evolve.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/scripts/evolve.ts).

A separate `runAdversarialLoop` mutates known successful attack vectors with fixed transformations to test whether a *target endpoint* remains vulnerable across rounds. It is a task-level security-test campaign, not an organizational decision to develop or adopt Lyrie's future abilities; source exports this separate callable module but `lyrie hack` does not execute it inline. ATP signed trust attestations and kill-switch constrain identity/claims/authorization but do not settle ultimate organization purpose/policy as an S5 decision. [packages/core/src/aav/adversarial-loop.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/aav/adversarial-loop.ts); [packages/core/src/hack/trust-attestation.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/hack/trust-attestation.ts); [packages/atp/src/verify.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/atp/src/verify.ts).

## S1 — Operations

- State: A
- Function: Perform bounded autonomous model-directed user/security tasks with actual tool/environment observations returned to the model.
- Disturbance / variety regulated: Unknown security/tool requests, differing repository/website states, uncertain code context, command failures, changing data and optional concurrent child work.
- Decisive decision or feedback right: First-party `LyrieEngine` accepts user task, model decides next built-in tool and arguments conditioned on previous actual Shield-gated result; optional model choice of `spawn_subagent` produces independently executed worker result, then parent model continues.
- Decision owner: Configured model acting through first-party LyrieEngine/ToolExecutor and separate first-party isolated subagent runner, rather than an externally authored ACP agent.
- Supporting / enforcement mechanisms: ModelRouter, Shield input/tool and untrusted output checks, memory retrieval, tool registry and tool execution, max turns/max tool calls, subagent context/time limits.
- Closure path: user/source task → first-party model/tool decision → real tool (or model-spawned subagent) execution → observation/error returned as tool role → model revises next action/final result.
- Boundary reachability: `scripts/start-all.ts` constructs real LyrieEngine, `LyrieEngine.initialize` registers tools including `spawn_subagent`, and `process` directly invokes `ToolExecutor.execute` in response to model actions. Documented `lyrie hack` is another static security task operation.
- Why this is / is not agent-owned: The model selects substantive tools/next steps dynamically; Lyrie owns implementation of loop and action-result feedback. Defensive tool rules constrain, but do not themselves choose the semantic task.
- Evidence: [packages/core/src/engine/lyrie-engine.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/lyrie-engine.ts); [packages/core/src/tools/tool-executor.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/tools/tool-executor.ts); [packages/core/src/tools/spawn-subagent.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/tools/spawn-subagent.ts); [scripts/start-all.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/scripts/start-all.ts).
- Basis: Explicit first-party reachable model/tool loop.
- Confidence: High for code-level path; no actual provider model or pentest task run attempted.
- Caveats: Model API keys and appropriate target authorization required. Prompt-only safety shouldn't be construed as a universal complete authorization system.


## S2 — Coordination

- State: —
- Function: No specific first-party function demonstrably corrects interfering or oscillating behavior between distinct autonomous operating units.
- Disturbance / variety regulated: Spawning too many subagent tasks can exceed configured capacity and messages may contain untrusted text, but those are general throughput and content-safety constraints rather than a witnessed cross-agent collision/oscillation.
- Decisive decision or feedback right: Subagent concurrency limit rejects new tasks, in-process bus routes Shield-filtered messages, and parent awaits/collects results; no interference-sensitive sibling adjustment judgment is evidenced.
- Decision owner: Static SubAgentManager limits and transport bus, with parent agent supplying task instructions but not a demonstrated S2 correction.
- Supporting / enforcement mechanisms: maxConcurrent, maxTurns, timeout/abort, results Map, message-bus subscriber/recipient routes, Shield filtering.
- Closure path: Model chooses spawn → capacity admission/error/result → same parent's task continuation; not conflict between two S1 actions → coordination selection → modified sibling actions.
- Distinct S1 units: Separately model-driven child loops are real when model-spawned; the configured manager can run several. Their concurrency alone is not S2.
- Inter-S1 disturbance: No source-specific competing target/worker write collision, oscillation or actual resource conflict addressed with mutual adaptive behavior, only fixed process admission.
- Why this is / is not agent-owned: An allowed maximum parallel count, a shared A2A bus and a task aggregation call don't independently prove S2 function or owner.
- Evidence: [packages/core/src/agents/sub-agent.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/sub-agent.ts); [packages/core/src/agents/message-bus.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/message-bus.ts); [packages/core/src/agents/subagent-runner.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/subagent-runner.ts).
- Basis: Bounded negative search on strongest coordination candidates.
- Confidence: Medium-high for standard current code.
- Caveats: Separate external users can organize worker teams, but their coordination isn't automatically first-party.

### Absence scope

- Surfaces inspected: SubAgentManager spawnAll, spawn_subagent model tool, message-bus, coordinator mode constants, multi-turn task loop and static HackOrchestrator stage sequencing.
- Plausible first-party paths checked: Shared worker concurrency, tool contention, agent-to-agent messages, parent-child delegation, program phase status.
- Why no material first-party path remains: No observed first-party collision-sensitive inter-S1 adjustment/feedback, beyond capacity rejection, generic transport and task-decomposition sequencing.


## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current manager of independently ongoing operations with system-wide prioritization, commitments and exception intervention was established.
- Disturbance / variety regulated: Long tasks, phase failures, accumulated child results and scan findings are regulated locally by S1 task loops and deterministic stage scripts.
- Decisive decision or feedback right: The model may choose to spawn or await child tasks, while HackOrchestrator always executes a fixed ordered security assessment workflow. Neither demonstrates live regulation of competing current operational work commitments across the whole deployment.
- Decision owner: Within-task Lyrie model and static script; no separate installed whole-current manager.
- Supporting / enforcement mechanisms: LyrieCoordinator prompt/whitelist (not activated in LyrieEngine), model router, task count limits, HackOrchestrator phase/scan report and daemon tick callbacks.
- Closure path: A child's output affects its parent's same task and scripted phases advance to report. No whole-installation current state → authorized resource/priority intervention → redistributed operating commitments feedback path identified.
- Why this is / is not agent-owned: Coordinator-labelled static constants lack runtime ownership, and the task's own next-step selection is S1 rather than Beer S3. The daemon schedules tick callback but doesn't own current cross-S1 resource arbitration.
- Evidence: [packages/core/src/agents/coordinator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/coordinator.ts); [packages/core/src/engine/lyrie-engine.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/lyrie-engine.ts); [packages/core/src/hack/orchestrator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/hack/orchestrator.ts); [packages/core/src/engine/daemon.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/daemon.ts).
- Basis: Bounded negative of supplied first-party whole-now decision paths.
- Confidence: Medium-high.
- Caveats: A different deployment using custom orchestration might implement current work management atop these APIs; not part of pinned standard configuration.

### Absence scope

- Surfaces inspected: Main model tool turns, spawned children, LyrieCoordinator class/use-site search, static hack phase, daemon tick, ModelRouter and trust-score dashboard.
- Plausible first-party paths checked: Coordinator mode, agent status/kill/message tools, priority scoring, incident queue, automated remediation revalidation, health dashboard and daemon scheduling.
- Why no material first-party path remains: No reachable first-party actor or constructor has a whole-current operational view *and* distinct relevant current-commitment selection/feedback rights.


## S3* — Complementary audit

- State: C
- Function: Challenge scanner-proposed vulnerability findings using distinct attack-surface/trust-boundary, structural reachability and code-path facts and feed corrections into reported and remediated claims.
- Disturbance / variety regulated: False-positive syntactic scanner matches, findings in tests/comments/dead code, missing reachability evidence and unjustified severity or unsupported confirmation.
- Decisive decision or feedback right: Static Stages A–D re-evaluate raw scanner claims using separate source/reachability/trust-boundary context, downgrade/deny confirmation and select which claims pass through to remediations and final security report.
- Decision owner: First-party deterministic `validateBatch` and precomputed separate `AttackSurface` evidence; there is no independently deciding model or human reviewer in the `lyrie hack` path.
- Supporting / enforcement mechanisms: RawFinding annotations, shield pattern reality checks, AttackSurface map/flow context, staged StageVerdict labels, severity/confidence thresholds, PoC snippet/human precondition and dedup logic.
- Closure path: Raw scanner finding → alternative trust-boundary/reachability/source code context → A/B/C/D validator sets `confirmed`/severity/confidence → HackOrchestrator only generates remediations from confirmed and serializes filtered/confirmed lists into actual report.
- Claim being audited: Whether a scanner-emitted potential vulnerability is supported as a confirmed/reachable security issue worth remediation.
- Ordinary reporting path: The scanning engine's raw findings and reported severity.
- Complementary access path: Independently built first-party AttackSurface representation and deterministic code-path/test-context heuristics, rather than simply accepting scanner label.
- Independence boundary: Different analysis rules and extra context within same process; no independent model, live PoC proof by default, tamper-proof scanner provenance or detached human verifier. Findings with incomplete evidence can slip through.
- Who acts on findings: `HackOrchestrator.run` consumes `validated`, creates suggested fixes only for confirmed findings and prepares JSON/SARIF/Markdown reports. Stage F auto-fix/PoC is not certified execution.
- Boundary reachability: `lyrie hack` command's `HackOrchestrator.run` calls `validateBatch(rawFindings,{surface,shield,fastMode})`; the resulting `confirmed` flags actually influence remediation/report state.
- Why this is / is not agent-owned: Deterministic complementary adjudication owns the challenge and return; `LyrieVerifier` class prompts cannot be given credit as a live autonomous audit where normal process never instantiates it. Thus S3*=C.
- Evidence: [packages/core/src/hack/orchestrator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/hack/orchestrator.ts); [packages/core/src/pentest/stages-validator.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/pentest/stages-validator.ts); [packages/core/src/pentest/attack-surface.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/pentest/attack-surface.ts); [packages/core/src/agents/verifier.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/agents/verifier.ts).
- Basis: Source-reachable static alternative-evidence adjudication, bounded coverage.
- Confidence: Medium; stage verification is weaker than independent artifact replay or secondary agent critique.
- Caveats: Part of routine security-pipeline gating; doesn't establish independent reviewer deployment. Some stages use metadata provided by same RawFinding source rather than independently rereading repository content.


## S4 — Outside-and-then intelligence

- State: —
- Function: No actual first-party future-oriented organizational capability-adaptation loop closed from external environment feedback through selected options into the installed agent's later operations.
- Disturbance / variety regulated: Outcome quality, evolving threats, adversarial target prompts and missed skills provide improvement clues but are not in themselves organizational prospective adaptation.
- Decisive decision or feedback right: Manual `lyrie evolve dream` invokes a heuristic outcome-to-markdown skill extractor and pruning, while engine post-task `checkForImprovement` is supplied an empty step list and always returns null. The extracted `~/.lyrie/evolve/skills/*.md` aren't the `~/.lyrie/skills/*.json` objects loaded by `SkillManager`. No real autonomous proposal/admission into future operational skill selection is shown.
- Decision owner: Operator invokes batch, deterministic score/prune rules and optional custom LLM interface that isn't the shipped default skill-content chooser.
- Supporting / enforcement mechanisms: DreamCycle, SkillExtractor heuristic fallback, scored task outcomes, SKILL.md files, cosine duplicate checks, training-data exporter; separate per-task adversarial corpus mutation.
- Closure path: Scored prior outcomes → written markdown skill candidates and report. **Missing:** admitted skill consumed by default SkillManager → changed later autonomous tool/strategy choice or a feedback loop with current management.
- External distinction: Threat feeds and target responses are observed in current research; no demonstrated environmental option tracking beyond task-level data.
- Future / prospective distinction: Dream is named as future skill improvement, but no installed skill-adoption/selection link into runtime was found.
- Adaptation option generated: Heuristic summaries/markdown patterns in a separate optional batch directory, or operator-selected train exporter output, not first-party model-chosen future strategy installed in the active engine.
- Path back into current capability / S3: No verified import from evolving markdown directory into active JSON skill registry or model/tool next-run control; developers could wire it later, not creditable now.
- Why this is / is not agent-owned: Default heuristic summaries and file creation do not constitute an autonomous model selecting tested future capability change. AAV mutation changes a **target test stimulus**, not Lyrie's enduring organizational skill.
- Evidence: [packages/core/src/engine/lyrie-engine.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/lyrie-engine.ts); [packages/core/src/skills/skill-manager.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/skills/skill-manager.ts); [packages/core/src/evolve/dream-cycle.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/evolve/dream-cycle.ts); [packages/core/src/evolve/skill-extractor.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/evolve/skill-extractor.ts); [scripts/evolve.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/scripts/evolve.ts); [packages/core/src/aav/adversarial-loop.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/aav/adversarial-loop.ts).
- Basis: Bounded negative investigation of stronger reachable model improvement candidates and missing operational return.
- Confidence: Medium-high for standard run; future integrations could close the path.
- Caveats: An operator can manually consume generated markdown or train another model externally; that is a different operating mode and doesn't establish an installed first-party S4.

### Absence scope

- Surfaces inspected: Dream Cycle/SkillExtractor, post-turn SkillManager, code-skill registration and load format, adversarial mutation loop, threat feed updates and model route configuration.
- Plausible first-party paths checked: Scored feedback to learned skills, generated SKILL.md deployment, self-heal pipeline, continuous threat watcher, cyclic AAV testing.
- Why no material first-party path remains: The generated artifacts are not consumed by the default runtime; no externally/prospectively owned option comparison, choice and return into actual future organizational capability is demonstrated.


## S5 — Policy and identity

- State: —
- Function: No separate ultimate purpose/ethos/policy authority or conflict settlement loop established for the deployed agent organization.
- Disturbance / variety regulated: Tool permissions, credentials, unauthorized commands, untrusted output and agent identity/scope revocation are security concerns governed by preconfigured trust rules.
- Decisive decision or feedback right: Operator/project maintainers configure Shield/permissions/trust certs, and deterministic signed ATP verifies scope/revocation and permission gates. No actor changes ultimate mission/identity under a legitimate higher-level policy decision.
- Decision owner: External operator/organization for policy selection; static cryptographic and Shield primitives for enforcing choices.
- Supporting / enforcement mechanisms: ATP identity certificates, receipts, scope permissions, revocation/kill-switch, Shield scans, risk classes, memory integrity and governance scorecard.
- Closure path: Static identity/allowed scope → validate request/tool/attestation and optionally block. No first-party ultimate value dispute → policy judgment → S3/S4 return or identity revision loop.
- Why this is / is not agent-owned: Cryptographic identity/safety enforcement isn't a live S5 policy holder, even if sophisticated or branded 'agent trust protocol'.
- Evidence: [packages/atp/src/verify.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/atp/src/verify.ts); [packages/atp/src/scope.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/atp/src/scope.ts); [packages/atp/src/kill-switch.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/atp/src/kill-switch.ts); [packages/core/src/governance/permissions.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/governance/permissions.ts); [packages/core/src/engine/shield-manager.ts](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai/blob/96048f6727c01760850e5ef5e1526c8cb9061db8/packages/core/src/engine/shield-manager.ts).
- Basis: Bounded negative of active policy/identity paths.
- Confidence: Medium-high.
- Caveats: The real parent security organization may provide S5 outside this standalone OSS runtime.

### Absence scope

- Surfaces inspected: ATP and signed trust rules, safety prompts/Shield, governance permissions/scorecard and human approvals.
- Plausible first-party paths checked: Identity certificate, signing, revocation, kill-switch, operator rules, audit receipts, model routing preferences.
- Why no material first-party path remains: Those verify or enforce already selected authority; no independently chosen ultimate purpose/ethos governance and corrective return occurs within first-party runtime.


## Distributed OSS parent arrangement

Project maintains a Rust Shield service, TypeScript agent engine, CLI security scanning and optional Claude-hosted Omega Skills. The first-party `LyrieEngine` supplies its own tool loop while externally served language model supplies token inference; Omega's host/agent roles are not automatically part of the same live TypeScript operator. Project governance/ATP identity owner is not equated with Beer S5. Registered subagents are tools of a task and no independently governed cross-task metasystem is inferred.

## Self-hosted and non-human modes

Local or hosted inference needs configured model provider and defensive tool access. Headless daemon supplies periodic tasks but not automatically a current whole-work control authority. An opt-in operator invocation of `lyrie redteam` can exercise AAV corpus mutations; those may challenge a target but don't rewrite Lyrie's own control plane. Opt-in PR remediation revalidation after actual opened PR applies proof comments, not a guaranteed independent systematic agent critic. No live pentest, security exploit, GPU training or target scan was executed in this review.

## Recursion

At one Lyrie deployment, the main model/tool loop is operational S1; child agent loops are nested task cells. Static security scanner produces raw vulnerability findings, while a separate deterministic validator can challenge/remediate those claims (bounded S3* constructor). Capacity limits and plain A2A message bus do not prove inter-S1 S2, task-level orchestration is not a metasystem S3, stand-alone dream artifacts do not close a future capability S4 loop, and static ATP policy doesn't implement S5.

## Variety and escalation

Model/tool actions and scanner integrations amplify response to unknown requests/target artifacts. Shield and ATP attenuate untrusted input/permissions; source validation challenges scanner label inflation. Suspicious findings or dangerous changes are escalated to output/user approval/PR checks, without evidence that any external operator is the first-party ultimate policy owner at assessed recursion.

## Evidence gaps

- Structural pinned-source review, not security effectiveness or remote exploit tests, nor claims about published CVE lab results.
- S3*=C is confined to distinct scanner validation evidence/heuristics and can be incomplete; no model/human independent verifier automatically installed in normal HackOrchestrator and no experimentally reproduced false-positive accuracy.
- Coordinator class and prompt exist but no identified ordinary engine activation/whole-current portfolio decision. A more complete hosted implementation might change S3; not borrowed.
- Dream output directory/format doesn't match normal loaded skills; generated patterns and training exporter alone don't demonstrate S4 feedback/admission.
- S2, S3, S4, S5 negative states are bounded standard-distribution findings, not universal inability to implement those functions.
