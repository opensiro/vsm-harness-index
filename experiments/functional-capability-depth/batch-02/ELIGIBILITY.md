# Batch 02 mechanical eligibility

Status: **READY FOR ENVIRONMENT FREEZE**

This record implements Phase 1 of issue #354. It is mechanical eligibility only. No Batch 02 semantic task was executed, no fixture result was inspected, and no non-S1 canonical state was used in the classifications below.

## Preflight boundary

- Batch 02 design merge commit: `2c48827a2064a96b0d78859b200316ce879feba2`.
- Current `main` rechecked before this record: `43f6ed035b8536b60aa1d4b75ba82ec785da6b0a`.
- The design commit is an ancestor of that `main`; the commits after it do not modify `experiments/functional-capability-depth/batch-02/`.
- GitHub issue #354 remains open and is the active execution issue.
- Frozen candidate refs below are unchanged from the committed Batch 02 contract.

## Mechanical gate and common-model intersection

The gate is the one frozen in [`README.md`](README.md): a candidate must have a documented first-party executable or supported host path, accept the unchanged task text, work in an isolated local workspace, expose filesystem mutation plus command execution, support one common model without first-party source modification, permit an external timeout, and leave output/process state plus the resulting workspace capturable.

For Phase 1, the common model compatibility intersection is:

- endpoint family: Anthropic API / Anthropic Messages-compatible direct provider path;
- exact model identifier: `claude-sonnet-4-6`.

The exact endpoint URL, credential mechanism, host versions, model parameters, output limit, network policy, wall-clock ceiling, environment digest, adapter commands, and deterministic run-order seed are **not** frozen here; they belong to `ENVIRONMENT.md` and must be committed before the first semantic run. Current Anthropic documentation lists `claude-sonnet-4-6` as active on 2026-09-22.

A supported host counts only as the candidate's documented execution substrate. Host-provided filesystem, shell, model transport, or other behavior is not thereby credited as first-party S1 capability; ownership is interpreted only after raw runs.

## Summary

| System | Frozen ref | Executable / host path | Exact task unchanged | Isolated workspace | FS + command path | Common model path | Timeout + capture | Final status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pi | `earendil-works/pi@71dca871bc80b6bc97be37f0ca3189399d651fff` | first-party Pi coding-agent CLI | yes | yes | `read` / `write` / `edit` / `bash` | direct Anthropic, `claude-sonnet-4-6` | external timeout; text/JSON/RPC + workspace | `eligible` |
| oh-my-pi | `can1357/oh-my-pi@dbf3afad4894bde827d90f965e77b3fe1c5a95e5` | first-party `omp` coding-agent CLI | yes | yes | first-party coding tools / shell | direct Anthropic, `claude-sonnet-4-6` | external timeout plus first-party `--max-time`; text/JSON/RPC + workspace | `eligible` |
| Ouroboros | `razzant/ouroboros@86806ee123ce8e26cc063cc1a618f975eea64f26` | first-party managed headless `ouroboros run` | yes | yes | managed external-project task path | direct `anthropic::` provider route | first-party `--timeout`; JSONL/result/patch + workspace | `eligible` |
| thClaws | `thClaws/thClaws@cd700937a71a391f052438d139b7b1c5a6456755` | first-party `thclaws -p` | yes | yes | workspace-scoped file tools + Bash | direct Anthropic, `claude-sonnet-4-6` | external timeout; text/stream-json + workspace | `eligible` |
| Headcount | `cbrock84/headcount@9cbf34005e3e8a980a6af9b55eb226bd926a62b3` | documented Claude Code plugin host | yes | yes | inherited Claude Code file/edit/Bash path | Claude Code direct Anthropic API path, `claude-sonnet-4-6` | external timeout; print/JSON/stream-json + workspace | `eligible` |
| Henterprise | `humbertobellor/henterprise@0bd56397676462e216f92b5b7800919a3597a99a` | documented Hermes Agent host/profile path | yes | yes | inherited Hermes terminal/file path | Hermes direct Anthropic provider, `claude-sonnet-4-6` | external timeout; single-query output + workspace | `eligible` |

Eligible cohort: **6 / 6**. The `<3` NOT READY stop condition does not apply.

## Pi

**Frozen evidence**

- [`README.md`](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md) identifies the first-party coding-agent CLI, agent runtime, multi-provider model layer, and source launcher.
- [`packages/coding-agent/README.md`](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) documents interactive, print, JSON, RPC, and SDK modes and the default `read`, `write`, `edit`, and `bash` tools.
- [`packages/coding-agent/src/cli/args.ts`](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/src/cli/args.ts) exposes `--provider`, `--model`, `--mode`, `--no-session`, tool selection, `--print/-p`, and positional messages.
- [`packages/agent/README.md`](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/agent/README.md) shows the Anthropic provider with exact model lookup `claude-sonnet-4-6` and tool-execution event streaming.

