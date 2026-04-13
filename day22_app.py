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

# --- 1. SETUP & AI BRAIN ---
load_dotenv()
# Note: In Streamlit Cloud, it will look in "Secrets". Locally, it looks in ".env"
token = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=token)

def get_ai_tagline(product, vibe):
    """The AI engine that powers your brand voices."""
    prompt = f"Role: {vibe} Copywriter. Task: Write a 5-word catchy tagline for {product}. No quotes, just the text."
    try:
        # Using Qwen 2.5 for maximum reliability in 2026
        response = client.chat_completion(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "AI Server busy. Please retry."

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
st.set_page_config(page_title="Webflow AI CMS Pro", page_icon="🚀", layout="wide")

if check_password():
    # SIDEBAR SETUP
    st.sidebar.success("🔓 Access Granted")
    with st.sidebar:
        st.header("Settings")
        brand_vibe = st.selectbox("Select Brand Voice", ["Luxury", "Gen-Z", "Professional", "Minimalist"])
        st.divider()
        st.markdown("### 👩‍💻 Developed by Shreya")
        st.info("AI Automation Expert for Webflow")
        st.write("[LinkedIn](https://linkedin.com/in/shreya) | [GitHub](https://github.com/shreyaa202)")

    # MAIN HEADER
    st.title("🤖 Webflow AI Content Manager")
    
    with st.expander("📖 User Guide"):
        st.write("""
        1. **Upload:** Drop your Webflow CSV export here.
        2. **Validate:** The app ensures 'Item_Name' and 'Category' exist.
        3. **Generate:** AI creates unique taglines for every row.
        4. **Export:** Download and import back into Webflow.
        """)

    uploaded_file = st.file_uploader("Step 1: Upload your Webflow Export (CSV)", type="csv")

    if uploaded_file:
        # DATA LOADING
        df = pd.read_csv(uploaded_file)
        
        # VALIDATION (Day 28 Fix)
        required_columns = ['Item_Name', 'Category']
        if not all(col in df.columns for col in required_columns):
            st.error(f"❌ Missing Columns! Your CSV must have: {', '.join(required_columns)}")
            st.stop()

        st.write("### 📊 Raw Data Preview")
        st.dataframe(df.head())

        # PROCESSING BUTTON
        if st.button("✨ Step 2: Generate AI Content"):
            with st.status("AI is processing your products...", expanded=True) as status:
                # Apply AI with a tiny delay to respect rate limits
                def process_row(name):
                    time.sleep(1) # Safety pause
                    return get_ai_tagline(name, brand_vibe)
                
                df['AI_Tagline'] = df['Item_Name'].apply(process_row)
                status.update(label="✅ Content Generated Successfully!", state="complete", expanded=False)
            
            st.balloons() # Day 27 Celebration

            # DISPLAY RESULTS
            st.write("### 🏆 AI Optimized Results")
            st.dataframe(df)

            # DOWNLOAD SECTION
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Step 3: Download for Webflow",
                data=csv,
                file_name="webflow_ready_export.csv",
                mime="text/csv",
            )

            # ANALYTICS SECTION (Day 24)
            st.divider()
            st.write("### 📈 Inventory & Price Insights")
            col1, col2 = st.columns(2)
            with col1:
                st.write("#### Stock by Product")
                st.bar_chart(data=df, x="Item_Name", y="Inventory")
            with col2:
                st.write("#### Price Distribution")
                st.line_chart(data=df, x="Item_Name", y="Price")

else:
    # LANDING PAGE (LOCKED)
    st.title("🔐 AI Manager Locked")
    st.info("Please enter your Admin Access Key in the sidebar to begin processing data.")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80", caption="Security Active")