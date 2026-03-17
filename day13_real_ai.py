import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Setup
load_dotenv()
token = os.getenv("HF_TOKEN")

# The Client handles the heavy lifting
client = InferenceClient(api_key=token)

print("--- 🚀 Connecting via Llama-3 (2026 Stable)... ---")

try:
    # 2. Swapping the model to Llama-3-8B-Instruct
    # This model has the highest availability in 2026
    response = client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": "Give me a one-sentence tip for a Webflow developer learning Python."}],
        max_tokens=100
    )

    # 3. Accessing the result
    answer = response.choices[0].message.content
    print(f"\nAI Response: {answer}")

except Exception as e:
    print(f"❌ Connection failed: {e}")