import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Setup
load_dotenv()
token = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=token)

# 2. Read the "Knowledge Base" (Day 8 skill)
with open("knowledge_base.txt", "r") as file:
    product_info = file.read()

print("--- 🪄 Generating Webflow SEO Tags for your Product... ---")

try:
    # 3. Requesting SEO Tags from Llama-3
    prompt = f"Write a professional Webflow Meta Title and Meta Description for this product: {product_info}. Format it as a JSON object."
    
    response = client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    # 4. Show the result
    print("\n--- AI SUGGESTED SEO ---")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"❌ Error: {e}")