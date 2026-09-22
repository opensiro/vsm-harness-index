# oh-my-pi — S1 capability evidence

## Frozen boundary

- repository: `can1357/oh-my-pi`
- review_ref: `dbf3afad4894bde827d90f965e77b3fe1c5a95e5`
- canonical S1 state: `A`
- canonical assessment: [`assessments/oh-my-pi.md`](../../../assessments/oh-my-pi.md)

## Credited S1 boundary

- first-party S1 actor / loop: the OMP coding-agent runtime and its built-in tool/edit/session surfaces;
- environment-facing action path: model decision → OMP tool protocol → first-party edit/search/shell/LSP/DAP integration → environment result → active agent trajectory;
- external substrates: model/provider inference, language/debug servers where used, compilers/interpreters and operating-system services, remote web/tool services, and optional external memory backends.

OMP materially transforms several inherited substrates, especially language-server and model outputs; those paths are marked `mixed` rather than credited wholesale as native.

## S1 evidence

| S1 dimension | Ownership | Evidence domain | Evidence type | Observation | Confidence |
| --- | --- | --- | --- | --- | --- |
| operational effectiveness | `mixed` | Coding / SWE | maintainer-reported comparative/ablation claims, **self-reported** | The frozen README reports edit/tool outcome changes attributed to harness mechanisms: Grok Code Fast 1 `6.7% → 68.3%`, Gemini 3 Flash `+5 pp` versus `str_replace`, and MiniMax `2.1×` pass rate. Only the MiniMax row explicitly says “same weights, same prompt.” The frozen repository does not independently reproduce the evaluation protocol, so all remain self-reported. | medium |
| environment-interaction fidelity | `mixed` | Coding / SWE | self-reported comparative claims + executable implementation | The same README reports edit-format gains across multiple models. First-party Hashline state stores full-file snapshots and guards edit state; OMP also owns LSP auto-detection/integration while the language server's semantic intelligence remains external. This is more direct than a feature-count claim because the edit path has attributed outcome deltas, but those deltas remain self-reported. | medium |
| operational state continuity | `native` | Coding / SWE | primary technical documentation | OMP retains Pi-style persistent sessions and adds first-party persistent project memory/session facilities. Session state is resumable and operational context can survive compaction; optional external memory backends are not credited as native. | medium |
| recovery / resilience | `native` | Coding / SWE | executable code path + primary documentation | Time-Traveling Stream Rules can be inspected/tested through the real matching pipeline and are designed to abort an off-policy stream, inject a rule, and retry. Hashline edit state also supplies action-local guards such as no-op/stale-state protection. No common failure-injection benchmark against another cohort member was found. | high |
| operational result assurance | `unclear` | Coding / SWE | implementation review | Hashline and LSP integration provide action-local validation signals, but no frozen first-party hard task-completion gate equivalent to a required test/check receipt was found. The separate advisor/review surface is not credited automatically because independent review is S3* topology. **insufficient evidence** for stronger task-level S1 assurance. | medium |
| efficiency | `mixed` | Coding / SWE | maintainer-reported comparative claim, **self-reported** | The frozen README reports `−61%` output tokens for Grok 4 Fast and attributes the reduction to the retry loop on bad diffs disappearing. The model is external while the edit protocol is first-party; the evidence is therefore `mixed` and self-reported. The frozen README does not expose enough protocol detail to treat this as independently reproduced efficiency evidence. | medium |
| portability / robustness | `mixed` | Coding / SWE | multi-model self-reported evidence + technical documentation | OMP reports positive edit/tool effects on Grok, Gemini, and MiniMax and ships the same runtime across macOS, Linux, and Windows with many providers. This is limited evidence that the operational mechanism is not tied to one model, but the reported evaluations are not one identical cross-model protocol and do not support universal robustness. | low-medium |

## Specialized-domain witnesses

- Coding / SWE: primary evidence context; edit/tool behavior, LSP/DAP integration, Hashline, and the self-reported harness comparisons all live here.
- Research / Science: web/PDF tooling exists, but no frozen controlled research-task result is used here. **insufficient evidence** for a comparative projection.
- Government / Public Administration: **insufficient evidence**.
- other applicable domains: debugger, shell, and general tool integrations are architecture evidence only unless paired with outcome evidence.

## Controlled / benchmark evidence

All values below are maintainer-reported in the frozen README and are therefore labeled **self-reported**; the record does not assume a stronger experimental control than the README documents:

- Grok Code Fast 1: `6.7% → 68.3%`, attributed to the edit format;
- Gemini 3 Flash: `+5 pp` versus `str_replace`;
- Grok 4 Fast: `−61%` output tokens, attributed to removal of the bad-diff retry loop;
- MiniMax: `2.1×` pass rate, explicitly described as “same weights, same prompt.”

These are useful harness-effect witnesses but are not treated as independently verified benchmark results.

## Unsupported or non-comparable claims

- The README phrase “most capable agent surface” is a maintainer claim and is not used as evidence.
- `31` tools, LSP/DAP operation counts, or code size are not capability scores.
- Language-server intelligence is not OMP-native; OMP owns the integration/control path, hence `mixed` where that intelligence contributes.
- Advisor/reviewer existence is not converted into S1 assurance without an observed S1 completion effect.
- Coding-specific edit gains are not generalized into universal S1 superiority.

## Primary evidence

- [`README.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/README.md)
- [`packages/coding-agent/src/edit/store.ts`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/packages/coding-agent/src/edit/store.ts)
- [`packages/coding-agent/src/commands/ttsr.ts`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/packages/coding-agent/src/commands/ttsr.ts)
- [`docs/lsp-config.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/docs/lsp-config.md)
