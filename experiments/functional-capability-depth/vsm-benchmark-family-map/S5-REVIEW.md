# S5 benchmark semantic review

Status: experimental, non-normative.

Issue: #399

This follow-up reviews benchmark and protocol candidates specifically against **S5 — Policy and identity** in the current `vsm-harness-profile`.

It does not change canonical assessments or autonomy ownership.

## Result

```text
reviewed direct S5 benchmark families: 0
```

The gap is narrower than “governance benchmarks do not exist”. Public work already covers policy enforcement, value conflicts, constitutional conformance, operational legislation, democratic aggregation and human escalation. What is still missing is a benchmark that executes the full S5 organizational closure:

```text
identity / ultimate-policy tension
        ↓
legitimate authority at the declared recursion
        ↓
actual adjudication / ratification / amendment
        ↓
newly decided policy
        ↓
subsequent operation demonstrably governed by that decision
```

A benchmark that fixes policy in advance and scores compliance or enforcement remains below this gate.

## Direct-S5 gate

A `direct` family must establish all of the following at its declared benchmark boundary:

1. a real mission, identity, ethos, constitutional-rule or ultimate-policy issue;
2. a lower-level tension that is not merely routine S1/S2/S3/S4 control;
3. a legitimate ultimate authority at that recursion level;
4. an actual decision, ratification, adjudication or amendment by that authority;
5. return of the newly decided policy into later operation;
6. evidence that separates policy ownership from enforcement of a pre-existing rule.

The authority may be autonomous, collective or Parent-governed. `P` is a valid ownership arrangement; direct S5 measurement does not require autonomous S5.

## Reviewed candidates

### AgentGovBench — `unsuitable`

Primary source: https://github.com/agentic-control-plane/agentgovbench

AgentGovBench exercises governance plumbing such as identity propagation, policy enforcement, delegation provenance, rate limits, audit completeness, tenant isolation and fail-mode behavior.

Those mechanisms can support governance, but the benchmark begins with policy already decided. It does not test who legitimately owns ultimate identity/policy authority or how a new policy decision is made and returned to operation.

Existing classification remains `unsuitable` for direct S5 measurement.

### RoleCDE — `proxy`

Primary sources:

- https://arxiv.org/abs/2606.01552
- https://github.com/rabbitrose/RoleCDE

RoleCDE exposes structured conflicts between role-specific values and alignment-oriented constraints. This is useful evidence about identity/value conflict reasoning.

The evaluated model is not established as the legitimate ultimate authority of an organization, and the benchmark does not require an adopted policy decision to govern later operation. It remains a proxy.

### Agent-ValueBench — `proxy`

Reviewed repository: `ValueByte-AI/Agent-ValueBench@3527b4a4ea8fc9dde6fbe27cd371c4ba7df76ac1`.

Primary sources:

- https://github.com/ValueByte-AI/Agent-ValueBench
- https://arxiv.org/abs/2605.10365

Agent-ValueBench contains 4,335 executable value-conflict tasks across 28 value systems and asks what values tool-using agents exhibit under those conflicts.

This is stronger behavioral evidence than text-only value dilemmas, and it may expose harness effects on expressed values. It still measures **expressed value choice**, not legitimate organizational authority to settle identity/ultimate policy and bind subsequent operation.

Classification: `proxy`.

### AgentCity — `proxy`

Primary sources:

- https://arxiv.org/abs/2604.07007
- https://agentcity.dev/

AgentCity is unusually close to an S5-relevant organization. Agents legislate operational smart-contract rules, deterministic software executes them, and humans adjudicate through an ownership chain.

The published architecture explicitly separates three contract tiers:

- foundational contracts — human-authored and agent-immutable;
- meta-contracts — procedural governance;
- operational contracts — agent-legislated task rules.

The benchmarked agent legislation is therefore below the ultimate foundational layer. Agents can exercise significant policy-making power without owning the system's ultimate identity/constitutional authority.

Classification: `proxy`, not direct S5.

### Constitutional AI Governance Stress Test (CGST) — `proxy`

Reviewed repository: `CognitiveThoughtEngine/cgst-framework@a70dd1ffd4b2c462a9c0680b6aa6d6b9ad788cdf`.

Primary source: https://github.com/CognitiveThoughtEngine/cgst-framework

CGST is strongly S5-relevant conformance evidence. Its governance rubric asks whether constitutional grounding, amendment authority, autonomy boundaries and other control layers exist and hold under review/stress.

But CGST is an assessment/scoring framework over an architecture. It does not itself execute an identity-level conflict, invoke the named legitimate authority, ratify a changed policy and then observe later operation under that new decision.

Classification: `proxy` / conformance evidence.

## Important adjacent protocols that are not benchmark families

### Constitutional Governance in Metric Spaces

Primary source: https://arxiv.org/abs/2605.13362

This work defines an end-to-end governance process in which a community can adopt policy and amend the constitution under aggregation/supermajority rules. It is useful evidence for what explicit S5 decision machinery can look like.

It is a computational governance process, not a benchmark of an agent harness's S5 capability, so it is not inserted into `map.json` as a benchmark family.

### Human Escalation Mechanism (HEM)

Primary source: https://datatracker.ietf.org/doc/draft-sato-soos-hem/

HEM specifies a non-bypassable human-escalation state, designation chain, structured decisions and return to execution. That is architecturally relevant to Parent-governed S5 closure when the escalated issue is actually identity/ultimate-policy level.

It is a protocol specification, not a benchmark result. Ordinary human confirmation also does not become S5 merely by using HEM; the escalated issue itself must be S5-level.

## Why enforcement is not enough

The distinction this review protects is:

```text
policy already exists
        ↓
propagate / enforce / audit it
        ≠
choose legitimate ultimate policy
```

AgentGovBench is the clearest negative control. A system can be excellent at enforcing policy and still have no ownership of S5.

Likewise, value preference is not authority:

```text
agent chooses between values in a scenario
        ≠
organization legitimately changes its identity/policy
```

## Missing benchmark shape

A direct S5 benchmark should create a bounded organizational conflict such as:

```text
current operational commitment / S3 pressure
                ↕
future adaptation / S4 proposal
                ↓
identity / constitutional conflict
                ↓
legitimate S5 authority
                ↓
ratified decision with provenance
                ↓
subsequent operations governed by that newly decided rule
```

Useful metrics could include:

- correct escalation to the legitimate authority;
- authority/provenance integrity;
- successful resolution of an identity/policy conflict;
- propagation of the **newly decided** rule into later behavior;
- resistance to unauthorized constitutional mutation;
- coherence across recursion boundaries.

No scalar S5 maturity score is implied.

## Canonical-system consequence

Because no direct S5 benchmark family is established, no direct canonical S5 observation should be invented.

Canonical ownership states remain repository-derived and heterogeneous (`A`, `P`, `A(P)`, `C(P)`, etc.). The absence of a direct benchmark does not weaken or reorder those states.

The companion `../s5-system-benchmarks/` layer records this coverage gap and representative canonical anchors.