**Gate application**

- Invocation/configuration: supported first-party CLI; no source patch required.
- Task text: can be passed as one unchanged positional message in print mode.
- Workspace: the adapter can launch Pi with the clean fixture copy as process working directory; Pi's own README states the source launcher can be run from any directory.
- Filesystem/commands: normal first-party coding-agent tool surface includes file reads/writes/edits and Bash.
- Common model: direct Anthropic provider and exact `claude-sonnet-4-6` are present at the frozen ref.
- Timeout/capture: external process timeout is sufficient; Pi exposes text/JSON/RPC output and the runner can inspect the post-run workspace.

Final status: **`eligible`**.

## oh-my-pi

**Frozen evidence**

- [`README.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/README.md) documents the first-party coding agent, installation paths, broad provider support, file/edit/shell execution, and local workspace operation.
- [`packages/coding-agent/src/cli/args.ts`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/packages/coding-agent/src/cli/args.ts) includes `cwd`, provider/model selection, non-interactive print mode, no-session operation, capture modes, and timeout configuration.
- [`packages/coding-agent/src/cli/flag-tables.ts`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/packages/coding-agent/src/cli/flag-tables.ts) is the CLI flag SSOT and exposes `--cwd`, `--mode`, `--provider`, `--model`, `--max-time`, `--session-dir`, and tool configuration.
- [`packages/metaharness/README.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/packages/metaharness/README.md) records benchmark execution with exact `anthropic/claude-sonnet-4-6` as a supported model identity.

**Gate application**

- Invocation/configuration: supported first-party CLI with explicit cwd/model/timeout controls.
- Task text: accepted as the ordinary positional prompt; no task-specific rewriting is needed.
- Workspace: `--cwd` can point to each clean fixture copy.
- Filesystem/commands: normal first-party coding-agent surface provides mutation and command execution.
- Common model: exact `anthropic/claude-sonnet-4-6` is documented at the frozen ref.
- Timeout/capture: runner timeout can wrap the process; first-party `--max-time` is additionally available. Output modes plus the workspace are capturable.

Final status: **`eligible`**.

## Ouroboros

**Frozen evidence**

- [`README.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/README.md) documents the native/headless runtime, configurable remote providers, CLI, and work on external projects.
- [`ouroboros/cli.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/cli.py) defines `run` as a managed headless task and exposes `--workspace`, `--prompt-file` (including stdin), `--memory-mode`, `--timeout`, `--jsonl`, `--patch-out`, and `--result-json-out`. The task body records the supplied workspace as an external workspace root.
- [`ouroboros/provider_models.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/provider_models.py) defines a direct `anthropic::` provider route backed by `ANTHROPIC_API_KEY`; provider selection is based on the model prefix and does not require a source edit.

**Gate application**

- Invocation/configuration: first-party managed headless task path.
- Task text: `--prompt-file -` can read the committed task text verbatim from stdin; no rewrite is needed.
- Workspace: `--workspace <clean-copy>` is a first-party external-project path.
- Filesystem/commands: external-project managed tasks are the documented operational path; the runner does not add tools.
- Common model: direct Anthropic routing accepts an `anthropic::` model identity without source modification; Phase 2 must freeze the exact configured value corresponding to `claude-sonnet-4-6` and verify it against the live common endpoint before any semantic run.
- Timeout/capture: first-party task timeout, JSONL/progress, result JSON, patch capture, and resulting workspace are available.

Final status: **`eligible`**.

## thClaws

**Frozen evidence**

- [`README.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/README.md) documents CLI and non-interactive `thclaws -p "prompt"`, local workspace operation, file tools, Bash, and the same engine across terminal/desktop surfaces.
- [`crates/core/src/bin/app.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/bin/app.rs) exposes `--print`, one-shot `--model`, `--no-session`, `--output-format text|stream-json`, allowed/disallowed tools, and iteration controls.
- [`user-manual/ch06-providers-models-api-keys.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/user-manual/ch06-providers-models-api-keys.md) documents the direct Anthropic provider (`ANTHROPIC_API_KEY`), states that `claude-sonnet-4-6` is the default model, and permits one-shot CLI model selection.

**Gate application**

- Invocation/configuration: first-party one-shot CLI.
- Task text: exact text can be supplied as the `--print` prompt.
- Workspace: CLI/non-interactive mode operates in the directory from which it is launched; the adapter can make the clean fixture copy that directory.
- Filesystem/commands: first-party workspace-scoped file tools and Bash are normal supported paths.
- Common model: direct Anthropic `claude-sonnet-4-6` is explicitly documented at the frozen ref.
- Timeout/capture: external runner timeout plus text/stream-json process output and the resulting workspace are sufficient.

