<div align="center">
  <h1>🛡️ Micro-AIDK</h1>
  <p><strong>A production-grade Python SDK to bulletproof your AI Agents.</strong></p>
</div>

---

## ⚡ The Problem
When building autonomous AI agents in production, you will inevitably face two critical failures:
1. **API Rate Limiting (503/429):** The provider's server gets overloaded, instantly crashing your Python thread.
2. **JSON Hallucinations:** You request a clean JSON response, but the LLM returns broken markdown blocks (e.g., ````json`), breaking your downstream parsing logic.

## 🚀 The Solution
**Micro-AIDK** is a lightweight, drop-in architecture that wraps your AI calls in a protective layer. It is built for absolute production stability.

### Core Architecture
* 🔄 **Exponential Backoff Engine:** Automatically intercepts `503 Service Unavailable` and `429 Rate Limit` crashes. It calculates an exponential mathematical delay (2s, 4s, 8s) and silently retries the request without killing your application.
* 🧩 **Universal Adapter Pattern:** Future-proof your codebase. Switch between Gemini, OpenAI, or any custom LLM with a single line of code. No logic rewrites required.
* 🧹 **Strict JSON Enforcer:** Automatically strips away hallucinated markdown formatting and validates the output into a clean, iterable Python Dictionary.

---

## 📦 Installation
```bash
pip install micro-aidk
```

---

## 💻 Quick Start: The Universal Engine

```python
import os
from dotenv import load_dotenv
from micro_aidk.engine import BulletproofAI, GeminiProvider

load_dotenv()

# 1. Initialize the Adapter (Easily swap to OpenAIProvider later)
provider = GeminiProvider(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Boot the Engine
ai_engine = BulletproofAI(provider=provider)

# 3. Fire the request. The Engine handles 503 errors and JSON validation silently.
prompt = "Generate a dummy user profile with name and age."
result = ai_engine.force_json(prompt)

print(result['name']) 
```

---
*Built for absolute resilience in autonomous systems.*
