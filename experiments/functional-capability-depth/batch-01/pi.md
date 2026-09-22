# Pi — S1 capability evidence

## Frozen boundary

- repository: `earendil-works/pi`
- review_ref: `71dca871bc80b6bc97be37f0ca3189399d651fff`
- canonical S1 state: `A`
- canonical assessment: [`assessments/pi.md`](../../assessments/pi.md)

No newer Pi revision is used in this record, even though the canonical assessment has a later `last_checked_ref`.

## Credited S1 boundary

- first-party S1 actor / loop: the provider-neutral agent loop in `packages/agent` plus the coding-agent session/runtime that exposes first-party coding tools;
- environment-facing action path: model tool call → Pi argument validation / tool dispatch → configured tool execution → tool result appended to the active trajectory → model continuation;
- external substrates: model/provider inference, the operating system and shell/filesystem reached by tools, and optional user/extensions/custom integrations.

The model's reasoning quality and any external tool implementation are not credited as Pi-native capability merely because Pi can invoke them.

## S1 evidence

| S1 dimension | Ownership | Evidence domain | Evidence type | Observation | Confidence |
| --- | --- | --- | --- | --- | --- |
| operational effectiveness | `unclear` | Coding / SWE | primary implementation and documentation | The frozen tree establishes a complete first-party tool loop, but no matched-model task-success benchmark or controlled before/after result was found that isolates Pi's effect. **insufficient evidence** for comparative operational effectiveness. | medium |
| environment-interaction fidelity | `native` | general tool execution; Coding / SWE | executable code path | `agent-loop.ts` validates tool arguments before execution. If generation stops at the output-token limit while tool calls may be truncated, Pi emits tool errors instead of executing potentially incomplete calls, allowing the model to reissue them. Tool results are returned into the same loop. | high |
| operational state continuity | `native` | Coding / SWE | primary technical documentation | Coding-agent sessions are persisted as JSONL trees, can be resumed/forked/branched, and retain full history. Automatic compaction is documented to trigger near or at context overflow while preserving the stored session history. | high |
| recovery / resilience | `native` | general tool execution; Coding / SWE | executable code path + technical documentation | The agent loop supports continuation, returns tool failures to the model, refuses truncated tool calls, and the coding-agent runtime documents context-overflow compaction followed by retry. This demonstrates recovery mechanisms, not a quantified recovery rate. | high |
| operational result assurance | `unclear` | Coding / SWE | implementation review | Argument validation and tool-error handling protect individual actions, but no frozen first-party task-completion gate, mandatory test/check stage, or host-attested completion proof was found. **insufficient evidence** for task-local result assurance beyond action-level guards. | medium |
| efficiency | `unclear` | general | primary documentation | Pi exposes token/cache/cost/context accounting and compaction, but no controlled comparison ties those mechanisms to fewer resources for comparable successful work. **insufficient evidence**. | high |
| portability / robustness | `native` | general; Coding / SWE | primary technical documentation | The same first-party loop is exposed through interactive, print/JSON, RPC, and SDK modes and supports many model providers. This is evidence for a portable execution path, but no fixed-task cross-provider study at the frozen ref demonstrates that task capability survives substrate changes. | medium |

## Specialized-domain witnesses

- Coding / SWE: strong implementation witness for the tool loop, session persistence, argument validation, and overflow recovery; no frozen matched-model task-success benchmark found.
- Research / Science: **insufficient evidence**.
- Government / Public Administration: **insufficient evidence**.
- other applicable domains: provider-neutral tool execution is general architecture evidence, not a domain-performance result.

## Controlled / benchmark evidence

- No reproducible matched-model benchmark or controlled Pi-vs-Pi ablation was found at the frozen ref.
- The strongest evidence used here is executable first-party loop behavior and primary session/runtime documentation.

## Unsupported or non-comparable claims

- Provider count or API breadth does not establish task robustness across providers.
- Model capability is inherited and is not Pi-native S1 capability.
- Tool availability alone is not environment-interaction fidelity.
- The absence of non-S1 VSM closure is not used as evidence against Pi.S1.
- Pi's current upstream head and later `last_checked_ref` are outside this frozen experiment.

## Primary evidence

- [`packages/agent/src/agent-loop.ts`](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/agent/src/agent-loop.ts)
- [`packages/coding-agent/README.md`](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md)
- [`README.md`](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md)
