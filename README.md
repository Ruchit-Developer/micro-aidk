# Micro-AIDK (AI Development Kit)

A lightweight, bulletproof Python SDK designed to intercept AI API crashes and enforce strict JSON responses.

## Why this exists
When building autonomous AI agents in production, APIs frequently throw `503 Service Unavailable` or `429 Rate Limit` errors. Additionally, LLMs frequently hallucinate markdown formatting (e.g., ````json`) when you just need raw JSON.

**Micro-AIDK solves this with two features:**
1. **Exponential Backoff Engine:** Automatically catches server overloads and retries the request using standard backoff math (2s, 4s, 8s) to prevent application crashes.
2. **Universal Adapter Pattern:** Easily hot-swap between Gemini, OpenAI, or custom LLM providers without rewriting your application logic.

## Installation
```bash
pip install -e .
```

## Quick Start
```python
import os
from dotenv import load_dotenv
from micro_aidk.engine import BulletproofAI, GeminiProvider

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Universal Engine
provider = GeminiProvider(api_key=api_key)
ai_engine = BulletproofAI(provider=provider)

# The engine will auto-retry on 503s and force a clean Python dictionary
result = ai_engine.force_json("Generate a fake user profile with name and age.")
print(result)
```
