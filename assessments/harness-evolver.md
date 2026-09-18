---
harness_id: harness-evolver
project_name: Harness Evolver
repository: https://github.com/raphaelchristi/harness-evolver
review_ref: 87fa7612358acccb01d34abf72426a7e47329642
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Harness Evolver

## Review boundary

- System in focus: Harness Evolver's first-party evolution loop, supplied agent-role prompts, selection/gating machinery, archive/state, and code-mutation workflow at pinned revision `87fa7612358acccb01d34abf72426a7e47329642`.
- Purpose and identity: autonomously improve an AI-agent harness by analyzing traces/results, generating alternative code changes, evaluating/selecting candidates, learning from the run, and repeating.
- Relevant environment: target harness/codebase, evaluation dataset and LangSmith experiment surface, external model/provider and coding-agent host, Git worktrees, and human-supplied objective/configuration.
- Standard-distribution boundary: repository skills, role prompts, Python tools and evolution state. Claude Code/Codex or other hosts, model providers and the target harness being evolved remain external actors/systems.
- First-party operating/deployment modes considered: plugin/skill-driven evolution with parallel proposers, evaluator, critic, architect, consolidator and test-generation roles.
- Recursion level: one harness-evolution organization. Generated candidate harnesses are separate systems-in-focus.
- Reviewed revision: `87fa7612358acccb01d34abf72426a7e47329642`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

The documented evolution loop performs preflight/baseline work, analyzes traces and results, launches proposer agents in isolated worktrees, evaluates candidates, compares and gates winners, merges the selected change, archives all candidates, updates regression guards and memory, then decides whether to continue. Proposers are autonomous model-driven actors with freedom to investigate, hypothesize, implement or abstain. A separate Critic role is expressly an anti-gaming auditor/fixer: it inspects high-scoring outputs and evaluator blind spots, detects score inflation and, when necessary, adds stricter evaluators that affect later iterations.

## Operational model

The primary transformation at this boundary is harness evolution itself. Proposer/evaluator activity, selection and accepted code mutation are stages and actors inside that operation. Parallel proposer worktrees isolate candidate edits, but the reviewed evidence does not establish a disturbance-specific peer coordination loop among proposer S1s. The Critic is different: it receives complementary access to outputs and score history specifically to challenge the ordinary evaluator path and can change the evaluation regime before subsequent evolution continues.

## Primary evidence

- [`docs/ARCHITECTURE.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/docs/ARCHITECTURE.md) — full evolution loop, role topology, gates, archive/memory and auto-triggered Critic/Architect paths.
- [`agents/harness-proposer.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/agents/harness-proposer.md) — model-driven proposer autonomy, isolated worktree mutation, self-abstention and candidate commits.
- [`agents/harness-critic.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/agents/harness-critic.md) — independent anti-gaming inspection, evaluator-blind-spot detection and mandatory corrective evaluator changes.

## S1 — Operations

- State: `A`.
- Function: execute the harness-evolution transformation: investigate failures, generate and implement candidate improvements, evaluate/select them and repeat.
- Disturbance / variety regulated: harness design uncertainty, benchmark failures, trace-derived failure modes and alternative implementation hypotheses.
- Decisive decision or feedback right: proposer agents choose their own diagnosis and code-change approach; the evolution run selects and installs accepted candidates.
- Decision owner: model-driven proposer/evolution actors operating under the first-party role/loop contract.
- Supporting / enforcement mechanisms: worktrees, evaluation tools, selection/constraint/efficiency gates, archive and regression bookkeeping.
- Closure path: accepted candidate changes replace current harness state and become the baseline/context for later iterations.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `—`.
- Distinct proposer agents can execute in parallel, but worktree isolation and staged waves primarily prevent candidate-state collision and organize search. The pinned distribution does not establish a concrete mutual-adjustment loop that observes destructive interference or oscillation among peer operational S1s and feeds a coordination response back into their later behaviour.
- Generic parallelism, shared archive/state and sequencing are therefore not promoted to S2.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- Selection, gates and iteration-stop logic regulate the primary evolution operation itself. No distinct first-party actor is shown holding a current whole-organization view plus discretionary authority over shared resources, commitments or priorities across an operational organization.
- The Architect/Consolidator names and deterministic gates are insufficient by themselves.
- Confidence: medium-high.

## S3* — Complementary audit

- State: `A`.
- Claim being audited: that high evaluator/benchmark scores correspond to substantive harness quality rather than evaluator gaming or score inflation.
- Ordinary reporting path: evaluator results and iteration scores used by the normal candidate-selection loop.
- Complementary access path: the separate Critic reads best-run outputs, evaluator behaviour and cross-iteration score history, explicitly checks substance, blind spots and suspicious jumps, and is triggered when evaluation quality is questionable.
- Independence boundary: Critic is a separate supplied agent role from proposer/evaluator and is tasked to challenge the evaluation regime rather than optimize the candidate directly.
- Decisive feedback right / owner: the Critic agent judges whether gaming exists and, when it does, is required to implement stricter evaluators.
- Closure path: new evaluator checks are written into the evolution configuration and constrain/re-score subsequent iterations, returning audit findings into later control of candidate acceptance.
- Basis / confidence: explicit + structural; high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Trace analysis, benchmark-driven self-improvement, archive mining and memory consolidation are internal optimization/learning around the target task distribution. The reviewed boundary does not establish an external-and-prospective environmental intelligence loop that models changing future conditions and returns adaptation options into present organizational capability.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- User goals, constraints, evaluator configuration and stop criteria bound the evolution search, but no runtime identity/ultimate-policy authority loop is supplied. Human configuration is not by itself parent-governed S5 closure.
- Confidence: high.

## Recursion

Candidate harnesses produced by the evolution loop may themselves contain viable organizations, but they are separate systems-in-focus and are not credited back to Harness Evolver.

## Variety and escalation

Parallel proposers amplify design variety; evaluation, constraint/efficiency gates and selection attenuate it. The Critic provides an exceptional corrective path for evaluator-gaming/quality disturbances rather than ordinary production scoring.

## Evidence gaps

The assessment does not infer behaviour from external Claude Code/Codex hosts beyond the actor responsibilities explicitly required by the first-party role/skill contracts.

## Admission conclusion

Canonical vector: `A — — A — —`.
