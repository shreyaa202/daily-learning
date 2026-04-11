import os
import pandas as pd
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. SETUP
load_dotenv()
client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

def generate_branded_tagline(product, vibe):
    # This is the "System" instruction that changes the AI's personality
    if vibe == "Luxury":
        system_instruction = "You are a high-end fashion editor. Use elegant, sophisticated language."
    elif vibe == "Gen-Z":
        system_instruction = "You are a trendy social media influencer. Use slang, emojis, and high energy."
    else:
        system_instruction = "You are a professional business consultant. Be clear and concise."

    # Combining the Personality + the Task
    prompt = f"{system_instruction}\n\nTask: Write a 5-word tagline for {product}."

    try:
        response = client.chat_completion(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=25
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)[:30]}"

# 2. TEST THE VIBES
product = "Cotton Tee"

print(f"--- 👕 Product: {product} ---")
print(f"💎 Luxury Vibe: {generate_branded_tagline(product, 'Luxury')}")
print(f"🔥 Gen-Z Vibe:  {generate_branded_tagline(product, 'Gen-Z')}")
print(f"💼 Business Vibe: {generate_branded_tagline(product, 'Professional')}")