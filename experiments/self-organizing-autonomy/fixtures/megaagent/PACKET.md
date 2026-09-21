# MegaAgent — frozen `S` strong-recursive candidate packet

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#306`

## Frozen revisions

- Experimental Methodology: `opensiro/vsm-harness-skills@947b42e77551ed1a86456f8a812c72a96a36506a`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Canonical Index baseline snapshot: `opensiro/vsm-harness-index@d53c54b2b8164c0d323c0bf10578417eab38af74`
  - `assessments/megaagent.md`
- Target repository: `Xtra-Computing/MegaAgent@c2e45ad99d8166db82b8f8516d2bcd722ad8540a`

Later repository or assessment changes are not inputs to this fixture run.

## Corpus role

MegaAgent is the real-system **strong recursive candidate**.

The target is deliberately difficult to classify because the standard runtime already:

- generates a task-specific initial organization;
- instantiates a CEO plus operational workers;
- runs each agent through its own model/tool/message loop;
- lets agents recursively recruit subordinates with `add_agent`;
- provides inter-agent communication and shared-artifact collision feedback;
- provides project-wide CEO current control;
- demonstrates a distinct testing/audit worker in the bundled run.

None of those properties establishes a new viable recursion by itself. The fixture asks whether primary evidence closes the full causal transition required by the experimental protocol.

## Released baseline

```text
S1  A
S2  A
S3  A
S3* A
S4  —
S5  —
```

Under the pinned experimental Methodology:

- S1/S2/S3/S3* satisfy the released-`A` prerequisite and must each be screened independently;
- S4/S5 are ineligible under their released `—` baselines;
- a positive witness for one eligible function does not transfer to another;
- a per-function positive witness remains separate from the strong recursive witness.

## Declared boundary

Use the same system-in-focus as the frozen canonical assessment:

- one first-party MegaAgent project organization at the target revision;
- root-generated CEO and worker-agent loops;
- recursively created subordinate agents through the same first-party `Agent` runtime;
- first-party `add_agent`, `talk`, task/TODO/status, shared file, execution and termination tools;
- shared Git-backed workspace and collision handling;
- root organization-wide idle/TODO monitor and final CEO completion/rework loop;
- bundled default-run logs as observed evidence of the shipped standard path.

Keep external LLM APIs, external benchmark/evaluation activity, repository-development workflows and the contents of the separate `files` submodule outside organizational ownership except where the first-party runtime operates on the mounted workspace.

The declared recursion for the released assessment is **one MegaAgent project organization**. Individual task-owning agents are S1 units. A recursively recruited subordinate is not automatically a lower viable system.

## Frozen experimental question

For each eligible function, determine whether primary evidence establishes a concrete transition in which:

1. the existing function-specific organizational/regulatory repertoire became materially insufficient for in-domain variety;
2. MegaAgent itself recognized that insufficiency;
3. MegaAgent endogenously reconstructed or extended the relevant repertoire rather than merely instantiating or selecting a pre-authored mechanism;
4. the reconstruction occurred within legitimate authority;
5. the reconstructed repertoire was integrated into subsequent operation;
6. later operation used it to absorb the original variety that the prior repertoire could not absorb; and
7. no external constructor supplied the missing organizational logic.

Then evaluate the stronger recursive question separately.

## Required per-function screen

| Function | Released baseline | Function-specific question |
| --- | --- | --- |
| S1 | `A` | Does a concrete operational disturbance cause MegaAgent to construct a materially new operational process/tool/local organization, integrate it and later use it, rather than simply recruiting another worker through the existing `add_agent` repertoire? |
| S2 | `A` | Does an inter-S1 interference/dependency disturbance exceed the existing `talk` plus Git/version-collision repertoire and cause endogenous reconstruction of the coordination regime with later closure? |
| S3 | `A` | Does a project-wide current-control disturbance exceed the existing CEO/message/global-monitor/reassignment/recruitment repertoire and cause endogenous reconstruction of current-control organization with later closure? |
| S3* | `A` | Does an audit disturbance exceed the existing distinct tester/inspection/testing/rework repertoire and cause endogenous reconstruction of complementary audit while preserving independence and corrective closure? |
| S4 | `—` | Ineligible. Record only the released prerequisite failure and any separate canonical reassessment question. |
| S5 | `—` | Ineligible. Record only the released prerequisite failure and any separate canonical reassessment question. |

For each eligible row record exactly one:

- `candidate-witness`
- `no-candidate-witness`
- `insufficient-evidence`

A `candidate-witness` must receive the complete candidate `S` test from the pinned Skills `SPEC.md`.

## Existing repertoire versus reconstruction

The following capabilities are part of the already available standard repertoire and therefore do not establish `S` merely by being exercised:

- root-time generation of the initial organization from `config.initial_prompt`;
- CEO delegation to initial workers;
- model-driven local tool choice;
- inter-agent `talk` messages;
- TODO/status updates;
- shared-file read/write/execution;
- Git lock/base-hash/collision feedback;
- CEO priority/reassignment messages;
- global idle/TODO monitoring and wake-up;
- final CEO proofreading/testing/rework instruction;
- `add_agent` creation of another `Agent` using model-supplied name/description/initial prompt;
- recursively calling the same subordinate-construction mechanism at greater hierarchy depth.

A qualifying experimental witness needs evidence that those mechanisms themselves cease to provide requisite variety and that MegaAgent constructs a materially new function-specific repertoire in response.

## Strong recursive witness — primary fixture question

