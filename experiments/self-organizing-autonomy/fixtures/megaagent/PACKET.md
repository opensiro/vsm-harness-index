# MegaAgent — frozen `S` strong-recursive candidate packet

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#306`

## Frozen revisions

- Experimental Methodology: `opensiro/vsm-harness-skills@947b42e77551ed1a86456f8a812c72a96a36506a`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Canonical Index baseline snapshot: `opensiro/vsm-harness-index@0404f35c88b52443cd0d61e3ab1eb48919ff5b1c`
  - `assessments/megaagent.md`
- Target repository: `Xtra-Computing/MegaAgent@c2e45ad99d8166db82b8f8516d2bcd722ad8540a`

Later repository, assessment, Profile, or experimental-Methodology changes are not inputs to this fixture run.

## Corpus role

MegaAgent is the **strong recursive candidate** for the older pinned experimental protocol.

The fixture tests two distinct questions that MUST remain separate:

1. whether any released-`A` function has a complete candidate `S` reconstruction witness; and
2. whether MegaAgent demonstrates the stronger recursive reorganization chain defined by the pinned `SPEC.md`.

Recursive agent creation, hierarchy depth, or dynamic role generation are candidate mechanisms only. They are not findings.

## Frozen canonical baseline

The canonical assessment at the pinned Index snapshot records:

```text
S1   A
S2   A
S3   A
S3*  A
S4   —
S5   —
```

Eligibility under the pinned experimental protocol is therefore:

| Function | Released state | `S` screening eligibility |
| --- | --- | --- |
| S1 | `A` | eligible |
| S2 | `A` | eligible |
| S3 | `A` | eligible |
| S3* | `A` | eligible |
| S4 | `—` | ineligible — function/ownership prerequisite absent |
| S5 | `—` | ineligible — function/ownership prerequisite absent |

Do not use the experiment to promote S4 or S5, or to repair a canonical baseline. Any evidence that the frozen assessment itself is wrong belongs in a separate reassessment transaction.

## Declared system boundary

Use exactly the frozen canonical system-in-focus:

- one first-party MegaAgent project organization;
- root organization generation and CEO bootstrap;
- first-party `Agent`/`Memory` model-tool loops;
- recursive subordinate creation through `add_agent`;
- inter-agent messaging and task/status state;
- shared Git-backed workspace and collision feedback;
- global idle/TODO monitoring;
- first-party execution/testing surfaces and completion/rework loop.

Keep outside ownership:

- external LLM APIs and their internal reasoning systems;
- benchmark/evaluation infrastructure;
- repository-development activity;
- the contents of the external `files` submodule except where MegaAgent operates on the mounted workspace;
- any maintainer or external actor supplying new organizational logic.

The declared recursion is one MegaAgent project organization. Task-owning agents are operational S1 units. A nested worker is not silently treated as a new viable recursion merely because `add_agent` instantiated another `Agent` object.

## Frozen architecture facts

At the target revision:

- `main.py` asks the model to propose an initial task-specific roster, instantiates the CEO, creates initial workers as subordinates, starts project allocation, monitors all agent/TODO state, and returns apparent completion to the CEO for terminate-versus-reassign judgment;
- every `Agent` owns a queue, memory, model loop and tool surface;
- `add_agent` lets a running agent instantiate another first-party `Agent` with a generated name/description/prompt and a supervisor relation;
- `talk` returns peer messages into agent context;
- shared-file reads expose current artifact content plus Git base hash;
- writes are serialized/version-aware and collision/conflict evidence is returned to the calling agent;
- the bundled Bob/Grace traces demonstrate project allocation, readiness/defect feedback, testing and corrective reassignment on the standard path.

These establish the frozen released baseline. They do not by themselves establish endogenous reconstruction.

## Per-function screening requirement

Reviewers MUST independently screen all four eligible released-`A` functions.

For each of S1, S2, S3 and S3*, record exactly one:

```text
candidate-witness
no-candidate-witness
insufficient-evidence
```

A `candidate-witness` only advances that row to the complete candidate test. It is not itself a positive `S` finding.

### S1 screening

Released function:

> autonomously execute a bounded project contribution through a model-driven local task/tool loop and produce shared project outcomes.

Ask whether an existing S1 repertoire becomes materially insufficient for an in-domain disturbance and MegaAgent itself reconstructs the operational process/tooling/local organization so later S1 operation closes that variety through the changed repertoire.

Do not count by itself:

- ordinary tool choice;
- retry/recovery;
- adding a subordinate because a task is merely complex;
- selecting another generated role/prompt;
- ordinary content generation inside the existing agent loop.

### S2 screening

Released function:

> attenuate dependency/readiness mismatch and conflicting concurrent mutations among distinct parallel S1 units through peer feedback plus version-aware shared-workspace regulation.

Ask whether the existing coordination repertoire is shown materially insufficient for an in-domain inter-S1 disturbance and MegaAgent reconstructs the coordination relation itself, integrates it, and later attenuates that disturbance through the changed relation.

Do not count by itself:

- another `talk` message;
- another hash-aware retry;
- an ordinary merge-conflict response;
- adding more workers without changing the coordination regime.

### S3 screening

Released function:

> regulate the project-wide current portfolio of commitments, priorities, defects, readiness and completion/rework through the model-driven CEO plus supporting global monitor.

Ask whether current-control repertoire insufficiency leads MegaAgent itself to reconstruct resource-allocation/accountability/escalation organization, integrate it, and subsequently close present-time whole-system variety through the reconstructed control repertoire.

