# thClaws — S1 capability evidence

## Frozen boundary

- repository: `thClaws/thClaws`
- review_ref: `cd700937a71a391f052438d139b7b1c5a6456755`
- canonical S1 state: `A`
- canonical assessment: [`assessments/thclaws.md`](../../../assessments/thclaws.md)

## Credited S1 boundary

- first-party S1 actor / loop: the Rust `Agent` loop, `ToolRegistry`, shared session driver, and goal/plan execution controls;
- environment-facing action path: user objective → provider response → first-party stream assembly / tool dispatch / permission and plan gates → tool result → continued first-party loop;
- external substrates: model/provider inference, operating-system commands and services, browser/MCP/external tools where configured, and third-party compilers/runtimes used by tasks.

The availability of an external MCP service or provider is not credited as native capability; thClaws's dispatch, state, recovery, and completion controls around those substrates are first-party.

## S1 evidence

| S1 dimension | Ownership | Evidence domain | Evidence type | Observation | Confidence |
| --- | --- | --- | --- | --- | --- |
| operational effectiveness | `unclear` | general; Coding / SWE | primary implementation and documentation | The frozen tree exposes a substantial operational loop, but no matched-model task-success benchmark or controlled before/after harness result was found. **insufficient evidence** for comparative operational effectiveness. | medium |
| environment-interaction fidelity | `native` | general tool execution | executable code path + technical manual | The first-party loop performs parse-then-execute tool handling, records tool results back into the trajectory, applies plan/permission gates, and handles malformed tool calls as explicit errors rather than silently treating them as successful actions. This demonstrates the action path, not a measured fidelity rate. | high |
| operational state continuity | `native` | general | executable implementation + primary documentation | Agent history is retained across turns, compaction preserves tool-use/tool-result pairing, sessions are resumable, and `/goal` state persists in the session across `/load`. Step-boundary compaction/clear mechanisms preserve a bounded current trajectory. | high |
| recovery / resilience | `native` | general | executable code path + technical manual | Provider startup calls retry with exponential backoff; configuration errors skip pointless retries; cancellation can interrupt retry sleep; oversized context has truncation/compaction rescue; a max-token stop gets a one-shot larger-output retry. The manual explicitly records that mid-stream provider errors do not retry, which bounds the claim. | high |
| operational result assurance | `native` | general; Coding / SWE | primary technical documentation tied to engine controls | `/goal` builds an audit prompt around concrete deliverables and evidence, and `--require <path>` creates a first-party hard gate: `MarkGoalComplete` is rejected while required artifacts are missing. Completion also requires an audit summary. Plan-mode instructions require runnable verification, although the prompt itself admits it cannot prove the model actually executed every check. | high |
| efficiency | `native` | general | technical documentation | Goals expose token/time budgets, a hard `1.5×` budget stop, and an iteration cap; compaction and usage accounting bound resource consumption. These are resource controls, not evidence that thClaws uses fewer resources for comparable successful work. **insufficient evidence** for comparative efficiency. | medium |
| portability / robustness | `native` | general | primary technical documentation | The same agent engine backs desktop, CLI, non-interactive, and web surfaces and supports multiple providers/platforms. No frozen fixed-task cross-provider or cross-platform outcome study was found, so observed capability survival under substrate change remains **insufficient evidence** despite the portable architecture. | medium |

## Specialized-domain witnesses

- Coding / SWE: implementation paths for tools, plans, goals, shell execution, and verification are directly relevant; no matched coding benchmark was found at the frozen ref.
- Research / Science: **insufficient evidence**.
- Government / Public Administration: **insufficient evidence**.
- other applicable domains: browser/document/media features are not treated as capability results without controlled task evidence.

## Controlled / benchmark evidence

- No matched-model task benchmark or controlled harness ablation was found at the frozen ref.
- The strongest evidence is executable loop behavior plus documented hard goal gates and recovery paths.

## Unsupported or non-comparable claims

- Model/provider count and tool breadth are not operational-effectiveness scores.
- The `/goal --require` file-existence gate proves only the named artifact condition; it does not prove semantic correctness of the artifact.
- Plan-mode verification instructions are not equivalent to host-attested proof that every check ran.
- Multi-platform/multi-provider support is not by itself evidence that task success is robust across substrates.
- Agent teams or other organizational breadth are not imported as S1 capability evidence.

## Primary evidence

- [`README.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/README.md)
- [`crates/core/src/agent.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/agent.rs)
- [`thclaws-technical-manual/agentic-loop.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/thclaws-technical-manual/agentic-loop.md)
- [`user-manual/ch31-loops-and-goals.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/user-manual/ch31-loops-and-goals.md)
