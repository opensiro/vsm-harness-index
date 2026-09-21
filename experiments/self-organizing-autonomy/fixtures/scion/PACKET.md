# Scion — frozen `S` fixture packet

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#287`

## Frozen revisions

- Experimental Methodology: `opensiro/vsm-harness-skills@d8588a1ffd73e9787ca826222c8ff7f31da3ec62`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Canonical Index baseline snapshot: `opensiro/vsm-harness-index@28e91dd2fb66675040bfdd9b6041c3bfbe15ed28`
  - `assessments/scion.md`
- Target repository: `annex-ai/scion@8a3e21f7d624e13eb5f14a18728c6f98172a5c55`

Later repository changes are not inputs to this fixture run.

## Released baseline

At the frozen canonical assessment:

```text
S1  A
S2  A
S3  A
S3* C
S4  A
S5  —
```

This vector is input only. The experiment does not modify it.

## Declared boundary

Use the same system-in-focus and operating boundary as the frozen canonical assessment:

- one first-party Scion assistant organization;
- ordinary interactive-agent operation;
- shipped `agent-team` mode and `handoff-to-agent` specialist cells;
- Heartbeat/current-work regulation;
- registered Observe → Reflect → Coach adaptation path and adaptation processor;
- first-party runtime/configuration needed to reach those paths;
- external model providers, MCP services, messaging platforms and user projects remain environment/dependencies;
- spawned specialists are not assumed to be complete viable recursions merely because they exist.

Do not enlarge the boundary to repository-development/CI activity or downstream compositions.

## Frozen experimental question

For each released positive VSM function, determine whether primary evidence establishes a transition in which:

1. the existing organizational/regulatory repertoire was materially insufficient for in-domain variety;
2. Scion itself recognized that insufficiency;
3. Scion endogenously reconstructed or extended the relevant repertoire rather than merely selecting or exercising a pre-authored option;
4. the reconstruction occurred within legitimate authority;
5. the reconstructed repertoire was integrated into subsequent operation;
6. the new repertoire absorbed the target variety that the prior repertoire could not absorb; and
7. no external constructor supplied the missing organizational logic.

A function can satisfy or fail this test independently of every other function.

## Required per-function screen

Explicitly screen:

| Function | Released baseline | Function-specific question |
| --- | --- | --- |
| S1 | `A` | Is there a concrete operational disturbance for which the existing action/tool/delegation repertoire was insufficient, followed by endogenous reconstruction of the operational repertoire and later use of that reconstruction to close the same variety? |
| S2 | `A` | Is there a concrete inter-specialist dependency/interface/deadlock disturbance that the existing team-coordination repertoire could not attenuate, followed by endogenous reconstruction of role/dependency/coordination organization and demonstrated later closure? |
| S3 | `A` | Is there a current whole-assistant/team control disturbance that exceeded existing priority/retry/reallocation/team-control repertoire, followed by endogenous reconstruction of current-control organization and subsequent closure? |
| S3* | `C` | Does Scion itself construct the missing independent complementary-audit organization at runtime, preserve sufficient independence, integrate findings into corrective control, and do so because the prior audit repertoire was insufficient? |
| S4 | `A` | Is there a disturbance showing that the existing Observe → Reflect → Coach/adaptation repertoire itself was insufficient, followed by endogenous reconstruction of how future/external variety is sensed, modeled or translated into later capability? |

S5 is `—` at the released baseline and is outside the required positive-function screen. If evidence appears to establish a released-baseline error, record it as a canonical reassessment question rather than silently turning the `S` experiment into a baseline rewrite.

For each required row record exactly one:

- `candidate-witness`
- `no-candidate-witness`
- `insufficient-evidence`

A `candidate-witness` must then receive the complete candidate `S` test from the pinned Skills `SPEC.md`.

## Primary evidence starting set

Reviewers may inspect any primary file at the frozen Scion revision needed to answer the question. The following paths are starting references, not a closed evidence list and not findings:

- `.agent/agent.toml`
- `src/mastra/agents/interactive.ts`
- `src/mastra/lib/loop-patterns/task-based.ts`
- `src/mastra/lib/loop-patterns/agent-team.ts`
- `src/mastra/tools/handoff-agent.ts`
- `docs/HEARTBEAT_SYSTEM.md`
- `src/mastra/lib/instructions/heartbeat.ts`
- `docs/ADAPTATION_SYSTEM.md`
- `src/mastra/workflows/observe-workflow.ts`
- `src/mastra/agents/observer.ts`
- `src/mastra/workflows/reflect-workflow.ts`
- `src/mastra/workflows/coach-workflow.ts`
- `src/mastra/processors/adaptation-processor.ts`
- `src/mastra/client.ts`
- `src/mastra/tools/index.ts`

Use repository history only when necessary to establish a concrete runtime transition and keep evidence pinned/immutable.

## Important negative tests

Do not count any of the following by itself as `S`:

- spawning a specialist;
- adding a role from an already-authored team procedure;
- changing task assignment or dependency order within the existing team-management repertoire;
- retrying/reprioritizing from the existing heartbeat repertoire;
- producing new observations, patterns or coaching suggestions through the existing adaptation pipeline;
- loading a different skill/tool/configuration;
- a human/developer changing Scion code or configuration;
- repository-development evolution outside the declared runtime boundary.

The question is reconstruction of the relevant organizational repertoire, not merely flexible use of it.

## Strong recursive witness — separate test

Separately ask whether Scion autonomously creates or reorganizes a **new viable recursion** because the prior organization lacks requisite variety.

A qualifying witness needs primary evidence for the chain:

```text
prior organization cannot absorb material in-domain variety
→ Scion recognizes organizational insufficiency
→ Scion defines a bounded lower purpose/domain
→ Scion creates/reorganizes an operational unit or subsystem
→ the new recursion obtains enough local coordination/current control/audit/adaptation/policy for its boundary
→ bounded autonomy is granted
→ parent/child authority and escalation are integrated without duplicate ultimate authority
→ the new recursion absorbs the variety that the prior organization could not
```

Ephemeral specialists, team nesting, delegation depth or role creation are not sufficient without these relations.

Record:

```text
strong_recursive_witness: yes | no | inconclusive
```

## Required decision record

Each independent reviewer must produce:

- reviewer/context declaration;
- frozen revisions and boundary confirmation;
- full per-function screening table for S1, S2, S3, S3*, S4;
- for every `candidate-witness`, the complete `SPEC.md` test fields;
- primary evidence links;
- counter-evidence and missing evidence;
- strongest alternative released-Methodology interpretation;
- `strong_recursive_witness`;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`

The overall finding must identify which function-specific witness, if any, carries it.

## Independence and publication boundary

Two independent reviews are required.

- Both reviewers receive this packet and the same frozen revisions.
- Review 2 must not see Review 1 reasoning or finding before completing its own record.
- Do not publish Review 1 into a discoverable GitHub artifact before Review 2 completes.
- After both judgments exist, publish `review-1.md`, `review-2.md` and `synthesis.md` together.
- Do not modify canonical assessment states, catalog, signatures, TLDR, rankings, Full-A views or released Methodology from this experiment.
