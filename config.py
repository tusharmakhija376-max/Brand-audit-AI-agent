import os
from dotenv import load_dotenv
load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY missing. Check your .env file.")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY missing. Check your .env file.")
