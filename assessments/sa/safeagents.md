---
harness_id: safeagents
project_name: SafeAgents
repository: https://github.com/huggingface/safeagents
review_ref: 0de8e22d2345b2379779161abbbffa72738a78a2
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SafeAgents

**Proposed canonical disposition:** `excluded-no-agentic-vsm`. This is not a dismissal of SafeAgents as a useful security proxy. The pinned first-party product enforces/reviews **proposed tool calls of separately operated agents**; it does not operate or supervise its own autonomous task-completing S1. Its optional model judge evaluates a call's apparent safety, not independently observed execution outcomes inside a first-party viable agent organization.

## Review boundary

- System in focus: one self-hosted SafeAgents reverse-proxy instance positioned between a separately installed coding-agent harness and that harness's model endpoint, including synchronous/streaming tool-call filtering, policy, atif-scan and optional verdict model.
- Purpose and identity: withhold or rewrite model-proposed tool calls violating declared tools/host access or scanner safety rules before the external harness executes them.
- Relevant environment: request conversation/user task, proposed tool name and arguments, model-provider response formats, streamed partial calls, malicious host/secret access proposals, user allowlists and optional judge outages.
- Standard-distribution boundary: first-party Starlette/httpx proxy, `Guard`, `Policy`, `Scanner`, `Judge`, SSE/non-stream rewriter, monitoring, journal and CLI. Actual Claude Code/Pi/OpenCode/Hermes/etc. agent task loops, their tools, workspace effects and provider inference remain external; atif-scan is a scanner dependency.
- Credited operating / distribution surfaces: [README and deployment](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/README.md), [HTTP reverse proxy](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/proxy.py), [tool guard and model-judge routing](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/guard.py), [optional judge](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/judge.py), [streamed and non-streaming tool replacement](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/rewrite.py), [tool/host policy](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/policy.py).
- Adjacent first-party surfaces excluded from ownership: offline simulation and harness compatibility test stubs, demo media, `scrub`/dataset publishing utilities, atif-scan's own project governance, optional external model endpoint execution and the host coding-agent's work/approval controller.
- First-party operating / deployment modes considered: `--log-only` observation, default in-line block mode, optional `--judge-model` over OpenAI-compatible endpoint, `--judge-fail-closed`, custom scanner plugins and allowed hosts, streamed Anthropic/OpenAI and non-stream responses, foreground/background proxy.
- Recursion level: one proxy security enforcement surface. An external coding agent to which a user points its base URL is a **client of the proxy**, not first-party SafeAgents S1.
- Reviewed revision: `0de8e22d2345b2379779161abbbffa72738a78a2`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The user separately starts a coding agent, pointing its model endpoint at a local SafeAgents listener. SafeAgents forwards each model request upstream and inspects generated tool-call blocks before passing them downstream. Undeclared tools and unmentioned hosts are rejected by deterministic request checks; atif-scan provides additional signals. For suspicious calls below the hard block threshold, an **optional separate LLM judge** receives only the user's message, proposed call and scanner findings, not the agent's reasoning/tool results, and selects `allow` or `block`. Policy/scanner blocks cannot be overridden by the judge. `rewrite.py` waits for complete tool arguments, removes blocked calls and substitutes a text notice, so the **external** harness does not run that call. SafeAgents does not receive the subsequent real tool execution result, code diff, task outcome or a worker state portfolio through this enforcement path. [Proxy](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/proxy.py); [guard](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/guard.py); [rewrite](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/rewrite.py).

## Operational model

An external coding agent chooses tools, executes allowed calls in its own harness and interprets resulting task feedback. SafeAgents is a pre-execution **security interposer** on the *model response*, not an additional self-contained coding agent/harness execution controller. Its optional judge is genuinely a model-owned local block/allow choice, but that one safety judgment neither becomes independent operational S1 nor receives the complementary execution-reality evidence required for a first-party S3* return. The proxy remains valuable precisely because it limits what an external agent may do; its actual deployment boundary is narrower than a VSM agent organization.

## S1 — Operations

