import os
from dotenv import load_dotenv
from micro_aidk.engine import BulletproofAI, GeminiProvider

# 1. Load API keys
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    print("Please add your API key to the .env file")
    exit(1)

# 2. Initialize the Universal Engine
gemini = GeminiProvider(api_key=api_key)
ai_engine = BulletproofAI(provider=gemini)

# 3. Test Exponential Backoff and JSON validation
prompt = "Generate a dummy user profile with name, age, and role. Return as JSON."
result = ai_engine.force_json(prompt)

print(result)
