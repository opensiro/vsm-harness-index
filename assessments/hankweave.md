---
harness_id: hankweave
project_name: hankweave
repository: https://github.com/SouthBridgeAI/hankweave-runtime
review_ref: 9ea76bbb826becb6ab148bec9dd3aeb00b410c61
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# hankweave

## Review boundary

- System in focus: one Hankweave long-horizon run using a first-party hank execution plan, codons/loops, harness adapters, rigs/workspace setup, budgets, sentinels, event journal, checkpoints/rollback, retry/recovery and runtime/socket lifecycle.
- Purpose and identity: execute long-running autonomous agentic programs reproducibly and repairably by orchestrating existing coding-agent harnesses as execution primitives while Hankweave owns sequencing, isolation, state, monitoring, budgets and recovery support.
- Relevant environment: hank-authored data/prompts/configuration, target files/workspace, external coding-agent harnesses and model providers, runtime failures, budget/resource limits and event-stream consumers.
- Standard-distribution boundary: first-party `hankweave-runtime`, hank/codon/loop configuration and supported adapters. Claude Code, Codex, Gemini CLI, Pi, OpenCode and other harnesses remain external autonomous execution backends; their undocumented internal organization is not imported into Hankweave.
- Credited operating / distribution surfaces: runtime server, codon runner and adapter invocation path, state manager/execution plan, rigs, budgets, retries/recovery, checkpoints/rollback, event journal, sentinels and socket/headless lifecycle.
- Adjacent first-party surfaces excluded from ownership: contributor/CI/release infrastructure, documentation indexing/publishing, tests, `learning/examples/` including Clausetta when used as an example/development workflow rather than part of the standard running hank, and Southbridge organizational processes outside a Hankweave run.
- First-party operating / deployment modes considered: headless/hermetic hank execution with supported harness adapters, codon/loop sequencing, configured budgets/retry policy, sentinels, checkpoints/rollback and programmatic/socket operation.
- Recursion level: one running hank. A codon invokes one autonomous agentic execution thread; the hank sequences those operational transformations over a long horizon but intentionally runs only one agentic thread at a time.
- Reviewed revision: `9ea76bbb826becb6ab148bec9dd3aeb00b410c61`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Hankweave explicitly describes itself as a runtime that orchestrates existing agent harnesses rather than reimplementing a coding agent. A hank declares prompts, codons, loops, rigs, sentinels, context boundaries and file tracking. The runtime starts the selected supported agent backend for a codon, streams/normalizes its events, persists state, advances the execution plan and creates checkpoints at codon boundaries. It is intentionally single-threaded at the agentic level: only one agent executes at a time.

The runtime supplies substantial deterministic regulation around that autonomous work. Budgets meter cost/time/tokens and can terminate variable loops; retry/recovery logic classifies failures and retries or stops according to authored policy; state and checkpoints support resume/rollback; the event journal records execution. These paths can strongly constrain current operation, but the inspected decisive choices are authored configuration and runtime rules rather than a first-party autonomous whole-hank S3 actor.

Sentinels are parallel observers over server-state and agentic-backbone events. They can trigger deterministic code or LLM calls, maintain their own history and emit/write outputs. The README frames them as noticers, real-time evals, drift/guardrail/cost monitors. At the pinned revision, however, sentinel outputs are persisted/broadcast and are deliberately not routed back into sentinels; no standard first-party path was established in which an independent sentinel audit judgment itself closes into Hankweave current-control intervention. That distinction prevents treating observability/evaluation naming as S3*.

Primary evidence:

- [`README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/README.md) — runtime boundary, single agentic thread, harness abstraction, sentinels, budgets, checkpoint/rollback and headless operation.
- [`server/hankweave-runtime.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/hankweave-runtime.ts) — codon lifecycle, state/retry/budget/sentinel integration, event routing and runtime control.
- [`server/budget.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/budget.ts) — deterministic budget tracking/enforcement and execution-plan allocation.
- [`server/retry-coordinator.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/retry-coordinator.ts) — authored retry/failure-policy bookkeeping.
- [`server/sentinels/sentinel.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/sentinels/sentinel.ts) and [`server/config-validation/sentinel.schema.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/config-validation/sentinel.schema.ts) — independent event-triggered observer execution, LLM/deterministic processing and output configuration.

## Operational model

