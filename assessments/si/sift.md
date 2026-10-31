---
harness_id: sift
project_name: SIFT
repository: https://github.com/KhanUzeb/SIFT
review_ref: c0ec1ec04a44cffc43c8d843b073b33f6a7b784d
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SIFT

## Review boundary

- System in focus: the MIT-licensed, first-party Python/FastAPI single-agent live-web research workflow, not the externally hosted LLMs, Tavily search service or third-party websites.
- Purpose and identity: answer an operator-submitted question from fresh searched/read pages, return a synthesized response with page-level citations and persist a note/trace.
- Relevant environment: unpredictable search results, stale model knowledge, inaccessible pages, rate limits, malformed tool calls, incomplete grounding and untrusted public web content.
- Standard-distribution boundary: `app/agent.py`, `llm.py`, `tools.py`, search/read/summarize/memory helpers, FastAPI `/research` route and the Streamlit client. Future roadmap features are not shipped capabilities.
- Credited operating mode: configured OpenAI-compatible model dynamically calls research tools; a deterministic heuristic mode is a degradation fallback, not evidence of model decision rights when providers fail.
- Recursion level: one research assistant/one question run; external search providers and websites are dependencies, not independently managed child business units.
- Reviewed revision: `c0ec1ec04a44cffc43c8d843b073b33f6a7b784d`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`/research` passes the question to `agent.run`. The run writes a scratchpad, asks a tool-calling LLM for one of `search`, `read`, `reformulate`, or `finish`, dispatches that act, records observations, and repeats until completion or the configured step limit. First-party code blocks premature finish while unread evidence is available, redirects duplicate reads, and falls back from native tool calling to JSON and a heuristic controller when needed. After the loop, a separate summarizer converts up to the configured number of read pages into an answer/citation list; JSON notes save history but are never read back into subsequent research decisions.

Pinned primary evidence:

- [First-party project, operating modes and explicitly missing cross-session learning](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/README.md)
- [Dynamic action loop, premature finish gate, duplicate read redirect and final answer](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/agent.py)
- [LLM action schema, provider/JSON fallback and deterministic heuristic](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/llm.py)
- [Tool dispatcher and observation feedback](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/tools.py)
- [Web-search wrapper and deduplication](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/search.py)
- [Page fetching, concurrency limit, timeout and rate-limit retry](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/reader.py)
- [Synthesis, source attribution and bounded page selection](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/summarizer.py)
- [JSON note/trace persistence and read-only note API](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/memory.py)
- [User request entry point](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/main.py)
- [Question-only system prompt, no general mission policy](https://github.com/KhanUzeb/SIFT/blob/c0ec1ec04a44cffc43c8d843b073b33f6a7b784d/app/prompts.py)

## Operational model

The user sets the research question and provider configuration. The configured model observes current steps and search/read outcomes to decide the next tool call, with fallback paths if the model is unavailable. A constructor-written loop retains an overview of the run, limits its duration, enforces a minimum evidential threshold when unread search results exist, and deterministically closes into summarization and persistence. No first-party multi-agent organization, independent management audit, future capability evolution or mission-policy authority is present in the reviewed shipped path.

## S1 — Operations

- State: A
- Function: navigate a live question-specific web-research task through evidence gathering and query changes.
- Disturbance / variety regulated: sparse or irrelevant search hits, inaccessible articles, partial observations and changing facts on the web.
- Decisive decision or feedback right: choose whether to search, what query to use, which returned URL to read, whether to reformulate and when to request finish.
- Decision owner: model behind the configured OpenAI-compatible loop client, called and bounded by first-party `llm.decide_next_action`; its internal policies are not inherited as SIFT management.
- Supporting / enforcement mechanisms: action JSON schema, `scratchpad_text`, search/read dispatcher, Tavily client, HTTP reader, retries and observations appended to `state.history`.
- Closure path: question → selected search/read/reformulate action → live result or failure observation → updated scratchpad → next model decision → finished/limited run.
- Boundary reachability: `app.main.research` calls `agent.run`, and the loop calls model `decide_next_action` on each step; configured native/structured model paths can choose among four actions.
- Why this is / is not agent-owned: ordinary model operation selects context-sensitive tool actions rather than following a fixed search-once pipeline; the backup heuristic is constructor-defined and does not change the positive assessment of the supported primary model mode.
- Evidence: pinned `agent.py`, `llm.py`, `tools.py`, `search.py` and `reader.py` above.
- Basis: source-shown operational decision path.
- Confidence: high for architecture, not for answer accuracy.
- Caveats: live provider calls and target-web retrieval were not executed for this assessment.

## S2 — Coordination

- State: —
- Function: no cross-peer operational-interference regulation within a continuing multi-unit S1 organization is shipped.
- Disturbance / variety regulated: duplicate URL reads, limited concurrent fetches and rate-limited web hosts are local I/O concerns, not competing peer-unit agendas.
- Decisive decision or feedback right: redirect repeated reads and enforce an HTTP semaphore/backoff under fixed first-party rules.
- Decision owner: constructor-written `agent._redirect_redundant_read` and `reader._semaphore`, not a separate S2 adaptive mediator.
- Supporting / enforcement mechanisms: URL deduplication, unread-result fallback, `asyncio.Semaphore` and retries.
- Closure path: one S1 research loop receives one tool observation; there is no inter-agent conflict → coordinated resolution → peer feedback path.
- Why this is / is not agent-owned: a single agent cannot acquire S2 merely by using concurrently fetched pages or provider rate limits.
- Evidence: pinned `agent.py`, `reader.py`, `search.py`, `README.md`.
- Basis: scoped negative.
- Confidence: high.
- Caveats: downstream deployments could add agents, but such systems are not in this frozen repo.

### Absence scope

- Surfaces inspected: main run loop, fetch concurrency, duplicate-read routing, Streamlit/FastAPI entry points and advertised future multi-agent ideas.
- Plausible first-party paths checked: multiple asynchronous page requests as peer operations, tool routing as S2 conflict resolution, future supervised subagents.
- Why no material first-party path remains: requests are I/O work inside a sole research agent; a multi-agent organization is explicitly a future possibility, not an implemented corrective loop.

## S3 — Inside-and-now control

- State: C
- Function: govern current per-question evidence-gathering commitments and terminate an entire bounded research episode into final delivery.
- Disturbance / variety regulated: premature model finish, repeated reads, never-ending research, malformed model calls and insufficient accessible source material.
- Decisive decision or feedback right: overrule early `finish` when fewer than two successful reads and an unread hit remains; cap steps; force completion after invalid decisions; select bounded pages for final answer and record the run status.
- Decision owner: explicit first-party `agent.run` control code and settings (`max_steps`, `max_pages_to_summarize`), not a model with unconditional release authority.
- Supporting / enforcement mechanisms: `AgentState` for whole-run view, successful-read counter, forced `READ`, `MAX_STEPS`, duplicate-read redirect, `summarizer.summarize` and note persistence.
- Closure path: state and all observations → model finish request or time/parse failure → guardrail decision to continue or close → synthesized answer, source list, steps and note ID.
- Boundary reachability: `agent.run` checks each `FINISH` against current grounding, may issue its own `READ`, and ends by calling summarizer and memory; this is on every `/research` path.
- Why this is / is not agent-owned: the episode-level control/right to permit completion is implemented by constructor-defined limits and release conditions rather than delegated to the agent.
- Whole-system current view: one research question's current step, history, search results, read pages and termination state.
- Current-control decision scope: only this research run; not portfolio-level organizational capacity, provider governance or an external user's business commitments.
- Evidence: pinned `agent.py`, `models.py`, `config.py`, `summarizer.py`.
- Basis: explicit bounded current-control closure.
- Confidence: medium; narrow single-run S3.
- Caveats: two-source minimum is conditional on an available unread result, not a guarantee of two sound sources.

## S3* — Complementary audit

- State: —
- Function: no independently governed, complementary challenge to S3's model of run quality or evidence is implemented.
- Disturbance / variety regulated: possible hallucination, unsupported assertions and false confidence; source citation and summary merging do not independently audit those risks.
- Decisive decision or feedback right: a real S3* path would separately investigate/contest the research controller's claims and return binding corrective findings; none is owned here.
- Decision owner: ordinary summarizer model and deterministic page-level citation assembler, both on the routine production path.
- Supporting / enforcement mechanisms: page summaries, merge prompt, source list, successful-read threshold and note traces.
- Closure path: read pages → summarized answer; no separate auditor investigation, challenge, S3 response and recheck.
- Why this is / is not agent-owned: model summarization and citations are outputs of the same run, not an independently commissioned audit with distinct corrective authority.
- Evidence: pinned `summarizer.py`, `prompts.py`, `agent.py`, `README.md`.
- Basis: independence test, scoped negative.
- Confidence: high.
- Caveats: page-level source attribution does not assert sentence-level verification.

### Absence scope

- Surfaces inspected: source list assembly, merge prompt, run guardrails, notes and README roadmap.
- Plausible first-party paths checked: grounding threshold as audit, separate summarization model as independent auditor, saved trace as audit evidence, prospective fact-checker subagent.
- Why no material first-party path remains: all present mechanisms directly complete the ordinary answer; an independently governed corrective verification loop is not shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective first-party capability adaptation across future research missions is present.
- Disturbance / variety regulated: changing web facts do alter current search/answer, but not the durable method, tools, policy or future operational repertoire.
- Decisive decision or feedback right: model may reformulate the current query; no agent or constructor path generates and selects new persistent future capabilities from environmental trends.
- Decision owner: current-run S1 model, fixed operator configuration, and append-only JSON note persistence.
- Supporting / enforcement mechanisms: run-local scratchpad and `memory.save_note`; note lookup is user-facing API only.
- Closure path: web observation → next action or final answer → stored note; no observed environment → future capability hypothesis → adoption → new later S1 capability loop.
- Why this is / is not agent-owned: real-time browsing and query reformulation solve the question at hand, and past notes never feed new runs.
- Evidence: pinned `agent.py`, `memory.py`, `main.py`, `README.md`.
- Basis: explicit documented no cross-session memory plus code reachability.
- Confidence: high.
- Caveats: a human may learn from saved notes outside SIFT; that external learning is not inherited.

### Absence scope

- Surfaces inspected: live research loop, note serialization and reads, settings, prompts and planned improvements.
- Plausible first-party paths checked: live information as S4 environmental scanning, query reformulation as adaptation, saved traces as learning and announced cross-session memory.
- Why no material first-party path remains: no future-facing option generation, persistent capability update or return-to-operation adoption path exists in the distributed program.

## S5 — Policy and identity

- State: —
- Function: no autonomous constitutional mission or final identity-policy right sits inside the research assistant.
- Disturbance / variety regulated: selection of legitimate research purpose, provider credentials and acceptable external information sources remains with the operator.
- Decisive decision or feedback right: the operator submits the question and configures model providers; the system prompt constrains the task to web-sourced answers but cannot redefine that mandate.
- Decision owner: outside user and constructor-level product configuration; the model chooses only task actions within the given mission.
- Supporting / enforcement mechanisms: `/research` input, settings, fixed tool schema and system prompt.
- Closure path: submitted question → configured research run → response to user; no mission legitimacy dilemma → parent or internal S5 adjudication → binding policy/identity update → system return.
- Why this is / is not agent-owned: tool selection, refusal of premature finish and a prompt about fresh sources do not confer ultimate organizational policy authority.
- Evidence: pinned `main.py`, `config.py`, `prompts.py`, `README.md`.
- Basis: bounded authority absence.
- Confidence: high.
- Caveats: outside organizational rules for how SIFT may be used are not evaluated.

### Absence scope

- Surfaces inspected: API and frontend mission intake, system prompt, provider settings, data persistence and future roadmap.
- Plausible first-party paths checked: prompt as identity policy, user query as internal S5, provider choice as governance, model self-termination as mission control.
- Why no material first-party path remains: all are constraints or actions within an externally assigned question, without a separately owned constitutional identity-decision loop.

## Recursion

The web sources, Tavily client and hosted models are suppliers/components of this research workflow. The assistant is a single bounded S1 operation; neither tool outputs nor page fetches demonstrate independent recursive viable organizations.

## Variety and escalation

Model-selected next actions amplify task-specific variety; action schema, step budget, minimum-read guard, provider/heuristic fallbacks, URL deduplication and HTTP backoff attenuate operational failure. When evidence is unavailable, deterministic summarization returns an explicit insufficiency response. Escalation to a higher autonomous manager/auditor/policy body is not shipped.

## Evidence gaps

- This is frozen source/README review; no LLM API request, Tavily query, external webpage run or user workflow was executed.
- No claim that note storage improves future-agent behavior; `save_note` is not read by `agent.run` and README explicitly says sessions are independent.
- The S3=C claim is restricted to present per-question release/termination control, not organizational management across a workforce.

## Assessment summary

Proposed `included`: model-selected live-web operations (S1=A) and constructor-controlled whole-run release/termination (S3=C). No multi-unit S2, independent S3* audit, future-capability S4 or ultimate-policy S5 is established. Vector **A · — · C · — · — · —**.
