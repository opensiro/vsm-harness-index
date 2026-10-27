---
harness_id: mi
project_name: mi
repository: https://github.com/pegov/mi
review_ref: 858f24223a194f6a1709e821a63eb72a3e716f32
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mi

## Review boundary

- System in focus: one installed mi terminal coding-agent session at the pinned source revision.
- Purpose and identity: transform a user's coding request into workspace investigation, file changes, shell actions and an answer.
- Relevant environment: local files and OS processes, configured local/OpenRouter/Jev endpoints, model context and user input.
- Standard-distribution boundary: Cargo-built Rust binary and its bundled session, compaction, skill, terminal and tool implementations; the user's model endpoint and instruction files are inputs.
- Credited operating / distribution surfaces: [Cargo.toml](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/Cargo.toml), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs), [src/chat.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/chat.rs), [src/tool/mod.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/tool/mod.rs), [src/xdg.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/xdg.rs).
- Adjacent first-party surfaces excluded from ownership: source-level tests, MCP echo/server transport and diagnostic logging do not supply an independent auditor or a second organization; no separate shipped development/governance agent was identified in the 36-entry source tree.
- First-party operating / deployment modes considered: local endpoint, OpenRouter and Jev command paths, interactive/resume and one-shot execution; instruction presets and skills. MCP clients/server are generic integration paths rather than borrowed governance.
- Recursion level: the coding session as the operational system, not an external host organization or upstream model provider.
- Reviewed revision: `858f24223a194f6a1709e821a63eb72a3e716f32`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

mi is a Rust terminal application. `run_chat` builds the system prompt, discovers local skills, registers read/tail/write/edit/bash tools and sends the active session to a configured model endpoint. It assembles streamed responses, dispatches model-selected calls and appends each result to the next model input. Session JSON is atomically saved and can be resumed. Context compaction creates a summary with retained recent messages, checks that it reduces context, and persists the candidate; one bounded recovery handles overflow/truncation.

Configuration selects model profiles, reasoning and prompt presets; root AGENTS.md and local skills supply instructions. Terminal events collect user requests and interrupts. Credits/context/status displays, transcript/logging and optional MCP transports support execution. The source does not package a multi-agent portfolio, audit actor or adaptive governance controller. There is no README at this pin; architecture was recovered from executable source rather than inferred from missing documentation.

