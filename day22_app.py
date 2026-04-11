# Webflow AI Content Manager
# A Streamlit app that connects to Hugging Face's Qwen-72B model to generate AI-optimized taglines for products in a Webflow export CSV. Users can select a brand vibe, upload their CSV, and get AI-generated content with insights.   
# for day 22 to day 25
import streamlit as st
import pandas as pd
import os
import time
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# --- 1. SETUP & AI BRAIN ---
load_dotenv()
client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

def get_ai_tagline(product, vibe):
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

# --- 2. SECURITY LOGIC ---
def password_entered():
    if st.session_state["password"] == "noida_ai_2026":
        st.session_state["password_correct"] = True
        del st.session_state["password"] 
    else:
        st.session_state["password_correct"] = False

def check_password():
    if "password_correct" not in st.session_state:
        st.sidebar.text_input("Enter Admin Access Key", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.sidebar.text_input("Enter Admin Access Key", type="password", on_change=password_entered, key="password")
        st.sidebar.error("❌ Invalid Key")
        return False
    return True

# --- 3. THE APP INTERFACE ---
st.set_page_config(page_title="Secure Webflow AI", page_icon="🔐")

if check_password():
    # EVERYTHING BELOW ONLY SHOWS AFTER LOGIN
    st.sidebar.success("🔓 Access Granted")
    st.title("🤖 Webflow AI Content Manager")
    
    with st.sidebar:
        st.header("Settings")
        brand_vibe = st.selectbox("Select Brand Voice", ["Luxury", "Gen-Z", "Professional"])

    uploaded_file = st.file_uploader("Upload your Webflow Export (CSV)", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### 📊 Preview Data")
        st.dataframe(df.head())

        if st.button("✨ Generate AI Content"):
            with st.status("AI is working...", expanded=True) as status:
                df['AI_Tagline'] = df['Item_Name'].apply(lambda x: get_ai_tagline(x, brand_vibe))
                status.update(label="✅ Content Generated!", state="complete", expanded=False)

            st.write("### 🏆 AI Optimized Results")
            st.dataframe(df)

            # Download Button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📂 Download for Webflow", csv, "ai_export.csv", "text/csv")

            # --- DATA VISUALIZATION SECTION ---
            st.divider()
            st.write("### 📈 Inventory Insights")
            col1, col2 = st.columns(2)
            with col1:
                st.bar_chart(data=df, x="Item_Name", y="Inventory")
            with col2:
                st.line_chart(data=df, x="Item_Name", y="Price")

else:
    st.title("🔐 Access Restricted")
    st.info("Please enter the Admin Key in the sidebar to unlock the AI Pipeline.")