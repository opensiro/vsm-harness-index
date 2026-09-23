# Sources and attribution

## Discovery catalog

`data/catalog.psv` is adapted from **Best of Agent Harnesses**, created by Ryan Alberts and contributors:

- source: <https://github.com/RyanAlberts/best-of-Agent-Harnesses>
- source file used for the cohort: `harnesses.json`
- reviewed revision: `e75e16efa8784f74c01c9004989c38b75ce7debd`
- license: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

The discovery source is used only to form the review cohort and provenance. The index retained in-scope agent-loop projects, excluded the source evaluation category, ordered the historical cohort by GitHub repository creation time, and added AgentLite as a documented local addition.

### Discovery refresh surfaces

For future append-only discovery, **Best of Agent Harnesses** is also useful as a machine-readable feed: the project publishes `harnesses.json`, `llms.txt`, and an MCP server for searching/comparing the maintained collection. These surfaces are discovery inputs only; a project still needs an independent pinned-revision assessment before entering this index.

The GitHub topic **`agent-harness`** is an additional direct repository-discovery surface:

- source: <https://github.com/topics/agent-harness>

Topic membership is used for recall only. It does not establish that a repository is in scope, reviewable, or correctly described as a harness; every candidate still goes through normal deduplication, scope review, and pinned-revision assessment before entering the index.

A second ecosystem reference used for recall is **Awesome Agent Harnesses** by NeuraLiying:

- source: <https://github.com/NeuraLiying/Awesome-Agent-Harnesses>

It is a broader survey of harness research, production harnesses, essays, and talks. No catalog data in this repository is adapted from that survey unless a future change explicitly records such provenance.

### OpenSiro-adjacent OSS discovery

Discovery is intentionally broader than repositories that self-identify as `agent-harness`.

Future repository sweeps should also search for OSS projects that are architecturally adjacent to the OpenSiro stack itself, including:

- agent control planes, governance runtimes, authority/delegation systems and bounded-autonomy middleware;
- multi-agent organizations, agent operating systems, fleet managers, persistent agent teams and recursive/hierarchical agent runtimes;
- agent identity, policy, approval, escalation, audit/evidence and runtime-interception systems when they expose a substantive executable control boundary;
- harness registries, indexes, catalogs, conformance suites, assessment frameworks and machine-checkable agent-organization standards;
- cybernetics/VSM-inspired agent systems even when they use different terminology;
- adjacent standardization projects whose implementation includes a deployable agent/runtime/control organization rather than only prose/specification artifacts.

Useful recall vocabulary includes `agent control plane`, `agent governance`, `agent authority`, `delegation`, `escalation`, `bounded autonomy`, `agent organization`, `autonomous organization`, `agent operating system`, `agent fleet`, `multi-agent hierarchy`, `recursive agents`, `conformance`, `agent standard`, `harness registry`, `harness index`, `assessment framework`, `cybernetics`, `viable system model`, and close functional equivalents.

This broader recall policy does **not** relax intake boundaries. Product-only offerings, papers/specifications without an executable first-party organization, dashboards/proxies without owned runtime/control machinery, benchmarks, observability-only layers and security primitives without a complete operational/control boundary remain adjacent unless direct source inspection proves otherwise. Candidate promotion still requires canonical identity normalization, global deduplication, an immutable review ref and the normal assessment workflow.

## Assessments

Every `assessments/<harness_id>.md` file is independently reconstructed from the named project's primary sources at its pinned `review_ref`. The upstream discovery descriptions and rankings are not used as VSM evidence.

Assessment prose and `data/signatures.psv` are original VSM Harness Index analysis and follow the repository's Apache 2.0 license. Linked projects and quoted or referenced source material retain their own terms.

## Generated comparative views

`TLDR.md` and `RANKINGS.md` combine the adapted discovery cohort metadata with original assessment-derived analysis. They are distributed under CC BY-SA 4.0 together with the adapted `data/catalog.psv` dataset. This does not relicense linked projects or their software.

The legacy `vsm_tldr` column in `data/catalog.psv` is retained only as historical migration material. New or refreshed assessments must be rebuilt from pinned primary sources rather than copied from that column.
