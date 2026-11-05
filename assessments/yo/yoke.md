---
harness_id: yoke
project_name: Yoke
repository: https://github.com/sinabs/spring-agent-scope
review_ref: 9af73c2683773c5b4c08eca0ef79044f3aef2f3c
reviewed_at: 2026-11-05
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

# Yoke

## Review boundary

- System in focus: Yoke HTTP conversational/weather agent service, not AgentScope Java as a whole.
- Purpose and identity: Serve multi-turn tool-using answers through POST chat and streaming AG-UI.
- Relevant environment: Users, weather/geocoding service, model endpoints and host process.
- Standard-distribution boundary: Spring Boot application and explicitly instantiated AgentScope ReAct composition.
- Credited operating / distribution surfaces: src/main controller, agent builder, codecs, WeatherTool, runtime state-store and application profiles.
- Adjacent first-party surfaces excluded from ownership: src/test fake-model/HTTP checks, Gradle/CI, brand assets and contributor development.
- First-party operating / deployment modes considered: Local/prod HTTP chat and AG-UI streaming; no separate supervised metasystem mode found.
- Recursion level: One service with conversational operational sessions.
- Reviewed revision: `9af73c2683773c5b4c08eca0ef79044f3aef2f3c`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Spring Boot constructs a fresh ReActAgent for each request from a shared configured builder. A shared in-memory AgentStateStore preserves and isolates session histories. The registered WeatherTool geocodes a city and returns validated current observations or bounded error text. Controllers own resource closure and SSE error events; codecs restrict client input to the latest user text. No worker hierarchy, autonomous scheduler, policy deliberator or audit/adaptation service is wired. [`README.md`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/README.md); [`src/main/java/com/yoke/config/AgentConfiguration.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/config/AgentConfiguration.java); [`src/main/java/com/yoke/controller/ChatController.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/controller/ChatController.java); [`src/main/java/com/yoke/codec/AguiStreamCodec.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/codec/AguiStreamCodec.java); [`src/main/java/com/yoke/tool/WeatherTool.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/tool/WeatherTool.java); [`src/main/resources/application.yml`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/resources/application.yml); [`src/test/java/com/yoke/controller/ChatHistoryTests.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/test/java/com/yoke/controller/ChatHistoryTests.java)

## Operational model

The conversational model/tool composition is the operational S1. HTTP, storage and weather parsing support its decisions; parallel requests and environment profiles do not create a metasystem.

## S1 — Operations

- State: A
- Function: Answer user requests through a concrete ReAct service with a registered live-weather action.
- Disturbance / variety regulated: Different user questions, city inputs, missing/invalid weather responses and conversation histories.
- Decisive decision or feedback right: Choose whether and with which city to call get_weather, incorporate its observation and formulate the next response.
- Decision owner: The configured model-driven ReAct agent instantiated by the first-party HTTP service.
- Supporting / enforcement mechanisms: AgentScope executes the loop; Yoke wires model, maxIters, WeatherTool, per-session state and HTTP/SSE lifecycle. Tool validation/timeouts constrain execution.
- Closure path: chat/stream builds the configured agent, calls it with server-owned history and returns the generated result; the weather observation is available to the agent and history is reused on later requests.
- Boundary reachability: AgentConfiguration registers WeatherTool in every built agent; both supported endpoints instantiate this builder. This credits the concrete local composition, not uninstantiated AgentScope features.
- Why this is / is not agent-owned: Removing the model-driven decision leaves HTTP transport and deterministic weather lookup but no discretionary question-to-action/answer selection.
- Evidence: [`README.md`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/README.md); [`src/main/java/com/yoke/config/AgentConfiguration.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/config/AgentConfiguration.java); [`src/main/java/com/yoke/controller/ChatController.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/controller/ChatController.java); [`src/main/java/com/yoke/codec/AguiStreamCodec.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/codec/AguiStreamCodec.java); [`src/main/java/com/yoke/tool/WeatherTool.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/tool/WeatherTool.java); [`src/main/resources/application.yml`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/resources/application.yml); [`src/test/java/com/yoke/controller/ChatHistoryTests.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/test/java/com/yoke/controller/ChatHistoryTests.java)
- Basis: structural
- Confidence: high
- Caveats: Model quality and production deployment not tested; in-memory state is lost on restart.

