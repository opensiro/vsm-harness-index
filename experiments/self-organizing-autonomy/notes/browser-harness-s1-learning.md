# Browser Harness — S1 learned-regulator candidate note

**Status:** exploratory research note; no experimental finding  
**Target repository:** `browser-use/browser-harness`  
**Target revision:** `afbcc381b963040c19627d788e40c7e7663171ee`  
**Canonical baseline:** `opensiro/vsm-harness-index` assessment `browser-harness.md`  
**Released baseline vector:** `A C — — — —`  
**Experimental protocol consulted:** `opensiro/vsm-harness-skills@50cb4a53c3ad41ecd08d188253ec6ad27e0cf979`  
**Recorded:** 2026-09-22

This note records why Browser Harness is a promising real-system candidate for the experimental self-organizing autonomy `S` corpus. It is **not** a fixture packet, independent review, synthesis, canonical reassessment, or `S` finding.

The working question is deliberately per-function:

> Can the already autonomous Browser Harness S1 endogenously increase its own operational decision/feedback repertoire from browser-task experience, integrate the change within the declared harness boundary, and later absorb relevant browser variety through the materially changed repertoire without an external constructor supplying the missing operational logic?

## Released eligibility

The canonical assessment at the same target revision records:

| Function | Released state | Experimental eligibility |
| --- | --- | --- |
| S1 | `A` | eligible |
| S2 | `C` | ineligible under released-`A` prerequisite |
| S3 | `—` | ineligible |
| S3* | `—` | ineligible |
| S4 | `—` | ineligible |
| S5 | `—` | ineligible |

Therefore this note concerns **S1 only**. It does not propose `S` for S2-S5 or S3* and does not change the released vector.

## Why Browser Harness is interesting

Browser Harness explicitly separates protected core browser machinery from an agent-editable operational workspace.

The repository README describes the intended loop as:

```text
agent encounters missing browser helper
→ agent writes the helper while working
→ helper becomes available
→ browser task closes
```

Primary evidence:

- `README.md` — states that the agent writes missing helpers as it works and that the harness improves with each task:  
  <https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/README.md>
- `agent-workspace/agent_helpers.py` — first-party agent-editable extension point for task-specific browser primitives:  
  <https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/agent-workspace/agent_helpers.py>
- `src/browser_harness/helpers.py` — loads the agent workspace helpers into the operational helper surface:  
  <https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/src/browser_harness/helpers.py>
- `AGENTS.md` — states that an agent operating the harness edits `agent-workspace/agent_helpers.py` and `agent-workspace/domain-skills/`:  
  <https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/AGENTS.md>

Architecturally, this is stronger than generic self-editing because the editable surface is an intended part of the operating harness and the generated repertoire can be loaded into later operation.

However, the experimental protocol explicitly rejects the shortcut:

```text
self-editing / adding tools / generating a skill ≠ S by itself
```

A positive witness still needs material repertoire inadequacy, endogenous reconstruction, legitimate integration, post-change closure, and an external-constructor check.

## Candidate path A — executable helper extension

The cleanest architectural candidate is the agent helper loop.

Possible transition:

```text
before
S1 encounters browser disturbance D
→ shipped helper repertoire cannot directly absorb D

adaptation
→ operating agent recognizes a missing primitive
→ operating agent constructs helper R inside agent-workspace
→ harness loader integrates R

after
same or equivalent disturbance class
→ S1 can use R as part of its operational repertoire
→ disturbance closes without the previously missing construction
```

### What this already establishes

- There is an explicit first-party mutable operational extension surface.
- The operating agent is authorized to write into that surface.
- The first-party runtime imports the resulting helpers.
- The repository presents missing-helper construction as part of normal operation rather than maintainer-only repository development.

### What is still missing for a positive fixture

A frozen trace must prove that a concrete missing helper represents **material functional repertoire inadequacy**, not merely a convenience wrapper over actions the agent could already perform unchanged.

The trace should reconstruct:

1. disturbance class;
2. prior operational repertoire;
3. evidence that the prior repertoire was insufficient;
4. recognition owner;
5. newly constructed helper;
6. authorization path;
7. integration into later harness operation;
8. post-change closure;
9. absence of an external constructor supplying the missing browser logic.

## Candidate path B — learned domain regulator

The second path may be stronger conceptually because Browser Harness stores field-tested site-specific decision rules that future agent runs are instructed to consume before rediscovering an approach.

Relevant first-party behavior:

- `CONTRIBUTING.md` says domain skills capture selectors, flows and edge cases the agent would otherwise have to rediscover and instructs contributors to let the harness write skills while it works:  
  <https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/CONTRIBUTING.md>
- `SKILL.md` says that, when domain skills are enabled, a site-specific task must read the matching domain-skill files before inventing an approach:  
  <https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/SKILL.md>
- `goto_url()` can surface matching domain-skill files from the agent workspace:  
  <https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/src/browser_harness/helpers.py>

