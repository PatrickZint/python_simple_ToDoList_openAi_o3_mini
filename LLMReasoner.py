import os
import requests
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LLMReasoner:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/chat/completions"

        if not self.api_key:
            raise ValueError("OpenAI API key is not configured")

    def get_chat_response(self, prompt):
        print("Using API Key:", self.api_key)
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "o3-mini",  # Specify GPT-4 or any other model
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            message = result["choices"][0]["message"]["content"]
            print("LM Studio Response received:", message)
            return message
        except requests.exceptions.RequestException as error:
            print("Error calling LM Studio API:", error)
            raise

# Example usage
if __name__ == "__main__":
    ai_client = LLMReasoner()
    response = ai_client.get_chat_response("Hello, how are you?")
    print("AI Response:", response)
