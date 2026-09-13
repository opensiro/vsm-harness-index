# VSM Harness Index

VSM Harness Index maps and compares real agent harnesses according to the organizational functions described by the [VSM Harness Profile](../vsm-harness-profile/PROFILE.md).

This is an organizational comparison, not a ranking and not a harness specification. The discovery cohort is adapted from [Best of Agent Harnesses](SOURCES.md) under CC BY-SA 4.0; detailed assessments use project evidence and may revise its provisional VSM interpretation.

## VSM TL;DR

Browse the separate [VSM TL;DR catalog](TLDR.md): 81 autonomy-centered
fingerprints, newest first; one non-agentic candidate is excluded. Included rows have explicit S1, S2, S3, S3*, S4, and S5 fields.

| Symbol | State | Meaning |
| --- | --- | --- |
| `A` | Agent-owned | Ready agent-owned enactment is available through the standard documented setup. |
| `C` | Composable | A first-party primitive is supplied, but the developer must compose the agent, authority, or feedback loop. |
| `P` | Parent-assisted | Runtime closure returns a parent identity or ultimate-policy decision to subsequent operation; valid only for S5. |
| `—` | No supplied path | The review boundary supports no material first-party path; this is not proof that one can never be built. |
| `?` | Unknown | The reviewed primary evidence is insufficient to establish the state. |

## Scope

The current cohort contains 82 candidates: 81 with an autonomous decision/action loop in the standard documented setup and one retained NO AGENTIC VSM exclusion. Four entries currently have detailed evidence-backed assessments. Catalog coverage is not evidence depth; new assessments should replace catalog-only hypotheses with primary-source findings.

## Repository data flow

```text
source catalog --> data/catalog.psv ---------------------> TLDR.md
                         ^                                  ^
assess-vsm-harness --> assessments + evidence --> entries -+
```

The JSON format is internal to this index and is not a harness specification. CSVs are derived and must be reproducible. Human-readable entry pages carry context that flat tables cannot. All new or refreshed assessments must use `vsm-skills/skills/assess-vsm-harness`.

## Contents

- [METHODOLOGY.md](METHODOLOGY.md) — index-specific publication rules; assessment logic lives in `vsm-skills`
- [SOURCES.md](SOURCES.md) — discovery provenance, modifications, and license attribution
- [TLDR.md](TLDR.md) — newest-first, six-system VSM fingerprint index
- [data/catalog.psv](data/catalog.psv) — ordered discovery cohort and provisional TL;DR
- [entries/](entries/) — human-readable mappings and citations
- [data/assessments/](data/assessments/) — current synchronized evidence artifacts
- `vsm-skills/skills/assess-vsm-harness/scripts/upsert_harness.py` — validates assessment artifacts and regenerates internal CSV projections
- [scripts/render_readme.py](scripts/render_readme.py) — regenerates the TLDR projection
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to add or update an entry

## License

No repository-wide license has been selected. The adapted discovery dataset and its rendered TL;DR table are available under CC BY-SA 4.0 as documented in [SOURCES.md](SOURCES.md). Do not assume that license applies to other repository content.
