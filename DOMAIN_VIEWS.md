# Domain Views

The VSM Harness Index is an evidence base for assessing agent harnesses. It is intentionally broader than any curated presentation layer built on top of it.

Domain views are downstream ways to organize assessed harnesses by the real-world work they are designed to perform. They do not replace the canonical catalog, assessments, TL;DRs, or autonomy rankings.

## Why Domain Views Exist

Many agent lists group projects by technical component: orchestration, memory, context, sandboxing, protocols, evaluation, or observability. Those categories are useful for implementation work, but they do not answer an organizational question:

> What kind of organization does this harness instantiate in a real operating domain, and where do operational autonomy, coordination, regulation, audit, adaptation, policy, and ultimate authority reside?

VSM assessments provide the evidence needed to answer that question consistently across otherwise very different domains.

## Candidate Domain Families

Downstream curated views may use domain families such as:

- Government and public administration
- Cybersecurity and incident response
- Scientific discovery and laboratory automation
- Industrial and robotic operations
- Enterprise operations
- Infrastructure and SRE
- Healthcare operations
- Legal and compliance operations
- Logistics and supply chain
- Autonomous or decentralized organizations

This list is illustrative rather than exhaustive. Domain labels should follow the upstream system's actual mission and evidence, not be inferred from generic capabilities.

## Domain Assignment Rule

Assign a domain only when the reviewed distribution is explicitly designed to perform work in that domain.

Do not assign a domain merely because:

- the maintainer belongs to that industry;
- the harness exposes generic governance, safety, workflow, or policy features;
- a downstream user could configure the harness for that domain;
- a README example happens to mention that domain.

A reusable constructor may therefore remain domain-neutral in the Index while appearing in a separate constructor/building-block view downstream.

## Relationship to VSM Assessment

Domain is an orthogonal dimension to the VSM autonomy vector.

Two systems in the same domain may implement very different organizational forms. Conversely, two systems in different domains may share a similar VSM structure.

For curated domain views, prefer entries that add organizational contrast rather than simply maximizing project count. Useful distinctions include:

- where S2 coordination resides;
- whether current-system regulation is agent-owned, constructor-owned, or parent-governed;
- whether S3* is operationally independent;
- whether S4 adaptation exists inside the harness;
- where S5 policy and ultimate authority remain;
- whether the system forms a reusable constructor or a domain-specific autonomous organization.

## Curation Is Downstream

The Index should remain exhaustive and evidence-oriented. Inclusion in a curated list is not an Index quality score and must not affect an assessment.

The dependency direction is:

```text
upstream project
      ↓
vsm-harness-index
      ↓
assessment / TL;DR / ranking
      ↓
curated domain views (for example awesome-vsm-harness)
```

Curated views may select representative harnesses using criteria such as domain relevance, organizational distinctiveness, evidence quality, and current activity. Those criteria belong to the downstream view, not to the canonical Index ranking.

## Non-Goal

This document does not introduce a new weighted score, ranking dimension, or required catalog field. It documents a stable interpretation layer that downstream consumers can use without changing the Index source-of-truth schema.
