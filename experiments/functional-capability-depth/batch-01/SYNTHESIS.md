# S1 capability comparison — Batch 01 synthesis

Status: **non-normative experiment result**

This synthesis was created only after all six frozen system evidence records were complete. It compares `system A.S1 ↔ system B.S1` on the seven Batch 01 S1 dimensions. It is not a harness ranking, does not assign a weighted score, and does not use non-S1 VSM closure as a prior.

## Evidence discipline

The synthesis uses only the frozen boundaries committed in [`README.md`](README.md):

- [`Pi`](pi.md) — `71dca871bc80b6bc97be37f0ca3189399d651fff`
- [`oh-my-pi`](oh-my-pi.md) — `dbf3afad4894bde827d90f965e77b3fe1c5a95e5`
- [`Ouroboros`](ouroboros.md) — `86806ee123ce8e26cc063cc1a618f975eea64f26`
- [`thClaws`](thclaws.md) — `cd700937a71a391f052438d139b7b1c5a6456755`
- [`Headcount`](headcount.md) — `9cbf34005e3e8a980a6af9b55eb226bd926a62b3`
- [`Henterprise`](henterprise.md) — `0bd56397676462e216f92b5b7800919a3597a99a`

All six canonical S1 states remain `A`. Findings below concern demonstrated S1 capability/evidence at those boundaries only.

## P1 — `Pi.S1 ↔ oh-my-pi.S1`

| S1 dimension | Pairwise outcome | Basis |
| --- | --- | --- |
| operational effectiveness | **stronger evidence for oh-my-pi** | On Coding/SWE evidence, OMP reports several edit/tool comparisons; the MiniMax row explicitly states `2.1×` pass rate with the same weights and same prompt. Pi has no frozen matched task-success experiment. All OMP results remain **self-reported**. |
| environment-interaction fidelity | **stronger evidence for oh-my-pi** | OMP couples executable Hashline/LSP/tool mechanisms to self-reported edit-format outcome deltas. Pi demonstrates argument validation and safe handling of truncated tool calls but no fidelity outcome measurement. Scope: Coding/SWE edit/tool interaction. |
| operational state continuity | **comparable under available evidence** | Both boundaries own resumable/persistent session state and compaction/current-trajectory continuity. No matched interruption/resume stress test orders them. |
| recovery / resilience | **incomparable** | Pi evidence emphasizes context-overflow and truncated-tool-call recovery; OMP evidence emphasizes TTSR course correction and edit-state guards. No common failure-injection condition supports an ordering. |
| operational result assurance | **insufficient evidence** | Pi has action-level validation but no hard task completion gate found. OMP has action-local edit/LSP checks, while separate advisor review is excluded as an automatic S1 bonus. |
| efficiency | **stronger evidence for oh-my-pi** | OMP reports a **self-reported** `−61%` output-token result attributed to elimination of a bad-diff retry loop; Pi exposes accounting/compaction but no matched successful-work resource comparison. Scope: the cited Coding/SWE intervention only. |
| portability / robustness | **stronger evidence for oh-my-pi, limited** | OMP reports positive edit/tool effects across several model families; Pi demonstrates broad provider architecture without a fixed-task cross-provider outcome study. The OMP protocols are not one universal cross-model benchmark, so this remains a limited Coding/SWE portability result. |

**Interpretation:** the common `S1=A` state does not encode the reported edit/tool-effect evidence available for OMP, while Pi serves as the narrow-S1 implementation control. This is not a global Pi-vs-OMP judgment.

## P2 — `oh-my-pi.S1 ↔ Ouroboros.S1`

