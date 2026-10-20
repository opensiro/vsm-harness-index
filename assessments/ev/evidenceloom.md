---
harness_id: evidenceloom
project_name: Evidence Loom
repository: https://github.com/simonguo/evidenceloom
review_ref: de30bd4262fe0198dcc349e318fb0c1f1f9fc410
reviewed_at: 2026-10-20
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

# Evidence Loom

## Review boundary

- System in focus: Public local-first market research desktop `simonguo/evidenceloom`, including **embedded first-party TradingAgents-compatible** LangGraph LLM analyst, researcher/debate, trader, risk and manager core, Python analysis sidecar, Rust Tauri desktop process supervision, frozen evidence snapshots, numeric/research-readiness validation and cross-run research memory.
- Purpose and identity: Help a human perform repeatable, bounded instrument market research cases and preserve provenance/quality signals for generated reports. Published README explicitly disclaims execution authority and financial/trading advice; this is not a deployed independent portfolio investment business.
- Relevant environment: Desktop user's selected instrument, analysis date, provider secrets, external market/news data endpoints, configured model clients, optional local SQLite/checkpoint stores and saved research versions. No broker trade execution or empirical profitability is assumed.
- Standard-distribution boundary: `tradingagents/graph/trading_graph.py`, `setup.py`, first-party analysts/managers, `frontend/server/run_analysis.py`, `src-tauri/src/analysis_execution.rs`, model clients, readiness and evidence/numeric/frozen-report validators and history/memory. The published `tradingagents/` subtree is **actually included** in this repository, not borrowed from a separately installed upstream package.
- Credited operating / distribution surfaces: [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py); [`tradingagents/graph/setup.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/setup.py); [`tradingagents/agents/analysts/market_analyst.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/analysts/market_analyst.py); [`tradingagents/agents/analysts/news_analyst.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/analysts/news_analyst.py); [`tradingagents/agents/researchers/bull_researcher.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/researchers/bull_researcher.py); [`tradingagents/agents/researchers/bear_researcher.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/researchers/bear_researcher.py); [`tradingagents/agents/managers/research_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/research_manager.py); [`tradingagents/agents/managers/portfolio_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/portfolio_manager.py); [`tradingagents/agents/risk_mgmt/conservative_debator.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/risk_mgmt/conservative_debator.py); [`tradingagents/agents/trader/trader.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/trader/trader.py); [`frontend/server/run_analysis.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/frontend/server/run_analysis.py); [`src-tauri/src/analysis_execution.rs`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/src-tauri/src/analysis_execution.rs); [`tradingagents/evidence/ledger.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/evidence/ledger.py); [`tradingagents/research/readiness.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/readiness.py); [`tradingagents/research/numeric_review.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/numeric_review.py); [`tradingagents/graph/research_memory.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/research_memory.py); [`tradingagents/graph/reflection.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/reflection.py).
- Adjacent first-party surfaces excluded from ownership: Screenshots, desktop acceptance fixtures, external stock/LLM data provider internals and accuracy, tests and synthetic gateway receipts, proposed professional quality standards, user decisions to buy/sell, report viewers and operator-owned desktop secrets. Their existence may establish architecture/validation but does not itself confer separate VSM management authority.
- First-party operating / deployment modes considered: Desktop Tauri host and Python packaged sidecar; default selected market/social/news/fundamental analysts, debate/risk agents, supported provider adapters, model-generated plan and output, conditional financial evidence readiness and decision withholding, saved evidence bundle/numeric review and report histories, outcome settlement/reflection memory with future task injection. No live provider calls or production trading run was executed here.
- Recursion level: One bounded instrument research task and its constituent model task roles. A sequence of research tasks can be retained, but analyst nodes are not assumed to be self-sustaining viable business departments. References to 'Research Manager' and 'Portfolio Manager' refer to named stages and final research recommendations, not a standing institutional S3.
- Reviewed revision: `simonguo/evidenceloom@de30bd4262fe0198dcc349e318fb0c1f1f9fc410`, immutable Git tree `699876ac1f713bd20fe0ff842ebf6976b75e439f`, GitHub stable ID `1308548569`, created `2026-07-22T08:01:46Z`, public nonfork/nonarchived, Apache-2.0.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Python `TradingAgentsGraph` creates real configured provider clients and a `GraphSetup` LangGraph execution graph. The model analyst nodes can call market/news/fundamental tools through bounded ToolNode turns, bull/bear researchers and risk roles supply competing analyses, Research Manager synthesizes an investment plan and Portfolio Manager generates a structured final recommendation. The Python sidecar `frontend/server/run_analysis.py` runs the same embedded graph as desktop, while Rust Tauri manages process/report lifecycles. Model decisions influence the contents of reports; graph conditional and router logic control execution bounds and provenance. [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py); [`tradingagents/graph/setup.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/setup.py); [`tradingagents/agents/analysts/market_analyst.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/analysts/market_analyst.py); [`tradingagents/agents/managers/research_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/research_manager.py); [`tradingagents/agents/managers/portfolio_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/portfolio_manager.py); [`frontend/server/run_analysis.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/frontend/server/run_analysis.py); [`src-tauri/src/analysis_execution.rs`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/src-tauri/src/analysis_execution.rs).

