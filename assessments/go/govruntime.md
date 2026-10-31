---
harness_id: govruntime
project_name: GovRuntime
repository: https://github.com/obmakesomething/govruntime
review_ref: 96bd0e1d34822c9e599734d37d00d8c307c058df
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# GovRuntime

## Review boundary

- System in focus: the shipped GovRuntime `@govruntime/govd`, `@govruntime/govctl` and read-only MCP governance runtime operating alongside an external coding agent.
- Purpose and identity: persist mandate/scope/evidence, judge normalized agent lifecycle/tool events against constitutional and repository policy, and return allow/warn/block/context without becoming the agent's task performer.
- Relevant environment: external Codex/Claude Code/Cursor workers, their repositories and hook events, operator-authored `.governance/` policy/cases/tickets, optional OPA, Linear packets and CI.
- Standard-distribution boundary: TypeScript policy/judgment/intent/docket/hook engine, CLI case/decision/ticket/branch commands, Claude/Codex adapters and read-only MCP posture tools; external agent binaries, model prompts/reasoning and their tool execution are outside.
- Credited operating / distribution surfaces: `README.md`, `docs/architecture.md`, `docs/policy-engine.md`, `packages/govd/src/{intent/analyzer,judgment/engine,policy/engine,handlers/pre_tool_use,state/loader,decision/engine,context/pack_renderer}.ts`, `packages/govctl/src/{commands/hook,hooks/codex_adapter,hooks/claude_code_adapter,gov}.ts`, `packages/mcp-server/src/index.ts`.
- Adjacent first-party surfaces excluded from ownership: development/CI, examples, tests, seed policy pack fixtures, release marketing and unimplemented phase-2 model-intent analyzer; they do not supply an operational autonomous agent.
- First-party operating / deployment modes considered: local `govctl` CLI, Codex/Claude hooks, advisory and hard-block policy modes, OPA or built-in engine, long-running `gov` case recorder/closure, read-only MCP server, optional Linear packet exports.
- Recursion level: GovRuntime as the first-party governance runtime around an agent session; the external coding agent may be viable independently but is not reclassified as owned by GovRuntime.
- Reviewed revision: `obmakesomething/govruntime@96bd0e1d34822c9e599734d37d00d8c307c058df`; frozen intake #2473/controller #2474 row 4, historical #188 row 9.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/README.md) explicitly states **“Not an agent framework”** and distinguishes “Agent framework: does the work” from “GovRuntime: governs how the work is authorized, scoped, checked, and recorded.” The [architecture](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/docs/architecture.md) specifies `govd` engine → `govctl` adapters → external product hooks, with user/developer-authored constitution, precedents and cases. It logs tool attempts, enforces scope, audit/evidence and stop posture; it does not select substantive code edits.

The apparently agentic [intent analyzer](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/intent/analyzer.ts) explicitly says phase 1 is **heuristic pattern matching** and a structured model call is reserved for phase 2+. Its `detectDeltaType`, `extractNewFacts` and `deriveNextAction` classify keywords and copy prompt facts; no model call or agent/tool loop exists. The [judgment engine](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/judgment/engine.ts) obtains allow/warn/review/block from deterministic built-in/OPA policy, path validation and configured enforcement modes, then writes a judgment to state. [PreToolUse](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/handlers/pre_tool_use.ts) returns that judgment to the external host. [Decision engine](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/decision/engine.ts) records operator-specified decisions and checks file patterns against stored invariants, not independent model-created governance.

The [MCP server](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/mcp-server/src/index.ts) advertises read-only `gov_current_posture`, `gov_current_ticket` and `gov_why`, where docket-derived narrative explicitly uses no model inference. [CLI case runner](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govctl/src/gov.ts) registers externally produced runs/stages, proof hashes, event logs and gate closure; recording a model-call ID does not make GovRuntime the model caller. The [Codex](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govctl/src/hooks/codex_adapter.ts) and [Claude](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govctl/src/hooks/claude_code_adapter.ts) adapters normalize external lifecycle events and return hook decisions/context.

