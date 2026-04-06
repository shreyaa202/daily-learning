import os
import time
import pandas as pd
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. SETUP
load_dotenv()
token = os.getenv("HF_TOKEN")
# We use a specific, reliable endpoint
client = InferenceClient(api_key=token)

# 2. DATA
df = pd.read_csv("clean_data.csv")

def get_tagline(product_name):
    # Qwen 2.5 is a "hidden gem" - fast and rarely busy
    model_id = "Qwen/Qwen2.5-72B-Instruct"
    
    prompt = f"Write a 5-word tagline for: {product_name}. Tagline only."
    
    try:
        # No more loop, just one clean call with a 3-second wait
        time.sleep(3) 
        print(f"🤖 HF is processing: {product_name}...")
        
        response = client.chat_completion(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)[:30]}"

# 3. RUN
print("--- 🌩️ Switching to Hugging Face (Qwen Server) ---")
df['AI_Tagline'] = df['Item_Name'].apply(get_tagline)

# 4. SAVE
df.to_csv("webflow_ready_cms.csv", index=False)
print("\n--- ✅ FINISHED! Check your folder ---")
print(df[['Item_Name', 'AI_Tagline']])