| S1 dimension | Pairwise outcome | Basis |
| --- | --- | --- |
| operational effectiveness | **incomparable** | OMP's frozen self-reported comparisons are edit/tool-focused; Ouroboros publishes end-to-end Terminal-Bench/OSWorld/SWE-style results. Different units and task conditions prevent a defensible direct ordering. |
| environment-interaction fidelity | **stronger evidence for oh-my-pi on Coding/SWE edit fidelity** | OMP exposes edit-specific comparative claims plus Hashline/LSP implementation evidence. Ouroboros has typed execution/evidence rails and end-to-end traces, but the frozen evidence does not isolate edit/tool fidelity in a matched ablation. |
| operational state continuity | **comparable under available evidence** | Both own substantial current-trajectory persistence/checkpoint mechanisms. No common interruption protocol measures which preserves state more effectively. |
| recovery / resilience | **incomparable** | OMP's stream-rule/edit-state recovery and Ouroboros's provider-death/retry-wall/custody/finalization rails cover different failure classes; no common failure-injection benchmark exists. |
| operational result assurance | **stronger evidence for Ouroboros** | Ouroboros demonstrates a first-party root completion path with host-attested verification/artifact evidence and task acceptance. OMP's independent advisor is not counted; no equivalent frozen hard root completion gate was found. |
| efficiency | **stronger evidence for oh-my-pi on the cited Coding/SWE intervention** | OMP has a **self-reported** token-reduction claim attributed to its edit/retry path; Ouroboros has native usage/cache/budget controls but no matched successful-work resource comparison in the frozen evidence. |
| portability / robustness | **stronger evidence for Ouroboros for whole-task multi-model robustness** | The same Ouroboros harness reports Terminal-Bench runs across multiple model substrates with public artifacts. OMP has multi-model edit claims, but not the same whole-task protocol. Both remain self-reported and domain-scoped. |

**Interpretation:** the pair has different dimension-specific evidence profiles without using Full-A status: OMP has more direct edit-fidelity/efficiency evidence, while Ouroboros has more direct root-assurance and whole-task multi-model evidence.

## P3 — `oh-my-pi.S1 ↔ thClaws.S1`

| S1 dimension | Pairwise outcome | Basis |
| --- | --- | --- |
| operational effectiveness | **stronger evidence for oh-my-pi** | OMP provides frozen self-reported Coding/SWE comparative deltas; no matched thClaws task-success benchmark was found. |
| environment-interaction fidelity | **stronger evidence for oh-my-pi on Coding/SWE edit fidelity** | thClaws has a concrete native parse/dispatch/result loop, but OMP additionally links its edit protocol to reported outcome deltas. This does not order non-coding environment interaction. |
| operational state continuity | **comparable under available evidence** | Both own resumable state and compaction/current-trajectory mechanisms. No common continuity stress test exists. |
| recovery / resilience | **incomparable** | OMP and thClaws demonstrate different recovery classes: TTSR/edit-state correction versus provider retry/context rescue/max-token continuation. |
| operational result assurance | **stronger evidence for thClaws** | thClaws `/goal --require` supplies a first-party hard artifact-existence condition that rejects `MarkGoalComplete` while unmet. OMP has action-local checks but no comparable frozen hard task-completion gate. This does not claim semantic correctness of the required artifact. |
| efficiency | **stronger evidence for oh-my-pi on the cited Coding/SWE intervention** | OMP reports a token-reduction claim attributed to its retry path; thClaws provides budgets/caps but no comparative resource-per-success result. |
| portability / robustness | **insufficient evidence** | Both have broad provider/platform architecture. OMP has model-specific edit results, but the available protocols are not aligned enough with thClaws to establish comparative robustness. |

## P4 — `oh-my-pi.S1 ↔ Headcount.S1`

