import os
import time
import pandas as pd
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. SETUP
load_dotenv()
client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

def clean_and_optimize():
    print("--- 📂 Loading Raw Data... ---")
    # Load the messy data we created on Day 17
    if not os.path.exists("messy_data.csv"):
        print("❌ Error: messy_data.csv not found!")
        return

    df = pd.read_csv("messy_data.csv")

    # 2. DATA CLEANING (Day 17 Skills)
    print("✨ Cleaning data...")
    df['Item_Name'] = df['Item_Name'].str.strip()
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
    df['Inventory'] = pd.to_numeric(df['Inventory'], errors='coerce').fillna(0)

    # 3. AI SEO GENERATION (Day 19 & 20 Skills)
    print("🤖 Generating SEO Descriptions (Slow & Steady)...")
    
    def get_seo_meta(row):
        time.sleep(3) # Safe delay
        product = row['Item_Name']
        cat = row['Category']
        
        # System Prompting (Day 20)
        prompt = f"You are an SEO Expert. Write a 10-word meta description for this {cat} product: {product}"
        
        try:
            response = client.chat_completion(
                model="Qwen/Qwen2.5-72B-Instruct",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=30
            )
            return response.choices[0].message.content.strip()
        except:
            return "Premium quality product for your collection."

    df['SEO_Description'] = df.apply(get_seo_meta, axis=1)

    # 4. FINAL EXPORT
    df.to_csv("FINAL_WEBFLOW_UPLOAD.csv", index=False)
    print("\n--- 🏆 PROJECT COMPLETE ---")
    print(df[['Item_Name', 'Price', 'SEO_Description']])
    print("\n📂 File saved as: FINAL_WEBFLOW_UPLOAD.csv")

if __name__ == "__main__":
    clean_and_optimize()