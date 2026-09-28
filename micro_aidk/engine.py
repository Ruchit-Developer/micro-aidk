import time
import json
import logging
from abc import ABC, abstractmethod
from google import genai
from google.genai.errors import APIError

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- 1. THE ADAPTER INTERFACE ---
class AIProvider(ABC):
    """Base class for all AI models. Any developer can add a new AI by extending this."""
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

# --- 2. SPECIFIC PROVIDERS ---
class GeminiProvider(AIProvider):
    def __init__(self, api_key: str, model: str = 'gemini-3.8-flash'):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text

class OpenAIProvider(AIProvider):
    """Example of how a developer adds OpenAI to our Universal Engine."""
    def __init__(self, api_key: str, model: str = 'gpt-4o-mini'):
        # import openai (developer would install this)
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> str:
        # Example implementation for OpenAI
        raise NotImplementedError("OpenAI SDK not installed. Developer must implement.")

# --- 3. THE UNIVERSAL ENGINE ---
class BulletproofAI:
    def __init__(self, provider: AIProvider):
        """Initializes the Universal Engine with ANY provider."""
        self.provider = provider

    def execute_with_retry(self, prompt: str, max_retries: int = 3, base_delay: int = 2) -> str:
        """Universal Exponential Backoff Engine."""
        for attempt in range(max_retries):
            try:
                logging.info(f"Attempt {attempt + 1}/{max_retries} - Generating content...")
                # We call generate() without knowing if it's Gemini, OpenAI, or Sarvam
                text = self.provider.generate(prompt)
                logging.info("SUCCESS: Payload received.")
                return text
                
            except Exception as e:
                # Get status code if it exists (handles different SDK error structures)
                status_code = getattr(e, 'code', getattr(e, 'status_code', 500))
                
                if status_code in [400, 401, 403, 404]:
                    logging.error(f"CRITICAL CONFIG ERROR ({status_code}). Crashing immediately.")
                    raise e
                
                if attempt == max_retries - 1:
                    logging.error(f"CRITICAL: Server did not recover after {max_retries} attempts.")
                    raise e
                    
                sleep_time = base_delay * (2 ** attempt)
                logging.warning(f"SERVER BUSY ({status_code}). Exponential Backoff triggered. Waiting {sleep_time} seconds...")
                time.sleep(sleep_time)

    def force_json(self, prompt: str) -> dict:
        """Universal JSON Enforcer."""
        system_instruction = "CRITICAL: You must respond ONLY with raw, valid JSON. Do not use markdown blocks like ```json."
        full_prompt = f"{system_instruction}\n\n{prompt}"
        
        raw_text = self.execute_with_retry(full_prompt)
        
        try:
            cleaned_text = raw_text.replace("```json", "").replace("```", "").strip()
            parsed_data = json.loads(cleaned_text)
            logging.info("SUCCESS: JSON parsed perfectly.")
            return parsed_data
            
        except json.JSONDecodeError:
            logging.error("FATAL: AI returned invalid JSON structure.")
            return {"error": "Invalid JSON", "raw_output": raw_text}