Counterfactual owner test: remove external Codex/Claude/model-agent hosts. GovRuntime still records tickets, returns context packs, validates literals, writes audit entries and blocks hypothetical tool events, but cannot interpret a coding objective into code/tool operations, observe results and select the next substantive act. Its `next_best_action` and `judgment` names are deterministic procedural recommendations, not first-party agent ownership. Canonical outcome: **`excluded-no-agentic-vsm`** at this first-party boundary.

## Operational model

An operator stores constitution/case/ticket/decision state. An *external* agent emits SessionStart/UserPrompt/PreToolUse/PostToolUse/Stop; the adapter loads state, heuristically classifies user wording, evaluates a rule/OPA condition and returns an allow/warn/block/context response. GovRuntime records results and can issue packets for external collaboration tools. It neither starts nor governs its own model/tool execution loop. Its strong audit and approval functionality remains valuable but is not a surrogate autonomous organization.

## S1 — Operations

- State: —
- Function: agent-owned substantive coding work would select edits/tools from objectives and repository feedback.
- Disturbance / variety regulated: open-ended coding tasks and tool observations; GovRuntime regulates scope, evidence, ticket state, tool authorization and exit conditions.
- Decisive decision or feedback right: choose the next semantic repository action or code change in response to observed work.
- Decision owner: external coding agent (Codex/Claude/etc.); human/user owns task mandate and policy.
- Supporting / enforcement mechanisms: policy engine, hook adapters, context packs, docket/audit, case CLI, MCP posture tools and deterministic prompt-delta classification.
- Closure path: external agent proposes tool call → GovRuntime deterministic policy block/warn/allow → external agent continues its own reasoning/tool loop. GovRuntime closes permission and audit, not task semantics.
- Why this is / is not agent-owned: no active model invocation or action-selection loop is shipped. The advertised model intent path is labeled *future phase 2*.
- Evidence: [README boundary](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/README.md); [intent analyzer](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/intent/analyzer.ts); [MCP server](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/mcp-server/src/index.ts).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: an external governed coding agent can be autonomously viable, but its autonomy is not imported.

### Absence scope

- Surfaces inspected: README/architecture, `govd` intent, hook/judgment/policy, `govctl` CLI and case-runner, MCP server and platform adapters.
- Plausible first-party paths checked: `next_best_action` intent keyword path, `PreToolUse` verdict, `gov` registered stages, MCP context exposure and planned phase-2 LLM call.
- Why no material first-party path remains: all live paths classify/enforce/report externally selected work; promised structured model inference is not implemented.

## S2 — Coordination

- State: —
- Function: attenuate inter-S1 conflict or oscillation between independent operating units and feed coordination back to their future actions.
- Disturbance / variety regulated: parallel agent-process ID collisions and overlapping branch/ticket scope are anticipated; these are data integrity and policy concerns, not demonstrated S1 peer autonomy.
- Decisive decision or feedback right: negotiate/resolve conflicting peer operational commitments and return changed behaviour to each affected agent.
- Decision owner: no first-party pair of autonomous S1s or S2 conflict authority; external agents choose actions, deterministic file-lock/ID and ticket rules enforce reservations.
- Supporting / enforcement mechanisms: persistent unique entity sequences, file locks, branch ledger, scope conflict detector and hook blocks.
- Closure path: concurrent state/hook input → lock/ID/policy checks → warning/block/single caller response; no peer conflict-resolution decision with both agents' subsequent action changes is wired.
- Why this is / is not agent-owned: “collision-safe” is an integrity guarantee. Conflict detector checks scope/policy, not agentic mutual interference mediation.
- Evidence: [conflict detector](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/conflict/detector.ts); [ID store](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/state/id_store.ts); [README release notes](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/README.md).
- Basis: structural negative.
- Confidence: high.
- Caveats: supported teams may compose GovRuntime with a separate multi-agent coordinator.

### Absence scope

- Surfaces inspected: IDs/locks, conflict detector, branch/ticket ledger, hook adapters, judgments and case state.
- Plausible first-party paths checked: concurrent process collision prevention, scope drift, branch conflict/recovery, ticket reissue.
- Why no material first-party path remains: no distinct GovRuntime-owned S1 peer units or S2-specific interference/attenuation/feedback relation; deterministic integrity and local enforcement are not S2.

