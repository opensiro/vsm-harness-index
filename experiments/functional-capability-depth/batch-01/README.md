# Functional capability depth — test batch 01

Status: **non-normative pilot batch**

This batch tests the hypothesis recorded in [`../NOTE.md`](../NOTE.md): canonical VSM closure / ownership and functional harness capability are related but distinct dimensions.

This batch MUST NOT change canonical VSM assessments, publication states, `TLDR.md`, `RANKINGS.md`, `FULL_A.md`, or any Profile / Methodology semantics.

## Pilot question

Can harnesses sharing the same canonical `S1=A` state exhibit materially different, evidence-backed **general S1 capability depth**, including cases where a narrower VSM profile has stronger first-party execution capability than a near-Full-A or Full-A organization?

The pilot is falsification-oriented. It should be considered unsuccessful if the proposed capability distinctions cannot be grounded reproducibly enough to survive independent review.

## General-domain rule

Batch 01 evaluates **general capability domains first**. It does not define S1 depth through any one applied vertical such as coding.

The generic capability layer is intended to support later specialized projections, following the same split used for the curated Awesome taxonomy:

```text
general capability / form layer
        ↓
        ├── Coding / SWE
        ├── Research / Science
        ├── Government / Public Administration
        ├── Cybersecurity / Incident Response
        ├── Infrastructure / SRE
        ├── Enterprise Operations
        └── other applied domains
```

Specialized domains may supply task distributions, success criteria, required environment reach and domain-specific evidence. They MUST NOT redefine the generic capability dimensions or turn strength in one vertical into universal harness quality.

Architectural/product shape such as `Base/Constructor` versus `Applied` is descriptive context, not a capability bonus.

## Frozen comparison cohort

Use the canonical Index assessment revision as the initial comparison boundary. Do not silently replace these refs with newer upstream heads during this pilot.

| Harness | Upstream | Frozen review ref | Canonical vector | Role in batch |
| --- | --- | --- | --- | --- |
| `oh-my-pi` | `can1357/oh-my-pi` | `dbf3afad4894bde827d90f965e77b3fe1c5a95e5` | `A A A(P) A — —` | thick first-party S1; Coding/SWE witness |
| `Ouroboros` | `razzant/ouroboros` | `86806ee123ce8e26cc063cc1a618f975eea64f26` | `A A A A A(P) A(P)` | current Full-A comparison; general-purpose runtime |
| `thClaws` | `thClaws/thClaws` | `cd700937a71a391f052438d139b7b1c5a6456755` | `A A A A — P` | near-Full-A, thick general-purpose first-party runtime |
| `Headcount` | `cbrock84/headcount` | `9cbf34005e3e8a980a6af9b55eb226bd926a62b3` | `A A A C A A` | near-Full-A organizational layer / host-inheritance case |
| `Henterprise` | `humbertobellor/henterprise` | `0bd56397676462e216f92b5b7800919a3597a99a` | `A C A C A A` | organizational-layer replication control |
| `Pi` | `earendil-works/pi` | `71dca871bc80b6bc97be37f0ca3189399d651fff` | `A — — — — —` | narrow-S1 control |

The canonical vectors are context only. They MUST NOT be used as inputs to a capability judgment except to select the VSM function being compared.

## Primary target: S1 capability depth

Batch 01 intentionally starts with S1 rather than attempting to score all six VSM functions at once.

For this pilot, `S1 capability depth` means the demonstrated ability of the assessed harness boundary to turn an operational objective into successful environment-facing work through its own model/tool execution path, independent of the applied domain used to observe that capability.

The assessment should distinguish at least:

- task effectiveness under a fixed or matched model where evidence exists;
- tool fidelity and correctness of environment interaction;
- breadth and adequacy of first-party execution primitives relevant to task completion;
- context handling and memory insofar as they affect current S1 work;
- recovery from tool, process, state, or trajectory failures;
- verification integrated into the operational loop;
- efficiency effects such as tokens, retries, latency, or cost when supported by controlled evidence;
- portability across models, environments, or task domains when supported by evidence.

These are general evidence dimensions, not feature counters.

## Explanatory capability vector

Use the candidate vector from the research note as a structured evidence map:

```text
E  execution/task effectiveness
T  tool fidelity and environment reach
C  context and memory quality
D  delegation / multi-agent execution quality
V  verification and review quality
R  recovery / resilience
O  operational maturity
B  benchmark / experimental evidence strength
```