| S1 dimension | Pairwise outcome | Basis |
| --- | --- | --- |
| operational effectiveness | **stronger evidence for oh-my-pi** | OMP has self-reported Coding/SWE harness-effect comparisons; Headcount has no matched Claude Code baseline with/without its skills. |
| environment-interaction fidelity | **stronger first-party evidence for oh-my-pi** | OMP owns material edit/tool control paths. Headcount explicitly does not execute actions itself; tool fidelity is primarily inherited from Claude Code. |
| operational state continuity | **capability primarily inherited rather than first-party for Headcount** | OMP owns session/current-trajectory mechanisms; no Headcount-owned session runtime was found. Claude Code supplies Headcount's live trajectory state. |
| recovery / resilience | **stronger first-party evidence for oh-my-pi** | OMP exposes executable recovery mechanisms. Headcount contains recovery/debugging procedures, but no controlled effect separates them from host execution. |
| operational result assurance | **incomparable** | Headcount owns an explicit completion-verification procedure but relies on Claude Code to execute/enforce it; OMP owns action-level guards but lacks an equivalent frozen hard completion gate. No common outcome assay orders the two forms. |
| efficiency | **stronger evidence for oh-my-pi on the cited Coding/SWE intervention** | OMP reports token reduction attributed to its edit/retry path; Headcount has no comparable resource experiment. |
| portability / robustness | **stronger evidence for oh-my-pi, limited** | OMP reports multi-model edit effects and owns a multi-provider runtime. Headcount's frozen distribution is Claude Code-specific, with no alternate-host task result. |

**Ownership result:** both remain canonical `S1=A`; the capability accounting nevertheless distinguishes a native/mixed runtime path from a host-inherited execution path.

## P5 — `Headcount.S1 ↔ Henterprise.S1`

| S1 dimension | Pairwise outcome | Basis |
| --- | --- | --- |
| operational effectiveness | **insufficient evidence** | Neither frozen repository provides a matched host run isolating the organizational layer's effect. |
| environment-interaction fidelity | **capability primarily inherited rather than first-party for both** | Claude Code executes Headcount actions; Hermes executes Henterprise actions. The two hosts are different and no host-matched fidelity evidence exists. |
| operational state continuity | **capability primarily inherited rather than first-party for both** | Neither overlay owns the underlying live session/runtime state at the frozen boundary. |
| recovery / resilience | **insufficient evidence** | Both contain procedures relevant to debugging/recovery, but no controlled failure/recovery traces isolate their effect from their hosts. |
| operational result assurance | **comparable under available evidence at the procedural layer** | Henterprise preserves the Headcount completion-verification procedure in Hermes format. In both cases the first-party layer requires real checks/output review while host execution remains external. Live runtime effect is not demonstrated, and Henterprise's migration report explicitly lacks a live Hermes load. |
| efficiency | **insufficient evidence** | Neither has a comparable successful-work resource study. |
| portability / robustness | **incomparable** | The Headcount→Henterprise migration demonstrates static format/contract portability, not matched task capability across Claude Code and Hermes. Henterprise's live Hermes integration remained unverified in the frozen migration report. |

**Replication result:** the same ownership rule applies consistently across both overlays without changing either canonical `S1=A` state.

## P6a — `Ouroboros.S1 ↔ Headcount.S1`

| S1 dimension | Pairwise outcome | Basis |
| --- | --- | --- |
| operational effectiveness | **stronger evidence for Ouroboros** | Ouroboros has self-reported matched-model/public benchmark artifacts; Headcount has no matched host-with/without-overlay outcome study. |
| environment-interaction fidelity | **stronger first-party evidence for Ouroboros** | Ouroboros owns a direct typed execution/evidence path; Headcount's action execution is primarily inherited from Claude Code. |
| operational state continuity | **stronger first-party evidence for Ouroboros** | Ouroboros owns task results, artifacts, retained delivery candidates, and checkpoints; Headcount relies on host session state. |
| recovery / resilience | **stronger first-party evidence for Ouroboros** | Ouroboros exposes explicit first-party provider/finalization/error recovery rails; Headcount has no isolated runtime recovery effect. |
| operational result assurance | **stronger evidence for Ouroboros** | Ouroboros's root completion path consumes host-attested evidence/acceptance. Headcount's completion-verification procedure is first-party guidance but host-executed and instruction-enforced. Independent S3* topology is not used for this ordering. |
| efficiency | **insufficient evidence** | Ouroboros owns resource accounting/control, but neither side supplies aligned resource-per-success evidence. |
| portability / robustness | **stronger evidence for Ouroboros, limited** | Ouroboros reports same-harness task results across multiple model substrates; Headcount has no alternate-host outcome evidence. The Ouroboros result remains self-reported and task-family scoped. |