## S3 — Inside-and-now control

- State: —
- Function: decide whole-system present resource, priority and commitment interventions for an operating agent organization.
- Disturbance / variety regulated: off-scope changes, missing evidence, unsafe tool calls, dirty stop and incomplete ticket criteria.
- Decisive decision or feedback right: evaluate whole current operations and change shared priorities/resources/accountability rather than merely permit a particular call.
- Decision owner: user/operator constitution and tickets supply constraints; `judgeToolCall` and `judgeCompletion` enforce configured policy on individual events.
- Supporting / enforcement mechanisms: advisory/hard-block modes, OPA, current posture, path checks, clean-state log, verdict and ticket diagnostics.
- Closure path: rule input → deterministic judgment → external host allowed/blocked/context-injected; no independent current whole-system management decision authority or return loop.
- Why this is / is not agent-owned: a policy engine can block a tool but does not choose whole-system operational tradeoffs; posture/status does not itself supply S3 decisor.
- Evidence: [judgment engine](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/judgment/engine.ts); [architecture modes](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/docs/architecture.md); [case CLI](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govctl/src/gov.ts).
- Basis: structural negative.
- Confidence: high.
- Caveats: human sponsors can govern a larger development organization, but a complete first-party parent S3 mode cannot be credited from local hook approvals.

### Absence scope

- Surfaces inspected: control engine, context pack, CLI current case/ticket, advisory/hard-block decisions, plan/stop hooks and evidence/proof checks.
- Plausible first-party paths checked: status snapshot → current intervention, manual ticket reissue, human review required, production mode setting.
- Why no material first-party path remains: no evidenced whole-system discretionary allocation authority with returned change to operations; observed gates enforce preselected constraints on individual acts.

## S3* — Complementary audit

- State: —
- Function: independent complementary reality inspection that can challenge ordinary operational reporting and return corrective findings to S3.
- Disturbance / variety regulated: unverifiable claimed completion, missing proofs, tampered records and unsafe changes.
- Decisive decision or feedback right: an independent audit owner evaluates raw reality beyond the ordinary control/report path, then requires correction.
- Decision owner: deterministic ledger/checksum/policy readers and external human auditors; no separate autonomous or constructor-owned complementary audit authority.
- Supporting / enforcement mechanisms: append-only audit, evidence references, hash verification, path literals, docket, ticket exit checks and `gov audit verify`.
- Closure path: same external lifecycle events → governance records/validation → routine warning/block or optional human inspection; no separate independent audit judgment/return to whole-system control.
- Why this is / is not agent-owned: audit-trail integrity and replay are important but not independent S3* merely by naming a ledger “audit”.
- Evidence: [audit ledger docs](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/docs/audit-ledger.md); [ledger implementation](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/audit/ledger.ts); [judgment code](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/judgment/engine.ts).
- Basis: structural negative.
- Confidence: high.
- Caveats: third-party independent auditors can use the logs, but are not packaged into a complementary operating feedback channel.

### Absence scope

- Surfaces inspected: ledger/audit verifier, hook event capture, judgment logs, evidence registry, stop check and MCP posture.
- Plausible first-party paths checked: audit hash verification, receipt/proof requirements, clean exit and independent replay.
- Why no material first-party path remains: verification is routine integrity and policy checking of the same operational event stream, with no independently owned alternative audit/return loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: sense external future conditions, develop adaptation options and return decisions that alter present system capability.
- Disturbance / variety regulated: changing coding tools, policy expectations, future task environments and enterprise governance.
- Decisive decision or feedback right: prospectively choose and deploy adaptive governance/agent capabilities from environmental foresight.
- Decision owner: developer/operator authors new packs, invariants and tools; no model-driven prospective innovation/selection exists in shipped runtime.
- Supporting / enforcement mechanisms: precedent/evidence/decision store, case reissue, Linear packet generation, pack install, planned phase-2 intent inference.
- Closure path: human policy edits/new precedent → deterministic enforcement update on next hook; no external-and-then autonomous strategy cycle or distinct parent adaptation loop at assessed agent recursion.
- Why this is / is not agent-owned: preserving memory and revising a ticket after explicit user correction does not make GovRuntime an environmental-intelligence function.
- Evidence: [intent analyzer phase distinction](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/intent/analyzer.ts); [decision/invariant engine](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/decision/engine.ts); [case workflow](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/README.md).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: workflow knowledge survives sessions and may improve external agents, but S4 requires a prospective organizational adaptation owner.

