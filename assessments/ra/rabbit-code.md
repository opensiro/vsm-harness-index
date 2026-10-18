---
harness_id: rabbit-code
project_name: rabbit-code
repository: https://github.com/2456868764/rabbit-code
review_ref: c49562fc92b7d6d6930e3ae5e49de8737c580b4f
reviewed_at: 2026-10-11
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

# rabbit-code

## Review boundary

- System in focus: the **actually shipped executable** `cmd/rabbit-code/main.go` at frozen source, its CLI command branches, bootstrap/config/trust flow and the internal Go `query/engine` modules that are present but not reachable as a configured live coding assistant from that binary.
- Purpose and identity: the project aims to develop a Claude Code-class coding agent, but at this revision the executable implements initialization/diagnostics/configuration rather than a user-task tool loop.
- Relevant environment: user shell, bootstrap configuration, Anthropic API/other external providers, potentially constructed Go engine for internal tests, developer roadmap/reference source.
- Standard-distribution boundary: shipped Go `cmd/rabbit-code` binary and its reachable operational modes; internal `query` library implementation is inspected for potential first-party reachability but not credited as an independently operated deployment via tests or hypothetical new first-party caller code.
- Credited operating / distribution surfaces: [cmd/rabbit-code/main.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/cmd/rabbit-code/main.go); [internal/app/bootstrap.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/bootstrap.go); [internal/app/headless_engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/headless_engine.go); [internal/query/engine/engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/engine/engine.go); [internal/query/loop.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/loop.go); [internal/query/default_tool_runner.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/default_tool_runner.go).
- Adjacent first-party surfaces excluded from ownership: developer tests simulating query engine with injected Assistant/ToolRunner, roadmap `docs/phases/`, reference-tree parity notes for Claude Code, API probe, CI and not-yet-integrated feature packages. These may prove component implementations but do not create a shipped operational S1.
- First-party operating / deployment modes considered: CLI config/probe/context/stop-hooks commands, startup/bootstrap/onboarding, ordinary main with default environment, headless shutdown hook; internal `engine.New(cfg)` potential as an unintegrated constructor, not an existing supported binary mode.
- Recursion level: one launched `rabbit-code` CLI process; no running autonomous coding S1 unit in frozen shipped entrypoint.
- Reviewed revision: `c49562fc92b7d6d6930e3ae5e49de8737c580b4f`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`internal/query/loop.go` genuinely contains a model/tool decision continuation, and `engine.New(parent,cfg)` can use it when callers inject Assistant/Turn. However `cmd/rabbit-code/main.go` never creates that mode. It branches into individual config/probe/context/stop-hook utilities, then invokes `app.Bootstrap`, registers `WireHeadlessEngineForShutdown`, runs onboarding/merged config/preconnect, prints `Phase 1 bootstrap OK` and exits. `WireHeadlessEngineForShutdown` explicitly creates `engine.New(parent,nil)` for shutdown-drain only. `New(nil)` has no assistant and `SubmitWithOptions` emits timed stub text rather than entering `runTurnLoop`. [cmd/rabbit-code/main.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/cmd/rabbit-code/main.go); [internal/app/headless_engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/headless_engine.go); [internal/query/engine/engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/engine/engine.go). The query engine and task/team tool types live under Go `internal/` and tests drive them with injected mocks/callers; they do not establish an enabled first-party CLI coding-agent mode. Built-in `NewDefaultToolRunner` registers file/shell operations when a configured engine exists, not in the actual shipped CLI. TeamCreate and Agent tools require callbacks for real execution; without them, they report stubs/errors. [internal/query/default_tool_runner.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/default_tool_runner.go); [internal/tools/teamcreatetool/team_create_tool.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/tools/teamcreatetool/team_create_tool.go); [internal/tools/agenttool/agent_tool.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/tools/agenttool/agent_tool.go).

## Operational model

The compiled CLI can prepare config, contact providers for diagnostics, and run startup/teardown. It cannot yet accept and autonomously work a normal user coding task through its first-party decision/tool/feedback loop. A developer could add a caller invoking the internal query engine, but such future integration cannot be borrowed as current standard distribution behavior. Therefore **canonical disposition is `excluded-no-agentic-vsm` rather than treating component-level test success as an admitted autonomous S1**.

