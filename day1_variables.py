# --- VARIABLES & DATA TYPES ---

# 1. String (Text)
name = "Shreya"
current_job = "Webflow Developer"
target_job = "AI Engineer"

# 2. Integer (Whole Numbers)
years_experience = 3
daily_coding_minutes = 60

# 3. Float (Decimals)
current_age = 22.0
time_to_learn = 0.5

# 4. Boolean (True/False)
is_learning_python = True

# --- USING THE DATA ---

# We use 'f-strings' to mix text and variables easily
print(f"Hi, I'm {name}. I am a {current_job} transitioning to {target_job}.")

# Doing some simple math
age_deadline = current_age + time_to_learn
print(f"I learn AI skill at the age of {age_deadline}.")

# Checking a condition
if is_learning_python:
    print("Status: 🟢 Gaining new skills!")