- State: —
- Function: no first-party autonomous software-task S1 that observes workspace/tool effects, chooses new task actions and closes user engineering objectives.
- Disturbance / variety regulated: inappropriate proposed tool use is regulated before execution; actual code-task disturbances and feedback stay with the external harness.
- Decisive decision or feedback right: the external coding agent owns *which engineering tool to request next* after execution feedback. SafeAgents can permit or suppress one already-proposed call, but cannot plan or execute the underlying task or receive tool results for its own continuation.
- Decision owner: external Claude Code/Pi/Hermes/OpenCode/etc. owns operational cognition; first-party guard/scanner and optional model judge own only call-level safety decisions.
- Supporting / enforcement mechanisms: tool policy, atif-scan, optional judge and response rewrites; neither a provider-agent session launcher nor a first-party task/worker loop is shipped.
- Closure path: model response → proposed tool call → SafeAgents permits or replaces → external harness may execute and choose later actions; SafeAgents records its verdict but no own S1 completion/feedback cycle.
- Why this is / is not agent-owned: optional judge semantic discretion is real, yet it is limited to a call's safety classification, not independent operational task adaptation; importing the caller's coding-agent S1 would cross a clear product boundary.
- Evidence: [README integration setup](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/README.md), [forwarding of requests](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/proxy.py), [pre-execution substitution](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/rewrite.py).
- Basis: bounded first-party source-path exclusion.
- Confidence: high for the current installed proxy boundary.
- Caveats: agent models and tools do operate when integrated with separate harnesses, but their autonomy is not borrowed by SafeAgents.

### Absence scope

- Surfaces inspected: main proxy, request/response parsing, safety guard, judge, CLI integration instructions, response rewriting, monitor/journal and compatible harness documentation.
- Plausible first-party paths checked: optional judge as agent, proxy calls to upstream provider, streamed tool rewriting, per-call blocking and tool replay.
- Why no material first-party path remains: no first-party loop chooses a sequence of task actions using real environment/tool results and retains responsibility for the task objective; only external agents do so.

## S2 — Coordination

- State: —
- Function: no attenuation loop for specific conflicts between distinct first-party operational S1 units.
- Disturbance / variety regulated: multiple tool calls in one model response and concurrent model requests can share a proxy, but are not two independently owned operations with competing goals.
- Decisive decision or feedback right: per-call policy and guards allow/block each proposal; no distinct collision detection and adjustment across two S1 workers.
- Decision owner: per-response deterministic scanner and optional judge, not a multi-agent coordination unit.
- Supporting / enforcement mechanisms: streaming argument buffering, per-request `Guard`, request-local call lists, configured host allowlist.
- Closure path: complete model-call arguments are checked and returned to one external harness, with no mutually adjusted inter-agent commitments.
- Why this is / is not agent-owned: blocking unsafe calls and processing concurrency is a permission gate, not VSM S2 reciprocal S1 conflict attenuation.
- Evidence: [guard response scope](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/guard.py), [stream state](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/rewrite.py).
- Basis: structural negative.
- Confidence: high.
- Caveats: an external multi-agent harness may coordinate agents and route all calls through SafeAgents; that coordination stays external.

### Absence scope

- Surfaces inspected: per-call review, streaming/non-stream tool rewriter, request-level config and numerous external harness setup guides.
- Plausible first-party paths checked: simultaneous tool requests, multiple HTTP connections, duplicate calls, host access contention and one model's multiple tool_calls.
- Why no material first-party path remains: no first-party S1 roster or conflict-aware mutual adjustment with returned operational commitments exists.

## S3 — Inside-and-now control

- State: —
- Function: no present whole-agent-organization resource/commitment governance beyond one proxy's call-permission rule.
- Disturbance / variety regulated: unsafe generated commands, unknown hosts, unrecognized tools and judge failures.
- Decisive decision or feedback right: user selects log-only/block and policy configuration; safeagents checks each response. Neither inspects task progress nor reallocates active agent sessions.
- Decision owner: operator for global proxy settings; deterministic guard or optional judge for one call's safety veto, not current multi-S1 portfolio supervision.
- Supporting / enforcement mechanisms: CLI proxy lifecycle, scanner severity, allowlists, monitoring histogram, call journal.
- Closure path: a call is suppressed and the originating harness sees a notice; there is no first-party all-agent current state/priority controller with a return to multiple operational work cells.
- Why this is / is not agent-owned: the class `Guard` is a safety gate, not a VSM S3 current manager; model-veto discretion alone does not establish a whole-system control loop.
- Evidence: [guard and its scope](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/guard.py), [monitor](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/monitor.py), [CLI](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/cli.py).
- Basis: source-boundary negative.
- Confidence: high.
- Caveats: a human may govern several external coding agents using proxy logs, but no SafeAgents-native S3 owner/action scope is established.