## S1 — Operations

- State: —
- Function: The repository implements reusable Go model/tool-loop code, but the only packaged binary entrypoint never invokes it with a live model/tool session. The main command runs initialization, config/probe/context/stop-hooks branches and exits. It installs a shutdown-only Engine with nil Config and stub Assistant, then prints Phase 1 bootstrap message and terminates.
- Disturbance / variety regulated: not a currently operated autonomous coding organization; candidate task/tool/policy disturbances remain in dormant modules or operator setup.
- Decisive decision or feedback right: no qualifying first-party operational function right reachable from the shipped executable mode.
- Decision owner: human/developer selects startup/configuration; dormant Go constructor requires additional caller integration.
- Supporting / enforcement mechanisms: interfaces, callbacks, state counters, configured tool builders and bootstrapping code under evaluation.
- Closure path: The `LoopDriver.runTurnLoop` source can make tool-use decisions if an outside caller provides an `Assistant/Turn` and invokes `Engine.Submit`; this is a dormant internal SDK surface, not a currently operated first-party CLI S1. It has no exported non-internal host package that can be imported by a third-party module. Source references cannot substitute for a packaged operating mode.
- Why this is / is not agent-owned: the decisive operation cannot run in the included first-party binary boundary; adding an external or future caller is not current ownership.
- Evidence: [cmd/rabbit-code/main.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/cmd/rabbit-code/main.go); [internal/app/headless_engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/headless_engine.go); [internal/query/engine/engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/engine/engine.go); [internal/query/loop.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/loop.go); [internal/query/default_tool_runner.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/default_tool_runner.go).
- Basis: structural.
- Confidence: high for the CLI entrypoint exclusion; medium for claims beyond examined source.
- Caveats: Go package modules are real implementations and may become included once they are wired into a supported runnable mode; no assertion of universal impossibility.

### Absence scope

- Surfaces inspected: entrypoint, standalone subcommands, bootstrap, engine wiring, query engine and tool registry.
- Plausible first-party paths checked: live API assistant initialization, CLI invocation, test-only model loop and headless library constructor.
- Why no material first-party path remains: The standard binary never constructs a live configured agent or receives user coding tasks; model-driven loop exists as internal code but lacks an operating path in the supported distribution..

## S2 — Coordination

- State: —
- Function: No operating first-party multi-S1 relationship exists at this frozen binary recursion. Generic tools, TeamCreate and SendMessage structures are API mirrors, with nil-callback fallbacks returning stubs rather than delivering team work.
- Disturbance / variety regulated: not a currently operated autonomous coding organization; candidate task/tool/policy disturbances remain in dormant modules or operator setup.
- Decisive decision or feedback right: no qualifying first-party operational function right reachable from the shipped executable mode.
- Decision owner: human/developer selects startup/configuration; dormant Go constructor requires additional caller integration.
- Supporting / enforcement mechanisms: interfaces, callbacks, state counters, configured tool builders and bootstrapping code under evaluation.
- Closure path: Model/tool scheduling in a dormant loop is not autonomous inter-S1 coordination; no actually running independent coding S1s generate a concrete collision and attenuating return.
- Why this is / is not agent-owned: the decisive operation cannot run in the included first-party binary boundary; adding an external or future caller is not current ownership.
- Evidence: [internal/tools/teamcreatetool/team_create_tool.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/tools/teamcreatetool/team_create_tool.go); [internal/tools/sendmessagetool/send_message_tool.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/tools/sendmessagetool/send_message_tool.go); [internal/tools/agenttool/agent_tool.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/tools/agenttool/agent_tool.go); [internal/query/default_tool_runner.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/default_tool_runner.go).
- Basis: structural.
- Confidence: high for the CLI entrypoint exclusion; medium for claims beyond examined source.
- Caveats: Go package modules are real implementations and may become included once they are wired into a supported runnable mode; no assertion of universal impossibility.

### Absence scope