This creates a candidate experience-to-regulation loop:

```text
task N
→ unknown browser/site variety
→ agent experiments
→ agent discovers a more reliable operating rule R
→ R is persisted as a domain skill

task N+1
→ equivalent site/disturbance class
→ matching skill is surfaced/read before inventing an approach
→ R changes later operational choice
→ relevant variety is absorbed with the changed repertoire
```

The key experimental question is whether this is merely memory/documentation or a **material change in the S1 decision/feedback repertoire** that alters later closure.

## Strong in-boundary candidate: Expedia URL-first regulator

At the pinned target revision, the repository contains a field-tested Expedia domain skill:

<https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/agent-workspace/domain-skills/expedia/automation.md>

It records a concrete inadequacy:

- date-picker interaction is repeatedly unreliable;
- coordinate clicks dismiss or mis-target the picker;
- multiple strategies were tried;
- dozens of retry attempts failed.

It then records a materially different operational rule:

```text
avoid the failing date-picker interaction path
→ encode the search state directly in URL parameters
→ use UI interaction only for the remaining cases
```

The domain skill therefore contains the outline of an escalation-boundary-like shift inside S1:

```text
before
browser task requires date selection
→ local interaction strategy repeatedly fails

after learned regulator
same class of task
→ URL-first path bypasses the failing interaction mechanism
→ task can continue under a different local regulator
```

The underlying domain skill entered the repository through merged PR #218:

<https://github.com/browser-use/browser-harness/pull/218>

This is a stronger candidate than the generic helper example because the evidence explicitly describes repeated operational failure and a changed strategy rather than only a missing convenience function.

### Remaining problem

The merged repository artifact proves that the changed regulator exists and was field-tested, but the future fixture still needs a judgment-safe provenance chain establishing that the **operating harness/agent itself formed the missing functional logic** rather than a human contributor supplying it after the fact.

That provenance question is the main unresolved external-constructor check.

## Corroborating development evidence outside the pinned fixture boundary

Later/open repository-development artifacts provide useful research leads but MUST NOT be silently imported into a fixture frozen at `afbcc381...`.

Example: PR #675 documents a Google Sheets failure mode where repeated runs reported success while autocomplete silently corrupted one cell per run. The proposed learned rule changes the write procedure and requires read-back verification:

<https://github.com/browser-use/browser-harness/pull/675>

This is conceptually close to the experimental pattern:

```text
repeated latent failure
→ detect stable limit of current write regulator
→ construct new write/verify regulator
→ use changed regulator on later writes
```

Because PR #675 is not part of the pinned target revision and its merge state differs from the standard-distribution boundary, it is **corroborating discovery evidence only**, not fixture evidence for this note.

## Candidate experimental screen

Current research interpretation, before an independent frozen review:

| Candidate-test field | Preliminary note |
| --- | --- |
| Released `A` prerequisite | satisfied for S1 by canonical assessment |
| Material in-domain adaptation pressure | strong candidate evidence, especially Expedia |
| Prior repertoire inadequacy | strong candidate evidence: repeated failed interaction attempts |
| Endogenous functional improvement | plausible but provenance must be reconstructed |
| Legitimate authorization | strong architectural evidence for agent-workspace mutation |
| Integration | strong architectural evidence for helper/domain-skill consumption |
| Post-change closure | plausible; needs trace-quality before/after evidence |
| External-constructor check | unresolved and decisive |
| Strong recursive witness | no evidence expected; not required for per-function S |

Do **not** convert this table into an experimental finding.

## Why this fixture would be valuable

Browser Harness could test a particularly important distinction in the experimental `S` proposal:

```text
functional self-improvement
≠ recursive viable-system reproduction
```

A positive S1 witness could exist with:

```text
S1=A baseline
→ operating experience exposes insufficient local regulator
→ system constructs/persists changed local regulator
→ later local operation absorbs equivalent variety differently
```

without establishing autonomous S3, S3*, S4, S5, or a newly viable recursive subsystem.

This would directly test the protocol claim that recursive reorganization is an optional realization/diagnostic dimension rather than a prerequisite for per-function `S`.

## Recommended next step

If promoted from note to fixture candidate:

1. freeze a judgment-free packet at one exact Browser Harness revision;
2. pin the exact Skills experimental protocol revision;
3. keep the canonical `A C — — — —` baseline separate;
4. select one concrete S1 transition rather than combining unrelated examples;
5. prefer a trace with explicit before-failure, endogenous construction, integration and later reuse;
6. perform the external-constructor check explicitly;
7. run two independent reviews under the normal experiment independence protocol;
8. record `strong_recursive_witness` separately.

A good fixture title would be:

> **Browser Harness — learned S1 regulator / persistent operational repertoire**

Possible sub-witnesses to investigate:

- executable `agent_helpers.py` self-extension;
- experience-derived persistent domain-skill regulation.

Until that frozen review exists, the correct status of this artifact remains:

```text
research note
not a fixture finding
not canonical S
```