### Absence scope

- Surfaces inspected: intent analyzer, packs/precedents, decision record, ticket reissue, external Linear packet, case CLI and roadmap docs.
- Plausible first-party paths checked: future phase-2 model call, retrospective decisions, human new rules and generated context packs.
- Why no material first-party path remains: only deterministic/governance-record changes under user initiative are shipped; no prospective sensing/options/authorized capability-change loop.

## S5 — Policy and identity

- State: —
- Function: settle ultimate identity/policy tensions for the first-party viable agent organization and return binding authority to operation.
- Disturbance / variety regulated: policy hierarchy, contradictory mandates, destructive action, enterprise security and user overrides.
- Decisive decision or feedback right: choose the system's legitimate ultimate identity/authority when conflicting control and adaptation matters arise.
- Decision owner: human/enterprise policy authors; the runtime deterministically orders configured constitution/statutes/precedents and enforces the outcome.
- Supporting / enforcement mechanisms: `.governance/constitution.yaml`, policy packs, OPA/builtin rules, `recordDecision`, invariants and human review requirements.
- Closure path: operator-authored rule hierarchy → deterministic allow/warn/block/context → external coding-agent action. No first-party legitimate identity-level arbitration owner with a separately evidenced return to autonomous CK operation.
- Why this is / is not agent-owned: the source's own preset explicitly says “model is not the court”; policy recording and enforcement are not system identity choice.
- Evidence: [init default constitution/precedents](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govctl/src/commands/init.ts); [decision engine](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/decision/engine.ts); [policy engine](https://github.com/obmakesomething/govruntime/blob/96bd0e1d34822c9e599734d37d00d8c307c058df/packages/govd/src/policy/engine.ts).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: genuine organizational governance can exist upstream; the published assessment does not deny that human authority, but does not borrow it as a first-party agentic S5 mode.

### Absence scope

- Surfaces inspected: constitution defaults, pack/invariant/decision commands, policy engine, judgment/approval, ticket and hook return.
- Plausible first-party paths checked: higher-authority override resolution, human gate, company precedent update, exported context pack.
- Why no material first-party path remains: these implement externally authored policy, not autonomous ultimate-policy settlement or a complete eligible first-party parent identity loop at the assessed runtime boundary.

## Distributed OSS parent arrangement

The repository's contributors and real enterprise policy authors can decide features and constraints. Their external rights are not made into a packaged, functionally closed S3/S4/S5 parent organization merely because the CLI supports versioned decisions. Hook policy authoring and PR governance are adjacent or higher recursion.

## Recursion

Separate coding-agent hosts may support viable nested organizations, and GovRuntime cases/tickets can span long work periods. Neither a case directory nor event streams create first-party autonomous operational units. The first-party evaluated entity is a governance layer, so the general Index inclusion boundary fails at S1.

## Variety and escalation

GovRuntime attenuates scope drift by persistent cases, ticket acceptance, path verification and allow/warn/block. It returns exceptional findings and human-review requirements through hooks, preserving audit evidence. These may be valuable escalation paths to an external user's authority, but an event/`BLOCKED` status is not itself S3/S4/S5 or a fully evidenced algedonic response chain at this recursion.

## Evidence gaps

No external Codex/Claude execution or OPA/cloud integration was run; the shipped source call graph and documentation were inspected at frozen SHA. A planned phase-2 structured model analyzer is expressly not active and cannot be counted. The negative states are bounded to this governance runtime, not a claim about autonomous capabilities of products that consume its hooks or MCP context.
