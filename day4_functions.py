# --- DAY 4: FUNCTIONS (REUSABLE COMPONENTS) ---
# 1. Defining the Function
# 'current' and 'multiplier' are called arguments (inputs)
def calculate_hike(current_salary, multiplier):
    new_salary = current_salary * multiplier
    return new_salary

# 2. Using the Function (Calling it)
shreya_current = 3.0
shreya_new = calculate_hike(shreya_current, 2.5)

print(f"Current Salary: {shreya_current} LPA")
print(f"Projected AI Engineer Salary: {shreya_new} LPA")

# 3. Another Function for AI Checks
def is_ai_ready(skill_list):
    if len(skill_list) >= 5:
        return "🔥 Ready to apply for Junior AI roles!"
    else:
        return f"📚 Need {5 - len(skill_list)} more skills to be job-ready."

# 4. Testing the second function
my_skills = ["Python", "Webflow", "Git", "API"]
print(f"Status Check: {is_ai_ready(my_skills)}")