Primary architecture: [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L461-L544), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L972-L1023), [src/chat.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/chat.rs#L24-L104), [src/xdg.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/xdg.rs#L8-L96), [src/skill.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/skill.rs#L94-L123).

## Operational model

The S1 unit is the active model-backed coding loop. The user selects the goal and configured constraints; within a turn the agent chooses which available action to take, its arguments and how to react to returned results. Rust dispatch, persistence, terminal UI and compaction enforce/support those choices. Removing the model's action selection leaves transport and predefined recovery, not materially the same discretionary coding decisions. Different model endpoints are alternative deployments of that unit, not separate coordinated S1s.

## S1 — Operations

- State: A
- Function: perform the requested coding transformation through iterative observation and action.
- Disturbance / variety regulated: unknown workspace contents, command errors, evolving files and intermediate results.
- Decisive decision or feedback right: select the next tool and arguments, interpret its result and continue or answer.
- Decision owner: the configured model acting as the coding agent.
- Supporting / enforcement mechanisms: tool registry, streaming assembler, OS/file tools, bounded error recovery and atomic session storage.
- Closure path: model tool call → actual tool result/error → Tool message saved in session → subsequent model request; a turn can contain multiple calls without a new human decision.
- Boundary reachability: `run_chat` directly installs tools and drives the repeated model/tool loop in the binary's supported execution modes; no custom agent wiring is needed.
- Why this is / is not agent-owned: the dispatcher executes model-selected actions; it does not select a fixed solution. Human goal/model choice does not decide every operational step.
- Evidence: [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L490-L529), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L686-L728), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L972-L1023), [src/chat.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/chat.rs#L24-L48).
- Basis: structural.
- Confidence: high for the source-defined loop.
- Caveats: provider/model availability and tool privileges are deployment conditions; no live model run or coding-quality measurement was performed.

## S2 — Coordination

- State: —
- Function: inter-unit coordination; no material first-party closure established in this boundary.
- Disturbance / variety regulated: Multiple model/tool requests and MCP integration do not establish multiple S1 units jointly regulating a shared disturbance.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: none established for this function; local configuration/user choices and coding decisions retain their ordinary owners.
- Supporting / enforcement mechanisms: the inspected controls support the coding loop and do not inherit this function.
- Closure path: no qualifying function-specific feedback/return path found.
- Why this is / is not agent-owned: Parallel network/terminal threads transport one session; tools are actions of that session. No first-party reservation, negotiation or conflict-feedback relation among distinct S1s was found.
- Evidence: [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L461-L1106), [src/cmd.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/cmd.rs).
- Basis: structural.
- Confidence: medium-high, bounded to the pinned distribution.
- Caveats: arbitrary externally supplied skills or surrounding organizations could implement additional functions; they are not credited.

### Absence scope

- Surfaces inspected: tool dispatch, the single active session, MCP sync transport and skill loading; executable command wiring and full top-level source inventory.
- Plausible first-party paths checked: Multiple model/tool requests and MCP integration do not establish multiple S1 units jointly regulating a shared disturbance.
- Why no material first-party path remains: Parallel network/terminal threads transport one session; tools are actions of that session. No first-party reservation, negotiation or conflict-feedback relation among distinct S1s was found.

## S3 — Inside-and-now control

- State: —
- Function: whole-current cohesion; no material first-party closure established in this boundary.
- Disturbance / variety regulated: Credits, context limits, model switching and interruption provide local execution controls, not a whole-system current-regulation decision over an operational portfolio.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: none established for this function; local configuration/user choices and coding decisions retain their ordinary owners.
- Supporting / enforcement mechanisms: the inspected controls support the coding loop and do not inherit this function.
- Closure path: no qualifying function-specific feedback/return path found.
- Why this is / is not agent-owned: No portfolio/current-control actor or function-specific parent supervisory return is wired. User adjustments regulate one task/configuration; predefined compaction and token limits do not own whole-system discretion.
- Evidence: [src/xdg.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/xdg.rs), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L461-L1106), [src/cmd.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/cmd.rs).
- Basis: structural.
- Confidence: medium-high, bounded to the pinned distribution.
- Caveats: arbitrary externally supplied skills or surrounding organizations could implement additional functions; they are not credited.

### Absence scope

- Surfaces inspected: status/credits, /model and /reasoning commands, compaction settings, interruption and endpoint modes; executable command wiring and full top-level source inventory.
- Plausible first-party paths checked: Credits, context limits, model switching and interruption provide local execution controls, not a whole-system current-regulation decision over an operational portfolio.
- Why no material first-party path remains: No portfolio/current-control actor or function-specific parent supervisory return is wired. User adjustments regulate one task/configuration; predefined compaction and token limits do not own whole-system discretion.

## S3* — Complementary audit

- State: —
- Function: complementary independent challenge; no material first-party closure established in this boundary.
- Disturbance / variety regulated: Logs, tool errors and session validation expose the same production path; no separately controlled complementary claim audit is shipped.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: none established for this function; local configuration/user choices and coding decisions retain their ordinary owners.
- Supporting / enforcement mechanisms: the inspected controls support the coding loop and do not inherit this function.
- Closure path: no qualifying function-specific feedback/return path found.
- Why this is / is not agent-owned: These are ordinary telemetry/integrity and the coder's own feedback, without independent audit judgment, alternate inspection mandate or corrective audit return.
- Evidence: [src/chat.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/chat.rs), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L461-L1106), [src/cmd.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/cmd.rs).
- Basis: structural.
- Confidence: medium-high, bounded to the pinned distribution.
- Caveats: arbitrary externally supplied skills or surrounding organizations could implement additional functions; they are not credited.

### Absence scope

- Surfaces inspected: log/SSE capture, session.validate, tools returning errors, MCP echo/server and compaction validation; executable command wiring and full top-level source inventory.
- Plausible first-party paths checked: Logs, tool errors and session validation expose the same production path; no separately controlled complementary claim audit is shipped.
- Why no material first-party path remains: These are ordinary telemetry/integrity and the coder's own feedback, without independent audit judgment, alternate inspection mandate or corrective audit return.

## S4 — Outside-and-then intelligence

