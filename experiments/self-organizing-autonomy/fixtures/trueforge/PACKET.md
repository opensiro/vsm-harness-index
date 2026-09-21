# TrueForge — frozen `S` clear-A control packet

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#301`

## Frozen revisions

- Experimental Methodology: `opensiro/vsm-harness-skills@947b42e77551ed1a86456f8a812c72a96a36506a`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Canonical Index baseline snapshot: `opensiro/vsm-harness-index@d36ec21b7514b13d6a8647a68c20e7f8a4735ade`
  - `assessments/trueforge.md`
- Target repository: `truefoundry/trueforge@651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88`

Later repository or assessment changes are not inputs to this fixture run.

## Corpus role

This is the real-system **clear `A` control**. It tests whether the candidate `S` protocol distinguishes:

```text
autonomous absorption of broad/novel task variety
through an already available operational repertoire
```

from:

```text
material insufficiency of that repertoire
→ endogenous reconstruction/extension
→ integration
→ post-change closure
```

The packet does not assert the experimental outcome.

## Released baseline

```text
S1  A
S2  —
S3  —
S3* —
S4  —
S5  —
```

Only S1 satisfies the released-`A` prerequisite for candidate `S` testing. S2/S3/S3*/S4/S5 fail the function/ownership prerequisite and cannot be promoted by this experiment.

## Declared boundary

Use the same system-in-focus and operating boundary as the frozen canonical assessment:

- one configured TrueForge root-agent session;
- first-party `AgentThread` / `AgentThreadOrchestrator` execution harness;
- shipped model/tool loop, local/MCP tools, sandbox/filesystem, context compaction, session persistence and approvals;
- dynamic subagents enabled as a normal first-party capability;
- root agent may decide whether to delegate and generate focused child instructions;
- children are bounded delegated workers inside the root task unless separate viable recursion is independently established;
- model providers, remote MCP servers, user-authored skills/plugins and application-specific business logic remain environment/dependencies.

Do not enlarge the boundary to contributor/CI activity, repository development, or downstream application-specific organization.

## Frozen S1 question

At the pinned TrueForge revision and declared root-session boundary, is there primary evidence for a concrete transition where:

1. the existing TrueForge operational repertoire was materially insufficient for a disturbance that remained inside the declared operating domain;
2. TrueForge itself recognized that repertoire insufficiency;
3. TrueForge endogenously reconstructed or extended its own S1 operational process/tooling/local organization rather than merely choosing among or instantiating existing mechanisms;
4. the reconstruction occurred within legitimate authority;
5. the reconstructed repertoire was integrated into later TrueForge operation;
6. later operation used it to absorb the original variety that the prior repertoire could not absorb; and
7. no external constructor supplied the missing organizational logic?

If no such transition is established, distinguish positive evidence that operation stays inside the existing repertoire from simple lack of evidence.

## Required baseline / eligibility screen

| Function | Released baseline | Experimental treatment |
| --- | --- | --- |
| S1 | `A` | Eligible. Record `candidate-witness`, `no-candidate-witness`, or `insufficient-evidence`. |
| S2 | `—` | Ineligible. Delegation/parallel children/shared sandbox are not promoted to S2 by this experiment. |
| S3 | `—` | Ineligible. Thread tracking/scheduling does not become autonomous S3 through `S`. |
| S3* | `—` | Ineligible. Approvals/tracing/ordinary result inspection do not create a released audit function. |
| S4 | `—` | Ineligible. Search, persistence, compaction and mounted skills/plugins do not become S4 through `S`. |
| S5 | `—` | Ineligible. Instructions/configuration/approval policy do not become S5 through `S`. |

A S1 `candidate-witness` must receive the complete candidate test from the pinned Skills `SPEC.md`.

## Existing S1 repertoire to distinguish from reconstruction

The standard distribution already gives the root agent substantial operational variety, including:

- iterative model → tool → observation → model execution;
- local and MCP tools;
- sandbox/filesystem actions;
- runtime decision whether to delegate;
- dynamically generated subagent instructions;
- multiple parallel one-level subagents;
- return of child final results to the root;
- context compaction and session persistence;
- configured approvals/authorization stops.

A hard or novel task that is solved by exercising these existing mechanisms is evidence of ordinary `A` closure, not `S` reconstruction.

## Important negative tests

None of the following establishes `S1=S` by itself:

- the root deciding to use a subagent;
- creating a new ephemeral child with generated instructions;
- changing the number or subject of delegated subtasks;
- concurrent child execution;
- mounting or invoking an already supplied local/MCP tool;
- using a user-authored skill/plugin that the parent supplied;
- context compaction, persistent sessions, retry or replanning;
- writing task artifacts inside the sandbox/filesystem;
- arbitrary task novelty handled by the same root execution loop.

The required change is to TrueForge's **own operational repertoire**, not a new case handled by that repertoire.

## Strong recursive witness — separate test

Separately ask whether TrueForge creates/reorganizes a new viable recursion because its prior organization lacks requisite variety.

Dynamic subagents are not sufficient. A qualifying strong witness needs primary evidence for:

```text
prior organization cannot absorb material in-domain variety
→ TrueForge recognizes organizational insufficiency
→ defines a bounded lower purpose/domain
→ creates/reorganizes an operational unit for that domain
→ establishes enough local coordination/current control/audit/adaptation/policy
→ grants bounded autonomy
→ integrates parent/child authority without duplicate ultimate authority
→ new recursion absorbs the previously unresolved variety
```

Record:

```text
strong_recursive_witness: yes | no | inconclusive
```

## Primary evidence starting set

Reviewers may inspect any primary artifact at the pinned target revision. Starting references:

- `README.md`
- `docs/key-features/subagents.mdx`
- `packages/trueforge-core/src/core/capabilities/builtins/DynamicSubAgents.ts`
- `packages/trueforge-core/src/core/runtime/AgentThread.ts`
- `packages/trueforge-core/src/core/runtime/AgentThreadOrchestrator.ts`
- first-party tool/MCP/sandbox/context/session capability sources needed to trace a claimed transition.

Repository history may be inspected only when needed to reconstruct stable provenance or a runtime transition. Maintainer development history is not itself an operating witness.

## Required decision record

Each independent reviewer must produce:

- reviewer/context declaration;
- frozen revisions and boundary confirmation;
- complete six-function baseline/eligibility table;
- S1 screening result;
- for S1 `candidate-witness`, every full `SPEC.md` candidate-test field;
- target disturbance and prior repertoire;
- insufficiency and recognition evidence;
- reconstructed repertoire and endogenous-construction evidence;
- authorization, integration and post-change closure;
- external-constructor check;
- primary evidence, counter-evidence and missing evidence;
- strongest alternative released-Methodology interpretation;
- any separate canonical reassessment question;
- `strong_recursive_witness`;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`.

## Independence and publication boundary

Two independent reviews are required.

- Both reviewers receive this packet and the same frozen revisions.
- Review 2 must not see Review 1 reasoning/finding before completing its own record.
- Review 1 must not be published as a discoverable GitHub review artifact before Review 2 completes.
- After both judgments exist, publish `review-1.md`, `review-2.md` and `synthesis.md` together.
- Do not modify canonical TrueForge states, catalog, signatures, TLDR, rankings, metrics or released Methodology from this experiment.
