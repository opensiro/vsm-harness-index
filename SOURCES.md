# Sources and attribution

## Discovery catalog

`data/catalog.psv` is adapted from **Best of Agent Harnesses**, created by Ryan
Alberts and contributors:

- source: <https://github.com/RyanAlberts/best-of-Agent-Harnesses>
- source file: `harnesses.json`
- reviewed revision: `e75e16efa8784f74c01c9004989c38b75ce7debd`
- license: [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)

Changes made by VSM Harness Index:

- retained projects marked as owning an agent loop (`autonomy_rank > 0`);
- excluded the source's evaluation category from this operational cohort;
- sorted the cohort by GitHub repository creation timestamp;
- added AgentLite from its primary repository because it is an in-scope harness absent from the source catalog;
- replaced editorial rankings and descriptions with original, autonomy-centered VSM
  TL;DR analysis;
- retained all 81 discovery rows at the reviewed revision, producing 82
  candidates after the local addition; the autonomy TLDR excludes candidates whose
  standard distribution does not establish an autonomous decision/action loop.

The adapted `data/catalog.psv` dataset and its rendered TL;DR table are made
available under CC BY-SA 4.0. This does not relicense linked projects, software, or other repository content.

The upstream catalog is used only for discovery. Each published fingerprint is
reconstructed from project documentation and source at the pinned review ref.
