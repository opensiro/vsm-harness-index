# Direct S5 benchmark coverage

Status: experimental, non-normative.

Initial issue: #399  
Primary-baseline follow-up: #436  
Direct-family update: #472

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Do reviewed public benchmark families directly exercise **S5 — Policy and identity** as defined by the current Profile, and can those results be linked to canonical Index systems without confusing policy enforcement with policy ownership?

Current answer:

```text
reviewed direct S5 benchmark families:             1
composed direct-S5 observations:                   1
canonical native/adapter-preserved observations:   0
S5 primary baseline:                               gap
```

GovSim-SelfGovern closes the previous **direct-family** hole at its benchmark-defined society boundary. It does not close the **canonical matched-primary** hole.

This remains an evidence-backed gap for the primary baseline, not a zero-capability judgment about systems that canonically establish S5.

## Direct gate

A direct S5 benchmark must exercise:

```text
identity / ultimate-policy tension
        ↓
legitimate authority at the declared recursion
        ↓
actual adjudication / ratification / amendment
        ↓
newly decided rule
        ↓
subsequent operation governed by that decision
```

For a cross-harness primary baseline, that functional path must additionally be native or adapter-preserved for each canonical system under materially matched comparison conditions.

Policy compliance, enforcement, identity propagation, refusal behavior, ordinary approvals, value preference, escalation plumbing and governance vocabulary are insufficient by themselves.

## GovSim-SelfGovern — direct composed S5

Primary source:

```text
arXiv:2609.22600 — From Certain Doom to Survival: Agent-Driven Self-Governance in LLM Agent Societies
```

GovSim-SelfGovern defines a five-agent society that can author executable Python laws through a constrained World API. Valid proposals are sandbox-checked, current members vote, majority-approved laws are enacted, and execution occurs before later round activity.

The direct S5 witness is specifically the **membership/identity authority path**:

```text
fatal resource wall / membership tension
        ↓
agent-authored executable membership law
        ↓
sandbox validation
        ↓
majority vote by current active members
        ↓
enactment
        ↓
agent.active = False
        ↓
member expelled / active system boundary changes
        ↓
subsequent rounds continue after the decision
```

The paper explicitly defines `agent.active = False` as exile. In the published pooled results:

- non-thinking democratic runs enact 8 of 460 exile proposals (1.7%);
- thinking democratic runs enact 31 of 122 exile proposals (25.4%).

The paper also reports that intact survival in the fatal-scarcity game is concentrated among runs that reduce membership early.

This directly exercises S5 at the **benchmark-defined society recursion** because legitimate current-member authority makes and enacts a membership decision that changes who belongs to the system, and the changed membership persists into later operation.

### Boundary and provenance limits

The observation is recorded as:

```text
direct-composed
system compatibility: benchmark-scaffolded
canonical harness: none
code revision: unresolved-authoritative-public-repository
```

The sandbox, voting procedure, game physics and constrained API are benchmark/evaluation membrane. No underlying model or canonical Index harness inherits native S5 ownership or capability by association.

No authoritative public code repository/revision for GovSim-SelfGovern was recovered in this review. Do not attach an unrelated GovSim repository by name similarity.

Not every law in the benchmark is S5. Catch caps, penalties, taxation, treasury disbursement and similar operational rules regulate current activity below the membership/identity layer. They are not promoted to S5 merely because they are legislated.

The broader reported G1 governance result (ICS 45.0% → 72.5%) also mixes multiple governance mechanisms and is not treated as an S5-only effect.

## Reviewed adjacent evidence classes

`coverage.json` preserves the earlier reviewed cases alongside GovSim-SelfGovern:

