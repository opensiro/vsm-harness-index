# Batch 02 execution environment

Status: **TERMINALLY UNAVAILABLE BEFORE FIRST SEMANTIC RUN**

This artifact records the Phase 2 execution-membrane preflight for issue #354. Phase 1 classified all six frozen systems as mechanically eligible. No candidate process was launched and no task result or evaluator result was observed.

## Repository boundary

- Batch 02 design merge: `2c48827a2064a96b0d78859b200316ce879feba2`.
- Phase 1 branch commit: `1ca5369cad78efa37616a4284d5d5b05d1e12666`.
- `main` at Phase 1 preflight: `43f6ed035b8536b60aa1d4b75ba82ec785da6b0a`.
- `main` recheck during Phase 2 preflight: `4ef595d58af4fa06ee2b3e7441c595d29745fdd1`.
- The intervening `main` commit concerns the BossConsole assessment/metrics and does not modify Batch 02 design artifacts.

## Observed execution runtime

The available execution runtime reported:

- OS: Debian GNU/Linux 13 (trixie), Debian 13.3.
- Architecture: `x86_64`.
- Kernel: `6.18.44`.
- Python: `3.13.5`.
- Node.js: `v22.16.0`.
- npm: `10.9.2`.
- uv: `0.10.0`.
- Git: `2.47.3`.
- OpenSSL: `3.5.5`.
- glibc: `2.41`.
- Docker: unavailable.
- Podman: unavailable.
- Rust toolchain: unavailable.
- Execution-environment fingerprint: `sha256:01020e2167276688a1394c0a6a513f43f653e35677f1bf91004538e8876ee039`.

The fingerprint is the SHA-256 of the observed OS release fields, architecture, kernel, and the listed Python/Node/npm/uv/Git/OpenSSL versions. It identifies this preflight observation; it is **not** evidence that a reusable image digest was available.

## Common provider/model freeze

The common model selected by the completed mechanical eligibility gate remains:

- endpoint type: direct Anthropic API / Anthropic Messages-compatible first-party provider path;
- exact model identifier: `claude-sonnet-4-6`.

No alternative model or provider path was substituted.

Held-constant model parameters were not activated because no provider session could be established. No adapter-level temperature, sampling, or model-output-limit override was applied.

Planned wall-clock ceiling, had execution become possible: **900 seconds per run**.

Network policy, had execution become possible:

- system-visible fixture workspace requires no public network;
- model-provider egress only may remain available;
- external evaluator runs after the harness exits and outside the harness-visible workspace.

Deterministic run-order seed: **`35420260922`**.

## Prepared adapter boundary

These are launch/configuration shapes only. They were never executed. Their digests are used in `RUN-MANIFEST.json` solely to identify the prepared configuration, not to imply a run occurred.

| System | Prepared adapter shape | Adapter digest |
| --- | --- | --- |
| Pi | `cwd=<workspace>; pi --print --no-session --provider anthropic --model claude-sonnet-4-6 <exact-task-text>` | `sha256:943dd7f8a8f1ef6071d8fa29790f30b0482f622c6a145a5197620f1f9f2c05f9` |
| oh-my-pi | `omp --cwd <workspace> --print --no-session --provider anthropic --model claude-sonnet-4-6 --max-time 900 <exact-task-text>` | `sha256:3bb3251e995f77c3766c76b2252a603a4a9eabc5d9d16c0879dc67fea36b417a` |
| Ouroboros | `ouroboros run --workspace <workspace> --memory-mode empty --timeout 900 --prompt-file <task.md>` with direct `anthropic::claude-sonnet-4-6` provider configuration | `sha256:bcd7c9ff8243468a19caae3ce0cc6affbe6a228ac9141ffa0b70dea53cd96079` |
| thClaws | `cwd=<workspace>; thclaws --print <exact-task-text> --model claude-sonnet-4-6 --no-session --output-format stream-json` | `sha256:86eaadc1718aecd444b040b963c1458c3ebd0c3de1079cf96934bd4449c8cd19` |
| Headcount | `cwd=<workspace>; claude -p --model claude-sonnet-4-6 <exact-task-text>` with one fixed Headcount plugin installation from the frozen candidate ref | `sha256:76f8a57d49f89d845499f674f5dab8f154c8c090afa4cae4eb30a2cd62538be7` |
| Henterprise | `cwd=<workspace>; hermes chat --provider anthropic --model claude-sonnet-4-6 --query-file <task.md>` with one fixed Henterprise organization installation shape | `sha256:42d494f48f64192d9bdd2ff7953d63f6728d8e79b490c57c28c4c9018fd649d1` |

Adapters would only launch/configure/capture/enforce timeout. They add no planning, retry, memory, tools, verification, summarization, delegation, or repair behavior.

## Terminal infrastructure blocker

Before installing or launching any candidate, the execution runtime was mechanically probed.

Observed at `2026-09-22T18:06:29Z`:

- `github.com` did not resolve through the runtime DNS path;
- `api.anthropic.com` did not resolve through the runtime DNS path;
- no `ANTHROPIC_API_KEY` or equivalent usable Anthropic credential name was exposed;
- the only provider-related environment name observed was `OPENAI_CLUSTER`, which does not satisfy the preregistered direct Anthropic model membrane.

Therefore the common provider/model membrane could not be instantiated. Starting any candidate would have produced an infrastructure failure before a semantic model turn and would not constitute a valid Batch 02 run.

No source changes, alternate models, alternate providers, task rewrites, or post-hoc relaxations were used to work around this condition.

## Execution decision

**No semantic run was started.**

All 54 planned `(system, task, repetition)` tuples are retained in deterministic shuffled order in `RUN-MANIFEST.json` and coded `terminally-unavailable-pre-run`. `start_time` and `end_time` are `null` because no run started; evaluator and semantic fields are also `null` rather than inferred.

This is an infrastructure terminal-unavailability outcome, not evidence for or against any candidate's S1 capability.