## P6b — `Ouroboros.S1 ↔ Henterprise.S1`

| S1 dimension | Pairwise outcome | Basis |
| --- | --- | --- |
| operational effectiveness | **stronger evidence for Ouroboros** | Ouroboros has self-reported matched/public benchmark artifacts; Henterprise has no live Hermes outcome benchmark and no with/without-overlay run. |
| environment-interaction fidelity | **stronger first-party evidence for Ouroboros** | Ouroboros owns a material direct execution path; Henterprise's live action path is primarily inherited from Hermes. |
| operational state continuity | **stronger first-party evidence for Ouroboros** | Ouroboros owns current-task persistence/checkpoint mechanisms; Henterprise does not own the Hermes session runtime. |
| recovery / resilience | **stronger first-party evidence for Ouroboros** | Ouroboros demonstrates explicit runtime failure rails; Henterprise has no isolated runtime recovery evidence. |
| operational result assurance | **stronger evidence for Ouroboros** | Ouroboros has first-party root acceptance/evidence gates. Henterprise supplies a verification procedure but relies on Hermes for execution and had no live Hermes integration proof in the migration environment. |
| efficiency | **insufficient evidence** | No aligned resource-per-success comparison exists. |
| portability / robustness | **stronger evidence for Ouroboros, limited** | Ouroboros reports whole-task operation across multiple model substrates. Henterprise demonstrates static migration to Hermes, not observed task-capability survival across hosts. |

## Batch-level findings

The batch supports the narrow research hypothesis: canonical `S1=A` does not by itself encode all demonstrated S1 capability properties. The useful distinctions are dimension-specific and survive the explicit ownership boundary.

Concrete examples:

- OMP's frozen Coding/SWE evidence contains self-reported comparative edit/tool and token effects that are absent from the Pi control record; the MiniMax row explicitly controls weights and prompt.
- thClaws demonstrates a native hard artifact-existence completion gate (`/goal --require`) that is a different S1 assurance mechanism from OMP's action-local guards.
- Ouroboros demonstrates a first-party root task acceptance/evidence path, while Headcount and Henterprise supply task procedures over external execution hosts.
- Headcount and Henterprise replicate the ownership-accounting case: visible operation can remain canonically autonomous S1 while much execution capability is `inherited` and specific first-party procedures are `mixed`.

These statements do **not** imply a harness-wide order.

## Success-criteria check

1. **At least four systems yield enough primary evidence:** met. Pi, OMP, Ouroboros, and thClaws expose substantial frozen first-party implementation evidence; Headcount and Henterprise additionally provide usable ownership-boundary evidence.
2. **At least one same-state pair exposes a capability distinction:** met at the level of demonstrated S1 mechanisms/effects, including OMP↔Pi edit/efficiency evidence and Ouroboros↔overlay result-assurance ownership.
3. **Difference survives ownership accounting:** met. Inherited host execution is not credited as Headcount/Henterprise-native, while their first-party verification procedures remain `mixed`.
4. **Non-S1 coverage excluded:** met. Full-A, S3*, S4, and S5 states are not used as S1 priors.
5. **Applied domains remain projections:** met. Coding/SWE and desktop-operation findings remain explicitly scoped.
6. **At least one honest incomparable result:** met in multiple dimensions, including recovery across Pi/OMP and OMP/Ouroboros, and portability across Headcount/Henterprise.
7. **Reconstructable from frozen evidence:** met structurally. Each outcome above points back to a per-system record containing frozen refs, ownership labels, evidence type, unsupported claims, and stable primary links.

## Interpretation boundary

Batch 01 supports continuing per-function capability research, but it does not yet justify a normative S1 capability score or a cross-function scoring framework. The strongest distinctions mix different evidence classes: self-reported comparative benchmark claims, executable mechanisms, and ownership-boundary evidence. A future replication should prefer common task/failure protocols across more pairs before treating the procedure as stable enough for normative promotion.

Accordingly, this batch does not modify canonical assessments and does not promote these S1 dimensions into S2/S3/S3*/S4/S5 criteria.
