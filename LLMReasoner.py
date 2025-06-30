import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LLMReasoner:
    def __init__(self):
        #self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_url = "http://localhost:1234/v1/chat/completions"

        if not self.api_key:
            raise ValueError("OpenAI API key is not configured")

    def get_chat_response(self, prompt):
        #print("Using API Key:", self.api_key)
        
        headers = {
            #"Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            #"model": "o1-mini",  # Specify GPT-4 or any other model
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            message = result["choices"][0]["message"]["content"]
            print("GPT-4 Response received:", message)
            return message
        except requests.exceptions.RequestException as error:
            print("Error calling GPT-4 API:", error)
            raise

# Example usage
if __name__ == "__main__":
    ai_client = LLMReasoner()
    response = ai_client.get_chat_response("Hello, how are you?")
    print("AI Response:", response)
