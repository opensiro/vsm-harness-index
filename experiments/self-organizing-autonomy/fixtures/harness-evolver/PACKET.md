# Harness Evolver — frozen `S` fixture packet

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#292`

## Frozen revisions

- Experimental Methodology: `opensiro/vsm-harness-skills@947b42e77551ed1a86456f8a812c72a96a36506a`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Canonical Index baseline snapshot: `opensiro/vsm-harness-index@79a40596e37f9e343b4e1254dad54f9ade362de8`
  - `assessments/harness-evolver.md`
- Target repository: `raphaelchristi/harness-evolver@87fa7612358acccb01d34abf72426a7e47329642`

Later repository changes are not inputs to this fixture run.

## Released baseline

```text
S1  A
S2  —
S3  —
S3* A
S4  —
S5  —
```

Only S1 and S3* satisfy the released-`A` prerequisite for candidate `S` testing. S2/S3/S4/S5 are ineligible under the frozen baseline. If experimental inspection suggests a baseline error, route it to normal canonical reassessment rather than changing the baseline inside this fixture.

## Declared boundary

Use the same system-in-focus and recursion as the canonical assessment:

- Harness Evolver's first-party evolution loop;
- supplied proposer/evaluator/critic/architect/consolidator/test-generation role contracts;
- selection/gating machinery, archive/state and mutation workflow;
- target harness/codebase, LangSmith, model/provider/coding-agent host and Git worktrees remain environment/dependencies as declared by the canonical assessment;
- **generated candidate harnesses are separate systems-in-focus** and their organizational changes are not credited back to Harness Evolver.

The primary transformation at this boundary is harness evolution itself.

## Frozen experimental question

For each eligible function, determine whether primary evidence establishes a transition in which:

1. the existing function-specific organizational/regulatory repertoire was materially insufficient for in-domain variety;
2. Harness Evolver itself recognized that insufficiency through the first-party organization;
3. it endogenously reconstructed or extended the relevant repertoire rather than merely selecting/exercising a pre-authored option;
4. the reconstruction occurred within legitimate authority;
5. the reconstructed repertoire was integrated into subsequent operation;
6. the new repertoire absorbed the target variety that the prior repertoire could not absorb; and
7. an external constructor did not supply the missing organizational logic.

S1 and S3* must be evaluated independently.

## Required baseline / eligibility screen

| Function | Released baseline | Eligibility / fixture question |
| --- | --- | --- |
| S1 | `A` | Eligible. Does Harness Evolver ever reconstruct **its own operational repertoire for harness evolution** after that repertoire proves insufficient, or do proposer code mutations only alter a separate target-harness system while Harness Evolver continues to use the same evolution machinery? |
| S2 | `—` | Ineligible under the released function/ownership prerequisite. Do not infer S2 from parallel proposer waves/worktree isolation. |
| S3 | `—` | Ineligible. Selection/gates/stop logic are not promoted to S3 by this experiment. |
| S3* | `A` | Eligible. When ordinary evaluator/benchmark scoring proves insufficient because of gaming, score inflation or a blind spot, does the independent Critic construct a materially new audit repertoire, integrate it, preserve complementary independence and close later evaluation/control through the reconstruction? |
| S4 | `—` | Ineligible. Archive/trace learning does not become experimental S4 without first establishing released A through normal reassessment. |
| S5 | `—` | Ineligible under the released function/ownership prerequisite. |

For eligible S1 and S3*, record exactly one:

- `candidate-witness`
- `no-candidate-witness`
- `insufficient-evidence`

A `candidate-witness` must then receive the complete candidate test from the pinned Skills `SPEC.md`.

## S1 boundary test — self-modification versus separate system

The repository exists to mutate and select changes to a target harness. That fact is not itself evidence that **Harness Evolver's own S1 repertoire** has reconstructed.

A positive S1 witness must keep one system-in-focus throughout the causal chain. It must show:

```text
Harness Evolver's existing evolution-operation repertoire is insufficient
→ first-party Harness Evolver recognizes that insufficiency
→ Harness Evolver changes its own operational process/tooling/local organization
→ the change becomes part of later Harness Evolver operation
→ that reconstructed Harness Evolver repertoire closes the original variety
```

By contrast:

```text
Harness Evolver operation
→ proposer changes target harness
→ target harness gains new capability/organization
```