The operational agent in a codon is autonomous and chooses substantive actions inside the invoked coding-agent harness. Hankweave supplies the first-party execution contract: select the adapter/model/config from the hank, prepare a deterministic workspace/rig, run the agent headlessly, normalize/persist events and result state, then advance the long-horizon plan. External harness internals are treated as execution substrate; credit is limited to the operational agent role actually reachable through Hankweave's shipped adapter contract.

Because Hankweave deliberately serializes agentic execution, codons/loops are not automatically multiple simultaneous S1 units requiring S2. Likewise, deterministic sequencing, budget allocation, retries and rollback are not upgraded to S3 simply because they affect all current work. Sentinels are kept separate from the main agent's event path, but their standard output/reporting path does not by itself establish S3* corrective closure.

## S1 — Operations

- State: A
- Function: perform the substantive autonomous transformation assigned to each agentic codon within a long-running hank.
- Disturbance / variety regulated: open-ended coding/data/research work, workspace state, tool outcomes, intermediate failures and task-specific ambiguity encountered during the codon's objective.
- Decisive decision or feedback right: choose the substantive tool/reasoning/file actions used to achieve the codon's prompt-defined outcome.
- Decision owner: the autonomous agent session invoked through a supported Hankweave harness adapter.
- Supporting / enforcement mechanisms: hank/codon prompt and configuration, adapter/shim process, deterministic rigs/workspace preparation, event normalization, context boundaries, state manager, filesystem/tool access and runtime lifecycle.
- Closure path: Hankweave prepares the codon/workspace → launches the configured autonomous agent harness → agent acts and receives tool/workspace observations in its execution loop → resulting artifacts/session outcome return to Hankweave → runtime persists completion and advances the hank.
- Boundary reachability: supported Claude Code/Codex/Gemini/Pi/OpenCode adapter invocation is a first-party standard Hankweave operating surface; the agent actor is external software but is directly instantiated as the documented operational primitive of a running hank rather than borrowed from an adjacent development system.
- Why this is / is not agent-owned: Hankweave controls execution conditions, while the invoked autonomous agent chooses the substantive steps within the codon; deterministic rigs/budgets do not make those task decisions.
- Evidence: [`README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/README.md), [`server/hankweave-runtime.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/hankweave-runtime.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this state does not import S2-S5 functions from the internals of Claude Code/Codex/etc.; only their role as autonomous S1 execution actors in the Hankweave operating contract is used.

## S2 — Coordination

- State: —
- Function: no material S2-specific attenuation of interference among distinct simultaneous S1 units is established at the reviewed hank recursion.
- Disturbance / variety regulated: not established as an inter-S1 disturbance.
- Decisive decision or feedback right: not established as S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: codon sequencing, loops, harness switching, context boundaries, rigs and checkpoints separate work over time but do not evidence coordination of interacting S1 units.
- Closure path: one codon completes before the execution plan advances to the next; this serial dependency path is not itself S2.
- Why this is / is not agent-owned: Hankweave explicitly chooses a single agentic thread; using different harnesses for different codons or sequencing transformations does not establish multiple interacting S1 units plus a conflict/oscillation attenuation loop.
- Evidence: [`README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/README.md), [`server/hankweave-runtime.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/hankweave-runtime.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a hank may sequence heterogeneous specialist codons, but specialization over time is not sufficient to reconstruct an S2 witness at this recursion.

### Absence scope

- Surfaces inspected: codon/loop execution plan, harness adapters, rigs, workspace boundaries, state manager, checkpointing, sentinels and event routing.
- Plausible first-party paths checked: harness switching, loop sequencing, codon boundaries, shared workspace state and sentinel parallel observation.
- Why no material first-party path remains: only one agentic operational thread runs at a time; no concrete interference/oscillation among distinct active S1 units and dedicated attenuation relation was established.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous whole-hank inside-and-now control owner is established in the standard distribution.
- Disturbance / variety regulated: budget exhaustion, codon failure, retryable errors, shutdown/resume conditions, loop completion, checkpoint/rollback requests and runtime lifecycle are regulated, but primarily by authored policy and deterministic runtime machinery.
- Decisive decision or feedback right: no first-party autonomous actor is shown choosing whole-hank resources, commitments, priorities or interventions from a current system view.
- Decision owner: hank author/operator configuration and deterministic runtime logic for the inspected paths; external clients can also issue runtime commands.
- Supporting / enforcement mechanisms: `Budget`, execution plan/state manager, retry coordinator, failure classification, auto-start/advance, checkpoints/rollback, shutdown watchdog and socket commands.
- Closure path: current events/state can trigger configured retry/stop/advance/budget effects, but those effects execute preselected rules rather than an autonomous organizational judgment over the whole running hank.
- Why this is / is not agent-owned: an S1 codon agent owns its local task actions. It is not evidenced as seeing/controlling the whole hank's current commitments, while the runtime mechanisms that do see the plan are deterministic enforcers.
- Evidence: [`README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/README.md), [`server/hankweave-runtime.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/hankweave-runtime.ts), [`server/budget.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/budget.ts), [`server/retry-coordinator.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/retry-coordinator.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: Hankweave has strong current-operation enforcement and programmatic control. Methodology 0.3.5 does not award `A` for enforcement authority, and the reviewed generic control APIs do not establish an S3-specific autonomous constructor sufficient for `C`.

### Absence scope

- Surfaces inspected: runtime/state manager, codon lifecycle, execution plan, budgets, retry/failure policy, loop termination, checkpoint/rollback, resume/shutdown commands, sentinels and headless/programmatic operation.
- Plausible first-party paths checked: budget distribution/termination, automatic next-codon start, failure retry/abort behavior, rollback/recovery, runtime commands and sentinel monitoring.
- Why no material first-party path remains: the identified whole-run effects are deterministic consequences of authored configuration or externally issued commands; no autonomous actor with whole-system current view and discretionary S3 feedback right is established.

## S3* — Complementary audit

- State: —
- Function: sentinels provide complementary observation/evaluation surfaces, but no standard first-party independent-audit-to-corrective-control closure is established strongly enough for S3*.
- Disturbance / variety regulated: sentinels can notice drift, laziness, convention violations, cost anomalies or event patterns, but the decisive organizational audit response is not closed by the standard runtime path.
- Decisive decision or feedback right: no standard independent verdict/right is established that can change subsequent whole-hank operation as S3*.
- Decision owner: sentinel processing can be deterministic or LLM-driven, while subsequent operational intervention remains authored/external unless separately composed.
- Supporting / enforcement mechanisms: separate sentinel trigger engine, event access, optional conversational history, LLM calls/structured output, output/log files, sentinel lifecycle/error events and WebSocket publication.
- Closure path: runtime/server and agentic-backbone events are routed to sentinels → sentinel computes/emits output → output is persisted/broadcast or written according to configuration; a standard findings → S3 corrective decision → changed subsequent operation path was not established.
- Why this is / is not agent-owned: the sentinel can independently notice and judge patterns, but complementary observation without a reconstructable corrective return loop is insufficient for S3*.
- Evidence: [`README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/README.md), [`server/sentinels/sentinel.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/sentinels/sentinel.ts), [`sentinel.schema.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/config-validation/sentinel.schema.ts), [`server/hankweave-runtime.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/hankweave-runtime.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: README examples describe guardrails/intervention and automatic throttling as possible sentinel uses. At the pinned standard runtime boundary, that capability is not enough to prove a default independent audit judgment with corrective closure; a concrete hank can compose such a loop and would require its own system-in-focus assessment.

### Absence scope

- Surfaces inspected: sentinel trigger/configuration/runtime, event routing, sentinel output/history, WebSocket/event journal, budget/retry/runtime control and documented sentinel use cases.
- Plausible first-party paths checked: drift/convention monitoring, LLM evaluators, guardrail examples, cost tracking/throttling claims, output files, sentinel events and consumer reactions.
- Why no material first-party path remains: the shipped sentinel machinery establishes observation and evaluator output, but the reviewed standard path does not close those findings into an independent audit decision that returns through S3 to alter subsequent hank operation without additional composition.

## S4 — Outside-and-then intelligence

- State: —
- Function: no standard runtime-level prospective environment-sensing adaptation loop is established at the assessed hank recursion.
- Disturbance / variety regulated: not established as S4 within the running-hank standard distribution.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: hanks can accumulate authored fixes, codons can process external data, sentinels can surface failure patterns and the repository includes Clausetta for generating harness shims, but these do not establish an always-reachable runtime S4 owner at this boundary.
- Closure path: operational outputs/failures can inform later human/developer repair; no first-party runtime loop autonomously senses future environmental change, chooses an adaptation and installs it into later hank capability.
- Why this is / is not agent-owned: maintainability and repairability are design goals, not by themselves S4. Clausetta is a separate example/development hank under `learning/examples/`, not imported as the S4 organ of every standard Hankweave run.
- Evidence: [`README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/README.md), [`learning/examples/clausetta/README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/learning/examples/clausetta/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a specific adaptive hank, including a Clausetta-based organization, may itself establish S4 and should be assessed as a separate system-in-focus rather than projected onto the runtime.

### Absence scope

- Surfaces inspected: runtime state/history, event journal, sentinels, checkpoint/recovery, examples/learning material, frozen-hank maintenance claims and Clausetta shim-generation example.
- Plausible first-party paths checked: accumulated fixes, event-derived repair, sentinel findings, automatic shim generation and runtime resume/recovery.
- Why no material first-party path remains: the running runtime does not close prospective external sensing → adaptation-option generation → selected capability change; the strongest adaptation example is a separately authored hank/development surface rather than a standard organ of the assessed runtime.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established for the running hank.
- Disturbance / variety regulated: hank prompts, runtime config, model choice, budgets, retry/failure policies and operator commands constrain execution but do not constitute an evidenced identity-level policy dispute.
- Decisive decision or feedback right: not established as S5.
- Decision owner: hank author/operator for configuration and purpose constraints.
- Supporting / enforcement mechanisms: hank JSON/frontmatter, prompt files, runtime config, budget limits, model/harness selection and programmatic/socket controls.
- Closure path: authored constraints govern execution directly; no identity/ultimate-policy matter is escalated to a legitimate S5 authority and returned as a changed governing policy through the runtime.
- Why this is / is not agent-owned: configuration and task prompts specify what the run should do, but Methodology 0.3.5 does not equate authored task purpose, budgets or operator control with S5 identity closure.
- Evidence: [`README.md`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/README.md), [`server/config.ts`](https://github.com/SouthBridgeAI/hankweave-runtime/blob/9ea76bbb826becb6ab148bec9dd3aeb00b410c61/server/config.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: human authors intentionally retain strong authority over hank purpose and constraints; static or invocation-time authorship alone is not a positive parent S5 loop.

### Absence scope

- Surfaces inspected: hank/config/prompt contracts, budgets, harness/model selection, runtime/socket controls, sentinel configuration and failure/retry policies.
- Plausible first-party paths checked: operator configuration, competing author/operator budgets, runtime control commands, prompt-defined purpose and sentinel policy.
- Why no material first-party path remains: these paths define or enforce execution constraints but do not reconstruct an identity/ultimate-policy issue → authoritative decision → returned policy governing subsequent operation.

## Distributed OSS parent arrangement

The SouthBridgeAI repository and contributors are an adjacent development organization. Their release/maintenance decisions are not imported into a running hank. A hank author/operator supplies configuration and may intervene programmatically, but no S3/S4/S5 parent mode is published without the corresponding function-specific parent feedback loop.

## Self-hosted and non-human modes

Hankweave is headless-first and intended for programmatic/hermetic operation. It can be managed by other systems or agents through its socket/event protocol. Generic external programmability does not create `C` or `(P)`: the composing controller must be part of a separately declared system boundary and establish the VSM function being claimed.

## Recursion

The assessment fixes recursion at one running hank, not at the external coding-agent harness and not at the SouthBridgeAI development organization. A sequence of codons is treated as one long-horizon operating program unless evidence establishes distinct interacting S1 units. Specific hanks that construct richer organizations are separate systems-in-focus.

## Variety and escalation

Hankweave absorbs long-horizon operational variety through deterministic rigs, codon/context boundaries, budgets, retries, checkpoints, rollback, event journaling and optional sentinels. Fatal/retryable failures and budget trips can change runtime state or stop execution, while external clients can resume/retry/rollback according to the exposed protocol. These are substantial reliability mechanisms without implying autonomous S3/S3* ownership.

## Evidence gaps

The negative S3* finding is sensitive to future sentinel integration: if a standard first-party mode gives a separate sentinel actor complementary evidence plus a direct findings-to-current-control return path, reassessment is warranted. Likewise, a future bundled adaptive controller that monitors external harness/runtime change and autonomously promotes generated shims into subsequent runs could establish S4 at the runtime boundary.