- Surfaces inspected: agent/team message tools, default registry, query scheduling and task package.
- Plausible first-party paths checked: TeamCreate OnTeamCreate, SendMessage SendMsg, Agent RunAgent and external child runtime wiring.
- Why no material first-party path remains: Callbacks for real teammate execution are not registered in the shipped runtime; tool schemas, stub outputs and generic turn sequencing cannot close an inter-S1 interference relation..

## S3 — Inside-and-now control

- State: —
- Function: There is no operated coding-agent organization whose current shared resource/task commitments are regulated by a first-party S3 authority. Context budgets, token counters, trust settings and API fallback code are enforcement mechanisms for a hypothetical assembled engine.
- Disturbance / variety regulated: not a currently operated autonomous coding organization; candidate task/tool/policy disturbances remain in dormant modules or operator setup.
- Decisive decision or feedback right: no qualifying first-party operational function right reachable from the shipped executable mode.
- Decision owner: human/developer selects startup/configuration; dormant Go constructor requires additional caller integration.
- Supporting / enforcement mechanisms: interfaces, callbacks, state counters, configured tool builders and bootstrapping code under evaluation.
- Closure path: No live managing agent or parent operator protocol consumes a whole-current operating view and returns resource/priority interventions across real executing S1s.
- Why this is / is not agent-owned: the decisive operation cannot run in the included first-party binary boundary; adding an external or future caller is not current ownership.
- Evidence: [internal/query/engine/engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/engine/engine.go); [internal/query/state.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/state.go); [internal/query/token_budget.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/token_budget.go); [internal/app/bootstrap.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/bootstrap.go).
- Basis: structural.
- Confidence: high for the CLI entrypoint exclusion; medium for claims beyond examined source.
- Caveats: Go package modules are real implementations and may become included once they are wired into a supported runnable mode; no assertion of universal impossibility.

### Absence scope

- Surfaces inspected: configuration, query state, budget counters, engine retry, bootstrap and permission tools.
- Plausible first-party paths checked: whole-current agent view, manager decision right, shared resource intervention and returned task state.
- Why no material first-party path remains: Only local runtime control implementations or bootstrap metadata are reachable, not an S3 managerial decision-and-return loop..

## S3* — Complementary audit

- State: —
- Function: No first-party live coding producer and independent complementary auditor operate through this CLI. Developer CI/tests and configured stop-hook parser cannot be an audit of an executing agent's factual completion claims.
- Disturbance / variety regulated: not a currently operated autonomous coding organization; candidate task/tool/policy disturbances remain in dormant modules or operator setup.
- Decisive decision or feedback right: no qualifying first-party operational function right reachable from the shipped executable mode.
- Decision owner: human/developer selects startup/configuration; dormant Go constructor requires additional caller integration.
- Supporting / enforcement mechanisms: interfaces, callbacks, state counters, configured tool builders and bootstrapping code under evaluation.
- Closure path: In the unintegrated query engine, stop-hooks may be called if an embedding config provides them, but the shipped binary does not submit coding work, let alone verify claimed completion from independent raw evidence.
- Why this is / is not agent-owned: the decisive operation cannot run in the included first-party binary boundary; adding an external or future caller is not current ownership.
- Evidence: [internal/query/engine/engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/engine/engine.go); [internal/tools/registry/registry.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/tools/registry/registry.go); [internal/app/headless_engine.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/headless_engine.go); [.github/workflows/ci.yml](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/.github/workflows/ci.yml).
- Basis: structural.
- Confidence: high for the CLI entrypoint exclusion; medium for claims beyond examined source.
- Caveats: Go package modules are real implementations and may become included once they are wired into a supported runnable mode; no assertion of universal impossibility.

### Absence scope

- Surfaces inspected: stop hooks, developer test infrastructure, engine events and parser.
- Plausible first-party paths checked: independent task claim, direct-source audit findings, authoritative corrective return.
- Why no material first-party path remains: No shipped running producer/checker organization or independent findings-to-control closure exists; code comments on future parity are not an audit owner..

## S4 — Outside-and-then intelligence

