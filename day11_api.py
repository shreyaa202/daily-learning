# --- DAY 11: TALKING TO THE INTERNET (APIs) ---
import requests

# 1. The URL of the API (This one gives a random advice)
api_url = "https://api.adviceslip.com/advice"

try:
    # 2. Making the 'GET' request (Like visiting a website in code)
    response = requests.get(api_url)
    
    # 3. Checking if the connection was successful (Status Code 200)
    if response.status_code == 200:
        # Convert the raw text into a Python Dictionary
        data = response.json()
        
        # Access the specific 'advice' inside the dictionary
        advice = data['slip']['advice']
        
        print("--- 🤖 AI-Like Advice Received ---")
        print(f"Advice: {advice}")
    else:
        print(f"❌ Failed to connect. Status: {response.status_code}")

except Exception as e:
    print(f"❌ An error occurred: {e}")