Final status: **`eligible`**.

## Headcount

**Frozen candidate evidence**

- [`README.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/README.md) identifies Headcount as an agent organization for Claude Code and documents marketplace/plugin installation.
- [`docs/GETTING-STARTED.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/docs/GETTING-STARTED.md) states that departments are independently installable Claude Code plugins; skills load through the host, and installing Headcount itself does not mutate the target repository or run work on its own.

**Supported host evidence used only for mechanical execution feasibility**

- Claude Code public host revision inspected for this gate: `anthropics/claude-code@56f36532530f88b572854538d685fcf781141e8c`.
- Claude Code documents non-interactive print mode, exact model selection, JSON/stream-json capture, and normal Read/Edit/Bash execution.
- Claude Code documents that `ANTHROPIC_API_KEY` is used for API-key authentication, including in non-interactive `-p` mode, allowing the host to share a direct Anthropic provider membrane rather than requiring a subscription-only transport.

**Gate application**

- Invocation/configuration: supported host-installation path is part of the frozen Headcount documentation. Phase 2 must pin the exact Claude Code host version and install the same Headcount surface before all runs; the adapter must not choose different departments or skills by task.
- Task text: Claude Code print mode can receive the committed text unchanged.
- Workspace: launch the documented host in each clean fixture copy.
- Filesystem/commands: inherited from the supported Claude Code host; this satisfies execution eligibility but is not automatically Headcount-owned capability.
- Common model: the host can use direct Anthropic API-key auth with exact `claude-sonnet-4-6` without modifying Headcount source.
- Timeout/capture: external runner timeout; print/JSON/stream-json output and the resulting workspace are capturable.

Final status: **`eligible`**.

## Henterprise

**Frozen candidate evidence**

- [`README.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/README.md) identifies Henterprise as an organization for Hermes Agent and documents two supported installation shapes: one Hermes profile over the whole organization through `skills.external_dirs`, or one profile per department. It also documents staged `SOUL.md` installation.

**Supported host evidence used only for mechanical execution feasibility**

- Hermes Agent public host revision inspected for this gate: `NousResearch/hermes-agent@6c4536aed298112e976cf7c484ee63e99150e09d` (the relevant provider/CLI documentation was already present in its parent `834580309d7643bbae9952f4d96f8769905e55a9`).
- Hermes documents single-query non-interactive execution via `hermes chat -q` and verbatim task input via `hermes chat --query-file`, including stdin.
- Hermes documents direct Anthropic execution with `ANTHROPIC_API_KEY` and the exact command shape `hermes chat --provider anthropic --model claude-sonnet-4-6`.
- Hermes provides terminal/file operation through its normal toolsets/backends.

**Gate application**

- Invocation/configuration: the frozen Henterprise repository explicitly defines the Hermes host-installation path. Phase 2 must pin the exact Hermes version and one fixed organization installation shape for every Henterprise run; the adapter must not select different profiles/skills by task.
- Task text: `--query-file -` can carry the exact committed text verbatim.
- Workspace: run the host with the clean fixture copy as its working directory / configured local terminal workspace.
- Filesystem/commands: inherited Hermes terminal/file capability satisfies execution eligibility but is not automatically Henterprise-owned capability.
- Common model: Hermes explicitly supports direct Anthropic `claude-sonnet-4-6` without candidate source modification.
- Timeout/capture: external runner timeout; single-query stdout/stderr plus the resulting workspace are capturable. Any telemetry not exposed comparably remains unobserved rather than inferred.

Final status: **`eligible`**.

## Adapter boundary for Phase 2

For every eligible system, the eventual adapter may only:

1. launch the documented first-party executable or supported host;
2. set the frozen provider/model/environment configuration;
3. pass the exact committed task text;
4. point the runtime at the clean copied workspace;
5. capture output/events/timestamps and the resulting workspace;
6. enforce the common wall-clock ceiling.

It must not add planning, retries, memory, tools, verification, summarization, delegation, repair logic, or any other S1 behavior. Any candidate/host behavior that performs those actions on its own remains behavior of the system-under-test plus its documented substrate and must be separated later by ownership accounting.

## Phase-1 decision

All six frozen systems pass the mechanical gate. Batch 02 therefore proceeds to Phase 2. The next required artifact is `ENVIRONMENT.md`; it must be committed before the first semantic task run. No semantic execution is authorized until the common environment and live common-model path are actually available and frozen.