Interpret these dimensions generically:

- a code edit, a browser action, a research retrieval step and an administrative system mutation are all possible observations of `T`, but none defines `T` by itself;
- a code-review benchmark can support `V` in a Coding/SWE projection, but general `V` requires evidence about the underlying verification mechanism rather than the application label;
- domain breadth alone does not establish greater `E`;
- `D` should be recorded separately because delegation can cross into S2/S3 topology and must not be allowed to inflate S1 merely because more agents exist.

Do **not** compute a weighted total or overall winner in this pilot.

## Capability ownership boundary

Every positive capability claim MUST label its ownership source as one of:

- `native` — implemented and owned inside the assessed first-party harness boundary;
- `inherited` — supplied primarily by an external host, coding agent, model provider, MCP/tool service, IDE, or other substrate;
- `mixed` — the harness adds a material first-party control/transformation over an inherited substrate;
- `unclear` — evidence is insufficient to assign the boundary confidently.

A host-inherited capability may matter to user-visible performance, but it MUST NOT be silently credited as first-party harness depth.

This distinction is especially important for `Headcount` and `Henterprise`, where organizational closure can be broad while low-level execution is supplied by the host runtime.

## Evidence-domain label

Every empirical claim SHOULD also identify the domain in which it was observed:

- `general` — directly demonstrated across multiple unrelated task/environment classes or by a domain-independent mechanism;
- `coding-swe`;
- `research-science`;
- `government-public-admin`;
- `cybersecurity-ir`;
- `infrastructure-sre`;
- `enterprise-ops`;
- another explicitly named applied domain.

Domain-specific evidence can support a general mechanism claim only when the mechanism and transfer argument are explicit. Otherwise it remains evidence for the specialized projection only.

**No absence penalty:** a harness does not lose general capability depth merely because it does not target a particular specialized domain. Missing applied-domain evidence means only that the corresponding specialized projection is unevaluated or unsupported.

## Evidence hierarchy

Prefer, in descending order:

1. reproducible fixed-model or matched-model task results;
2. public traces / artifacts sufficient to inspect the claimed harness effect;
3. controlled ablations or before/after results attributable to a specific harness mechanism;
4. executable tests or code paths that directly demonstrate the mechanism;
5. primary technical documentation tied to concrete implementation;
6. maintainer claims without reproducible evidence.

A feature list alone is insufficient evidence for greater capability depth.

Self-reported benchmark results may be recorded, but MUST be labeled `self-reported` unless independently reproduced or externally verified.

## Pairwise tests

The batch should answer these comparisons without producing an overall ranking.

### P1 — same `S1=A`, radically different topology

`oh-my-pi` vs `Pi`

Question: does the shared canonical `S1=A` state conceal a materially different first-party S1 execution surface and evidence base on **generic capability dimensions**?

Coding/SWE evidence may be used as a witness where available, but the pairwise conclusion must distinguish the specialized observation from the general mechanism claim.

### P2 — narrow profile vs Full-A

`oh-my-pi` vs `Ouroboros`

Question: can a non-Full-A harness equal or exceed the Full-A system on one or more **general S1 capability dimensions** while remaining clearly weaker in organizational coverage?

A Coding/SWE projection may be reported separately because both systems expose coding evidence, but it MUST NOT substitute for the general comparison.

A result in either direction is acceptable. The test is whether the distinction can be represented without treating Full-A as a performance prior.

### P3 — thick runtime vs near-Full-A runtime

`oh-my-pi` vs `thClaws`

Question: can two strong first-party runtimes with different product emphasis be compared on generic `E/T/C/V/R/O/B` dimensions without collapsing product/domain breadth into quality?

A specialized Coding/SWE view may additionally expose where `oh-my-pi` is optimized more deeply for source-code work, while thClaws may expose evidence from broader applied environments.

### P4 — deep runtime vs organizational overlay

`oh-my-pi` vs `Headcount`

Question: does an explicit `native / inherited / mixed` boundary prevent broad organizational closure from being mistaken for first-party general S1 execution depth?

Do not infer that coding specialization itself makes `oh-my-pi` generally stronger; compare only generic mechanisms/evidence that cross the domain boundary.

### P5 — replication of host-inheritance distinction

`Headcount` vs `Henterprise`

