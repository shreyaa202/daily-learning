# Webflow AI Content Manager
# A Streamlit app that connects to Hugging Face's Qwen-72B model to generate AI-optimized taglines for products in a Webflow export CSV. Users can select a brand vibe, upload their CSV, and get AI-generated content with insights.   
# for day 22 to day 30 of the 30-day AI challenge.
# st.balloons() # This adds a celebratory animation on the screen

import streamlit as st
import pandas as pd
import os
import time
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# --- 1. SETUP & AI ENGINE ---
load_dotenv()
token = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=token)

def get_ai_seo_content(item_name, category, mode):
    """Advanced AI Generator for SEO Metadata."""
    if mode == "Tagline":
        prompt = f"Role: Marketing Expert. Task: Write a 5-word catchy tagline for a {category} called '{item_name}'. No quotes."
    else:
        prompt = f"Role: SEO Specialist. Task: Write a 150-character meta description for a {category} product: '{item_name}'. Focus on high-conversion keywords."
    
    try:
        response = client.chat_completion(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=40
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "Content pending... system busy."

# --- 2. SECURITY LAYER ---
def check_password():
    def password_entered():
        if st.session_state["password"] == "noida_ai_2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.sidebar.text_input("Admin Access Key", type="password", on_change=password_entered, key="password")
        return False
    return st.session_state["password_correct"]

# --- 3. THE PROFESSIONAL DASHBOARD ---
st.set_page_config(page_title="AI-SEO Automation Pro", page_icon="📈", layout="wide")

if check_password():
    st.sidebar.success("🔓 Authorized Session")
    with st.sidebar:
        st.header("⚙️ Control Panel")
        brand_vibe = st.selectbox("Brand Voice", ["Luxury", "Gen-Z", "Professional", "Minimalist"])
        output_type = st.radio("Output Type", ["Tagline", "SEO Meta Description"])
        st.divider()
        st.info("Developed by Shreya Tripathi | Webflow AI Engineer")

    st.title("🚀 Professional AI-SEO Optimizer")
    st.markdown("#### Automating Webflow CMS workflows with Large Language Models")

    uploaded_file = st.file_uploader("Upload Webflow Export (CSV)", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # VALIDATION
        if not all(col in df.columns for col in ['Item_Name', 'Category']):
            st.error("❌ Missing required columns: 'Item_Name' and 'Category'")
            st.stop()

        # --- RESUME FEATURE: BUSINESS METRICS ---
        st.divider()
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric("Total Items", len(df))
        with m_col2:
            hours_saved = round((len(df) * 5) / 60, 1) # Assuming 5 mins/item manual work
            st.metric("Manual Hours Saved", f"{hours_saved} hrs")
        with m_col3:
            # Assuming a content writer charges $30/hr
            savings = round(hours_saved * 30, 2)
            st.metric("Estimated Agency Savings", f"${savings}")
        st.divider()

        st.write("### 📂 Data Preview")
        st.dataframe(df.head(), use_container_width=True)

        if st.button("⚡ Start Bulk Optimization"):
            with st.status("AI Engine warming up...", expanded=True) as status:
                st.write("Connecting to Qwen-72B Inference Node...")
                
                # Processing with a progress bar
                results = []
                progress_bar = st.progress(0)
                for i, row in df.iterrows():
                    res = get_ai_seo_content(row['Item_Name'], row['Category'], output_type)
                    results.append(res)
                    progress_bar.progress((i + 1) / len(df))
                    time.sleep(0.5) # Safety delay
                
                df['AI_Optimized_Content'] = results
                status.update(label="✅ Optimization Complete!", state="complete")
            
            st.balloons()
            st.write("### 🏆 Final Results")
            st.dataframe(df, use_container_width=True)

            # PROFESSIONAL EXPORT
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Webflow-Ready CSV", csv, "seo_optimized_export.csv", "text/csv")

            # VISUAL ANALYTICS
            st.divider()
            st.write("### 📊 Dataset Distribution")
            c1, c2 = st.columns(2)
            with c1:
                st.write("#### Category Breakdown")
                st.bar_chart(df['Category'].value_counts())
            with c2:
                st.write("#### Inventory Priority")
                st.line_chart(df.set_index('Item_Name')['Inventory'])

else:
    st.title("🔐 Enterprise Portal Locked")
    st.info("Please enter the Admin Key to access the Bulk SEO Automation Pipeline.")