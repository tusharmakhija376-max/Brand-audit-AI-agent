A multi-agent AI system that generates comprehensive brand audit reports using live web data.

## Live Demo
https://web-production-782e2.up.railway.app

## What It Does
Enter any brand name and get a complete AI-powered audit in under 60 seconds:
- Searches live web for customer reviews, news, and social mentions
- Analyzes public perception using 4 specialized AI agents
- Produces a structured brand audit report
- Independently scores the report quality using LLM-as-Judge

## Agent Pipeline

User Input (Brand Name)
          ↓
Tavily Search (Live Web Data)
          ↓
Agent 1: Perception Researcher
          ↓
Agent 2: Sentiment Analyst
          ↓
Agent 3: Audit Report Writer
          ↓
Agent 4: LLM-as-Judge (Quality Scoring)
          ↓
Final Scored Brand Audit Report

## Tech Stack
- LLM: Llama 3.3 70B via Groq LPU
- Search: Tavily Search API
- Frontend: Streamlit
- Deployment: Railway
- Language: Python 3.13

## Agents

| Agent | Role | Input | Output |
|-------|------|-------|--------|
| Perception Researcher | Extracts themes from web data | Tavily search results | Structured perception report |
| Sentiment Analyst | Scores emotional tone | Perception report | Sentiment scores 0-10 |
| Audit Report Writer | Writes professional audit | Perception + Sentiment | Full structured report |
| LLM-as-Judge | Evaluates report quality | Audit report | Quality scores out of 50 |

## LLM-as-Judge Rubric
- Objectivity: 0-10
- Insight Depth: 0-10
- Actionability: 0-10
- Evidence Quality: 0-10
- Structural Clarity: 0-10
- Total: 50 points


## Project layout

.
├── app.py                 # Streamlit UI
├── config.py              # Env loading, API key helpers, model defaults
├── gemini_agents.py       # Multi-step campaign pipeline
├── tools                  # Function-calling tools (catalog, Tavily search)
├── architecture.png       # Architecture Diagram
├── problem_statement.txt  # Generated images + Markdown (gitignored except .gitkeep)
├── requirements.txt
├── .env.example.pages     # Template only — copy to `.env` locally
└── README.md

## Project Context
Semester IV B.Tech. Electronics and Communication
Agentic AI Systems Project