- State: —
- Function: Memory-directory resolver, auto-compaction, user settings and context recovery code manage immediate context and hypothetical future recall, without an operated prospective external-scan and capability-adaptation process.
- Disturbance / variety regulated: not a currently operated autonomous coding organization; candidate task/tool/policy disturbances remain in dormant modules or operator setup.
- Decisive decision or feedback right: no qualifying first-party operational function right reachable from the shipped executable mode.
- Decision owner: human/developer selects startup/configuration; dormant Go constructor requires additional caller integration.
- Supporting / enforcement mechanisms: interfaces, callbacks, state counters, configured tool builders and bootstrapping code under evaluation.
- Closure path: An internal memory helper alone is not future options evaluation; the actual CLI only initializes/shuts down, with no agent task capability that could be modified by a source-evidenced S4 decision.
- Why this is / is not agent-owned: the decisive operation cannot run in the included first-party binary boundary; adding an external or future caller is not current ownership.
- Evidence: [internal/query/engine/memdir_bootstrap.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/engine/memdir_bootstrap.go); [internal/query/engine/auto_compact_chain.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/query/engine/auto_compact_chain.go); [internal/app/engine_memdir.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/engine_memdir.go); [cmd/rabbit-code/main.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/cmd/rabbit-code/main.go).
- Basis: structural.
- Confidence: high for the CLI entrypoint exclusion; medium for claims beyond examined source.
- Caveats: Go package modules are real implementations and may become included once they are wired into a supported runnable mode; no assertion of universal impossibility.

### Absence scope

- Surfaces inspected: memory directories, context helpers, API recovery and config setup.
- Plausible first-party paths checked: external prospective signal, capability option, accepted future adaptation and returned operating change.
- Why no material first-party path remains: No first-party live future-oriented adaptation cycle is completed, and memory/context support is not promoted to S4..

## S5 — Policy and identity

- State: —
- Function: Configured trust rules and bootstrap policy are developer/user access controls; the frozen binary does not operate a legitimate organizational ultimate-policy issue-and-return authority.
- Disturbance / variety regulated: not a currently operated autonomous coding organization; candidate task/tool/policy disturbances remain in dormant modules or operator setup.
- Decisive decision or feedback right: no qualifying first-party operational function right reachable from the shipped executable mode.
- Decision owner: human/developer selects startup/configuration; dormant Go constructor requires additional caller integration.
- Supporting / enforcement mechanisms: interfaces, callbacks, state counters, configured tool builders and bootstrapping code under evaluation.
- Closure path: Per-operation tool guard or startup trust prompt does not make an S5 identity authority without deliberation and consequential return into an operating coding organization.
- Why this is / is not agent-owned: the decisive operation cannot run in the included first-party binary boundary; adding an external or future caller is not current ownership.
- Evidence: [internal/app/bootstrap.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/bootstrap.go); [internal/app/trust_storage.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/app/trust_storage.go); [internal/tools/bashtool/bash_security.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/internal/tools/bashtool/bash_security.go); [cmd/rabbit-code/main.go](https://github.com/2456868764/rabbit-code/blob/c49562fc92b7d6d6930e3ae5e49de8737c580b4f/cmd/rabbit-code/main.go).
- Basis: structural.
- Confidence: high for the CLI entrypoint exclusion; medium for claims beyond examined source.
- Caveats: Go package modules are real implementations and may become included once they are wired into a supported runnable mode; no assertion of universal impossibility.

### Absence scope

- Surfaces inspected: trust/config, tool permission and bootstrap surfaces.
- Plausible first-party paths checked: identity/policy dispute trigger, legitimate deciding authority and binding returned policy.
- Why no material first-party path remains: No source-evidenced S5 deciding actor, issue path or returned change to operational identity/policy is shipped..

## Recursion

No running autonomous S1 coding unit is established inside the only packaged command. The unintegrated internal query-loop implementation is a potential future lower recursion, not a presently operated child or parent organization.

## Variety and escalation

Current variety is configuration, initialization, probes and source component testing. Error recovery and state capture in `internal/query` could later regulate model/tool operating disturbances, but they are not exercised by the shipped binary.

## Evidence gaps

- No production trace is claimed. The decisive first-party boundary is directly visible in the frozen binary entrypoint, startup wire and stub engine semantics.
- This is not a claim that no source code for an agent loop exists; the distinction is its lack of shipped executable reachability. If a separate documented supported deployment executable exists outside this pinned distribution, a fresh same-ref review with concrete first-party evidence is appropriate.
