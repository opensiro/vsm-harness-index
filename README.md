# VSM Harness Index

VSM Harness Index maps and compares real agent harnesses according to the organizational functions described by the [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md).

This is an organizational comparison, not a ranking and not a harness specification. The discovery cohort is adapted from [Best of Agent Harnesses](SOURCES.md) under CC BY-SA 4.0; fingerprints are independently reconstructed from pinned primary project sources.

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

The current cohort contains 82 candidates: 81 with an autonomous decision/action loop in the standard documented setup and one retained NO AGENTIC VSM exclusion. Every fingerprint records a pinned review ref and review date in the catalog.

## Repository data flow

```text
primary project sources --> data/catalog.psv --> TLDR.md
```

`data/catalog.psv` is the single source of truth and `TLDR.md` is its reproducible projection. All new or refreshed reviews must use [`assess-vsm-harness`](https://github.com/opensiro/vsm-skills/tree/main/skills/assess-vsm-harness).

## Contents

- [METHODOLOGY.md](METHODOLOGY.md) — index-specific publication rules; assessment logic lives in `vsm-skills`
- [SOURCES.md](SOURCES.md) — discovery provenance, modifications, and license attribution
- [TLDR.md](TLDR.md) — newest-first, six-system VSM fingerprint index
- [data/catalog.psv](data/catalog.psv) — ordered discovery cohort and reviewed TL;DR
- [scripts/render_tldr.py](scripts/render_tldr.py) — regenerates the TLDR projection
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to add or update an entry

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The adapted discovery dataset in `data/catalog.psv` and its generated `TLDR.md` projection are licensed under [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt); attribution and modifications are documented in [SOURCES.md](SOURCES.md). Linked projects retain their own terms.