Question: is the native/inherited distinction reproducible across two independently assessed organizational-layer systems rather than being an artifact of one project?

This pair also tests whether an Enterprise/organizational applied domain can remain a projection over the same generic capability model.

### P6 — Full-A vs near-Full-A

`Ouroboros` vs `Headcount` and `Henterprise`

Question: does Full-A provide any observable **general S1 capability** advantage once execution-substrate ownership is separated, or is the difference mainly in higher-order organizational closure?

This is exploratory only; no causal claim should be made from topology alone.

## Per-harness record

Create one evidence record per harness under this directory when the pilot is executed:

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

Each harness record should contain:

```markdown
# <harness>

## Frozen boundary
- repository:
- review_ref:
- canonical S1 state: A

## S1 operational boundary
- what counts as first-party S1:
- external substrates:

## General capability evidence map
| Dimension | Ownership | Evidence domain | Evidence type | Observation | Confidence |
| --- | --- | --- | --- | --- | --- |
| E | native/inherited/mixed/unclear | general / applied-domain | ... | ... | ... |
| T | ... | ... | ... | ... | ... |
| C | ... | ... | ... | ... | ... |
| D | ... | ... | ... | ... | ... |
| V | ... | ... | ... | ... | ... |
| R | ... | ... | ... | ... | ... |
| O | ... | ... | ... | ... | ... |
| B | ... | ... | ... | ... | ... |

## Specialized domain witnesses
### Coding / SWE
- ...

### Research / Science
- ...

### Other applicable views
- ...

## Controlled / benchmark evidence
- ...

## Unsupported or non-comparable claims
- ...

## Provisional general S1-depth conclusion
- qualitative only; no scalar score in Batch 01
```

A harness does not need evidence for every specialized domain. Empty domain views are expected and MUST NOT count against general capability depth.

## Synthesis rules

`SYNTHESIS.md` may state only evidence-backed pairwise conclusions.

Allowed examples:

- `oh-my-pi demonstrates stronger first-party evidence for general tool-interaction fidelity than X at the frozen boundary; the strongest observed witness is in Coding/SWE`;
- `X has broader organizational closure, but this batch does not establish greater general S1 capability`;
- `X is stronger on the Coding/SWE projection, while general recovery remains incomparable`;
- `the available evidence is insufficient to compare recovery between X and Y`;
- `most of Y's execution capability is inherited from host Z, so first-party S1 depth remains indeterminate`.

Disallowed in Batch 01:

- overall harness rankings;
- weighted totals;
- deriving capability from the number of VSM `A` states;
- treating Full-A as a quality bonus;
- treating tool count as execution quality;
- treating specialized-domain breadth as general capability depth;
- treating one specialized-domain benchmark as universal harness quality;
- penalizing a harness for not targeting a specialized applied domain;
- converting experimental conclusions into canonical autonomy states;
- modifying upstream repositories to create evidence for this pilot.

## Success criteria

Batch 01 supports the research direction only if all of the following hold:

1. at least four of six harnesses yield enough primary evidence to populate a meaningful **general** S1 evidence map;
2. at least one same-state pair (`S1=A` vs `S1=A`) exhibits a defensible general capability distinction not expressible by the canonical state alone;
3. the distinction survives explicit `native / inherited / mixed` boundary accounting;
4. specialized-domain evidence can be kept as a projection without silently redefining the generic dimensions;
5. at least one pair remains honestly `incomparable` on one or more dimensions, demonstrating that the method does not force a total order;
6. an independent reviewer can reconstruct the pairwise conclusion from the frozen evidence without relying on the original researcher's semantic impression.

The hypothesis should be weakened or rejected if the distinctions depend mainly on feature counting, maintainer marketing claims, domain labels, unfrozen upstream changes, or subjective overall impressions.

## Promotion boundary

This batch is Index-local experimental research only.

If the pilot produces a stable, reproducible capability procedure, the procedure itself should be proposed upstream in `opensiro/vsm-harness-skills`. The Index should retain frozen real-system evidence, pilot records, and any later derived experimental views.

If Awesome/domain views later consume this experiment, the intended direction is:

```text
canonical VSM closure
        +
general capability evidence
        ↓
curated generic capability/form views
        ↓
specialized applied-domain projections
```

The specialized views remain derived presentations; they do not become a second canonical assessment system.