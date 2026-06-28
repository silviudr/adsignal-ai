# AdSignal — Claude Build Plan

## Purpose

Build **AdSignal**, an AI-powered media buyer command center for the It's Today Media build contest.

The product should be a Render-hosted web app that helps a media buying team turn campaign performance exports and creative metadata into clear decisions:

- What to pause
- What to scale
- What is wasting spend
- What creatives are fatiguing
- Which creative angles are working
- Which landing pages may be mismatched
- What tests to run next

The demo should work with a one-click synthetic dataset, while also supporting CSV uploads.

---

## Contest Context

It's Today Media is running a build contest for a **Marketing Development Engineer**.

They want a tool that solves a real problem for their media buying team. They advertise across platforms such as:

- Meta
- Google
- Taboola
- TikTok

They report on campaign data, optimize media spend, build landing pages, generate leads, and need AI-first internal tools that help the business make more money.

Deadline: **July 4, 2026 at 11:59 PM ET**.

Submission requires:

1. Working demo, preferably live URL
2. GitHub repo
3. README answering:
   - What does this tool do?
   - Why did you build this one?
   - What would you build next if this were your full-time job?

---

## Product Name

Preferred name:

# AdSignal

Subtitle:

> AI-powered campaign triage and creative performance intelligence for media buyers.

Alternative positioning:

> Upload campaign data. Find what is wasting money. Learn which creative angles work. Get tomorrow's test plan.

---

## Core Product Idea

AdSignal ingests campaign performance data and creative metadata, calculates media buying metrics, detects useful patterns, and uses an LLM to generate a clear action plan.

It combines three ideas:

1. **Campaign triage**
   - Detect wasted spend, pause candidates, scale candidates, high CTR / low CVR mismatch, CPA spikes, ROAS decay, and possible creative fatigue.

2. **Creative-to-results analysis**
   - Connect creative attributes such as hook style, CTA, offer angle, emotional angle, funnel stage, and audience intent to performance outcomes.

3. **AI media buyer copilot**
   - Let the user ask natural-language questions about the dataset, such as:
     - What should I pause today?
     - Which creative angle works best on Meta?
     - Which ads have high CTR but poor conversion?
     - Why did ROAS drop?
     - What should we test next?

---

## MVP Scope

### Must Have

- Flask web app
- Render-compatible deployment
- Gunicorn production server
- One-click demo dataset loader
- CSV upload support
- Pandas-based metric calculations
- Campaign/ad/adset triage
- Creative metadata ingestion
- LLM-generated executive summary
- LLM-generated action plan
- LLM-generated creative test recommendations
- Simple ask-the-data question box
- Clean README
- Synthetic CSV generator script

### Nice to Have

- Chart.js charts
- Markdown report export
- Landing-page alignment critique
- SQLite persistence for uploaded analyses
- Provider switch between OpenRouter and Baseten

### Do Not Build for MVP

- Authentication
- Real Meta/Google/TikTok/Taboola API integrations
- Background jobs
- Complex RAG/vector database
- Real image/video analysis
- Multi-user workspaces
- React frontend
- Overcomplicated styling

---

## Recommended Stack

| Layer | Choice |
|---|---|
| Web framework | Flask |
| Hosting | Render.com |
| Server | Gunicorn |
| Data processing | Pandas, NumPy |
| LLM backend | OpenRouter first |
| Optional LLM backend | Baseten-compatible OpenAI-style endpoint |
| Frontend | Server-rendered Jinja templates |
| Styling | Bootstrap or minimal CSS |
| Charts | Chart.js |
| Storage | SQLite optional, file/session-based acceptable for MVP |
| Config | Environment variables |

---

## Environment Variables

Use these environment variables:

```text
SECRET_KEY=change-me
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=...
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet
OPENROUTER_SITE_URL=https://your-render-url.onrender.com
OPENROUTER_APP_NAME=AdSignal
BASETEN_API_KEY=...
BASETEN_MODEL_URL=...
```

For the MVP, only OpenRouter needs to work. Baseten can be added as an optional provider interface.

---

## Proposed Repo Structure

```text
adsignal/
  app.py
  requirements.txt
  Procfile
  runtime.txt
  README.md
  .env.example
  .gitignore

  data/
    sample_campaign_daily_performance.csv
    sample_creative_metadata.csv
    sample_landing_pages.csv

  scripts/
    generate_mock_data.py

  adsignal/
    __init__.py
    config.py

    llm/
      __init__.py
      base.py
      openrouter.py
      baseten.py

    services/
      __init__.py
      ingest.py
      metrics.py
      triage.py
      creative_intelligence.py
      landing_page_analysis.py
      report.py
      qa.py

    templates/
      base.html
      index.html
      dashboard.html
      report.html

    static/
      css/
        app.css
      js/
        dashboard.js
```

