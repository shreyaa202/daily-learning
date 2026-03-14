# --- DAY 2: CONDITIONALS & LOGIC ---

# 1. Setup some status variables
coding_hours_today = 2
knows_python_basics = True
has_pushed_to_github = True

# 2. The Decision Tree
print("--- AI Career Advisor ---")

if coding_hours_today == 0:
    print("Action: Try to spend at least 15 minutes coding today to keep the streak!")

elif coding_hours_today > 0 and not knows_python_basics:
    print("Action: Keep focusing on Day 1 variables and data types.")

elif knows_python_basics and not has_pushed_to_github:
    print("Action: Your code is ready, but your GitHub is empty. Push your work!")

elif knows_python_basics and has_pushed_to_github:
    print("Action: Awesome! You are ready for Day 3 (Lists and Loops).")

else:
    print("Action: Keep exploring and stay curious!")

# 3. Simple Comparison
current_salary = 3  # LPA
target_salary = 8   # LPA

if target_salary >= current_salary * 2:
    print("Note: This is a big jump! Focus on high-value AI skills like RAG.")