## S2 — Coordination

- State: —
- Function: A per-request conversational S1 is shipped; separate sessions have no coordinated operational commitments. No distinct inter-S1 attenuation function is supplied.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Session-ID isolation, shared stateless WeatherTool, concurrent request handling and README warning that same-session requests are not serialized.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`README.md`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/README.md); [`src/main/java/com/yoke/config/AgentConfiguration.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/config/AgentConfiguration.java); [`src/main/java/com/yoke/controller/ChatController.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/controller/ChatController.java); [`src/main/java/com/yoke/codec/AguiStreamCodec.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/codec/AguiStreamCodec.java); [`src/main/java/com/yoke/tool/WeatherTool.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/tool/WeatherTool.java); [`src/main/resources/application.yml`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/resources/application.yml); [`src/test/java/com/yoke/controller/ChatHistoryTests.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/test/java/com/yoke/controller/ChatHistoryTests.java)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete src/main Java/resource tree, README/README_CN, Gradle dependency wiring, controller/config/codec/tool/session tests and repository CI.
- Plausible first-party paths checked: Session-ID isolation, shared stateless WeatherTool, concurrent request handling and README warning that same-session requests are not serialized.
- Why no material first-party path remains: A per-request conversational S1 is shipped; separate sessions have no coordinated operational commitments. No distinct inter-S1 attenuation function is supplied.

## S3 — Inside-and-now control

- State: —
- Function: No whole-service current-control actor with shared commitment/resource discretion is wired; max iterations, configuration and lifecycle cleanup bound individual S1 calls.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Builder maxIters/model configuration, profile startup validation, request cleanup and virtual-thread settings; no operator current-view/returned intervention loop.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`README.md`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/README.md); [`src/main/java/com/yoke/config/AgentConfiguration.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/config/AgentConfiguration.java); [`src/main/java/com/yoke/controller/ChatController.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/controller/ChatController.java); [`src/main/java/com/yoke/codec/AguiStreamCodec.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/codec/AguiStreamCodec.java); [`src/main/java/com/yoke/tool/WeatherTool.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/tool/WeatherTool.java); [`src/main/resources/application.yml`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/resources/application.yml); [`src/test/java/com/yoke/controller/ChatHistoryTests.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/test/java/com/yoke/controller/ChatHistoryTests.java)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete src/main Java/resource tree, README/README_CN, Gradle dependency wiring, controller/config/codec/tool/session tests and repository CI.
- Plausible first-party paths checked: Builder maxIters/model configuration, profile startup validation, request cleanup and virtual-thread settings; no operator current-view/returned intervention loop.
- Why no material first-party path remains: No whole-service current-control actor with shared commitment/resource discretion is wired; max iterations, configuration and lifecycle cleanup bound individual S1 calls.

## S3* — Complementary audit