remains a transformation of a separate system-in-focus unless primary evidence establishes otherwise.

## S3* boundary test — adaptive complementary audit

The canonical assessment already establishes an autonomous Critic as complementary audit. The experimental question starts **after** that released `A` baseline.

Potentially relevant evidence includes:

- Critic triggers for suspicious score jumps/evaluator-quality concerns;
- inspection of high-scoring outputs and evaluator blind spots;
- addition or implementation of stricter evaluators;
- arbitrary regex/code evaluator construction versus selection of pre-authored evaluator templates;
- persistence into `.evolver.json` or other authoritative evaluator configuration;
- re-use of the changed evaluator regime in subsequent candidate evaluation/selection;
- preservation of the Critic's independent challenge role after the change.

Do not call this `S3*=S` merely because `add_evaluator.py` can append an evaluator or because the Critic has Write/Bash authority. A qualifying witness needs a concrete disturbance and closure chain:

```text
ordinary audit repertoire misses/games a material defect
→ Critic recognizes the audit insufficiency
→ Critic constructs materially new audit logic
→ new audit logic is authorized and integrated
→ later evaluation/control actually uses it
→ original audit variety is closed
```

If the Critic only selects one of a fixed set of already-authored checks for a case the existing regime already anticipates, record that as use of existing repertoire, not reconstruction.

## Primary evidence starting set

Reviewers may inspect any primary artifact at the pinned target revision needed to answer the frozen question. Start with:

- `docs/ARCHITECTURE.md`
- `skills/evolve/SKILL.md`
- `agents/harness-proposer.md`
- `agents/harness-evaluator.md`
- `agents/harness-critic.md`
- `tools/add_evaluator.py`
- `tools/run_eval.py`
- `tools/read_results.py`
- `tools/regression_tracker.py`
- `tools/update_config.py`
- `tools/archive.py`
- `tools/log_iteration.py`
- `CLAUDE.md`
- `tests/test_tools.py`

Repository history may be inspected when needed for stable provenance, but repository-development history is not an operating witness by itself.

## Important negative tests

Do not count any of the following by itself as `S`:

- mutating a generated candidate/target harness;
- merging the winning target-harness worktree;
- choosing another pre-authored proposer lens;
- selecting a pre-authored evaluator template;
- adding an evaluator name with no implementation;
- ordinary regression tracking or test generation;
- generic Write/Bash authority;
- a maintainer/developer adding new evaluator code outside the operating loop;
- archive/memory accumulation;
- a model/provider or external coding host supplying the material missing organizational logic outside the first-party role contract.

## Strong recursive witness — separate test

Evaluate separately whether Harness Evolver creates and integrates a new **viable recursion** because its prior organization cannot absorb material in-domain variety.

Generated candidate harnesses are separate systems-in-focus, so their internal viability does not automatically establish recursive self-organization of Harness Evolver.

A positive strong witness must show a new lower recursion **inside the Harness Evolver organization** with enough local operational, coordination, current-control, complementary-audit, adaptation and policy relations for the delegated purpose, bounded autonomy, parent integration, and demonstrated absorption of the prior unresolved variety.

Record:

```text
strong_recursive_witness: yes | no | inconclusive
```

## Required decision record

Each independent reviewer must produce:

- reviewer/context declaration;
- frozen revision and boundary confirmation;
- complete S1/S2/S3/S3*/S4/S5 baseline/eligibility table;
- complete candidate screen for S1 and S3*;
- for every `candidate-witness`, the complete `SPEC.md` test fields;
- explicit same-system boundary analysis for S1;
- explicit complementary-independence analysis for S3*;
- primary evidence links and caveats;
- any separate canonical reassessment question;
- strongest alternative released-Methodology interpretation;
- `strong_recursive_witness`;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`

The overall finding must name the eligible function-specific witness, if any, that carries it.

## Independence and publication boundary

Two independent reviews are required.

- Both reviewers receive this packet and the same frozen revisions.
- Review 2 must not see Review 1 reasoning or finding before completing its own record.
- Do not publish Review 1 in a discoverable GitHub artifact before Review 2 completes.
- After both judgments exist, publish `review-1.md`, `review-2.md` and `synthesis.md` together.
- Do not modify canonical assessment states, catalog, signatures, TLDR, rankings, metrics or released Methodology from this experiment.
