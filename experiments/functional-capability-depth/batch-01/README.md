# S1 capability comparison — test batch 01

Status: **non-normative pilot batch**

This batch tests the hypothesis recorded in [`../NOTE.md`](../NOTE.md): systems can share the same canonical VSM closure state for a function while differing materially in the capability of that same function.

This batch MUST NOT change canonical VSM assessments, publication states, `TLDR.md`, `RANKINGS.md`, `FULL_A.md`, or any Profile / Methodology semantics.

## Pilot question

Among systems whose canonical state is `S1=A`, can we establish reproducible, evidence-backed differences in **S1 capability** without using broader VSM coverage as a performance prior?

The unit of comparison is:

```text
system A.S1  ↔  system B.S1
```

not:

```text
system A  ↔  system B
```

as a global harness-quality judgment.

Batch 01 is intentionally limited to S1. It does not define S2/S3/S3*/S4/S5 capability criteria.

## Frozen comparison cohort

Use the canonical Index assessment revision as the frozen comparison boundary. Do not silently replace these refs with newer upstream heads during this pilot.

| Harness | Upstream | Frozen review ref | Canonical vector | S1 cohort reason |
| --- | --- | --- | --- | --- |
| `oh-my-pi` | `can1357/oh-my-pi` | `dbf3afad4894bde827d90f965e77b3fe1c5a95e5` | `A A A(P) A — —` | `S1=A`; thick first-party operational runtime |
| `Ouroboros` | `razzant/ouroboros` | `86806ee123ce8e26cc063cc1a618f975eea64f26` | `A A A A A(P) A(P)` | `S1=A`; Full-A system with first-party operational loop |
| `thClaws` | `thClaws/thClaws` | `cd700937a71a391f052438d139b7b1c5a6456755` | `A A A A — P` | `S1=A`; thick first-party general-purpose runtime |
| `Headcount` | `cbrock84/headcount` | `9cbf34005e3e8a980a6af9b55eb226bd926a62b3` | `A A A C A A` | `S1=A`; organizational layer with host-inherited execution |
| `Henterprise` | `humbertobellor/henterprise` | `0bd56397676462e216f92b5b7800919a3597a99a` | `A C A C A A` | `S1=A`; second host-inheritance / organizational-layer case |
| `Pi` | `earendil-works/pi` | `71dca871bc80b6bc97be37f0ca3189399d651fff` | `A — — — — —` | `S1=A`; narrow-S1 control |

The non-S1 canonical states are context only. They MUST NOT be used as inputs to the S1 capability judgment.

In particular:

- Full-A gives no S1 capability bonus;
- absence of S4/S5 gives no S1 capability penalty;
- broad organizational topology must not substitute for S1 evidence.

## S1 capability under test

For this pilot, S1 capability means the demonstrated capacity of the credited S1 boundary to turn an operational objective into successful environment-facing work under defined conditions.

Batch 01 compares these candidate S1-specific dimensions:

### 1. Operational effectiveness

Can S1 complete the operational objective successfully under matched or otherwise comparable conditions?

Prefer:

- pass / completion rate;
- task success under a fixed model;
- controlled before/after harness effects;
- reproducible task traces.

### 2. Environment-interaction fidelity

How reliably does S1 convert decisions into correct environment-facing actions?

Possible evidence:

- tool-call correctness;
- edit / mutation correctness;
- command / process execution fidelity;
- browser, filesystem, repository or other environment interaction where applicable;
- detection of failed or stale actions.

Tool count alone is not evidence of greater fidelity.

### 3. Operational state continuity

How well does S1 preserve and use state needed for the current operational trajectory?

Possible evidence:

- context continuity;
- persistent or resumable task state;
- working-memory discipline;
- artifact / observation retention;
- recovery of the current task after interruption.

This is about current S1 operation, not S4 learning or long-horizon organizational adaptation.

### 4. Recovery / resilience

How effectively can S1 detect and recover from failures inside its operational trajectory?

Possible evidence:

- failed tool-call recovery;
- invalid edit / command correction;
- retry policy quality;
- rollback / alternate-path behavior;
- recovery from process or context failure;
- controlled failure-injection results.

### 5. Operational result assurance

How well does S1 establish that its own operational output is acceptable before treating the task as complete?

Possible evidence:

- first-party tests or checks integrated into the S1 loop;
- output validation;
- execution-result checking;
- task-local verification mechanisms.

