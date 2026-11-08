# Index public showcase QA — 2026-11-08

**Status: PARTIALLY_VERIFIED — not yet PUBLIC_SHOWCASE_READY.**

**Owning issue:** [#3018](https://github.com/opensiro/vsm-harness-index/issues/3018)  
**Readback baseline:** Index `main@13fcb356e3d577c54d7c35b5abf1abfbe531b33f` after merged [#3019](https://github.com/opensiro/vsm-harness-index/pull/3019) and [#3020](https://github.com/opensiro/vsm-harness-index/pull/3020). This dated report is a QA snapshot, **not** a new normative assessment or a durable claim about future corpus state. Subsequent readback on an integrated commit should be recorded on #3018.

## Reproducible visitor walkthrough

1. Start at [README](../README.md) in the `I'm human` section. Choose the [web introduction](https://opensiro.com/vsm-index.html), [paginated monitor](https://opensiro.com/harness-monitor.html), [full-table edition](https://opensiro.com/harness-server.html), or GitHub-native [TLDR](../TLDR.md) / [Rankings](../RANKINGS.md).
2. Open a harness name in TLDR or Rankings: it now leads to the **canonical Index assessment**, while the adjacent `source` link leads to the upstream repository. Both remain separate.
3. Compare [Henterprise](../assessments/he/henterprise.md) (Full-A: `A A A A A A`; pinned `193e8fdac0d17abf833ab68e5179b273a6084e4c`) with [Onion Harness](../assessments/on/onion-harness.md) (`A A P — P P`; pinned `dc2be116eddad9c45018d0d8590fa6cc96387bfe`). Read their review boundary, supporting evidence, decision ownership, uncertainties and limits. Pinned upstream commits: [Henterprise](https://github.com/humbertobellor/henterprise/commit/193e8fdac0d17abf833ab68e5179b273a6084e4c), [Onion Harness](https://github.com/chenofchina/onion-harness/commit/dc2be116eddad9c45018d0d8590fa6cc96387bfe).
4. Interpret functions using the authoritative [Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md), states and ranking using [Skills synthesis](https://github.com/opensiro/vsm-harness-skills/blob/main/SYNTHESIS.md), corpus states using [metrics](../METRICS.md) and provenance/licensing via [SOURCES](../SOURCES.md). **Coverage is not a product-quality, safety, maturity or viability score.**

## Evidence and acceptance checklist

| Check | Result | Evidence / limit |
| --- | --- | --- |
| Human entry navigation to web and GitHub-native views | **PASS** (source/link check) | Merged #3019; `README.md` links to 3 dedicated web pages, TLDR, Rankings, Full-A, metrics and contributions. Web page GET returned HTTP 200 on 2026-11-08. |
| Explanation of S1/S2/S3/S3*/S4/S5 and A/C/P/—/? modes | **PASS** (text/source review) | Authoritative Profile and Skills links; README human summary and website [autonomy key](https://opensiro.com/vsm-index.html#state-key). This QA does not redefine semantics. |
| Distinguish publication states and Full-A | **PASS** | `data/metrics.json`, `METRICS.md` and `FULL_A.md`: 1,060 included; 1,148 canonical (88 excluded); 9 proposed; 88 reassessment events; 2 Full-A. No score or certification implied. |
| Canonical and upstream traceability | **PASS** | Merged #3020 changed renderer plus all three generated views. Exact local check found **1,060 TLDR**, **1,060 Rankings**, **2 Full-A** rows, with all canonical target files present, source links retained, unique anchors, no non-included rows. |
| Contrasting pinned examples | **PASS** | Henterprise and Onion Harness canonical assessments; both declared upstream pinned commits were retrieved from GitHub. |
| First-visit representative HTTP links | **PASS** (sample only) | GitHub README views, example assessments and pinned upstream trees responded HTTP 200; 3 website interfaces and homepage responded HTTP 200. Does **not** establish all third-party links globally or fully working frontend JavaScript. |
| Generated views, metrics, provenance, exclusions | **PASS** | `validate_tldr.py` 1,157 standalone files; `check_index.py` 1,148 canonical, 9 proposed, 88 reassessment events. Generated files unchanged by check mode, row link targets match `included` states. |
| Full documented validation | **PASS** | `render_tldr.py --check`, `render_full_a.py --check`, `render_metrics.py --check`, `sync_metrics_readme.py --check`, `check_index.py`, `validate_tldr.py`, **87 unit tests PASS** on integrated baseline 13fcb356; #3020 CI `validate` success (includes pinned Skills structural checker, analytics, stars and provenance). New PR CI must run separately. |
| Attribution and licensing | **PASS** (documentation) | [SOURCES.md](../SOURCES.md): adapted discovery catalog and generated comparisons under CC BY-SA 4.0; original assessment prose and repository code/docs Apache 2.0; upstream projects retain their own licenses. README exposes provenance. |
| Published website compared with Index source | **PARTIAL** | Live `harness-monitor.html` and `harness-server.html` returned 200, showed corpus count 1,060 and recorded generator source `opensiro/vsm-harness-index@8ef26789403d7cf682e67dcc7985a0317a76bb00`, **older than readback** `13fcb356`. No change to corpus data occurred in #3019/#3020, but a future website sync should be verified in its owning repo. |
| Actual public GitHub desktop + narrow/mobile interaction, keyboard/screen reader basics | **NOT TESTED** | HTTP/status and Markdown source review are not equivalent to browser interaction, responsive rendering, or screen-reader testing. Requires a working interactive browser runtime and accessibility QA. |
| Full third-party link crawl and large-table performance | **NOT TESTED** | Representative links checked, not all 1,060 upstream links; tables are large. No latency claim or accessibility certification. |

## Boundaries / follow-up

The public source-navigation improvements are reviewable and landed via #3019 and #3020. No canonical assessment, pinned evidence, historical provenance, publication state, ranking algorithm or Methodology meaning was changed. This report and the README entry enhancements only document verified paths. Keep #3018 **open** until actual browser/mobile accessibility checks and website synchronization/readback are performed, and record the final integrated commit on the issue before changing the status to `PUBLIC_SHOWCASE_READY`.
