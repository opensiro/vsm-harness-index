# Harness Evolver — frozen `S` fixture packet

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#292`

## Supersession note

This packet supersedes the pre-review packet that used canonical baseline snapshot `opensiro/vsm-harness-index@79a40596e37f9e343b4e1254dad54f9ade362de8` and therefore treated `S3*=A` as eligible for experimental `S` screening.

Before any Harness Evolver independent review began, canonical same-ref correction [`#298`](https://github.com/opensiro/vsm-harness-index/pull/298) established that the pinned runtime exposes an S3*-specific constructor path but does not operationally close arbitrary Critic-added evaluator definitions into later scoring. The canonical state is therefore `S3*=C` under current Methodology.

The earlier packet remains preserved in Git history, but it MUST NOT be used for a new review. Both independent reviewers must use this refrozen packet and the revisions below.

## Frozen revisions

- Experimental Methodology: `opensiro/vsm-harness-skills@947b42e77551ed1a86456f8a812c72a96a36506a`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Canonical Index baseline snapshot: `opensiro/vsm-harness-index@96f7c3bc1fb72b27c2118db1f4953c5b1f75a868`
  - `assessments/harness-evolver.md`
- Target repository: `raphaelchristi/harness-evolver@87fa7612358acccb01d34abf72426a7e47329642`

Later repository or assessment changes are not inputs to this fixture run.

## Released baseline

```text
S1  A
S2  —
S3  —
S3* C
S4  —
S5  —
```

Under the pinned experimental Methodology, only released `A` functions may advance to `candidate-witness`. Therefore **S1 is the only eligible function** in this fixture.

- S3* is an ineligible constructor control: experimental `S` cannot bypass the released `A` prerequisite.
- S2/S3/S4/S5 are ineligible under their released `—` baselines.
- If evidence challenges any frozen released baseline, record a separate canonical reassessment question rather than changing the baseline inside this experiment.

## Declared boundary

Use the same system-in-focus and recursion as the corrected canonical assessment:

- Harness Evolver's first-party evolution organization;
- shipped `/harness:evolve` procedure and supplied proposer/evaluator/Critic/Architect/Consolidator roles;
- selection/gating machinery, archive/state and first-party mutation/evaluation tools;
- target harness/codebase, LangSmith service, external model/provider/coding-agent host and Git worktrees remain environment/dependencies as declared by the canonical assessment;
- **target/generated candidate harnesses are separate systems-in-focus** and their changing organizational repertoire is not credited back to Harness Evolver.

The primary transformation at this boundary is harness evolution itself.

## Frozen experimental question

For eligible S1, determine whether primary evidence establishes one complete transition in which:

1. Harness Evolver's existing **own operational repertoire for harness evolution** became materially insufficient for in-domain variety;
2. Harness Evolver itself recognized that insufficiency through its first-party organization;
3. it endogenously reconstructed or extended that own operational repertoire rather than merely mutating a target harness or selecting/exercising a pre-authored option;
4. the reconstruction occurred within legitimate authority;
5. the reconstructed repertoire became integrated into later Harness Evolver operation;
6. the new repertoire absorbed the target variety that the prior Harness Evolver repertoire could not absorb; and
7. no external constructor supplied the missing organizational logic.

The experiment must keep one system-in-focus throughout this causal chain.

## Required baseline / eligibility screen

| Function | Released baseline | Eligibility / fixture question |
| --- | --- | --- |
| S1 | `A` | **Eligible.** Is there a concrete disturbance for which Harness Evolver reconstructs its own evolution-operation process/tooling/local organization, integrates that reconstruction, and later closes the same variety through it? |
| S2 | `—` | Ineligible. Parallel proposer waves, worktree isolation, sequencing or shared archive/state do not establish S2 or experimental S2. |
| S3 | `—` | Ineligible. Candidate selection, gates and iteration-stop logic are not promoted to S3 by this experiment. |
| S3* | `C` | Ineligible under `SPEC.md §3.1`. The Critic plus `add_evaluator.py` is retained as a constructor/closure control, not an experimental `S3*` candidate. |
| S4 | `—` | Ineligible. Trace/archive/memory learning does not become experimental S4 without first establishing released `A` through normal reassessment. |
| S5 | `—` | Ineligible under the released function/ownership prerequisite. |

For S1 record exactly one:

- `candidate-witness`
- `no-candidate-witness`
- `insufficient-evidence`

A `candidate-witness` must then receive the complete candidate `S` test from the pinned Skills `SPEC.md`.

For S2/S3/S3*/S4/S5 record only the frozen baseline, prerequisite failure and any separate canonical-reassessment question exposed by primary evidence. Do not issue an experimental `candidate-witness` for those rows.

## S1 boundary test — self-modification versus separate system

Harness Evolver is designed to mutate and select changes to a target harness. That is strong autonomous operational evidence for its released S1, but it is not by itself evidence that **Harness Evolver's own S1 repertoire** has reconstructed.

A qualifying S1 transition must have this shape:

```text
Harness Evolver's existing evolution-operation repertoire
cannot absorb a material in-domain disturbance
→ Harness Evolver recognizes its own repertoire insufficiency
→ Harness Evolver constructs a materially new/altered evolution process,
  tool, or local operating organization
→ the reconstruction becomes part of later Harness Evolver operation
→ later Harness Evolver operation uses it to absorb the original variety
```

By contrast, this remains ordinary operation over a separate system-in-focus:

```text
Harness Evolver operation
→ proposer diagnoses target failure
→ proposer changes target harness code
→ target harness gains new capability/organization
→ winner is selected/merged
```

Even sophisticated target self-modification, target architecture changes, new target tools/agents, or recursive organization inside the generated target do not transfer to Harness Evolver's own `S` witness.

## S3* constructor control — not eligible for `S`

The corrected canonical assessment records `S3*=C`:

```text
ordinary evaluator regime becomes suspect
→ independent Critic judges gaming/blind spots
→ Critic selects/builds corrective evaluator configuration
→ add_evaluator.py persists evaluator name/definition
→ [missing shipped edge: arbitrary definition is not executed by run_eval.py]
```

Reviewers may inspect this path only to preserve the released boundary and to detect a possible future canonical reassessment issue. It MUST NOT advance to experimental `S3*` in this frozen run because released `A` closure is not established.

In particular:

- `add_evaluator.py` writing `code_evaluators` is a constructor path, not closed audit feedback;
- `run_eval.py::load_evaluators()` at the target revision does not load arbitrary stored code-evaluator definitions;
- the separate `harness-evaluator` role handles `correctness` / `conciseness`, not arbitrary Critic-added code checks;
- `S` cannot repair or bypass that released ownership/closure classification.

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

Do not count any of the following by itself as S1 `S`:

- mutating a generated candidate/target harness;
- merging the winning target-harness worktree;
- changing the target harness architecture;
- adding a target tool, prompt, workflow, specialist or agent;
- choosing another pre-authored proposer lens/mode/operator;
- ordinary retry/regression tracking/test generation;
- archive/memory accumulation;
- generic Write/Edit/Bash authority;
- a maintainer/developer changing Harness Evolver outside the assessed operating loop;
- a model/provider or external coding host supplying the material missing organizational logic outside the first-party role contract.

The question is endogenous reconstruction of **Harness Evolver's own operational repertoire with later closure**.

## Strong recursive witness — separate test

Evaluate separately whether Harness Evolver creates and integrates a new viable recursion **inside the Harness Evolver organization** because its prior organization cannot absorb material in-domain variety.

Target/generated candidate harnesses are separate systems-in-focus, so their internal viability does not establish recursive self-organization of Harness Evolver.

A positive strong witness must show:

```text
prior Harness Evolver organization cannot absorb material in-domain variety
→ it recognizes organizational insufficiency
→ defines a new bounded internal operational purpose/domain
→ creates/reorganizes an internal operational unit for that domain
→ establishes enough local coordination/current control/audit/adaptation/policy
→ grants bounded autonomy
→ integrates parent/child authority without duplicate ultimate authority
→ the new recursion absorbs the previously unresolved variety
```

Literal S1–S5 component names are not required; functional viability is.

Record:

```text
strong_recursive_witness: yes | no | inconclusive
```

## Required decision record

Each independent reviewer must produce:

- reviewer/context declaration;
- frozen revision and boundary confirmation;
- complete S1/S2/S3/S3*/S4/S5 baseline/eligibility table;
- complete candidate screen for **S1 only**;
- for an S1 `candidate-witness`, every complete `SPEC.md` candidate-test field;
- explicit same-system boundary analysis distinguishing Harness Evolver from the evolved target;
- S3* prerequisite/control note confirming that `C` is not eligible for experimental `S`;
- primary evidence links and caveats;
- any separate canonical reassessment question;
- strongest alternative released-Methodology interpretation;
- `strong_recursive_witness`;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`

A positive overall finding must name the eligible S1 witness that carries it. Evidence from an ineligible function cannot substitute for that witness.

## Independence and publication boundary

Two independent reviews are required.

- Both reviewers receive this packet and the same frozen revisions.
- Review 2 must not see Review 1 reasoning or finding before completing its own record.
- Do not publish Review 1 in a discoverable GitHub artifact before Review 2 completes.
- After both judgments exist, publish `review-1.md`, `review-2.md` and `synthesis.md` together.
- Do not modify canonical assessment states, catalog, signatures, TLDR, rankings, metrics or released Methodology from this experiment.