Do not silently credit independent complementary review here. A distinct S3* reviewer remains S3* topology; Batch 01 may record that its output informs S1, but must not turn S3* existence into an S1 capability bonus without showing the actual operational effect.

### 6. Efficiency

How much resource does S1 require for comparable successful work?

Possible evidence:

- model tokens;
- tool calls;
- retries;
- wall-clock latency;
- model / infrastructure cost.

Efficiency is only comparable when task/model/environment conditions are sufficiently aligned.

### 7. Portability / robustness

Does the observed S1 capability survive changes in substrate?

Possible evidence:

- multiple models;
- multiple task families;
- multiple environments;
- repeated runs;
- controlled model or tool substitutions.

This dimension is especially important before promoting evidence from one specialized domain into a general S1 claim.

## Applied-domain evidence

S1 capability is the comparison target. Coding, research, government, SRE, security, and other domains are **evidence contexts / projections**.

```text
S1 capability comparison
        ↓
        ├── Coding / SWE witness
        ├── Research / Science witness
        ├── Government / Public Administration witness
        ├── Cybersecurity / Incident Response witness
        ├── Infrastructure / SRE witness
        └── other applied-domain witnesses
```

A domain-specific result remains domain-specific unless a transfer claim is supported.

Examples:

Allowed:

```text
oh-my-pi.S1 shows stronger edit/tool fidelity than X.S1 on the frozen Coding/SWE evidence.
```

Not automatically allowed:

```text
oh-my-pi.S1 is universally stronger than X.S1.
```

A harness is never penalized for lacking evidence in an unrelated specialized domain. The corresponding projection is simply unsupported / unevaluated.

## Capability ownership boundary

Every positive S1 capability claim MUST label its ownership source as one of:

- `native` — implemented and owned inside the credited first-party S1 boundary;
- `inherited` — supplied primarily by an external host, model, coding agent, runtime, IDE, MCP/tool service, or other substrate;
- `mixed` — S1 adds a material first-party control/transformation over inherited capability;
- `unclear` — evidence is insufficient to assign the boundary confidently.

User-visible ability and first-party S1 capability are not always the same thing.

This boundary is a core test for Headcount and Henterprise: their canonical `S1=A` state remains unchanged, while the pilot asks what portion of operational capability can be credited to the first-party S1 versus the host.

## Evidence hierarchy

Prefer, in descending order:

1. reproducible fixed-model / matched-model task comparisons;
2. public traces or artifacts sufficient to inspect the claimed S1 effect;
3. controlled ablations or before/after results attributable to an S1 mechanism;
4. executable tests / code paths demonstrating the mechanism;
5. primary technical documentation tied to concrete implementation;
6. maintainer claims without reproducible evidence.

Feature lists are supporting architecture evidence, not S1 capability scores.

Self-reported benchmark results may be recorded, but MUST be labeled `self-reported` unless independently reproduced or externally verified.

## Pairwise tests

### P1 — narrow S1 vs thick S1

`Pi.S1` ↔ `oh-my-pi.S1`

Question: does the shared `S1=A` state conceal reproducible differences in operational effectiveness, environment fidelity, state continuity, recovery, assurance, efficiency, or portability?

### P2 — non-Full-A S1 vs Full-A S1

`oh-my-pi.S1` ↔ `Ouroboros.S1`

Question: can S1 capability be compared without allowing Ouroboros's S4/S5 closure or Full-A status to influence the S1 judgment?

Coding/SWE may provide a shared specialized evidence context, but any conclusion must remain scoped to the evidence actually available.

### P3 — thick runtime vs thick runtime

`oh-my-pi.S1` ↔ `thClaws.S1`

Question: can two substantial first-party runtimes with different product emphasis be compared on S1-specific dimensions without treating product breadth as capability?

### P4 — first-party runtime vs organizational overlay

`oh-my-pi.S1` ↔ `Headcount.S1`

Question: does explicit `native / inherited / mixed` accounting distinguish first-party S1 capability from host-supplied execution while preserving both systems' canonical `S1=A` classification?

### P5 — host-inheritance replication

`Headcount.S1` ↔ `Henterprise.S1`

Question: can the same S1 ownership-accounting rule be applied consistently to two organizational-layer systems?

### P6 — Full-A S1 vs host-inherited S1

`Ouroboros.S1` ↔ `Headcount.S1` and `Henterprise.S1`

Question: after isolating the S1 boundary, what S1 capability evidence remains comparable, and what remains inherited or incomparable?

No conclusion about S2–S5 should be drawn from this test.