- State: —
- Function: external prospective capability adaptation; no material first-party closure established in this boundary.
- Disturbance / variety regulated: Model metadata fetches, prompt presets, skills and context compaction do not build externally oriented future adaptation options and return them to current capability.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: none established for this function; local configuration/user choices and coding decisions retain their ordinary owners.
- Supporting / enforcement mechanisms: the inspected controls support the coding loop and do not inherit this function.
- Closure path: no qualifying function-specific feedback/return path found.
- Why this is / is not agent-owned: Model information configures the current request; skills load supplied instructions and compaction preserves context. No first-party prospective adaptation owner/options/current-capability loop or qualifying parent mode is wired.
- Evidence: [src/skill.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/skill.rs), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L461-L1106), [src/cmd.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/cmd.rs).
- Basis: structural.
- Confidence: medium-high, bounded to the pinned distribution.
- Caveats: arbitrary externally supplied skills or surrounding organizations could implement additional functions; they are not credited.

### Absence scope

- Surfaces inspected: get_model_info, configuration profiles, skill discovery and compaction preparation/summary/recovery; executable command wiring and full top-level source inventory.
- Plausible first-party paths checked: Model metadata fetches, prompt presets, skills and context compaction do not build externally oriented future adaptation options and return them to current capability.
- Why no material first-party path remains: Model information configures the current request; skills load supplied instructions and compaction preserves context. No first-party prospective adaptation owner/options/current-capability loop or qualifying parent mode is wired.

## S5 — Policy and identity

- State: —
- Function: ultimate identity/policy closure; no material first-party closure established in this boundary.
- Disturbance / variety regulated: System prompt presets, AGENTS.md and user commands constrain operations but do not establish a runtime identity-policy issue/authority/return loop.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: none established for this function; local configuration/user choices and coding decisions retain their ordinary owners.
- Supporting / enforcement mechanisms: the inspected controls support the coding loop and do not inherit this function.
- Closure path: no qualifying function-specific feedback/return path found.
- Why this is / is not agent-owned: The user can replace instructions, but the distribution supplies no function-specific identity-policy deliberation/escalation and authoritative return; no internal autonomous S5 or qualified parent loop is evidenced.
- Evidence: [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs), [src/main.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/main.rs#L461-L1106), [src/cmd.rs](https://github.com/pegov/mi/blob/858f24223a194f6a1709e821a63eb72a3e716f32/src/cmd.rs).
- Basis: structural.
- Confidence: medium-high, bounded to the pinned distribution.
- Caveats: arbitrary externally supplied skills or surrounding organizations could implement additional functions; they are not credited.

### Absence scope

- Surfaces inspected: build_system_prompt, profiles/presets, root instructions, terminal input and local skill invocation; executable command wiring and full top-level source inventory.
- Plausible first-party paths checked: System prompt presets, AGENTS.md and user commands constrain operations but do not establish a runtime identity-policy issue/authority/return loop.
- Why no material first-party path remains: The user can replace instructions, but the distribution supplies no function-specific identity-policy deliberation/escalation and authoritative return; no internal autonomous S5 or qualified parent loop is evidenced.

## Distributed OSS parent arrangement

The MIT-licensed repository and its human maintainer do not become the deployed session's parent metasystem through co-location. No organization-level S3/S4/S5 loop is credited; local user configuration was checked separately above.

## Self-hosted and non-human modes

Local endpoint and hosted endpoint modes retain the same coding-loop ownership. Self-hosting, prompt replacement and terminal interruption do not by themselves close a parent-governed S3/S4/S5 function.

## Recursion

No recursive viable unit is demonstrated. Tools, transport threads and model alternatives are not separately viable child systems.

## Variety and escalation

Tool results/errors amplify the coder's observations; context summaries attenuate history and can discard distinctions. Overflow recovery is bounded, and interruption/error return reaches the user, but it is not a separately established algedonic or governance channel.

## Evidence gaps

Static source assessment only. Rust cargo was unavailable in the inspection environment, so native Rust tests and compilation were not run; no live provider-backed agent task, hidden configuration, benchmark or independent semantic review is claimed. Absence findings concern the frozen first-party distribution, not all possible user-installed skills/integrations.

## Index execution provenance

New serial batch #2177, frozen intake #2176, row 1. Source assessment by the executing Index S1 actor; transport/CI are supporting machinery. Proposed publication and canonical admission remain separate transactions.
