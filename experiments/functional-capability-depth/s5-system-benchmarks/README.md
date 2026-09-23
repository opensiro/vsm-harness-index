# Direct S5 benchmark coverage gap

Status: experimental, non-normative.

Initial issue: #399

Primary-baseline follow-up: #436

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Do any reviewed public benchmark families directly exercise **S5 — Policy and identity** as defined by the current Profile, and can those results be linked to canonical Index systems without confusing policy enforcement with policy ownership?

Current answer remains:

```text
reviewed direct S5 benchmark families: 0
canonical native/adapter-preserved direct-S5 observations: 0
S5 primary baseline: gap
```

This is an evidence-backed gap result, not a zero-capability judgment about systems that canonically establish S5.

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

For a cross-harness primary baseline, that functional path must additionally be native or adapter-preserved for each canonical system under matched comparison conditions.

Policy compliance, enforcement, identity propagation, refusal behavior, ordinary approvals, value preference, escalation plumbing and governance vocabulary are insufficient by themselves.

## Reviewed evidence classes

`coverage.json` preserves the original reviewed cases:

- AgentGovBench — `unsuitable`: pre-existing policy enforcement, not ultimate-policy ownership;
- RoleCDE — `proxy`: value/role conflict reasoning without organizational authority/closure;
- Agent-ValueBench — `proxy`: executable value-conflict behavior without legitimate policy authority;
- AgentCity — `proxy`: rich constitutional organization, but benchmarked agent legislation remains below human-authored foundational authority;
- CGST — `proxy`: constitutional/governance conformance and stress evidence, not an executed amendment/adjudication→operation benchmark;
- Constitutional Governance in Metric Spaces — useful governance process, but not an agent-harness benchmark family;
- HEM — useful Parent-authority escalation protocol, but not a benchmark family.

## Primary-baseline follow-up

The follow-up search asks a stricter question than whether constitutional mechanisms now exist:

```text
constitutional mechanism exists
        !=
direct S5 benchmark exists
        !=
matched canonical S5 baseline exists
```

### Constitutional Agent Governance — strong mechanism, not benchmark

Pinned source:

```text
CognitiveThoughtEngine/constitutional-agent-governance@368717cb50b70826412f85022d23b3fd8a0dec77
```

This is the strongest new S5-shaped implementation candidate in the follow-up search. Its first-party amendment-authority tests exercise concrete closure mechanics:

- proposer and ratifier must be distinct;
- ratifiers must hold registered authority;
- ordinary amendments require `RATIFIER` authority;
- hard-constraint and authority-registry changes require `CONSTITUTIONAL_AUTHORITY`;
- successful ratification changes constitution state/version;
- authority-registry mutation is itself authority-gated;
- last-root guards prevent amendment from eliminating ultimate constitutional authority;
- amendment records retain decision provenance.

That is materially closer to the S5 functional shape than generic policy enforcement.

It still does **not** close the primary-baseline requirement. The public artifact is a first-party conformance/regression suite for one library/runtime boundary, not a reusable matched cross-harness capability benchmark. The repository is also not currently a canonical Index system under an independently assessed S5 boundary.

It is therefore recorded as:

```text
candidate-native-mechanism-not-benchmark
```

not as a direct benchmark family and not as a zero score.

### MAC — constitution optimization remains proxy

Pinned implementation:

```text
rushil-thareja/MAC-Multi-Agent-Constitution-Learning@76aea7ce2cd95e46cfcf015a70895fdc267a0f4f
```

Paper:

```text
arXiv:2603.15968
```

MAC uses specialized agents to accept, edit or reject structured rule updates and evaluates the resulting learned constitutions on PII tagging and other agentic tasks.

This is measurable constitution/rule adaptation, but the optimized rule set is selected for task reward. The evaluated system is not established as the legitimate ultimate-policy authority of an organization resolving an identity-level tension, and benchmark improvement does not establish organizational ratification or authority provenance.

Keep it `proxy`; constitution adaptation by itself is not S5 ownership.

### CMAG — operation under fixed constitutional governance

Paper:

```text
arXiv:2603.13189
```

CMAG compares constitutional governance regimes under adversarial multi-agent conditions and reports cooperation, autonomy, integrity and fairness outcomes.

The constitution is supplied as the governance filtering/optimization layer. The experiment therefore measures behavior **under** policy rather than legitimate ultimate authority deciding or amending the policy itself.

Keep it `proxy`, not direct S5.

### GPS-Bench — policy analysis is not organizational S5

Paper:

```text
arXiv:2609.03553
```

GPS-Bench compares reasoning and multi-agent simulation approaches for evidence-grounded public-policy impact prediction.

Its object is external governance-policy analysis: actor behavior and downstream effects of public policy. It does not exercise the evaluated harness's own identity or ultimate-policy authority.

Record it as `unsuitable` for direct S5 while retaining it as useful policy-analysis context.

## Canonical native-path gap

`canonical_observations.json` remains intentionally empty.

Representative canonical systems already establish several real S5 ownership arrangements from repository evidence:

- `headcount` — `A`;
- `henterprise` — `A`;
- `ouroboros` — `A(P)`;
- `thclaws` — `P`;
- `masters-of-ai-harness` — `C(P)`.

For baseline research each is marked:

```text
candidate-native-no-direct-results
```

This means only that no admitted direct matched S5 benchmark observation currently exists for that canonical path. It does **not** mean the function is absent or weak.

The separation is deliberate:

```text
canonical repository evidence
→ establishes S5 function / ownership

benchmark evidence
→ would measure capability of that established S5 path
```

Absence of the second layer cannot rewrite the first.

## Why governance benchmarks still do not collapse the gap

Several nearby benchmark shapes are useful without being direct S5:

```text
policy compliance
→ tests whether an existing rule is followed

constitutional filtering
→ tests outcomes under a supplied rule set

constitution optimization
→ searches for a better rule/prompt under task reward

policy simulation
→ predicts effects of external policy
```

Direct S5 instead needs the evaluated organizational system to confront an identity/ultimate-policy tension, route it to legitimate authority, actually decide/ratify/amend policy, preserve decision provenance, and then operate under the changed rule.

For the OpenSiro primary baseline, two or more canonical systems must eventually expose that path under matched comparison conditions.

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
- `coverage.json` — reviewed proxy/unsuitable/protocol/candidate cases and canonical native-path gaps;
- `validate.py` — checks the zero-direct-family contract, required follow-up cases and current canonical S5 states;
- `../vsm-benchmark-family-map/S5-REVIEW.md` — initial semantic argument and primary-source provenance.

## Non-goals

This layer does not:

- infer S5 from policy/governance/constitution/amendment terminology;
- treat enforcement of a pre-existing rule as S5 authority;
- treat unit or conformance tests as a matched benchmark result;
- infer autonomy from a governance/value score;
- infer S5 from constitution optimization alone;
- rank `A`, `P`, `A(P)`, `C(P)` or other ownership arrangements;
- create a scalar S5 or overall harness score;
- modify canonical assessments, Profile, Skills, catalog, TLDR, rankings, Full-A or self-organizing-autonomy artifacts.