Unlike a plain LLM wrapper, the product implements its own independent evidence systems: EvidenceBundle and ledger track actual provider/market-input attempts and hashes; ResearchReadiness explicitly blocks unsupported recommendations based on required pre-acquired inputs, and numeric-review/frozen-claim evaluation can compare report statements against saved values without trusting model prose. These are *research product quality and provenance* safeguards, but no autonomous S3 controlling independent S1 operating units is present to audit; they do not become organizational S3* simply because checks are independent from a model. [`tradingagents/evidence/ledger.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/evidence/ledger.py); [`tradingagents/research/readiness.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/readiness.py); [`tradingagents/research/numeric_review.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/numeric_review.py); [`tradingagents/evaluation/runner.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/evaluation/runner.py); [`docs/RESEARCH_READINESS.md`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/docs/RESEARCH_READINESS.md).

The `ResearchMemory` component stores model final-decision snapshots, later attempts outcome settlement and a retrospective reflection, and can provide lessons as past_context to a later instrument research run. This establishes real task-to-task memory, but not an independent organizational prospective adaptation mandate or future capability acceptance loop. [`tradingagents/graph/research_memory.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/research_memory.py); [`tradingagents/graph/reflection.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/reflection.py); [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py).

## Operational model

A user configures a bounded research input and approved data/model providers; multiple model agents independently reason about aspects of that **same task**, with a model-authored report/decision and deterministic report-readiness guard. S1 agentic decisions own task reasoning and optional tools; no first-party managers of separately viable S1 businesses, systemic independent management audit, prospective organization-level adaptation, or identity/policy charter are evidenced.

## S1 — Operations

