---
harness_id: mini-ai-harness
project_name: mini-ai-harness
repository: https://github.com/TejasQ/basically-ai-harness
review_ref: ea40e4dec975e6a0c56412bf8217581a1761329c
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mini-ai-harness

## Review boundary

- System in focus: The runnable TypeScript browser agent under agent/, selected by npm run agent.
- Purpose and identity: Enable a model to complete a user-style web interaction through an iterative browser tool loop.
- Relevant environment: Browser pages, redirects, DOM state, OpenRouter model responses and tool errors.
- Standard-distribution boundary: Frozen default branch 0; agent/ plus package entry wiring. Evaluate the actual upvote demo, not the more elaborate README description.
- Credited operating / distribution surfaces: [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/1-tools.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/1-tools.ts); [agent/browser.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/browser.ts)
- Adjacent first-party surfaces excluded from ownership: eval/ is an adjacent fixed-dataset model evaluation program with separate npm entry; it is not wired as an auditor/controller of the browser agent. README tutorial/presentation claims do not substitute for shipped source.
- First-party operating / deployment modes considered: npm run agent selects one browser session and one model-backed loop. npm run eval is examined only as an adjacent mode. No first-party multi-agent or operator-governed metasystem mode found.
- Recursion level: One browser-task execution.
- Reviewed revision: `ea40e4dec975e6a0c56412bf8217581a1761329c`
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The entry point opens a BrowserSession, creates session-bound tools and initial messages, runs a model-driven loop and closes the session in finally. The loop calls OpenRouter via the OpenAI SDK; model tool calls navigate/read/fill/click/inspect the page, with result or error messages fed back. A model stop ends the run. Trace entries record iterations. At this frozen ref, MAX_CONTEXT_MESSAGES is declared but unused; there is no agent/4-guardrails.ts or agent/6-harness.ts, and the entry point does not run a final verifier. The separate eval runner scores fixed expected answers and does not return findings into agent operations. No persistence, scheduler or maintainer-governance runtime is wired.

## Operational model

One agent chooses browser actions from changing DOM observations. Tool execution is sequential within a response, and SDK/browser lifecycle code supplies transport and environment. The literal task and model are developer-selected; the agent retains the action choice. Multiple models mentioned in README are not concurrent S1 units in the shipped entry.

## S1 — Operations

- State: A
- Function: Complete a browser task using model-selected environment actions.
- Disturbance / variety regulated: Page state, redirects, already-voted stories and browser/tool errors.
- Decisive decision or feedback right: Select which browser tool and arguments to use next; interpret observations and finish.
- Decision owner: The model-backed agent called by runLoop.
- Supporting / enforcement mechanisms: Session-bound tool registry, BrowserSession, message history and model transport.
- Closure path: tool_calls → execute → tool/error messages → next completion; finish_reason stop returns the answer.
- Why this is / is not agent-owned: Without the model, the registry/browser cannot decide task-specific actions; the installed entry wires that choice without user composition.
- Evidence: [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/1-tools.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/1-tools.ts); [agent/browser.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/browser.ts)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.
- Boundary reachability: package.json agent script directly executes agent/7-index.ts, which calls the first-party runLoop with first-party tools.

## S2 — Coordination

- State: —
- Function: No inter-S1 disturbance-regulation path in the selected single-agent run.
- Disturbance / variety regulated: Potential browser task changes are within one agent's local operation.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Sequential tool execution within one agent is not coordination among distinct operational units.
- Evidence: [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/browser.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/browser.ts); [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/browser.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/browser.ts); [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json)
- Plausible first-party paths checked: Session ownership, tool iteration, model selection and both npm entry points.
- Why no material first-party path remains: The shipped agent entry creates one session and one autonomous unit; no multi-unit collision mode plus coordinating decision/feedback relation is present.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control authority beyond the local agent loop.
- Disturbance / variety regulated: Run duration, context growth and errors would need bounded current regulation.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: The model's next local tool action and stop are operational S1 choices. No supervisor allocates resources or revises commitments on behalf of a larger current system.
- Evidence: [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/3-context.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/3-context.ts); [README.md](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/3-context.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/3-context.ts); [README.md](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/README.md)
- Plausible first-party paths checked: Loop termination, unused MAX_CONTEXT_MESSAGES, browser lifecycle, documented guardrail/harness paths and any operator mode.
- Why no material first-party path remains: README's guardrail/final-verification description is not implemented by the frozen entry or files. No whole-current decision owner and returned constraint path remains; hypothetical additions are not C.

