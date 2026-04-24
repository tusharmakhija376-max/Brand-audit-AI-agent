from groq import Groq
import os
from dotenv import load_dotenv
from tools.search import run_all_searches
import time

load_dotenv(override=True)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "llama-3.3-70b-versatile"

def call_llm(system_prompt, user_message):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=2048
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling LLM: {str(e)}"

PERCEPTION_PROMPT = """
You are an expert Brand Perception Researcher.
Analyze the search results about a brand and extract key themes.
1. Identify TOP 5 recurring themes in customer reviews
2. Note significant news events affecting brand reputation
3. Summarize social media sentiment
4. Highlight reputation risks or controversies
5. Note consistent strengths
Format with these sections:
- Customer Review Themes
- News and Media Coverage
- Social Media Sentiment
- Reputation Risks
- Consistent Strengths
Be specific and objective.
"""

def perception_researcher_agent(brand_name, search_data):
    user_message = f"""
Brand being researched: {brand_name}
CUSTOMER REVIEWS DATA:
{search_data['reviews']}
NEWS AND MEDIA DATA:
{search_data['news']}
SOCIAL MEDIA DATA:
{search_data['social']}
Please provide your structured perception research report.
"""
    return call_llm(PERCEPTION_PROMPT, user_message)

SENTIMENT_PROMPT = """
You are an expert Brand Sentiment Analyst.
Given a perception research report, provide:
1. OVERALL SENTIMENT SCORE from 0 to 10
2. Scores for each category out of 10:
   - Product/Service Quality
   - Customer Service
   - Brand Trust and Credibility
   - Value for Money
   - Social Responsibility
3. PRIMARY EMOTION associated with the brand
4. Key SENTIMENT DRIVERS
5. VULNERABLE SEGMENTS
Always show scores as X/10. Be analytical.
"""

def sentiment_analyst_agent(brand_name, perception_report):
    user_message = f"""
Brand being analyzed: {brand_name}
PERCEPTION RESEARCH REPORT:
{perception_report}
Please provide your complete sentiment analysis with all scores.
"""
    return call_llm(SENTIMENT_PROMPT, user_message)

REPORT_PROMPT = """
You are a Senior Brand Strategy Consultant.
Write a complete brand audit report with this exact structure:

# BRAND AUDIT REPORT

## Executive Summary
3 to 4 sentences on the most critical finding.

## 1. Reputation Analysis
Current Reputation Score out of 10 with detailed analysis.

## 2. Messaging Consistency Analysis
Are brand claims consistent with customer experience?

## 3. Positioning Gaps
What positions is the brand missing?

## 4. Competitive Threat Assessment
Which competitor could exploit this brand weaknesses?

## 5. Strategic Recommendations
Immediate Actions 0 to 3 months and Medium Term Actions 3 to 12 months.

## 6. Key Risk Factors
What could damage this brand reputation soon?

Be specific. Every claim must be grounded in the research data provided.
"""

def audit_report_writer_agent(brand_name, perception_report, sentiment_analysis):
    user_message = f"""
Brand being audited: {brand_name}
PERCEPTION RESEARCH:
{perception_report}
SENTIMENT ANALYSIS:
{sentiment_analysis}
Please write the complete brand audit report.
"""
    return call_llm(REPORT_PROMPT, user_message)

JUDGE_PROMPT = """
You are an independent AI evaluator assessing brand audit report quality.
Score the report on these 5 criteria each out of 10:
1. OBJECTIVITY - Is it balanced and evidence-based?
2. INSIGHT DEPTH - Are there non-obvious useful insights?
3. ACTIONABILITY - Are recommendations specific and clear?
4. EVIDENCE QUALITY - Are claims backed by data?
5. STRUCTURAL CLARITY - Is it well organized?

Your response format:

## QUALITY EVALUATION REPORT

### Score Breakdown:
| Criterion | Score | Justification |
|-----------|-------|---------------|
| Objectivity | X/10 | reason |
| Insight Depth | X/10 | reason |
| Actionability | X/10 | reason |
| Evidence Quality | X/10 | reason |
| Structural Clarity | X/10 | reason |

### TOTAL QUALITY SCORE: XX/50
### Percentage: XX%
### Overall Assessment: 1 paragraph summary
### Strongest Section: which section and why
### Weakest Section: which section needs improvement
### Verdict: EXCELLENT or GOOD or ADEQUATE or NEEDS IMPROVEMENT
"""

def llm_judge_agent(brand_name, audit_report):
    user_message = f"""
Please evaluate this brand audit report for {brand_name}.
BRAND AUDIT REPORT:
{audit_report}
Provide your complete quality evaluation with all scores.
"""
    return call_llm(JUDGE_PROMPT, user_message)

def run_brand_audit_pipeline(brand_name):
    results = {}
    search_data = run_all_searches(brand_name)
    results["search_data"] = search_data
    time.sleep(3)
    perception = perception_researcher_agent(brand_name, search_data)
    results["perception"] = perception
    time.sleep(3)
    sentiment = sentiment_analyst_agent(brand_name, perception)
    results["sentiment"] = sentiment
    time.sleep(3)
    audit_report = audit_report_writer_agent(brand_name, perception, sentiment)
    results["audit_report"] = audit_report
    time.sleep(3)
    judge_evaluation = llm_judge_agent(brand_name, audit_report)
    results["judge_evaluation"] = judge_evaluation
    return results