- State: A
- Function: LLM-driven multi-role research operations: gather and interpret instrument market/news/fundamental information, select indicators and tools, argue competing research/risk cases, and produce bounded model-directed final investment-research reports.
- Disturbance / variety regulated: Changing instrument data, data gaps/staleness, alternative forecasts, conflicting analyst/risk reports, provider or tool errors, missing evidence, ambiguous directional rating and output-format failures.
- Decisive decision or feedback right: Configured model analysts may choose market data tools, relevant indicators and reasoning; bull/bear and risk debate agents generate analysis; Research Manager and Portfolio Manager synthesize cases into a model-authored research recommendation subject to deterministic readiness guards and final output validation. Results and tool observations are threaded through LangGraph task state.
- Decision owner: First-party configured LangGraph LLM analyst/research/debate/manager nodes drive substantive task analysis. The graph builder and deterministic readiness/output validators constrain execution but do not themselves choose a forecast or investment thesis; human desktop user selects instrument, dates, provider and analysts.
- Supporting / enforcement mechanisms: Concrete model providers in llm_clients, LangGraph StateGraph/ToolNode, conditional analyst tool loop, debate and risk nodes, manager structured output, run_analysis sidecar, Tauri shell, evidence/readiness gates and checkpoint state.
- Closure path: User's bounded research run → selected LLM analysts may invoke data tools → tool observations enter research state → bull/bear debate and research plan → trader/risk debate → model Portfolio Manager produces decision → first-party readiness/quality guards can withhold or label output → report saved with evidence → user reads finished research. The model can respond to new data within the current analysis.
- Why this is / is not agent-owned: The shipping `TradingAgentsGraph` and `GraphSetup` connect concrete model analysts and managers with actual tools and output downstream; `frontend/server/run_analysis.py` constructs and calls this embedded core. Not just an architectural README or uninstantiated library interface.
- Evidence: Removing the model from the embedded source leaves no mechanism to make context-specific analyst/tool selections and debate resolutions. Autonomy is within a selected research task; it does not establish actual trading execution or investment profit.
- Basis: [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py); [`tradingagents/graph/setup.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/setup.py); [`tradingagents/agents/analysts/market_analyst.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/analysts/market_analyst.py); [`tradingagents/agents/managers/research_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/research_manager.py); [`tradingagents/agents/managers/portfolio_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/portfolio_manager.py); [`tradingagents/agents/risk_mgmt/conservative_debator.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/risk_mgmt/conservative_debator.py); [`frontend/server/run_analysis.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/frontend/server/run_analysis.py); [`tradingagents/llm_clients/factory.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/llm_clients/factory.py).
- Confidence: Source-based first-party operational wiring and research outputs, not empirical model reliability/trading performance.
- Caveats: High for S1 within research-run recursion.
- Boundary reachability: The source includes the complete first-party LangGraph assembler, specific concrete analyst ToolNode/call paths, named model clients and Python CLI/desktop run_analysis entry. Given configured provider credentials and data endpoints, these are normally invoked directly to select research tools, debate and construct the output; the autonomous role is not an unimplemented extension seam.


## S2 — Coordination

- State: —
- Function: No demonstrated dedicated S2 regulator of interference between separately viable, continuing S1 business operating units. The analyst/research/trader/risk roles are stages in one market research case, even when debate actively combines competing model viewpoints.
- Disturbance / variety regulated: Analyst results may conflict, debate agents disagree, selected data may be incomplete and multiple stage calls contend for tool limits.
- Decisive decision or feedback right: ConditionalLogic and LangGraph phase routing schedule analysts and debate rounds, while Research Manager adjudicates competing opinions for one report. These do not balance reciprocal business-unit disturbances or update distinct continuing unit commitments as S2's own mandate.
- Decision owner: Selected model debate agents and Research Manager for one task; graph's deterministic routers and shared state, not an independent S2 organizational coordinator.
- Supporting / enforcement mechanisms: Market/news/fundamentals analysts, bull/bear debate, bounded rounds, task state, research/risk aggregation and stage mapping.
- Closure path: Conflicting research opinions → manager authors one investment plan → trader/risk agents review → report; it closes a single artifact and not inter-S1 relational stabilization.
- Why this is / is not agent-owned: Different task names and agent opinions are not independent viable operations capable of sustaining separate customers, budgets and operational boundaries. A 'Research Manager' label is not a VSM S2 duty.
- Evidence: [`tradingagents/graph/setup.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/setup.py); [`tradingagents/agents/managers/research_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/research_manager.py); [`tradingagents/agents/researchers/bull_researcher.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/researchers/bull_researcher.py); [`tradingagents/agents/researchers/bear_researcher.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/researchers/bear_researcher.py); [`tradingagents/agents/risk_mgmt/conservative_debator.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/risk_mgmt/conservative_debator.py); [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py).
- Basis: Bounded negative after evaluating all first-party debate, routing and common-state surfaces.
- Confidence: High.
- Caveats: Could support multi-department organizational analysis if separately deployed, but no first-party mediation of those departments is shown.

### Absence scope

- Surfaces inspected: Whole analyst/debate/risk roles, shared LangGraph AgentState, conditional routers and bounded tool limits; associated reports and pipeline edges.
- Plausible first-party paths checked: Checked bull/bear/risk debate as a possible coordination-of-disturbances mechanism, and researcher manager as a possible inter-agent mediator with independent unit obligations.
- Why no material first-party path remains: First-party evidence shows debate/consensus about one instrument research artifact. The role nodes are finite task components, not independently viable operating departments. No interdepartmental S2 decision right and reciprocal return changing continuing unit commitments is present.