- AgentGovBench — `unsuitable`: pre-existing policy enforcement, not ultimate-policy ownership;
- RoleCDE — `proxy`: value/role conflict reasoning without organizational authority/closure;
- Agent-ValueBench — `proxy`: executable value-conflict behavior without legitimate policy authority;
- AgentCity — `proxy`: rich constitutional organization, but benchmarked agent legislation remains below human-authored foundational authority;
- CGST — `proxy`: constitutional/governance conformance and stress evidence, not an executed amendment/adjudication→operation benchmark;
- Constitutional Governance in Metric Spaces — useful governance process, but not an agent-harness benchmark family;
- Agent Parliament — actual constitutional ratification/amendment process evidence, but not a reusable harness benchmark;
- HEM — useful Parent-authority escalation protocol, but not a benchmark family;
- Constitutional Agent Governance — strong amendment/authority mechanism evidence, but a conformance/regression suite rather than a matched capability benchmark;
- MAC — measurable constitution optimization without established legitimate ultimate organizational authority;
- CMAG — operation under a fixed constitutional governance layer;
- GPS-Bench — external policy-analysis capability, not the evaluated system's own organizational S5.

## Canonical native-path gap

`canonical_observations.json` remains intentionally empty.

Representative canonical systems already establish several real S5 ownership arrangements from repository evidence:

- `headcount` — `A`;
- `henterprise` — `A`;
- `ouroboros` — `A(P)`;
- `thclaws` — `P`;
- `masters-of-ai-harness` — `C(P)`.

For baseline research each remains:

```text
candidate-native-no-direct-results
```

This means only that no admitted direct canonical native/adapter-preserved S5 benchmark observation currently exists for that path. It does **not** mean S5 is absent or weak.

The separation is deliberate:

```text
canonical repository evidence
→ establishes S5 function / ownership

benchmark-defined composed evidence
→ can establish direct S5 capability at that composed boundary

matched canonical benchmark evidence
→ would support a cross-harness S5 primary
```

The second layer now exists through GovSim-SelfGovern. The third does not.

## Why the primary gap remains

The current evidence state is:

```text
direct S5 benchmark family exists
        !=
canonical native direct-S5 observation exists
        !=
matched canonical S5 baseline exists
```

GovSim-SelfGovern supplies a legitimate direct benchmark-defined S5 organization but no native or adapter-preserved canonical harness rows. The primary baseline therefore remains `gap`.

A future primary requires materially matched evidence for two or more canonical-linkable S5 paths under the same authority/change/subsequent-operation protocol, with recoverable model/configuration provenance.

## Reopen model

The current primary gap should be reconsidered when public evidence supplies one of:

1. an immutable canonical native/adapter-preserved direct S5 result satisfying the complete authority → decision/change → subsequent-operation chain;
2. a materially matched benchmark comparing multiple canonical-linkable S5 systems under that chain;
3. GovSim-SelfGovern or another direct family exposing adapter-preserved canonical rows with sufficient immutable model/configuration provenance for a matched primary cell.

Another benchmark-scaffolded direct family alone is useful evidence depth, but does not satisfy the matched canonical primary gate.

## Source of truth

- `benchmark_observations.json` — direct composed benchmark observations; currently GovSim-SelfGovern;
- `canonical_observations.json` — direct canonical S5 observations; currently `[]`;
- `coverage.json` — reviewed direct/proxy/unsuitable/protocol/candidate cases and canonical native-path gaps;
- `validate.py` — checks direct-family/composed/canonical separation and current canonical S5 states;
- `matched-cell/s5-primary-search-closure.json` — current fail-closed primary-gap disposition and reopen conditions;
- `../vsm-benchmark-family-map/S5-REVIEW.md` — semantic mapping rationale and primary-source provenance.

## Non-goals

This layer does not:

- infer S5 from policy/governance/constitution/amendment terminology;
- treat enforcement of a pre-existing rule as S5 authority;
- treat every GovSim-SelfGovern law as S5;
- attribute the benchmark-defined S5 organization to an underlying model or unrelated repository;
- treat unit or conformance tests as a matched benchmark result;
- infer autonomy from a governance/value score;
- rank `A`, `P`, `A(P)`, `C(P)` or other ownership arrangements;
- create a scalar S5 or overall harness score;
- modify canonical assessments, Profile, Skills, catalog, TLDR, rankings, Full-A or self-organizing-autonomy artifacts.
