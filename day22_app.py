import streamlit as st
import pandas as pd
import os
import time
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. SETUP & AI BRAIN
load_dotenv()
client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

def get_ai_tagline(product, vibe):
    # System Instruction based on Sidebar selection
    prompt = f"Role: {vibe} Copywriter. Task: 5-word tagline for {product}. No quotes."
    try:
        response = client.chat_completion(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "AI is resting... try again!"

# 2. UI LAYOUT
st.set_page_config(page_title="Webflow AI", page_icon="🤖")
st.title("🤖 Webflow AI Content Manager")

with st.sidebar:
    st.header("Settings")
    brand_vibe = st.selectbox("Select Brand Voice", ["Luxury", "Gen-Z", "Professional"])
    st.success("AI Connected")

uploaded_file = st.file_uploader("Upload your Webflow Export (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 📊 Preview Data")
    st.dataframe(df.head())

    # 3. THE MAGIC BUTTON
    if st.button("✨ Generate AI Content"):
        with st.status("AI is working on your products...", expanded=True) as status:
            st.write("Connecting to Qwen-72B...")
            
            # We apply the AI to every row
            df['AI_Tagline'] = df['Item_Name'].apply(lambda x: get_ai_tagline(x, brand_vibe))
            
            status.update(label="✅ Content Generated!", state="complete", expanded=False)

        # 4. SHOW RESULTS & DOWNLOAD
        st.write("### 🏆 AI Optimized Results")
        st.dataframe(df)

        # Download button so the user can take the data back to Webflow
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📂 Download for Webflow", csv, "ai_webflow_export.csv", "text/csv")

        # 5. DATA VISUALIZATION (Day 24 addition)
        st.divider()
        st.write("### 📈 Inventory Insights")
        
        # Create two columns for charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("#### Stock Levels")
            # A simple bar chart: Item Name vs Inventory
            st.bar_chart(data=df, x="Item_Name", y="Inventory", color="#4285F4")

        with col2:
            st.write("#### Price Distribution")
            # A line chart for pricing
            st.line_chart(data=df, x="Item_Name", y="Price", color="#EA4335")

        st.success("Analysis Complete! You are ready to export.")