For speed, it is acceptable to keep a flatter structure initially, but avoid one giant file if possible.

---

## Required CSV Files

Generate three synthetic CSV files.

### 1. `sample_campaign_daily_performance.csv`

Each row represents daily performance for a creative/ad combination.

Columns:

```text
date
platform
campaign_id
campaign_name
adset_id
adset_name
ad_id
creative_id
offer_id
landing_page_id
traffic_type
audience_segment
spend
impressions
clicks
conversions
revenue
frequency
```

Derived metrics calculated by app:

```text
ctr = clicks / impressions
cpc = spend / clicks
cvr = conversions / clicks
cpa = spend / conversions
roas = revenue / spend
profit = revenue - spend
```

### 2. `sample_creative_metadata.csv`

Columns:

```text
creative_id
platform
headline
primary_text
cta
image_description
creative_format
hook_style
offer_angle
emotion
funnel_stage
```

Example hook styles:

```text
curiosity
problem_solution
authority
first_person_proof
direct_benefit
urgency
social_proof
```

Example offer angles:

```text
cost_savings
pain_relief
financial_improvement
home_protection
career_growth
convenience
risk_reduction
```

### 3. `sample_landing_pages.csv`

Columns:

```text
landing_page_id
offer_id
url
page_type
hero_headline
hero_subheadline
primary_cta
trust_elements
length
main_promise
```

Example page types:

```text
advertorial
lead_form
quiz
calculator
comparison_page
short_form_sales_page
```

---

## Synthetic Data Requirements

The mock data must look realistic and contain intentionally planted patterns.

Recommended scale:

- 30 days
- 4 platforms: Meta, Google, TikTok, Taboola
- 5 offers
- 40 to 60 creatives
- 800 to 1,500 daily performance rows

### Offers to Include

Use affiliate/performance-style verticals. Avoid medical claims that sound too specific or regulated.

Suggested offers:

1. Solar/home energy rebate lead gen
2. Joint comfort routine/supplement-style lead gen
3. Budgeting or savings app
4. Home warranty/home protection lead gen
5. Online education/career training lead gen

### Platforms

```text
Meta
Google
TikTok
Taboola
```

### Traffic Types

```text
cold
warm
retargeting
lookalike
search_intent
native_discovery
```

### Audience Segments

Examples:

```text
homeowners_45_plus
active_adults_50_plus
budget_conscious_parents
young_professionals
career_switchers
new_homeowners
retirees_planning
```

---

## Patterns to Encode in Mock Data

The dataset should not be random. It should tell realistic media-buying stories that the product can discover.

### Pattern 1: High CTR / Low CVR Mismatch

Scenario:

- Taboola curiosity ads get high CTR and low CPC.
- But conversion rate is poor.
- CPA is high and ROAS is weak.

Expected recommendation:

> These creatives attract curiosity clicks but do not convert efficiently. Review message match and landing-page promise before scaling.

### Pattern 2: Underfunded Winner

Scenario:

- A Meta problem/solution creative has moderate spend.
- Strong CVR.
- Low CPA.
- High ROAS.
- Stable CTR.

Expected recommendation:

> This is a scale candidate. Increase budget cautiously and monitor CPA/ROAS for degradation.

### Pattern 3: Creative Fatigue

Scenario:

- A creative starts strong in the first 7-10 days.
- CTR declines over time.
- CPC rises.
- CPA rises.
- Frequency rises.

Expected recommendation:

> Likely creative fatigue. Refresh the hook, rotate new variations, or shift spend to newer creatives.

### Pattern 4: Platform-Specific Creative Angles

Scenario:

- Authority hooks perform better on Taboola.
- First-person proof works better on TikTok.
- Direct benefit and problem/solution hooks work better on Meta.
- Google search intent performs well when the landing page promise is direct.

Expected recommendation:

> Adapt creative strategy by platform instead of reusing the same hook everywhere.

### Pattern 5: Landing Page Mismatch

Scenario:

- Ad promises a quick eligibility check.
- Landing page asks for a heavy consultation.
- CTR is good but CVR is bad.

Expected recommendation:

> The ad creates quick-check intent, but the landing page asks for too much commitment. Test a lighter lead form or quiz-style page.

---

## Core Metric Calculations

Implement `services/metrics.py`.

For each row and grouped aggregate, calculate:

```python
ctr = clicks / impressions if impressions else 0
cpc = spend / clicks if clicks else None
cvr = conversions / clicks if clicks else 0
cpa = spend / conversions if conversions else None
roas = revenue / spend if spend else 0
profit = revenue - spend
```

Aggregate by:

- campaign
- adset
- ad
- creative
- platform
- offer
- landing page
- hook style
- offer angle
- funnel stage

---

## Triage Rules

Implement deterministic rules first. Do not rely only on the LLM.

### Pause Candidate

A campaign/ad/creative is a pause candidate if:

- Spend is meaningful, and
- CPA is much worse than account average, or
- ROAS is below threshold, or
- It has spend and clicks but zero/near-zero conversions.

Example rule:

```text
spend > median spend AND roas < 0.8 AND cpa > 1.5x account average CPA
```

### Scale Candidate

A campaign/ad/creative is a scale candidate if:

```text
roas > 1.5x account average ROAS
AND conversions >= minimum meaningful volume
AND CPA < account average CPA
```

### Watch Candidate

Good early signal but not enough data:

```text
CTR high
CVR decent
spend/conversions still low
```

### Creative Refresh Candidate

Possible fatigue if:

```text
CTR decline over recent period
CPC increase
CPA increase
frequency increase
```

### Landing Page Mismatch Candidate

```text
CTR above average
CVR below average
CPA high
```

---

## LLM Responsibilities

Use the LLM for explanation, synthesis, and recommendations, not for raw metric calculation.

### Good LLM Tasks

- Explain why a campaign is a pause/scale/watch candidate
- Summarize performance patterns
- Generate next test ideas
- Generate creative variants
- Explain landing-page mismatch
- Answer natural-language questions about summarized data

### Bad LLM Tasks

- Calculating metrics from raw rows
- Making unsupported claims
- Inventing platform data
- Replacing deterministic triage logic

---

## LLM Provider Interface

Create a clean abstraction.

```python
class LLMClient:
    def chat(self, messages, model=None, temperature=0.2):
        raise NotImplementedError
```

OpenRouter implementation should call the OpenAI-compatible chat completions endpoint.

Pseudo-interface:

```python
client = get_llm_client()
response = client.chat([
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
])
```

The rest of the app should not know whether the provider is OpenRouter or Baseten.

---

## Main Report Prompt

The report prompt should receive a compact JSON summary, not raw CSV.

Include:

- Account-level totals
- Top/worst campaigns
- Top/worst creatives
- Hook-style performance summary
- Platform performance summary
- Fatigue candidates
- Mismatch candidates
- Triage table

Prompt instruction:

```text
You are an AI media buying analyst. You help a performance marketing team decide what to pause, scale, refresh, investigate, and test next.

Use only the data provided. Do not invent metrics. Be specific. Prefer actionable recommendations over generic advice.

Return:
1. Executive summary
2. Biggest risks
3. Scale candidates
4. Pause candidates
5. Creative fatigue signals
6. Landing-page/message-match issues
7. Next 5 tests to run
8. Tomorrow morning action plan
```

---

## Ask-the-Data Prompt

For Q&A, pass compact context and the user's question.

System instruction:

```text
You are AdSignal, an AI copilot for media buyers. Answer questions using only the uploaded campaign and creative analysis context. If the data is insufficient, say what is missing. Give practical media buying recommendations.
```

Example questions to support:

- What should I pause today?
- What should I scale?
- Which creative angle works best on Meta?
- Which ads have high CTR but bad conversion?
- Which campaigns look fatigued?
- What should my media buyer do tomorrow morning?
- What creative tests should we run next?

---

## UI Pages

### Home Page

Content:

```text
AdSignal
AI-powered campaign triage and creative performance intelligence for media buyers.

Upload campaign data or use the built-in demo dataset to find what is wasting spend, what is ready to scale, what creatives are fatiguing, and what tests to run next.
```

Buttons:

- Load Demo Dataset
- Upload CSV Files

Upload fields:

- Campaign performance CSV
- Creative metadata CSV
- Landing pages CSV optional

### Dashboard Page

Sections:

1. KPI cards
   - Spend
   - Revenue
   - ROAS
   - CPA
   - Conversions
   - Profit

2. Action board
   - Pause
   - Scale
   - Watch
   - Refresh creative
   - Landing-page review

3. Charts
   - Spend vs revenue by platform
   - ROAS by hook style
   - CPA by platform
   - CTR/CVR mismatch table

4. Creative intelligence
   - Best hook styles
   - Worst hook styles
   - Best CTAs
   - Platform-specific patterns

5. AI report
   - Markdown-rendered report from LLM

6. Ask AdSignal
   - Question form
   - Answer panel

---

## Render Deployment Files

### `requirements.txt`

Minimum:

```text
Flask
pandas
numpy
requests
python-dotenv
gunicorn
markdown
pydantic
```

Optional:

```text
scikit-learn
```

Avoid heavy packages unless truly needed.

### `Procfile`

