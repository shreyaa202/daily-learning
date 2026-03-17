import os
import requests
from dotenv import load_dotenv

# This looks for the file named .env
load_dotenv()
token = os.getenv("HF_TOKEN")

# Ensure the header is using the variable, NOT the hardcoded string
HEADERS = {"Authorization": f"Bearer {token}"}
token = os.getenv("HF_TOKEN")

# THE NEW ROUTER URL
API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"
HEADERS = {"Authorization": f"Bearer {token}"}

def query_ai(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

print("--- 🚀 Connecting to New AI Router... ---")
output = query_ai("Give me a one-sentence tip for a Webflow developer.")

if isinstance(output, list):
    print(f"AI Response: {output[0]['generated_text']}")
else:
    print(f"Response: {output}")