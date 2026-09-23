# Direct S5 benchmark coverage gap

Status: experimental, non-normative.

Issue: #399

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Do any reviewed public benchmark families directly exercise **S5 — Policy and identity** as defined by the current Profile, and can those results be linked to canonical Index systems without confusing policy enforcement with policy ownership?

Current answer:

```text
reviewed direct S5 benchmark families: 0
canonical native/adapter-preserved direct-S5 observations: 0
```

This is an evidence-backed gap result.

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

Policy compliance, enforcement, identity propagation, refusal behavior, ordinary approvals, value preference, escalation plumbing and governance vocabulary are insufficient by themselves.

## Reviewed evidence classes

`coverage.json` preserves the reviewed cases:

- AgentGovBench — `unsuitable`: pre-existing policy enforcement, not ultimate-policy ownership;
- RoleCDE — `proxy`: value/role conflict reasoning without organizational authority/closure;
- Agent-ValueBench — `proxy`: executable value-conflict behavior without legitimate policy authority;
- AgentCity — `proxy`: rich constitutional organization, but benchmarked agent legislation remains below human-authored foundational authority;
- CGST — `proxy`: constitutional/governance conformance and stress evidence, not an executed amendment/adjudication→operation benchmark;
- Constitutional Governance in Metric Spaces — useful governance process, but not an agent-harness benchmark family;
- HEM — useful Parent-authority escalation protocol, but not a benchmark family.

## Canonical observations

`canonical_observations.json` is intentionally empty.

The absence of a direct benchmark must not be converted into an autonomy judgment. Canonical S5 states are established independently from repository evidence.

Representative anchors in this pass preserve several ownership arrangements:

- `headcount` — `A`;
- `henterprise` — `A`;
- `ouroboros` — `A(P)`;
- `thclaws` — `P`;
- `masters-of-ai-harness` — `C(P)`.

These states are categorical ownership arrangements, not a maturity ordering.

## Missing benchmark shape

A future direct S5 benchmark should force a real constitutional/identity-level decision and measure both authority integrity and downstream closure. One useful pattern is:

```text
S3 current pressure
      ↕
S4 future proposal
      ↓
identity / constitutional conflict
      ↓
legitimate S5 authority
      ↓
ratified policy change
      ↓
later operations visibly constrained by the changed rule
```

Potential dimensions include:

- correct escalation to legitimate authority;
- decision provenance and authority integrity;
- constitutional/identity conflict resolution;
- propagation of a newly decided rule;
- resistance to unauthorized policy mutation;
- cross-recursion coherence.

These are S5 capability dimensions, not new VSM systems and not a scalar maturity score.

## Source of truth

- `canonical_observations.json` — direct canonical S5 observations; currently `[]`;
- `coverage.json` — reviewed proxy/unsuitable/protocol cases and canonical anchors;
- `validate.py` — checks the zero-direct-family contract and current canonical S5 states;
- `../vsm-benchmark-family-map/S5-REVIEW.md` — semantic argument and primary-source provenance.

## Non-goals

This layer does not:

- infer S5 from policy/governance terminology;
- treat enforcement of a pre-existing rule as S5 authority;
- infer autonomy from a governance/value score;
- rank `A`, `P`, `A(P)`, `C(P)` or other ownership arrangements;
- modify canonical assessments, Profile, Skills, catalog, TLDR, rankings or Full-A.