## S3 — Inside-and-now control

- State: —
- Function: No continuing whole-current S3 manager of several independently viable S1 departments, despite multi-role workflow supervision and a model 'Portfolio Manager' for one instrument recommendation.
- Disturbance / variety regulated: Research-stage failures, missing evidence, incorrect numerical assertions, risk disagreement, interrupted desktop sidecar, and inadequate confidence.
- Decisive decision or feedback right: Portfolio Manager chooses a model-authored final investment thesis from a *single analysis's* research/risk state, and local readiness gate may disallow a recommendation; Rust host controls process cancellation/version persistence. No agent manages organization-wide operational resource allocations, departmental commitments and resulting consequences.
- Decision owner: LLM Portfolio Manager and deterministic readiness/Rust desktop policy for one task, human research user as consumer. No supported independently authorized current executive over separately viable S1s, autonomous or parent-governed.
- Supporting / enforcement mechanisms: PortfolioDecision schema, readiness gate, graph checkpointer, analysis execution/cancellation, frozen run evidence and report store.
- Closure path: Within-run opinions → final model report with rating or withheld REVIEW → desktop persisted version; no enduring multi-unit current-resource/priority decision loop returned to separate viable operational departments.
- Why this is / is not agent-owned: Use of terms 'portfolio' and 'manager' in a trading research flow does not establish that this application runs an organization's operating departments; recommendation is a report artifact, not a manager's binding commitments over separate S1 units.
- Evidence: [`tradingagents/agents/managers/portfolio_manager.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/agents/managers/portfolio_manager.py); [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py); [`tradingagents/research/readiness.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/readiness.py); [`frontend/server/run_analysis.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/frontend/server/run_analysis.py); [`src-tauri/src/analysis_execution.rs`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/src-tauri/src/analysis_execution.rs); [`docs/RESEARCH_READINESS.md`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/docs/RESEARCH_READINESS.md).
- Basis: Explicitly reviewed strongest candidate whole-case manager and readiness/cancel paths as potential S3.
- Confidence: High.
- Caveats: The research report may guide a human portfolio manager outside the app; that institution's management authority is not first-party source evidence.

### Absence scope

- Surfaces inspected: LLM Research Manager and Portfolio Manager, final proposal, risk stage, ready/review gate, Tauri desktop run control and reports.
- Plausible first-party paths checked: Checked whole-case portfolio manager as a business decision authority, gate as an S3 risk manager, human GUI as parent S3(P), and process supervisor as whole-current executive.
- Why no material first-party path remains: Portfolio Manager is a model research-report synthesis step without legitimate authority over a standing portfolio of separately viable S1 operations. Readiness and process controls govern current report/run state, not allocation of resources and commitments across an institution.


## S3* — Complementary audit

- State: —
- Function: No independent complementary S3* audit of an S3 management description of real organizational operations and mandatory returned managerial correction.
- Disturbance / variety regulated: Research input manipulation, fabricated citations, conflicting evidence, unsupported numeric report prose, missing market rows and stale provider outputs.
- Decisive decision or feedback right: Frozen EvidenceBundle, ResearchReadiness gate, numeric checks, settlement/evaluation and provenance hashing can independently reject or label current *research claims* against saved inputs; however they inspect one study's data and model text, not organizational S3 ordinary management reports or actual multi-S1 operational reality.
- Decision owner: First-party deterministic evidence and numeric checkers, optional reflective LLM, audit consumers; no independently chartered management auditor or S3 corrective recipient.
- Supporting / enforcement mechanisms: Evidence ledger and report snapshot, frozen claim evaluator, numeric span/decimal validator, source readiness policy, report versioning and traceability metadata.
- Closure path: Acquired research inputs/model output → deterministic proof/numeric checks → error/REVIEW status/report labels. No whole-current S3 managerial claim → independent direct field evidence from viable S1 operations → binding correction returned to S3.
- Why this is / is not agent-owned: Evidence checks are substantive and separate from authors' text generation, but audit object and return path are *per-report research quality*, not organizational management truth. Work-product verification alone cannot establish S3*.
- Evidence: [`tradingagents/evidence/ledger.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/evidence/ledger.py); [`tradingagents/research/readiness.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/readiness.py); [`tradingagents/research/numeric_review.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/numeric_review.py); [`tradingagents/evaluation/runner.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/evaluation/runner.py); [`tradingagents/memory/evaluation.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/memory/evaluation.py); [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py); [`docs/RESEARCH_READINESS.md`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/docs/RESEARCH_READINESS.md).
- Basis: Strongest S3* analogue examined; detailed negative only for organizational audit scope, not a denial of genuine evidence verification.
- Confidence: High.
- Caveats: Saved evidence hashes establish provenance/integrity, not necessarily correctness or future predictive value. No general financial audit endorsement.

