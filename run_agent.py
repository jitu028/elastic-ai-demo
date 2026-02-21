import os
from dotenv import load_dotenv

# Load .env first so GEMINI_API_KEY is available
load_dotenv(override=True)

# Remove GOOGLE_API_KEY from this process so the Google GenAI SDK
# doesn't override GEMINI_API_KEY (SDK prefers GOOGLE_API_KEY when both are set)
os.environ.pop("GOOGLE_API_KEY", None)

from agent.agent import run_security_agent

if __name__ == "__main__":
    run_security_agent()
