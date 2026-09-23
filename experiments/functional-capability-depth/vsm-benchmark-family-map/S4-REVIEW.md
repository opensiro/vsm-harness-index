# Follow-up semantic review: S4 direct benchmark candidates

Status: experimental, non-normative.

Issue: #397

Reviewed Profile: `vsm-harness-profile` `0.2.4`.

`map.json` remains the machine-readable source of truth. This note records the function-first argument for adding direct S4 benchmark families.

## Decision

The review promotes three S4 families/modes to `direct` at their benchmark-defined adaptation boundaries:

```text
A-Evolve harness-evolution protocol                 direct
SkillEvolBench                                      direct
EvoHarnessBench self-evolving adaptation mode       direct
```

`SkillLearnBench`, `FutureSim`, and `ClawArena` remain `proxy` for S4.

`AdaPlanBench` and `CostBench` remain `unsuitable` for direct S4 measurement because they primarily exercise current-task replanning.

## S4 gate applied

The Profile requires more than learning, memory, prompt editing or reaction to an external event. A direct S4 benchmark must expose:

1. external/future-relevant distinctions;
2. interpretation of those distinctions into adaptation options;
3. a persistent change to capability;
4. return of that change into later operation;
5. prospective/deployment evidence separating durable adaptation from current-episode repair.

The three direct families satisfy this at their own declared benchmark boundaries. None of those semantic decisions transfers S4 ownership into a canonical product merely because that product/model is used as a task solver.

## A-Evolve — direct

Reviewed implementation:

`A-EVO-Lab/a-evolve@96ed93ba7ee0b9519fc55c963afb47a1975eb1ae` on `release/harness-evolution`.

The official implementation defines harness self-evolution as updating an editable external harness — prompts, skills, memories and tools — from execution evidence.

Its runners:

```text
copy initial harness
    ↓
solve external task stream
    ↓
collect execution evidence
    ↓
evolver proposes persistent harness changes
    ↓
update harness between batches
    ↓
run later tasks using evolved workspace
```

The paper/implementation deliberately separates:

- `harness-updating`: whether an evolver can produce useful persistent updates from evidence;
- `harness-benefit`: whether a later task-solving agent can exploit the evolved harness.

Exp0 fixes the task-solving agent and varies the evolver; Exp1 fixes the evolver and varies the agent. The train/test route further separates adaptation from later use.

That closes the S4 structure at the benchmark boundary: environmental/operational evidence is interpreted into an adaptation option, that option changes persistent capability, and later operation tests whether the change matters.

### Boundary caution

A-Evolve supplies the adaptation organization. If it runs a canonical harness/model as the task solver, the result is not automatically evidence for that canonical harness's own S4 path.

## SkillEvolBench — direct

Reviewed implementation:

`AIoT-MLSys-Lab/SkillEvolBench@9e3daa339987c3cfa624121e1be442593a53d43c`.

The benchmark contains 180 tasks across six real-world agent environments. Within each latent procedural family:

- T1–T3 are acquisition tasks;
- execution trajectories and verifier feedback feed a separate Skill Author;
- the Skill Author induces or revises a persistent skill library;
- the learned capability is frozen;
- T4–T6 test future transfer under context shift, adversarial shortcuts and skill composition.

Canonical dynamic baselines invoke `SkillAuthor.propose` after every learning trial; the benchmark also compares against no-skill and raw-trajectory controls. This directly distinguishes persistent procedural adaptation from mere episodic trace reuse.

The repository contains an additional lifecycle maintainer that can retire/quarantine/narrow skills after evaluation, with effects applying only to future environments. That component is useful corroborating architecture, but the canonical benchmark ladder currently defers full-lifecycle baselines; the direct classification does **not** depend on that optional component.

### Boundary caution

SkillEvolBench can use Codex CLI, Claude Code, Gemini CLI and other task-solving agents. Its Skill Author and adaptation protocol remain benchmark-hosted. Running a CLI inside the benchmark therefore does not make the CLI's canonical S4 path measured.

