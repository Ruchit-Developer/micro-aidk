<div align="center">
  <h1 align="center">[ MICRO-AIDK ]</h1>
  <p align="center">
    <code>A production-grade, fault-tolerant Python SDK for autonomous AI pipelines.</code>
  </p>
  
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.12-black?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Google_Gemini-Ready-black?style=for-the-badge&logo=google&logoColor=white" />
    <img src="https://img.shields.io/badge/OpenAI-Compatible-black?style=for-the-badge&logo=openai&logoColor=white" />
  </p>
</div>

---

## // SYSTEM ARCHITECTURE
When deploying autonomous agents in production environments, developers face two critical points of failure:
1. **Upstream Rate Limiting:** APIs throwing `503 Service Unavailable` or `429 Too Many Requests`, resulting in thread termination.
2. **Data Hallucination:** LLMs returning raw markdown strings instead of valid JSON objects, breaking downstream parsers.

`micro-aidk` is a drop-in architectural wrapper that enforces absolute stability.

### Core Modules
* **Exponential Backoff Engine:** Intercepts critical server crashes (503/429) at the network layer. Automatically calculates an exponential mathematical delay (2s, 4s, 8s) and re-executes the payload without terminating the host application.
* **Universal Adapter Pattern:** Decouples the application logic from the LLM provider. Hot-swap between `GeminiProvider` or `OpenAIProvider` dynamically.
* **Strict JSON Enforcement:** Implements automatic string sanitation to strip out hallucinated markdown and forces the payload into a strictly typed Python Dictionary.

---

## // DEPLOYMENT

Install directly from source:
```bash
pip install git+https://github.com/[YOUR-USERNAME]/micro-aidk.git
```

---

## // EXECUTION PROTOCOL

```python
import os
from dotenv import load_dotenv
from micro_aidk.engine import BulletproofAI, GeminiProvider

load_dotenv()

# [1] Initialize the Universal Adapter 
provider = GeminiProvider(api_key=os.getenv("GEMINI_API_KEY"))

# [2] Boot the Fault-Tolerant Engine
ai_engine = BulletproofAI(provider=provider)

# [3] Execute payload. Engine handles all 503 errors and JSON validation silently.
prompt = "Generate a dummy user profile with name and age."
payload = ai_engine.force_json(prompt)

print(payload['name']) 
```

---
*Maintained for autonomous systems requiring 99.9% uptime.*