### Absence scope

- Surfaces inspected: proxy lifecycle, Guard, journal, CLI controls, optional LLM judge and per-request monitor.
- Plausible first-party paths checked: blocked call correction, policy updates, agent roster overview, tool budget and emergency stop.
- Why no material first-party path remains: no current agent portfolio ownership, scheduling, commitments or system-wide return to controlled S1 operations exists.

## S3* — Complementary audit

- State: —
- Function: no independent audit of actual **operational outcome claims against material execution reality**, returning a correction to a first-party S1/current-control organization.
- Disturbance / variety regulated: malicious or unexpected *planned* tool arguments are judged before execution, not claims about completed work.
- Decisive decision or feedback right: optional model judge may classify a proposed call as safe/unsafe and block it; it never observes actual tool output, workspace changes, passed tests, physical effects or independent S1 progress.
- Decision owner: judge model owns contextual **pre-execution policy** classification; deterministic scanner owns severe fixed-rule blocks. Neither is a S3* auditor of SafeAgents-owned S1 work.
- Supporting / enforcement mechanisms: task text, proposed call argument, scanner findings, separate judge prompt and JSON verdict, stream suppression and log.
- Closure path: policy/scanner/judge → allow/block one unexecuted proposal → external harness gets a text notice; there is no independently evidenced operational success/discrepancy → auditor finding → first-party S1 correction loop.
- Why this is / is not agent-owned: a separate model can be an independent policy judge without qualifying as a VSM complementary auditor; first-party code explicitly withholds tool results and agent reasoning from that judge. Distinguish genuine agentic safety veto from an independent check on operating truth.
- Claim being audited: the candidate *request* appears authorized/safe, not that an S1 agent achieved what it claims.
- Ordinary reporting path: external model's proposed tool-call message.
- Complementary access path: judge receives user-authored instructions and scanner signals distinct from external model prose, but no extra real execution observation or independently measured outcome.
- Independence boundary: judge context is separated from the proposing agent's reasoning and cannot override hard scanner blocks; this is a meaningful policy independence property, but not sufficient S3* outcome-reality independence.
- Who acts on findings: response rewriter blocks a call for the external harness; no SafeAgents-owned task agent receives an operational audit correction.
- Evidence: [judge limited inputs](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/judge.py), [guard routing and optional verdict](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/guard.py), [stream response rewrite](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/rewrite.py).
- Basis: explicit narrower positive pre-execution judgment contrasted with absent VSM audit closure.
- Confidence: medium-high for declared in-line proxy boundary.
- Caveats: an external harness may collect actual tool outcomes and use SafeAgents as one input to its independent audit system; that larger composition is not present in this repository.

### Absence scope

- Surfaces inspected: judge prompt/protocol, scanner evidence, policy veto, journal/monitor, streamed rewrites and proxy model-request handling.
- Plausible first-party paths checked: agent narrative-independent review, raw tool-result audit, completion claims, post-execution exception feedback and separate reviewer model.
- Why no material first-party path remains: the only first-party reviewer path is before external tool execution and has no access to operational outcomes or a SafeAgents-owned S1; hence no completed S3* reality-check return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no future-environment strategic option selection and adoption changing an owned operating organization.
- Disturbance / variety regulated: new exploit patterns, novel model failure modes and user security preferences are external changes SafeAgents could eventually respond to.
- Decisive decision or feedback right: user may configure plugins, add allowed hosts, adjust severity or choose judge model; updates are operator-selected current policy, not a first-party prospective adaptation loop.
- Decision owner: human installer/administrator; built-in scanner has no prospective learning or model-driven capability adoption.
- Supporting / enforcement mechanisms: pluggable atif-scan rules, CLI flags, published benchmark for judge-model selection and manual releases.
- Closure path: a selected rule changes future call filters; no autonomous outside scanning of future options plus binding return to S3 capability is evidenced.
- Why this is / is not agent-owned: using new patterns via plugin and comparing judge models offline are useful configuration/benchmark workflows, not S4 without a prospective organizational return.
- Evidence: [README plugin and benchmark](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/README.md), [guard config](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/guard.py).
- Basis: bounded negative.
- Confidence: high at the proxy recursion.
- Caveats: future automatic security-rule learning could change this; no such cycle is inferred.

