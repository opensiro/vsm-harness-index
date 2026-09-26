---
harness_id: webthinker
project_name: WebThinker
repository: https://github.com/RUC-NLPIR/WebThinker
review_ref: db387eb3261de9b5e2db7d2d7fb20af2aceb7882
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# WebThinker

## Review boundary

- System in focus: one first-party WebThinker deep-research run at pinned revision `db387eb3261de9b5e2db7d2d7fb20af2aceb7882`, using the shipped problem-solving or report-generation runtime, its main reasoning model, auxiliary model calls, web-search/page-exploration tools and current-run report state.
- Purpose and identity: answer a complex user question or produce a research article by autonomously deciding when and how to search, inspect web pages, synthesize information, write report sections, inspect the current report and request edits.
- Relevant environment: user question/dataset item; external web/search services and fetched pages; user-served main and auxiliary model endpoints; tokenizer/model artifacts; local caches/output files; optional evaluation/training infrastructure outside the running research episode.
- Standard-distribution boundary: `scripts/run_web_thinker.py`, `scripts/run_web_thinker_report.py`, first-party prompts and search adapters used by those entrypoints. External model servers, search engines, websites, benchmark datasets/evaluators and offline training pipelines remain environment/adjacent systems.
- Credited operating / distribution surfaces: `README.md`; `scripts/run_web_thinker.py`; `scripts/run_web_thinker_report.py`; `scripts/prompts/prompts.py`; `scripts/prompts/prompts_report.py`; search helpers called directly by the runtime.
- Adjacent first-party surfaces excluded from ownership: benchmark evaluation scripts/results, dataset packaging, released model weights and offline RL/DPO/training claims, paper/project presentation surfaces and repository development/governance.
- First-party operating / deployment modes considered: single-question and dataset problem-solving mode; single-question and dataset report-generation mode; Bing or Serper search; optional local LoRA adapter loading around a run.
- Recursion level: one deep-research episode is the system-in-focus. Main-reasoning, auxiliary reader/writer/editor and Deep Web Explorer calls are functionally inspected as parts of that operation; separate prompts/models do not become separate viable systems solely from role separation.
- Reviewed revision: `db387eb3261de9b5e2db7d2d7fb20af2aceb7882`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

WebThinker ships two principal runtime paths. `run_web_thinker.py` executes a reasoning loop in which the main model can emit a search-query marker; the harness executes the search, gathers/fetches web pages, invokes a nested Deep Web Explorer that may itself search or click links, extracts the resulting information and feeds it back into the same reasoning sequence until the model finishes or search/token limits are reached.

`run_web_thinker_report.py` extends that pattern for long-form research reports. An auxiliary model first produces a search plan. The main reasoning model then chooses among current-run operations represented by explicit markers: search, write a section, inspect the current article outline and request an edit. Search results and Deep Web Explorer findings are returned to the reasoning trace; section writing and editing are executed by auxiliary-model calls; the current article is retained in runtime state. After the main loop ends, an auxiliary final-report editor performs structural cleanup of the produced article.

The architecture therefore closes a substantive deep-research operation, but it does not establish multiple independent S1 units whose mutual disturbances require S2. The central reasoning path and auxiliary writer/reader/editor calls cooperate on one current research product. Likewise, the report `check_article` operation is not a complementary audit channel: the implementation returns the article's headings/outline to the same ordinary reasoning loop, without an independent reviewer claim, evidence path or authority. The final editor is also ordinary production/refinement of the same output.

Web access is extensive but task-local. Searches, page clicks and Deep Web Explorer calls acquire evidence needed for the current question/report. The pinned runtime does not turn those observations into a persistent prospective change in WebThinker's future installed capabilities or organizational posture. README discussion of RL/DPO training is adjacent/offline development rather than closure of the shipped inference harness.

Primary evidence:

- [`README.md`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/README.md) — project identity, shipped problem-solving/report entrypoints, autonomous search/page navigation and report write/check/edit claims.
- [`scripts/run_web_thinker.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker.py) — executable reasoning/search loop, nested Deep Web Explorer, search/click feedback, limits and result reinjection.
- [`scripts/run_web_thinker_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker_report.py) — report search-plan, search/write/check/edit loop, article state, auxiliary writing/editing and final refinement.
- [`scripts/prompts/prompts_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/prompts/prompts_report.py) — explicit semantics of report tools: search for current evidence, write a section, return the current outline, edit on instruction and structurally refine the final report.

## Operational model

The operational unit is one research episode. The main reasoning model observes the user question plus accumulated reasoning/search feedback and decides whether more information is needed or whether to continue toward an answer/report. When it selects a web action, first-party runtime code executes the search or page retrieval and returns extracted information. In report mode, the same reasoning path decides when to write, inspect or edit the current article; auxiliary model calls materialize those requested operations and return the changed article/context. This produces a closed current-task feedback loop and supports `S1=A`.

Auxiliary components increase task variety but are not separately credited as S2/S3/S3*. They do not hold independent operational missions, whole-system current-control rights or complementary audit authority. Model endpoints, search providers and top-level user task/configuration remain external constraints/resources rather than S5 owners.

## S1 — Operations

- State: A
- Function: execute a complete deep-research task by autonomously choosing and iterating reasoning, web search/page exploration, evidence synthesis and, in report mode, section writing/editing until an answer or report is produced.
- Disturbance / variety regulated: incomplete or stale knowledge, uncertain search direction, irrelevant search results, inaccessible pages, missing report sections, newly discovered evidence, current-article incompleteness and bounded token/search budgets.
- Decisive decision or feedback right: decide whether and what to search next, when to explore/click further, when enough evidence exists to continue reasoning or write, which report section/edit to request and when the current research work is complete.
- Decision owner: the model-driven WebThinker reasoning path instantiated by the first-party runtime; nested explorer and auxiliary writer/reader/editor calls execute subordinate task-local decisions/functions.
- Supporting / enforcement mechanisms: explicit search/click/write/check/edit markers, asynchronous search adapters, page fetching and caching, Deep Web Explorer loop, runtime history/article/document-memory state, BM25 document retrieval, interaction/token limits and auxiliary generation calls.
- Closure path: user question/current trace -> reasoning model selects a research action -> first-party runtime executes search/exploration or report operation -> web evidence/article change returns into the sequence -> reasoning model chooses the next action -> answer/report progresses until completion/limit.
- Boundary reachability: `scripts/run_web_thinker.py` and `scripts/run_web_thinker_report.py` are shipped documented entrypoints and directly instantiate the credited reasoning/action/feedback paths without requiring an adjacent benchmark or training controller.
- Why this is / is not agent-owned: deterministic code executes selected calls and limits, while substantive search direction, follow-up exploration, report-operation selection and task completion choices are model-generated from live research state.
- Evidence: [`README.md`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/README.md); [`scripts/run_web_thinker.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker.py); [`scripts/run_web_thinker_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker_report.py); [`scripts/prompts/prompts_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/prompts/prompts_report.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the operator supplies the top-level task, endpoints and search credentials; autonomy is assessed for the within-run operational choices, not for those parent configuration decisions.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 disturbance-attenuation function is established at the declared boundary.
- Disturbance / variety regulated: none qualifying; search planning, nested web exploration and auxiliary writing/editing coordinate steps of one research operation rather than attenuating interaction among distinct S1 units.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: shared sequence state, document memory, caches, semaphore/concurrency limits and task routing are present but are not sufficient for S2.
- Closure path: no material S2-specific closure path established.
- Why this is / is not agent-owned: there is no evidenced S2 organizational function to classify for ownership.
- Evidence: [`scripts/run_web_thinker.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker.py); [`scripts/run_web_thinker_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker_report.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: separate model roles and concurrent processing do not establish S2 without a concrete inter-operation disturbance and attenuating feedback relation.

### Absence scope

- Surfaces inspected: problem-solving loop, report loop, Deep Web Explorer, search/page reader paths, document memory/BM25, auxiliary writer/editor calls and runtime concurrency/limits.
- Plausible first-party paths checked: main-versus-auxiliary model routing; nested explorer; concurrent dataset sequences; caches and semaphore controls; report write/check/edit operations.
- Why no material first-party path remains: no distinct S1 units with a demonstrated mutual oscillation/resource/interference disturbance and no first-party mechanism whose organizational purpose is to attenuate such an inter-S1 disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no separate superior inside-and-now regulator over multiple operational units is established.
- Disturbance / variety regulated: current research progress and report completeness are regulated inside the same S1 operation.
- Decisive decision or feedback right: no current-control right distinct from the S1's own search/reason/write/edit decisions is established.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: auxiliary search plan, interaction/token limits, report article state and batch concurrency are present but do not create a superior organizational control layer.
- Closure path: no material S3-specific whole-system current-control path established.
- Why this is / is not agent-owned: the main reasoning model has broad control over one research episode, but that is operational task control rather than S3 over a set of independently operating units.
- Evidence: [`scripts/run_web_thinker.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker.py); [`scripts/run_web_thinker_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker_report.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: the auxiliary search plan and central reasoning loop are not credited from component names or sequencing alone.

### Absence scope

- Surfaces inspected: search planning, main reasoning loop, nested explorer, report state/actions, concurrency handling, search/token limits and evaluation hooks.
- Plausible first-party paths checked: search-plan generation, centralized main-model decisions, batch semaphore, max-interaction/search limits, report checking and final refinement.
- Why no material first-party path remains: no whole-system view and separate current-control authority over multiple S1 units/resources/commitments is established at the assessed recursion.

## S3* — Complementary audit

- State: —
- Function: no qualifying complementary independent audit function is established.
- Disturbance / variety regulated: report outline inspection and final structural cleanup can expose incompleteness/redundancy, but they remain ordinary in-band production/refinement of the same current report.
- Decisive decision or feedback right: no independent reviewer forms a separate audit judgement over an operational claim and returns findings through a complementary access path.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: `check_article` outline return, auxiliary editor, final report editor and optional benchmark evaluation are present but do not satisfy the S3* independence/claim requirements.
- Closure path: no material complementary-audit closure path established.
- Why this is / is not agent-owned: there is no qualifying S3* function; auxiliary-model use alone does not create organizational audit independence.
- Evidence: [`scripts/run_web_thinker_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker_report.py); [`scripts/prompts/prompts_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/prompts/prompts_report.py); `scripts/evaluate/` as an adjacent evaluation surface.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the tool name `check_article` is specifically not treated as sufficient evidence for S3*; its implementation returns the current article outline to the ordinary reasoning path rather than establishing an independent audit channel.

### Absence scope

- Surfaces inspected: report `check_article`, `edit_article`, final-report refinement, auxiliary model calls, problem-solving/report loops and benchmark evaluation directory.
- Plausible first-party paths checked: current-article outline inspection; auxiliary writer/editor; final structural editor; offline evaluation hooks.
- Why no material first-party path remains: no distinct audited claim plus complementary evidence/access path, independence boundary and returned audit findings acting on operation is established inside the shipped runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate prospective environmental-intelligence/adaptation function is established.
- Disturbance / variety regulated: web uncertainty and missing knowledge are regulated for the current research question/report, not for WebThinker's future organizational posture or installed capability set.
- Decisive decision or feedback right: none established for prospective adaptation beyond current-task search and synthesis.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: web search, page exploration, caches, document memory and README-described offline RL/DPO development do not establish runtime S4 closure.
- Closure path: no material S4-specific prospective change path established.
- Why this is / is not agent-owned: the runtime senses the external web extensively, but uses that information to complete the current task rather than to select/persist future organizational adaptation.
- Evidence: [`README.md`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/README.md); [`scripts/run_web_thinker.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker.py); [`scripts/run_web_thinker_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker_report.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: offline training/weight construction is adjacent development and is not imported into the inference harness boundary merely because the project describes progressive improvement through RL/DPO.

### Absence scope

- Surfaces inspected: web search/exploration loops, caches/document memory, LoRA loading, README training discussion, report refinement and runtime outputs.
- Plausible first-party paths checked: external-information acquisition; persistent caches; optional LoRA load/unload; released optimized models; RL/DPO roadmap/claims.
- Why no material first-party path remains: no shipped first-party inference path converts prospective environmental observations into a model-owned persistent capability/posture change for future independent runs.

## S5 — Policy and identity

- State: —
- Function: no runtime authority over organizational identity, ultimate purpose or binding top-level policy is established.
- Disturbance / variety regulated: none qualifying; the research question, model endpoints, credentials, search engine, limits and core instructions are externally supplied/configured.
- Decisive decision or feedback right: no runtime actor can redefine WebThinker's ultimate mission or authoritatively close constitutional/policy conflicts.
- Decision owner: user/operator and repository configuration outside the assessed autonomous runtime.
- Supporting / enforcement mechanisms: static prompts, command-line arguments, search/token/interaction limits and model/LoRA selection constrain operation but are not runtime S5 ownership.
- Closure path: no material S5-specific closure path established.
- Why this is / is not agent-owned: WebThinker decides how to pursue the supplied research task, not what its ultimate identity/purpose should be.
- Evidence: [`README.md`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/README.md); [`scripts/run_web_thinker.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker.py); [`scripts/run_web_thinker_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/run_web_thinker_report.py); [`scripts/prompts/prompts_report.py`](https://github.com/RUC-NLPIR/WebThinker/blob/db387eb3261de9b5e2db7d2d7fb20af2aceb7882/scripts/prompts/prompts_report.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: highly directive system/prompt instructions can constrain an agent without transferring ultimate policy authority to the agent.

### Absence scope

- Surfaces inspected: CLI configuration, prompts, problem-solving/report runtime, model/LoRA selection, limits and output/evaluation paths.
- Plausible first-party paths checked: task completion signal, search plan, static research instructions, model selection and final report refinement.
- Why no material first-party path remains: purpose and constitutional constraints are supplied externally; no runtime path authoritatively redefines or reconciles them at the identity/policy level.

## Recursion, variety and escalation

WebThinker adds substantial operational variety to one research S1 through autonomous search, nested page exploration, auxiliary reading/writing/editing and current-run document memory. Those mechanisms remain inside the research operation at this boundary. No higher VSM function is inferred from role names, web access, report checking or offline training surfaces.

## Standalone conclusion

`A — — — — —`

WebThinker autonomously closes a substantive deep-research operation. No material first-party S2, superior S3, complementary-independent S3*, prospective S4 or runtime S5 closure is established at the pinned boundary.