```text
web: gunicorn app:app
```

### `runtime.txt`

Example:

```text
python-3.11.9
```

### Render Start Command

If not using Procfile:

```text
gunicorn app:app
```

---

## README Structure

The README is part of judging. Make it strong.

Suggested sections:

1. Project name and tagline
2. Live demo URL
3. Screenshots or demo GIF if available
4. What does this tool do?
5. Why I built this one
6. How it works
7. Data model
8. AI architecture
9. Local setup
10. Render deployment
11. What I would build next as full-time engineer
12. Notes on synthetic demo data

Important README language:

```text
AdSignal is not another ad copy generator. It is a decision layer for media buyers. It turns campaign performance and creative history into concrete actions: pause, scale, refresh, investigate, or test next.
```

Synthetic data note:

```text
The demo includes synthetic campaign data generated to resemble common paid-media export patterns. This allows the workflow to be evaluated without access to private ad accounts. The app also supports CSV uploads using the documented schema.
```

---

## What to Build Next Section

Use this in README:

```text
If this were my full-time job, I would extend AdSignal in five directions:

1. Direct connectors for Meta, Google, TikTok, and Taboola APIs.
2. Scheduled daily anomaly alerts sent to Slack/email.
3. Multimodal creative analysis for image and video ads.
4. Landing-page/ad-message match scoring using page scraping and LLM critique.
5. Persistent creative intelligence memory across offers, platforms, and campaigns so the team can ask what has historically worked and why.
```

---

## Suggested Build Order

### Phase 1 — Skeleton

- Create Flask app
- Add home page
- Add demo dataset button
- Add file upload form
- Add requirements and Procfile
- Confirm Render deployment works early

### Phase 2 — Mock Data

- Build `generate_mock_data.py`
- Generate the three CSV files
- Validate that planned patterns appear in aggregates

### Phase 3 — Metrics and Triage

- Implement CSV loading
- Calculate derived metrics
- Aggregate performance
- Implement deterministic triage rules
- Render action board

### Phase 4 — LLM Report

- Implement OpenRouter client
- Build compact analysis context
- Generate AI report
- Render Markdown report

### Phase 5 — Ask-the-Data

- Add question form
- Pass analysis context to LLM
- Return grounded answer

### Phase 6 — Polish

- Add charts
- Improve UI copy
- Add README
- Add screenshots
- Test Render live demo
- Test with fresh sample data

---

## Day-by-Day Hackathon Plan

### June 28

- Finalize scope
- Create repo
- Build Flask skeleton
- Build mock data generator
- Commit initial data files

### June 29

- Implement metric calculations
- Implement triage rules
- Build dashboard table output
- Validate the synthetic data produces meaningful findings

### June 30

- Add OpenRouter client
- Add AI report generation
- Add Markdown rendering
- Add strong report prompts

### July 1

- Add creative intelligence summaries
- Add ask-the-data interface
- Add landing-page mismatch detection

### July 2

- Deploy to Render
- Fix environment variables
- Add charts and polish UI
- Add sample screenshots

### July 3

- Write README
- Test complete demo flow
- Clean code
- Add .env.example
- Record Loom fallback if useful

### July 4

- Final smoke test
- Submit early
- Avoid risky late refactors

---

## Key Demo Story

The demo must make the judge feel this:

```text
I can click one button, see a realistic media buying dataset, and immediately understand where money is being wasted, which creative patterns are working, and what my team should test tomorrow.
```

The killer demo question:

```text
What should my media buyer do tomorrow morning?
```

Expected answer style:

```text
Start by pausing the Taboola curiosity creatives attached to LP_003 because they generated high CTR but weak conversion and CPA well above account average. Move a controlled portion of budget into the Meta problem/solution adset for the home energy offer, which has stable CTR, strong CVR, and ROAS above account average. Refresh CR_014 and CR_018 because CTR has declined while frequency and CPA rose over the last week. For the next test, create three direct-benefit variants that preserve the winning savings promise but reduce curiosity gap.
```

---

## Engineering Principles

- Deterministic calculations first, LLM synthesis second.
- Do not overclaim.
- Do not invent metrics.
- Make the demo one-click usable.
- Prefer useful and ugly over beautiful and fragile.
- Keep the code readable because the contest says they will read it.
- Keep architecture simple enough that another engineer could extend it.

---

## Definition of Done

The project is ready to submit when:

- The app is live on Render.
- The demo dataset loads with one click.
- The dashboard shows meaningful KPIs and action categories.
- The AI report gives specific recommendations.
- The ask-the-data box works.
- The README clearly explains what it does, why this tool, and what comes next.
- The repo has clean setup instructions.
- The code does not expose API keys.
- The app still works after a cold Render restart.