Do not count by itself:

- ordinary CEO reassignment;
- changing priorities;
- recruiting another worker within the existing management contract;
- another completion/rework cycle using the same control machinery.

### S3* screening

Released function:

> complementary operational-reality checking through a distinct testing worker whose contradictory findings return into CEO corrective control.

Ask whether the existing audit repertoire is materially insufficient and MegaAgent reconstructs audit strategy, evidence access, probes, sampling, or auditor composition while preserving complementary independence and corrective return.

Do not count by itself:

- running another existing test;
- ordinary tester reassignment;
- adding a reviewer whose role remains dependent on implementer claims;
- increasing reviewer count without reconstructing the audit relation.

## Complete candidate test for any advanced row

For every function screened `candidate-witness`, reconstruct every edge from the pinned `SPEC.md`:

```text
released A closure
→ material in-domain repertoire insufficiency
→ MegaAgent recognizes the insufficiency
→ MegaAgent endogenously reconstructs/extends the function-specific repertoire
→ legitimate authorization at the declared recursion
→ reconstructed repertoire is integrated
→ later operation closes the target variety through the changed repertoire
→ no external constructor supplied the material missing organizational logic
```

A failure or evidence gap at any required edge must remain visible.

## Strong recursive witness — separate diagnostic

Independently reconstruct or reject the complete strong-recursive chain:

```text
1. material in-domain variety exceeds the current organization
2. MegaAgent recognizes organizational insufficiency
3. MegaAgent defines a new bounded operational purpose/domain for unresolved variety
4. MegaAgent creates or reorganizes a lower operational unit for that domain
5. the lower unit gains enough local coordination, current control,
   complementary audit, adaptation and policy relations to remain viable
6. bounded autonomy is granted and parent/child authority is integrated
   without duplicate ultimate authority
7. the new recursion demonstrably absorbs variety the prior organization could not
```

Record only:

```text
strong_recursive_witness: yes | no | inconclusive
```

The following are insufficient shortcuts:

- `add_agent` exists;
- a worker recursively calls `add_agent`;
- hierarchy depth increases;
- a generated prompt calls an agent a manager/CEO/specialist;
- a subordinate has its own LLM/tool loop;
- the parent delegates a difficult subtask;
- the child has further children;
- more parallel capacity improves completion.

The lower organization must be functionally viable for a newly bounded delegated domain, not merely nested.

## Authority and recursion checks

A claimed recursive witness must identify:

- the new lower unit's bounded purpose;
- which operational work it owns;
- how inter-S1 coordination is closed locally;
- who regulates its present-time whole;
- whether complementary operational-reality access exists;
- whether future/adaptation and identity/policy relations are sufficient for the delegated purpose under the pinned protocol's viability test;
- what autonomy is actually granted;
- how escalation returns to the parent;
- why parent and child do not both hold duplicate ultimate authority over the same recursion.

Do not infer these from component names.

## External-constructor test

For every claimed reconstruction, ask whether the material missing organizational logic came from:

- a maintainer/developer;
- an external model/runtime outside the declared system boundary;
- the user/parent as a design instruction;
- a pre-authored organizational template already present at T0;
- benchmark/repository-development activity outside operating distribution.

If an external actor supplies the missing logic, the positive `S` edge fails even if MegaAgent executes the supplied design autonomously.

## Primary evidence starting set

Reviewers may inspect any primary artifact at the frozen target revision. Start with:

- `README.md` — documented latest root runtime and dynamic organization behavior;
- `main.py` — initial organization generation, CEO bootstrap, global monitor and completion return;
- `agent.py` — independent agent loops, subordinate creation, messaging, tool feedback and memory;
- `llm.py` — tool contract including `add_agent`, `talk`, file operations, execution and termination;
- `utils.py` — shared Git workspace/version/collision regulation;
- `config.py` — generated-organization prompt and bounded agent/runtime constraints;
- `logs/Bob.log` — observed CEO assignment/reallocation/corrective control;
- `logs/Grace.log` — observed readiness/dependency feedback and complementary testing path.

Repository history may be inspected only to establish provenance or an actual operating transition at the frozen boundary. Maintainer development is not itself an operating witness.

## Required independent review record

Each independent reviewer must produce:

- reviewer/context declaration;
- confirmation of all frozen revisions and boundary;
- six-function baseline/eligibility table;
- S1 screening result;
- S2 screening result;
- S3 screening result;
- S3* screening result;
- S4/S5 prerequisite exclusion confirmation;
- complete candidate test for every `candidate-witness` row;
- primary evidence, counter-evidence and missing evidence;
- strongest alternative interpretation under released Profile/Methodology;
- `strong_recursive_witness` with all seven edges explicitly addressed;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`.

If inspection exposes a possible canonical-assessment error, record it as a separate reassessment question without changing this frozen baseline.

## Independence and publication boundary

Two independent reviews are required.

- Both reviewers receive this packet and identical frozen inputs.
- Review 2 must not see Review 1 reasoning/finding before completing its own record.
- Neither review should be published to a discoverable GitHub artifact before both judgments exist.
- After both exist, publish both review records and synthesis together.
- Preserve disagreements; do not force consensus by rewriting a review.

## Non-goals

This packet does not:

- assert that MegaAgent supports experimental `S`;
- assert that recursive workers are viable recursions;
- change canonical MegaAgent states;
- change catalog/signatures/TLDR/rankings/metrics/Full-A;
- redefine VSM recursion or viability;
- import later clarified `S` semantics into the older pinned protocol.
