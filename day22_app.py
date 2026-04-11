# Webflow AI Content Manager
# A Streamlit app that connects to Hugging Face's Qwen-72B model to generate AI-optimized taglines for products in a Webflow export CSV. Users can select a brand vibe, upload their CSV, and get AI-generated content with insights.   
# for day 22 to day 25
import streamlit as st
import pandas as pd
import os
import time
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. SETUP
load_dotenv()
client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

# 2. THE SECURITY LOCK
def check_password():
    """Returns True if the user had the correct password."""
    if "password_correct" not in st.session_state:
        # First run, show the input
        st.sidebar.text_input(
            "Enter Admin Access Key", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, retry
        st.sidebar.text_input(
            "Enter Admin Access Key", type="password", on_change=password_entered, key="password"
        )
        st.sidebar.error("❌ Invalid Key")
        return False
    else:
        return True

def password_entered():
    """Checks whether a password entered by the user is correct."""
    if st.session_state["password"] == "noida_ai_2026": # Your Secret Key!
        st.session_state["password_correct"] = True
        del st.session_state["password"]  # don't store password
    else:
        st.session_state["password_correct"] = False

# 3. APP LOGIC
st.set_page_config(page_title="Secure AI Manager", page_icon="🔐")

if check_password():
    # EVERYTHING INSIDE HERE IS SECURE
    st.sidebar.success("🔓 Access Granted")
    st.title("🤖 Webflow AI Content Manager")
    
    # ... (Your previous file_uploader and AI logic goes here)
    st.write("Welcome back, Shreya. The AI is ready for your CSV.")
    
    # (Rest of your Day 24 code...)
else:
    # THIS SHOWS IF THE KEY IS WRONG
    st.title("🔐 Access Restricted")
    st.info("Please enter the Admin Key in the sidebar to use the AI Pipeline.")