The strongest witness requires one causal chain at the declared parent boundary:

```text
material in-domain variety exceeds the current MegaAgent organization
→ MegaAgent recognizes organizational insufficiency
→ MegaAgent defines a new bounded operational purpose/domain for the unresolved variety
→ MegaAgent creates or reorganizes a lower operational unit for that domain
→ the lower unit obtains enough local coordination/current control/complementary audit/adaptation/policy relations for its boundary
→ the lower unit receives bounded autonomy
→ parent/child authority and escalation are integrated without duplicate ultimate authority
→ the new recursion absorbs the variety the prior organization could not
```

The review must reconstruct or reject every edge separately.

### Lower-recursion evidence requirements

Do not infer local viability from parent-level functions. A candidate lower unit needs evidence at its own declared boundary for the organizational relations required by the strong-recursive protocol.

In particular:

- a subordinate's own task loop can support local S1, but does not prove local S2/S3/S3*/S4/S5;
- a parent CEO's whole-project S3 cannot be silently credited as the child's local current control;
- parent/global Git collision machinery is not automatically the child's own S2 ownership;
- a sibling tester does not automatically become the child's independent S3*;
- generated role text or a supervisor line does not establish local S5;
- model-driven recruitment does not by itself define a legitimate lower-recursion policy boundary;
- hierarchy depth, names such as CEO/manager/tester, or nested `Agent` objects are not viability evidence.

If the lower unit depends on parent-level regulatory functions, record that relationship explicitly and determine whether it still satisfies the strong-recursive test rather than silently duplicating parent authority.

## Transition evidence versus boot-time construction

MegaAgent generates an organization at startup. That is not automatically an `S` transition because the experimental distinction concerns reconstruction when an **existing** repertoire proves insufficient during in-domain operation.

Reviewers must distinguish:

### Initial construction

```text
user project goal
→ pre-authored organization-generation mechanism
→ initial roster/CEO/workers
→ ordinary project operation
```

from a candidate reconstruction transition:

```text
already-operating organization
→ concrete unresolved variety / failure / capacity gap
→ endogenous recognition that current organization/repertoire is insufficient
→ materially new organizational/repertoire construction
→ integration
→ later closure of that same unresolved variety
```

Runtime `add_agent` after startup is therefore important evidence to inspect, but still only a candidate transition until insufficiency, new viable relations, integration and post-change absorption are all demonstrated.

## Primary evidence starting set

Reviewers may inspect any primary artifact at the pinned target revision needed to answer the frozen questions. Start with:

- `main.py` — initial organization generation and global completion/rework loop;
- `agent.py` — per-agent loop, subordinate registry, recursive `add_agent`, `talk` and task/status behavior;
- `llm.py` — first-party tool contract exposed to agents;
- `utils.py` — shared Git-backed mutation/collision path;
- `config.py` — initial organization prompt, CEO identity and runtime bounds;
- `logs/Bob.log` — observed CEO allocation/current-control behavior;
- `logs/Grace.log` — observed testing/audit and dependency behavior;
- every bundled runtime log containing observed `add_agent` / `Add agent:` events, especially recruitment after initial organization;
- any corresponding messages/status/artifacts showing the trigger for recruitment and what the recruited subtree later accomplished.

Repository history may be inspected for immutable provenance when needed. Maintainer development outside the assessed runtime is not itself an operating witness.

## Important negative tests

None of the following establishes experimental `S` by itself:

- generating the initial roster;
- adding one subordinate through the existing `add_agent` tool;
- creating a deeper agent tree;
- writing a new role description or prompt;
- task decomposition/delegation without the mapped function-specific disturbance;
- ordinary `talk` coordination;
- ordinary Git collision recovery;
- CEO reassignment/reprioritization using existing authority;
- testing/re-testing through the existing audit arrangement;
- more agents, more messages or more hierarchy depth;
- a repository maintainer adding a new mechanism between runs.

Likewise, a generated subtree that performs useful work but lacks evidence of enough local viable-system relations is not a strong recursive witness.

## Required decision record

Each independent reviewer must produce:

- reviewer/context declaration;
- frozen revisions and boundary confirmation;
- complete six-function baseline/eligibility table;
- S1/S2/S3/S3* screening results;
- complete candidate-test fields for every `candidate-witness`;
- S4/S5 prerequisite notes and any separate canonical reassessment questions;
- explicit inventory of observed runtime subordinate creation beyond the initial roster;
- for the strongest subordinate/reorganization event: trigger, recognized insufficiency, bounded purpose/domain, created/reorganized unit, local regulatory relations, authority/autonomy, parent integration, post-change effect and external-constructor check;
- evidence that claimed lower-recursion functions are local rather than borrowed from parent/global mechanisms;
- primary evidence, counter-evidence and missing evidence;
- strongest alternative interpretation under released Profile/Methodology;
- `strong_recursive_witness: yes | no | inconclusive`;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`.

A positive strong-recursive result must name the concrete runtime transition that carries it. Capability-only evidence is insufficient.

## Independence and publication boundary

Two independent reviews are required.

- Both reviewers receive this packet and the same frozen revisions.
- Review 2 must not see Review 1 reasoning/finding before completing its own record.
- Review 1 must not be published as a discoverable GitHub review artifact before Review 2 completes.
- After both judgments exist, publish `review-1.md`, `review-2.md` and `synthesis.md` together.
- Do not modify canonical MegaAgent states, catalog, signatures, TLDR, rankings, metrics or released Methodology from this experiment.