### Absence scope

- Surfaces inspected: rule/plugin configuration, judge benchmark and model choice, updates, logs and current policy admission.
- Plausible first-party paths checked: future threat adaptation, benchmark-informed judge selection, policy plugin deployment and learned task-safety profiles.
- Why no material first-party path remains: configuration and external research do not close future option→operating capability under a first-party VSM metasystem.

## S5 — Policy and identity

- State: —
- Function: no recognized ultimate-purpose/identity-policy conflict processed by legitimate S5 authority and returned as a system charter.
- Disturbance / variety regulated: user-authorized hosts versus attempted model tool calls, credential privacy and acceptable tool risk, all local safety concerns.
- Decisive decision or feedback right: installer chooses local proxy settings and model policies; judge can block a call but cannot define the system's enduring identity or reconcile an ultimate policy dilemma.
- Decision owner: external user and product authors define rules; no separate first-party identity-level regulator.
- Supporting / enforcement mechanisms: allowlist, severity threshold, optional fail-closed judge error handling and log-only mode.
- Closure path: policy permits or rejects individual proposed tools; no legitimate constitutional question is escalated and resolved with binding whole-system return.
- Why this is / is not agent-owned: a safety guardrail and independent block decision are not VSM S5 merely because they constrain all tool actions passing through the proxy.
- Evidence: [guard choices](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/guard.py), [policy implementation](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/src/safeagents/policy.py), [CLI policies](https://github.com/huggingface/safeagents/blob/0de8e22d2345b2379779161abbbffa72738a78a2/docs/commands.md).
- Basis: bounded negative.
- Confidence: high.
- Caveats: policy-setter human authority in a host organization remains outside this source-declared proxy level.

### Absence scope

- Surfaces inspected: CLI flags, host/tool policies, judge prompt, scanner plugins, severity threshold and error behavior.
- Plausible first-party paths checked: exception approval, policy prompt, trusted host amendment, block rationale and human safety changes.
- Why no material first-party path remains: these govern individual call safety, not legitimate ultimate-purpose policy adoption by a self-owned autonomous operating organization.

## Distributed OSS parent arrangement

SafeAgents is a publicly redistributable security add-on. Each operator controls its own external coding agent and model endpoint; the Hugging Face maintainer, local user and client harness do not become a first-party SafeAgents S1/S5 hierarchy simply because the proxy sits on their network path.

## Self-hosted and non-human modes

Without a judge, scanner and request policies are deterministic; `--log-only` records potential blocks without enforcement. With an explicitly configured judge the proxy adds a model-owned contextual veto but still does not launch the client coding agent, receive tool-result feedback or own task completion. Failure handling may allow or block on judge error according to configuration; neither mode establishes S1 or independent outcome audit.

## Recursion

The model endpoint, SafeAgents proxy and external coding harness are three components of a possible larger installation, but this assessment declares the first-party SafeAgents proxy as the system. Changing that boundary to the full external host would borrow unassessed agent autonomy and instruction governance.

## Variety and escalation

Tool and host declaration checks, atif-scan detectors, optional model contextual judgment, buffered streaming and explicit block notices attenuate unsafe proposed calls. Monitoring and journals improve operator visibility. The originating agent may receive the block notice and adapt its own task plan, but that subsequent autonomous action belongs to its separate harness, not to SafeAgents.

## Evidence gaps

- Exact pinned source and public operating docs establish the response-block path. No real paid judge inference or installed external harness session was executed in this review.
- The optional judge can materially decide whether a suspicious call is blocked, a real agentic safety feature. It sees user task/call/scanner findings, not independent observations of actual completed operations. This is not enough to close a first-party VSM S3* audit.
- External Codex/Claude/Pi/Hermes S1 work is deliberately not credited to the proxy. The lack of a first-party adaptive task loop is the main inclusion-boundary reason for the proposed `excluded-no-agentic-vsm` disposition.
- Tool security policies, judge choice and plugin updates are not automatically S3/S4/S5 organizational governance.