- State: —
- Function: Tool response validation and repository tests are ordinary production/development checks; no complementary independent audit judgment returns corrective control into the service.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Weather numeric/body-limit checks, model error mapping, history tests and CI; test fake models are adjacent development witnesses.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`README.md`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/README.md); [`src/main/java/com/yoke/config/AgentConfiguration.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/config/AgentConfiguration.java); [`src/main/java/com/yoke/controller/ChatController.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/controller/ChatController.java); [`src/main/java/com/yoke/codec/AguiStreamCodec.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/codec/AguiStreamCodec.java); [`src/main/java/com/yoke/tool/WeatherTool.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/tool/WeatherTool.java); [`src/main/resources/application.yml`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/resources/application.yml); [`src/test/java/com/yoke/controller/ChatHistoryTests.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/test/java/com/yoke/controller/ChatHistoryTests.java)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete src/main Java/resource tree, README/README_CN, Gradle dependency wiring, controller/config/codec/tool/session tests and repository CI.
- Plausible first-party paths checked: Weather numeric/body-limit checks, model error mapping, history tests and CI; test fake models are adjacent development witnesses.
- Why no material first-party path remains: Tool response validation and repository tests are ordinary production/development checks; no complementary independent audit judgment returns corrective control into the service.

## S4 — Outside-and-then intelligence

- State: —
- Function: Current-weather sensing answers the present user request; it does not generate prospective options that change the service capability. No adaptation or parent adaptation loop is wired.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Current-only weather tool, conversation history, provider settings and Learn More references; changing dependencies manually is contributor work.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`README.md`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/README.md); [`src/main/java/com/yoke/config/AgentConfiguration.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/config/AgentConfiguration.java); [`src/main/java/com/yoke/controller/ChatController.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/controller/ChatController.java); [`src/main/java/com/yoke/codec/AguiStreamCodec.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/codec/AguiStreamCodec.java); [`src/main/java/com/yoke/tool/WeatherTool.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/tool/WeatherTool.java); [`src/main/resources/application.yml`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/resources/application.yml); [`src/test/java/com/yoke/controller/ChatHistoryTests.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/test/java/com/yoke/controller/ChatHistoryTests.java)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete src/main Java/resource tree, README/README_CN, Gradle dependency wiring, controller/config/codec/tool/session tests and repository CI.
- Plausible first-party paths checked: Current-only weather tool, conversation history, provider settings and Learn More references; changing dependencies manually is contributor work.
- Why no material first-party path remains: Current-weather sensing answers the present user request; it does not generate prospective options that change the service capability. No adaptation or parent adaptation loop is wired.

## S5 — Policy and identity

- State: —
- Function: Static system prompt, registered-tool restriction and production key validation do not provide identity/ultimate-policy issue routing, legitimate returned decision and governed subsequent operation.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: application profile/system prompt, AG-UI input filtering, tool registration and CONTRIBUTING/CI; no runtime policy-proposal/decision-return mode.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`README.md`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/README.md); [`src/main/java/com/yoke/config/AgentConfiguration.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/config/AgentConfiguration.java); [`src/main/java/com/yoke/controller/ChatController.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/controller/ChatController.java); [`src/main/java/com/yoke/codec/AguiStreamCodec.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/codec/AguiStreamCodec.java); [`src/main/java/com/yoke/tool/WeatherTool.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/java/com/yoke/tool/WeatherTool.java); [`src/main/resources/application.yml`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/main/resources/application.yml); [`src/test/java/com/yoke/controller/ChatHistoryTests.java`](https://github.com/sinabs/spring-agent-scope/blob/9af73c2683773c5b4c08eca0ef79044f3aef2f3c/src/test/java/com/yoke/controller/ChatHistoryTests.java)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete src/main Java/resource tree, README/README_CN, Gradle dependency wiring, controller/config/codec/tool/session tests and repository CI.
- Plausible first-party paths checked: application profile/system prompt, AG-UI input filtering, tool registration and CONTRIBUTING/CI; no runtime policy-proposal/decision-return mode.
- Why no material first-party path remains: Static system prompt, registered-tool restriction and production key validation do not provide identity/ultimate-policy issue routing, legitimate returned decision and governed subsequent operation.

## Recursion

Per-request agents and independent histories do not demonstrate recursively viable organizations.

## Variety and escalation

Model choice amplifies action variety; fixed tool registration, server-owned history, iteration caps and timeout/input validation attenuate it. HTTP errors are operational failure channels, without evidence of an exceptional organizational authority path.

## Evidence gaps

Source-based assessment; no live model/weather requests or JDK25 execution was used. This limits empirical quality claims, not the reconstructed shipped wiring.