### Absence scope

- Surfaces inspected: Separate EvidenceBundle, citation audit, first-party numeric review, frozen selected-claim evaluator, ResearchReadiness policy, model reflection and report version artifacts.
- Plausible first-party paths checked: Checked independent numeric-source truth checks and audit/replay as actual S3 ordinary-management claim inspections, and whether findings mandate organizational managerial corrective action.
- Why no material first-party path remains: These are robust *report/data* validation systems, but the audited object is one bounded instrument research output. No distinct organizational S3 reporting owner, direct inspection of independently viable S1 field operations or S3 corrective management return is shipped.


## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party autonomous outside-and-then strategic environmental intelligence that develops and accepts changes to the continuing organization's future operating capabilities.
- Disturbance / variety regulated: Research outcomes may drift with changing market context, memories of previous studies become relevant, next analysis may need different evidence or prompts.
- Decisive decision or feedback right: ResearchMemory settles prior decisions against recorded market outcomes and Reflector produces a lesson reintroduced into future *similar instrument analyses*; source freshness and research readiness influence next current study. No actor selects a prospective organization-level adaptation portfolio, accepts new future capability/policy and closes the change into enduring operations.
- Decision owner: LLM reflecting on past task outcome and deterministic record store; user/maintainer sets future instruments, analyst configuration and capability releases, not a distinct standing S4 strategic intelligence owner.
- Supporting / enforcement mechanisms: MemoryStore, settlement eligibility, ResearchMemory.reflection and past_context injection, frozen version comparison and readiness policy.
- Closure path: Past selected research conclusion → later dated market settlement → model-produced lesson → persisted context included in future research task. This is bounded retrospective S1 performance learning, not authorized prospective organizational adaptation and return.
- Why this is / is not agent-owned: Learning from outcome is real first-party feedback but does not on its own establish a future-institutional environmental research/option/adoption decision function; there are no independently viable S1 organizations to adapt.
- Evidence: [`tradingagents/graph/research_memory.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/research_memory.py); [`tradingagents/graph/reflection.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/reflection.py); [`tradingagents/graph/trading_graph.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/graph/trading_graph.py); [`tradingagents/memory/evaluation.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/memory/evaluation.py); [`docs/PROFESSIONAL_QUALITY.md`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/docs/PROFESSIONAL_QUALITY.md).
- Basis: Bounded negative with an actual cross-run feedback path disclosed, rather than incorrectly claiming no memory.
- Confidence: Medium-high.
- Caveats: Future-outcome labels and benchmarks are retrospective and subject to available data; this assessment does not judge investment alpha.

### Absence scope

- Surfaces inspected: ResearchMemory outcome settlement, Reflector later-dated lessons, frozen report comparison, analyst prompt past_context, external market news capture and future study notes.
- Plausible first-party paths checked: Checked historical settlement/lesson reinjection as an S4 adaptive loop, changing market data as environmental scouting and design improvement from quality findings.
- Why no material first-party path remains: The closed path only improves later *similar research tasks* by including historical lessons. No autonomous institution-level prospective research option adoption or modified future operational capability charter/current-management return is shown.


## S5 — Policy and identity