## S3* — Complementary audit

- State: —
- Function: No complementary independent audit of browser-agent reporting.
- Disturbance / variety regulated: A model may report success without changing the intended page state.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Tool traces and DOM tools belong to the acting agent's routine path. The fixed-dataset eval does not audit this run or feed a corrective decision back.
- Evidence: [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/1-tools.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/1-tools.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [eval/4-runner.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/eval/4-runner.ts); [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/1-tools.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/1-tools.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [eval/4-runner.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/eval/4-runner.ts); [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json)
- Plausible first-party paths checked: Trace storage, hooks in createTools, browser state inspection, finalization and separate evaluation entry.
- Why no material first-party path remains: No first-party independent complementary inspection-and-return path is wired to this agent. The hooks are optional tool-observation callbacks and the entry does not attach an auditor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No externally prospective adaptation of the harness's present capability.
- Disturbance / variety regulated: Web pages change, but sensing them is the current task.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Navigation and story inspection produce the task outcome, not future-environment options with a capability/control return.
- Evidence: [agent/1-tools.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/1-tools.ts); [agent/3-context.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/3-context.ts); [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [README.md](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [agent/1-tools.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/1-tools.ts); [agent/3-context.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/3-context.ts); [agent/5-loop.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/5-loop.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [README.md](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/README.md)
- Plausible first-party paths checked: Live web observations, model swapping, task definition, context and adjacent model evaluation.
- Why no material first-party path remains: No future-oriented option-development/selection path returns to change current harness capability; developer edits and presentation material do not supply an S4 parent mode.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy closure.
- Disturbance / variety regulated: Task and model are fixed in the entry; generic instructions bound behaviour.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: The context prompt and hard-coded task are configuration, not an authoritative identity-policy issue/decision/return loop.
- Evidence: [agent/3-context.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/3-context.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/2-model.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/2-model.ts); [README.md](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/README.md); [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [agent/3-context.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/3-context.ts); [agent/7-index.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/7-index.ts); [agent/2-model.ts](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/agent/2-model.ts); [README.md](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/README.md); [package.json](https://github.com/TejasQ/basically-ai-harness/blob/ea40e4dec975e6a0c56412bf8217581a1761329c/package.json)
- Plausible first-party paths checked: System prompt, model/task selection, environment credentials and any first-party human governance entry.
- Why no material first-party path remains: No legitimate ultimate authority receives an identity-policy issue and returns a binding decision into operation. README and license are not runtime S5.

## Distributed OSS parent arrangement

Only developer task/model setup is visible. Neither the project maintainer nor an eval user is wired as parent S3/S4/S5 authority for the browser session.

## Self-hosted and non-human modes

Running the local TypeScript demo requires an API key and browser runtime. It does not add supervisory/identity functions. No intentionally non-human organization is claimed.

## Recursion

No nested operational organization; the browser is an environment/tool surface, not a recursive viable unit.

## Variety and escalation

Browser tool exceptions become model-readable Error strings; malformed tool arguments and non-stop/non-tool finish reasons have limited recovery. Trace collection records ordinary operations. No algedonic path is established.

## Evidence gaps

Source-only assessment; no model API call, browser launch, login or upvote was performed. No native test script is provided, and tsconfig includes src rather than the shipped agent/eval directories, so no native typecheck/test PASS is claimed. The discrepancy between README guardrail/verifier claims and frozen source is explicit, not filled with assumed files. MIT LICENSE is present.