## EvoHarnessBench self-evolving adaptation — direct

Primary paper/project evidence:

- arXiv `2609.04280`, v2 dated 2026-09-10;
- project page `https://mas-orchestra.salesforceresearch.ai/evoharness/`;
- public dataset artifacts under the authors' Hugging Face collection.

No unambiguous official GitHub implementation repository was recovered during this review. Do not attach one of the unrelated repositories named `evoharness` by string similarity.

The benchmark places non-stationarity in an externally evolving harness of tools, skills and specialist agents.

Two settings must remain separate:

### Deployment-only evaluation

The agent receives changed harness capabilities but does not perform persistent inner adaptation. This setting measures robustness/retention under harness change and is **not** direct S4 by itself.

### Self-evolving adaptation evaluation

The agent can update persistent adaptation state from accumulated experience and carry those memories/skills/prompts across subsequent harness versions. Held-out evaluation then tests adaptation/retention as the environment/harness continues to change.

Only this self-evolving mode is mapped `direct` for S4. It establishes the necessary inner loop from external change and operational experience into persistent capability that affects later operation.

## SkillLearnBench — proxy

Reviewed implementation:

`cxcscmu/SkillLearnBench@a0da045a8bf64b8a8ff20730c4d6ef10dc4e2c5b`.

SkillLearnBench evaluates continual-learning methods that generate/refine skills for real tasks. Its self-feedback and teacher-feedback baselines are strongly S4-relevant because execution failure and external guidance can revise reusable skill artifacts.

It remains `proxy` at the family level because the core feedback loop commonly improves/retries the same task family and does not isolate frozen prospective deployment as cleanly as SkillEvolBench. A future mode-specific review could promote a stricter transfer protocol if primary evidence supports it.

## Existing proxies remain unchanged

### FutureSim

FutureSim directly exercises chronological external sensing and belief/forecast revision, but its closed loop is a forecast state. It does not require a persistent organizational capability change returning to later operation.

### ClawArena

ClawArena exercises staged environmental evidence and dynamic belief revision. Belief revision alone is not the complete S4 adaptation loop.

## Canonical-system linkage

Current Index assessments already establish S4 through multiple ownership arrangements, including representative examples:

- `headcount` — `A`;
- `henterprise` — `A`;
- `kadath` — `A`;
- `omniscientist` — `A`;
- `super-agent` — `A`;
- `bossconsole` — `A(P)`;
- `exo` — `A(P)`;
- `agentyou` — `C`.

The direct-family review does not change those canonical states.

No reviewed observation in this pass demonstrates that A-Evolve, SkillEvolBench or EvoHarnessBench exercised one of those canonical systems' **own** first-party S4 implementation. The current canonical direct-S4 registry therefore remains empty.

## Resulting coverage statement

```text
reviewed direct S4 benchmark families/modes: 3
canonical native/adapter-preserved direct-S4 observations: 0
```

The semantic S4 benchmark gap is closed, while the canonical linkage gap remains open.

## Primary sources

- Profile: https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md
- A-Evolve implementation: https://github.com/A-EVO-Lab/a-evolve/tree/96ed93ba7ee0b9519fc55c963afb47a1975eb1ae
- A-Evolve paper: https://arxiv.org/abs/2605.30621
- SkillEvolBench implementation: https://github.com/AIoT-MLSys-Lab/SkillEvolBench/tree/9e3daa339987c3cfa624121e1be442593a53d43c
- SkillEvolBench paper: https://arxiv.org/abs/2605.24117
- EvoHarnessBench paper: https://arxiv.org/abs/2609.04280
- EvoHarnessBench project: https://mas-orchestra.salesforceresearch.ai/evoharness/
- SkillLearnBench implementation: https://github.com/cxcscmu/SkillLearnBench/tree/a0da045a8bf64b8a8ff20730c4d6ef10dc4e2c5b
- SkillLearnBench paper: https://arxiv.org/abs/2604.20087
