---
harness_id: drinky
project_name: Drinky
repository: https://github.com/clebert/drinky
review_ref: 868f50c2604a5619238c6235cd63820d9c724c38
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Drinky

## Review boundary

- System in focus: the installed first-party Drinky Zig terminal coding-agent process: one Agent/tool execution loop, seven bundled coding tools, account/model adapter, compiled instructions, project skill guard, transient conversation, TUI, Telegram remote controller and Herdr status report.
- Purpose and identity: execute user-directed coding tasks against local files using a model-backed read/search/edit/bash loop, maintaining session transcript and terminal or paired private-chat control.
- Relevant environment: workspace code and commands, shell errors, model/provider responses and quota signals, project instruction files, configured limits, terminal steering and optional paired Telegram input.
- Standard-distribution boundary: shipped src/*.zig, lib/ai/*.zig, lib/ai/tool/*.zig and src/remote/*.zig compiled into the single Drinky process; the Zig standard library and external providers are dependencies, not imported organizational function owners.
- Credited operating / distribution surfaces: terminal model/tool run, concurrent read-only and barrier-separated mutating tool batches, model/account switching, current-turn retry/cancel/steering, project instructions and skill loading, optional private Telegram input/output and Herdr pane notification.
- Adjacent first-party surfaces excluded from ownership: repository tests and scripts/test-audit.sh, developer BACKLOG/FEATURES intentions not wired to the product, external user-supplied skill instructions, Telegram service, external model providers and the maintainers' development organization.
- First-party modes checked: local session, terminal steering and retry, model selection, tool batch execution, paired Telegram remote control, skill guard, transcript/status and configured bash/request limits.
- Recursion level: one Drinky running agent. Read-only threads run tools for the *same* operational actor; user/remote control is another interface to that process, not a separate S1 organization.
- Reviewed revision: 868f50c2604a5619238c6235cd63820d9c724c38 (batch #1013 row 4), observed 2026-10-24, MIT.

## Repository architecture

The Zig Agent in lib/ai/Agent.zig owns one conversation history and executes a model-request → model-selected tool calls → first-party tool dispatch → recorded tool-result feedback loop until the model stops calling tools. lib/ai/tool/root.zig advertises seven bundled tools: read, write, edit, find, grep, bash, describe_drinky. Read-only calls may run concurrently on bounded threads; mutating calls are barriers in this one actor's tool batch. Retry/cancel/transcript receipts are operational reliability mechanisms.

The UI/App and optional Telegram remote attachment steer the same session and mirror updates; the remote pairing controller owns bot state and I/O tasks, not a portfolio of autonomous coding units. There are no shipped subagent roles or workflows; README explicitly identifies one agent job. Project skill content is user-provided instructions loaded into the existing coding loop. The build has no first-party permission gate or sandbox; instructions and limits are not constitutional governance.

Frozen primary sources: [Agent loop](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/Agent.zig), [tool registry](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/tool/root.zig), [remote controller](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/remote/Controller.zig), [session status](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/State.zig), [product README](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/README.md).

## Operational model

An operator sends a task from terminal or paired chat. One model-backed Agent chooses code actions, while source tools execute and return real local-file/shell observations. The operator can interrupt, steer, retry or change the model in the same process. The model/provider, Telegram bot and Herdr app are environmental interfaces. No live LLM-agent, provider or Browser quality tests were run in this assessment.

## S1 — Operations

- State: A
- Function: perform repository coding actions with open-ended model decisions revised from current tool observations.
- Disturbance / variety regulated: changing source structure, ambiguous implementation steps, tool errors, changing operator intent, provider failures and tool-result variance.
- Decisive decision or feedback right: select which source operations/commands to attempt next and whether to revise them from returned results.
- Decision owner: the active model-backed Drinky Agent instance.
- Supporting / enforcement mechanisms: seven tool implementations, provider-neutral transport, output/time bounds, tool-call completion receipts, retry/steering and compiled context instructions.
- Closure path: user objective + tool specifications → model selects actions → read/search/edit/write/bash execution → recorded tool results → subsequent model call or stop.
- Boundary reachability: the Agent loop and bundled tool registry are reachable from the shipped single Zig CLI/TUI executable and optional paired chat interface.
- Why this is / is not agent-owned: without a model, static Zig tool functions cannot choose arbitrary coding actions or adapt to tool evidence; the model owns those next-action decisions.
- Evidence: [lib/ai/Agent.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/Agent.zig), [tool/root.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/tool/root.zig), [src/App.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/App.zig).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the selected provider can fail or limit reachability; source inspection establishes executable path, not effectiveness with a live LLM.

## S2 — Coordination

- State: —
- Function: no independent S1-to-S1 interference attenuation with corrective coordination feedback is established.
- Disturbance / variety regulated: concurrent read/search tool scheduling and ordered write barriers occur inside one model actor, not across autonomous operational units.
- Distinct S1 units: only one first-party model-backed operating Agent; read-only tool threads do not own separate coding agendas.
- Inter-S1 disturbance: none among a population of separately acting shipped S1 units at this boundary.
- Attenuating coordination relation: fixed batching/barriers prevent intra-agent tool races but are not an inter-S1 conflict regulator.
- Feedback into subsequent S1 behaviour: tool results return to the same parent model; no S2-specific conflict finding and altered relations among distinct S1 units.
- Decisive decision or feedback right: no separate S2 decision found.
- Decision owner: no S2 owner; the single Agent and static executor own task decisions and scheduling respectively.
- Supporting / enforcement mechanisms: read-only_calls_max, mutating tool barriers, bounded tool rounds and result-slot accounting.
- Closure path: tool actions → serialized/concurrent dispatch → same-Agent result feedback exists, but multiple S1 conflict → S2 regulation → changed distinct-unit behavior is absent.
- Boundary reachability: the batching code is shipped; a multi-agent coordination mode is not.
- Why this is / is not agent-owned: dynamic choice of task actions does not turn deterministic per-batch tool scheduling into organizational S2.
- Evidence: [Agent.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/Agent.zig), [tool/root.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/tool/root.zig), [README.md](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/README.md).
- Basis: explicit + structural bounded absence review.
- Confidence: high.
- Caveats: external users could run several separate Drinky processes, but the installed product does not wire their independent work into one S2 control loop.

### Absence scope

- Surfaces inspected: shipped tool registry, Agent calls/rounds, threaded readonly runner, model instructions, Telegram remote controller and product capabilities.
- Plausible first-party paths checked: read-only concurrency as distinct S1s, serialized writes as S2, paired remote input as another working unit, and user-run parallel process coordination.
- Why no material first-party path remains: there is one current coding Agent with tool-level concurrency, and no distinct inter-agent coordination actor or rule-feedback path.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current allocation/commitment management across independently accountable S1 operating units.
- Disturbance / variety regulated: current turn failure/cancellation, provider quota and the attached remote UI do not constitute a multiactor operating portfolio.
- Whole-system current view: per-process transcript/status, account/model/usage and optional Herdr or Telegram mirror show one session only.
- Current-control decision scope: operator may steer, cancel, resume/retry or switch models for this one coding session, without a separately tasked current-resource manager.
- Decisive decision or feedback right: no qualifying S3 current control right evidenced.
- Decision owner: single S1 agent and human operator of a selected session.
- Supporting / enforcement mechanisms: Agent receipt, account quota display, state file, paired bot and Herdr event reports.
- Closure path: process state → user-visible feedback → task steering exists; current whole-organization bargaining over S1 commitments is not wired.
- Why this is / is not agent-owned: the remote controller owns network attachment and delivers user actions but does not allocate resources among independent operational units.
- Evidence: [remote/Controller.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/remote/Controller.zig), [src/State.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/State.zig), [Agent.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/Agent.zig).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: a human can manage several sessions externally; this assessment does not import an external human organization as an internal Drinky S3.

### Absence scope

- Surfaces inspected: one-agent process lifecycle, TUI actions, remote chat control, session state, cost/usage/status and Herdr socket reporting.
- Plausible first-party paths checked: Telegram as S3 manager, terminal user as parent S3, multiple UI endpoints as S1 portfolio and model quota as whole-current budget.
- Why no material first-party path remains: all surfaced controls address the same transient coding session and expose no independent-unit commitment regulation.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary audit judgment with sufficiently independent operational access and returned corrective decision.
- Disturbance / variety regulated: coding claims could be incorrect, but the product does not ship a separate reviewer or independent verification control path.
- Claim being audited: whether model-proposed code edits and reported outcomes are correct.
- Ordinary reporting path: the same Agent records tool stdout/stderr and its own model responses in one transcript.
- Complementary access path: no shipped independent review actor or direct alternative evidence channel beyond ordinary read/search/bash observations and user-authored skills.
- Independence boundary: the transcript, tool output and any self-analysis all belong to the working Agent; external human review is not a first-party audit mode.
- Audit judgment / decisive feedback right: no separate independent risk or correctness verdict owner.
- Decisive decision or feedback right: no S3*-specific judgment right evidenced.
- Decision owner: main coding Agent for current actions; optional user review remains external.
- Supporting / enforcement mechanisms: transcript result slots, tool-error reports, source inspection tools and developer test scripts.
- How findings enter subsequent control: tool results inform the model, but no separately produced independent audit finding is returned to current control.
- Who acts on findings: the Agent reacts to ordinary tool feedback, subject to user steering.
- Closure path: code action → its own tool observation → model continuation exists; separate audit → corrective return is absent.
- Boundary reachability: no built-in reviewer/subagent workflow was found in the shipped seven-tool registry and single-agent loop.
- Why this is / is not agent-owned: the model can critique its own work if prompted, but it has no complementary independent audit mandate and access distinct from its normal task path.
- Evidence: [Agent.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/Agent.zig), [tool/root.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/tool/root.zig), [README.md](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/README.md).
- Basis: explicit + structural bounded absence review.
- Confidence: high.
- Caveats: repository scripts/test-audit.sh is developer test infrastructure, not the runtime's complementary organizational reviewer.

### Absence scope

- Surfaces inspected: shipped tool registry and Agent loop, developer audit script, system prompt, instruction files, skills, remote operator controls and capability descriptions.
- Plausible first-party paths checked: ordinary bash tests as S3*, self-critique, transcript correctness receipts, user-authored reviewer skill and remote human checking.
- Why no material first-party path remains: no independent complementary evidence/judgment owner and return is wired to the distributed product.

## S4 — Outside-and-then intelligence

- State: —
- Function: no future-facing environmental intelligence loop evaluating and adopting new organizational capabilities.
- Disturbance / variety regulated: provider quotas, live catalog changes, project-specific model choice and prompt-history reuse concern current tool availability and user continuity.
- Decisive decision or feedback right: no autonomous prospective capability planning/adoption decision.
- Decision owner: operator chooses provider/model and edits configuration/skills, while providers supply catalog metadata.
- Supporting / enforcement mechanisms: provider model list refresh, quota and cost state, prompt history, model selection and developer backlog.
- Closure path: current service metadata → displayed choices/current model update exists; horizon scan → prospective capability option → adoption/change in organizational control does not.
- Why this is / is not agent-owned: refreshing remote provider metadata and remembering chosen models do not give a first-party adaptation actor decision ownership.
- Evidence: [src/State.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/State.zig), [lib/ai/Catalog.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/lib/ai/Catalog.zig), [BACKLOG.md](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/BACKLOG.md).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: developers may later implement roadmap features; frozen planned work is not current product S4.

### Absence scope

- Surfaces inspected: model catalog and account state, per-turn retries, instruction and skill loading, prompt history, product feature list and developer backlog.
- Plausible first-party paths checked: dynamic catalog as environmental scanning, model switch as adaptation, current provider error response as strategy and future roadmap development as in-boundary S4.
- Why no material first-party path remains: observed actions affect immediate run options or external maintenance rather than a product-owned prospective organizational adaptation cycle.

## S5 — Policy and identity

- State: —
- Function: no installed ultimate organizational identity/purpose decision and authoritative return path.
- Disturbance / variety regulated: local tool risks and workspace trust are not referred into a Drinky constitutional policy forum.
- Decisive decision or feedback right: no identity-level policy controversy adjudication evidenced.
- Decision owner: external user/configuration/developers choose instructions and limits; no first-party S5 authority is installed.
- Supporting / enforcement mechanisms: small system prompt, user AGENTS.md/skills, configured bash time limits and request bounds, external container advice.
- Closure path: prompt/configuration → Agent action constraints is present; ultimate identity dispute → legitimate policy decision → authoritative adoption feedback is absent.
- Why this is / is not agent-owned: the README explicitly states there is no runtime permission gate/sandbox; even an added one would not alone establish ultimate identity/policy governance.
- Evidence: [README.md](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/README.md), [system_prompt.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/system_prompt.zig), [Config.zig](https://github.com/clebert/drinky/blob/868f50c2604a5619238c6235cd63820d9c724c38/src/Config.zig).
- Basis: explicit + structural bounded absence review.
- Confidence: high.
- Caveats: legitimate human decisions over external project rules exist, but no in-boundary whole-organization ultimate-policy closure was found.

### Absence scope

- Surfaces inspected: compiled prompt, skill/instruction loader, configured tool/request limits, model selection, remote pairing controls, source README and developer backlog.
- Plausible first-party paths checked: prompt rules as constitution, paired Telegram operator as S5, system self-description as identity governance and permission/sandbox limitations.
- Why no material first-party path remains: those are task instructions, interface controls or missing security enforcement; no identity-level legitimate decision institution exists inside the assessed product.

## Recursion

Drinky ships one viable task-performing model/tool actor, with bounded parallel read-only tool workers but no separately accountable subagent/child viable system. The Telegram chat, TUI and Herdr pane expose or control the same actor, not new organizational recursion. External vendors, projects and maintainers are outside the chosen recursion.

## Variety and escalation

Drinky amplifies coding response variety through model-selected file/command tools, runtime provider choice and direct user steering. It attenuates operational variety through tool batching, max rounds/tool calls, bash timeouts and unambiguous tool-result receipts. Unexpected risks may be managed by the operator or an external container, but this does not prove internal S2–S5 functions. A developer test script does not supply independent S3* review.

## Evidence gaps

- The reviewed source and first-party README establish one operational model/tool loop, with no credited multi-agent organizational functions; no provider-backed coding effectiveness test was run.
- No agent-specific independent audit or external future-adaptation evidence is imported from developer tests, backlog or user-provided skills.
- Telegram remote control and Herdr status report are interfaces to one session, not separate governance of a population of S1 units.
- Safety caution: the frozen product explicitly lacks a permission gate or sandbox; the S5 negative classification is not a security approval.