## Per-system S1 evidence record

Create one S1 evidence record per system when the pilot is executed:

```text
batch-01/
  README.md
  oh-my-pi.md
  ouroboros.md
  thclaws.md
  headcount.md
  henterprise.md
  pi.md
  SYNTHESIS.md
```

Each record should contain:

```markdown
# <system> — S1 capability evidence

## Frozen boundary
- repository:
- review_ref:
- canonical S1 state: A

## Credited S1 boundary
- first-party S1 actor / loop:
- environment-facing action path:
- external substrates:

## S1 evidence
| S1 dimension | Ownership | Evidence domain | Evidence type | Observation | Confidence |
| --- | --- | --- | --- | --- | --- |
| operational effectiveness | native/inherited/mixed/unclear | general / applied-domain | ... | ... | ... |
| environment-interaction fidelity | ... | ... | ... | ... | ... |
| operational state continuity | ... | ... | ... | ... | ... |
| recovery / resilience | ... | ... | ... | ... | ... |
| operational result assurance | ... | ... | ... | ... | ... |
| efficiency | ... | ... | ... | ... | ... |
| portability / robustness | ... | ... | ... | ... | ... |

## Specialized-domain witnesses
- Coding / SWE:
- Research / Science:
- Government / Public Administration:
- other applicable domains:

## Controlled / benchmark evidence
- ...

## Unsupported or non-comparable claims
- ...
```

Do not assign an overall harness capability score in the per-system record.

## Synthesis

`SYNTHESIS.md` should compare **S1 to S1** dimension-by-dimension.

Example shape:

```text
                         OMP.S1    Ouroboros.S1    thClaws.S1
operational effect          ?            ?              ?
tool/environment fidelity   ?            ?              ?
state continuity            ?            ?              ?
recovery                    ?            ?              ?
result assurance            ?            ?              ?
efficiency                  ?            ?              ?
portability                 ?            ?              ?
```

The synthesis may state pairwise evidence-backed relations such as:

- stronger evidence for dimension X under domain Y;
- comparable under the available evidence;
- incomparable because conditions differ;
- primarily native versus primarily inherited;
- insufficient evidence.

It MUST NOT force a total order.

## Disallowed conclusions

Batch 01 must not:

- rank harnesses globally;
- produce a weighted harness-wide capability total;
- infer S1 capability from the number of VSM `A` states;
- treat Full-A as an S1 quality bonus;
- treat absence of S4/S5 as an S1 penalty;
- treat tool count as S1 quality;
- turn S3* review capability into S1 capability merely because a reviewer exists;
- treat specialized-domain breadth as general S1 strength;
- treat one specialized benchmark as universal S1 capability;
- convert experimental capability findings into canonical VSM states;
- modify upstream systems to manufacture evidence for the pilot.

## Success criteria

Batch 01 supports the research direction only if all of the following hold:

1. at least four of six systems yield enough primary evidence for a meaningful S1 comparison;
2. at least one `S1=A` pair exhibits a defensible capability difference not expressible by the canonical S1 state alone;
3. the difference survives explicit `native / inherited / mixed` accounting;
4. non-S1 VSM coverage can be excluded from the S1 judgment without losing the comparison;
5. applied-domain evidence can remain scoped as a projection rather than redefining S1;
6. at least one dimension or pair remains honestly `incomparable` where evidence does not support an ordering;
7. an independent reviewer can reconstruct the S1 pairwise conclusion from the frozen evidence without relying on the original researcher's overall impression of either harness.

The hypothesis should be weakened or rejected if the apparent distinctions depend mainly on feature counting, broader VSM coverage, maintainer marketing, domain labels, unfrozen upstream changes, or subjective global impressions.

## Promotion boundary

This batch is Index-local experimental research only.

If a stable S1 capability-comparison procedure emerges, that procedure should be proposed upstream in `opensiro/vsm-harness-skills` as an **S1-specific** experimental protocol.

Later S2/S3/S3*/S4/S5 capability experiments should define their own function-specific criteria rather than reuse the S1 dimensions mechanically.

The intended long-term shape is:

```text
canonical VSM closure / ownership
        │
        ├── S1 capability comparison across systems
        ├── S2 capability comparison across systems
        ├── S3 capability comparison across systems
        ├── S3* capability comparison across systems
        ├── S4 capability comparison across systems
        └── S5 capability comparison across systems
                 │
                 └── applied-domain projections where useful
```

No harness-wide capability score is required.