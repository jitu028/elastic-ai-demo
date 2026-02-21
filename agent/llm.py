import time
from google import genai
import os

def safe_generate(prompt, model="gemini-2.0-flash", retries=5):
    # Initialize client here (lazily) so GEMINI_API_KEY is read after dotenv loads
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    for i in range(retries):
        try:
            return client.models.generate_content(
                model=model,
                contents=prompt
            ).text
        except Exception as e:
            if "429" in str(e):
                wait = 2 ** i
                print(f"Rate limited... retrying in {wait}s")
                time.sleep(wait)
            else:
                raise
    return "LLM failed after retries"
