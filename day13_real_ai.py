import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Setup
load_dotenv()
token = os.getenv("HF_TOKEN")

# The Client automatically handles the URL and routing for you
client = InferenceClient(api_key=token)

print("--- 🚀 Connecting via Official HF Client... ---")

try:
    # 2. Make the call using the 'chat_completion' method
    # This is the 2026 standard for talking to text models
    response = client.chat_completion(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[{"role": "user", "content": "Give me a one-sentence tip for a Webflow developer."}],
        max_tokens=100
    )

    # 3. Access the result (Professional JSON parsing)
    answer = response.choices[0].message.content
    print(f"\nAI Response: {answer}")

except Exception as e:
    print(f"❌ Connection failed: {e}")