- State: —
- Function: No legitimate first-party constitutional identity or ultimate mission decision function for a continuing institution or recognized parent.
- Disturbance / variety regulated: API credential theft, report falsification, dangerous process access, investor misinterpretation, data tampering and unsupported model recommendations.
- Decisive decision or feedback right: Local desktop host manages credentials/proc lifecycle; strict static report/evidence/research-readiness contracts and disclaimer constrain accepted artifacts. These rules enforce developer/user-defined product policy and traceability, rather than autonomously choosing the enterprise's identity or receiving a legitimate parent S5 decision with returned binding charter.
- Decision owner: Product developers and external human desktop owner set policies; Rust/Python checks execute them deterministically, not autonomous constitutional S5.
- Supporting / enforcement mechanisms: Tauri desktop permissions, application secrets, evidence contract, research-readiness gate, report versioning and output-quality constraints.
- Closure path: Configured policy/data limitations → validation failure or REVIEW status → user-facing report; no internal constitutional issue → legitimate S5 mandate/purpose decision → returned revised organizational identity and rights.
- Why this is / is not agent-owned: Refusing a weak recommendation or labeling report quality is good product governance but remains task/evidence acceptance, not ultimate organizational identity governance.
- Evidence: [`tradingagents/research/readiness.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/research/readiness.py); [`tradingagents/evidence/ledger.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/tradingagents/evidence/ledger.py); [`frontend/server/run_analysis.py`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/frontend/server/run_analysis.py); [`src-tauri/src/analysis_execution.rs`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/src-tauri/src/analysis_execution.rs); [`README.md`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/README.md); [`docs/RESEARCH_READINESS.md`](https://github.com/simonguo/evidenceloom/blob/de30bd4262fe0198dcc349e318fb0c1f1f9fc410/docs/RESEARCH_READINESS.md).
- Basis: Bounded negative across human desktop control, private data and first-party developer-specified rules.
- Confidence: High.
- Caveats: Human regulators, institutional investment committees and users may have external S5; no governance is borrowed from outside the repository.

### Absence scope

- Surfaces inspected: Local Tauri host/secrets, project safety disclaimer, researcher readiness gate, report-quality/provenance contracts, data usage and export rules.
- Plausible first-party paths checked: Checked human operator as parent policy decision maker, deterministic 'REVIEW' withholding as legitimate identity judgment and static research contracts as enforceable S5 policy.
- Why no material first-party path remains: No source-backed legitimate ultimate organizational identity decision owner or return mandate exists. User/developer-defined report acceptance and local privacy rules are operating-product constraints, not constitutional authority.



## Recursion

The coherent viable task recursion is *research service for one selected instrument/report*. Analyst/researcher/trader/risk roles may have distinct prompts and models, but the code composes them into one finite case. Its managers judge one report, and its validators check the report's actual data; none is a demonstrated continuing separate managerial or S3* audit institution. Longer-term organizational deployment would need distinct accountable viable units and parent relationships with source-backed decision and return loops.

## Variety and escalation

Changing market data/news, data gaps, provider errors and debater disagreements create task variety; model analysts and synthesis choose a bounded analysis (S1). A deterministic gate can withhold direction as `REVIEW` rather than misrepresent missing evidence as `Hold`. Report/audit and numeric errors return to user/system as bounded research-product statuses, not automatically algedonic S3/S5 messages. Historical settlement/reflection returns to later task context, not proven enterprise strategy.

## Evidence gaps

- Assessment based on actual first-party embedded source pinned to immutable Git SHA, not only README/demos. Source Python `compileall` for embedded `tradingagents/` and analysis sidecar PASS. No paid LLM inference, live financial recommendation run, Node desktop integration or Rust full-suite check was executed in this assessment.
- EvidenceBundle, frozen claim and readiness gates establish implementation pathways and report provenance limits; they do not guarantee factual truth, data-provider completeness or investment prediction. The project's own quality documentation explicitly bounds those claims.
- Upstream TradingAgents compatibility does not permit attributing external upstream repository code outside this included source. The source distribution is Apache-2.0, but no unneeded code redistribution was performed.
- If a human investment organization uses Evidence Loom reports for S3 or S4 decisions, the institution's role/authority and return receipts are *outside* this source-bounded general harness assessment.
